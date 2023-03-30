from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

USER_TYPE = (
    ('Customer', 'Customer'),
    ('Agent', 'Agent'),
)

COMP_STATUS = (
    ('Pending', 'Pending'),
    ('Work in Progress', 'Work in Progress'),
    ('Completed', 'Completed'),
)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    address1 = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400)
    city = models.CharField(max_length=20)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='profile_pic')
    user_type = models.CharField(max_length=20, choices=USER_TYPE, default='Customer')

    def save(self, *args, **kwargs):
        self.city = self.city.lower()
        return super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_type


class Complaint(models.Model):
    title = models.CharField(max_length=288)
    description = models.TextField(max_length=1024)
    status = models.CharField(max_length=20, choices=COMP_STATUS, default='Pending')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    solved_by = models.CharField(max_length=128, blank=True, null=True)
    solved_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class ComplaintDocument(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    files = models.FileField(upload_to='complaint_doc')

    def __str__(self):
        return str(self.files)

class Action(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    actions = models.TextField(max_length=1024)

    def __str__(self):
        return self.actions