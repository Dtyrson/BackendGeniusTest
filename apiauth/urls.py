from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from apiauth import views


urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("dashboard/", views.dashboard),
    path('huggingFace/', views.index)
]