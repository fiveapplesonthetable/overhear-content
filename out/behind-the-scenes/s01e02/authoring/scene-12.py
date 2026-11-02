ID = 'behind-the-scenes-s01e02-scene-12'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 12
TITLE = '哪怕是备用方案  (Even as Plan B)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'

INTRO = "Bu Xiaogu storms into the producer's office. She feels she has been tricked into wasting her time on a backup guest."

LABELS = {
    'bu_xiaogu': '布小谷',
    'chun_yuqiao': '淳于乔',
    'kaiwen': '凯文'
}

STORY = [
    ('bu_xiaogu', '这些笔迹，是我跟李铭基那边沟通的所有的细节的记录。', 'These notes are a record of all the details I communicated with Li Mingji.', [(433, '这些笔迹'), (434, '是我跟李铭记那边'), (435, '沟通的所有的细节的记录')], 'ASR "李铭记" -> "李铭基"'),
    ('bu_xiaogu', '包括每次被挂断的电话，被问到的所有的问题，', 'Including every phone call that was hung up, and all the questions asked,', [(436, '包括每次被挂断的电话'), (437, '被问到的所有的问题')], 'Punctuation supplied.'),
    ('bu_xiaogu', '还有李铭基提的所有的要求，我都一笔一画地写到上面。', 'And all the demands Li Mingji made, I wrote them all down stroke by stroke.', [(438, '还有李铭记提的所有的要求'), (439, '我都一笔一画地写到上面')], 'ASR "李铭记" -> "李铭基"'),
    ('bu_xiaogu', '我就想问问，我付出的这些时间，真的会有价值吗？', 'I just want to ask, will this time I put in really have value?', [(440, '我就想问问'), (441, '我付出的这些时间'), (442, '真的会有价值吗')], 'Punctuation supplied.'),
    ('bu_xiaogu', '哪怕是作为备用方案。', 'Even if just as a backup plan.', [(443, '哪怕是作为普兰比')], 'ASR "普兰比" -> "备用方案"'),
    ('bu_xiaogu', '其实每次要请什么艺人，问问粉团科技的吉秀不就好了吗？', 'Actually, every time you want to invite an artist, wouldn\'t it be fine just to ask Ji Xiu from Fentuan Tech?', [(444, '其实每次要请什么艺人'), (445, '问问粉团科技的急修'), (446, '不就好了吗')], 'ASR "急修" -> "吉秀"'),
    ('bu_xiaogu', '何必每次假装让底层的小员工做方案呢？', 'Why pretend to let lowly small employees make proposals every time?', [(447, '何必每次假装'), (448, '让底层的小员工'), (449, '做方案呢')], 'Punctuation supplied.'),
    ('bu_xiaogu', '就算再底层、再小的员工，也不愿意为此浪费自己的生命。', 'Even the lowest, smallest employee would not be willing to waste their life for this.', [(450, '就算再底层'), (451, '再小的员工'), (452, '也不愿意为此'), (453, '浪费自己的生命')], 'Punctuation supplied.'),
    ('chun_yuqiao', '滚出去。', 'Get out.', [(454, '滚出去')], 'Punctuation supplied.'),
    ('kaiwen', '误会，误会，误会。', 'Misunderstanding, misunderstanding, misunderstanding.', [(455, '误会 误会 误会')], 'Punctuation supplied.'),
    ('kaiwen', '刚才是杏子打电话过来，说辛惠美同意来参加半决赛，', 'Xingzi just called to say that Xin Huimei agreed to participate in the semifinal,', [(456, '刚才是杏子打电话过来'), (457, '说杏卫美同意'), (458, '来参加半决赛')], 'ASR "杏卫美" -> "辛惠美"'),
    ('kaiwen', '客座导师。当然因为演出还被雪藏，总决赛来不了。', 'As guest mentor. Of course, because her performances are still frozen, she cannot come to the finals.', [(459, '客座导师'), (460, '当然因为演出还被雪藏'), (461, '总决赛来不了')], 'Punctuation supplied.'),
    ('kaiwen', '所以第一方案还是李铭基。', 'So the first plan is still Li Mingji.', [(462, '所以A计划'), (463, '还是李明晋')], 'ASR "A计划" -> "第一方案", "李明晋" -> "李铭基"'),
    ('chun_yuqiao', '不用滚了，慢慢走着去吧。', 'No need to roll out, you can walk slowly.', [(464, '不用滚了'), (465, '慢慢走着去吧')], 'Punctuation supplied.')
]

CLOSING = ('kaiwen', '回头见！')

OPENER = "In the office, Xiaogu confronts Chun Yuqiao with pages of notes, thinking she was assigned busywork."

WALK = [
    (0, None, "'These notes are a record of all the details I communicated with Li Mingji.' She calls her notes \"biji\", literally 'pen tracks'."),
    (1, None, "'Including every phone call that was hung up, and all the questions asked.' She lists her frustrations, using \"baokuo\" for 'including'."),
    (2, None, "'And all the demands Li Mingji made, I wrote them all down stroke by stroke.' She emphasizes her meticulous effort with \"yibiyihua\", 'stroke by stroke'."),
    (3, None, "'I just want to ask, will this time I put in really have value?' She asks if her time will have \"jiazhi\", meaning 'value'."),
    (4, None, "'Even if just as a backup plan.' The phrase \"napa shi\" means 'even if it is'."),
    (5, None, "'Actually, every time you want to invite an artist, wouldn\\'t it be fine just to ask Ji Xiu from Fentuan Tech?' The phrase \"bu jiu hao le ma\" is a handy way to say 'wouldn\\'t it be fine?'."),
    (6, None, "'Why pretend to let lowly small employees make proposals every time?' She feels used, saying \"hebi\", meaning 'why bother' or 'there is no need'."),
    (7, None, "'Even the lowest, smallest employee would not be willing to waste their life for this.' The word \"jiusuan\", 'even if', sets up a hypothetical situation."),
    (8, None, "'Get out.' The phrase \"gun chuqu\" is a very harsh way to say 'get out'."),
    (9, None, "'Misunderstanding, misunderstanding, misunderstanding.' Kaiwen rushes in repeating \"wuhui\", 'misunderstanding', to defuse the situation."),
    (10, None, "'Xingzi just called to say that Xin Huimei agreed to participate in the semifinal.' He explains the sudden change, using \"gangcai\" for 'just now'."),
    (11, None, "'As guest mentor. Of course, because her performances are still frozen, she cannot come to the finals.' The superstar is \"xuecang\", 'snow hidden' or 'frozen', by her label."),
    (12, None, "'So the first plan is still Li Mingji.' He uses \"diyi fangan\" for 'first plan'."),
    (13, None, "'No need to roll out, you can walk slowly.' Chun Yuqiao retracts his harsh dismissal with dry sarcasm, saying \"buyong gun le\", 'no need to roll'." )
]

TRANSITION = "Let's listen to the whole argument again."
OUTRO = "Xiaogu's effort on Li Mingji turns out to be crucial for the finals. In this scene you learned how to stand your ground and clear up a misunderstanding."
