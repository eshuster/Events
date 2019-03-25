from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import *
from .serializers import *
from .scraper import *
from .event_service import *
from .search_manager import *

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt


#-----------------------------------------------------------------------------
@api_view(['GET'])
def events(request):
	events = Event.objects.all()
	serializer = EventSerializer(events, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PUT", "DELETE"])
def event(request, id):
	event = get_object_or_404(Event, id=id)
	
	if request.method == 'GET':
		serializer = EventSerializer(event, context={'request': request})
		
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	elif request.method == 'PUT':
		serializer = EventSerializer(event, data=request.data,context={'request': request})
		
		if serializer.is_valid():
			serializer.save()
			
			return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		event.delete()
		
		return Response(status=status.HTTP_204_NO_CONTENT)
	
@api_view(['POST'])
def create_event(request):
	serializer = EventSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

@api_view(['GET'])
def scrape_eventbrite_by_location(request):
	scraper = Scraper()
	response = scraper.scrape_eventbrite_by_location()

	return Response(response, status=status.HTTP_200_OK)
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
@api_view(['GET'])
def search_events(request):
	events = Event.search_results.search(**request.GET)
	events = EventSerializer(events, context={'request': request}, many=True)
	
	return Response(events.data, status.HTTP_200_OK)
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
@api_view(['GET'])
def authorize(request):
	authorization = Authorize()
	response = authorization.authorize()

	return HttpResponse(response)

@api_view(['GET'])
def eventbrite_callback(request):
	os.environ["oauth_token"] = request.GET['code']

	return Response({})
#-----------------------------------------------------------------------------








