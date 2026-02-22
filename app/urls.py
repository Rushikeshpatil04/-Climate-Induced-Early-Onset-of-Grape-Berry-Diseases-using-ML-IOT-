from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name= "home"),
    path("register", views.register, name= "register"),
    path("log_in", views.log_in, name= "log_in"),
    path("dashboard", views.dashboard, name= "dashboard"),
    path('upload_crop_image/', views.upload_crop_image, name='upload_crop_image'),
    path("log_out", views.log_out, name= "log_out"),
    path("crop_dis", views.crop_dis, name= "crop_dis"),
    path("fert_report", views.fert_report, name= "fert_report"),
    path('upload',views.upload , name='upload'),
    path('predict',views.predict , name='predict'),


]