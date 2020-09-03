from TensesGrammer.Const import *
import re


def verb_ing(token):
    if re.search(r' {} '.format(token),str(non_continuous_verb))!=None: return token
    #special case
    if re.search(r' {} '.format(token),str(special_verbs))!=None: return token+"ing"
    #lie-->lying
    if token[-2:]=='ie': return token[:-2] +'ying'
    # live --> living
    if token[-1]=='e': return token[:-1]+"ing"
    #fix --> fixing, enjoy --> enjoying, snow --> snowing
    if token[-1] in ['w','x','y'] and token[-2] in str(vowel): return token + "ing"
    #stop-->stopping
    if token[-2] in ["u",'o','i','a']: return token +token[-1]+"ing"
    return token +'ing'
# print(verb_ing('play'))

def verb_s(token):
    if token[-1]=='y' and re.search(token[-2],str(vowel)) != None: return token+"s"
    #cry --> cries
    if token[-1]=='y':return token[:-1]+"ies"
    #watch --> watches, guess --> guesses, mix --> mixes
    if token[-2:]in ['ss','ch','zz','sh'] or token[-1] in['x','o'] or token[-3:]=="tch" : return token+"es"
    if token.lower()=='have': return "has"
    if token.lower()=='be':  return "is"
    return token+"s"
# verb_s('play')

def verb_ed(token):
    #play-->played , box-->boxed ,row-->rowed
    if token[-1] in ['w','x','y']  and re.search(token[-2],str(vowel)) != None: return token +"ed"
    #study-->studied
    if token[-1]=='y' and re.search(token[-2],str(consonant)) != None: return token[:-1]+"ied"
    #arrive-->arrived
    if token[-1]=='e': return token +"d"
    #stop-->stopped
    if re.search(token[-1],str(consonant))!= None and re.search(token[-2],str(vowel)) != None: return token + token[-1]+'ed'
    #have,has-->had
    if token.lower()=='have' or token.lower()=='has': return "had"
    return token +"ed"
# verb_ed('arrive')