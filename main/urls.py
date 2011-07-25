from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from tef.main.views import archive
from tef.main.views import home
from tef.main.views import mission
from tef.main.views import comingsoon
from tef.main.views import neuroblastoma
from tef.main.views import evan
from tef.main.views import help
from tef.main.views import events
from tef.main.views import contact
from tef.main.views import donate


urlpatterns = patterns('',
    url(r'home', home),
    url(r'mission', mission),
    url(r'neuroblastoma', neuroblastoma),
    url(r'evan', evan),
	url(r'posts', archive),
	url(r'help', help),
	url(r'events', events),
	url(r'contact', contact),
	url(r'donate', donate),
    url(r'^$', comingsoon),
    
)