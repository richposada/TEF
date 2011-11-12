# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from tef.main.models import Post
from tef.main.models import Friend
from tef.main.models import FriendForm
from tef.main.models import ContactForm
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


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
	
def cancel(request):
	t = loader.get_template("cancel.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def donation(request):
	t = loader.get_template("donation.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))	

def thanks(request):
	t = loader.get_template("thanks.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def leadership(request):
	t = loader.get_template("leadership.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def contact_thanks(request):
	t = loader.get_template("contact_thanks.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def EVANFest(request):
	t = loader.get_template("EVANFest2011.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def EVANFest2011Pictures(request):
	t = loader.get_template("EVANFest2011Pictures.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def EVANFest2011MorePics(request):
	t = loader.get_template("EVANFest2011MorePics.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))

def friend(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		form = FriendForm(request.POST) 
		if form.is_valid(): 
			form.save()
			return HttpResponseRedirect('/main/thanks') 
	else:
		form = FriendForm()		
		
	con = {'form': form}
	con.update(csrf(request))
	return render_to_response('friend.html', con)

			
def comingsoon(request):
	t = loader.get_template("comingsoon.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def privacypolicy(request):
	t = loader.get_template("privacypolicy.html")
	c = RequestContext(request)
	return HttpResponse(t.render(c))
	
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = request.POST.get('subject', '')
			message = request.POST.get('message', '')
			from_email = request.POST.get('from_email', '')
			if subject and message and from_email:
			      try:
			          send_mail(subject, message, 'no-reply@theevanfoundation.org', ['richposada@gmail.com'])
			      except BadHeaderError:
			          return HttpResponse('Invalid header found.')
			      return HttpResponseRedirect('/main/contact_thanks')			
	else:
		form = ContactForm()
		
	con = {'form': form}
	con.update(csrf(request))
	return render_to_response('contact.html', con)
	