ID = 'behind-the-scenes-s01e01-scene-18'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 1
SCENE = 18
TITLE = '公司有间谍！  (There Is a Spy at the Company!)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'ji_xiu': '吉秀', 'bu_xiaogu': '布小谷', 'qin_xiao': '秦箫'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E01'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e01.zh.srt'
INTRO = ('Passing down a quiet corridor, Bu Xiaogu overhears Ji Xiu talking on the phone about taking down '
 'Chun Yuqiao. Alarmed, Xiaogu tells Qin Xiao — who warns her to stay out of office politics. Listen first.')
OPENER = "Let's unpack what Xiaogu overhears and how Qin Xiao reacts."
STORY = [
 ('ji_xiu',
  '星天也在用我们提供的数据。',
  'Xingtian is also using the data we provide.',
  [(570, '星天也在用'), (571, '我们提供的数据')],
  'Combined across cues 570-571.'),
 ('ji_xiu',
  '我们公司是最专业的。',
  'Our company is the most professional.',
  [(573, '我们公司'), (574, '是最专业的')],
  'Combined across cues 573-574.'),
 ('ji_xiu',
  '最想搞掉的就是那个淳于乔。',
  'The one you want to take down most is that Chun Yuqiao.',
  [(581, '最想搞掉的'), (582, '就是那个淳于乔')],
  'Combined across cues 581-582.'),
 ('bu_xiaogu',
  '公司有间谍！',
  'There is a spy in the company!',
  [(583, '公司有间谍')],
  'Punctuation supplied for reading.'),
 ('bu_xiaogu',
  '我刚才听见她打电话了，她要出卖淳于总！',
  'I just heard her making a phone call — she is going to betray Director Chun Yu!',
  [(587, '我刚才听见她打电话了'), (588, '她要出卖淳于总')],
  'Combined across cues 587-588.'),
 ('qin_xiao',
  '你听错了吧，你别多管闲事啊。',
  'You must have misheard; do not go meddling in other people\'s business.',
  [(589, '你听错了吧'), (590, '你别多管闲事啊')],
  'Combined across cues 589-590.'),
 ('bu_xiaogu',
  '那我也不能不管吧，这怎么办啊？',
  'Well, I cannot just ignore it either — what should I do?',
  [(591, '那我也不能'), (591, '不管吧'), (592, '这怎么办啊')],
  'Simplified 坐视不管 to 不管 across cues 591-592.'),
 ('bu_xiaogu',
  '我们的艺人方案特别重要，不能泄露！',
  'Our guest-artist plan is especially important; it must not leak!',
  [(602, '我们'), (603, '方案特别重要'), (604, '不能泄露')],
  '艺人 corrects the ASR homophone in cue 603.'),
 ('qin_xiao',
  '职场里边很复杂，你听我的，先顾自己。',
  'Inside the workplace things are complicated; listen to me and look after yourself first.',
  [(593, '职场里边很复杂'), (606, '你听我的'), (607, '先顾自己')],
  'Paired cues 593 and 606-607.'),
]
WALK = [
 (0,
  None,
  "'Xingtian is also using the data we provide.' Notice compact \"zai yong\" for 'is using', where \"zai\" right "
  'before an action shows it is currently underway, and \"tigong\" means \'provide\'.'),
 (1,
  None,
  "'Our company is the most professional.' Mandarin frequently drops \"de\" between \"women\", 'we', and a close "
  'institution like \"gongsi\", \'company\', while \"zhuanye\" means \'professional\'.'),
 (2,
  None,
  "'The one you want to take down most is that Chun Yuqiao.' Colloquial \"gaodiao\" puts \"diao\", 'off' or 'away', "
  'after catch-all action \"gao\" to mean knock out or get rid of a rival.'),
 (3,
  None,
  "'There is a spy in the company!' Location \"gongsi\" comes first, then \"you\", 'have' or 'there is', and "
  '\"jiandie\", \'spy\' — Chinese uses \"you\" where English says \'there is\'.'),
 (4,
  None,
  "'I just heard her making a phone call — she is going to betray Director Chun Yu!' Everyday \"da dianhua\" "
  "literally says 'hit the telephone' for making a call, and \"gangcai\" means 'just a moment ago'."),
 (5,
  None,
  "'You must have misheard; do not go meddling in other people\'s business.' Putting \"cuo\", 'wrong', onto \"ting\", "
  "'listen', creates \"tingcuo\", 'mishear', and \"duoguan xianshi\" warns against poking into idle business."),
 (6,
  None,
  "'Well, I cannot just ignore it either — what should I do?' Double negative \"buneng buguan\", literally 'cannot "
  "not care', means 'cannot just stand by', and \"zenme ban\" is the classic cry 'what do I do?'."),
 (7,
  None,
  "'Our guest-artist plan is especially important; it must not leak!' Remember \"zhongyao\" for 'important' and "
  '\"xielou\" for leaking confidential news.'),
 (8,
  None,
  "'Inside the workplace things are complicated; listen to me and look after yourself first.' Short, urgent "
  '\"ni ting wo de\" means \'take my word for it\', followed by \"gu ziji\", \'look out for yourself\'.'),
]
TRANSITION = 'Now listen to the whole overheard call and campus warning again.'
OUTRO = ('Ignoring Qin Xiao\'s caution, Xiaogu decides she has to warn Chun Yuqiao in person. You learned '
 '"da dianhua" for making a call, "tingcuo" for mishearing, and "zenme ban" for "what should I do?".')
CLOSING = ('qin_xiao', '回头见！')
