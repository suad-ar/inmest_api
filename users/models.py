from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class IMUser (AbstractUser):
    USER_TYPE_CHOICES = [
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin')
    ]
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name}"
    

class Cohort(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohorts')  
    
    def __str__(self):
        return self.name
    
class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohort_members')

    def __str__(self):
        return f"{self.member.user.username} - {self.cohort.name}"