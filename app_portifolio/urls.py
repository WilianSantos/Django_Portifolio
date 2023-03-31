from django.urls import path

from .views import IndexView


urlpatterns = [
    path('', IndexView.index, name='index')
]
