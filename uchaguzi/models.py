from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Models
class PollingStation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    county = models.CharField(max_length=50)
    constituency = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    assigned_user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True,null=True, related_name='polling_station')
    
    # special (dunder) method
    def __str__(self):
        return self.name   
      
class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number = models.IntegerField(blank=True,null=True, unique=True)
    seat = models.CharField(max_length=30)
    party = models.CharField(max_length=30)
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # special (dunder) method
    def __str__(self):
        return self.first_name
    
class POResult(models.Model):
    candidate_first_name = models.CharField(max_length=30)
    candidate_middle_name = models.CharField(max_length=30)
    candidate_last_name = models.CharField(max_length=30)
    id_number = models.IntegerField(blank=True,null=True)
    votes = models.IntegerField()
    polling_station = models.CharField(max_length=50)
    is_published = models.BooleanField(blank=True,null=True, default=False)
    assigned_user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True, related_name='po_results')
    
    # special (dunder) method
    def __str__(self):
        return str(self.votes)
    
class FinalResult(models.Model):
    candidate_first_name = models.CharField(max_length=30)
    candidate_middle_name = models.CharField(max_length=30)
    candidate_last_name = models.CharField(max_length=30)
    votes = models.IntegerField()
    polling_station = models.CharField(max_length=50)
    
    # special (dunder) method
    def __str__(self):
        return self.candidate_first_name
    


