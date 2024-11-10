from django.urls import path
from rest_framework.documentation import include_docs_urls
from .views import RegisterUserView, RegisterWarehouseAssistantView, LoginView

urlpatterns = [
    path('docs/', include_docs_urls(title='API Documentation')),
    path('register/user', RegisterUserView.as_view(), name='register_user'),
    path('register/warehouse-assistant', RegisterWarehouseAssistantView.as_view(), name='register_warehouse_assistant'),
    path('login', LoginView.as_view(), name='login'),
]
