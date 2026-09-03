from django.urls import path
from .views import *

urlpatterns = [
   path('', entry, name='entry'),
   path('klienten/', klienten_list, name='klienten_list'),
   path('klienten/liste/', klienten_list, name='klienten_list'),
   path('klienten/detail/<int:id>', klienten_detail, name='klienten_detail'),
   path('klienten/update/', klienten_update, name='klienten_update'),
]