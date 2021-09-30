from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern


urlpatterns = [path("usersEp/", include("api.urls"))]
