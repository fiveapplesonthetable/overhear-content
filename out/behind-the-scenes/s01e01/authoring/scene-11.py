ID = 'behind-the-scenes-s01e01-scene-11'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = '四百个小时的录像  (Four Hundred Hours of Footage)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'wang_er': '王尔', 'bu_xiaogu': '布小谷', 'xiaoye': '小叶'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E01'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e01.zh.srt'
INTRO = ('Moments later, Wang Er drops a mountain of binders and hard drives onto Bu Xiaogu\'s desk so she '
 'can prepare for next week\'s meeting with Chun Yuqiao. Listen first.')
OPENER = "Let's break down each line. Wang Er walks over with Xiaogu's first real assignment."
STORY = [
 ('wang_er',
  '小谷，准备好和淳于乔开会。',
  'Xiaogu, get ready to have a meeting with Chun Yuqiao.',
  [(333, '小谷'), (335, '准备好和淳于乔开会')],
  'Trimmed ASR surname prefix in cue 333.'),
 ('bu_xiaogu',
  '现在吗？',
  'Right now?',
  [(336, '现在')],
  'Added 吗 so the single-word surprised question is unmistakable.'),
 ('wang_er',
  '下个星期的这个时候，我们要从现在就开始准备。',
  'This time next week — we need to start preparing right from now.',
  [(337, '下个星期的这个时候'), (339, '我们要从现在就开始准备')],
  'Combined cues 337 and 339.'),
 ('wang_er',
  '这些资料，还有这四百个小时的录像资料。',
  'These files, plus these four hundred hours of video recordings.',
  [(340, '这些资料'), (341, '还有这四百个小时的'), (342, '录像资料')],
  'Combined across cues 340-342.'),
 ('wang_er',
  '你要全部研究清楚。',
  'You need to study all of it thoroughly.',
  [(343, '你要全部研究清楚')],
  'Punctuation supplied for reading.'),
 ('bu_xiaogu',
  '没有问题！',
  'No problem at all!',
  [(344, '没有问题')],
  'Punctuation supplied for reading.'),
 ('xiaoye',
  '用不着了，下周你就死了。',
  'You will not need that drink anymore — next week you are dead.',
  [(347, '用不着了'), (348, '下周你就死了')],
  'Combined across cues 347-348.'),
 ('bu_xiaogu',
  '下周我就死了？',
  'Next week I am dead?',
  [(349, '下周我就死了')],
  'Punctuation supplied for reading.'),
 ('xiaoye',
  '待会儿你就知道了。',
  'In a little while you will find out.',
  [(350, '待会儿你就知道了')],
  'Punctuation supplied for reading.'),
]
WALK = [
 (0,
  None,
  "'Xiaogu, get ready to have a meeting with Chun Yuqiao.' Adding \"hao\" right after \"zhunbei\", 'prepare', shows "
  'the preparation is complete and solid — \'get fully ready\'.'),
 (1,
  None,
  "'Right now?' Dropping \"ma\" onto \"xianzai\", 'now', turns a single time word into a startled yes-or-no question."),
 (2,
  None,
  "'This time next week — we need to start preparing right from now.' Notice how Chinese says 'next week' using "
  '\"xiage xingqi\", literally \'the downward week\', while \"cong xianzai\" means \'from now\'.'),
 (3,
  None,
  "'These files, plus these four hundred hours of video recordings.' Conversational \"haiyou\" means 'and also' or "
  "'plus', and \"sibai\" puts \"si\", 'four', before \"bai\", 'hundred'."),
 (4,
  None,
  "'You need to study all of it thoroughly.' Putting \"qingchu\", 'clear', directly after \"yanjiu\", 'research' or "
  "'study', expresses studying the material until every detail is clear."),
 (5,
  None,
  "'No problem at all!' Earlier we heard brisk \"mei wenti\"; keeping the full \"meiyou\" in \"meiyou wenti\" sounds "
  'extra emphatic and eager to impress a boss.'),
 (6,
  None,
  "'You will not need that drink anymore — next week you are dead.' Handy \"yongbuzhao\" means 'have no need for', "
  'and \"xiazhou\" is a brisk two-syllable way to say \'next week\'.'),
 (7,
  None,
  "'Next week I am dead?' Xiaogu only swaps \"ni\", 'you', to \"wo\", 'I', and raises her pitch — Mandarin often "
  'echoes a statement with rising intonation to ask an incredulous question.'),
 (8,
  None,
  "'In a little while you will find out.' Remember \"daihuir\" (often pronounced \"daihuir\" with fourth tone in the "
  "north) for 'in a moment', paired with \"zhidao\", 'know' or 'find out'."),
]
TRANSITION = "Now let's hear the whole assignment scene once more."
OUTRO = ('Xiaogu dives straight into four hundred hours of footage so she will be ready for next week\'s meeting. '
 'You learned "xianzai", two ways to say "next week", and "meiyou wenti".')
CLOSING = ('bu_xiaogu', '下次见！')
