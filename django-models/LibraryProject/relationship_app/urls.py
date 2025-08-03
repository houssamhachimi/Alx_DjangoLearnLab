from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # ✅ Required for the check
from . import views  # ✅ Required to expose views.register

urlpatterns = [
    path('register/', views.register, name='register'),  # ✅ views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ LoginView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅ LogoutView
]
