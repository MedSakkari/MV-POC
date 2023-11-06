from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Interface admin django
    path('admin/', admin.site.urls),

    # Les URLs de l'application chatbot_ai
    path('api/', include('chatbot_ai.urls')),
    # Les URLs de l'application chatbot_core
    path('api/', include('chatbot_core.urls')),
    # Les URLs de l'application chatbot_dashboard
    path('api/', include('chatbot_dashboard.urls')),
    # Les URLs de l'application chatbot_manager
    path('api/', include('chatbot_manager.urls')),
    # Les URLs de l'application user_manager
    path('api/', include('user_manager.urls')),
]
