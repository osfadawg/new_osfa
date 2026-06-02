from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExampleModel
from .serializers import ExampleModelSerializer

# Create your views here.
@api_view(['GET'])
def example_list(request):
     data = ExampleModel.objects.all()
     serializer = ExampleModelSerializer(data, many=True)
     return Response(serializer.data)