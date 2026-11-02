ID = 'behind-the-scenes-s01e01-scene-24'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = '只能取消通告  (We Have to Cancel the Booking)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'bu_xiaogu': '布小谷', 'xingzi': '杏子', 'agent': '经纪人'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E01'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e01.zh.srt'
INTRO = ('Panic hits Xingtian when Yin Zhengyu signs with the rival show. Bu Xiaogu immediately calls '
 'younger brother Yin Jiaxi\'s agent to activate her backup plan — only to receive a crushing blow. '
 'Listen first.')
OPENER = "Now let's walk through the crisis and the phone call."
STORY = [
 ('bu_xiaogu',
  '怎么了，杏子姐？',
  'What happened, Sister Xingzi?',
  [(793, '怎么了 杏子姐')],
  'Punctuation supplied for reading.'),
 ('xingzi',
  '尹正宇来不了这边，当然是有人泄露了消息。',
  'Yin Zhengyu cannot come to our side; obviously someone leaked the news.',
  [(795, '来不了这边'), (798, '当然是有人泄露了消息')],
  'Restored 尹正宇 from distorted ASR in cue 794 and paired cues 795 and 798.'),
 ('bu_xiaogu',
  '明天就要录节目了，那咱们怎么办啊？',
  'We are taping the show tomorrow — what do we do now?',
  [(800, '明天就要录节目了'), (801, '那咱们怎么办啊')],
  'Combined across cues 800-801.'),
 ('xingzi',
  '又不是只有一套方案。',
  'It is not as if we only have one plan.',
  [(802, '又不是只有一套')],
  'Replaced 节目 with 方案 for clarity on the backup plan.'),
 ('bu_xiaogu',
  '喂，你好，我是星天娱乐的布小谷。',
  'Hello, this is Bu Xiaogu from Xingtian Entertainment.',
  [(805, '喂 你好'), (806, '我是星天娱乐的布小谷')],
  'Combined across cues 805-806.'),
 ('bu_xiaogu',
  '现在我们已经确定要跟尹家希先生合作了。',
  'We have now confirmed that we want to work with Mister Yin Jiaxi.',
  [(809, '现在我们已经确定'), (810, '要跟尹家希先生合作了')],
  'Combined across cues 809-810.'),
 ('agent',
  '我们家希不可能跟星天合作了。',
  'There is no way our Jiaxi can work with Xingtian anymore.',
  [(813, '不可能'), (814, '跟星天'), (814, '合作了')],
  '家希 corrects the ASR homophone in cue 813.'),
 ('bu_xiaogu',
  '为什么？',
  'Why?',
  [(815, '为什么')],
  'Punctuation supplied for reading.'),
 ('agent',
  '他不能再上其他的节目，只能取消通告。',
  'He cannot appear on any other shows, so we can only cancel the booking.',
  [(821, '不能再上其他的节目'), (825, '只能取消通告')],
  'Paired cues 821 and 825.'),
]
WALK = [
 (0,
  None,
  "'What happened, Sister Xingzi?' Whenever someone rushes in with bad news, \"zenme\" in \"zenme le\" plus their "
  'name is the most natural expression for asking what went wrong.'),
 (1,
  None,
  "'Yin Zhengyu cannot come to our side; obviously someone leaked the news.' Notice \"lai bu liao\": here \"liao\" "
  "(not \"le\") follows \"lai bu\" to say circumstances make it impossible to come, and \"xiaoxi\" means 'news'."),
 (2,
  None,
  "'We are taping the show tomorrow — what do we do now?' Pairing \"mingtian\", 'tomorrow', with \"jiu yao... le\" "
  'stresses how close the deadline is — \'as soon as tomorrow!\'.'),
 (3,
  None,
  "'It is not as if we only have one plan.' Reassuring \"you bushi\", 'it isn't as though', reminds Xiaogu of "
  '\"zhiyou\", \'only have\', and measure word \"tao\" for a complete set or plan.'),
 (4,
  None,
  "'Hello, this is Bu Xiaogu from Xingtian Entertainment.' Answering or opening a telephone call starts with \"wei\" "
  '(pronounced rising second tone on the phone), followed immediately by \"ni hao\".'),
 (5,
  None,
  "'We have now confirmed that we want to work with Mister Yin Jiaxi.' Polite \"xiansheng\" after a man's name means "
  "'Mister', and \"hezuo\" is the standard word for collaborating or working together."),
 (6,
  None,
  "'There is no way our Jiaxi can work with Xingtian anymore.' Strong \"bu keneng\" slams the door shut: \"keneng\" "
  "means 'possible', so \"bu keneng\" means 'impossible'."),
 (7,
  None,
  "'Why?' Three syllables every beginner needs by heart: \"weishenme\", literally 'for what', asks 'why?'."),
 (8,
  None,
  "'He cannot appear on any other shows, so we can only cancel the booking.' Useful \"zhineng\", 'can only', shows "
  'having no other choice, and \"quxiao\" means cancel an appointment, flight, or TV booking \"tonggao\".'),
]
TRANSITION = 'Now listen to the whole phone-call crisis once more.'
OUTRO = ('Both Yin Zhengyu and Yin Jiaxi are blocked by the rival\'s exclusive clause, and Xiaogu blames '
 'herself. You learned phone greeting "wei", "lai bu liao", "weishenme", and "quxiao".')
CLOSING = ('bu_xiaogu', '下次见！')
