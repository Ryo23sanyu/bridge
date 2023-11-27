from django.contrib import admin
from django.urls import path
from . import views # 現在のディレクトリ(カレントディレクトリ)からviwsのパッケージをimport

app_name ="pdfmr"

urlpatterns = [
    path('top/', views.top, name='top'),
]