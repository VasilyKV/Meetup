import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from meetup_db.models import Speaker, Speech, Event
from meetup_db.models import get_event_discription, get_groups, get_events, get_speech_events, get_event_speeches

print(get_events(2))
print(get_speech_events(2))
print(get_event_discription(1))
print(get_event_speeches(1))