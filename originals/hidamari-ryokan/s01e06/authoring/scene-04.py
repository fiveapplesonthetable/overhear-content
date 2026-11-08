ID = 'hidamari-ryokan-s01e06-scene-04'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = 'レモンケーキと鋭い目  (Lemon Cake and Sharp Eyes)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'yuka': '由香', 'daiki': '大輝', 'haruto': '陽翔'}

INTRO = 'Out in the courtyard, Yuka sets down a plate of warm glazed lemon cake for Daiki and Haruto. Between bites, observant older brother Daiki glances toward the lobby window. Listen first.'

STORY = [
    ('yuka', '焼きたてをお持ちしました！端っこ多めの、金曜日のレモンケーキですよ！', 'Fresh from the oven! Friday lemon cake with extra corner pieces!'),
    ('daiki', '一口食べるぞ……陽翔、目を閉じろ！おじいさんのケーキの味と全く同じだ！', 'One bite... Haruto, close your eyes! That tastes exactly like Grandfather\'s cake!'),
    ('haruto', '和子先生から金曜日の話を聞いて、由香さんが今朝焼いてくれたんだ。', 'After hearing our Friday story from Miss Kazuko, Yuka baked it for us this morning.'),
    ('daiki', 'お前は一体、どんな魔法みたいな旅館に迷い込んだんだ？', 'Just what kind of magical inn did you wander into, little brother?'),
    ('haruto', '雨の夜に屋根裏のランプを直して、見知らぬ人の鞄を守ってくれる宿さ。', "An inn that fixes attic lamps on a rainy night and guards a stranger's bag."),
    ('daiki', 'じゃあ教えてくれ。どうして受付の奥にいる優しそうな紳士は、今にも泣きそうなんだ？', 'Then tell me why the kind gentleman behind reception looks ready to cry any second?'),
    ('yuka', 'えっ！窓から隆さんが見えましたか？私、二倍広く笑ったつもりだったのに！', 'Oh! Did you spot Takashi through the window? Here I tried smiling twice as wide!'),
    ('haruto', '由香、中で何かあったの？またボイラーが壊れた？', '由香, is something wrong inside? Did the boiler break again?'),
    ('yuka', 'パイプより大変なの……正午に、建物の持ち主から書留の手紙が届いたんです。', 'Worse than a pipe... at noon a registered letter arrived from the building owner.'),
    ('daiki', '不動産の手紙ですか？陽翔と私に見せてください。私は市役所で契約を担当していますし、弟は保存法に詳しい！', 'A property letter? Please let Haruto and me see it: I handle contracts at City Hall, and my brother knows heritage law!'),
    ('haruto', 'えっ、兄さん……今も市役所の契約課で働いているの！？', 'Wait, brother... you still work in the contract division at City Hall?!'),
    ('yuka', 'お二人とも！？湯呑みはそのままでいいから、今すぐ中へ来て！', 'Both of you?! Leave your teacups right there and come inside this very second!'),
]

OPENER = "Taste, tears, and a City Hall surprise turn the tide in the courtyard. Let's walk through six lines."

WALK = [
    (1, None, ["'One bite... Haruto, close your eyes! That tastes exactly like Grandfather\'s cake!' Talking about food flavour uses ", (None, '味'), ", meaning 'taste' or 'flavour', paired with ", (None, '全く同じ'), " for 'completely identical'."]),
    (3, None, ["'Just what kind of magical inn did you wander into, little brother?' Notice ", (None, '魔法みたいな'), ", literally 'like magic', built on ", (None, '魔法'), " for 'magic'."]),
    (5, None, ["'Then tell me why the kind gentleman behind reception looks ready to cry any second?' Adding a look-alike ending onto 'cry' creates ", (None, '泣きそうな'), ", 'looking about to cry'."]),
    (9, None, ["'A property letter? Please let Haruto and me see it: I handle contracts at City Hall, and my brother knows heritage law!' Municipal offices are called ", (None, '市役所'), ", 'City Hall', and ", (None, '詳しい'), " means 'well-informed' or 'expert in'."]),
    (10, None, ["'Wait, brother... you still work in the contract division at City Hall?!' Everyday conversation about where someone works uses ", (None, '働いている'), ", from 'to work'."]),
    (11, None, ["'Both of you?! Leave your teacups right there and come inside this very second!' Leaving something untouched as it is uses the handy chunk ", (None, 'そのままで'), '.']),
]

TRANSITION = "Now let's hear the courtyard turning point again."

OUTRO = "Haruto knows historic preservation rules AND Daiki works in municipal contracts at City Hall! Let's hurry inside to the front desk next time."

CLOSING = ('yuka', 'じゃあね！')
