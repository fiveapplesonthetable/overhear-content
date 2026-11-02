ID = 'behind-the-scenes-s01e01-scene-12'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = '我在飞机上已经看过了  (I Already Read It on the Plane)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'xingzi': '杏子', 'wang_er': '王尔', 'chun_yuqiao': '淳于乔'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E01'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e01.zh.srt'
INTRO = ('A week later, senior producer Xingzi summons the team to Chun Yuqiao\'s conference room. Wang Er '
 'tries to let Bu Xiaogu present her guest-star data, only for Chun Yuqiao to cut them short. Listen first.')
OPENER = "Let's step through the production meeting. Xingzi gives Wang Er a precise countdown."
STORY = [
 ('xingzi',
  '王老师，二十二分钟之后总编室开会。',
  'Teacher Wang, there is a meeting in the chief editor\'s office in twenty-two minutes.',
  [(351, '老师'), (352, '二十二分钟之后'), (353, '开会')],
  '王老师 and 总编室 correct the ASR homophones in cues 351 and 353.'),
 ('wang_er',
  '此外就是客座明星的人选问题。',
  'Besides that, there is the question of choosing the guest star.',
  [(358, '此外就是'), (359, '客座明星的人选问题')],
  'Combined across cues 358-359.'),
 ('xingzi',
  '对手那边拼着命地跟我们抢人。',
  'The rival network is fighting tooth and nail with us to snap up talent.',
  [(365, '那边'), (366, '拼着命地跟我们抢人')],
  'Replaced the Latin rival acronym in cue 365 with 对手.'),
 ('wang_er',
  '这部分数据是实习助理布小谷做的。',
  'This section of data was prepared by intern assistant Bu Xiaogu.',
  [(369, '这部分数据'), (370, '是实习助理布小谷'), (371, '做的')],
  'Combined across cues 369-371.'),
 ('wang_er',
  '我觉得还是让她来讲解一下比较好。',
  'I think it would be better to have her explain it.',
  [(372, '我觉得还是'), (373, '来讲解一下比较好')],
  'Adapted pronoun spelling to 她 for Xiaogu across cues 372-373.'),
 ('xingzi',
  '淳于总是睡着了吗？',
  'Has Director Chun Yu fallen asleep?',
  [(374, '淳于总'), (375, '是睡着了吗')],
  'Combined across cues 374-375.'),
 ('wang_er',
  '这样吧，还是由我来亲自讲。',
  'How about this — let me explain it myself instead.',
  [(376, '这样吧'), (377, '还是由我来亲自讲')],
  'Combined across cues 376-377.'),
 ('chun_yuqiao',
  '王总，开什么玩笑呢？',
  'Director Wang, what kind of joke is this?',
  [(378, '王总'), (379, '开什么玩笑呢')],
  'Combined across cues 378-379.'),
 ('chun_yuqiao',
  '我在飞机上已经看过了，基本能过。',
  'I already read it on the plane; overall it passes.',
  [(380, '我在飞机上'), (380, '已经看过了'), (381, '基本能过')],
  'Trimmed repeated pronoun in cue 380 and combined with cue 381.'),
]
WALK = [
 (0,
  None,
  "'Teacher Wang, there is a meeting in the chief editor\'s office in twenty-two minutes.' Where English says 'in "
  "twenty-two minutes', Mandarin places \"zhihou\", 'after', right after the duration \"ershier fenzhong\"."),
 (1,
  None,
  "'Besides that, there is the question of choosing the guest star.' Formal meeting transition \"ciwai\" means "
  "'in addition', and \"renxuan\" literally combines 'person' and 'choice' for 'candidate'."),
 (2,
  None,
  "'The rival network is fighting tooth and nail with us to snap up talent.' Dramatic \"pinzhe ming\" literally "
  "means risking one's life, while \"qiang\" means snatch or compete fiercely for stars."),
 (3,
  None,
  "'This section of data was prepared by intern assistant Bu Xiaogu.' Wrapping an action in \"shi... de\" — here "
  '\"shi Bu Xiaogu zuo de\" — spotlights who did a completed job rather than just saying it was done.'),
 (4,
  None,
  "'I think it would be better to have her explain it.' Opening with \"juede\" in \"wo juede\", 'I think', and "
  'closing with \"bijiao\", \'comparatively\', gives you a polite way to float a suggestion.'),
 (5,
  None,
  "'Has Director Chun Yu fallen asleep?' Notice \"shuizhao\" with second-tone \"zhao\": adding \"zhao\" after "
  '\"shui\", \'sleep\', marks actually falling asleep rather than merely lying down.'),
 (6,
  None,
  "'How about this — let me explain it myself instead.' Quick \"zheyang ba\", literally 'like this, okay?', pivots "
  'smoothly when a plan changes, and \"qinzi\" means \'in person\'.'),
 (7,
  None,
  "'Director Wang, what kind of joke is this?' Mandarin splits the two-syllable expression \"kai wanxiao\", 'crack a "
  "joke', right down the middle to slip \"shenme\", 'what', inside it."),
 (8,
  None,
  "'I already read it on the plane; overall it passes.' Location \"zai feiji shang\", 'on the plane', comes before "
  'the action in Mandarin, and \"kanguo\" uses \"guo\" to mark past experience — having read it already.'),
]
TRANSITION = 'Now listen to the whole conference-room exchange again.'
OUTRO = ('Chun Yuqiao was wide awake the entire time — and he is far from pleased to see an untrained intern '
 'in his meeting. You heard "zhihou" for "after", "wo juede", and "kai wanxiao".')
CLOSING = ('xingzi', '回头见！')
