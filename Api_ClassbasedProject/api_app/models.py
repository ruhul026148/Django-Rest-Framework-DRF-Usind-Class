from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)
    age=models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'