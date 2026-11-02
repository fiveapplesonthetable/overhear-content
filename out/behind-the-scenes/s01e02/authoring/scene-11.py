ID = 'behind-the-scenes-s01e02-scene-11'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = '敲定档期  (Landing Both Guests)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'

INTRO = "Bu Xiaogu is managing to confirm guest singer Li Mingji, just as her colleagues secure Xin Huimei."

LABELS = {
    'bu_xiaogu': '布小谷',
    'kaiwen': '凯文',
    'xingzi': '杏子'
}

STORY = [
    ('bu_xiaogu', '喂，您好，这里是星天娱乐。', 'Hello, this is Xingtian Entertainment.', [(415, '喂 您好'), (416, '这里是星天娱乐')], 'Punctuation supplied.'),
    ('bu_xiaogu', '凯文哥，已经敲定那边的档期，好。刚才提了好多要求啊。', "Brother Kaiwen, we've already finalized their schedule, good. They raised so many demands just now.", [(419, '凯文哥'), (420, '已经进那边的档期OK'), (421, '刚才提了好多要求啊')], 'ASR "进那边的档期OK" -> "敲定那边的档期，好"'),
    ('kaiwen', '喂，你说。', 'Hello, speak.', [(423, '喂 你说')], 'Punctuation supplied.'),
    ('xingzi', '辛惠美要来上节目了。', 'Xin Huimei is coming to appear on the program.', [(424, '幸会们要来上节目了')], 'ASR "幸会们" -> "辛惠美"'),
    ('kaiwen', '搞定？真的假的？', 'Done? Real or fake?', [(425, '搞定'), (426, '真的假的')], 'Punctuation supplied.'),
    ('kaiwen', '漂亮！', 'Beautiful!', [(430, '漂亮')], 'Punctuation supplied.'),
    ('kaiwen', '辛惠美搞定了！', 'Xin Huimei is settled!', [(431, '幸会没搞定了')], 'ASR "幸会没" -> "辛惠美"'),
    ('bu_xiaogu', '李铭基的事交给我了。', 'The Li Mingji matter is left to me.', [(432, '李铭记的事交给我了')], 'ASR "李铭记" -> "李铭基"')
]

CLOSING = ('kaiwen', '明天见！')

OPENER = "In the office, Bu Xiaogu finally gets a difficult guest star on the line."

TRANSITION = "Let's review the scene."

OUTRO = "They now have two guests booked."

WALK = [
    (0, None, "'Hello, this is Xingtian Entertainment.' She says \"zheli shi\", literally 'here is', followed by the company name."),
    (1, None, "'Brother Kaiwen, we've already finalized their schedule, good. They raised so many demands just now.' She confirms the booking using \"qiaoding\" for 'finalize'."),
    (2, None, "'Hello, speak.' Kaiwen picks up his own ringing phoneone and answers with \"wei\", 'hello'."),
    (3, None, "'Xin Huimei is coming to appear on the program.' Xingzi delivers the news using \"shang\", 'go up', for appearing on a show."),
    (4, None, "'Done? Real or fake?' He asks if it is \"zhende\", 'real', or \"jiade\", 'fake'."),
    (5, None, "'Beautiful!' The word \"piaoliang\" means 'beautiful', but it is also used to cheer a fantastic outcome."),
    (6, None, "'Xin Huimei is settled!' He announces the breakthrough with \"gaoding le\", meaning 'settled' or 'done'."),
    (7, None, "'The Li Mingji matter is left to me.' Xiaogu chimes in using \"jiao gei\", 'hand over to'.")
]
