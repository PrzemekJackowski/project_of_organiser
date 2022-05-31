from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, LogInForm
from .models import UserInf


class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "create_user.html", {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            color = form.cleaned_data['color']
            initial = username[0]
            if password == password2:
                user = User.objects.create_user(username, email, password)
                UserInf.objects.create(user_id=user, color=color, initial=initial)
                return HttpResponse(f'User {username} has been created.')
            return HttpResponse("Passwords are not the same.")
        return render(request, "create_user.html", {"form": form})


class LogInView(View):
    def get(self, request):
        form = LogInForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                next_parameter = request.GET.get('next')
                if next_parameter:
                    return redirect(next_parameter)
                return HttpResponseRedirect('/')
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Incorrect login or password')
        return render(request, "login.html", {'form': form})


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
