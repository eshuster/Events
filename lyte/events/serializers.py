from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = ('id','name', 'start_date', 'organizer_id', 'ticket_cost','created','last_updated')
        # fields = ('id','name', 'start_date', 'organizer_name', 'ticket_cost','created','last_updated')