from django.urls import path

from .views import CountryListCreateView, CountryDetailView
urlpatterns = [
    path('', CountryListCreateView.as_view(), name='country_list_create'),
    path('<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
]
