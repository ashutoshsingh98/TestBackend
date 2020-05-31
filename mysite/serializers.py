from rest_framework import serializers
from .models import Activity, M_user


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['start_time', 'end_time']

class MemberSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = M_user
        fields = ['eid', 'real_name', 'tz', 'activities']