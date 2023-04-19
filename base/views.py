from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Chore

# Create your views here.
class Login(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('chores')
class PendingChore(LoginRequiredMixin, ListView):
    model = Chore
    context_object_name = 'chores'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['chores'] = context['chores'].filter(assigned_to=self.request.user)
    #     context['chores'] = context['chores'].filter(complete = False).count()
    #     return context
    #


class ChoreDetail(LoginRequiredMixin, DetailView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/chore.html'

class CreateChore(LoginRequiredMixin, CreateView):
    model = Chore
    template_name = 'base/chore_form.html'
    fields = '__all__'
    success_url = reverse_lazy('chores')

class EditChore(LoginRequiredMixin,UpdateView):
    model = Chore
    template_name = 'base/chore_form.html'
    fields = '__all__'
    success_url = reverse_lazy('chores')

class DeleteChore(LoginRequiredMixin, DeleteView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/delete_chore.html'
    success_url = reverse_lazy('chores')

