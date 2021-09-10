from django.urls import path

from TFIDFapp import views
from .views import AddFileView, ClearAllView, chose_file, make_table, fill_db

urlpatterns = [
    path('', AddFileView.as_view(), name='add_file'),
    path('chose_file/', chose_file, name='chose_file'),
    path('clear_all/', ClearAllView.as_view(), name='clear_all'),
    path('make_table/', make_table, name='make_table'),
    path('fill_db/', fill_db, name='fill_db'),
]
