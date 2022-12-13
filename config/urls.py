from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from config import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),  # Home
    # Menu    
    path('dashboard/', include('dashboard.urls', namespace='dashboard')), # Dashboard
    # Apps 
    path('layouts/', include('layouts.urls')),  # Layout
    path('authentication/', include('authentication.urls')),  # Authentication

    path('admin/', admin.site.urls),  # Admin
]

handler403 = views.error_403
handler404 = views.error_404
handler500 = views.error_500

import sys
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

if settings.DEBUG:
    if not TESTING:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


