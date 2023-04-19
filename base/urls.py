from django.urls import path
from .views import PendingChore, ChoreDetail, CreateChore, EditChore, DeleteChore


urlpatterns = [
    path('', PendingChore.as_view(), name='chores'),
    path('chore/<int:pk>', ChoreDetail.as_view(), name='chore'),
    path('create-chore/', CreateChore.as_view(), name='create-chore'),
    path('edit-chore/<int:pk>', EditChore.as_view(), name='edit-chore'),
    path('delete-chore/<int:pk>', DeleteChore.as_view(), name='delete-chore'),
]
