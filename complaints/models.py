# models.py
from django.db import models


class Complaint(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    product_service = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    problem_date = models.DateField()
    location = models.CharField(max_length=200)
    frequency = models.CharField(max_length=50)
    impact = models.CharField(max_length=50)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)
    anonymous = models.BooleanField(default=False)
    contact_email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    userName = models.CharField(max_length=100, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    complaint = models.ForeignKey(Complaint, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=100, blank=True, null=True)  # This should be included
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user or "Anonymous"} on {self.complaint}'
