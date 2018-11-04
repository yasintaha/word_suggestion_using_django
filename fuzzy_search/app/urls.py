from django.conf.urls import url
from app import views


urlpatterns = [
	url(r'^search$', views.SuggestionView.as_view(), name='test'),
]