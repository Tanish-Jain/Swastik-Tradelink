"""tradelink URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from store.views import cart, checkout, contact, index, product, signin, signup
from . import settings
from django.conf.urls.static import static
from store.views.signin import signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.Index.as_view(), name='homepage'),
    path('contact', contact.contact, name='contact'),
    path('product/<int:id>', product.product, name='product'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout', checkout.Checkout.as_view(), name='checkout'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('signin', signin.Signin.as_view(), name='signin'),
    path('signout', signout, name='signout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
