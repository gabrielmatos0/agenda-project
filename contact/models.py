from django.db import models
from django.utils import timezone

# id (primary key)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), piture (imagem)
# owner (foreign key)

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


    def __str__(self):
        return self.first_name + ' | ' + self.phone
