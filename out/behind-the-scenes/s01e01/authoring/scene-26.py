ID = 'behind-the-scenes-s01e01-scene-26'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 1
SCENE = 26
TITLE = '提前了录影时间  (Moved Up the Taping Time)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'bu_xiaogu': '布小谷', 'wang_er': '王尔', 'wen_simo': '闻思默'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E01'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e01.zh.srt'
INTRO = ('In the finale of Episode 1, Bu Xiaogu rushes to tell Wang Er that Chun Yuqiao moved the taping '
 'forward. As host Wen Simo welcomes real guest mentor Liu Fan on stage, Wang Er realises even he '
 'was kept completely in the dark. Listen first.')
OPENER = "Now let's unpack the final reveal of Episode 1 line by line."
STORY = [
 ('bu_xiaogu',
  '王尔老师，淳于总提前了录影时间！',
  'Teacher Wang Er, Director Chun Yu moved up the taping time!',
  [(881, '老师'), (882, '提前了录影')],
  '王尔老师 and 时间 correct the ASR homophones in cues 881-882.'),
 ('wang_er',
  '他根本就没有告诉我。',
  'He did not tell me at all.',
  [(883, '根本就没有告诉我')],
  'Added 他 for a clear complete sentence.'),
 ('wen_simo',
  '女士们，先生们，接下来！',
  'Ladies and gentlemen, up next!',
  [(886, '女士们 先生们'), (887, '接下来')],
  'Combined across cues 886-887.'),
 ('wen_simo',
  '有请本场十二歌王的客座导师，刘凡先生！',
  'Please welcome tonight\'s Twelve Singers guest mentor, Mister Liu Fan!',
  [(889, '有请'), (890, '十二歌王'), (891, '客座导师'), (894, '刘凡先生')],
  'Condensed from cues 889-894.'),
 ('wang_er',
  '也许从一开始，他就没打算过用我。',
  'Maybe right from the beginning, he never intended to use me.',
  [(895, '也许从一开始'), (896, '他就没打算过用我')],
  'Combined across cues 895-896.'),
 ('wang_er',
  '我就不该来当什么联合制作人。',
  'I never should have come to be some co-producer.',
  [(898, '来当什么联合制作人')],
  '不该 corrects the ASR homophone 不敢 in cue 898.'),
 ('wang_er',
  '在他眼里，我们都是工具。',
  'In his eyes, we are all tools.',
  [(899, '在他眼里'), (900, '我们都是工具')],
  'Combined across cues 899-900.'),
 ('wang_er',
  '只是他的一个棋子。',
  'Just one chess piece of his.',
  [(901, '他的一个棋子')],
  'Added 只是 for natural sentence flow.'),
]
WALK = [
 (0,
  None,
  "'Teacher Wang Er, Director Chun Yu moved up the taping time!' Useful \"tiqian\", literally 'lift ahead', means "
  'move a schedule earlier than planned.'),
 (1,
  None,
  "'He did not tell me at all.' Adding \"genben\" before \"meiyou\" intensifies a negative into 'not at all' or "
  "'never in the slightest', and \"gaosu\" means 'tell'."),
 (2,
  None,
  "'Ladies and gentlemen, up next!' Formal stage hosts open big moments with \"nvshimen\" and \"xianshengmen\" — "
  "'ladies, gentlemen', adding \"men\" onto each title to address the whole crowd."),
 (3,
  None,
  "'Please welcome tonight\'s Twelve Singers guest mentor, Mister Liu Fan!' Broadcast phrase \"youqing\" is the "
  "polished stage equivalent of 'please welcome to the stage', and \"daoshi\" means 'mentor'."),
 (4,
  None,
  "'Maybe right from the beginning, he never intended to use me.' Soft \"yexu\" means 'perhaps', \"cong yi kaishi\" "
  "means 'right from the start', and \"dasuan\" means 'intend' or 'plan to'."),
 (5,
  None,
  "'I never should have come to be some co-producer.' Regretful \"bugai\" shortens \"bu yinggai\" ('should not have'), "
  'while \"dang\" means serve as or work as a role.'),
 (6,
  None,
  "'In his eyes, we are all tools.' Frame someone's viewpoint with \"zai ta yanli\", literally 'inside his eyes', "
  'and \"gongju\" means a tool or instrument.'),
 (7,
  None,
  "'Just one chess piece of his.' Calling yourself someone's \"qizi\", 'chess piece' or 'pawn', captures how "
  'completely Chun Yuqiao outmanoeuvred both the spy and his own team.'),
]
TRANSITION = 'Now listen to the closing scene of Episode 1 once more.'
OUTRO = ('Chun Yuqiao outsmarted the leak and saved the show — leaving Xiaogu in awe and Wang Er quietly '
 'bitter. Congratulations on completing Episode 1 of Behind the Scenes! See you in Episode 2!')
CLOSING = ('bu_xiaogu', '再见！')
