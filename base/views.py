from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Chore


# Create your views here.
class PendingChore(ListView):
    model = Chore
    context_object_name = 'pending'


class ChoreDetail(DetailView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/chore.html'

