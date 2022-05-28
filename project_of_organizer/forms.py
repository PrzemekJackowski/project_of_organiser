from django import forms

from project_of_organizer.models import Categories, Activities


categories = Categories.objects.all()
CATEGORIES = []
for category in categories:
    CATEGORIES.append((category.id, category))
activities = Activities.objects.all()
ACTIVITIES = []
for activity in activities:
    ACTIVITIES.append((activity.id, activity))


class FamilyForm(forms.Form):
    name = forms.CharField(label="Family's name", max_length=64)
    description = forms.CharField(labe="Description")


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
    password = forms.PasswordInput()
    email = forms.EmailField(label="E-mail")
    family = forms.CharField(label="Family's code")
    color = forms.ChoiceField(choices=COLORS)


class CategoryForm(forms.Form):
    name = forms.CharField(label="Category's name")
    description = forms.CharField(label="Description")


class ActivityForm(forms.Form):
    name = forms.CharField(label="Activity's name")
    category = forms.ChoiceField(choices=CATEGORIES)
    description = forms.CharField(label="Description")


class PlanForm(forms.Form):
    activity = forms.ChoiceField(choices=ACTIVITIES)
    day = forms.DateTimeField(label="Start of activity")
    duration = forms.TimeField(label="Duration of activity")