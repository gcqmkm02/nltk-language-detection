#!/usr/bin/env python3
#coding:utf-8
# Author: Hafid Mermouri
# Created: 09/02/2017

import sys

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def _calc_ratios(text):

    ratios = {}

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_words = words_set.intersection(stopwords_set)

        ratios[lang] = len(common_words)

    return ratios


def detect_language(text):

    ratios = _calc_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)
    most_common_words = ratios[most_rated_language]
    del ratios[most_rated_language]
    second_most_rated_language = max(ratios, key=ratios.get)
    second_most_common_words = ratios[second_most_rated_language]


    print("La probabilité est %s%% que le texte est écrite en %s" %(_calc_probability(most_common_words, second_most_common_words), most_rated_language))


def _calc_probability(most, secode_most) :
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)

if __name__=='__main__':

    #text snipet from http://latta.blog.lemonde.fr/2017/02/08/goal-line-technology-un-nouveau-bug-contre-son-camp/
    #text = '''
    #Многие дистрибутивы Linux включают Thunderbird по умолчанию и большинство из них имеют систему управления пакетами (менеджер пакетов), которая позволяет вам легко установить Thunderbird. Как правило, вы должны использовать систему управления пакетами, потому что это позволит:
    #'''

    text = '''
    Многие дистрибутивы Linux включают по умолчанию и большинство из них имеют систему управления пакетами (менеджер пакетов), которая позволяет вам легко установить. Как правило, вы должны использовать систему управления пакетами, потому что это позволит:
    '''

    detect_language(text)
