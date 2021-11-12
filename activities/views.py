from django.db.utils import IntegrityError
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import Facilitator, Instructor
from .serializers import ActivitySerializer, SubmissionSerializer
from .models import Activity, Submission


class Createactivity(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Facilitator]

    def post(self, request):
        try:
            title = request.data['title']
            points = request.data['points']
            activity = Activity.objects.create(title=title, points=points)
            serializer = ActivitySerializer(activity)

            output = {**serializer.data}
            submissions = output.pop('submission_set')
            output['submissions'] = submissions

            return Response(output, status=201)

        except IntegrityError:
            return Response({"error": "activity already exists"}, status=400)
        
    
    def get(self, request):
        user = request.user
        if not user.is_staff:
            return Response({"detail": "You do not have permission to perform this action."})

        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True) 

        output = []

        for i in serializer.data:
            obj_data = {**i}
            submissions = obj_data.pop('submission_set')
            obj_data['submissions'] = submissions
            output.append(obj_data)

        return Response(output, status=200)


class SubmitActivity(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, activity_id):
        try:
            activity = Activity.objects.get(id=activity_id)
            user = request.user
            if user.is_staff or user.is_superuser:
                return Response({"error": "Only students can submit activities"}, status=400)
            repo = request.data["repo"]
            
            submission = Submission.objects.create(user_id=user.id, activity_id=activity.id, repo=repo, grade=None)
            serializer = SubmissionSerializer(submission)

            return Response(serializer.data, status=201)

        except Activity.DoesNotExist:
            return Response({"error": "Activity Not Found"}, status=404)

        except User.DoesNotExist:
            return Response({"error": "User Not Found"}, status=404)

        except KeyError as e:
            return Response({"error": f"is missing {str(e)}"})


class ScoreSubmission(APIView):
    permission_classes = [IsAuthenticated, Facilitator]
    authentication_classes = [TokenAuthentication]

    def put(self, request, submission_id):
        try:
            submission = Submission.objects.get(id=submission_id)
            grade = request.data['grade']

            submission.grade = grade
            submission.save()

            serializer = SubmissionSerializer(submission)

            return Response(serializer.data)

        except Submission.DoesNotExist:
            return Response({"error": "Submission Not Found"}, status=404)   

        except KeyError as e:
            return Response({"error": f"is missing {str(e)}"})


class ActivityById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [Facilitator]

    def put(self, request, activity_id):
        try:
            activity = Activity.objects.get(id=activity_id)
            title = request.data['title']
            points = request.data['points']
            
            if activity.submission_set.first():
                return Response({"error": "You can not change an Activity with submissions"}, status=400)
            
            activity.title = title
            activity.points = points
            activity.save()
            serializer = ActivitySerializer(activity)
            output = {**serializer.data}
            submissions = output.pop('submission_set')
            output['submissions'] = submissions

            return Response(output, status=200)
            
        except KeyError as e:
            return Response({"error": f"is missing {str(e)}"})

        except Activity.DoesNotExist:
            return Response({"error": "Activity Not Found"}, status=404)

        except IntegrityError:
            return Response({"error": "activity already exists"}, status=400)
      


    def get(self, request, activity_id):
        try:
            activity = Activity.objects.get(id=activity_id)
            serializer = ActivitySerializer(activity)

            return Response(serializer.data, status=200)

        except Activity.DoesNotExist:
            return Response({"error": "Activity Not Found"}, status=404)

    def delete(self, request, activity_id):
        try:
            activity = Activity.objects.get(id=activity_id)
            activity.delete()

            return Response('', status=204)

        except Activity.DoesNotExist:
            return Response({"error": "Activity Not Found"}, status=404)


class Submissions(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        
        if not user.is_staff and not user.is_superuser:
            submissions = user.submission_set
            serializer = SubmissionSerializer(submissions, many=True)

            return Response(serializer.data, status=200)

        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(submissions, many=True)

        return Response(serializer.data, status=200)


