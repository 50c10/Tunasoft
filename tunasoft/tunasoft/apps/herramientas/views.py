# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def listado_view(request):
	return render_to_response('herramientas/listado.html', context_instance=RequestContext(request))