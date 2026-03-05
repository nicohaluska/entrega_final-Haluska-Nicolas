from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('pages/', PostListView.as_view(), name='pages'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='page_detail'),
    path('pages/create/', PostCreateView.as_view(), name='page_create'),
]
