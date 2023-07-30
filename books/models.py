from django.db import models

class Book(models.Model):
    BookName=models.CharField(max_length=40)
    BookDesc=models.CharField(max_length=500)
    author= models.CharField(max_length=30)

