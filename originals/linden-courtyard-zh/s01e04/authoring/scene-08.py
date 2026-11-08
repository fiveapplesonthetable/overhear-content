# Authoring module for linden-courtyard-zh-s01e04-scene-08.
ID = 'linden-courtyard-zh-s01e04-scene-08'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'The Boy on the Stairs  (台阶上的小男孩)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = '院子里，伊芙琳女士向汉娜讲起当年那个总坐在第三级木台阶上静静听琴的弟弟：每次雨天弹完琴，他都会好奇为什么下雨时钢琴声更温暖。话音未落，凯勒布走了出来，接上了二十五年前的答案！我们先完整听一遍。'
OPENER = '现在让我们放慢语速，逐句品味这场跨越二十五年的动人重逢。'
TRANSITION = '感受了这些饱含深情的英语表达，我们再连贯听一遍整场戏。'
OUTRO = '原来凯勒布就是当年坐在第三级台阶上听雨声与琴声的小男孩，而星期一晚上留在门阶上的那只蓝色行李箱正是他的！他到底藏着怎样的故事？我们下一集揭晓！'
CLOSING = ('caleb', 'Goodbye!')
STORY = [
    ('hannah', 'Tell me more about the two boys on Linden Street, Miss Evelyn!', '快跟我多讲讲菩提树街那两个小男孩的事吧，伊芙琳女士！'),
    ('evelyn', 'The older brother was bold and loud, always rushing through his music scales.', '哥哥性格大胆又热闹，每次练音阶总是风风火火地赶着弹完。'),
    ('hannah', 'And the younger brother with the wooden train?', '那拿着木头小火车的弟弟呢？'),
    ('evelyn', 'Quiet as a mouse! He sat on the third stair listening to every single note.', '安静得像只小老鼠！他总是坐在第三级台阶上，一字不落地听着每一个音符。'),
    ('hannah', 'Listening to the sound of the room... wait a second!', '倾听整个房间的声音……等一秒钟！'),
    ('evelyn', 'Whenever I finished playing, he asked why the piano sounded warmer when it rained.', '每当我弹完曲子，他就会问为什么下雨的时候钢琴听起来更温暖。'),
    ('caleb', 'Because wet wooden shutters soften the echo from the stone street...', '因为淋湿的木百叶窗柔化了石板街传来的回声……'),
    ('hannah', 'Caleb! Were you standing right there?!', '凯勒布！您刚才一直就站在那儿吗？！'),
    ('evelyn', 'Good heavens... look at your eyes! Little Caleb from the third stair?!', '我的天哪……快看看你的眼睛！第三级台阶上的小凯勒布？！'),
    ('caleb', "Miss Evelyn?! My brother's Friday piano teacher?!", '伊芙琳女士？！我哥哥星期五的钢琴老师？！'),
    ('hannah', 'Wait, then Monday night on our step... the second blue suitcase...', '等等，那星期一晚上留在咱们门阶上的……第二只蓝色行李箱……'),
    ('caleb', 'Yes, Hannah. That blue suitcase is mine, and I owe you both the whole truth.', '是的，汉娜。那只蓝色行李箱是我的，我欠你们二位全部的真相。'),
]
WALK = [
    (0, None, ["'快跟我多讲讲菩提树街那两个小男孩的事吧，伊芙琳女士！' 美式英语表示居住或位于某条街道上，固定搭配表面介词说出", (None, 'on Linden Street'), '街道名称首字母大写且前头不加定冠词。']),
    (1, None, ["'哥哥性格大胆又热闹，每次练音阶总是风风火火地赶着弹完。' 形容做事情急匆匆、图快走过场，用短语", (None, 'rushing through'), '把大男孩坐不住、急着弹完音阶出去玩的模样写活了。']),
    (2, None, ["'那拿着木头小火车的弟弟呢？' 英语没有单独一个词专指弟弟，而是用比较级加兄弟组成", (None, 'younger brother'), '清晰区分出家里年纪较小的弟弟。']),
    (3, None, ["'安静得像只小老鼠！他总是坐在第三级台阶上，一字不落地听着每一个音符。' 英语里有一句家喻户晓的经典比喻", (None, 'Quiet as a mouse'), '形容小孩或房间安安静静、一点声响都不出。']),
    (4, None, ["'倾听整个房间的声音……等一秒钟！' 脑海里突然闪过一道灵光、意识到两件事的关联时，喊出一句", (None, 'wait a second'), '汉娜瞬间想到了研究房间声学的凯勒布！']),
    (5, None, ["'每当我弹完曲子，他就会问为什么下雨的时候钢琴听起来更温暖。' 句首的时间引导词", (None, 'Whenever'), '表示“每当、无论何时”，用来讲述过去反复发生的美好默契；而动词完成后面必须接动名词形式，说成', (None, 'finished playing'), '绝不能换成动词不定式。']),
    (6, None, ["'因为淋湿的木百叶窗柔化了石板街传来的回声……' 形容词加上词尾变成及物动词，说出", (None, 'soften the echo'), '凯勒布用如今专业的声学建筑师语言回答了儿时的问题。']),
    (7, None, ["'凯勒布！您刚才一直就站在那儿吗？！' 惊讶地发现对方刚刚一直站在旁边听着，用过去进行时疑问句", (None, 'Were you standing'), '生动传达出猝不及防的惊喜。']),
    (8, None, ["'我的天哪……快看看你的眼睛！第三级台阶上的小凯勒布？！' 遇到意想不到的重逢或惊喜时，文雅又复古的感叹短语", (None, 'Good heavens'), '真切流露出老钢琴老师难以置信的激动。']),
    (9, None, ["'伊芙琳女士？！我哥哥星期五的钢琴老师？！' 一连串修饰语紧凑排开：", (None, "My brother's Friday piano teacher"), '先用所有格指明是我哥哥的，再说星期五和钢琴，重逢相认的一刻令人动容。']),
    (10, None, ["'等等，那星期一晚上留在咱们门阶上的……第二只蓝色行李箱……' 具体到某一天星期几的夜晚，可以直接把星期名词放在前面修饰夜晚，说成", (None, 'Monday night'), '口语里常常连介词都省去，紧凑推进悬念。']),
    (11, None, ["'是的，汉娜。那只蓝色行李箱是我的，我欠你们二位全部的真相。' 放在系动词后面独立表明归属时，必须使用名词性物主代词说出", (None, 'is mine'), '为第四集留下最扣人心弦的结尾！']),
]
