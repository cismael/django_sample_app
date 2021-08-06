# feeds.py
# -*- coding: utf-8

from django.utils.feedgenerator import Rss201rev2Feed

from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from monblog.models import Article

from datetime import datetime

class RssArticle(Feed):
    feed_type = Rss201rev2Feed
    link = "/fluxRss/"
    title = "/fluxRss_title.html"
    description = "/fluxRss_description.html"
    
    def items(self):
        return Article.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.titre

    def item_description(self, item):
        return item.contenu

    def item_pubdate(self, item):
        text = "Date De Publication : "
        return item.date
        # datetime.combine(datetime.strptime("5 Mar 12", "%d %b %y") ,datetime.strptime("0130","%H%M").time()

    def item_link(self, item):
        return reverse('monblog.views.lireUnArticle', args=[item.id])
