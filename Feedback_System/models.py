from django.db import models

# Create your models here.

class Student(models.Model):
    reg_id = models.CharField(max_length=12,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.IntegerField()
    branch = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name


class Faculty(models.Model):
    fac_id = models.CharField(max_length=5,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name


class Hod(models.Model):
    hod_id = models.CharField(max_length=5,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name


class Subject(models.Model):
    sub_id = models.CharField(max_length=5,primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    year = models.IntegerField()
    sem = models.IntegerField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    form_id = models.CharField(max_length=5,primary_key=True)
    fac_id = models.ForeignKey(Faculty,on_delete=models.PROTECT)
    sub_id = models.ForeignKey(Subject,on_delete=models.PROTECT)
    five = models.IntegerField()
    four = models.IntegerField()
    three = models.IntegerField()
    two = models.IntegerField()
    one = models.IntegerField()
    result = models.FloatField()
