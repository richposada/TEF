# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from tef.main.models import Post

def archive(request):
	posts = Post.objects.all()
	t = loader.get_template("archive.html")
	c = Context({'posts' : posts})
	return HttpResponse(t.render(c))

def home(request):
	posts = Post.objects.all()
	t = loader.get_template("home.html")
	c = Context({'posts' : posts})
	return HttpResponse(t.render(c))
	
def mission(request):
	t = loader.get_template("mission.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def neuroblastoma(request):
	t = loader.get_template("neuroblastoma.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def evan(request):
	t = loader.get_template("evan.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def help(request):
	t = loader.get_template("help.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def events(request):
	t = loader.get_template("events.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))	
	
def contact(request):
	t = loader.get_template("contact.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def donate(request):
	t = loader.get_template("donate.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))

	
def comingsoon(request):
	t = loader.get_template("comingsoon.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	