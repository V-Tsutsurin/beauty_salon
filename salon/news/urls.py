from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('news/', views.news, name='news'),
    # path('<int:discount_id>/', views.detail, name='detail'),

]