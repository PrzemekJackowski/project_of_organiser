from django.shortcuts import render
from django.views import View
from .forms import UserForm


class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "CreateUser.html", {"form": form})

    def post(self, request, user_id):
        form = UserForm(request.POST)
        if form.is_valid():

