from django.db import models

# Create your models here.


# company model
class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100,
        choices=(
            ("IT", "IT"),
            ("Non IT", "Non IT"),
            ("Mobile Phones", "Mobile Phones"),
        ),
    )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
# Employee Model
