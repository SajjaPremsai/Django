from django.urls import path
from . import views

urlpatterns = [
    path(route="",view=views.login,name="login"),
    path(route="login/",view= views.login_request , name="login_request"),
    path(route="login/dashboard/",view=views.dashboard,name="dashboard"),
]
