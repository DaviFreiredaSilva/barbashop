from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib import messages

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    messages.success(request, 'Usuário autenticado com sucesso.')