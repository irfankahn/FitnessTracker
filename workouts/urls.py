from django.urls import path
from .views import WorkoutListCreateView, WorkoutDetailView, UserWorkoutListView

urlpatterns = [
    path('', WorkoutListCreateView.as_view(), name='workouts'),  # List and create workouts
    path('user/', UserWorkoutListView.as_view(), name='user-workouts'),  # User-specific workouts
    path('<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),  # Detail view for individual workouts
]
