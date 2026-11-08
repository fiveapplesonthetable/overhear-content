# Authoring module for linden-courtyard-zh-s01e05-scene-04.
ID = 'linden-courtyard-zh-s01e05-scene-04'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Two Chairs Under the Tree  (树下的两把椅子)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '时间来到上午十一点二十分。汉娜、泰莎和格雷厄姆在老菩提树下悄悄布置出一张安静的角落小桌，连头顶的纸灯笼也重新捋直了。先完整听一遍吧。'
OPENER = '现在我们放慢脚步，逐句听听大家忙前忙后时的暖心对话。'
TRANSITION = '体会了格雷厄姆嘴硬心软的幽默，我们再完整听一遍整场戏。'
OUTRO = '庭院树下茶杯摆好，柠檬蛋糕正在晾架上散发甜香，而阁楼上的凯勒布已经紧张得换了三回衬衫。汉娜赶紧上楼去给他打气了，一会儿见。'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Let us put the small wooden table right here under the tree, away from the door.', '咱们把这张小木桌就放在树下这儿，离门口远一点。'),
    ('graham', 'Good spot. Two solid chairs, facing the garden herbs instead of the lobby window.', '好位置。放两把结实的椅子，朝向花园香草丛，避开前厅的窗户。'),
    ('tessa', 'Here is a clean white cloth and two blue teacups.', '这里是一块干净的白桌布，还有两只蓝茶杯。'),
    ('hannah', 'Graham, are you polishing those hanging paper lanterns for noon?', '格雷厄姆，您是为了中午重逢在擦亮那些悬挂的纸灯笼吗？'),
    ('graham', 'The wire needed straightening anyway. Nothing sentimental about good maintenance.', '反正铁丝本来也需要捋直了。日常维修保养可没什么好多愁善感的。'),
    ('tessa', 'Oh, listen to Mister Maintenance! Yesterday you fixed the boiler, today you fix two brothers!', '哟，听听这位维修先生说的！昨天您修好了锅炉，今天又来修补两兄弟的关系啦！'),
    ('graham', 'I fix pipes and chairs. People have to fix their own words.', '我只管修水管和椅子。人与人之间的话，得靠他们自己去修补。'),
    ('hannah', 'What time does your watch say now, Graham?', '您的手表现在显示几点了，格雷厄姆？'),
    ('graham', 'Eleven twenty. Cake ready, Tessa?', '十一点二十分。蛋糕烤好了吗，泰莎？'),
    ('tessa', 'Cooling on the rack right now, golden crust and sweet lemon sugar!', '这会儿正在晾架上放凉呢，金黄的表皮配上清甜的柠檬糖霜！'),
    ('hannah', 'Look upstairs at the attic window: Caleb has changed his shirt three times!', '快看楼上阁楼的窗户：凯勒布已经换了三次衬衫啦！'),
    ('tessa', 'Go talk to him, Hannah, before he wears out the wooden floor!', '快去跟他说说话吧，汉娜，再不去他都要把木地板踩穿了！'),
]
WALK = [
    (0, None, ["'咱们把这张小木桌就放在树下这儿，离门口远一点。' 安排座位想留出私密空间时，短语", (None, 'away from the door'), '简洁指明离出入口远一些、不受来往打扰的位置。']),
    (1, None, ["'好位置。放两把结实的椅子，朝向花园香草丛，避开前厅的窗户。' 这里的现在分词形式", (None, 'facing'), '紧跟在名词后面作修饰，贴切说明椅子正面朝着花园绿植的方向。']),
    (2, None, ["'这里是一块干净的白桌布，还有两只蓝茶杯。' 这个简短的单音节词", (None, 'cloth'), '既可以泛指布料，在布置餐桌的语境下也自然指代铺在桌面上的餐布或桌布。']),
    (3, None, ["'格雷厄姆，您是为了中午重逢在擦亮那些悬挂的纸灯笼吗？' 修饰庭院装饰时，分词加材质与名词组成", (None, 'hanging paper lanterns'), '层次分明地描绘出悬在半空中的纸灯笼。']),
    (4, None, ["'反正铁丝本来也需要捋直了。日常维修保养可没什么好多愁善感的。' 当物品需要被修整时，动词需要后面直接接动名词构成", (None, 'needed straightening'), '主动形式就自带“需要被拉直”的含义。']),
    (5, None, ["'哟，听听这位维修先生说的！昨天您修好了锅炉，今天又来修补两兄弟的关系啦！' 泰莎故意把头衔和职责连起来戏称他为", (None, 'Mister Maintenance'), '调侃他嘴上不承认，行动却比谁都热心。']),
    (6, None, ["'我只管修水管和椅子。人与人之间的话，得靠他们自己去修补。' 在所有格后面加上强调词构成", (None, 'their own words'), '朴实而深刻地道出解铃还须系铃人的道理。']),
    (7, None, ["'您的手表现在显示几点了，格雷厄姆？' 询问对方表上的时刻，英语习惯把手表当作说话的主语，问出", (None, 'What time does your watch say'), '听起来非常地道传神。']),
    (8, None, ["'十一点二十分。蛋糕烤好了吗，泰莎？' 熟人之间忙碌核对进度时，常省去系动词直接问两词短句", (None, 'Cake ready'), '干脆利落又合乎日常节奏。']),
    (9, None, ["'这会儿正在晾架上放凉呢，金黄的表皮配上清甜的柠檬糖霜！' 烘焙出炉后把糕点架空散热，固定使用介词短语", (None, 'on the rack'), '准确指明放在烤盘冷却架上面。']),
    (10, None, ["'快看楼上阁楼的窗户：凯勒布已经换了三次衬衫啦！' 英语表达三次及以上的次数时，直接用数词搭配复数名词说出", (None, 'three times'), '一语戳破凯勒布坐立不安的紧张劲儿。']),
    (11, None, ["'快去跟他说说话吧，汉娜，再不去他都要把木地板踩穿了！' 英语里的短语动词", (None, 'wears out'), '本意是用旧磨破，这里夸张打趣他在屋里来回踱步快把地板磨穿了。']),
]
