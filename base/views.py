from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Chore, Son


# Create your views here.
class Login(LoginView):
    model = Chore
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('chores')




class PendingChore(LoginRequiredMixin, ListView):
    model = Chore
    context_object_name = 'chores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            chores = context['chores']
        else:
            chores = context['chores'].filter(assigned_to__user=self.request.user)
        if chores:
            context['unassigned'] = chores.filter(assigned_to__user=None)
            context['chores'] = chores.filter(assigned_to__user=self.request.user)
            context['incomplete_chores_count'] = context['chores'].filter(complete=False).count()
            context['account'] = chores.first().assigned_to.account
        return context


class UnassignedChore(LoginRequiredMixin, ListView):
    model = Chore
    context_object_name = 'unassigned'
    template_name = 'base/unassigned_chores.html'

    def get_queryset(self):
        return super().get_queryset().filter(assigned_to__isnull=True)





class ChoreDetail(LoginRequiredMixin, DetailView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/chore.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chores'] = Chore.objects.all()
        return context


class CreateChore(LoginRequiredMixin, CreateView):
    model = Chore
    template_name = 'base/chore_form.html'
    fields = ['title', 'description', 'value', 'complete', 'assigned_to']
    success_url = reverse_lazy('chores')

    def form_valid(self, form):
        chore = form.save(commit=False)
        son = Son.objects.get(user=self.request.user)
        chore.assigned_to = son
        chore.save()
        return super().form_valid(form)


class EditChore(LoginRequiredMixin, UpdateView):
    model = Chore
    template_name = 'base/chore_form.html'
    fields = ['title', 'description', 'value', 'complete', 'assigned_to']
    success_url = reverse_lazy('chores')

    def form_valid(self, form):
        chore = form.save(commit=False)
        son = Son.objects.get(user=self.request.user)
        chore.assigned_to = son
        if chore.complete:
            chore.add_value(son)
        print(son, chore.assigned_to, "heerr")
        chore.save()
        return super().form_valid(form)


class DeleteChore(LoginRequiredMixin, DeleteView):
    model = Chore
    context_object_name = 'chore'
    template_name = 'base/delete_chore.html'
    success_url = reverse_lazy('chores')

