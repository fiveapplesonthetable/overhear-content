ID = 'behind-the-scenes-s01e02-scene-17'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = '决定留在星天  (Choosing to Stay at Xingtian)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'lin_jie': '林姐', 'bu_xiaogu': '布小谷'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'
INTRO = (
    'On the busy studio floor, Lin Jie reminds exhausted Bu Xiaogu that she still has gentler career '
    'options, prompting Xiaogu to phone Professor Fang with her final answer on DTS. Listen to their conversation first.'
)
OPENER = "Let's unpack what they say. Lin Jie checks the stage setup first and then speaks candidly with Xiaogu."
STORY = [
    (
        'lin_jie',
        '这边的灯光位置都调好了吗？',
        'Are the lighting positions over here all adjusted?',
        [(575, '位置都调好了')],
        'Expanded cue 575 into a direct check from Lin Jie.',
    ),
    (
        'bu_xiaogu',
        '调好了，林姐。',
        'They are all adjusted, Lin Jie.',
        [(575, '调好了')],
        'Short confirmation echoing cue 575.',
    ),
    (
        'lin_jie',
        '我听说你是传媒学院的好学生。',
        'I heard you are a strong student from Media College.',
        [(579, '我听说你是'), (580, '学院的')],
        '传媒学院 fixes ASR 崇利学院 in cue 580; 好学生 simplifies 尖子生.',
    ),
    (
        'lin_jie',
        '节目制作可是非常苦的。',
        'Show production is really tough work.',
        [(581, '节目制作可是非常苦的')],
        'Punctuation supplied for reading.',
    ),
    (
        'lin_jie',
        '这不比坐办公室那么舒服。',
        'This does not compare to sitting comfortably in an office.',
        [(582, '不比'), (583, '办公室')],
        'Simplified cues 582-583 for beginner clarity.',
    ),
    (
        'lin_jie',
        '其实你现在还有机会选。',
        'Actually you still have a chance to choose right now.',
        [(584, '其实你现在还有')],
        '机会选 paraphrases 还有得选 in cue 584.',
    ),
    (
        'lin_jie',
        '要是觉得太累，别勉强自己。',
        'If it feels too tiring, do not force yourself.',
        [(585, '要是觉得')],
        '别勉强自己 gives a clean A1 rendering of cue 586.',
    ),
    (
        'bu_xiaogu',
        '谢谢林姐，我想清楚了。',
        'Thank you, Lin Jie, I have thought it through clearly.',
        [],
        'Bridge before Xiaogu steps aside to call Professor Fang.',
    ),
    (
        'bu_xiaogu',
        '喂，方老师，不好意思，我的论文要晚交了。',
        'Hello, Professor Fang, sorry, I will hand in my thesis late.',
        [(605, '喂 方老师'), (606, '不好意思'), (607, '我的论文要晚交了')],
        'Combined across cues 605-607.',
    ),
    (
        'bu_xiaogu',
        '关于电视台那份工作，我已经决定了。',
        'Regarding that job at the television network, I have decided already.',
        [(609, '关于'), (610, '我已经决定了')],
        '电视台 replaces ASCII DTS in cue 609 so spoken Mandarin uses pure Chinese characters.',
    ),
    (
        'bu_xiaogu',
        '我要留在星天。',
        'I want to stay at Xingtian.',
        [(611, '我要留在星天')],
        'Punctuation supplied for reading.',
    ),
    (
        'bu_xiaogu',
        '就算从现场组做起，我也要做下去。',
        'Even starting from the floor crew, I will keep doing it.',
        [(613, '做起'), (614, '我也要做下去')],
        '现场组 fixes the ASR homophone 县长组 in cue 613.',
    ),
]
WALK = [
    (
        0,
        None,
        '\'Are the lighting positions over here all adjusted?\' Adding "hao" after an action word like "tiao", '
        '\'adjust\', signals that the job is properly finished, so "tiaohao" means \'adjusted and ready\'.',
    ),
    (
        1,
        None,
        '\'They are all adjusted, Lin Jie.\' Mandarin speakers usually answer yes-or-no questions by echoing the '
        'key action chunk "tiaohao le" instead of reaching for a separate word for \'yes\'.',
    ),
    (
        2,
        None,
        '\'I heard you are a strong student from Media College.\' Leading with "wo tingshuo", literally \'I hear '
        'say\', introduces secondhand news naturally, and "chuanmei xueyuan" is Media College.',
    ),
    (
        3,
        None,
        '\'Show production is really tough work.\' Slipping "keshi" before "feichang ku" adds an emphatic \'mind '
        'you, it really is\', where "ku" literally means \'bitter\' for grueling work.',
    ),
    (
        4,
        None,
        '\'This does not compare to sitting comfortably in an office.\' Using "bu bi" sets up a negative comparison, '
        'and "zuo bangongshi", \'sit in an office\', is shorthand for a desk job.',
    ),
    (
        5,
        None,
        '\'Actually you still have a chance to choose right now.\' Starting with "qishi", \'actually\', softens '
        'advice, while "haiyou jihui" reassures someone that the door is still open.',
    ),
    (
        6,
        None,
        '\'If it feels too tiring, do not force yourself.\' Conversational "yaoshi" means \'if\', and "bie '
        'mianqiang ziji" warmly tells someone not to push themselves against their will.',
    ),
    (
        7,
        None,
        '\'Thank you, Lin Jie, I have thought it through clearly.\' Combining "xiang", \'think\', with "qingchu", '
        '\'clear\', builds "xiang qingchu le" for having made up your mind.',
    ),
    (
        8,
        None,
        '\'Hello, Professor Fang, sorry, I will hand in my thesis late.\' Answering or starting a phone call begins '
        'with "wei", and polite "buhaoyisi" apologizes for handing in her "lunwen", \'thesis\', late.',
    ),
    (
        9,
        None,
        '\'Regarding that job at the television network, I have decided already.\' Opening with "guanyu", '
        '\'regarding\', sets the topic cleanly, and "yijing jueding le" announces a firm decision.',
    ),
    (
        10,
        None,
        '\'I want to stay at Xingtian.\' Short and resolute, "liuzai" joins "liu", \'stay\', with "zai", \'at\', '
        'to name the company she is choosing.',
    ),
    (
        11,
        None,
        '\'Even starting from the floor crew, I will keep doing it.\' Notice the pair "zuoqi", \'start doing from\', '
        'and "zuoxiaqu", \'keep on doing\', framed inside "jiusuan ... ye", \'even if ... still\'.',
    ),
]
TRANSITION = 'Now let us hear the whole conversation once more.'
OUTRO = (
    'Remembering Yuqiao\'s challenge, Xiaogu turns down the safe DTS offer and commits to proving herself '
    'at Xingtian from the ground up. You learned "ku" for tough work, "buhaoyisi" for polite apologies, '
    'and "jiusuan ... ye" for \'even if\'. See you next time!'
)
CLOSING = ('bu_xiaogu', '再见！')
