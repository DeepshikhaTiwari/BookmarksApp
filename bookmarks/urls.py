from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmark/', views.BookmarkListView.as_view(), name='bookmark'),
    path('bookmark/<int:pk>', views.BookmarkDetailView.as_view(), name='bookmark-detail'),

    path('bookmark/create/', views.CreateBookmark.as_view(), name='bookmark-create'),
    path('bookmark/<int:pk>/update/', views.UpdateBookmark.as_view(), name='bookmark-update'),
    path('bookmark/<int:pk>/delete/', views.DeleteBookmark.as_view(), name='bookmark-delete'),

]
