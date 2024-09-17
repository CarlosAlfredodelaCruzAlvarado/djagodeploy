# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import ComplaintList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('complaints.urls')),  # API routes
    path('', include('complaints.urls')),  # Frontend routes if applicable
        path('complaints/', ComplaintList.as_view(), name='complaints'),

]
