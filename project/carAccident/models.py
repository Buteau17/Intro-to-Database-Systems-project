# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Caraccident(models.Model):
    year = models.IntegerField(primary_key=True)
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    type = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    amountofdeath = models.IntegerField(db_column='AmountOfdeath')  # Field name made lowercase.
    amountofinjuries = models.IntegerField(db_column='AmountOfInjuries')  # Field name made lowercase.
    sequenceofpartiesinvolved = models.IntegerField(db_column='SequenceOfPartiesInvolved')  # Field name made lowercase.
    vehicletype = models.CharField(db_column='VehicleType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    levelofinjury = models.IntegerField(db_column='LevelOfInjury', blank=True, null=True)  # Field name made lowercase.
    weather = models.IntegerField(db_column='Weather', blank=True, null=True)  # Field name made lowercase.
    speedlimit = models.IntegerField(db_column='SpeedLimit', blank=True, null=True)  # Field name made lowercase.
    typeofroad = models.IntegerField(db_column='TypeOfroad', blank=True, null=True)  # Field name made lowercase.
    locationofaccident = models.IntegerField(db_column='LocationOfAccident', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caraccident'
