# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Avg, Count, Min, Sum, Q


class Caraccident(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
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

def GetLevelofinjurybygender():
    result1 = (Caraccident.objects
        .filter(gender__exact=1)
        .filter(levelofinjury__isnull=False)
        .values('levelofinjury')
        .annotate(count=Count('levelofinjury'))
        .order_by('levelofinjury')
    )
    result2 = (Caraccident.objects
        .filter(gender__exact=2)
        .filter(levelofinjury__isnull=False)
        .values('levelofinjury')
        .annotate(count=Count('levelofinjury'))
        .order_by('levelofinjury')
    )
    data1 = dict()
    data2 = dict()
    for row in result1:
        data1[row['levelofinjury']] = row['count']
    for row in result2:
        data2[row['levelofinjury']] = row['count']
    data = dict()
    data = {
        'male': data1,
        'female': data2
    }
    return data

def AmountAccidentbymonth():
    result = (Caraccident.objects
        .filter(sequenceofpartiesinvolved__exact=1)
        .values('month')
        .annotate(deadcount=Count('sequenceofpartiesinvolved'))
        .order_by('month')
    )
    data = dict()
    for row in result:
        data[row['month']] = row['deadcount']
    return data


def GetDeathByGender():
    result = (Caraccident.objects
        .filter(Q(levelofinjury=1) | Q(levelofinjury=5))
        .values('gender')
        .annotate(deadcount=Count('levelofinjury'))
        .order_by('gender')
    )
    data = dict()
    for row in result:
        if row['gender'] == 1:
            data['male'] = row['deadcount']
        elif row['gender'] == 2:
            data['female'] = row['deadcount']
    return data

def Weather():
    map = {
        1: "heavy rain",
        2: "strong wind",
        3: "wind and sand",
        4: "fog or smoke",
        5: "snowy",
        6: "rainy",
        7: "cloudy",
        8: "sunny"
    }
    result = (Caraccident.objects
        .filter(sequenceofpartiesinvolved__exact=1)
        .filter(weather__isnull=False)
        .values('weather')
        .annotate(count=Count('weather'))
        .order_by('weather')
    )
    data = dict()
    for row in result:
        data[map[row['weather']]] = row['count']
    return data