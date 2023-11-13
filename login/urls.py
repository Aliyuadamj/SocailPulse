from django.urls import path
from . import views

urlpatterns = [
    path('', views.logins, name="logins"),
    path('<int:pk>', views.login, name="login"),
    path('create', views.create_login, name="create_login"),
    path('<int:pk>/update', views.update_login, name="login_update"),
    path('<int:pk>/delete', views.login_delete, name='login_dalete'),
]