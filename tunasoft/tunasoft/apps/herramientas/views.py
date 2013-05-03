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

@login_required(login_url='/login/')
def calendario_view(request):
	return render_to_response('herramientas/calendario.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def miembros_view(request):
	return render_to_response('herramientas/miembros.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def dashboard_view(request):
	return render_to_response('herramientas/dashboard.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def preferences_view(request):
	return render_to_response('herramientas/preferences.html', context_instance=RequestContext(request))