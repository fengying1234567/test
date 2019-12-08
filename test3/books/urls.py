from django.conf.urls import url
from books import views
urlpatterns = [
    url(r'^index$',views.index),
    url(r'^index2$',views.index2),
    url(r'^books$',views.show_books),
    url(r'^books/(\d+)$',views.detail),
    url(r'^feng$', views.feng123),


]

