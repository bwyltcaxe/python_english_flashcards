"""
URL configuration for language_flashcards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cards/', views.cards_list, name='cards-list'),
    path('cards/add/', views.add_card, name='add-card'),
    path('cards/edit/<int:card_id>/', views.edit_card, name='edit-card'),
    path('exam/', views.exam_collections, name='exam'),
    path('exam/<int:collection_id>/', views.exam_session, name='exam-session'),
]
