ID = 'behind-the-scenes-s01e01-scene-13'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = '这是总编室  (This Is the Chief Editor\'s Office)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'chun_yuqiao': '淳于乔', 'wang_er': '王尔', 'bu_xiaogu': '布小谷'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E01'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e01.zh.srt'
INTRO = ('Still in the conference room, Chun Yuqiao scolds Wang Er for bringing a green intern to a '
 'production meeting. Bu Xiaogu speaks up to ask what the rules are, then worries outside that '
 'she was rude. Listen first.')
OPENER = "Let's unpack this tense first encounter. Chun Yuqiao draws a sharp line for Wang Er."
STORY = [
 ('chun_yuqiao',
  '想带新人随便，但是别带到制作会上来。',
  'Mentor newcomers all you like, but do not bring them to the production meeting.',
  [(384, '想带新人随便'), (385, '但是别'), (386, '带到制作会上来')],
  'Trimmed 给我 in cue 385 for clean beginner flow.'),
 ('wang_er',
  '小朋友才刚开始实习。',
  'The youngster has only just started her internship.',
  [(387, '小朋友'), (388, '才刚开始实习')],
  'Singular 小朋友 across cues 387-388.'),
 ('chun_yuqiao',
  '这是总编室，不是育儿室。',
  'This is the chief editor\'s office, not a nursery.',
  [(391, '这是总编室'), (392, '不是育儿室')],
  'Combined across cues 391-392.'),
 ('chun_yuqiao',
  '总编室是个讲究效率的地方。',
  'The chief editor\'s office is a place that cares about efficiency.',
  [(398, '总编室'), (399, '是个讲究效率的地方')],
  'Combined across cues 398-399.'),
 ('bu_xiaogu',
  '我也想问一下，实习多久才可以来这儿工作？',
  'I would also like to ask: how long must we intern before we may work here?',
  [(401, '我也想问一下'), (403, '多久'), (404, '才可以'), (405, '工作')],
  '实习 corrects ASR homophone 实行 across cues 401-405.'),
 ('bu_xiaogu',
  '我们先沟通好了，以免将来产生误会。',
  'Let us communicate clearly first, so we avoid misunderstandings in the future.',
  [(406, '我们先沟通好了'), (407, '以免将来产生误会')],
  'Combined across cues 406-407.'),
 ('wang_er',
  '见到你的大师兄了，感觉怎么样？',
  'Now that you have met your senior alumnus, how does it feel?',
  [(409, '见到你的大师兄了'), (410, '感觉怎么样')],
  'Trimmed initial words in cue 409 and combined with cue 410.'),
 ('bu_xiaogu',
  '我刚刚是不是太没礼貌了？',
  'Was I way too impolite just now?',
  [(412, '我刚刚是不是'), (413, '太没礼貌了')],
  'Combined across cues 412-413.'),
 ('wang_er',
  '你甭纠结，他基本上不会记得你是谁。',
  'Do not agonise over it — he basically will not remember who you are.',
  [(414, '你甭纠结'), (416, '基本上不会记得你是谁')],
  'Paired cues 414 and 416.'),
]
WALK = [
 (0,
  None,
  "'Mentor newcomers all you like, but do not bring them to the production meeting.' Blunt \"suibian\" means 'as you "
  "please' or 'suit yourself', followed by \"danshi bie...\", 'but don't...'."),
 (1,
  None,
  "'The youngster has only just started her internship.' Calling an intern \"xiaopengyou\", literally 'little friend', "
  'treats her like a kid, and \"cai gang\" stresses \'only just\'.'),
 (2,
  None,
  "'This is the chief editor\'s office, not a nursery.' Balanced \"zhe shi..., bushi...\" ('this is..., not...') "
  'delivers a razor-sharp contrast, turning \"yuershi\", \'childcare room\', into a sting.'),
 (3,
  None,
  "'The chief editor\'s office is a place that cares about efficiency.' Useful \"jiangjiu\" means be particular about "
  'standards, paired here with \"xiaolv\", \'efficiency\'.'),
 (4,
  None,
  "'I would also like to ask: how long must we intern before we may work here?' Notice \"duojiu\" for 'how long', "
  'followed by \"cai keyi\", which means \'only then is it permitted\'.'),
 (5,
  None,
  "'Let us communicate clearly first, so we avoid misunderstandings in the future.' Workplace staple \"goutong\" "
  "means 'communicate', and \"yimian\" is a slightly more formal cousin of \"miande\" for 'lest' or 'to avoid'."),
 (6,
  None,
  "'Now that you have met your senior alumnus, how does it feel?' An older male graduate from the same school or "
  'department is fondly called a \"dashixiong\", literally \'eldest martial brother\'.'),
 (7,
  None,
  "'Was I way too impolite just now?' For 'just now' a moment ago, reach for \"ganggang\", while \"mei limao\" "
  "literally says 'have no manners' for 'impolite'."),
 (8,
  None,
  "'Do not agonise over it — he basically will not remember who you are.' Northern colloquial \"beng\" fuses "
  '\"buyong\" (\'no need\') into one punchy syllable, and \"jiujie\" means twist yourself in knots worrying.'),
]
TRANSITION = "Now let's listen to the whole confrontation and hallway aftermath again."
OUTRO = ('Xiaogu stood her ground politely, even if her idol barely glanced her way. You heard "zhe shi..., '
 'bushi...", "duojiu" for "how long", and "mei limao" for "impolite".')
CLOSING = ('wang_er', '再见！')
