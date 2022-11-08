from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Models  
class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    seat = models.CharField(max_length=30)
    party = models.CharField(max_length=30)
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # special (dunder) method
    def __str__(self):
        return self.first_name
    
class PollingStation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    county = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # special (dunder) method
    def __str__(self):
        return self.name
    
class Result(models.Model):
    candidate_first_name = models.CharField(max_length=30)
    candidate_middle_name = models.CharField(max_length=30)
    candidate_last_name = models.CharField(max_length=30)
    votes = models.IntegerField()
    polling_station = models.ForeignKey(PollingStation, on_delete=models.PROTECT)
    
    # special (dunder) method
    def __str__(self):
        return self.candidate_first_name
    


