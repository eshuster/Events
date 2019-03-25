from .models import * 
from django.shortcuts import render, get_object_or_404

class EventService:

	def add_events(self, list_of_events):
		for event in list_of_events['events']:
			ticket_classes = list(filter(lambda x : x['on_sale_status']=="AVAILABLE", event['ticket_classes']))

			if len(ticket_classes) == 0:
				new_event = Event(name=event['name']['text'], start_date=event['start']['utc'], organizer_id=event['organization_id'], ticket_cost=0)
			else:
				if event['is_free'] == True:
					new_event = Event(name=event['name']['text'], start_date=event['start']['utc'], organizer_id=event['organization_id'], ticket_cost=0)
				else:
					if ticket_classes[0]['free']==True or 'cost' not in ticket_classes[0]:
						new_event = Event(name=event['name']['text'], start_date=event['start']['utc'], organizer_id=event['organization_id'], ticket_cost=0)
					else:
						new_event = Event(name=event['name']['text'], start_date=event['start']['utc'], organizer_id=event['organization_id'], ticket_cost=float(ticket_classes[0]['cost']['major_value']))
			new_event.save()
