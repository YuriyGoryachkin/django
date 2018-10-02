from django.urls import path
from .views import *

app_name = 'auth'
urlpatterns = [
#     path('login', login, name='login'),
    path('logout', logout, name='logout'),
#     path('register', register, name='register'),
#     path('edit', edit, name='edit'),
]
