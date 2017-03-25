from django.conf.urls import url
from FeelREST import views
from rest_framework.urlpatterns import format_suffix_patterns
from keras.models import model_from_yaml
import os
module_dir = os.path.dirname(__file__)  # get current directory



urlpatterns = [
    url(r'^images/$', views.image_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)


