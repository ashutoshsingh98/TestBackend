from ... models import M_user, Activity
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('real_name', type=str, help='Indicates real name')


    def handle(self, *args, **kwargs):
        real_name = kwargs['real_name']
        start_time = datetime.now()
        end_time = datetime.now()
        name = M_user.objects.get(real_name=real_name)
        activity = Activity(member_id=name, start_time=start_time, end_time=end_time)
        activity.save()
