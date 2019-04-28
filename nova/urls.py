"""nova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from core.views import UserViewSet
from core.views.ContaineView import ContainerView

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    # url('admin/', admin.site.urls),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    # url(r'^', include(router.urls)),
    url(r'^core', ContainerView.as_view(), name='core'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]