from django.contrib.auth import user_logged_in, user_logged_out
from django.db import models
from django.contrib.auth.models import User


class LoggedUser(models.Model):
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username

    def login_user(sender, request, user, **kwargs):
        LoggedUser(user=user).save()

    def logout_user(sender, request, user, **kwargs):
        try:
            u = LoggedUser.objects.get(user=user)
            u.delete()
        except LoggedUser.DoesNotExist:
            pass

    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)