"""monblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


from monblog import views as myapp_views

# from monblog.models import Article
# from monblog.models import Commentaire
from monblog.feeds import RssArticle

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', myapp_views.accueil, name='accueil'),
    url(r'^feeds/$', RssArticle()),

    url(r'^articles/', myapp_views.articles, name='articles'),
    url(r'^articles/(?P<id>\d+)$', myapp_views.lireUnArticle, name='lireUnArticle'),
    url(r'^lireUnArticle/(?P<id>\d+)$', myapp_views.lireUnArticle, name='lireUnArticle'),
    url(r'^addNewArticle/', myapp_views.addNewArticle, name='addNewArticle'),
    # url(r'^addNewCommentaire/', addNewCommentaire, name='addNewCommentaire'),

    url(r'^recherche/', myapp_views.recherche, name='recherche'),
    url(r'^contact/', myapp_views.contact, name='contact'),
    url(r'^mentionsLegales/', myapp_views.mentionsLegales, name='mentionsLegales'),

    url(r'^connexion_inscription/', myapp_views.connexion_inscription, name='connexion_inscription'),
    url(r'^connexion/', myapp_views.connexion, name='connexion'),
    url(r'^inscription/', myapp_views.inscription, name='inscription'),
    url(r'^deconnexion/', myapp_views.deconnexion, name='deconnexion'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]

# urlpatterns += patterns['',
#     (r'^media/(?P<path>.*)$',
#         'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#             'show_indexes': True,
#         },
#     ),
# ]