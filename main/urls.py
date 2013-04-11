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
from tef.main.views import kristen
from tef.main.views import hannah
from tef.main.views import news
from tef.main.views import treats
from tef.main.views import julianna
from tef.main.views import springtime
from tef.main.views import EVANFest2012
from tef.main.views import Year2012Review
from tef.main.views import golf

urlpatterns = patterns('',
    url(r'home', golf),
    url(r'mission', mission),
    url(r'neuroblastoma', neuroblastoma),
    url(r'evan', evan),
	url(r'posts', archive),
	url(r'help', help),
	url(r'events', events),
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
	url(r'kristen', kristen),
	url(r'hannah', hannah),
	url(r'news', news),
	url(r'treats', treats),
	url(r'julianna', julianna),
	url(r'springtime', springtime),
	url(r'EVANFest2012', EVANFest2012),
	url(r'Year2012Review', Year2012Review),
	url(r'golf', golf),
    url(r'^$', golf),
    
)