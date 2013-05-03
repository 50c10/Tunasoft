from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tunasoft.apps.herramientas.views',
	url(r'^listado/$','listado_view',name='vista_Listado'),
	url(r'^dashboard/$','dashboard_view',name='dashboard_view'),
	url(r'^preferences/$','preferences_view',name='preferences_view'),
)