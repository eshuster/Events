from django.db import models
from .models import *

class SearchManager(models.Manager):
	def get_queryset(self):
		return super(SearchManager, self).get_queryset()

	def search(self, **kwargs):
		qs = self.get_queryset()
		if kwargs.get('name', ''):
			qs = qs.filter(name__icontains = kwargs['name'][0])
		if kwargs.get('ticket_cost', ''):
			qs = qs.filter(ticket_cost = kwargs['ticket_cost'] if type(kwargs['ticket_cost']) == int else kwargs['ticket_cost'][0])
		if kwargs.get('start_date', ''):
			if type(kwargs['start_date']) != list:
				search_date = kwargs['start_date']
			else:
				search_date = datetime.strptime(kwargs['start_date'][0], '%Y-%m-%d')
			qs = qs.filter(start_date__year = search_date.year, start_date__month = search_date.month, start_date__day = search_date.day )
		return qs