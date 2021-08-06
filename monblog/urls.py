# urls.py
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

# from django.conf.urls.defaults import *

from monblog.models import Article
from monblog.models import Commentaire

from monblog.feeds import RssArticle

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
   url(r'^$', 'monblog.views.accueil', name='accueil'),
   url(r'^feeds/$', RssArticle()),

   url(r'^articles/', 'monblog.views.articles', name='articles'),
   url(r'^articles/(?P<id>\d+)$', 'monblog.views.lireUnArticle', name='lireUnArticle'),
   url(r'^lireUnArticle/(?P<id>\d+)$', 'monblog.views.lireUnArticle', name='lireUnArticle'),   
   url(r'^addNewArticle/', 'monblog.views.addNewArticle', name='addNewArticle'),
   # url(r'^addNewCommentaire/', 'monblog.views.addNewCommentaire', name='addNewCommentaire'),
   
   url(r'^recherche/', 'monblog.views.recherche', name='recherche'),
   url(r'^contact/', 'monblog.views.contact', name='contact'),
   url(r'^mentionsLegales/', 'monblog.views.mentionsLegales', name='mentionsLegales'),
   
   url(r'^connexion_inscription/', 'monblog.views.connexion_inscription', name='connexion_inscription'),
   url(r'^connexion/', 'monblog.views.connexion', name='connexion'),
   url(r'^inscription/', 'monblog.views.inscription', name='inscription'),
   url(r'^deconnexion/', 'monblog.views.deconnexion', name='deconnexion'),

   # Uncomment the admin/doc line below to enable admin documentation:
   url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

   # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$',
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        },
    ),
)
