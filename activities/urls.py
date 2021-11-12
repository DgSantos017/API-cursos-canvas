from django.urls import path
from .views import Createactivity, SubmitActivity, ScoreSubmission, ActivityById, Submissions

urlpatterns = [
    path('activities/', Createactivity.as_view()),
    path('activities/<int:activity_id>/submissions/', SubmitActivity.as_view()), 
    path('submissions/<int:submission_id>/', ScoreSubmission.as_view()),
    path('activities/<int:activity_id>/', ActivityById.as_view()),
    path('submissions/', Submissions.as_view())
]
