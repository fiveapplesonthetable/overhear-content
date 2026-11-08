# Authoring module for linden-courtyard-zh-s01e03-scene-08.
ID = 'linden-courtyard-zh-s01e03-scene-08'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Ice-Cold Pipes  (冰冷的水管)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '格雷厄姆从地下室检查回来，带来了一个坏消息：老锅炉上的黄铜压力阀彻底坏了。虽然厚砖墙能保住夜里的室温，但明早七点的淋浴水将会冰凉刺骨。先完整听一遍这段对话。'
OPENER = '现在让我们放慢语速，一句一句拆解他们连夜制定的抢修计划。'
TRANSITION = '理解了这些紧迫又生动的口语，我们再连贯听一遍。'
OUTRO = '全城只有桥那头的老五金店卖这种尺寸的黄铜阀门，而且明早七点整才开门。汉娜和格雷厄姆定好闹钟，准备明早跟冷水澡赛跑！我们下集见。'
CLOSING = ('graham', 'See you tomorrow!')
STORY = [
    ('arthur', 'Tell me it was just a tiny air bubble, Graham! Please!', '快告诉我那只是一个小气泡，格雷厄姆！拜托了！'),
    ('graham', 'Bad news. The brass pressure valve on the old boiler just gave up.', '坏消息。老锅炉上的黄铜压力阀刚刚彻底罢工了。'),
    ('hannah', 'Does that mean no radiators tonight, or no hot water too?', '那意思是今晚没暖气了，还是连热水也没有了？'),
    ('graham', 'The rooms will stay warm until morning, Hannah, because the brick walls hold heat.', '房间到明早都会一直保持暖和，汉娜，因为老砖墙能蓄热。'),
    ('arthur', 'Thank heavens! And the morning showers?', '谢天谢地！那明早的淋浴呢？'),
    ('graham', 'By tomorrow morning, the shower water will be ice cold.', '到明天早上，淋浴喷头里的水会像冰一样冷。'),
    ('arthur', 'Ice cold showers?! With the Portland Travel Guide inspector on the third floor?!', '冰水澡？！三楼还住着波特兰旅游指南的评审员呢？！'),
    ('hannah', 'Do you have a spare brass valve in your toolbox?', '你的工具箱里有备用的黄铜阀门吗？'),
    ('graham', 'Used my last one in winter. Only the old hardware shop past the bridge sells this size.', '冬天把最后一个用掉了。只有过了桥那家老五金店才卖这个尺寸。'),
    ('hannah', 'What time does that hardware shop open?', '那家五金店几点钟开门？'),
    ('graham', 'Seven sharp, half an hour before breakfast.', '七点整，就在早餐开始前半小时。'),
    ('hannah', 'Set your alarm, Graham. Tomorrow morning we beat the cold showers!', '定好你的闹钟，格雷厄姆。明天一早咱们抢在冷水澡前搞定它！'),
]
WALK = [
    (0, None, ["'快告诉我那只是一个小气泡，格雷厄姆！拜托了！' 满怀侥幸心理、盼着对方给出好消息时，口语常以祈使句开头说出", (None, 'Tell me'), '带着急切恳求的语气，意思是“快跟我说没事吧”。']),
    (1, None, ["'坏消息。老锅炉上的黄铜压力阀刚刚彻底罢工了。' 公布棘手情况先用短语", (None, 'Bad news'), '提醒大家做好心理准备；而说老旧机器零件坏掉报废，口语常拟人化地说它', (None, 'gave up'), '就像零件撑不住投降了一样形象。']),
    (2, None, ["'那意思是今晚没暖气了，还是连热水也没有了？' 在问句末尾轻轻加上副词", (None, 'too'), '把担忧往前推进一层，追问“是不是连热水也一并断了”。']),
    (3, None, ["'房间到明早都会一直保持暖和，汉娜，因为老砖墙能蓄热。' 表示持续处于某种温度或状态，用系动词停留搭配形容词，说成", (None, 'stay warm'), '比单纯说温暖更强调“一直保住热乎劲儿”。']),
    (4, None, ["'谢天谢地！那明早的淋浴呢？' 听到坏消息里总算还有一线转机时，老派又地道的感叹语", (None, 'Thank heavens'), '脱口而出，完美对应汉语里的“谢天谢地”。']),
    (5, None, ["'到明天早上，淋浴喷头里的水会像冰一样冷。' 英语喜欢用具体名词直接给形容词加戏，", (None, 'ice cold'), "字面就是像冰块一样冷，画面感十足地强调“冰凉刺骨”。"]),
    (6, None, ["'冰水澡？！三楼还住着波特兰旅游指南的评审员呢？！' 表示在建筑物的第几层楼上，英语一律使用表面接触介词，固定说成", (None, 'on the third floor'), '就像人站在那一层楼板上面一样。']),
    (7, None, ["'你的工具箱里有备用的黄铜阀门吗？' 询问有没有多余留着应急的零件或钥匙，最核心的形容词就是", (None, 'spare'), '放在名词前面直接表示“备用的、替换用的”。']),
    (8, None, ["'冬天把最后一个用掉了。只有过了桥那家老五金店才卖这个尺寸。' 买工具零件和水管配件的店铺叫作", (None, 'hardware shop'), '也就是五金店；而指路时用介词短语', (None, 'past the bridge'), '清晰说明位置在“走过桥之后再往前”的地方。']),
    (9, None, ["'那家五金店几点钟开门？' 询问商店营业或活动开始的具体钟点，用疑问词组加助动词说出", (None, 'What time does'), '后面紧跟单数主语和动词原形开门。']),
    (10, None, ["'七点整，就在早餐开始前半小时。' 强调时间一分不差，在数字后面直接跟上形容词锋利的，组成", (None, 'Seven sharp'), '地道干脆地表示“七点整、分秒不差”。']),
    (11, None, ["'定好你的闹钟，格雷厄姆。明天一早咱们抢在冷水澡前搞定它！' 睡前调好闹钟准备早起，英语固定用设定这个动词，说出", (None, 'Set your alarm'), '充满干劲地为第三集画上悬念十足的句号。']),
]
