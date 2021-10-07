
"""area51 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blogging/', include('blogging.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# from order.views import CreateCheckoutSessionView, stripe_webhook

urlpatterns = [
    path('admin/', admin.site.urls),

    #including django provided links for auth and password reset
    path('', include('django.contrib.auth.urls')),

    #path for home
    path('', views.IndexView.as_view(), name='home'),
    

    #path for apps
    path('user/', include('gnm_users.urls')),
    path('product/', include('product.urls')),
    path('seller/', include('seller.urls')),
    path('order/', include('order.urls')),
    path('blog/', include('blog.urls')),

    #for payment
    # path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    # path('webhook/stripe', stripe_webhook, name='stripe-webhook')
]


# to remove django sidebar
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

# to serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

