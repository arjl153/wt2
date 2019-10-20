from django.urls import path

from . import views
app_name = 'main_app'

urlpatterns = [
    path('', views.Index.as_view(), name = 'Index'),
    path('search_page', views.SearchPage.as_view(), name = 'SearchPage')
]