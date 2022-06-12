import pytest
from django.contrib.auth.models import User
from pythonProject.project_of_organiser.project_of_organizer.models import UserInf, Family, Categories, Activities, \
    Plans, Events, UserEvent


def create_user():
    """
    Function creates a tester user for tests.
    """
    user = User.objects.create_user(username='tester', password='password')
    return user


@pytest.mark.django_db
def test_creating_userinf():
    """
    Testing user form and creating UserInf object.
    """
    user = User.objects.get(id=1)
    userinf = UserInf.objects.create(user_id=user.id, initial=user.username[0], color="red")

    assert len(UserInf.objects.all()) == 1
    assert UserInf.objects.get(user_id=1) == userinf
    assert UserInf.objects.get(initial="t", color="red") == userinf


@pytest.mark.django_db
def test_creating_family():
    """
    Testing Family form and creating Family object.
    """
    family = Family.objects.create(family_name="FamilyTestName", description="test", family_code="FamilyT0")

    assert len(Family.objects.all()) == 1
    assert Family.objects.get(user_id=1) == family
    assert Family.objects.get(family_code="FamilyT0") == family


@pytest.mark.django_db
def test_creating_category():
    """
    Testing Categories form and creating Categories object.
    """
    category = Categories.objects.create(category_name="CategoryTestName", description="test")

    assert len(Categories.objects.all()) == 1
    assert Categories.objects.get(id=1) == category
    assert Categories.objects.get(category_name="CategoryTestName") == category


@pytest.mark.django_db
def test_creating_activity():
    """
    Testing Activities form and creating Activities object.
    """
    category = Categories.objects.get(id=1)
    activity = Activities.objects.create(activity_name="ActivityTestName", category=category, description="test")

    assert len(Activities.objects.all()) == 1
    assert Activities.objects.get(id=1) == activity
    assert Activities.objects.get(category=category) == activity


@pytest.mark.django_db
def test_creating_plan():
    """
    Testing Plans form and creating Plans object.
    """
    user = User.objects.get(id=1)
    family = Family.objects.get(id=1)
    userinf = UserInf.objects.get(id=1)
    activity = Activities.objects.get(id=1)
    plan = Plans.objects.create(activity=activity, user=user, family=family, date="07.07.2022", start="12.00",
                                finish="13.00", extra_info="test", color=userinf.color, initial=userinf.initial)

    assert len(Plans.objects.all()) == 1
    assert Plans.objects.get(user=user) == plan
    assert Plans.objects.get(activity=activity) == plan


@pytest.mark.django_db
def test_creating_event():
    """
    Testing Events form and creating Events object.
    """
    family = Family.objects.get(id=1)
    userinf = UserInf.objects.get(id=1)
    activity = Activities.objects.get(id=1)
    event = Events.objects.create(activity=activity, family=family, date="07.07.2022", start="12.00", finish="13.00")

    assert len(Events.objects.all()) == 1
    assert Events.objects.get(family=family) == event
    assert Events.objects.get(activity=activity) == event


@pytest.mark.django_db
def test_join_event():
    """
    Testing joining events by user form and creating UserEvent object.
    """
    user = User.objects.get(id=1)
    event = Events.objects.get(id=1)
    userevent = UserEvent.objects.create(user=user, event=event, extra_info="test")

    assert len(UserEvent.objects.all()) == 1
    assert UserEvent.objects.get(user=user) == userevent
    assert UserEvent.objects.get(eveny=event) == userevent
