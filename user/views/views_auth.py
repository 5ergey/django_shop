from django.views import generic

class RegistrationView(generic.TemplateView):
    pass

class LoginView(generic.TemplateView):
    pass

class LogoutView(generic.TemplateView):
    pass

class EmailVerifyView(generic.TemplateView):
    pass

class ResendVerificationView(generic.TemplateView):
    pass

class PasswordResetView(generic.TemplateView):
    pass

class PasswordResetConfirmView(generic.TemplateView):
    pass

class PasswordChangeView(generic.TemplateView):
    pass
