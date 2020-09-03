import logging
from TensesGrammer.Tenses import *
logging.basicConfig(level=logging.INFO)

def GrammerSolver(text):
    doc = nlp(u'{}'.format(text))
    explain=[]
    if re.search(r' before|after|until|when|while|because', text) != None:   return special_cases(text)
    for ent in doc.ents:
        if ent.label_ == 'NUM' and re.search('in {} year'.format(ent.text), text) != None:
            explain.append('Simple Future Tense')
            explain.append('here we use the future tense because we talk about future plans')
            explain.append(f'and because we use a special expression which is in year like : in {ent.label_} year')
            text,tense_explain=future(doc)
            explain = [*explain, *tense_explain]
            return text,explain
    for ent in doc.ents:
        if ent.label_ == 'DATE' and re.search('last {}'.format(ent.text), text) != None:
            explain.append('Past Simple Tense')
            explain.append('here we use the past simple tense because we talk about past memories or facts')
            explain.append(f'and because we use a special expression which is last before a date expression like : last {ent.label_ }')
            text, tense_explain = past_simple(doc)
            explain = [*explain, *tense_explain]
            return text, explain
    if re.search('in \d{4}', text) != None:
        year=re.search('in \d{4}', text)
        year=year.group(0)
        explain.append('Past Simple Tense')
        explain.append('here we use the past simple tense because we talk about past memories or facts')
        explain.append(f'and because we use a special expression which is in before a year date like : {year}')
        text, tense_explain = past_simple(doc)
        explain = [*explain, *tense_explain]
        return text, explain
    if re.search('on \d{4}', text) != None:
        year=re.search('on \d{4}', text)
        year=year.group(0)
        explain.append('Past Simple Tense')
        explain.append('here we use the past simple tense because we talk about past memories or facts')
        explain.append(f'and because we use a special expression which is in before a year date like : {year}')
        text, tense_explain = past_simple(doc)
        explain = [*explain, *tense_explain]
        return text, explain
    if re.search('by \d{4}', text) != None:
        year = re.search('by \d{4}', text)
        year = year.group(0)
        explain.append('Past Perfect Tense')
        explain.append('here we use the past perfect tense because we talk about past ')
        explain.append(f'and because we use a special expression which is by before a year date like : {year}')
        text, tense_explain = past_perfect(doc)
        explain = [*explain, *tense_explain]
        return text, explain
    # if re.search('pm|am', text) != None:
    #     time = re.search('by \d{4}', text)
    #     # time = time.group(0)
    #     explain.append('here we use the past continuous tense because we talk about past continuous actions')
    #     explain.append(f'and because we use a special expression which is in before a year date like : {time}')
    #     text, tense_explain = past_continuous(doc)
    #     explain = [*explain, *tense_explain]
    #     return text, explain
    for t in tenses:
        if (getsentencetense(doc, t['uses'])):
            explain.append('if we find in the sentence a uses for a special tense')
            explain.append('we use that tense')
            return t['fun'](doc)

    for tense in tensesFinder:
            sentencetense=contexttense(str(doc))
            explain.append(f'{sentencetense}')
            explain.append(f'from the context of the sentence we realize that the tense is {sentencetense}')
            if (getsentencetense(nlp(sentencetense), tense['uses'])):
                return tense['fun'](doc)
    return (present_simple(doc))

# print(GrammerSolver('she (visit) paris three times'))
# print(GrammerSolver('I (study) since three oclock'))
# print(GrammerSolver('they (interview) people all week'))
# print(GrammerSolver('I (watch) a film before I (go) to bed'))
# print(GrammerSolver('by 1980 , they (travel) to Canada'))
# print(GrammerSolver('I (see) him when he (finish) work'))
# print(GrammerSolver('I sometimes (go) out with my friends'))
# print(GrammerSolver('sand gazelles (live) in the desert , they are wild animals'))
# print(GrammerSolver('yesterday, I (watch) a football match'))
# print(GrammerSolver('I (stay) at home tomorrow'))
# print(GrammerSolver('they ignored the warnings that other climbers (give) them'))
# print(GrammerSolver('I recevied a letter from sara , she (promise) to write since a long time'))
# print(GrammerSolver('everyday I (do) the shopping for mam'))
# print(GrammerSolver('Adam (work) daily in their family shop,he is a hardwork person'))
# print(GrammerSolver('I (spend) all afternoon fixing my computer'))
# print(GrammerSolver('my uncle finally passed his test , he (take) it three times'))

print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

# print(GrammerSolver('the police sergeant (interview) two people so far today'))
# print(GrammerSolver('the detectives (interview) people all week'))
# print(GrammerSolver('jack (study) law and history for four years'))
# print(GrammerSolver('sara (write) an essay all morning she was good at it'))
# print(GrammerSolver('I (play) the piano since I was 13'))
# print(GrammerSolver('she just (be) shopping'))
# print(GrammerSolver('Adam just (come) out of the sea , he (swim) with his friends'))
# print(GrammerSolver('he just (finish) work,he (start) since 8 oclock this morning'))
# print(GrammerSolver('they (celebrate) sameras graduation'))
# print(GrammerSolver('I (pass) my exam test and I (have) interviews for university place'))
# print(GrammerSolver('I (start) learning the mizmar but I only (play) for a few weeks'))
# print(GrammerSolver('we just (come) back from lattakia'))
# print(GrammerSolver('I (sort) out my bedroom cupboards all morning'))
# print(GrammerSolver('in 1854 , people of irlend , they (emigrate) abroad'))
# print(GrammerSolver('by 1854 , people of irlend , they (emigrate) abroad'))
# print(GrammerSolver('irish people emigrated because they (die) of starvation'))
# print(GrammerSolver('sara did not feel very confident about talking her driving test ,she (fail) twice'))
# print(GrammerSolver('it (be) one of the most destructive earthquakes of the 20th century'))
# print(GrammerSolver('the earthquake that hit Agadir,(last) only seconds ,it was a disaster'))

# print(GrammerSolver('in 1960 ,the city (be) evacuated , it was empty'))
# print(GrammerSolver('they (move) 3km south while it (build)'))
# print(GrammerSolver('while they (move) 3km south, it (build)'))
# print(GrammerSolver('my father helped to run an engineering film that (build) bridges , he made a masterpiece'))
# print(GrammerSolver('it was difficult to be a way from home but we (work) hard to fit it'))
# print(contexttense('it was difficult to be a way from home'))
# print(GrammerSolver('we went to a school and we (attend) to school with children from all the world'))
# print(GrammerSolver('my family returned from england but they (learn) so much about a new culture'))
# print(GrammerSolver('last year,I (spend) two months in china'))

# print(GrammerSolver('I went to the doctor this morning, I (feel) ill'))
# print(GrammerSolver('I (feel) ill during the night'))
# print(GrammerSolver('I (dream) about visiting china for many years'))
# print(GrammerSolver('my father retired last year,he (work) to the same company all his life'))
# print(GrammerSolver('he (look) to find work for two weeks and yesterday he was offered two jops'))

# print(GrammerSolver('it was a clean place because they (clean) all their streets'))
# print(GrammerSolver('the people were angry , so they (call) the mayer'))
# print(GrammerSolver('I (visit) cairo before I (visit) damascus'))
# print(GrammerSolver('in 2000 , they (move) to Australia'))
# print(GrammerSolver('I (know) him since 2000'))
# print(GrammerSolver('people (move) from one country to another , they (choose) to emigrate while they (have) to move from wars'))
# print(GrammerSolver('in recent years it (increase) sharply while in other part of world it (decrease)'))

# print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')

