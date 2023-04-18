from django.urls import path
from .views import PendingChore, ChoreDetail

urlpatterns = [
    path("", PendingChore.as_view(), name="pending"),
    path("chore/<int:pk>", ChoreDetail.as_view(), name="chore")
]