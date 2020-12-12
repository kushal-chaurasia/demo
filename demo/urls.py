
from django.contrib import admin
from django.urls import path , include
from api import views

urlpatterns = [
    path('/', views.home),
    path('admin/', admin.site.urls),
    path('cardinfo/<int:ck>', views.card_detail),
    path('cardinfo/', views.card_list)
]
