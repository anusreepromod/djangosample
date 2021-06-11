from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('hello/',views.hello),
    path('html/' , views.htm),
    path('sample/',views.sample)

]