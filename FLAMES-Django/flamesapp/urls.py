from django.urls import path
from .views import FLAMES

urlpatterns = [
    path('', FLAMES, name='flames'),
    # other URL patterns...
]
