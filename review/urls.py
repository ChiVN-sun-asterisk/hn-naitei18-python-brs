from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    BooksListView,
    SearchBookListView,
    request_form,
    BookDetailView,
    
)

urlpatterns = [
    path('', views.index, name='index'),
    path('books', BooksListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('search-book-results/', SearchBookListView.as_view(), name='search'),
    path('request/', request_form, name='request'),
    path('list-request/', views.list_request, name='list-request'),
    path('books/<int:pk>/mark-favorite/', views.MarkFavorite.as_view(), name='mark-favorite'),
    path('books/<int:pk>/mark-read/', views.MarkRead.as_view(), name='mark-read'),
    path('delete-review/<int:pk>', views.delete_review, name='delete-review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
