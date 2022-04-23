from  django.urls import path
from .views import HomeView, LoginView, LogoutView, SigninView


app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signin/', SigninView.as_view(), name='signin'),
]