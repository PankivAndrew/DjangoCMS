from django.conf.urls import url
from Tours import views

urlpatterns = [
    url(r'^sofa', views.index, name='index')

]
