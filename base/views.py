from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Chore

# Create your views here.
class PendingChore(ListView):
    model = Chore
    context_object_name = 'chores'

class ChoreDetail(DetailView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/chore.html'

class CreateChore(CreateView):
    model = Chore
    template_name = 'base/chore_form.html'
    fields = '__all__'
    success_url = reverse_lazy('chores')

class EditChore(UpdateView):
    model = Chore
    template_name = 'base/chore_form.html'
    fields = '__all__'
    success_url = reverse_lazy('chores')

class DeleteChore(DeleteView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/delete_chore.html'
    success_url = reverse_lazy('chores')

