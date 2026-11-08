# Authoring module for linden-courtyard-zh-s01e03-scene-07.
ID = 'linden-courtyard-zh-s01e03-scene-07'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Returning the Notebook  (归还笔记本)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = '汉娜赶上三楼把皮面笔记本还给凯勒布。两人在阁楼门口聊起刚才那声奇怪的金属敲击声，一摸暖气片才发现下半截已经渐渐变凉了。我们先完整听一遍。'
OPENER = '现在放慢语速，逐句听听汉娜归还失物和应对突发状况的体贴表达。'
TRANSITION = '掌握了这些客气又自然的句式，我们再完整听一遍。'
OUTRO = '凯勒布温和通情达理，表示盖着厚毛毯很舒服，汉娜则立刻下楼请格雷厄姆去地下室检查锅炉。我们下场戏见。'
CLOSING = ('caleb', 'Have a good night!')
STORY = [
    ('hannah', 'Excuse me, Caleb? Sorry to disturb you.', '打扰一下，凯勒布？抱歉惊扰您休息了。'),
    ('caleb', 'Oh, my leather notebook! Thank you! I was just looking for it.', '噢，我的皮面笔记本！太谢谢你了！我正到处找它呢。'),
    ('hannah', 'You left it by the soup cup on the front counter.', '您把它落在前台柜台的汤杯旁边了。'),
    ('caleb', 'All my street notes from this week are in here. You saved me.', '我这一整周的街道笔记全在里面呢。你真是救了我大忙。'),
    ('hannah', 'We are glad you find our courtyard peaceful for your... work.', '我们很高兴您觉得我们的庭院安静平和，适合您的……工作。'),
    ('caleb', 'Very peaceful! Though did you hear a funny metal knock just now?', '非常宁静！不过你刚才有没有听到一声古怪的金属敲击声？'),
    ('hannah', 'Yes! It sounded like it came from the heating pipe in the corner.', '听到了！听起来像是从角落那根暖气管里传出来的。'),
    ('caleb', 'Feel the radiator. The bottom is warm, while the top is turning cool.', '摸摸这组暖气片。下半截还是暖的，上半截却正在变凉。'),
    ('hannah', 'Oh! Sometimes old pipes have a little air bubble at night.', '噢！有时候老管道到了夜里会有一点小气泡。'),
    ('caleb', 'I have a warm blanket, so I am quite comfortable tonight.', '我有一条暖和的毛毯，所以今晚住得很舒服。'),
    ('hannah', 'Thank you for being so patient! Graham will check the basement right away.', '谢谢您这么耐心体谅！格雷厄姆马上就去地下室检查。'),
    ('caleb', 'Good night, Hannah. See you at breakfast.', '晚安，汉娜。早餐时见。'),
]
WALK = [
    (0, None, ["'打扰一下，凯勒布？抱歉惊扰您休息了。' 夜晚敲门或打断别人忙事情时，最得体礼貌的开场白就是", (None, 'Sorry to disturb you'), '比普通的不好意思更显尊重与分寸感。']),
    (1, None, ["'噢，我的皮面笔记本！太谢谢你了！我正到处找它呢。' 表示寻找遗失的东西，英语要在动词看后面加上介词才变成寻找的意思，说成", (None, 'looking for it'), '配合过去进行时说明刚才一直在找。']),
    (2, None, ["'您把它落在前台柜台的汤杯旁边了。' 表示紧挨着某个小物件旁边，介词用法非常轻巧，直接说", (None, 'by the soup cup'), '就能精准指明“在汤杯旁边”。']),
    (3, None, ["'我这一整周的街道笔记全在里面呢。你真是救了我大忙。' 指着手里的本子说东西全装在里头，口语常把两个方位词叠用成", (None, 'in here'), '比单说一个在这里更有捧在手心的画面感。']),
    (4, None, ["'我们很高兴您觉得我们的庭院安静平和，适合您的……工作。' 这里的发现并不是找东西，而是采用宾语加宾语补足语结构", (None, 'you find our courtyard peaceful'), '表示亲身体验后“觉得庭院很宁静”。']),
    (5, None, ["'非常宁静！不过你刚才有没有听到一声古怪的金属敲击声？' 日常口语里的形容词", (None, 'funny'), '除了好笑滑稽之外，还经常用来表示“蹊跷的、有点不对劲的”。']),
    (6, None, ["'听到了！听起来像是从角落那根暖气管里传出来的。' 描述刚才听见的动静像是什么来头，在感官动词后面加上介词引导整句，说出", (None, 'It sounded like'), '地道表达“听上去好像是……”。']),
    (7, None, ["'摸摸这组暖气片。下半截还是暖的，上半截却正在变凉。' 描述温度或天气渐渐发生变化，英语常用转动一词作系动词，说出", (None, 'turning cool'), "细腻表现出热量正一点点散去的过程。"]),
    (8, None, ["'噢！有时候老管道到了夜里会有一点小气泡。' 英语一天早中晚的介词各有分工，唯独到了夜晚固定搭配小介词说成", (None, 'at night'), '而且中间绝不加定冠词。']),
    (9, None, ["'我有一条暖和的毛毯，所以今晚住得很舒服。' 副词修饰形容词组成", (None, 'quite comfortable'), '语气平和舒缓，传达出“相当舒适、完全够暖和了”的体谅。']),
    (10, None, ["'谢谢您这么耐心体谅！格雷厄姆马上就去地下室检查。' 感谢对方展现出的美好品质时，介词后接系动词的动名词形式，说出", (None, 'for being so patient'), '真诚致谢客人的宽容与耐心。']),
    (11, None, ["'晚安，汉娜。早餐时见。' 约好第二天早饭时段碰面，把三餐当作日常活动节点，搭配介词直接说", (None, 'at breakfast'), '简短自然，无需加任何冠词。']),
]
