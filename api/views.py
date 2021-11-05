from .serializers import HeroSerializer
from .models import Hero
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

class HeroViewSet(ListView):
    @api_view(['DELETE'])
    def delete_all_items(request):
        Hero.objects.all().delete()
        serializer_class = HeroSerializer
        return Response(serializer_class)
