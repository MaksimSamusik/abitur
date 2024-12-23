from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from .forms import *
from .models import Services


class AdmissionProcedure(TemplateView):
    template_name = 'entrants/admission_procedure.html'
    extra_context = {'title': 'Порядок приёма'}


class Diagnostics(TemplateView):
    template_name = 'entrants/diagnostics.html'
    extra_context = {'title': 'Профориентационная диагностика'}


class Ct(TemplateView):
    template_name = 'entrants/ct.html'
    extra_context = {'title': 'Выдача сертификатов ЦТ'}


class MainPage(TemplateView):
    template_name = 'entrants/main.html'
    extra_context = {'title': 'Личный кабинет абитуриента'}


class OpenDay(TemplateView):
    template_name = 'entrants/open_day.html'
    extra_context = {'title': 'День открытых дверей'}


class PassingGrades(TemplateView):
    template_name = 'entrants/passing_grades.html'
    extra_context = {'title': 'Проходные баллы'}


def profile(request):
    applications = Application.objects.filter(user=request.user).values('overall_rating', 'specialization', 'name')
    return render(request, 'entrants/profile.html', {'applications': applications})


class RegistrationUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'entrants/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'entrants/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegistrationRT(TemplateView):
    template_name = 'entrants/reg_rt.html'
    extra_context = {'title': 'Регистрация на РТ'}


class ServicesHome(ListView):
    model = Services
    template_name = 'entrants/services.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Наши услуги'}

    def get_queryset(self):
        return Services.objects.filter(is_published=True)


class Test(TemplateView):
    template_name = 'entrants/test.html'
    extra_context = {'title': 'Профориентационный тест'}


def success_page(request):
    return render(request, 'entrants/success.html')


def declaration(request):
    applications = Application.objects.filter(user=request.user).values('overall_rating', 'specialization', 'name',
                                                                        'email', 'phone_number', 'passport_series',
                                                                        'passport_number', 'math', 'physics', 'ru_by',
                                                                        'language', 'rating', 'foreign_language')
    return render(request, 'entrants/declaration.html', {'applications': applications})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def send_declaration(request):
    if request.method == 'POST':
        form = ApplicationForm(request.user, request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            request.session['application_submitted'] = True
            return redirect('success')
    else:
        form = ApplicationForm(request.user)
    return render(request, 'entrants/send_declaration.html', {'form': form})
