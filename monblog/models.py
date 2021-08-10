# models.py
# -*- coding: utf-8 -*-

from django.db import models


class Article(models.Model):
    titre = models.CharField(max_length=150)
    auteur = models.CharField(max_length=55)
    contenu = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    def __str__(self):
        return u'%s' % self.titre
    class Meta:
        ordering = ['-date']
    # def get_absolute_url(self):
    #         return ('/articles/', (), {})

class Commentaire(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    auteurDuCommentaire = models.CharField(max_length=55)
    texteDuCommentaire = models.CharField(max_length=500)
    dateCommentaire = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    def __str__(self):
        return u'%s' % self.texteDuCommentaire
    class Meta:
        ordering = ['-dateCommentaire']


class Contact(models.Model):
    sujet = models.CharField(max_length=100)
    message = models.CharField(max_length=1500)
    envoyeur = models.EmailField(max_length=200)
    def __str__(self):
	    return u'%s' % self.sujet
