from django import forms

from project_of_organizer.models import Categories, Activities
from .widget import DatePickerInput, TimePickerInput


class FamilyForm(forms.Form):
    family_name = forms.CharField(label="Family's name", max_length=64)
    description = forms.CharField(label="Description")


class UserForm(forms.Form):
    COLORS = (
        ("aqua", "aqua"),
        ("blue", "blue"),
        ("brown", "brown"),
        ("cyan", "cyan"),
        ("crimson", "crimson"),
        ("darkgreen", "darkgreen"),
        ("deeppink", "deeppink"),
        ("forestgreen", "forestgreen"),
        ("fuchsia", "fuchsia"),
        ("gold", "gold"),
        ("green", "green"),
        ("indigo", "indigo"),
        ("lavender", "lavender"),
        ("lightcoral", "lightcoral"),
        ("lime", "lime"),
        ("magenta", "magenta"),
        ("maroon", "maroon"),
        ("olive", "olive"),
        ("orange", "orange"),
        ("purple", "purple"),
        ("red", "red"),
        ("salmon", "salmon"),
        ("silver", "silver"),
        ("violet", "violet"),
        ("yellow", "yellow"),
    )
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Insert password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reinsert password", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")
    color = forms.ChoiceField(choices=COLORS)


class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Insert password", widget=forms.PasswordInput)


class AddToFamilyForm(forms.Form):
    family_code = forms.CharField(label="Family code")


class CategoryForm(forms.Form):
    category_name = forms.CharField(label="Category's name")
    description = forms.CharField(label="Description")


class ActivityForm(forms.Form):
    categories = Categories.objects.all()
    CATEGORIES = []
    for category in categories:
        CATEGORIES.append((category.id, category.category_name))
    activity_name = forms.CharField(label="Activity's name")
    category = forms.ChoiceField(choices=CATEGORIES)
    description = forms.CharField(label="Description")


class PlanForm(forms.Form):
    activities = Activities.objects.all()
    ACTIVITIES = []
    for activity in activities:
        ACTIVITIES.append((activity.id, activity.activity_name))
    activity = forms.ChoiceField(choices=ACTIVITIES)
    day = forms.DateField(label="Start of activity", widget=DatePickerInput)
    start = forms.TimeField(label="Start of activity", widget=TimePickerInput)
    finish = forms.TimeField(label="Finish of activity", widget=TimePickerInput)
    item = forms.CharField(label="Item needed for that", required=False)
    info = forms.CharField(label="Extra info about", required=False)
