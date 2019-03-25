from .event_service import *
from django.db import models
from lyte.config import *

import requests
import json
import geocoder

class Scraper:
	def __init__(self):
		self.token = os.environ.get('oauth_token')
		
		coordinates = geocoder.ip('me').latlng
		# self.latitude = "37.7440158"
		self.latitude = str(coordinates[0])
		# self.longitude = "-122.47460219999999"
		self.longitude = str(coordinates[1])

	def scrape_eventbrite_by_location(self):
		url = "https://www.eventbriteapi.com/v3/events/search?location.longitude=" + self.longitude + "&location.latitude=" + self.latitude + "&expand=ticket_classes&token=" + self.token
		response = requests.get(url)

		event_service = EventService()
		event_service.add_events(response.json())

		return response.json()
		