# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Tblfollower(models.Model):

    #__Tblfollower_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    datestring = models.TextField(max_length=255, null=True, blank=True)

    #__Tblfollower_FIELDS__END

    class Meta:
        verbose_name        = _("Tblfollower")
        verbose_name_plural = _("Tblfollower")


class Tblfollowing(models.Model):

    #__Tblfollowing_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    datestring = models.TextField(max_length=255, null=True, blank=True)

    #__Tblfollowing_FIELDS__END

    class Meta:
        verbose_name        = _("Tblfollowing")
        verbose_name_plural = _("Tblfollowing")


class Tblblocked(models.Model):

    #__Tblblocked_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    datestring = models.TextField(max_length=255, null=True, blank=True)

    #__Tblblocked_FIELDS__END

    class Meta:
        verbose_name        = _("Tblblocked")
        verbose_name_plural = _("Tblblocked")


class Tblfriend(models.Model):

    #__Tblfriend_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    datestring = models.TextField(max_length=255, null=True, blank=True)

    #__Tblfriend_FIELDS__END

    class Meta:
        verbose_name        = _("Tblfriend")
        verbose_name_plural = _("Tblfriend")


class Tblcreator(models.Model):

    #__Tblcreator_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Tblcreator_FIELDS__END

    class Meta:
        verbose_name        = _("Tblcreator")
        verbose_name_plural = _("Tblcreator")



#__MODELS__END
