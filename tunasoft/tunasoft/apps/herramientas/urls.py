from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tunasoft.apps.herramientas.views',
	url(r'^listado/$','listado_view',name='vista_Listado'),
)