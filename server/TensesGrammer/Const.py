import spacy

nlp1 = spacy.load('en_core_web_md')

non_continuous_verb=nlp1('hate like love prefer want wish appear feel hear see seem smell sound taste deny disagree mean promise satisfy surprise believe imagine know mean realize recognize remember understand be belong concern depend involve matter need owe own possess')
consonant = nlp1('b c d f g h j k l m n p q r s t v w x y z')
vowel = nlp1('a e i u o ')
pronouns=nlp1('it he she they you we I')
special_verbs = nlp1('age agree disagree dye free knee refere singe tiptoe')
special_words = nlp1('while when before after')


dict_v2={'be':'was','bear':'bore','beat':'beat','become':'became','begin':'began','bend':'bent','bet':'bet','bid':'bid',
'bind':'bound','bite':'bit','bleed':'bled','blow':'blew','break':'broke','breed':'bred',
'bring':'brought','broadcast':'broadcast','build':'built','burn':'burnt','burst':'burst',
'bust':'bust','buy':'bought','cast':'cast','catch':'caught','choose':'chose','cling':'clung','come':'came','cost':'cost',
'creep':'crept','cut':'cut','deal':'dealt','dig':'dug','dive':'dove','do':'did','draw':'drew','dream':'dreamt','drink':'drank',
'drive':'drove','eat':'ate','fall':'fell','feed':'fed','feel':'felt','fight':'fought','find':'found','flee':'fled','fling':'flung',
'fly':'flew','forbid':'forbade','forecast':'forecast','forget':'forgot','forsake':'forsook','freeze':'froze','get':'got',
'give':'gave','grind':'ground','go':'went','grow':'grew','hang':'hung','have':'had','hear':'heard','hide':'hid','hit':'hit',
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

dict_v3={'was':'been','were':'been','bore':'born','beat':'beaten','became':'become','began':'begun','bent':'bent','bet':'bet',
'bid':'bid','bound':'bound','bit':'bitten','bled':'bled','blew':'blown','broke':'broken','bred':'bred',
'brought':'brought','broadcast':'broadcast','built':'built','burnt':'burnt','burst':'burst',
'bust':'bust','bought':'bought','cast':'cast','caught':'caught','chose':'chosen','clung':'clung','came':'come','cost':'cost',
'crept':'crept','cut':'cut','dealt':'dealt','dug':'dug','dove':'dove','did':'done','drew':'drawn','dreamt':'dreamt','drank':'drunk',
'drove':'driven','ate':'eaten','fell':'fallen','fed':'fed','felt':'felt','fought':'fought','found':'found','fled':'fled','flung':'flung',
'flew':'flown','forbade':'forbidden','forecast':'forecast','forgot':'forgotten','forsook':'forsaken','froze':'frozen','got':'got',
'gave':'given','ground':'ground','went':'gone','grew':'grown','hung':'hung','have':'had','heard':'heard','hid':'hidden','hit':'hit',
'held':'held','hurt':'hurt','kept':'kept','knew':'known','laid':'laid','led':'led','learnt':'learnt','left':'left','lent':'lent',
'let':'let','lay':'lain','lit':'lit','lost':'lost','made':'made','meant':'meant','met':'met','paid':'paid','proved':'proven',
'put':'put','quit':'quit','read':'read','rid':'ridden','rode':'ridden','rang':'rung','rose':'risen','ran':'run','sawed':'sawed',
'said':'said','saw':'seen','sought':'sought','sold':'sold','sent':'sent','set':'set','sewed':'sewn','shook':'shaken','sheared':'shorn',
'shed':'shed','shone':'shone','shot':'shot','showed':'shown','shut':'shut','sang':'sung','sank':'sunk','sat':'sat','slew':'slain',
'sleep':'slept','slide':'slid','sling':'slung','slink':'slunk','slit':'slit','sow':'sowed','speak':'spoke','speed':'sped',
'spent':'spent','spun':'spun','spit':'spit','split':'split','spread':'spread','sprang':'sprung','stood':'stood','stole':'stolen',
'stuck':'stuck','stung':'stung','stunk':'stunk','strode':'stridden','struck':'struck','strung':'strung','strove':'striven',
'swore':'sworn','swept':'swept','swelled':'swollen','swam':'swum','swung':'swung','took':'taken','taught':'taught','tore':'torn',
'told':'told','thought':'thought','throve':'thrived','threw':'thrown','thrust':'thrust','trod':'trod','understood':'understood',
'woke':'woken','wore':'worn','wove':'woven','wept':'wept','wet':'wet','won':'won','wound':'wound','wrung':'wrung','wrote':'written'}


unregular_verbs = " ".join(dict_v2.keys())
unregular_verbs=nlp1(unregular_verbs)