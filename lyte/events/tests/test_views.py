import json 

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from rest_framework import status

from ..models import *
from ..serializers import *
from ..scraper import *
from ..event_service import *
from ..search_manager import *

client = Client()

class EventViews(TestCase):

	def setUp(self):
		Event.objects.create(name="Test Event 1", start_date="2021-03-24", organizer_id=12345, ticket_cost=100)
		Event.objects.create(name="Test Event 2", start_date="2021-03-24", organizer_id=12345, ticket_cost=100)
		Event.objects.create(name="Test Event 3", start_date="2021-03-24", organizer_id=12345, ticket_cost=100)

	def test_get_all_events(self):
		response = client.get(reverse('events'))
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		
		self.assertEqual(response.json(), serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_event(self):
		response = client.get(reverse('event', kwargs={'id': "1" }))
		event = Event.objects.get(name="Test Event 1")
		serializer = EventSerializer(event)

		self.assertEqual(response.json(), serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid(self):
		response = client.get(reverse('event', kwargs={'id': "10" }))
        
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_create_valid_event(self):
		valid_params = {
			'name': 'Test Event 4',
			'start_date': '2021-03-21T20:12:56.730Z',
			'organizer_id': 12345,
			'ticket_cost': 100
		}

		response = client.post(reverse('create_event'), data=json.dumps(valid_params), content_type='application/json')
		
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_event(self):
		valid_params = {
			'name': 'Test Event 1', #Already Present
			'start_date': '2021-05-03',
			'organizer_id': 12345,
			'ticket_cost': 100
		}

		response = client.post(reverse('create_event'), data=json.dumps(valid_params), content_type='application/json')
		
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


	def test_update_event(self):
		valid_params = {
			'name': '(Updated) Test Event 1',
			'start_date': '2021-03-21T20:12:56.730Z',
			'organizer_id': 12345,
			'ticket_cost': 100
		}
		response = client.put(reverse('event', kwargs={'id': "1" }), data=json.dumps(valid_params), content_type='application/json')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_delete_event(self):
		
		response = client.delete(reverse('event', kwargs={'id': "1" }), content_type='application/json')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)






