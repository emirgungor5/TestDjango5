from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)


class OrganizationUser(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
