ID = 'hidamari-ryokan-s01e05-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = '赤い印鑑の手紙  (The Red-Stamped Letter)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'yuka': '由香'}

INTRO = 'After welcoming Daiki into the courtyard so the brothers can talk privately, Mio slips back inside to the front desk, where Yuka watches happily and Takashi opens the registered envelope. Listen first.'

STORY = [
    ('yuka', '美央ちゃん、ガラス越しに見て！二人が木の下で向かい合って立っているよ！', 'Mio, look through the glass! The two of them are standing face to face under the tree!'),
    ('mio', '二人とも帰ったりしませんでしたね！陽翔さんが今、二つの椅子を指さしています！', 'Neither of them walked away! Right now Haruto is pointing at the two chairs!'),
    ('takashi', '素晴らしいですね……待っている間に、大家さんからの手紙にざっと目を通しましょう。', 'How wonderful... while we wait, let me glance through this letter from the landlord.'),
    ('yuka', 'どうせ通りの雨戸を塗り替えるとか、退屈なお知らせだよ。', 'It is probably some boring notice about repainting the street shutters.'),
    ('takashi', 'えっ……そんな。椅子はどこですか？膝の力が抜けてしまいました。', 'What... oh no. Where is my chair? My knees just went weak.'),
    ('mio', '隆さん！顔が真っ白ですよ！座ってください、手紙に何と書いてあるんですか？', 'Takashi! Your face went completely white! Sit down—what does the letter say?'),
    ('takashi', '美央さん、一番上の行を読んでください。私の眼鏡の見間違いだと言って！', 'Mio, please read the top line. Tell me my glasses are playing tricks on me!'),
    ('mio', '「物件売却のお知らせ。中庭八番館を、商業オフィス用として売却いたします。」', "'Notice of Property Sale: Number Eight Courtyard Building is offered for commercial office sale.'"),
    ('yuka', '商業オフィスとして売却！？私たちの旅館とキッチンを灰色の事務所にする気！？', 'Commercial office sale?! Turning our inn and kitchen into grey offices?!'),
    ('takashi', '新しい買い手が建物を調査するまで、猶予はたった三十日しかありません！', 'We only have thirty days before new buyers inspect the building!'),
    ('mio', '待ってください……このお知らせの裏に、折りたたまれた二枚目の紙が留めてあります……', 'Hold on... clipped to the back of this notice is a folded second page...'),
    ('takashi', '外の人にはまだ一言も言わないで！まずはあの兄弟に金曜日の午後を過ごさせてあげましょう！', 'Not a single word to anyone outside yet! Let those brothers have their Friday afternoon first!'),
]

OPENER = "A happy reunion outside collides with a sudden property crisis inside. Let's walk through six lines."

WALK = [
    (0, None, ["'Mio, look through the glass! The two of them are standing face to face under the tree!' Facing each other directly is ", (None, '向かい合って'), ', seen ', (None, 'ガラス越しに'), ", 'through the glass'."]),
    (2, None, ["'How wonderful... while we wait, let me glance through this letter from the landlord.' Reading quickly over a page uses the picturesque idiom ", (None, '目を通しましょう'), ", literally 'let one's eyes pass through'."]),
    (5, None, ["'Takashi! Your face went completely white! Sit down—what does the letter say?' Adding an intensifier prefix turns 'white' into ", (None, '真っ白'), ", 'pure white' or 'pale as a sheet', describing ", (None, '顔'), ", 'face'."]),
    (7, None, ["'Notice of Property Sale: Number Eight Courtyard Building is offered for commercial office sale.' Public announcements and letters start with ", (None, 'お知らせ'), ", the standard noun for a 'notice'."]),
    (9, None, ["'We only have thirty days before new buyers inspect the building!' Counting days reaches ", (None, '三十日'), ", 'thirty days', framed by ", (None, 'たった'), " for 'merely' or 'only'."]),
    (10, None, ["'Hold on... clipped to the back of this notice is a folded second page...' Flat sheets of paper use ", (None, '二枚目'), ", meaning 'the second page', tucked on ", (None, '裏'), ", 'the back side'."]),
]

TRANSITION = "Now let's hear the Episode 5 cliffhanger again from start to finish."

OUTRO = 'Outside under the tree two estranged brothers finally sit down together, while inside at the desk a thirty-day sale notice threatens the entire Hidamari Inn! Episode 5 is done—see you for the Season 1 finale in Episode 6.'

CLOSING = ('takashi', 'また会いましょう！')
