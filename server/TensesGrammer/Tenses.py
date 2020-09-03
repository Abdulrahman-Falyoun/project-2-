from TensesGrammer.Verbs import *
from TensesGrammer.PrepareFunction import *

def present_simple(doc):
    explain=['Present Simple Tense']
    explain.append('because it is present simple we use the verb 1')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        if re.search(r'{}'.format(i),'he she it') != None:
            explain.append(f'if the subject is he or she or it or relevance of these subjects we use the verb-s to become {verb_s(verb)}');
            explain.append('remember that we add s to regular verbs in the present tense and the subject must be singular ');
            doc = re.sub(r'{}'.format(verb), r'{}'.format(verb_s(verb)), str(doc))
        elif re.search(r'{}'.format(i),'I') != None and verb=='be':
            explain.append('if the subject is I or relevance of it and verb is be then the auxiliary verb is am so the object and subject become ==>  I am ');
            dic[i]='am'
        elif verb=='be':
            explain.append(' the verb we want to convert  is be and we want to convert it to the present simple tense ==> are');
            dic[i]='are'
        doc = re.sub(r'\(|\)',r'',str(doc))
    return doc,explain
# print(present_simple('she (play) games always'))
def past_simple(doc):
    explain = ['Past Simple Tense']
    explain.append('because it is past simple we use the verb 2')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        if re.search(r"{}".format(verb), str(unregular_verbs)) != None:
            explain.append('here our varb is  unregular verb ')
            explain.append('in unregular verbs we dont use the verb-ed ')
            explain.append('then we get its verb 2 from the unregular verbs list')
            verb = re.search(r"{}".format(verb), str(unregular_verbs))
            verb=verb.group(0)
            for k,v in dict_v2.items():
                if k==verb:
                    dic[i]=v
                    explain.append(f'{v}')
                    doc = re.sub(r'{}'.format(verb), r'{}'.format(dic[i]), str(doc))
                    doc = re.sub(r'\(|\)',r'',str(doc))
                else:
                    pass
        elif(verb=='be' and  re.search(r'{}'.format(i),'he she it He She It') != None ):
            explain.append('if our verb is be and the subject is he or she or it or its relevence')
            dic[i]='was'
        elif (verb == 'be' and re.search(r'{}'.format(i), 'I we We You you they They') != None):
            explain.append('if our verb is be and the subject is I or we or you or they or its relevence')
            dic[i] = 'were'
        else:
            explain.append('here is you notice the verb is not a unregular verb')
            explain.append('so we use the verb-ed whatever the subject is')
            explain.append(f'{verb_ed(verb)}')
            dic[i]=verb_ed(verb)
            doc = re.sub(r'{}'.format(verb), r'{}'.format(dic[i]), str(doc))
            doc = re.sub(r'\(|\)',r'',str(doc))
    return doc,explain
# print(past_simple('adam (win) another prize in 1999 and he is very proud '))
def present_perfect(doc):
    explain=['Present Perfect Tense']
    explain.append('as you notice the tense is present perfect so we use auxiliary verbs like has have')
    explain.append('and because it is perfect we use the verb 3 ')
    dic = prepare(doc)
    for i in dic:
        verb = dic[i]
        if re.search(r"{}".format(verb), str(unregular_verbs)) != None:
            explain.append('here our varb is  unregular verb ')
            explain.append('in unregular verbs we dont add ed in the end of the verb ')
            explain.append('then we get its verb 3 from the unregular verbs list')
            verb = re.search(r"{}".format(verb), str(unregular_verbs))
            verb = verb.group(0)
            for k, v in dict_v2.items():
                if k == verb:
                    v2 = v
                    for k_1, v_1 in dict_v3.items():
                        if k_1 == v2:
                            dic[i] = v_1
                            if re.search(r'{}'.format(i), ' he she it He She It ') != None:
                                explain.append('if our subject is he or she or it or its relevence we use has ')
                                explain.append(f'has {dic[i]}')
                                doc = re.sub(r'{}'.format(verb), r'has {}'.format(dic[i]), str(doc))
                                doc = re.sub(r'\(|\)', r'', str(doc))
                            else:
                                explain.append('if our subject is we or they or you or I or its relevence we use heve ')
                                explain.append(f'have {dic[i]}')
                                doc = re.sub(r'{}'.format(verb), r'have {}'.format(dic[i]), str(doc))
                                doc = re.sub(r'\(|\)', r'', str(doc))
                        else:
                            pass
        else:
            explain.append('here as you notice the verb is a regular verb')
            explain.append('so we add ed in the end of the verb whatever the subject is')
            dic[i] = verb_ed(verb)
            if re.search(r'{}'.format(i), 'he she it I') != None:
                explain.append('if our subject is he or she or it or I or its relevence we use has ')
                doc = re.sub(r'{}'.format(verb), r'has {}'.format(dic[i]), str(doc))
                doc = re.sub(r'\(|\)', r'', str(doc))
            else:
                explain.append('if our subject is we or they or you or its relevence we use heve ')
                doc = re.sub(r'{}'.format(verb), r'have {}'.format(dic[i]), str(doc))
                doc = re.sub(r'\(|\)', r'', str(doc))

    return doc,explain
# print(present_perfect('She (go) abroad just'))
def present_continuous(doc):
    explain=['Present Continuous Tense']
    explain.append('as you notice the tense is present continuous so we use auxiliary verbs like am is are')
    explain.append('and because it is continuous we use the verb-ing')
    dic = prepare(doc)
    for i in dic:
        verb = dic[i]
        if re.search(r'{}'.format(i), 'he she it') != None:
            explain.append('if our subject is he or she or it  or its relevence we use is ')
            explain.append(f'is {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'is {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)', r'', str(doc))

        elif re.search(r'{}'.format(i), ' they we you I') != None:
            explain.append('if our subject is we or they or you or I or its relevence we use are ')
            explain.append(f'are {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'are {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)', r'', str(doc))

        else:
            explain.append('if our subject is I we use am ')
            explain.append(f'am {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'am {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)', r'', str(doc))

    return doc,explain
# print(present_continuous('I (drink) my tea now'))
def past_continuous(doc):
    explain = ['Past Continuous Tense']
    explain.append('as you notice the tense is past continuous so we use auxiliary verbs like was were')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        if re.search(r'{}'.format(i),'he she it')!=None:
            explain.append('if our subject is he or she or it or its relevence we use was ')
            explain.append(f'was {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'was {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)',r'',str(doc))
        else:
            explain.append('if our subject is we or they or you or I or its relevence we use were ')
            explain.append(f'were {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'were {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)',r'',str(doc))

    return doc,explain
# print(past_continuous('Sara (write) an essay all morning '))
def past_perfect(doc):
    explain=['Past Perfect Tense']
    explain.append('as you notice the tense is past perfect so we use auxiliary verbs like had')
    explain.append('and because it is perfect we use the verb 3 ')
    dic = prepare(doc)
    for i in dic:
        verb = dic[i]
        if re.search(r"{}".format(verb), str(unregular_verbs)) != None:
            explain.append('here our varb is  unregular verb ')
            explain.append('in unregular verbs we dont add ed in the end of the verb ')
            explain.append('then we get its verb 3 from the unregular verbs list')
            verb = re.search(r"{}".format(verb), str(unregular_verbs))
            verb = verb.group(0)
            for k, v in dict_v2.items():
                if k == verb:
                    v2 = v
                    for k_1, v_1 in dict_v3.items():
                        if k_1 == v2:
                            dic[i] = v_1
                            explain.append(' we use had whatever the subject is because it is past tense')
                            explain.append(f'had {dic[i]}')
                            doc = re.sub(r'{}'.format(verb), r'had {}'.format(dic[i]), str(doc))
                            doc = re.sub(r'\(|\)', r'', str(doc))
                        else:
                            pass
        else:
            explain.append('here as you notice the verb is a regular verb')
            explain.append('so we use the verb-ed whatever the subject is because it is past tense')
            dic[i] = verb_ed(verb)
            explain.append(' we use had whatever the subject is')
            explain.append(f'had {dic[i]}')
            doc = re.sub(r'{}'.format(verb), r'had {}'.format(dic[i]), str(doc))
            doc = re.sub(r'\(|\)', r'', str(doc))

    return doc,explain
# print(past_perfect('I (finish) '))
def future(doc):
    explain=['Future Tense']
    explain.append('in the future tense we use verb-0')
    explain.append('because it is future tense we add will before the verb which is a verb-0')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        explain.append(f'will {verb}')
        doc = re.sub(r'{}'.format(verb), r'will {}'.format(verb), str(doc))
        doc = re.sub(r'\(|\)',r'',str(doc))
    return doc,explain
# future('i (sing) another new song soon')
def continuous_future(doc):
    explain=['Continuous Future Tense']
    explain.append('because it is future tense we add will be before the verb')
    explain.append('because it is continuous we use the verb-ing ')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        verb=verb
        explain.append(f'will be {verb_ing(dic[i])}')
        doc = re.sub(r'{}'.format(verb), r'will be {}'.format(verb_ing(dic[i])), str(doc))
        doc = re.sub(r'\(|\)',r'',str(doc))
    return doc,explain
# continuous_future('i (sing) another new song soon')
def perfect_future(doc):
    explain = ['Perfect Future Tense']
    explain.append('because it is perfect future tense we add will have before the verb')
    explain.append('because it is perfect we use the verb 3 ')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        if re.search(r"{}".format(verb), str(unregular_verbs)) != None:
            explain.append('here our varb is  unregular verb ')
            explain.append('in unregular verbs we dont use the verb-ed')
            explain.append('then we get its verb 3 from the unregular verbs list')
            verb = re.search(r"{}".format(verb), str(unregular_verbs))
            verb=verb.group(0)
            for k,v in dict_v2.items():
                if k==verb:
                    v2=v
                    for k_1,v_1 in dict_v3.items():
                        if k_1==v2:
                            dic[i]=v_1
                            explain.append('also we add will have before the verb3')
                            explain.append(f'will have {dic[i]}')
                            doc = re.sub(r'{}'.format(verb), r'will have {}'.format(dic[i]), str(doc))
                            doc = re.sub(r'\(|\)',r'',str(doc))
                        else:
                            pass
        else:
            explain.append('here as you notice the verb is a regular verb')
            explain.append('so we add ed in the end of the verb whatever the subject is')
            explain.append('also we add will have before the verb3')
            explain.append(f'will have {verb_ed(verb)}')
            dic[i]=verb_ed(verb)
            doc = re.sub(r'{}'.format(verb), r'will have {}'.format(dic[i]), str(doc))
            doc = re.sub(r'\(|\)',r'',str(doc))
    return doc,explain
# print(perfect_future('i (write) another new song soon'))
def Present_perfect_continuous(doc):
    explain = ['Present Perfect Continuous Tense']
    explain.append('as you notice the tense is present so we use auxiliary verbs like has have')
    explain.append('also because it is perfect we use the been')
    explain.append('also because it is continuous we use the verb-ing ')
    dic=prepare(doc)
    for i in dic:
        verb=dic[i]
        if re.search(r'{}'.format(i),' he she it ')!=None:
            explain.append('if our subject is he or she or it or I or its relevence we use has been ')
            explain.append(f'has been {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'has been {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)',r'',str(doc))
        else:
            explain.append('if our subject is we or they or you or its relevence we use heve ')
            explain.append(f'have been {verb_ing(dic[i])}')
            doc = re.sub(r'{}'.format(verb), r'have been {}'.format(verb_ing(dic[i])), str(doc))
            doc = re.sub(r'\(|\)',r'',str(doc))

    return doc,explain
# Present_perfect_continuous('I (work) for this company for more than thirty year')
def Past_perfect_continuous(doc):
    explain = ['Past Perfect Continuous Tense']
    explain.append('as you notice the tense is past so we use auxiliary verbs like had')
    explain.append('also because it is perfect we use the been')
    explain.append('also because it is continuous we use the verb-ing ')
    dic = prepare(doc)
    for i in dic:
        explain.append('also we add had because it is a past tense whatever the subject is')
        explain.append('so we add had been before the verb-ing')
        explain.append(f'had been {verb_ing(dic[i])}')
        doc = re.sub(r'{}'.format(dic[i]), r'had been {}'.format(verb_ing(dic[i])), str(doc))
        doc = re.sub(r'\(|\)', r'', str(doc))

    return doc,explain
# Past_perfect_continuous('I (sing) another new song soon')


tenses = [
    {
        "uses": ["in the present", "every", "sometimes", "always", "often", "usually", "seldom", "never", "normally",
                 "traditionally", "now"],
        "fun": present_simple
    },
    {
        "uses": ["in the past", "yesterday", "ago", "the other day","century","decade","last year",
                 "last month","last day","last week","last hour","last minute","last second"],
        "fun": past_simple
    },
    {
        "uses": ["soon", "in the future", "in one year", "in a year", "in year"],
        "fun": future
    },
    {
        "uses": ["at the moment", "look!", "listen!", " next week ", " next month ", " next year ", "next day ",
                 "permanently", "regularly","tomorrow"],
        "fun": present_continuous
    },
    {
        "uses": ["by this time tomorrow", "by this time next week", "by this time next year",
                 "by this time month","at this time tomorrow", "at this time next month",
                 "at this time next year","at this time next week", "by 3 o’clock tomorrow",
                 "by this time next summer", "by this time next autumn","by this time next winter",
                 "by this time next spring","at this time next summer","at this time next autumn",
                 "at this time next winter" ,"at this time next spring"
],
        "fun": continuous_future
    },
    {
        "uses": [
            "by the end of this year", "by the end of tomorrow", "by the end of this term", "by the end of this week",
            "by the end of this month", "by the end of this day",
            "in another years ", "in another months", "in another days", "in another weeks"
        ],
        "fun": perfect_future
    },
{
        "uses": [
            "just", "yet", "never", "ever", "already", "so far", "up to now", "recently", "today",
            "this week", "this month", "this year", "this day", "lately", "once", "twice", "many times",
            "several times","times","this minute","this hour","this second"],
        "fun": present_perfect
    },
    {
        "uses": ["as long as", "during", "all the night", "at night", "all the afternoon","all the evening",
                 "all the morning","all morning", "all night", "all afternoon","all morning","all evening"],
        "fun": past_continuous
    },

    {
        "uses": [
            "already", "by the time", "as soon as", 'by the end of the year',
            "by the end of the month", "by the end of the week", "by the end of the day"
        ],
        "fun": past_perfect
    },
    {
        "uses": ["all day","all the day", "all night","all the night", "all week",
                 "all the week", "still","all year" , "all the year"],
        "fun": Past_perfect_continuous
    },
    {
        "uses": ['for', 'since'],
        "fun": Present_perfect_continuous
    }

]

tensesFinder = [
    {
        "uses": ['SimplePresent','SimplePresentModal_One','SimplePresentModal_Two'],
        "fun": present_simple
    },
    {
        "uses": ['SimplePast'],
        "fun": past_simple
    },
    {
        "uses": ['SimpleFuture'],
        "fun": future
    },
    {
        "uses": ['PresentContinuous'],
        "fun": present_continuous
    },
    {
        "uses": ['FutureContinuous'],
        "fun": continuous_future
    },
    {
        "uses": ['FuturePerfect'],
        "fun": perfect_future
    },
{
        "uses": ['PresentPerfect'],
        "fun": present_perfect
    },
    {
        "uses": ['PastContinuous'],
        "fun": past_continuous
    },

    {
        "uses": ['PastPerfect'],
        "fun": past_perfect
    },
    {
        "uses": ['PastPerfectContinuous'],
        "fun": Past_perfect_continuous
    },
    {
        "uses": ['PresentPerfectContinuous'],
        "fun": Present_perfect_continuous
    }

]

def special_cases(doc):
    sents = []
    explain=[]
    u = re.search(r'until', str(doc))
    a = re.search(r'after', str(doc))
    b = re.search(r'before', str(doc))
    when = re.search(r'when', str(doc))
    wh = re.search(r'while', str(doc))
    be = re.search(r'because', str(doc))

    explain=[f'special words cases']
    if u != None:
        explain.append('as you notice here we observe a special word case which is the word until ')
        explain.append('until is word that connect two sentence')
        explain.append('the first sentence must be in a past perfect tense')
        explain.append('the second sentence must be in a past simple tense')
        sents = re.split(r'(until)', str(doc))
        firstsentence, arr1 =past_perfect(nlp(sents[0])) if re.findall(r"\((\w+)\)", sents[0]) != None else sents[0]
        arr1.insert(1, firstsentence)
        secondsentence, arr2 = past_simple(nlp(sents[2])) if re.findall(r"\((\w+)\)", sents[2]) != None else sents[2]
        arr2.insert(1, secondsentence)
        explain = [*explain, *arr1, *arr2]
        text = f'{firstsentence} until {secondsentence}'
        return text,explain
    if a != None:
        explain.append('as you notice here we observe a special word case which is the word after ')
        explain.append('after is word that connect to sentence')
        explain.append('the first sentence must be in a past simple tense')
        explain.append('the second sentence must be in a past perfect tense')
        sents = re.split(r'(after)', str(doc))
        firstsentence, arr1 = past_simple(nlp(sents[0])) if re.findall(r"\((\w+)\)", sents[0]) != None else sents[0]
        arr1.insert(1, firstsentence)
        secondsentence, arr2 = past_perfect(nlp(sents[2])) if re.findall(r"\((\w+)\)", sents[2]) != None else sents[2]
        arr2.insert(1, secondsentence)
        explain = [*explain, *arr1, *arr2]
        text = f'{firstsentence} after {secondsentence}'
        return text,explain
    if b != None:
        explain.append('as you notice here we observe a special word case which is the word before ')
        explain.append('before is word that connect two sentence')
        explain.append('the first sentence must be in a future tense')
        explain.append('the second sentence must be in a present simple tense')
        sents = re.split(r'(before)', str(doc))
        firstsentence, arr1 = future(nlp(sents[0])) if re.findall(r"\((\w+)\)", sents[0]) != None else sents[0]
        arr1.insert(1, firstsentence)
        secondsentence, arr2 = present_simple(nlp(sents[2])) if re.findall(r"\((\w+)\)", sents[2]) != None else sents[2]
        arr2.insert(1, secondsentence)
        explain = [*explain, *arr1, *arr2]
        text = f'{firstsentence} before {secondsentence}'
        return text,explain
    if when != None:
        explain.append('as you notice here we observe a special word case which is the word when ')
        explain.append('when is word that connect two sentence')
        explain.append('the first sentence must be in a past perfect continuous tense')
        explain.append('the second sentence must be in a past continuous tense')
        sents = re.split(r'(when)', str(doc))
        firstsentence, arr1 = Past_perfect_continuous(nlp(sents[0])) if re.findall(r"\((\w+)\)", sents[0]) != None else sents[0]
        arr1.insert(1, firstsentence)
        secondsentence, arr2 = past_continuous(nlp(sents[2])) if re.findall(r"\((\w+)\)", sents[2]) != None else sents[2]
        arr2.insert(1, secondsentence)
        explain = [*explain, *arr1, *arr2]
        text = f'{firstsentence} when {secondsentence}'
        return text,explain
    if wh != None:
        explain.append('as you notice here we observe a special word case which is the word while ')
        explain.append('while is word that connect two sentence')
        explain.append('the first sentence must be in a past perfect continuous tense')
        explain.append('the second sentence must be in a past continuous tense')
        sents = re.split(r'(while)', str(doc))
        firstsentence,arr1=Past_perfect_continuous(nlp(sents[0])) if re.findall(r"\((\w+)\)", sents[0]) != None else sents[0]
        arr1.insert(1, firstsentence)
        secondsentence,arr2=past_continuous(nlp(sents[2])) if re.findall(r"\((\w+)\)", sents[2]) != None else sents[2]
        arr2.insert(1, secondsentence)
        explain=[*explain,*arr1,*arr2]
        text = f'{firstsentence} while {secondsentence}'
        return text,explain
    if be != None:
        explain.append('as you notice here we observe a special word case which is the word because ')
        explain.append('because is word that connect two sentence')
        explain.append('the first sentence must be in a past simple tense')
        explain.append('the second sentence must be in a past continuous tense')
        sents = re.split(r'(because)', str(doc))
        firstsentence, arr1 = past_simple(nlp(sents[0])) if re.findall(r"\((\w+)\)", sents[0]) != None else sents[0]
        arr1.insert(1, firstsentence)
        secondsentence, arr2 = past_continuous(nlp(sents[2])) if re.findall(r"\((\w+)\)", sents[2]) != None else sents[2]
        arr2.insert(1, secondsentence)
        explain = [*explain, *arr1, *arr2]
        text = f'{firstsentence} because {secondsentence}'
        return text,explain
# special_cases('I (go) to school when I (finish)')
