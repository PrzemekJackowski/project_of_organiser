from django.contrib.auth.models import User
from django.db import models


class Family(models.Model):
    family_name = models.CharField(unique=True, max_length=64, default="Family_name")
    description = models.TextField()
    family_code = models.CharField(unique=True, max_length=8)

    @property
    def name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.name


class UserInf(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    families = models.ManyToManyField(Family)
    initial = models.CharField(max_length=1)
    color = models.CharField(max_length=32)


class Categories(models.Model):
    category_name = models.CharField(unique=True, max_length=64, default="Category's name")
    description = models.TextField()

    @property
    def name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.name


class Activities(models.Model):
    activity_name = models.CharField(unique=True, max_length=64, default="Activity's name")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()

    @property
    def name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.name


class Plans(models.Model):
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE)
    user = models.IntegerField()
    day = models.DateTimeField()
    duration = models.TimeField()
