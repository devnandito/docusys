from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docusys.users.urls', namespace='users')),
    path('', include('docusys.levels.urls', namespace='levels')),
    # path('', include('pos.categories.urls', namespace='categories')),
    # path('', include('pos.clients.urls', namespace='clients')),
    # path('', include('pos.products.urls', namespace='products')),
    # path('', include('pos.sales.urls', namespace='sales')),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)