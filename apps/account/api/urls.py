from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from apps.account.api.views import Logout,Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
