# Authoring module for linden-courtyard-zh-s01e02-scene-03.
ID = 'linden-courtyard-zh-s01e02-scene-03'
SHOW = 'linden-courtyard-zh'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Counting the Change  (分毫不差的找零)'
LEVEL = 'A1 — 入门级'
PAIR = 'en-zh'
LABELS = {'hannah': 'Hannah', 'arthur': 'Arthur', 'tessa': 'Tessa'}
INTRO = '只用了九分钟，汉娜就拎着两大袋食材气喘吁吁地跑回了前台，连找回的零钱都分毫不差。可泰莎一摸黄油包装纸，却发现了一个新意外！先完整听一遍吧。'
OPENER = '下面我们逐句拆解这段账目清点与厨房急中生智的对话。'
TRANSITION = '听明白了海盐黄油怎么化险为夷，我们再连贯听一遍整场戏。'
OUTRO = '不配甜果酱的海盐黄油，拿来炒鸡蛋反而成了绝妙美味！大家长舒一口气，厨房里顿时热闹起来。先再见啦，我们下场戏见。'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('hannah', 'Nine minutes! Here are the milk, the eggs, and the apples!', '九分钟！牛奶、鸡蛋和苹果全都买回来啦！'),
    ('tessa', 'You are a hero, Hannah! Give me the milk first for the coffee machine.', '汉娜，你真是大救星！快先把牛奶给我加进咖啡机里。'),
    ('arthur', 'Impressive speed! Did the shopkeeper give you a receipt?', '速度真惊人！杂货铺老板给你开收据了吗？'),
    ('hannah', 'Right here! Everything cost thirty-eight, so here is twelve in change.', '就在这儿！所有东西一共花了三十八美元，所以这是找回的十二美元零钱。'),
    ('arthur', 'Ten, eleven, twelve. Exact to the last coin, thank you!', '十块、十一、十二块。精确到最后一枚硬币，太谢谢你了！'),
    ('tessa', 'Wait a second, Hannah... which pack of butter did you grab?', '等一下，汉娜……你刚才随手拿的是哪一包黄油？'),
    ('hannah', 'The gold wrapper on the top shelf. Why?', '最上面那层货架上金色包装纸的那块呀。怎么啦？'),
    ('tessa', 'That is extra salty sea butter! My sweet jam rolls need plain butter!', '那可是特咸的海盐黄油！我的甜果酱面包卷需要原味黄油呀！'),
    ('hannah', 'Oh no! All the wrappers looked the same when I was running!', '噢糟糕！我刚才一路小跑，所有包装纸看起来全都一个样！'),
    ('arthur', 'Can we serve salty butter with sweet strawberry jam?', '咱们能拿咸黄油配甜草莓果酱端给客人吗？'),
    ('tessa', 'Wait, salty butter is terrible for jam, but amazing for scrambled eggs!', '等等，咸黄油配果酱糟透了，可拿来做炒鸡蛋简直绝了！'),
    ('hannah', 'Phew! Quick thinking saves breakfast again.', '呼——好险！急中生智又一次拯救了早餐。'),
]
WALK = [
    (0, None, ["'九分钟！牛奶、鸡蛋和苹果全都买回来啦！' 当递上或展示不止一样物品时，句首倒装结构要把系动词换成复数，说出", (None, 'Here are'), '清脆响亮地报出战果。']),
    (1, None, ["'汉娜，你真是大救星！快先把牛奶给我加进咖啡机里。' 朋友或同事在紧要关头帮了大忙，英语口语最爱夸对方是", (None, 'a hero'), '热情洋溢又特别接地气。']),
    (2, None, ["'速度真惊人！杂货铺老板给你开收据了吗？' 动词给后面接双宾语", (None, 'give you a receipt'), '先说收票的人“你”，再说物品“一张收据”，语序和汉语完全一致。']),
    (3, None, ["'就在这儿！所有东西一共花了三十八美元，所以这是找回的十二美元零钱。' 请留心花费动词", (None, 'cost'), '的过去式和原形长得一模一样；句末固定搭配', (None, 'in change'), '专门表示结账找回来的零钱。']),
    (4, None, ["'十块、十一、十二块。精确到最后一枚硬币，太谢谢你了！' 亚瑟一边数钱一边夸赞", (None, 'to the last coin'), '生动形容账目算得分毫不差、一分钱也没错。']),
    (5, None, ["'等一下，汉娜……你刚才随手拿的是哪一包黄油？' 在货架上几种包装之间询问具体哪一种时，用疑问词搭配量词说出", (None, 'which pack'), '比宽泛地问什么更精准。']),
    (6, None, ["'最上面那层货架上金色包装纸的那块呀。怎么啦？' 货架表面属于平面接触，因此英语选用介词组成", (None, 'on the top shelf'), '指明是在最顶上一层搁板上拿的。']),
    (7, None, ["'那可是特咸的海盐黄油！我的甜果酱面包卷需要原味黄油呀！' 烘焙和餐桌上说不加额外海盐或香料的普通黄油，固定用形容词搭配说出", (None, 'plain butter'), '表达起来朴素又直接。']),
    (8, None, ["'噢糟糕！我刚才一路小跑，所有包装纸看起来全都一个样！' 表示几样东西外观毫无二致，感官动词后接定冠词短语", (None, 'looked the same'), '记住相同这个词前面永远少不了定冠词。']),
    (9, None, ["'咱们能拿咸黄油配甜草莓果酱端给客人吗？' 征求大家能不能这样上菜救急时，用情态动词开头提问", (None, 'Can we serve'), '后面紧跟要端上餐桌的食物。']),
    (10, None, ["'等等，咸黄油配果酱糟透了，可拿来做炒鸡蛋简直绝了！' 西式早餐桌上出场率最高的词组就是", (None, 'scrambled eggs'), '特指把蛋液搅匀炒得松软嫩滑的炒鸡蛋。']),
    (11, None, ["'呼——好险！急中生智又一次拯救了早餐。' 危机解除时先长舒一口气发出拟声感叹词", (None, 'Phew'), '紧接着用动名词词组', (None, 'Quick thinking'), '夸赞泰莎脑子转得快、临场应变妙。']),
]
