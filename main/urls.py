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
from tef.main.views import cale
from tef.main.views import carly
from tef.main.views import girlscout
from tef.main.views import daisy
from tef.main.views import springtime
from tef.main.views import EVANFest2012
from tef.main.views import Year2012Review
from tef.main.views import golf
from tef.main.views import research
from tef.main.views import fish
from tef.main.views import pizza
from tef.main.views import alyssaclaire
from tef.main.views import townsend

urlpatterns = patterns('',
    url(r'home', golf),
    url(r'mission', mission),
    url(r'neuroblastoma', neuroblastoma),
    url(r'evan', evan),
	url(r'posts', archive),
	url(r'help', help),
	url(r'events', fish),
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
	url(r'news', fish),
	url(r'treats', treats),
	url(r'julianna', julianna),
	url(r'cale', cale),
	url(r'carly', carly),
	url(r'girlscout', girlscout),
	url(r'daisy', daisy),
	url(r'townsend', townsend),
	url(r'alyssaclaire', alyssaclaire),
	url(r'springtime', springtime),
	url(r'EVANFest2012', EVANFest2012),
	url(r'Year2012Review', Year2012Review),
	url(r'golf', golf),
	url(r'research', research),
	url(r'fish', fish),
    url(r'^$', golf),
    
)