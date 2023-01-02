"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from curso.views import index, PostList, PostDetalle, PostCrear, PostBorrar, PostActualizar, UserSignUp, UserLogIn, UserLogout, AvatarActualizar, UserActualizar, MensajeDetalle, MensajeListar, MensajeCrear, MensajeBorrar

urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('actualizacion_exitosa/', TemplateView.as_view(template_name = "ejemplo/actualizacion_exitosa.html")),
    path('curso/', index, name="curso-index"),
    path('curso/listar', PostList.as_view(), name="curso-listar"), 
    path('curso/<int:pk>/detalle/', PostDetalle.as_view(), name="curso-detalle"), 
    path('curso/crear', PostCrear.as_view(), name="curso-crear"),
    path('curso/<int:pk>/borrar/', PostBorrar.as_view(), name="curso-borrar"),
    path('curso/<int:pk>/actualizar/', PostActualizar.as_view(), name="curso-actualizar"),
    path('curso/signup', UserSignUp.as_view(), name="curso-signup"),
    path('curso/login', UserLogIn.as_view(), name="curso-login"),
    path('curso/logout/', UserLogout.as_view(), name="curso-logout"),
    path('curso/avatares/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="curso-avatar-actualizar"),
    path('curso/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="curso-users-actualizar"),
    path('curso/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="curso-mensajes-detalle"),
    path('curso/mensajes/listar/', MensajeListar.as_view(), name="curso-mensajes-listar"),
    path('curso/mensaje/crear/', MensajeCrear.as_view(), name="curso-mensajes-crear"),
    path('curso/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="curso-mensajes-borrar"),
    path('curso/about', TemplateView.as_view(template_name='curso/about.html'), name="curso-about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)