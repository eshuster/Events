from django.test import TestCase
from ..models import *
from ..search_manager import *
from ..serializers import *


class SearchManagerTest(TestCase):
	def setUp(self):
		self.event_list = []
		self.event_list.append(Event.objects.create(name="Test Event 1", start_date="2019-03-21", organizer_id=12345, ticket_cost=10))
		self.event_list.append(Event.objects.create(name="Test Event 2", start_date="2019-03-21", organizer_id=12345, ticket_cost=20))
		self.event_list.append(Event.objects.create(name="Test Event 3", start_date="2019-03-25", organizer_id=12345, ticket_cost=30))
		self.event_list.append(Event.objects.create(name="Test Event 4", start_date="2019-03-25", organizer_id=12345, ticket_cost=30))
		self.event_list.append(Event.objects.create(name="Test Event 5", start_date="2019-03-25", organizer_id=12345, ticket_cost=30))

	def test_search_by_name(self):
		events = Event.objects.get(name="Test Event 1")
		search_results = Event.search_results.search(**{'name': '1'})

		self.assertEqual(events.id, search_results[0].id)

	def test_search_by_cost(self):
		events = Event.objects.filter(ticket_cost="30")
		search_results = Event.search_results.search(**{'ticket_cost': 30})

		self.assertEqual(events[0].id, search_results[0].id)
		self.assertEqual(events[1].id, search_results[1].id)
		self.assertEqual(events[2].id, search_results[2].id)


	def test_search_by_start_date(self):
		search_date = datetime.strptime('2019-03-21', '%Y-%m-%d')
		events = Event.objects.filter(start_date__year = search_date.year, start_date__month = search_date.month, start_date__day = search_date.day)
		search_results = Event.search_results.search(**{'start_date': search_date})

		self.assertEqual(events[0].id, search_results[0].id)
		self.assertEqual(events[1].id, search_results[1].id)
