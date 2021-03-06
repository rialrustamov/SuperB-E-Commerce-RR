"""SuperB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns


from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from core.views import *


urlpatterns = i18n_patterns(
    path("core/", include('core.urls')),
    path("order/", include('order.urls')),
    path("blog/", include('blog.urls')),
    path("product/", include('product.urls')),
    # path('jet/', include('jet.urls', 'jet')),
    path("user/", include("user.urls")),
    path("", index, name="index"),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
)

urlpatterns += [
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
