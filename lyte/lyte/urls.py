from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path('admin/', admin.site.urls),
    path('events/', views.events, name='events'),
    re_path(r'searchevents/$', views.search_events, name='search_events'),
    path('event/<int:id>', views.event, name='event'),
    path('event/', views.create_event, name='create_event'),
    path('eventbrite/', views.scrape_eventbrite_by_location, name='scrape_eventbrite_by_location'),
    path('authorize/', views.authorize, name='authorize'),
    path('callback/', views.eventbrite_callback, name='eventbrite_callback')
]

