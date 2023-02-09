from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

from shop.views import handler404p, handler500p

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
]

handler404 = handler404p
handler500 = handler500p
