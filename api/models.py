from django.db import models


class APITestModel(models.Model):
    year = models.IntegerField(null=False)
