from django.contrib import admin
from django.urls import path

from project_of_organizer.views import CreateUserView, LogInView, LogOutView, CreateFamilyView, FamiliesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_in/', CreateUserView.as_view()),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('create_family/', CreateFamilyView.as_view(), name="create_family"),
    path('families/', FamiliesListView.as_view(), name="families"),
]
