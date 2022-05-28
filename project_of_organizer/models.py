from django.db import models

COLORS = (
    (1, "aqua"),
    (2, "blue"),
    (3, "brown"),
    (4, "cyan"),
    (5, "crimson"),
    (6, "darkgreen"),
    (7, "deeppink"),
    (8, "forestgreen"),
    (9, "fuchsia"),
    (10, "gold"),
    (11, "green"),
    (12, "indigo"),
    (13, "lavender"),
    (14, "lightcoral"),
    (15, "lime"),
    (16, "magenta"),
    (17, "maroon"),
    (18, "olive"),
    (19, "orange"),
    (20, "purple"),
    (21, "red"),
    (22, "salmon"),
    (23, "silver"),
    (24, "violet"),
    (25, "yellow"),
)


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
    color = models.FloatField(choices=COLORS)


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
