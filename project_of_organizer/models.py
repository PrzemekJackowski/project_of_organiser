from django.db import models


class Family(models.Model):
    name = models.CharField(unique=True, max_length=64)
    description = models.TextField()
    family_code = models.CharField(unique=True, max_length=8)

    @property
    def name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.name


class UserInf(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE())
    initial = models.CharField(max_length=1)
    color = models.CharField()


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=64)
    description = models.TextField()

    @property
    def name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.name


class Activities(models.Model):
    name = models.CharField(unique=True, max_length=64)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE())
    description = models.TextField()

    @property
    def name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.name


class Plans(models.Model):
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE())
    user = models.IntegerField()
    day = models.DateTimeField()
    duration = models.TimeField()
