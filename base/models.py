from django.db import models
from django.contrib.auth.models import User


class Son(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True, blank=True,
                             limit_choices_to={'is_superuser': False}
                             )
    age = models.IntegerField(null=True, blank=True)
    account = models.DecimalField(max_digits=8, decimal_places=2,
                                  null=True, blank=True)

    def __str__(self):
        return self.name


class Chore(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=8, decimal_places=2,
                                null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    assigned_to = models.ForeignKey(Son, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='chores')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']



