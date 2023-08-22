from django.db import models
import datetime

# Create your models here.
class Newapp(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    pub_date=models.DateField(default=datetime.date.today)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def isexpensive(self):
        if self.price>50:
            return True
        else:
            return False
        

class student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    grade=models.CharField(max_length=10)
    is_enrolled=models.BooleanField()
    
    def is_passing(self):
        if self.grade<="C":
            return True
        else:
            return False
