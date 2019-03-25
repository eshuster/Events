from django.db import models
from datetime import datetime    
from django.utils.timezone import now
from .validations import *
from .search_manager import *
from django import forms
from django.core import validators

class Event(models.Model):
	name = models.CharField(max_length=100, unique=True)
	start_date = models.DateTimeField(validators=[validate_start_date])
	organizer_id = models.CharField(max_length=100)
	ticket_cost = models.IntegerField(validators=[validate_even])
	created = models.DateTimeField(auto_now_add=True)	
	last_updated = models.DateTimeField(auto_now_add=True)
	
	objects = models.Manager()
	search_results = SearchManager()

	def __str__(self):
		return self.name