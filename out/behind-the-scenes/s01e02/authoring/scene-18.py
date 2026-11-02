ID = 'behind-the-scenes-s01e02-scene-18'
SHOW = 'behind-the-scenes'
SEASON = 1
EPISODE = 2
SCENE = 18
TITLE = '调整后台布局  (Redesigning the Backstage Layout)'
LEVEL = 'A1 — beginner'
PAIR = 'zh-en'
LABELS = {'lin_jie': '林姐', 'bu_xiaogu': '布小谷', 'crew': '场务'}
SOURCE_NAME = 'Behind the Scenes (幕后之王, 2019) S01E02'
SOURCE_FILE = 'sources/behind-the-scenes/s01/e02.zh.srt'
INTRO = (
    'Backstage at the studio, Bu Xiaogu spots a bottleneck in how the dressing rooms are arranged '
    'and pitches an overnight fix to Lin Jie right before Xin Huimei arrives. Listen to their conversation first.'
)
OPENER = "Let's unpack what they say. Xiaogu steps up to Lin Jie with an idea to make backstage traffic smoother."
STORY = [
    (
        'bu_xiaogu',
        '报告林姐，我有话想说。',
        'Reporting in, Lin Jie, I have something to say.',
        [(617, '报告林姐')],
        'Expanded cue 617 with a natural beginner lead-in.',
    ),
    (
        'bu_xiaogu',
        '我觉得后台的化妆间不太合理。',
        'I feel the backstage dressing rooms are not very reasonable.',
        [(618, '后台的化妆间'), (619, '合理')],
        'Condensed cues 618-619 for A1 clarity.',
    ),
    (
        'bu_xiaogu',
        '艺人走后台也不方便。',
        'It is inconvenient for the artists walking backstage too.',
        [(622, '后台的')],
        'Simplified cues 622-623; 艺人 fixes ASR 一人.',
    ),
    (
        'bu_xiaogu',
        '如果换一下房间，效率会高很多。',
        'If we swap the rooms around, efficiency will be much higher.',
        [(624, '如果'), (624, '房间'), (626, '效率会高很多')],
        '换一下 fixes ASR 废掉一下 (对调一下) in cue 625.',
    ),
    (
        'lin_jie',
        '现在录制太忙了，来不及调整。',
        'Right now taping is too busy, there is no time to adjust.',
        [(627, '现在'), (627, '录制'), (628, '太忙了'), (629, '来不及'), (630, '调整')],
        'Condensed across cues 627-630.',
    ),
    (
        'bu_xiaogu',
        '我可以负责安排，一个晚上就能做好。',
        'I can take charge of the setup and finish in one night.',
        [(631, '我可以负责'), (632, '一个晚上')],
        'Simplified cues 631-633 for beginner clarity.',
    ),
    (
        'bu_xiaogu',
        '我再请几个同事过来帮忙。',
        'I will also ask a few colleagues to come over and help.',
        [(634, '几个同事'), (635, '过来帮忙')],
        '请 replaces 借 in cue 634 for everyday clarity.',
    ),
    (
        'lin_jie',
        '你先画一张图，明天让我看一下。',
        'Draw a floor plan first and let me take a look tomorrow.',
        [(637, '图'), (638, '明天让我看一下')],
        'Simplified cues 636-638.',
    ),
    (
        'bu_xiaogu',
        '好的，林姐！',
        'Got it, Lin Jie!',
        [],
        'Crisp A1 reply replacing dialectal 好嘞 in cue 639.',
    ),
    (
        'lin_jie',
        '小谷，这个新布局真清楚，真棒！',
        'Xiaogu, this new layout is really clear, great job!',
        [(640, '小谷'), (641, '布局')],
        'Cleaned up cues 640-643.',
    ),
    (
        'crew',
        '林姐，辛惠美来了！',
        'Lin Jie, Xin Huimei has arrived!',
        [(648, '来了')],
        '辛惠美 fixes the ASR homophone 新会员 in cue 648.',
    ),
    (
        'lin_jie',
        '好，大家快去准备吧！',
        'Good, everyone go get ready right away!',
        [],
        'Closing action beat as the crew scrambles to welcome Xin Huimei.',
    ),
]
WALK = [
    (
        0,
        None,
        '\'Reporting in, Lin Jie, I have something to say.\' Playfully opening with "baogao", \'report\', sounds '
        'like an eager student raising her hand, while "you hua xiang shuo" means \'have something to say\'.',
    ),
    (
        1,
        None,
        '\'I feel the backstage dressing rooms are not very reasonable.\' Backstage is "houtai", literally \'rear '
        'stage\', and "huazhuangjian" joins "huazhuang", \'makeup\', with "jian", \'room\'.',
    ),
    (
        2,
        None,
        '\'It is inconvenient for the artists walking backstage too.\' Performers are called "yiren", and "bu '
        'fangbian", \'not convenient\', is a polite everyday way to point out a practical snag.',
    ),
    (
        3,
        None,
        '\'If we swap the rooms around, efficiency will be much higher.\' Adding "yixia" after "huan", \'swap\', '
        'makes the change sound quick and manageable, while "xiaolv" means \'efficiency\'.',
    ),
    (
        4,
        None,
        '\'Right now taping is too busy, there is no time to adjust.\' Essential chunk "laibuji" means \'not enough '
        'time to make it\', and "tiaozheng" is the word for \'adjust\'.',
    ),
    (
        5,
        None,
        '\'I can take charge of the setup and finish in one night.\' Volunteering with "wo keyi fuze", \'I can '
        'take responsibility\', shows initiative, and "jiu neng" stresses how quickly it can be done.',
    ),
    (
        6,
        None,
        '\'I will also ask a few colleagues to come over and help.\' Workplace peers are "tongshi", literally '
        '\'same affairs\', and "guolai bangmang" chains \'come over\' directly into \'help out\'.',
    ),
    (
        7,
        None,
        '\'Draw a floor plan first and let me take a look tomorrow.\' Flat sheets like maps, drawings, or charts '
        'count with "zhang", so "yi zhang tu" is \'one diagram\', softened at the end by "kan yixia".',
    ),
    (
        8,
        None,
        '\'Got it, Lin Jie!\' Brisk "haode" sounds warmer and more attentive than bare "hao" when acknowledging '
        'an instruction at work.',
    ),
    (
        9,
        None,
        '\'Xiaogu, this new layout is really clear, great job!\' Here "buju" means \'layout\', and exclaiming '
        '"zhen bang" is an enthusiastic way to say \'awesome\' or \'great job\'.',
    ),
    (
        10,
        None,
        '\'Lin Jie, Xin Huimei has arrived!\' Notice how "lai le", literally \'has come\', naturally covers '
        '\'has arrived\' or \'is here\' when announcing a guest.',
    ),
    (
        11,
        None,
        '\'Good, everyone go get ready right away!\' Addressing the whole group as "dajia", \'everyone\', plus '
        '"kuai qu zhunbei ba" rallies the team into action.',
    ),
]
TRANSITION = 'Now let us hear the whole conversation once more.'
OUTRO = (
    'Xiaogu\'s clear backstage floor plan wins Lin Jie\'s praise just as guest mentor Xin Huimei walks into '
    'the studio. You learned "houtai" for backstage, "huazhuangjian" for dressing room, and "laibuji" when '
    'time is too tight. See you next time!'
)
CLOSING = ('bu_xiaogu', '明天见！')
