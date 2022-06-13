from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, LogInForm, FamilyForm, AddToFamilyForm, CategoryForm, ActivityForm, \
    PlanForm, EventForm, JoinEventForm
from .models import UserInf, Family, Categories, Activities, Plans, Events, UserEvent


class WelcomeView(View):
    """
    View to welcome user. It does not have any other special option.
    """
    def get(self, request):
        messages = [
            'Welcome in Self-Made Organizer APP!',
            'You can use that application to create plans or plan events for family.',

            'For enter some part of application, you have to be logged.',
            'Please, sign up and start using that application!',

            'Have a nice day!']
        return render(request, "welcome.html", {"messages": messages})


class CreateUserView(View):
    """
    View prepared to create User and related object UserInf. Extra info about user exist for join user to family.
    """
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
            users = User.objects.all()
            existing = False
            for us in users:
                if us.username == username:
                    existing = True
            if existing:
                return HttpResponse('User with that username is just existing.')
            else:
                if password == password2:
                    user = User.objects.create_user(username, email, password)
                    UserInf.objects.create(user_id=user, color=color, initial=initial)
                    return HttpResponse(f'User {username} has been created.')
                return HttpResponse("Passwords are not the same.")
        return render(request, "create_user.html", {"form": form})


class LogInView(View):
    """
    View created for log in user. This view authenticating and, after that login user.
    """
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
                return HttpResponse('Incorrect login or password.')
        return render(request, "login.html", {'form': form})


class LogOutView(LoginRequiredMixin, View):
    """
    View created to log out user.
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class CreateFamilyView(LoginRequiredMixin, View):
    """
    View prepared to create object Family. Object is related with UserInf in relation One to Many. View creating
    individual family code, using when user want to become a member of family.
    """
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
                return HttpResponse(f'Family {family_name} has been created. Code of this family is {family_code}.')
            return HttpResponse('Family with that name is just existed.')
        return render(request, "create_family.html", {"form": form})


class AddToFamilyView(LoginRequiredMixin, View):
    """
    View prepared for users who want to join to family. Using individual family code, view gets user id and update
    UserInf.family field with Family object.
    """
    def get(self, request):
        form = AddToFamilyForm()
        return render(request, "add_to_family.html", {"form": form})

    def post(self, request):
        form = AddToFamilyForm(request.POST)
        if form.is_valid():
            family = Family.objects.get(family_code=form.cleaned_data['family_code'])
            user = request.user
            userinf = UserInf.objects.get(user_id=user.id)
            if not userinf.family:
                userinf.family = family
                userinf.save()
                return HttpResponse(f'You have been added to family {family.family_name}.')
            return HttpResponse(f'You have been already joined to family {userinf.family.family_name}.')
        return render(request, "add_to_family.html", {"form": form})


class AddCategoryView(LoginRequiredMixin, View):
    """
    View prepared to create a category of activities. Main function is archiving activities with the same information.
    """
    def get(self, request):
        form = CategoryForm()
        return render(request, "create_category.html", {"form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            description = form.cleaned_data['description']
            categories = Categories.objects.filter(category_name=category_name)
            if not categories:
                Categories.objects.create(category_name=category_name, description=description)
                return HttpResponse(f'You have been created category {category_name}.')
            return HttpResponse('Category with that name is just existed.')
        return render(request, "create_category.html", {"form": form})


class AddActivityView(LoginRequiredMixin, View):
    """
    View prepared to create activities, which user can later use to create individual plans.
    """
    def get(self, request):
        form = ActivityForm()
        return render(request, "create_activity.html", {"form": form})

    def post(self, request):
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity_name = form.cleaned_data['activity_name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            activities = Activities.objects.filter(activity_name=activity_name)
            if not activities:
                Activities.objects.create(activity_name=activity_name, category=category, description=description)
                return HttpResponse(f'You have been created activity {activity_name}.')
            return HttpResponse('Activity with that name is just existed.')
        return render(request, "create_activity.html", {"form": form})


class AddPlanView(LoginRequiredMixin, View):
    """
    View prepared for users who want to create plans. Creates object Plans, connected with UserInf object,
    Family object and Activities object.
    """
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
            extra_info = form.cleaned_data['extra_info']
            color = userinf.color
            initial = userinf.initial
            plans = Plans.objects.filter(user=user)
            planned = False
            for plan in plans:
                if plan.day == day and ((plan.start >= start and plan.finish <= finish)
                                        or (plan.start <= start and plan.finish >= finish)):
                    planned = True
            if planned:
                return HttpResponse('You have planned something else on that time.')
            else:
                Plans.objects.create(activity=activity, user=user, family=family,
                                     day=day, start=start, finish=finish,
                                     extra_info=extra_info, color=color, initial=initial)
                return HttpResponse('Plan has been added.')
        return render(request, "create_plan.html", {"form": form})


class PlansListView(LoginRequiredMixin, View):
    """
    View created to show plans and events for logged user.
    """
    def get(self, request):
        user = request.user
        userinf = UserInf.objects.get(user_id=user.id)
        family = userinf.family
        plans = Plans.objects.filter(family=family)
        events = UserEvent.objects.filter(user=user)
        return render(request, "plans_list.html", {"plans": plans, "family": family, "user": user,
                                                   "events": events, "userinf": userinf})


class AddEventView(LoginRequiredMixin, View):
    """
    View prepared to create Events - Plans for more than one User. Creating Event is not similar to join to that event!
    """
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
    """
    View created to list events in chosen family. There user can come to view to join chosen event.
    """
    def get(self, request):
        user = request.user
        userinf = UserInf.objects.get(user_id=user.id)
        family = userinf.family
        events = Events.objects.filter(family=family)
        return render(request, "events.html", {"events": events, 'family': family})


class JoinEventView(LoginRequiredMixin, View):
    """
    View prepared to join chosen event by logged user.
    """
    def get(self, request, event_id):
        form = JoinEventForm()
        return render(request, "join_event.html", {"form": form})

    def post(self, request, event_id):
        form = JoinEventForm(request.POST)
        if form.is_valid():
            user = request.user
            event = Events.objects.get(id=event_id)
            extra_info = form.cleaned_data['extra_info']
            userevents = UserEvent.objects.all()
            joined = False
            for userevent in userevents:
                if userevent.user == user and userevent.event == event:
                    joined = True
            if joined:
                return HttpResponse("You have been already joined to that event.")
            else:
                UserEvent.objects.create(user=user, event=event, extra_info=extra_info)
                return HttpResponse("You have joined to event.")
        return render(request, "join_event.html", {"form": form})
