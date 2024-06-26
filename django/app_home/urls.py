from django.urls import path, include
from .views import streamlit_view, authenticate_user, get_users

urlpatterns = [
    path("", streamlit_view),
    path('authenticate/', authenticate_user, name='authenticate_user'),
    path('get_users/', get_users, name='get_users'),
    # Other URL patterns
]
