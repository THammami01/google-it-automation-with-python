from django.urls import re_path
from django.contrib import admin
from feedback import views

urlpatterns = [
    re_path(r'^feedback/', views.feedback_list),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.feedback_index),
]
