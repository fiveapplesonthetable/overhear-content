# Authoring module for linden-courtyard-zh-s01e01-scene-07.
ID = 'linden-courtyard-zh-s01e01-scene-07'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'Tea and a Warm Cardigan  (热薄荷茶与暖羊毛衫)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'tessa': 'Tessa', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = '泰莎把受惊的伊芙琳请到温暖的咖啡角，端上热薄荷茶与蜂蜜，还拿出一件从未穿过的柔软羊毛开衫借给她应急；格雷厄姆则把那只神秘蓝箱子妥善锁好。先听一遍吧。'
OPENER = '现在让我们逐句品味这场充满人情味的傍晚对话。'
TRANSITION = '感受过这份热茶般的暖意后，我们再完整听一遍整场戏。'
OUTRO = '有了热薄荷茶和合身的羊毛开衫，伊芙琳终于安心上楼休息了。可到了夜里九点钟，庭院大门口突然响起了门铃声……我们下场戏见。'
CLOSING = ('tessa', 'Good night!')
STORY = [
    ('tessa', "Here you are, ma'am: hot mint tea and honey.", '女士，给您：热薄荷茶配蜂蜜。'),
    ('evelyn', 'Oh, thank you, Tessa. My hands were cold from the shock!', '噢，谢谢你，泰莎。刚才吓了一跳，我的手都是冰凉的！'),
    ('tessa', 'And look, this soft wool cardigan is clean and never worn. Try it on.', '您再看，这件柔软的羊毛开衫干干净净，还从来没穿过呢。您试穿一下吧。'),
    ('evelyn', 'Are you sure? It looks lovely and warm!', '你确定可以吗？它看起来又漂亮又暖和！'),
    ('graham', "It fits you very well, ma'am.", '女士，这件衣服您穿起来非常合身。'),
    ('evelyn', 'You good people are saving my whole trip.', '你们这些好心人真是挽救了我的整趟旅程。'),
    ('tessa', 'A traveler cannot sit upstairs sad on her first evening in Portland!', '哪能让远道而来的旅客在波特兰的第一个傍晚闷闷不乐地独坐楼上呢！'),
    ('graham', 'I locked the other blue suitcase safely in our luggage closet.', '我已经把另一只蓝色行李箱稳妥地锁进咱们的行李储物间了。'),
    ('evelyn', 'Thank you, Graham. That little wooden train inside looked old and precious.', '谢谢你，格雷厄姆。里面那列小木头火车看起来有些年头了，一定很珍贵。'),
    ('tessa', 'Whoever owns it will surely look for it soon.', '不管是谁的箱子，主人肯定很快就会来找它的。'),
    ('evelyn', 'I think I will sleep well tonight after all.', '我想今晚我终究还是能睡个好觉了。'),
    ('graham', "Rest well, ma'am. Ring down if you need anything.", '女士，祝您好好休息。如果您需要任何东西，请随时按铃叫楼下。'),
]
WALK = [
    (0, None, ["'女士，给您：热薄荷茶配蜂蜜。' 双手把茶点、钥匙或找零递到客人面前时，说一句", (None, 'Here you are'), '是最自然贴心的礼貌递物用语。']),
    (1, None, ["'噢，谢谢你，泰莎。刚才吓了一跳，我的手都是冰凉的！' 谈论喝茶前刚才的状态，英语把复数系动词换成过去式，说出", (None, 'My hands were cold'), '清楚交代刚才双手发凉，而此刻已经暖过来了。']),
    (2, None, ["'您再看，这件柔软的羊毛开衫干干净净，还从来没穿过呢。您试穿一下吧。' 试穿衣物时如果用代词指代那件衣服，代词必须夹在短语动词中间，说成", (None, 'Try it on'), '千万不能放到最后面。']),
    (3, None, ["'你确定可以吗？它看起来又漂亮又暖和！' 夸赞眼前的衣物好看时，用感官连系动词搭配形容词", (None, 'It looks lovely'), '注意这个以副词常见词尾收尾的词其实是纯正的形容词。']),
    (4, None, ["'女士，这件衣服您穿起来非常合身。' 形容衣服大小长短正合适，英语用衣服作主语、人作宾语，说出", (None, 'It fits you'), '简单三个词就夸得恰到好处。']),
    (5, None, ["'你们这些好心人真是挽救了我的整趟旅程。' 代词后面直接跟上形容词和复数名词构成同位称呼", (None, 'You good people'), '流露出长辈对大家仗义相助的真挚感激。']),
    (6, None, ["'哪能让远道而来的旅客在波特兰的第一个傍晚闷闷不乐地独坐楼上呢！' 英语里的方位词", (None, 'upstairs'), '本身就包含了“在楼上”的完整方位概念，直接跟在动词坐的后面，前面不用加任何介词。']),
    (7, None, ["'我已经把另一只蓝色行李箱稳妥地锁进咱们的行李储物间了。' 格雷厄姆用规则过去式", (None, 'I locked'), '向客人汇报箱子已经锁好，让人倍感踏实可靠。']),
    (8, None, ["'谢谢你，格雷厄姆。里面那列小木头火车看起来有些年头了，一定很珍贵。' 这个温情的形容词", (None, 'precious'), '专门用来形容饱含心意、不可替代的珍贵旧物，比单纯说价格昂贵更有温度。']),
    (9, None, ["'不管是谁的箱子，主人肯定很快就会来找它的。' 句首用复合代词", (None, 'Whoever'), '引出未知的主人，后半句则用短语动词', (None, 'look for'), '准确表达“寻找某物”的意思。']),
    (10, None, ["'我想今晚我终究还是能睡个好觉了。' 放在句末的短语", (None, 'after all'), '用来总结一波三折后的欣慰心情，相当于汉语的“说到底、终归还是”。']),
    (11, None, ["'女士，祝您好好休息。如果您需要任何东西，请随时按铃叫楼下。' 酒店服务中最经典的万金油礼貌从句就是", (None, 'if you need anything'), '让住客感到随时都有人照应。']),
]
