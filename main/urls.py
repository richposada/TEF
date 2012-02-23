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
from tef.main.views import cancel
from tef.main.views import donation
from tef.main.views import friend
from tef.main.views import thanks
from tef.main.views import contact_thanks
from tef.main.views import privacypolicy
from tef.main.views import leadership
from tef.main.views import EVANFest
from tef.main.views import EVANFest2011Pictures
from tef.main.views import EVANFest2011MorePics
from tef.main.views import partners

urlpatterns = patterns('',
    url(r'home', home),
    url(r'mission', mission),
    url(r'neuroblastoma', neuroblastoma),
    url(r'evan', evan),
	url(r'posts', archive),
	url(r'help', help),
	url(r'events', EVANFest),
	url(r'contact', contact),
	url(r'donate', donate),
	url(r'cancel', cancel),
	url(r'donation', donation),
	url(r'friend', friend),
	url(r'thanks', thanks),
	url(r'contact_thanks', contact_thanks),
	url(r'privacypolicy', privacypolicy),
	url(r'leadership', leadership),
	url(r'pictures', EVANFest2011Pictures),
	url(r'more', EVANFest2011MorePics),
	url(r'partners', partners),
    url(r'^$', home),
    
)