from django.urls import path
from .views import PendingChore, ChoreDetail, CreateChore, EditChore, DeleteChore, Login, UnassignedChore
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PendingChore.as_view(), name='chores'),
    path('unassigned/', UnassignedChore.as_view(), name='unassigned'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('chore/<int:pk>', ChoreDetail.as_view(), name='chore'),
    path('create-chore/', CreateChore.as_view(), name='create-chore'),
    path('edit-chore/<int:pk>', EditChore.as_view(), name='edit-chore'),
    path('delete-chore/<int:pk>', DeleteChore.as_view(), name='delete-chore'),
]
