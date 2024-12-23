from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name="main"),
    path('admission_procedure/', AdmissionProcedure.as_view(), name="admission_procedure"),
    path('ct/', Ct.as_view(), name="ct"),
    path('diagnostics/', Diagnostics.as_view(), name="diagnostics"),
    path('open_day/', OpenDay.as_view(), name="open_day"),
    path('passing_grades/', PassingGrades.as_view(), name="passing_grades"),
    path('profile/', profile, name="profile"),
    path('registration/', RegistrationUser.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('reg_rt/', RegistrationRT.as_view(), name="reg_rt"),
    path('send_declaration/', send_declaration, name="send"),
    path('services/', ServicesHome.as_view(), name="services"),
    path('test/', Test.as_view(), name="test"),
    path('success_page/', success_page, name="success"),
    path('declaration/', declaration, name="declaration"),
    path('password-reset/', PasswordResetView.as_view(template_name="entrants/password_reset_form.html")
         , name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="entrants/password_reset_done.html")
         , name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="entrants/password_reset_confirm.html")
         , name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="entrants/password_reset_complete.html")
         , name='password_reset_complete'),

]
