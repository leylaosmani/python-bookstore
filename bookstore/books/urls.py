from django.urls import path

from . import views


urlpatterns = [
    # Route for login page
    path('login/', views.loginPage, name="login"),
    # Route for login page
    path('logout/', views.logoutUser, name="logout"),
    # Route for register page
    path('register/', views.registerUser, name="register"),

    path('', views.books, name="books"),

    path('book/<str:pk>/', views.book, name="book"),

    path('add_book/', views.addBook, name="add_book"),
    
    path('update_book/<str:pk>/', views.updateBook, name="update_book"),
    
    path('delete_book/<str:pk>/', views.deleteBook, name="delete_book"),
]