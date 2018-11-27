from django.urls import path
from web_misperris import views
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # VISTAS GENERALES (INDEX Y FORMULARIO REGISTRO DE USUARIO) 
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('login/', views.login, name='login'),
    path('registrado/<int:pk>/', views.registrado, name='registrado'),
    #VISTAS DEL ADMINISTRADOR 
	path('listar/', views.RescatadoList.as_view(), name = 'rescatado_list'),
	path('listarr/', views.RescatadoListR.as_view(), name = 'rescatado_list_rescatado'),
	path('listara/', views.RescatadoListA.as_view(), name = 'rescatado_list_adoptado'),
	path('listard/', views.RescatadoListD.as_view(), name = 'rescatado_list_disponible'),	
	path('crear/', views.RescatadoCreate.as_view(), name = 'rescatado_create'),
	path('editar/(?P<pk>[\w-]+)$', views.RescatadoUpdate.as_view(), name = 'rescatado_update'),
	path('eliminar/(?P<pk>[\w-]+$', views.RescatadoDelete.as_view(), name = 'rescatado_delete'),
	#VISTA DE USUARIO 
	path('usuario/', views.usuario.as_view(), name = 'usuario'),

	path('auth/', include('social_django.urls', namespace='social')),  # <- login social
	path('rescatadoapi/', views.RescatadoList.as_view()),
	path('rescatadoapi/(?P<pk>[\w-]+)$', views.RescatadoDetail.as_view()),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)