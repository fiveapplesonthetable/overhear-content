"""Reviewed, token-specific annotations for the German first-day taster."""
import importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
EP=Path(__file__).resolve().parent.parent
SID='die-discounter-s01e01-scene-01'
def table(title,cols,rows):return {'title':title,'columns':cols,'rows':[{'cells':r} for r in rows]}
def examples(*rows):return [{'text':a,'trans':b} for a,b in rows]
L={}
def lex(k,ipa,pos,gloss,meanings,ex,forms=None,more=None,**extra):
 L[k]={'lemma':k,'stress':ipa,'pos':pos,'gloss':gloss,'meanings':[{'en':a,'note':b} for a,b in meanings],'forms':forms,'moreForms':more or [],'examples':examples(*ex),'related':[],**extra}
lex('ja','jaː','part','yes; affirmative emphasis',[('yes','An affirmative response. Here it introduces his answer to the camera.'),('affirmative emphasis','Unstressed ja can mark shared or apparent knowledge; that use is different from an ordinary yes.')],[('Ja, ich bin hier.','Yes, I am here.'),('Ja, das stimmt.','Yes, that is correct.')])
lex('ich','ɪç','pron','I',[('I','Subject pronoun referring to the speaker; always written lowercase except at the start of a sentence.')],[('Ich bin müde.','I am tired.'),('Ich kenne dich.','I know you.')],table('First-person singular pronoun',['Case','Form'],[['Nominative','ich'],['Accusative','mich'],['Dative','mir'],['Genitive (rare)','meiner']]))
lex('sein','zaɪn','verb','to be',[('to be','Links a subject to a name, description or location. The present forms are irregular.'),('perfect auxiliary','Used with certain verbs to form a compound past; the lesson uses it as a main verb.')],[('Ich bin neu.','I am new.'),('Heute ist Montag.','Today is Monday.')],table('Present',['Person','Singular','Plural'],[['1st','ich bin','wir sind'],['2nd','du bist','ihr seid'],['3rd','er/sie/es ist','sie sind'],['Formal','Sie sind','Sie sind']]),[table('Simple past',['Person','Singular','Plural'],[['1st','ich war','wir waren'],['2nd','du warst','ihr wart'],['3rd','er/sie/es war','sie waren']]),table('Other useful forms',['Form','German'],[['Perfect','ich bin gewesen'],['Infinitive','sein'],['Imperative, du','sei!'],['Imperative, ihr','seid!'],['Imperative, formal','seien Sie!']])])
lex('titus','ˈtiːtʊs','name','Titus',[('Titus','The new supermarket employee speaking in this taster. This is his name, not a vocabulary phrase.')],[('Ich bin Titus.','I am Titus.'),('Titus ist neu hier.','Titus is new here.')],register='personal name')
lex('heute','ˈhɔʏtə','adv','today',[('today','Refers to the current day. A time expression may begin a German statement, followed by the finite verb.')],[('Heute ist mein erster Tag.','Today is my first day.'),('Ich komme heute.','I am coming today.')])
lex('mein','maɪn','det','my',[('my','Marks the speaker as possessor. Its ending follows the gender, number and case of the following noun, not the gender of the speaker.')],[('Mein Tag beginnt früh.','My day begins early.'),('Ich kenne meine Kollegen.','I know my colleagues.')],table('Possessive determiner: nominative / accusative',['Noun type','Nominative','Accusative'],[['Masculine','mein Tag','meinen Tag'],['Feminine','meine Arbeit','meine Arbeit'],['Neuter','mein Geld','mein Geld'],['Plural','meine Freunde','meine Freunde']]),[table('Possessive determiner: dative / genitive',['Noun type','Dative','Genitive'],[['Masculine','meinem Tag','meines Tages'],['Feminine','meiner Arbeit','meiner Arbeit'],['Neuter','meinem Geld','meines Geldes'],['Plural','meinen Freunden','meiner Freunde']])])
lex('erste','ˈeːɐ̯stə','num','first',[('first','An ordinal word. In mein erster Tag the ending -er marks masculine nominative singular after the uninflected possessive mein.')],[('Das ist mein erster Tag.','This is my first day.'),('Sie ist die erste Kundin.','She is the first customer.')],table('First: useful nominative phrases',['Gender / number','After definite article','After possessive'],[['Masculine','der erste Tag','mein erster Tag'],['Feminine','die erste Woche','meine erste Woche'],['Neuter','das erste Mal','mein erstes Mal'],['Plural','die ersten Tage','meine ersten Tage']]))
lex('tag','taːk','noun','day',[('day','Can refer to a calendar day or the daylight part of it. Here: the first day in a job.')],[('Heute ist ein guter Tag.','Today is a good day.'),('Ich arbeite drei Tage.','I work for three days.')],table('Day: noun cases',['Case','Singular','Plural'],[['Nominative','der Tag','die Tage'],['Accusative','den Tag','die Tage'],['Dative','dem Tag','den Tagen'],['Genitive','des Tages / Tags','der Tage']]),gender='m',plural='Tage')
lex('hier','hiːɐ̯','adv','here',[('here','A location near the speaker or the place currently under discussion. In this interview it means this workplace.')],[('Ich bin hier.','I am here.'),('Hier ist dein Platz.','Here is your place.')])
lex('der','deːɐ̯','det','the',[('the','The definite article changes with gender, number and case. Die before anderen is accusative plural, not feminine singular.')],[('Der Tag ist lang.','The day is long.'),('Ich kenne die anderen.','I know the others.')],table('Definite article',['Case','Masculine','Feminine','Neuter','Plural'],[['Nominative','der','die','das','die'],['Accusative','den','die','das','die'],['Dative','dem','der','dem','den'],['Genitive','des','der','des','der']]))
lex('andere','ˈandəʁə','pron','other; the others',[('the others','With a definite article, refers to other people or things already understood. Die anderen here means the other staff.'),('other / another','Can also accompany a noun, as in eine andere Arbeit.')],[('Die anderen sind schon hier.','The others are already here.'),('Ich suche eine andere Arbeit.','I am looking for another job.')],table('The others: plural pronoun',['Case','Phrase'],[['Nominative','die anderen'],['Accusative','die anderen'],['Dative','den anderen'],['Genitive','der anderen']]))
lex('kennen','ˈkɛnən','verb','to know; be familiar with',[('to know a person or thing','Takes an accusative object. For knowing a fact or an answer, wissen is usually the relevant verb.')],[('Ich kenne die anderen noch nicht.','I do not know the others yet.'),('Kennst du diesen Laden?','Do you know this shop?')],table('Present',['Person','Singular','Plural'],[['1st','ich kenne','wir kennen'],['2nd','du kennst','ihr kennt'],['3rd','er/sie/es kennt','sie kennen'],['Formal','Sie kennen','Sie kennen']]),[table('Other useful forms',['Form','German'],[['Simple past','ich kannte'],['Perfect','ich habe gekannt'],['Imperative, du','kenn! / kenne!'],['Imperative, ihr','kennt!'],['Imperative, formal','kennen Sie!']])])
lex('noch','nɔx','adv','still; yet',[('yet','In noch nicht, something has not happened up to now.'),('still','Can also describe a state continuing: Ich bin noch hier.')],[('Ich kenne ihn noch nicht.','I do not know him yet.'),('Sie ist noch hier.','She is still here.')])
lex('nicht','nɪçt','part','not',[('not','Negates a statement or part of one. In noch nicht so gut it qualifies how well he knows the others.')],[('Ich bin nicht müde.','I am not tired.'),('Ich kenne sie noch nicht.','I do not know her yet.')])
lex('so','zoː','adv','so; that; to that extent',[('so / that','Specifies degree before an adjective or adverb: nicht so gut means not so well.'),('like this / in this way','Can refer to a manner of doing something.')],[('Ich kenne ihn nicht so gut.','I do not know him that well.'),('So geht das.','This is how it works.')])
lex('gut','ɡuːt','adj','good; well',[('well','Used adverbially without an ending to describe how well he knows people.'),('good','As an adjective before a noun, takes an appropriate ending: ein guter Tag.')],[('Ich kenne sie gut.','I know her well.'),('Das ist ein guter Tag.','That is a good day.')],table('Comparison',['Degree','Form'],[['Positive','gut'],['Comparative','besser'],['Superlative, adverbial','am besten']]))
lex('aber','ˈaːbɐ','conj','but',[('but','A coordinating conjunction introducing a contrast. It does not itself occupy the first position of the clause that follows.')],[('Ich bin neu, aber ich kenne ihn.','I am new, but I know him.'),('Das ist gut, aber teuer.','That is good, but expensive.')])
lex('um','ʊm','conj','in order to; to (purpose)',[('to / in order to','Here starts um … zu + infinitive, explaining a purpose. This is not the prepositional sense around, and does not itself govern a noun case here.')],[('Ich bin hier, um zu arbeiten.','I am here to work.'),('Ich komme, um dich zu sehen.','I am coming to see you.')],governs='Purpose clause: um … zu + infinitive; understood actor normally shared with the main clause.')
lex('freund','fʁɔʏnt','noun','friend',[('friend','Freunde finden means to make friends. The plural Freunde in this lesson does not specify one individual friend.'),('boyfriend','Singular mein Freund can mean my boyfriend, depending on the relationship and context.')],[('Ich möchte Freunde finden.','I would like to make friends.'),('Er ist ein guter Freund.','He is a good friend.')],table('Friend: noun cases',['Case','Singular','Plural'],[['Nominative','der Freund','die Freunde'],['Accusative','den Freund','die Freunde'],['Dative','dem Freund','den Freunden'],['Genitive','des Freundes / Freunds','der Freunde']]),gender='m',plural='Freunde')
lex('zu','tsuː','part','to (infinitive marker)',[('to','Here marks the infinitive in a purpose clause. It is not the dative preposition used before a destination or person.')],[('Ich habe Zeit, um zu lesen.','I have time to read.'),('Ich bin hier, um Geld zu verdienen.','I am here to earn money.')],governs='Infinitive marker in um … zu; no noun case in this use.')
lex('finden','ˈfɪndən','verb','to find; make (friends)',[('to find','Discover or come upon a person, thing or solution.'),('to make friends','Freunde finden is idiomatic; English normally uses make rather than find.')],[('Ich finde meinen Schlüssel.','I find my key.'),('Hier kann man Freunde finden.','You can make friends here.')],table('Present',['Person','Singular','Plural'],[['1st','ich finde','wir finden'],['2nd','du findest','ihr findet'],['3rd','er/sie/es findet','sie finden'],['Formal','Sie finden','Sie finden']]),[table('Other useful forms',['Form','German'],[['Simple past','ich fand'],['Perfect','ich habe gefunden'],['Imperative, du','finde!'],['Imperative, ihr','findet!'],['Imperative, formal','finden Sie!']])])
lex('geld','ɡɛlt','noun','money',[('money','Usually a mass noun in this general sense; German does not use an indefinite article in Geld verdienen.'),('funds','The plural Gelder is used for particular sums, allocations or funds, rather than ordinary coins counted one by one.')],[('Ich verdiene Geld.','I earn money.'),('Das Geld ist für die Miete.','The money is for the rent.')],table('Money / funds: noun cases',['Case','Singular','Plural (funds)'],[['Nominative','das Geld','die Gelder'],['Accusative','das Geld','die Gelder'],['Dative','dem Geld','den Geldern'],['Genitive','des Geldes / Gelds','der Gelder']]),gender='n',plural='Gelder (particular funds or sums)')
lex('verdienen','fɛɐ̯ˈdiːnən','verb','to earn; to deserve',[('to earn','Receive money for work.'),('to deserve','Be worthy of something: Du verdienst eine Pause.')],[('Ich verdiene hier Geld.','I earn money here.'),('Du verdienst eine Pause.','You deserve a break.')],table('Present',['Person','Singular','Plural'],[['1st','ich verdiene','wir verdienen'],['2nd','du verdienst','ihr verdient'],['3rd','er/sie/es verdient','sie verdienen'],['Formal','Sie verdienen','Sie verdienen']]),[table('Other useful forms',['Form','German'],[['Simple past','ich verdiente'],['Perfect','ich habe verdient'],['Participle','verdient'],['Imperative, du','verdien! / verdiene!'],['Imperative, ihr','verdient!'],['Imperative, formal','verdienen Sie!']])])
lex('tschüss','tʃʏs','interj','bye',[('bye','An informal farewell. Added as the lesson closing, not claimed as speech from the original excerpt.')],[('Tschüss, bis morgen!','Bye, see you tomorrow!'),('Tschüss, einen schönen Tag noch!','Bye, have a nice day!')],register='informal')
# Every whitespace token is annotated separately; no phrase is silently assigned to one word.
W={
 'ja':('ja','yes','affirmative opening; not the unstressed shared-knowledge use'),
 'ich':('ich','I','first person singular, nominative; subject'),
 'bin':('sein','am','present indicative, first person singular'),
 'titus':('titus','Titus','male personal name'),
 'heute':('heute','today','time adverb'),
 'ist':('sein','is','present indicative, third person singular'),
 'mein':('mein','my','possessive determiner, masculine nominative singular'),
 'erster':('erste','first','ordinal, masculine nominative singular; -er after mein'),
 'tag':('tag','day','masculine nominative singular; noun written with a capital'),
 'hier':('hier','here','place adverb; this workplace'),
 'die':('der','the','definite article, accusative plural; modifies anderen'),
 'anderen':('andere','others','accusative plural after die; refers to the other employees'),
 'kenne':('kennen','know','present indicative, first person singular; accusative object'),
 'noch':('noch','yet','time adverb; noch nicht means not yet'),
 'nicht':('nicht','not','negative particle'),
 'so':('so','so','degree adverb before gut; not so well'),
 'gut':('gut','well','adjective used adverbially, uninflected'),
 'aber':('aber','but','coordinating conjunction introducing a contrast'),
 'um':('um','in order','conjunction opening a purpose clause; paired with zu + infinitive'),
 'freunde':('freund','friends','masculine noun, accusative plural; object of finden'),
 'zu':('zu','to','infinitive marker in a purpose clause'),
 'finden':('finden','make','infinitive; Freunde finden means make friends, literally find friends'),
 'geld':('geld','money','neuter noun, accusative singular; mass sense'),
 'verdienen':('verdienen','earn','infinitive after zu'),
 'tschüss':('tschüss','bye','informal farewell; added lesson closing')
}
spec=importlib.util.spec_from_file_location('draft',EP/'authoring/scene-01.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
script=json.loads((EP/'scene-01.json').read_text());translations={t:e for _,t,e,*_ in m.STORY};translations[m.CLOSING[1]]='Bye!'
lines=[]
for i,s in enumerate(script['segments']):
 if s['v']=='narrator':continue
 words=[]
 for t in s['t'].split():
  k=re.sub(r'[^\wäöüß]','',t.lower());lemma,g,gram=W[k];entry=L[lemma]
  ipa=entry['stress']
  if k=='bin':ipa='bɪn'
  if k=='ist':ipa='ɪst'
  if k=='die':ipa='diː'
  if k=='erster':ipa='ˈeːɐ̯stɐ'
  if k=='anderen':ipa='ˈandəʁən'
  if k=='kenne':ipa='ˈkɛnə'
  if k=='freunde':ipa='ˈfʁɔʏndə'
  words.append({'t':t,'lemma':lemma,'pos':entry['pos'],'stress':ipa,'gloss':g,'gram':gram})
 lines.append({'seg':i,'trans':translations[s['t']],'words':words})
notes={'schemaVersion':1,'id':SID,'lines':lines,'lexicon':L}
(EP/'scene-01.notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
(ROOT/'dictionary/de-en.json').write_text(json.dumps({'schemaVersion':1,'pair':'de-en','entries':L},ensure_ascii=False,indent=2)+'\n')
print(f'{len(lines)} native segments; {len(L)} distinct lemmas; full per-token annotations, independent forms/examples')
