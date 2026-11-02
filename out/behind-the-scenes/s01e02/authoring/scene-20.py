ID = 'behind-the-scenes-s01e02-scene-20'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 20
TITLE = '台上的质疑  (Questioning the Verdict Onstage)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'wen_simo': '闻思默', 'chun_yuqiao': '淳于乔', 'xin_huimei': '辛惠美'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'
INTRO = (
    'Host Wen Simo welcomes Xin Huimei and opens the Twelve Singers semifinal while Chun Yuqiao '
    'directs cameras from the control room, until Huimei challenges the show onstage. Listen to their conversation first.'
)
OPENER = "Let's unpack what they say. Wen Simo first ushers Xin Huimei backstage and then opens the live taping."
STORY = [
    (
        'wen_simo',
        '惠美老师，化妆间这边请。',
        'Mentor Huimei, dressing room right this way please.',
        [(650, '这边请')],
        'Incorporates merged backstage ushering cue 650; 化妆间 fixes ASR 报章间 in cue 649.',
    ),
    (
        'wen_simo',
        '欢迎大家来到十二歌王的现场！',
        'Welcome everyone to the live studio of Twelve Singers!',
        [(656, '来到现场'), (697, '十二歌王')],
        'Condensed stage opening across cues 656 and 697.',
    ),
    (
        'wen_simo',
        '现在我们的节目正式开始！',
        'Now our show officially begins!',
        [(660, '我们的节目正式开始')],
        'Added 现在 for spoken flow.',
    ),
    (
        'chun_yuqiao',
        '一号机准备，二号机看全景。',
        'Camera one get ready, camera two take the wide shot.',
        [(661, '一号机'), (662, '二号机全景')],
        'Simplified control-room camera call across cues 661-662.',
    ),
    (
        'chun_yuqiao',
        '灯光准备，开始吧。',
        'Lights get ready, let us start.',
        [(686, '灯光准备')],
        'Expanded cue 686 with 开始吧.',
    ),
    (
        'wen_simo',
        '所有歌手的表演已经全部结束了。',
        'All the singers have now finished their performances.',
        [(699, '表演已经全部')],
        '结束了 replaces formal 完毕了 in cue 699 for A1 clarity.',
    ),
    (
        'wen_simo',
        '白杨和倪徽，谁可以继续留在舞台呢？',
        'Between Bai Yang and Ni Hui, who can stay onstage?',
        [(701, '白杨和'), (702, '谁可以继续留在舞台')],
        '倪徽 fixes the ASR homophone 霓慧 in cue 701.',
    ),
    (
        'wen_simo',
        '下面有请导师辛惠美为我们点评。',
        'Next, please welcome mentor Xin Huimei to share her critique.',
        [(706, '有请'), (707, '导师'), (708, '辛惠美'), (709, '点评')],
        'Condensed cues 706-709.',
    ),
    (
        'xin_huimei',
        '我觉得选手白杨的声音非常美。',
        'I think contestant Bai Yang has a very beautiful voice.',
        [(710, '我觉得'), (710, '选手白杨'), (711, '声音非常美')],
        'Condensed cues 710-711.',
    ),
    (
        'wen_simo',
        '不过白杨刚才有点紧张，大家心里应该有结果了。',
        'Though Bai Yang was a little nervous just now, everyone probably has a verdict in mind.',
        [(719, '紧张'), (724, '结果了')],
        'Simplified cues 718-724 for beginner clarity.',
    ),
    (
        'xin_huimei',
        '你们既然都有结果了，还要我点评干什么？',
        'Since you already have a verdict, why ask me to critique at all?',
        [(725, '你们既然都有结果了'), (726, '还要我点评干什么')],
        'Combined across cues 725-726.',
    ),
    (
        'xin_huimei',
        '我的点评能改变结果吗？',
        'Can my critique change the outcome?',
        [(727, '我的点评能改变')],
        '结果 harmonizes with the preceding line.',
    ),
]
WALK = [
    (
        0,
        None,
        '\'Mentor Huimei, dressing room right this way please.\' Guiding a guest with "zhebian qing", literally '
        '\'this side please\', is polite hospitality you will hear in hotels, restaurants, and studios alike.',
    ),
    (
        1,
        None,
        '\'Welcome everyone to the live studio of Twelve Singers!\' Warm "huanying dajia" greets an audience '
        'or group of visitors, followed by "laidao", \'arrive at\'.',
    ),
    (
        2,
        None,
        '\'Now our show officially begins!\' Placing "zhengshi", \'officially\', right before "kaishi", \'begin\', '
        'gives a broadcast or ceremony a crisp opening.',
    ),
    (
        3,
        None,
        '\'Camera one get ready, camera two take the wide shot.\' Ordinal numbers form with "hao", \'number\', '
        'so "yi hao ji" is \'camera one\', while "quanjing" literally means \'full view\' for a wide shot.',
    ),
    (
        4,
        None,
        '\'Lights get ready, let us start.\' Stage lighting is "dengguang", built from \'lamp\' and \'light\', '
        'paired with "zhunbei", \'get ready\'.',
    ),
    (
        5,
        None,
        '\'All the singers have now finished their performances.\' Stage performances are "biaoyan", and stacking '
        '"quanbu", \'entirely\', before "jieshu le" emphasizes that every single singer is done.',
    ),
    (
        6,
        None,
        '\'Between Bai Yang and Ni Hui, who can stay onstage?\' Here "jixu" means \'continue\', and "wutai" '
        'joins \'dance\' with \'platform\' as the everyday word for \'stage\'.',
    ),
    (
        7,
        None,
        '\'Next, please welcome mentor Xin Huimei to share her critique.\' Hosts say "youqing" to invite a speaker '
        'or performer forward, and "dianping" means \'comment on\' or \'critique\'.',
    ),
    (
        8,
        None,
        '\'I think contestant Bai Yang has a very beautiful voice.\' Competition entrants are "xuanshou", '
        '"shengyin" is \'voice\' or \'sound\', and "mei" means \'beautiful\'.',
    ),
    (
        9,
        None,
        '\'Though Bai Yang was a little nervous just now, everyone probably has a verdict in mind.\' Putting '
        '"youdian" before an unpleasant feeling like "jinzhang", \'nervous\', means \'a bit too nervous\'.',
    ),
    (
        10,
        None,
        '\'Since you already have a verdict, why ask me to critique at all?\' Starting with "jiran", \'since\', '
        'sets up a pointed challenge, and trailing "gan shenme" snaps \'what for?\'.',
    ),
    (
        11,
        None,
        '\'Can my critique change the outcome?\' Action word "gaibian" means \'change\' or \'alter\', paired with '
        '"jieguo", \'outcome\' or \'result\'.',
    ),
]
TRANSITION = 'Now let us hear the whole conversation once more.'
OUTRO = (
    'Instead of playing along with the script, Xin Huimei challenges the show live onstage in front of the '
    'entire studio audience. You learned "zhebian qing" to guide a guest, "zhengshi kaishi" to open an event, '
    'and "gaibian jieguo" for changing an outcome. See you next time!'
)
CLOSING = ('wen_simo', '下次见！')
