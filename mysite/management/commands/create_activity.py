from ... models import M_user, Activity
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('real_name', type=str, help='Indicates real name')
        parser.add_argument('start_time', type=str, help='Indicates start_time')
        parser.add_argument('end_time', type=str, help='Indicates end_time')


    def handle(self, *args, **kwargs):
        real_name = kwargs['real_name']
        start_time = kwargs['start_time']
        end_time = kwargs['end_time']
        name = M_user.objects.get(real_name=real_name)
        activity = Activity(member_id=name, start_time=start_time, end_time=end_time)
        activity.save()
