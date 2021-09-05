from api.views import testView
from django.urls import path

urlpatterns = [
    path('', testView.as_view(), name='home')
]
