from django.contrib.auth.models import User
from django.db import models


class Family(models.Model):
    family_name = models.CharField(unique=True, max_length=64, default="Family_name")
    description = models.TextField()
    family_code = models.CharField(unique=True, max_length=8)


class UserInf(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    initial = models.CharField(max_length=1)
    color = models.CharField(max_length=32)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)


class Categories(models.Model):
    category_name = models.CharField(unique=True, max_length=64, default="Category's name")
    description = models.TextField()

    @property
    def name(self):
        return "{}".format(self.category_name)

    def __str__(self):
        return self.name


class Activities(models.Model):
    activity_name = models.CharField(unique=True, max_length=64, default="Activity's name")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()

    @property
    def name(self):
        return "{}".format(self.activity_name)

    def __str__(self):
        return self.name


class Plans(models.Model):
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)
    day = models.DateField()
    start = models.TimeField(default="12:00")
    finish = models.TimeField(default='12:15')
    extra_info = models.TextField(null=True)
    color = models.CharField(max_length=16, null=True)
    initial = models.CharField(max_length=1, null=True)


class Events(models.Model):
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)
    day = models.DateField()
    start = models.TimeField(default="12:00")
    finish = models.TimeField(default='12:15')


class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    extra_info = models.TextField(null=True)
