# nltk-language-detection
# English below
# la code ajouté et modifie par: Dung Ali Hafez
Verrez la cette site:
https://www.le-geek.com/detection-de-langue-en-nlp-natural-language-processing/

##  
# maintenant on lit le texte de stdin
# ce pendenant
# elinks -dump site | python3 ./app.py 
# cat app.py | python3 ./app.py
# sont possible
#
#
#  
# Bug: texte_dans une langue pas supporte
# 17/03/2020
# nltk package recoginize pas les langues comme Japonais, Chinois, Vietnamienne...
# comme vous pouvez voir avec index.nginx-japonais dans le dossier examples il détécte langue anglais même
# si le fichier était écrit en Japonais.
# example: cat examples/texte_coreen.txt | python3 ./app.py 
#
# détecte que le texte est écrite en langue anglais et pas en coréen
#


[![N|Solid](http://www.le-geek.com/wp-content/uploads/2017/02/geek.png)](https://www.le-geek.com/)

Automatic detection of text language with Python and NLTK.
This script uses a very simple approach based on stopwords comparaison. The stopwords list with the most commun words wins the association.
## Dependencies
you have to install [NLTK package](http://www.nltk.org/api/nltk.html) for Python to run this script.

## How it works
just give the script a brunch of text to analyse and the script will :
  - Parse and tokenize you text
  - Compare the tokens with all stopwords lists contained in NLTK corpus in all available languages
  - Select the most relevant language
  - Calculate the relevancy level of the selected language

## Documentation
If you want to know how this script works, just have a look at this blog post titled [Detection de langue en NLP](https://www.le-geek.com/detection-de-langue-en-nlp-natural-language-processing/) i wrote (in french) on my personnal blog [le-geek.com](https://www.le-geek.com/)
