from django.urls import path

from sibdev.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home')
]