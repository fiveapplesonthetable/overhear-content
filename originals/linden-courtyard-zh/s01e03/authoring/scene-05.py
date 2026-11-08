# Authoring module for linden-courtyard-zh-s01e03-scene-05.
ID = 'linden-courtyard-zh-s01e03-scene-05'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = 'Half Price and Quiet Beams  (半价优惠与静谧木梁)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb', 'graham': 'Graham'}
INTRO = '汉娜和格雷厄姆领着凯勒布走上三楼阁楼房，向他说明今晚半价并附赠早餐。没想到凯勒布一眼就看中了屋顶的实木大梁和窗外隔绝车声的宁静。我们先完整听一遍。'
OPENER = '现在让我们放慢语速，一句一句细听凯勒布看房时的反应。'
TRANSITION = '理解了这些地道表达，我们按正常语速再完整听一遍。'
OUTRO = '原本棘手的重订风波圆满化解，凯勒布欣喜地收下了阁楼的小银钥匙。我们下场戏见。'
CLOSING = ('hannah', 'Good night!')
STORY = [
    ('hannah', 'Here we are, sir. Watch your head on this low wooden beam.', '先生，我们到了。当心这道低矮的木房梁碰着您的头。'),
    ('caleb', 'Oh... look at the proportions of this timber roof!', '噢……快看这木结构屋顶的比例多漂亮！'),
    ('graham', 'Solid oak, eighty years old. Not a single leak.', '实心橡木，八十年历史了。一处漏水都没有。'),
    ('hannah', 'Because of our mistake, tonight is half price, with breakfast included.', '由于我们的失误，今晚房费半价，并且包含早餐。'),
    ('caleb', 'Listen for a second... you cannot hear a single car from the street.', '仔细听一秒钟……街上一辆汽车的声音都听不到。'),
    ('hannah', 'Only the courtyard tree and the rain.', '只有庭院里的大树和雨声。'),
    ('caleb', 'To tell you the truth, I hate noisy first floor rooms. I love this space!', '跟你们说实话，我最讨厌吵闹的一楼房间了。我太喜欢这个空间了！'),
    ('graham', 'Really? You do not mind the extra stairs?', '真的吗？您不介意多爬这几段楼梯吗？'),
    ('caleb', 'Not at all! And this wide desk under the window is ideal for my work.', '一点儿也不介意！而且窗下这张宽敞的书桌做我的工作再理想不过了。'),
    ('hannah', 'What a relief! Here is your silver key, Caleb.', '真让人松了一口气！给您小银钥匙，凯勒布。'),
    ('caleb', 'Thank you both for being honest instead of sending me back into the rain.', '谢谢你们二位坦诚相待，而不是把我打发回大雨里去。'),
    ('graham', 'Sleep well, sir. Breakfast starts at seven thirty downstairs.', '睡个好觉，先生。早餐七点半在楼下开始供应。'),
]
WALK = [
    (0, None, ["'先生，我们到了。当心这道低矮的木房梁碰着您的头。' 走过低矮门框或阁楼斜顶时，最地道的贴心提醒就是", (None, 'Watch your head'), '用动词看护搭配你的头，简短有力地叫人“小心碰头”。']),
    (1, None, ["'噢……快看这木结构屋顶的比例多漂亮！' 英语区分不同用途的木材，专门用来做建筑房梁和屋架的厚重木料叫作", (None, 'timber'), '一听就透着内行建筑师的专业眼光。']),
    (2, None, ["'实心橡木，八十年历史了。一处漏水都没有。' 形容老房子、古树或人物的岁数，直接把数字、复数年份和形容词连成", (None, 'eighty years old'), '放在句中做补充说明，稳重又自豪。']),
    (3, None, ["'由于我们的失误，今晚房费半价，并且包含早餐。' 当后面紧跟的是名词短语“我们的失误”而不是完整句子时，必须加上介词说成", (None, 'Because of'), '礼貌交代打折补偿的原因。']),
    (4, None, ["'仔细听一秒钟……街上一辆汽车的声音都听不到。' 英语常借用泛指代词你来描述任何人在这个房间里的切身感受，说出", (None, 'you cannot hear'), '意思是“站在这儿一点儿车声都听不见”。']),
    (5, None, ["'只有庭院里的大树和雨声。' 英语习惯直接用名词修饰名词，", (None, 'courtyard tree'), '把庭院放在树的前面作定语，寥寥两词就勾勒出窗外雨打树叶的静谧画面。']),
    (6, None, ["'跟你们说实话，我最讨厌吵闹的一楼房间了。我太喜欢这个空间了！' 注意美式英语里的楼层叫法，临街的底层一楼直接叫作", (None, 'first floor'), '和汉语里说的“一楼”正好一一对应。']),
    (7, None, ["'真的吗？您不介意多爬这几段楼梯吗？' 用陈述语序配合上扬的疑问语调说出", (None, 'You do not mind'), '比生硬的一般疑问句更能传达格雷厄姆又惊又喜的确认语气。']),
    (8, None, ["'一点儿也不介意！而且窗下这张宽敞的书桌做我的工作再理想不过了。' 回答别人“你介意吗”的时候，最干脆爽朗的否定答复就是", (None, 'Not at all'), '意思是“完全不介意、一点儿都没关系”。']),
    (9, None, ["'真让人松了一口气！给您小银钥匙，凯勒布。' 悬着的心终于放下时，这句感叹短语", (None, 'What a relief'), '在日常口语里出现频率极高，地道表达“可算松了一大口气”。']),
    (10, None, ["'谢谢你们二位坦诚相待，而不是把我打发回大雨里去。' 表示“没有做某事，而是选择了另一种做法”，复合介词后面必须接动名词，说成", (None, 'instead of sending'), '清晰对比出客栈的厚道。']),
    (11, None, ["'睡个好觉，先生。早餐七点半在楼下开始供应。' 夜晚道别祝福客人安眠时，一句简单温暖的祈使短语", (None, 'Sleep well'), '亲切自然，相当于汉语里的“祝您好眠、睡个好觉”。']),
]
