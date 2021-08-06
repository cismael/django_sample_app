# forms.py
# -*- coding: utf-8 -*-

from django import forms

class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sujet du mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Contenu de votre message...'}))
    envoyeur = forms.EmailField(label="Votre adresse mail", widget=forms.TextInput(attrs={'placeholder': 'xyz@example.com'}))
    

class AddNewArticleForm(forms.Form):
    titre = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': "Titre de l'article"}))
    contenu = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder': "Contenu de l'article..."}))


class AddNewCommentaireForm(forms.Form):
    texteDuCommentaire = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': "Laisser un commentaire"}))


class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    email = forms.EmailField(label="Votre adresse mail", widget=forms.TextInput(attrs={'placeholder': 'xyz@example.com'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    passwordConfirm = forms.CharField(label="Confirmation Mot de passe", widget=forms.PasswordInput(attrs={'placeholder': 'Confirmation du mot de passe'}))


choix=[('select1',"Cochez pour faire une recherche normale (titres d'article, auteurs ou contenus)"),
         ('select2','Cochez pour faire une recherche RAW SQL (une clé de tri est OBLIGATOIRE)')
      ]

choix2=[('',"Choisir (Optionnel)"),
        ('titre',"Trier les articles par titre"),
        ('auteur','Trier les articles par auteur'),
        ('contenu','Trier les articles par contenu'),
        ('date','Trier les articles par date')
      ]

class RechercheForm(forms.Form):
    recherche = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Article à rechercher"}))
    Type = forms.ChoiceField(choices=choix, widget=forms.RadioSelect())
    Cle = forms.ChoiceField(choices=choix2, required=False)

