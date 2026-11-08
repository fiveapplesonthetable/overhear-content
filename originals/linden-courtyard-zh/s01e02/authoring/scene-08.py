# Authoring module for linden-courtyard-zh-s01e02-scene-08.
ID = 'linden-courtyard-zh-s01e02-scene-08'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Two Names, One Room  (两个名字，同一间房)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '傍晚雨声淅沥，亚瑟核对晚间入住名单时突然脸色发白：昨天他没戴老花镜在平板电脑上接预订，竟把两位互不相识的住客同时订进了七号房，而全店早已客满！先听一遍第二集压轴戏。'
OPENER = '现在让我们逐句拆解这场火烧眉毛的订房危机。'
TRANSITION = '理清了整桩乌龙的来龙去脉，我们再连贯听一遍现场原声。'
OUTRO = '门外大雨滂沱，八点整的晚班火车四十分钟后就要进站！汉娜灵机一动想到了三楼楼梯上方的阳光阁楼书房——他们能赶在客人进门前收拾妥当吗？明天见，我们后续剧集揭晓！'
CLOSING = ('arthur', 'See you tomorrow!')
STORY = [
    ('arthur', 'Graham... Hannah... please tell me room six is free tonight.', '格雷厄姆……汉娜……快告诉我今晚六号房还空着没人住。'),
    ('hannah', 'No, Arthur, the couple from the south checked into room six an hour ago.', '没有呀，亚瑟，从南方来的那对夫妇一小时前就已经登记入住六号房了。'),
    ('graham', 'Every key from one to seven is taken, and room eight has wet paint.', '从一号到七号的每一把钥匙都有主了，而且八号房刚刷了油漆还没干。'),
    ('arthur', 'Oh, disaster! Yesterday I took a phone booking on the tablet without my glasses!', '噢，大灾难呀！昨天我没戴眼镜在平板电脑上接了一笔电话预订！'),
    ('hannah', 'Wait, let me look at the tablet screen and the paper book together.', '等等，让我把平板屏幕和纸质登记簿放在一起对照看看。'),
    ('graham', 'Let me guess. You promised somebody a room we do not have?', '让我猜猜看。你把一间咱们根本没有的空房答应给别人了？'),
    ('hannah', 'Arthur! Room seven is already occupied, and you booked a second guest into room seven!', '亚瑟！七号房明明已经有人住了，你竟然又把第二位客人订进了七号房！'),
    ('arthur', "And he arrives on the eight o'clock evening train, in forty minutes!", '而且他坐的是晚上八点整那趟火车，还有四十分钟就到了！'),
    ('graham', 'Told you that tablet is a trap.', '早跟你说过那台平板电脑是个坑人的陷阱吧。'),
    ('arthur', 'It is raining outside and every hotel on our street is full! What do we do?', '外面正在下雨，咱们这条街上每一家酒店都住满了！这下我们该怎么办？'),
    ('hannah', 'Wait, what is on the third floor above the stairs?', '等等，楼梯上方的三楼那儿是什么地方？'),
    ('graham', 'The old sunny attic study... follow me, quickly!', '是那间向阳的老阁楼书房……快跟我来！'),
]
WALK = [
    (0, None, ["'格雷厄姆……汉娜……快告诉我今晚六号房还空着没人住。' 在酒店住宿语境里，短语", (None, 'is free tonight'), '不是说免费赠送，而是指房间今晚“空置、还没有安排客人入住”。']),
    (1, None, ["'没有呀，亚瑟，从南方来的那对夫妇一小时前就已经登记入住六号房了。' 办妥手续住进某间客房，英语固定使用动态介词短语", (None, 'checked into room six'), '配一般过去时交代一小时前已入住。']),
    (2, None, ["'从一号到七号的每一把钥匙都有主了，而且八号房刚刷了油漆还没干。' 两个短词组成的", (None, 'wet paint'), '正是公园长椅和装修房间门口最常见的提示语“油漆未干”。']),
    (3, None, ["'噢，大灾难呀！昨天我没戴眼镜在平板电脑上接了一笔电话预订！' 在电脑、手机或平板这类电子设备屏幕上操作时，英语一律选用介词组成", (None, 'on the tablet'), '首尾呼应了第一集找眼镜的伏笔。']),
    (4, None, ["'等等，让我把平板屏幕和纸质登记簿放在一起对照看看。' 表示共同的副词", (None, 'together'), '放在句尾，清楚表示把电子记录与手写账本“合在一块儿比对核查”。']),
    (5, None, ["'让我猜猜看。你把一间咱们根本没有的空房答应给别人了？' 看穿真相前先慢条斯理来一句", (None, 'Let me guess'), '是英语日常口语中温和调侃同伴出岔子的经典开场。']),
    (6, None, ["'亚瑟！七号房明明已经有人住了，你竟然又把第二位客人订进了七号房！' 名词“书”在这里直接充当规则动词用过去式说出", (None, 'you booked'), '意思是你办理了预订登记，把重房危机点得一清二楚。']),
    (7, None, ["'而且他坐的是晚上八点整那趟火车，还有四十分钟就到了！' 列车时刻表和早已确定的抵达行程，英语常直接用一般现在时", (None, 'he arrives'), '来表示板上钉钉即将发生的事。']),
    (8, None, ["'早跟你说过那台平板电脑是个坑人的陷阱吧。' 口语里常省掉主语我，直接用过去式开头说出", (None, 'Told you'), '相当于老朋友之间那句得意的“我早就提醒过你吧”。']),
    (9, None, ["'外面正在下雨，咱们这条街上每一家酒店都住满了！这下我们该怎么办？' 遇到棘手状况向同伴讨主意时，最地道的求助短句就是", (None, 'What do we do'), '用一般现在时迫切询问“咱们眼下怎么办”。']),
    (10, None, ["'等等，楼梯上方的三楼那儿是什么地方？' 美式英语从地面一楼算起，序数词短语", (None, 'on the third floor'), '指的就是整栋老客栈最顶上的三楼空间。']),
    (11, None, ["'是那间向阳的老阁楼书房……快跟我来！' 格雷厄姆立刻反应过来，一句干脆利落的祈使短语", (None, 'follow me'), '带着大家直奔阁楼救急，也为下一集埋下了精彩伏笔。']),
]
