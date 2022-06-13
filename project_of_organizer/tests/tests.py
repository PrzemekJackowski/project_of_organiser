import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from project_of_organizer.models import UserInf, Family, Categories, Activities, Plans, Events, UserEvent


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        self.family = Family.objects.create(family_name="TestFamily", description="test", family_code="TestFam0")
        self.userinf = UserInf.objects.create(user_id=self.user, initial=self.user.username[0], color="red",
                                              family=self.family)
        self.category = Categories.objects.create(category_name="TestCategory", description="Test")
        self.activity = Activities.objects.create(activity_name="TestActivity", category=self.category,
                                                  description="Test")
        self.plan = Plans.objects.create(activity=self.activity, user=self.user, family=self.userinf.family,
                                         day="2022-07-07", start="12:00", finish="13:00", extra_info="test",
                                         color=self.userinf.color, initial=self.userinf.initial)
        self.event = Events.objects.create(activity=self.activity, family=self.userinf.family, day="2022-08-08",
                                           start="12:00", finish="13:00")
        self.userevent = UserEvent.objects.create(user=self.user, event=self.event, extra_info="test")

    def test_userinf(self):
        user = self.user
        userinf = self.userinf
        family = self.family
        families = Family.objects.all()
        self.assertEqual(userinf.user_id, user)
        self.assertEqual(userinf.family, family)
        self.assertEqual(len(families), (int(family.family_code[7]) + 1))
        self.assertEqual(userinf.initial, user.username[0])

    def test_plan(self):
        user = self.user
        userinf = self.userinf
        family = self.family
        category = self.category
        activity = self.activity
        plan = self.plan
        self.assertEqual(activity.category, category)
        self.assertEqual(plan.user, user)
        self.assertEqual(plan.family, family)
        self.assertEqual(plan.color, userinf.color)

    def test_event(self):
        user = self.user
        family = self.family
        category = self.category
        activity = self.activity
        event = self.event
        userevent = self.userevent
        self.assertEqual(activity.category, category)
        self.assertEqual(userevent.user, user)
        self.assertEqual(event.family, family)
        self.assertEqual(userevent.event, event)
