from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, LogInForm, FamilyForm, AddToFamilyForm, CategoryForm, ActivityForm, \
    PlanForm, EventForm, JoinEventForm
from .models import UserInf, Family, Categories, Activities, Plans, Events, UserEvent


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
            else:
                return HttpResponse('Incorrect login or password')
        return render(request, "login.html", {'form': form})


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class CreateFamilyView(LoginRequiredMixin, View):
    def get(self, request):
        form = FamilyForm()
        return render(request, "create_family.html", {"form": form})

    def post(self, request):
        form = FamilyForm(request.POST)
        if form.is_valid():
            family_name = form.cleaned_data['family_name']
            description = form.cleaned_data['description']
            families = Family.objects.filter(family_name=family_name)
            if not families:
                families = len(Family.objects.all())
                if families < 10:
                    family_code = family_name[:7] + str(families)
                elif families < 100:
                    family_code = family_name[:6] + str(families)
                elif families < 1000:
                    family_code = family_name[:5] + str(families)
                elif families < 10000:
                    family_code = family_name[:4] + str(families)
                elif families < 100000:
                    family_code = family_name[:3] + str(families)
                Family.objects.create(family_name=family_name, description=description, family_code=family_code)
                return HttpResponse(f'Family {family_name} has been created.Code of this family is {family_code}')
            return HttpResponse('Family with that name is just existed.')
        return render(request, "create_family.html", {"form": form})


class FamiliesListView(View):
    def get(self, request):
        families = Family.objects.all()
        return render(request, "families_list.html", {"families": families})


class AddToFamilyView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddToFamilyForm()
        return render(request, "add_to_family.html", {"form": form})

    def post(self, request):
        form = AddToFamilyForm(request.POST)
        if form.is_valid():
            family = Family.objects.get(family_code=form.cleaned_data['family_code'])
            user = request.user
            userinf = UserInf.objects.get(user_id=user.id)
            userinf.family = family
            userinf.save()
            return HttpResponse(f'You have been added to family {family.family_name}')
        return render(request, "add_to_family.html", {"form": form})


class AddCategoryView(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, "create_category.html", {"form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            description = form.cleaned_data['description']
            Categories.objects.create(category_name=category_name, description=description)
            return HttpResponse(f'You have been created category {category_name}')
        return render(request, "create_category.html", {"form": form})


class CategoriesListView(View):
    def get(self, request):
        categories = Categories.objects.all()
        return render(request, "categories_list.html", {"categories": categories})


class AddActivityView(LoginRequiredMixin, View):
    def get(self, request):
        form = ActivityForm()
        return render(request, "create_activity.html", {"form": form})

    def post(self, request):
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity_name = form.cleaned_data['activity_name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            Activities.objects.create(activity_name=activity_name, category=category, description=description)
            return HttpResponse(f'You have been created activity {activity_name}')
        return render(request, "create_activity.html", {"form": form})


class ActivitiesListView(View):
    def get(self, request):
        activities = Activities.objects.all()
        return render(request, "activities_list.html", {"activities": activities})


class AddPlanView(LoginRequiredMixin, View):
    def get(self, request):
        form = PlanForm()
        return render(request, "create_plan.html", {"form": form})

    def post(self, request):
        form = PlanForm(request.POST)
        if form.is_valid():
            user = request.user
            activity = form.cleaned_data['activity']
            userinf = UserInf.objects.get(user_id=user.id)
            family = userinf.family
            day = form.cleaned_data['day']
            start = form.cleaned_data['start']
            finish = form.cleaned_data['finish']
            Plans.objects.create(activity=activity, user=user, family=family, day=day, start=start, finish=finish)
            return HttpResponse(f'Plan has been added')
        return render(request, "create_plan.html", {"form": form})


class PlansListView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        userinf = UserInf.objects.get(user_id=user.id)
        family = userinf.family
        plans = Plans.objects.filter(family=family)
        events = UserEvent.objects.filter(user=user)
        return render(request, "plans_list.html", {"plans": plans, "family": family, "user": user, "events": events})


class AddEventView(LoginRequiredMixin, View):
    def get(self, request):
        form = EventForm()
        return render(request, "create_event.html", {"form": form})

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            user = request.user
            userinf = UserInf.objects.get(user_id=user.id)
            family = userinf.family
            activity = form.cleaned_data['activity']
            day = form.cleaned_data['day']
            start = form.cleaned_data['start']
            finish = form.cleaned_data['finish']
            Events.objects.create(activity=activity, family=family, day=day, start=start, finish=finish)
            return HttpResponse(f'Event has been created')
        return render(request, "create_event.html", {"form": form})


class EventListView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        userinf = UserInf.objects.get(user_id=user.id)
        family = userinf.family
        events = Events.objects.filter(family=family)
        return render(request, "events.html", {"events": events, 'family': family})


class JoinEventView(LoginRequiredMixin, View):
    def get(self, request, event_id):
        form = JoinEventForm()
        return render(request, "join_event.html", {"form": form})

    def post(self, request, event_id):
        form = JoinEventForm(request.POST)
        if form.is_valid():
            user = request.user
            event = Events.objects.get(id=event_id)
            extra_info = form.cleaned_data['extra_info']
            UserEvent.objects.create(user=user, event=event, extra_info=extra_info)
            return HttpResponse("You have joined to event.")
        return render(request, "join_event.html", {"form": form})


class WelcomeView(View):
    def get(self, request):
        messages = [
            'Welcome in Self-Made Organizer APP!',
            'You can use that application to create plans or plan events for family.',
            
            'For enter some part of application, you have to be logged.',
            'Please, sign up and start using that application!',
            
            'Have a nice day!']
        return render(request, "welcome.html", {"messages": messages})
