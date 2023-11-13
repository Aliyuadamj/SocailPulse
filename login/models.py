from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('id',)


class Login(BaseModel):
    first_name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    new_password = models.CharField(max_length=150)
    date_of_birth = models.DateField(max_length=8)
    genderchoice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Custom", "Custom"),
    )
    gender = models.CharField(choices=genderchoice, max_length=7)
    images = models.ImageField(upload_to="login", blank=True, null=True)

