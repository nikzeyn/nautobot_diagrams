"""Urls for nautobot_diagrams."""

from django.urls import path

from nautobot_diagrams import views


urlpatterns = [
    # path('random/', views.RandomAnimalView.as_view(), name='random_animal'),
    path('site_topology/', views.SiteTopologyView.as_view(), name='site_topology'),
    path('topology/', views.TopologyView.as_view(), name='topology'),
]