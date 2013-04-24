from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tunasoft.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^contact/$','contact_view',name='vista_contact'),
)