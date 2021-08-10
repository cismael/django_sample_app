# views.py
# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
# from django.core.context_processors import csrf

from django.db.models import Q
from django.core.mail import EmailMessage
from django.contrib.syndication.views import Feed

from monblog.forms import ConnexionForm
from monblog.forms import InscriptionForm
from monblog.forms import ContactForm
from monblog.forms import AddNewArticleForm
from monblog.forms import AddNewCommentaireForm
from monblog.forms import RechercheForm

from monblog.models import Article
from monblog.models import Commentaire
from monblog.models import Contact


def accueil(request):
    dernierArticle = Article.objects.order_by('-date')[0]
    article_list = Article.objects.order_by('date')
    article_total = len(article_list)
    
    envoi = False
    if request.method == 'POST':
        form = AddNewCommentaireForm(request.POST) 
        if form.is_valid():
            texteDuCommentaire = form.cleaned_data['texteDuCommentaire']
            user = request.user.username
            article_id = request.POST['article_id']
            article = Article.objects.get(id=article_id)
            com = Commentaire(auteurDuCommentaire=user, texteDuCommentaire=texteDuCommentaire, article=article)
            com.save()
            form = AddNewCommentaireForm()
            envoi = True
    else: 
        form = AddNewCommentaireForm()

    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'base.html', {'form': form, 'article_dernier': dernierArticle, 'total': article_total, 'les_commentaires': dernierArticle, 'user_is_logged': user_is_logged})


def articles(request):
    articles = Article.objects.order_by('-date')
    # articles = Article.objects.all()
    envoi = False
    if request.method == 'POST':
        form = AddNewCommentaireForm(request.POST) 
        if form.is_valid():
            texteDuCommentaire = form.cleaned_data['texteDuCommentaire']
            user = request.user.username
            article_id = request.POST['article_id']
            article = Article.objects.get(id=article_id)
            com = Commentaire(auteurDuCommentaire=user, texteDuCommentaire=texteDuCommentaire, article=article)
            com.save()
            form = AddNewCommentaireForm()
            envoi = True
    else: 
        form = AddNewCommentaireForm()

    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'articles.html', {'form': form, 'liste_des_articles': articles, 'user_is_logged': user_is_logged})


def lireUnArticle(request, id):
    article = Article.objects.get(id=id)
    if article:
        article_exist = True
    else:
        article_exist = False
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True

    envoi = False
    if request.method == 'POST':
        form = AddNewCommentaireForm(request.POST) 
        if form.is_valid():
            texteDuCommentaire = form.cleaned_data['texteDuCommentaire']
            user = request.user.username
            # article_id = request.POST['article_id']
            article = Article.objects.get(id=id)
            com = Commentaire(auteurDuCommentaire=user, texteDuCommentaire=texteDuCommentaire, article=article)
            com.save()
            form = AddNewCommentaireForm()
            envoi = True
    else: 
        form = AddNewCommentaireForm()
    return render(request, 'lireUnArticle.html', {'form': form, 'article': article, 'article_exist': article_exist, 'user_is_logged': user_is_logged})


@login_required(login_url='/connexion')
def addNewArticle(request):
    envoi = False
    if request.method == 'POST':
        form = AddNewArticleForm(request.POST) 
        if form.is_valid():
            titre = form.cleaned_data['titre']
            auteur = request.user.username
            contenu = form.cleaned_data['contenu']
            art = Article(titre=titre, auteur=auteur, contenu=contenu)
            art.save()
            form = AddNewArticleForm()
            envoi = True
    else: 
        form = AddNewArticleForm()
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'addNewArticle.html', {'form': form, 'envoi': envoi, 'user_is_logged': user_is_logged})


def recherche(request):
    user_is_logged = ''
    cleDeTri = ''
    articles = '' 
    article_total = ''
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = RechercheForm(request.POST) 
        if form.is_valid():
            recherche = form.cleaned_data['recherche']
            Type = form.cleaned_data['Type']
            Cle = form.cleaned_data['Cle']
            if Type == 'select1':
                articles = Article.objects.filter(Q(titre__contains=recherche) | Q(auteur__contains=recherche) | Q(contenu__contains=recherche)).order_by('-date')
                article_total = len(articles)
                form = RechercheForm()
            if Type == 'select2':
                # Si l'utilisateur n'a pas choisi de clé de tri, on trie par date par défaut
                if Cle == '':
                    cleDeTri = 'date'
                else:
                    cleDeTri = Cle # Sinon on tri selon la clé renseignée par l'utilisateur
                # Maintenant ou crée la requête SQL
                debutQuery = "SELECT * FROM monblog_article"
                debutQuery += " WHERE titre LIKE " + "'%%" + recherche +  "%%'"
                debutQuery += " OR auteur LIKE " + "'%%" + recherche +  "%%'"
                debutQuery += " OR contenu LIKE " + "'%%" + recherche +  "%%'"
                debutQuery += " ORDER BY "
                finQuery = " DESC"
                articles = Article.objects.raw(debutQuery+cleDeTri+finQuery)
                # print articles.query
                article_total = len(list(articles))
                form = RechercheForm()
    else: 
        form = RechercheForm()
    if articles:
        results = True
    else:
        results = False

    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'recherche.html', {'form': form, 'results': results, 'liste_des_articles': articles, 'total': article_total, 'titre': "Les articles", 'user_is_logged': user_is_logged})


def contact(request):
    envoi = False
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            contact = Contact()
            email = EmailMessage(sujet, message, envoyeur)
            email.send()
            envoi = True
            form = ContactForm()
    else: 
        form = ContactForm()
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'contact.html', {'form': form, 'envoi': envoi, 'user_is_logged': user_is_logged})


def mentionsLegales(request):
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'mentionsLegales.html', {'titre': "Les articles", 'user_is_logged': user_is_logged})


def connexion_inscription(request):
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'connexion_inscription.html', {'titre': "Page De Connexion", 'user_is_logged': user_is_logged})


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', { 'form': form, 'titre': "Page D'Inscription", 'error': error})


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            passwordConfirm = form.cleaned_data['passwordConfirm']
            # On crée l'utilisateur
            if password == passwordConfirm:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                # envoi = True
            # else envoi = False
                user = authenticate(username=username, password=password)  # on vérifie si les données sont correctes
                if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # on connecte l'utilisateur
                else: # sinon une erreur sera affichée
                    error = True
    else: 
        form = InscriptionForm()  # On crée un formulaire vide
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'inscription.html', {'form': form, 'titre': "Page D'Inscription", 'user_is_logged': user_is_logged})


def deconnexion(request):
    auth.logout(request)
    request.session.flush()
    # request.user = AnonymousUser
    user_is_logged = False
    if request.user.is_authenticated:
        user_is_logged = True
    return render(request, 'base.html', {'titre': "Page De Déconnexion", 'user_is_logged': user_is_logged})
