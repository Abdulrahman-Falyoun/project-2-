import spacy

nlp1 = spacy.load('en_core_web_md')

non_continuous_verb=nlp1('hate like love prefer want wish appear feel hear see seem smell sound taste deny disagree mean promise satisfy surprise believe imagine know mean realize recognize remember understand be belong concern depend involve matter need owe own possess')
consonant = nlp1('b c d f g h j k l m n p q r s t v w x y z')
vowel = nlp1('a e i u o ')
pronouns=nlp1('it he she they you we I')
special_verbs = nlp1('age agree disagree dye free knee refere singe tiptoe')
special_words = nlp1('while when before after because until')


dict_v2={'be':'was','bear':'bore','beat':'beat','become':'became','begin':'began','bend':'bent','bet':'bet','bid':'bid',
'bind':'bound','bite':'bit','bleed':'bled','blow':'blew','break':'broke','breed':'bred',
'bring':'brought','broadcast':'broadcast','build':'built','burn':'burnt','burst':'burst',
'bust':'bust','buy':'bought','cast':'cast','catch':'caught','choose':'chose','cling':'clung','come':'came','cost':'cost',
'creep':'crept','cut':'cut','deal':'dealt','dig':'dug','dive':'dove','do':'did',"dose":"done",'draw':'drew','dream':'dreamt','drink':'drank',
'drive':'drove','eat':'ate','fall':'fell','feed':'fed','feel':'felt','fight':'fought','find':'found','flee':'fled','fling':'flung',
'fly':'flew','forbid':'forbade','forecast':'forecast','forget':'forgot','forsake':'forsook','freeze':'froze','get':'got',
'give':'gave','grind':'ground','go':'went','grow':'grew','hang':'hung','have':'had','has':'had','hear':'heard','hide':'hid','hit':'hit',
'hold':'held','hurt':'hurt','keep':'kept','know':'knew','lay':'laid','lead':'led','learn':'learnt','leave':'left','lend':'lent',
'let':'let','lie':'lay','light':'lit','lose':'lost','make':'made','mean':'meant','meet':'met','pay':'paid','prove':'proved',
'put':'put','quit':'quit','read':'read','rid':'rid','ride':'rode','ring':'rang','rise':'rose','run':'ran','saw':'sawed',
'say':'said','see':'saw','seek':'sought','sell':'sold','send':'sent','set':'set','sew':'sewed','shake':'shook','shear':'sheared',
'shed':'shed','shine':'shone','shoot':'shot','show':'showed','shut':'shut','sing':'sang','sink':'sank','sit':'sat','slay':'slew',
'sleep':'slept','slide':'slid','sling':'slung','slink':'slunk','slit':'slit','sow':'sowed','speak':'spoke','speed':'sped',
'spend':'spent','spin':'spun','spit':'spit','split':'split','spread':'spread','spring':'sprang','stand':'stood','steal':'stole',
'stick':'stuck','sting':'stung','stink':'stunk','stride':'strode','strike':'struck','string':'strung','strive':'strove',
'swear':'swore','sweep':'swept','swell':'swelled','swim':'swam','swing':'swung','take':'took','teach':'taught','tear':'tore',
'tell':'told','think':'thought','thrive':'throve','throw':'threw','thrust':'thrust','tread':'trod','understand':'understood',
'wake':'woke','wear':'wore','weave':'wove','weep':'wept','wet':'wet','win':'won','wind':'wound','wring':'wrung','write':'wrote'}

dict_v3={'be':'been','bear':'born','beat':'beaten','become':'become','begin':'begun','bend':'bent','bet':'bet',
'bid':'bid','bind':'bound','bite':'bitten','bleed':'bled','blow':'blown','break':'broken','breed':'bred',
'bring':'brought','broadcast':'broadcast','build':'built','burn':'burnt','burst':'burst',
'bust':'bust','buy':'bought','cast':'cast','catch':'caught','choose':'chosen','cling':'clung','come':'come','cost':'cost',
'creep':'crept','cut':'cut','deal':'dealt','dig':'dug','dive':'dove','do':'done',"dose":"done",'draw':'drawn','dream':'dreamt','drink':'drunk',
'drive':'driven','eat':'eaten','fall':'fallen','feed':'fed','feel':'felt','fight':'fought','find':'found','flee':'fled','fling':'flung',
'fly':'flown','forbid':'forbidden','forecast':'forecast','forget':'forgotten','forsake':'forsaken','freeze':'frozen','get':'got',
'give':'given','grind':'ground','go':'gone','grow':'grown','hang':'hung','have':'had','has':'had','hear':'heard','hide':'hidden','hit':'hit',
'hold':'held','hurt':'hurt','keep':'kept','know':'known','lay':'laid','lead':'led','learn':'learnt','leave':'left','lend':'lent',
'let':'let','lie':'lain','light':'lit','lose':'lost','make':'made','mean':'meant','meet':'met','pay':'paid','prove':'proven',
'put':'put','quit':'quit','read':'read','rid':'ridden','ride':'ridden','ring':'rung','rise':'risen','run':'run','saw':'sawed',
'say':'said','see':'seen','seek':'sought','sell':'sold','send':'sent','set':'set','sew':'sewn','shake':'shaken','shear':'shorn',
'shed':'shed','shine':'shone','shoot':'shot','show':'shown','shut':'shut','sing':'sung','sink':'sunk','sit':'sat','slay':'slain',
'sleep':'slept','slide':'slid','sling':'slung','slink':'slunk','slit':'slit','sow':'sowed','speak':'spoken','speed':'sped',
'spend':'spent','spin':'spun','spit':'spit','split':'split','spread':'spread','spring':'sprung','stand':'stood','steal':'stolen',
'stick':'stuck','sting':'stung','stink':'stunk','stride':'stridden','strike':'struck','string':'strung','strive':'striven',
'swear':'sworn','sweep':'swept','swell':'swollen','swim':'swum','swing':'swung','take':'taken','teach':'taught','tear':'torn',
'tell':'told','think':'thought','thrive':'thrived','throw':'thrown','thrust':'thrust','tread':'trod','understand':'understood',
'wake':'woken','wear':'worn','weave':'woven','weep':'wept','wet':'wet','win':'won','wind':'wound','wring':'wrung','write':'written'}


unregular_verbs = " ".join(dict_v2.keys())
unregular_verbs=nlp1(unregular_verbs)