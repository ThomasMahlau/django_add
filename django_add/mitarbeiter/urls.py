from django.urls import path
from .views import *

urlpatterns = [
   path('', entry, name='entry'),
   path('mitarbeiter/', mitarbeiter_list, name='mitarbeiter_list'),
   path('mitarbeiter/liste/', mitarbeiter_list, name='mitarbeiter_list'),
   path('mitarbeiter/liste/filter/', mitarbeiter_list_filter, name='mitarbeiter_list_filter'),
   path('mitarbeiter/detail/<int:id>', mitarbeiter_detail, name='mitarbeiter_detail'),
   #path('mitarbeiter/update/', mitarbeiter_update, name='mitarbeiter_update'),
   path('login', loginSeite, name='loginSeite'),
   path('logout', logoutBenutzer, name='logout'),
   path('register', register, name='register'),
]