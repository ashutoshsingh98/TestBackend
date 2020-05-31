from ... models import M_user, Activity
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('eid', type=str, help='Indicates eid')
        parser.add_argument('real_name', type=str, help='Indicates real name')
        parser.add_argument('tz', type=str, help='Indicates tz')


    def handle(self, *args, **kwargs):
        eid = kwargs['eid']
        real_name = kwargs['real_name']
        tz = kwargs['tz']
        start_time = datetime.now()
        end_time = datetime.now()
        name = M_user.objects.create_user(real_name=real_name, eid=eid, tz=tz, password=123)
        activity = Activity(member_id=name, start_time=start_time, end_time=end_time)
        activity.save()
