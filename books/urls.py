from django.urls import path
from tutorial.urls import router

import books.views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', books.views.BookViewset, basename='books')

router.register('users', books.views.UserViewset, basename='users')

urlpatterns = [
    # path('', books.views.BookListApiView.as_view()),
    # path('books/', books.views.book_list_view),
    # path('<int:pk>/detail/', books.views.BookDetailView.as_view()),
    # path('<int:pk>/delete/', books.views.BookDeleteApiView.as_view()),
    # path('<int:pk>/update/', books.views.BookUpdateApiView.as_view()),
    #
    # path('books/create/', books.views.BookCreateApiView.as_view()),
    #
    # path('list/create/', books.views.BookListCreateApiView.as_view()),
    # path('update/delete/<int:pk>/', books.views.BookUpdateDeleteApiView.as_view()),
    #
    # path('book/', books.views.BookListApi.as_view()),
    # path('create/', books.views.BookCreateApi.as_view()),
    # path('detail/<int:pk>/', books.views.BookDetailApi.as_view()),
    # path('delete/<int:pk>/', books.views.BookDeleteApi.as_view()),
    # path('<int:pk>/update/', books.views.BookUpdateApi.as_view())


]

urlpatterns = urlpatterns + router.urls