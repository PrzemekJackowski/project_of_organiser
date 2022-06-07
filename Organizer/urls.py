from django.contrib import admin
from django.urls import path

from project_of_organizer.views import WelcomeView, CreateUserView, LogInView, LogOutView, CreateFamilyView, \
    FamiliesListView, AddToFamilyView, AddCategoryView, CategoriesListView, AddActivityView, ActivitiesListView, \
    AddPlanView, PlansListView, AddEventView, EventListView, JoinEventView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('admin/', admin.site.urls),
    path('sign_in/', CreateUserView.as_view()),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('create_family/', CreateFamilyView.as_view(), name="create_family"),
    path('families/', FamiliesListView.as_view(), name="families"),
    path('join_family/', AddToFamilyView.as_view(), name="join_family"),
    path('create_category/', AddCategoryView.as_view(), name="create_category"),
    path('categories/', CategoriesListView.as_view(), name="categories"),
    path('create_activity/', AddActivityView.as_view(), name="create_activity"),
    path('activities/', ActivitiesListView.as_view(), name="activities"),
    path('create_plan/', AddPlanView.as_view(), name="create_plan"),
    path('plans/', PlansListView.as_view(), name='plans'),
    path('create_event/', AddEventView.as_view(), name='create_event'),
    path('events/', EventListView.as_view(), name='events'),
    path('join_event/<int:event_id>', JoinEventView.as_view(), name='join_event')
]
