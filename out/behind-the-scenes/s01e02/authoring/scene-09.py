ID = 'behind-the-scenes-s01e02-scene-09'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = '明天之前答复  (One Day Left to Decide on DTS)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'bu_xiaogu': '布小谷', 'fang': '方老师'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'
INTRO = ('In the Xingtian pantry, Bu Xiaogu gets a phone call from her advisor Professor Fang about her thesis '
 'deadline and the prestigious DTS job offer. Listen to their call first.')
OPENER = "Let's unpack what they say. Xiaogu answers her phone politely when she sees Professor Fang calling."
STORY = [
 ('bu_xiaogu',
  '喂，方老师。',
  'Hello, Professor Fang.',
  [(357, '喂 方老师')],
  'Punctuation supplied for reading.'),
 ('fang',
  '小谷啊，论文期限快到了，你知道吗？',
  'Xiaogu, the thesis deadline is almost here, do you know?',
  [(358, '小谷啊'), (359, '期限快到了'), (360, '你知道吗')],
  '论文 corrects the ASR homophone 洛文 in cue 359.'),
 ('bu_xiaogu',
  '我知道。',
  'I know.',
  [(361, '我知道')],
  'Punctuation supplied for reading.'),
 ('fang',
  '你真的想放弃去电视台工作的机会吗？',
  'Do you really want to give up the chance to work at the TV network?',
  [(362, '真的想放弃'), (363, '工作的机会')],
  '电视台 adapts English DTS into pure Chinese characters.'),
 ('bu_xiaogu',
  '方老师，我还在想。',
  'Professor Fang, I am still thinking.',
  [],
  'Bridge line reflecting Xiaogu hesitating on the line.'),
 ('fang',
  '小谷啊，人生大事一定要慎重。',
  'Xiaogu, major life decisions must be made carefully.',
  [(364, '小谷啊'), (365, '人生大事一定要慎重')],
  'Combined across cues 364-365.'),
 ('fang',
  '不过你还得尽快回复我。',
  'However, you still have to reply to me as soon as possible.',
  [(366, '不过'), (367, '你还得尽快回复我')],
  'Combined across cues 366-367.'),
 ('fang',
  '这样吧，明天之前给我一个最终答复。',
  'How about this, give me a final answer before tomorrow.',
  [(368, '这样吧'), (369, '明天之前'), (370, '给我一个最终答复')],
  'Combined across cues 368-370.'),
 ('bu_xiaogu',
  '好的，我知道了。',
  'All right, I understand.',
  [(371, '好的')],
  'Expanded slightly for a natural phone reply.'),
 ('bu_xiaogu',
  '谢谢您，方老师。',
  'Thank you, Professor Fang.',
  [(372, '谢谢您 方老师')],
  'Punctuation supplied for reading.'),
 ('bu_xiaogu',
  '老师再见。',
  'Goodbye, Professor.',
  [(373, '老师再见')],
  'Punctuation supplied for reading.'),
]
WALK = [
 (0,
  None,
  "'Hello, Professor Fang.' People in Mandarin answer the phone with \"wei\", pronounced with a rising tone when checking "
  'who is there, followed by family name \"Fang\" plus \"laoshi\", \'teacher\'.'),
 (1,
  None,
  "'Xiaogu, the thesis deadline is almost here, do you know?' Framing \"dao\", 'arrive', inside \"kuai... le\" means "
  "something is right around the corner, and \"qixian\" is the word for 'deadline'."),
 (2,
  None,
  "'I know.' Just three syllables—\"wo zhidao\"—acknowledges a reminder plainly without adding \"le\", since she "
  'already knew about the date beforehand.'),
 (3,
  None,
  "'Do you really want to give up the chance to work at the TV network?' In Mandarin, \"qu dianshitai gongzuo\" "
  "describes \"jihui\", 'opportunity', from the front, linked by \"de\", while \"fangqi\" means 'give up'."),
 (4,
  None,
  "'Professor Fang, I am still thinking.' Combining \"hai\", 'still', and \"zai\", 'in the middle of', before "
  '\"xiang\", \'think\', tells the listener she has not made up her mind yet.'),
 (5,
  None,
  "'Xiaogu, major life decisions must be made carefully.' Literally \"rensheng dashi\" says 'big matters of human "
  "life', and \"shenzhong\" means weighing a serious choice with real care."),
 (6,
  None,
  "'However, you still have to reply to me as soon as possible.' Here \"dei\" is pronounced third tone and means "
  "'have to' in everyday speech, paired with \"jinkuai\", 'as soon as possible', and \"huifu\", 'reply'."),
 (7,
  None,
  "'How about this, give me a final answer before tomorrow.' Opening with \"zheyang ba\" proposes a practical middle "
  'ground, and \"mingtian zhiqian\" puts \"zhiqian\", \'before\', after \"mingtian\", \'tomorrow\'.'),
 (8,
  None,
  "'All right, I understand.' Adding \"le\" onto \"wo zhidao\" shifts the meaning from 'I already know' to 'got it, "
  "I have taken note of what you just said'."),
 (9,
  None,
  "'Thank you, Professor Fang.' Switching from casual \"ni\" to respectful \"nin\" in \"xiexie nin\" shows polite "
  'warmth toward a mentor or elder.'),
 (10,
  None,
  "'Goodbye, Professor.' Putting a title like \"laoshi\" right before \"zaijian\", 'goodbye', is the standard polite "
  'way for a student to end a call or leave an office.'),
]
TRANSITION = "Now let's hear the whole conversation once more."
OUTRO = ('Professor Fang gives Xiaogu until tomorrow to choose between DTS and staying at Xingtian. You learned how '
 'to answer the phone with "wei", say a deadline is close with "kuai dao le", and thank an elder politely with '
 '"xiexie nin". See you next time!')
CLOSING = ('fang', '明天见！')
