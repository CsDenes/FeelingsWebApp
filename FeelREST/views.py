from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from FeelREST.models import Image
from FeelREST.serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import base64
from keras.preprocessing.image import load_img, img_to_array
from FeelREST.KerasManager import KerasManager

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from keras.models import model_from_yaml
import os

module_dir = os.path.dirname(__file__)  # get current directory


'''
# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
'''


@api_view(['GET', 'POST'])
def image_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Image.objects.all()
        serializer = ImageSerializer(snippets, many=True)
        print("get arrived")

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():

            loaded_model = KerasManager.loadModel()

            serializer.save()
            imageData = base64.b64decode(request.data["name"])
            file_path = os.path.join(module_dir, "image.png")

            with open(file_path, 'wb') as f:
                f.write(imageData)

            img = load_img(file_path)
            testX = img_to_array(img)
            testX = testX.reshape((1,) + testX.shape)

            predict = loaded_model.predict(testX)

            an = float(predict[0][0])
            di = float(predict[0][1])
            fe = float(predict[0][2])
            ha = float(predict[0][3])
            sa = float(predict[0][4])
            su = float(predict[0][5])

            return Response(json.dumps({"an" : an, "di" : di, "fe" : fe, 'ha': ha, "sa" : sa, "su" : su}), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)