"""Explicitly reviewed eojeol annotations and small paradigms, no automatic morphology guesses."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
EP=Path(__file__).resolve().parents[1]
def table(title, rows):return {'title':title,'columns':['use','form'],'rows':[{'cells':list(row)} for row in rows]}
def entry(lemma,pos,gloss,examples,forms=None,notes=''):
 return {'lemma':lemma,'stress':None,'pos':pos,'gloss':gloss,'meanings':[{'en':gloss,'note':notes}],
         'forms':forms,'moreForms':[],'examples':[{'text':text,'trans':trans} for text,trans in examples],'related':[]}
LEX={
 'KBS':entry('KBS','name','KBS, the Korean broadcasting network', [('KBS에서 일해요.','I work at KBS.'),('KBS에 가요.','I am going to KBS.')],notes='The initialism is read 케이비에스 in Korean. This is entity information, not an invented personal-name history.'),
 '신입사원':entry('신입사원','noun','new employee', [('저는 신입사원이에요.','I am a new employee.'),('신입사원이 왔어요.','A new employee has arrived.')],table('Noun and common attachments', [('plain noun','신입사원'),('with subject particle','신입사원이'),('with topic particle','신입사원은'),('polite identification','신입사원입니다'),('respectful confirmation','신입사원이시죠')]),'신입 means newly joining and 사원 is a member of company staff. In the source the attached 이시죠 respectfully checks the addressee\'s identity. RR: sinipsawon.'),
 '아':entry('아','interj','ah; oh', [('아, 알겠어요.','Ah, I understand.'),('아, 그렇군요.','Oh, I see.')],notes='A natural reaction or moment of recognition; its force depends on the surrounding words. RR: a.'),
 '네':entry('네','interj','yes; polite acknowledgement', [('네, 맞아요.','Yes, that is right.'),('네, 알겠습니다.','Yes, understood.')],notes='A short respectful answer or acknowledgement. In this exchange it confirms the camera operator\'s question. RR: ne.'),
 '왜':entry('왜','adv','why', [('왜 가세요?','Why are you going?'),('왜 뛰세요?','Why are you running?')],notes='Asks for a reason. It can stand immediately before the word describing the action. RR: wae.'),
 '뛰다':entry('뛰다','verb','run', [('왜 뛰세요?','Why are you running?'),('저는 매일 뛰어요.','I run every day.')],table('Common action forms', [('dictionary form','뛰다'),('polite present','뛰어요'),('respectful form used in the question','뛰세요'),('formal present','뜁니다'),('polite past','뛰었어요')]),'The visible running and two source readings establish the running sense here, matching the dictionary\'s separate running entry. 뛰세요 is a respectful question in this context; the same written form can be used as a request in other contexts. RR: ttwida.'),
 '저':entry('저','pron','I; me, spoken respectfully', [('저는 신입사원이에요.','I am a new employee.'),('제가 할게요.','I will do it.')],table('Pronoun attachments', [('plain form','저'),('topic','저는'),('subject','제가'),('object','저를'),('possessive','제')]),'The speaker lowers himself in relation to the listener. Here it also sits naturally in a hesitant explanation. RR: jeo.'),
 '입사식':entry('입사식','noun','company induction ceremony', [('입사식이 있어요.','There is a company induction ceremony.'),('입사식에 가요.','I am going to the induction ceremony.')],table('Noun attachments', [('plain noun','입사식'),('subject','입사식이'),('object','입사식을'),('destination or event','입사식에')]),'A ceremony for people joining a company. 입사 refers to entering company employment and 식 marks a ceremony. RR: ipsasik.'),
 '하다':entry('하다','verb','do; perform; take part in', [('일을 해요.','I work.'),('지금 뭐 해요?','What are you doing now?')],table('Common forms', [('dictionary form','하다'),('polite present','해요'),('formal present','합니다'),('polite past','했어요'),('background explanation used here','하는데요')]),'With the ceremony word, English naturally uses have or attend a scheduled event. The source does not say Seung-chan organizes it. The final 데요 gives background to the question he was asked. RR: hada.'),
 '늦다':entry('늦다','verb','be late; run late', [('회사에 늦었어요.','I was late for work.'),('늦어서 죄송해요.','I am sorry for being late.')],table('Lateness forms', [('dictionary form','늦다'),('polite present','늦어요'),('polite past','늦었어요'),('modifier before a following noun','늦은'),('giving the reason','늦어서')]),'Here the concern is being late for a scheduled event. The word also has a descriptive use for a late time or season. 늦은 occurs before 거 in his impression of being late. RR: neutda; the used form 늦은 is neujeun.'),
 '것':entry('것','noun','thing; fact; nominalizing bound noun', [('이것은 제 것이에요.','This is mine.'),('좋은 거예요.','It is a good thing.')],table('Written and spoken forms', [('plain written form','것'),('spoken form used here','거'),('with subject particle','것이 / 게'),('with topic particle','것은 / 건')]),'The National Institute of Korean Language identifies 거 as the spoken form of 것. In the source it helps turn the preceding idea into something that can seem to be the case. It has no separate word in the natural English translation. RR: geot; spoken geo.'),
 '같다':entry('같다','adj','be like; seem; be the same', [('두 사람이 같아요.','The two people are alike.'),('비가 올 것 같아요.','I think it will rain.')],table('Common comparison and impression forms', [('dictionary form','같다'),('polite present','같아요'),('polite past','같았어요'),('modifier','같은'),('ordinary linking form','같아서'),('spoken linking form used here','같아가지고')]),'With a preceding clause and 것 or 거, it presents an impression. The spoken 아가지고 here links that impression to his reason for running. Keep it distinct from the literal sameness use. RR: gatda.'),
}
# Each tuple is one whole written eojeol. Attached copulas/particles are explained, not guessed apart.
WORDS={
 'KBS 신입사원이시죠?': [('KBS','KBS','KBS','proper network name','케이비에스'),('신입사원이시죠?','신입사원',"you are a new employee, right?",'noun + respectful confirmation 이시죠','신입사원이시죠')],
 '아, 네.': [('아,','아','ah','reaction','아'),('네.','네','yes','respectful acknowledgement','네')],
 '왜 뛰세요?': [('왜','왜','why','asks for a reason','왜'),('뛰세요?','뛰다','are you running','respectful question in 세요','뛰세요')],
 '아, 저 입사식 하는데요.': [('아,','아','ah','hesitant reaction','아'),('저','저','I','humble first-person pronoun','저'),('입사식','입사식','induction ceremony','noun, ceremony for new employees','입사식'),('하는데요.','하다','have','scheduled event; polite background explanation','하는데요')],
 '늦은 거 같아가지고.': [('늦은','늦다','late','modifier before 거','늦은'),('거','것','thing; fact','spoken bound noun, no separate English word here','거'),('같아가지고.','같다','because; think','spoken impression linked as the reason','같아가지고')],
}
TRANS={
 'KBS 신입사원이시죠?': "You're a new KBS employee, right?", '아, 네.':'Ah, yes.',
 '왜 뛰세요?':'Why are you running?', '아, 저 입사식 하는데요.':'Ah, I have an induction ceremony.',
 '늦은 거 같아가지고.':"Because I think I'm late.",
}
script=json.loads((EP/'scene-01.json').read_text());lines=[]
for i,seg in enumerate(script['segments']):
 if seg['v']=='narrator':continue
 text=seg['t'];words=[];cursor=0
 for token,lemma,gloss,gram,reading in WORDS[text]:
  start=text.find(token,cursor);assert start>=cursor
  end=start+len(token);assert text[start:end]==token
  words.append({'t':token,'lemma':lemma,'stress':None,'reading':reading,'span':[start,end],
                'pos':LEX[lemma]['pos'],'gloss':gloss,'gram':gram})
  cursor=end
 assert [x['t'] for x in words]==text.split()
 lines.append({'seg':i,'trans':TRANS[text],'words':words})
(EP/'scene-01.notes.json').write_text(json.dumps({'schemaVersion':1,'id':script['id'],'lines':lines,'lexicon':LEX},ensure_ascii=False,indent=2)+'\n')
print(f'{len(lines)} native segments, {len(LEX)} lexicon entries, {sum(len(x["words"]) for x in lines)} annotated occurrences')
