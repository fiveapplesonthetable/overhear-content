ID = 'behind-the-scenes-s01e02-scene-16'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 16
TITLE = '睡过头了  (Oversleeping in the Dorm)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'bu_xiaogu': '布小谷', 'qin_xiao': '秦箫'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'
INTRO = (
    'Back in their Media College dorm room, exhausted Bu Xiaogu wakes up late in the morning after '
    'her roommate Qin Xiao let her sleep through her alarm. Listen to their conversation first.'
)
OPENER = "Let's unpack what they say. Xiaogu bolts upright in bed the moment she checks the clock."
STORY = [
    (
        'bu_xiaogu',
        '啊？已经十一点了！',
        'What? It is already eleven!',
        [(560, '十一点了')],
        'Cleaned up ASR prefix 五点 before 十一点了 in cue 560.',
    ),
    (
        'bu_xiaogu',
        '秦箫，你怎么不叫我呀？',
        'Qin Xiao, how come you did not wake me up?',
        [(562, '你怎么不叫我呀')],
        'Added roommate name 秦箫 to replace garbled cue 561.',
    ),
    (
        'qin_xiao',
        '我发誓，我叫了你一百遍了。',
        'I swear, I called you a hundred times.',
        [(563, '我发誓'), (564, '我叫了你一百遍了')],
        'Combined across cues 563-564.',
    ),
    (
        'qin_xiao',
        '好吧，后来想想还是算了。',
        'Alright, on second thought I decided to let it go.',
        [(565, '好吧'), (566, '后来想想还是算了')],
        'Combined across cues 565-566.',
    ),
    (
        'qin_xiao',
        '你最近太累了，应该多睡一会儿。',
        'You have been too tired lately and should sleep a bit longer.',
        [],
        'Gentle A1 paraphrase of cue 567 about exhaustion.',
    ),
    (
        'qin_xiao',
        '你想吃什么？',
        'What would you like to eat?',
        [(568, '你想吃什么')],
        'Punctuation supplied for reading.',
    ),
    (
        'qin_xiao',
        '我去给你买。',
        'I will go buy it for you.',
        [(569, '我去给你买')],
        'Punctuation supplied for reading.',
    ),
    (
        'bu_xiaogu',
        '不用了，我现在没时间吃饭。',
        'No need, I have no time to eat right now.',
        [],
        'Natural A1 reply as Xiaogu scrambles out of bed.',
    ),
    (
        'bu_xiaogu',
        '昨晚我又不小心睡着了。',
        'Last night I accidentally fell asleep again.',
        [(570, '又不小心睡着了')],
        '昨晚 condenses 昨晚上 in cue 570.',
    ),
    (
        'bu_xiaogu',
        '我的论文还没写完呢。',
        'My thesis is still not finished yet.',
        [(571, '论文')],
        'Expanded cue 571 with 还没写完呢.',
    ),
    (
        'bu_xiaogu',
        '今天上班还迟到了！',
        'And I am late for work today too!',
        [(572, '上班还迟到了')],
        'Added 今天 for clarity.',
    ),
    (
        'qin_xiao',
        '那你快去吧，路上小心！',
        'Then hurry off, and take care on the way!',
        [],
        'Short send-off from roommate Qin Xiao.',
    ),
]
WALK = [
    (
        0,
        None,
        '\'What? It is already eleven!\' Clock hours in Mandarin simply pair the number with "dian", \'o\'clock\', '
        'so "shiyi dian" is \'eleven\', and "yijing ... le" underscores how late it has gotten.',
    ),
    (
        1,
        None,
        '\'Qin Xiao, how come you did not wake me up?\' Everyday "jiao" means both \'call\' and \'wake someone up\', '
        'while soft final "ya" keeps the complaint playful between friends.',
    ),
    (
        2,
        None,
        '\'I swear, I called you a hundred times.\' Opening with "wo fashi" means \'I swear\', and "yibai bian" '
        'counts a hundred full rounds of trying to wake her.',
    ),
    (
        3,
        None,
        '\'Alright, on second thought I decided to let it go.\' Conceding with "haoba" admits the truth, and '
        'versatile "suanle" shrugs off an effort with \'forget it\' or \'let it be\'.',
    ),
    (
        4,
        None,
        '\'You have been too tired lately and should sleep a bit longer.\' Putting "duo", \'more\', right before '
        'the action in "duo shui yihuir" is how Mandarin says \'sleep a little longer\'.',
    ),
    (
        5,
        None,
        '\'What would you like to eat?\' Notice how Mandarin leaves the question word in place: "ni xiang chi '
        'shenme" literally runs \'you want eat what\'.',
    ),
    (
        6,
        None,
        '\'I will go buy it for you.\' Slipping "gei ni", \'for you\', ahead of "mai", \'buy\', is the standard '
        'way to offer to pick something up for someone.',
    ),
    (
        7,
        None,
        '\'No need, I have no time to eat right now.\' Polite "buyong le" declines an offer warmly, and "mei '
        'shijian" is the go-to chunk for having no time.',
    ),
    (
        8,
        None,
        '\'Last night I accidentally fell asleep again.\' Literally, "bu xiaoxin" says \'not careful\' for doing '
        'something by accident, and "shuizhao" adds "zhao" onto "shui" to mean \'fall asleep\'.',
    ),
    (
        9,
        None,
        '\'My thesis is still not finished yet.\' Framing an unfinished task with "hai mei ... ne" means \'still '
        'have not yet\', while "xiewan" joins \'write\' with \'finish\'.',
    ),
    (
        10,
        None,
        '\'And I am late for work today too!\' Going to work is "shangban", literally \'step onto shift\', and '
        '"chidao" is the everyday word for \'arrive late\'.',
    ),
    (
        11,
        None,
        '\'Then hurry off, and take care on the way!\' Friends say "lushang xiaoxin", literally \'careful on the '
        'road\', whenever someone dashes out the door.',
    ),
]
TRANSITION = 'Now let us hear the whole conversation once more.'
OUTRO = (
    'Xiaogu rushes out of the dorm late for studio prep with her graduation thesis still unfinished. '
    'You learned how to tell the hour with "dian", say you fell asleep with "shuizhao", and talk about '
    'being late for work with "shangban chidao". See you next time!'
)
CLOSING = ('qin_xiao', '回头见！')
