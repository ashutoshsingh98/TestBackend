from .models import M_user
from .serializers import MemberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def activity_list(request):
    json_dict = {}
    json_dict['ok'] = False
    if request.method == 'GET':
        json_dict['ok'] = True
        activities = M_user.objects.all()
        serializer = MemberSerializer(activities, many=True)
        json_dict['Members'] = serializer.data
        return Response(json_dict)


@api_view(['GET', 'DELETE'])
def activity_detail(request, pk):
    try:
        activity = M_user.objects.get(pk=pk)
    except M_user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(activity)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
