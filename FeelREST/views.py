from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from FeelREST.models import Image
from FeelREST.serializers import ImageSerializer


# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
