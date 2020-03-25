#!/usr/bin/env python3
#coding:utf-8
# Author: Hafid Mermouri
# Created: 09/02/2017
#
# la code ajouté et modifie par: Dung Ali Hafez  
# 08/03/2020

# maintenant on lit le texte de stdin
# ce pendenant
# elinks -dump site | python3 ./app.py   
# cat une_texte | python3 ./app.py 
# sont possible

#



import sys

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

debougage = 0  # si 1 on debougge
in_active = 1  # si 1, applis lit le texte de stdin

def _calc_ratios(texte):

    ratios = {}

    tokens = wordpunct_tokenize(texte)
    words = [word.lower() for word in tokens]

    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_words = words_set.intersection(stopwords_set)

        ratios[lang] = len(common_words)

    return ratios


def detect_language(texte):

    ratios = _calc_ratios(texte)

    premiere_langue = max(ratios, key=ratios.get)
    most_common_words = ratios[premiere_langue]
    del ratios[premiere_langue]
    deuxieme_langue = max(ratios, key=ratios.get)
    second_most_common_words = ratios[deuxieme_langue]
  
    if(debougage == 1):
      del ratios[deuxieme_langue]
      troiseme_langue = max(ratios, key=ratios.get)
      troiseme_mots = ratios[troiseme_langue]

      print("Les mots en commune sont:\n", premiere_langue, most_common_words, "\n")
      print(deuxieme_langue, second_most_common_words, "\n")
      print(troiseme_langue, troiseme_mots, "\n")      

    print("La probabilité est %s%% que la texte est écrite en %s" %(_calc_probability(most_common_words, second_most_common_words), premiere_langue))




    # Pour être satisfaisant, le niveau de probabilité doit être supérieur à 60%
def _calc_probability(most, secode_most) :
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)



if __name__=='__main__':

    # example texte en français 
    #text snipet from http://latta.blog.lemonde.fr/2017/02/08/goal-line-technology-un-nouveau-bug-contre-son-camp/
    textefr = '''
    Le match de Ligue 1 Bordeaux-Rennes, ce week-end, a été le théâtre du troisième incident significatif
    lié à l’usage de la Goal Line Technology depuis sa mise en œuvre dans divers championnats depuis deux saisons.
    La montre de l’arbitre central Sébastien Desiage a vibré à la 44e minute, indiquant que le ballon était
    entièrement entré dans la cage bordelaise au moment où le gardien Cédric Carrasso se saisissait de celui-ci,
    pourtant nettement devant la ligne de but. Sébastien Desiage a heureusement choisi d’ignorer l’alerte et de ne
    pas valider ce but virtuel, au grand soulagement du gardien des Girondins.

    '''

    
    if ( in_active == 1 ):
      texte = ""
      print("Entrez votre texte")
      for ligne in sys.stdin:
        texte += ligne
    else: 
      texte = textefr
 
    # debougage 
    if(debougage == 1):
      print(texte) 
   

    detect_language(texte)
