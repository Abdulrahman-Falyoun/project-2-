from spacy.matcher import PhraseMatcher
from TensesGrammer.Const import *
import en_core_web_md
import neuralcoref
import re
from TenseFinder.TenseParser import TenseParser

nlp = en_core_web_md.load()
nlp1 = spacy.load('en_core_web_md')
neuralcoref.add_to_pipe(nlp)
#1
def getsentencetense(doc,tense_uses):
    material_patterns = [nlp(text) for text in tense_uses]
    matcher = PhraseMatcher(nlp.vocab)
    matcher.add('tense', None, *material_patterns)
    matches = matcher(doc)
    return len(matches)!=0
# getsentencetense(doc,past_continous_uses)

#2
def getpronouns(text):
    result = re.sub(r'\'m', r' am', text)
    result = re.sub(r'\'s', r' is', result)
    result = re.sub(r'\'re', r' are', result)
    result = re.sub(r'n\'t', r' not', result)
    return(result)
# 3
def replacenounwithpronoun(text):
    verbs = re.findall(r"\((\w+)\)", text)
    text = re.sub(r'\(|\)', r'', text)
    doc = nlp('{}'.format(text))
    if len(doc._.coref_clusters)!=0:
        for pronoun in doc._.coref_clusters[0][1]:
            doc = re.sub(r'{}'.format(doc._.coref_clusters[0][0]), r'{}'.format(pronoun), str(doc))

    for verb in verbs:
        doc = re.sub(r'{}'.format(verb), r'({})'.format(verb), str(doc))
    return doc
# replacenounwithpronoun('sara has a dog and she love him')
#4
def getsubjectandverb(text):
    sentences = []
    dic = {}
    pronoun = 0
    doc = nlp1('{}'.format(text))
    sentences = re.split(r', | and | or | but | so | nor ', str(doc))
    for sent in sentences:
        verbs = re.findall(r"\((\w+)\)", sent)
        sent = re.sub(r'\(|\)', r'', sent)
        for verb in verbs:
           sent=nlp1('{}'.format(sent))
           if verb !=None:
               for word in sent:
                   if word.pos_=='PRON' and word.head.pos_ == 'VERB'and word.head.text == verb or re.search(r'{}'.format(word.text),str(pronouns))!=None and word.pos_=='PRON' and word.head.pos_ == 'NOUN'and word.head.dep_=='nsubj':
                        pronoun=word
                        break
               dic[pronoun]=verb
    return dic
# print(getsubjectandverb('she (love) traveling and She (go) abroad almost every summer'))
#5
def prepare(doc):
    doc=getpronouns(str(doc))
    doc=replacenounwithpronoun(str(doc))
    tools=getsubjectandverb(str(doc))
    dic=dict(tools)
    return dic
#6
def contexttense(text):
    sentences = re.split(r', | and | or | but | so | nor |,| ,', text)
    for sent in sentences:
        if re.search(r"\((\w+)\)", sent)!=None:
            sentences.remove(sent)

    tense_parser = TenseParser()
    if len(sentences) !=0:
       return tense_parser.find_tense_simple_form_str(sentences[0])


print(contexttense('he run a mile every day'))


