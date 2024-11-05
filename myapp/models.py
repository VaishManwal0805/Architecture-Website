from django.db import models

# Create your models here.
class SavedForm(models.Model):
    name=models.CharField(max_length=200,null=False,default='Anonymous')
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name
