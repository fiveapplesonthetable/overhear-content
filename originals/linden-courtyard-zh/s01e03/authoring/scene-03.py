# Authoring module for linden-courtyard-zh-s01e03-scene-03.
ID = 'linden-courtyard-zh-s01e03-scene-03'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Left at the Landing  (楼梯平台左转)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'arthur': 'Arthur'}
INTRO = '在众人的巧手布置下，阁楼房铺好了干净床单、摆上了蓝地毯，黄铜台灯也亮起了柔和的暖光。就在这时，楼下传来了庭院大门的铃声。我们先听一遍整场对话。'
OPENER = '现在放慢速度，一句一句品味他们布置房间和商量折扣的对话。'
TRANSITION = '掌握了这些鲜活口语，我们再连贯听一遍整场戏。'
OUTRO = '八点整，冒雨赶来的客人准时按响了门铃，汉娜胸有成竹地下楼去迎接。我们下场戏见。'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('tessa', 'Tuck that sheet corner tight, Hannah! Here go the two soft pillows.', '把那个床单角塞紧实，汉娜！这两个软枕头放这儿啦。'),
    ('hannah', 'Done! And the blue rug fits right beside the bed.', '搞定！而且这块蓝地毯放在床边正合适。'),
    ('arthur', 'Where should I hang this round mirror? Left of the window or right?', '我该把这面圆镜挂在哪儿呢？窗户左边还是右边？'),
    ('hannah', 'Right beside the desk, where the light is good.', '就挂在书桌旁边，那儿光线好。'),
    ('tessa', "Plug in Graham's brass lamp... oh, look how warm that yellow light is!", '插上格雷厄姆的黄铜台灯……噢，看那柔和的黄光多暖和呀！'),
    ('arthur', 'Honestly, I almost want to sleep up here myself tonight!', '老实说，今晚连我自己都差点想睡在这上面了！'),
    ('hannah', 'Wait, what discount should we offer him for changing rooms?', '等等，请他换房间，我们该给他什么折扣呢？'),
    ('arthur', 'Half price for tonight, and free breakfast all week!', '今晚房费半价，外加整周免费早餐！'),
    ('tessa', 'Generous! Did you just hear the courtyard gate bell downstairs?', '真慷慨！你们刚才听到楼下庭院大门的铃声了吗？'),
    ('hannah', "Eight o'clock on the dot! Our guest is here!", '八点整！我们的客人到了！'),
    ('arthur', 'My heart is pounding! Hannah, you explain it, you sound calm and honest!', '我的心怦怦直跳！汉娜，你来解释吧，你说话听起来沉稳又诚恳！'),
    ('hannah', 'Leave it to me. Let us go down and welcome him.', '包在我身上。咱们下楼去迎接他吧。'),
]
WALK = [
    (0, None, ["'把那个床单角塞紧实，汉娜！这两个软枕头放这儿啦。' 整理床铺时把床单边角整齐塞进床垫底下，英语有一句极其形象的动作指令", (None, 'Tuck that sheet corner tight'), '尾词用形容词紧实来说明塞好后的平整状态。']),
    (1, None, ["'搞定！而且这块蓝地毯放在床边正合适。' 在方位介词前面加上副词修饰，说成", (None, 'right beside'), '起到强调精准位置的作用，意思是“恰恰就在……旁边”。']),
    (2, None, ["'我该把这面圆镜挂在哪儿呢？窗户左边还是右边？' 征求别人摆放物品的意见时，用疑问词加情态动词说出", (None, 'Where should I hang'), '温和礼貌地询问“我该把它挂在哪里最合适”。']),
    (3, None, ["'就挂在书桌旁边，那儿光线好。' 在地点后面顺手补充说明那块区域的优点，英语直接跟关系副词引导的分句", (None, 'where the light is good'), '自然衔接“那里采光充足”。']),
    (4, None, ["'插上格雷厄姆的黄铜台灯……噢，看那柔和的黄光多暖和呀！' 把电器插头插进插座通电，日常固定使用短语动词", (None, 'Plug in'), '简单两个小词就把接通电源的动作说清楚了。']),
    (5, None, ["'老实说，今晚连我自己都差点想睡在这上面了！' 句尾加上反身代词", (None, 'myself'), '并不是做宾语，而是用来加强主语我的语气，凸显“连我本人都想住”。']),
    (6, None, ["'等等，请他换房间，我们该给他什么折扣呢？' 说明提供补偿或道谢的缘由时，介词后面直接跟动名词形式，说成", (None, 'for changing rooms'), '注意换房间牵涉两间房，因此客房一词习惯用复数。']),
    (7, None, ["'今晚房费半价，外加整周免费早餐！' 酒店住宿最实用的两个优惠表达：一个是干脆利落的", (None, 'Half price'), '表示半价折扣；另一个是', (None, 'free breakfast'), '表示免费赠送早餐，旅行入住时经常能听到。']),
    (8, None, ["'真慷慨！你们刚才听到楼下庭院大门的铃声了吗？' 确认就在一秒钟前刚发生的声响，美式英语常把一般过去时和副词连用，问出", (None, 'Did you just hear'), '语气急促又有现场感。']),
    (9, None, ["'八点整！我们的客人到了！' 形容时间分秒不差、准时到达，除了常见的整点表达，口语里说", (None, 'on the dot'), '更加生动，仿佛指针精准落在了刻度圆点上。']),
    (10, None, ["'我的心怦怦直跳！汉娜，你来解释吧，你说话听起来沉稳又诚恳！' 祈使句一般省略主语，但当需要明确指定“由你来做”时，特意保留代词说出", (None, 'you explain it'), '重音落在你身上，满是托付和信任。']),
    (11, None, ["'包在我身上。咱们下楼去迎接他吧。' 当别人把棘手的差事托付给你，自信又可靠地接下任务时，一句", (None, 'Leave it to me'), '地道传达出汉语里“交给我吧、包在我身上”的笃定。']),
]
