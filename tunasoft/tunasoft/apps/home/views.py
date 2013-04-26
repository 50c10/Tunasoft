# Create your views here.
from django.contrib.auth import logout , authenticate ,login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from tunasoft.apps.home.forms import LoginForm
def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	return render_to_response('home/about.html', context_instance=RequestContext(request))

def contact_view(request):
	return render_to_response('home/contact.html', context_instance=RequestContext(request))

def web_view(request):
	return render_to_response('home/web.html', context_instance=RequestContext(request))

def sistemas_view(request):
	return render_to_response('home/sistemas.html', context_instance=RequestContext(request))

def movil_view(request):
	return render_to_response('home/movil.html', context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/listado')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/listado')
				else:
					mensaje = "usuario o password incorrecto"
		form = LoginForm()
		ctx ={'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))