from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=222, blank=True)
    phone = models.CharField(max_length=222, blank=True)
    email = models.EmailField()
    message = models.TextField(blank=True)
    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
