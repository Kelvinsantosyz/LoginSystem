from django.urls import path
from .views import home, signup, signin

urlpatterns = [
    path('index/', home, name='home'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
]
