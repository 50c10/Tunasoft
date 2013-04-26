# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from tunasoft.apps.herramientas.models import herramienta

@login_required(login_url='/login/')
def listado_view(request):
	herramientas = herramienta.objects.filter(status=True)
	ctx = {'herramientas':herramientas}
	return render_to_response('herramientas/listado.html', ctx, context_instance=RequestContext(request))