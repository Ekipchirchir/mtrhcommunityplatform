from .views import *
from django.urls import path 

urlpatterns =[
    path('home/', home, name= 'home' ),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('messages/', messages, name='messages'),
    path('departments/', departments, name='departments'),
    path('ict/', ict, name='ict'),
    path('pharmacy/', pharmacy, name='pharmacy'),
    path('finance/', pharmacy, name='finance'),
    path('administration/', pharmacy, name='administration'),
    path('lab/', lab, name = 'lab'),
    path('radiology/', radiology, name = 'radiology'),
    path('supplychain/', supplychain, name = 'supplychain'),
    path('kitchen/', kitchen, name = 'kitchen'),
    path('icu/', icu, name = 'icu'),
    path('emergency/', emergency, name = 'emergency'),
    path('ict/', ict, name = 'ict'),
    path('footer/', footer, name = 'footer'),
    path('announcements/', footer, name = 'announcements'),
]