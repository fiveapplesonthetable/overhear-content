ID = 'hidamari-ryokan-s02e01-scene-02'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 2
TITLE = '本を動かして  (Move the Books)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'yuka': '由香', 'kenji': '健二'}

INTRO = "In the quiet back hallway behind the kitchen, Mio and Kenji stand before a tall wooden bookcase packed with old travel guides. Yuka hurries out of the café corner wiping flour from her hands. Let's listen in first."

STORY = [
    ('yuka', '本当なの？私のキッチンの壁の後ろに、秘密の部屋があるの？', "Is it true? There's a secret room behind my kitchen wall?"),
    ('mio', '由香さん、手伝ってください。この緑の本を椅子に置きましょう。', "Yuka, please help me. Let's put these green books on the chair."),
    ('kenji', '一番上の棚からだ。そうすれば、本棚が軽くなる。', 'Start with the top shelf. That way the bookcase gets lighter.'),
    ('yuka', 'この旅行の本、私たち二人より古いよ、美央ちゃん！', 'These travel books are older than both of us, Mio!'),
    ('mio', 'これが最後の棚です。健二さん、三で引きますか？', 'This is the last shelf. Kenji, shall we pull on three?'),
    ('kenji', '一、二、三！左側をこっちに動かして！', 'One, two, three! Slide the left side toward me!'),
    ('yuka', '本棚の後ろを見て！白いペンキと、真鍮の鍵穴！', 'Look behind the bookcase! White paint and a brass keyhole!'),
    ('mio', '本物のドアです！ずっとこの廊下に隠れていたんですね！', 'A real door! It was hiding in this hallway all along!'),
    ('kenji', '杉の箱の大きい鍵を試してみよう。', "Let's try the big key from the cedar box."),
    ('yuka', '回る、健二さん？', 'Does it turn, Kenji?'),
    ('kenji', '右にしっかり一回……よし、開いたぞ！', "One firm turn to the right... there, it's open!"),
    ('mio', 'まず取っ手を上げてください。玄関のドアと同じです！', 'Lift the handle first. Just like the front door!'),
]

OPENER = "This scene is all action words: put, pull, slide, try, turn and lift. Let's walk through six lines."

WALK = [
    (0, None, ["'Is it true? There's a secret room behind my kitchen wall?' The word for 'secret' is ", (None, '秘密'), ", so a secret room is simply a 'secret's room' in Japanese."]),
    (2, None, ["'Start with the top shelf. That way the bookcase gets lighter.' Kenji's plan starts at the top ", (None, '棚'), ", the word for 'shelf'. Then the bookcase ", (None, '軽くなる'), ": 'light' plus 'become' means 'gets lighter'."]),
    (3, None, ["'These travel books are older than both of us, Mio!' To compare, Japanese puts the thing you measure against first, then ", (None, 'より古い'), ", literally 'than-old'. Swap in any describing word, like 'bigger than'."]),
    (6, None, ["'Look behind the bookcase! White paint and a brass keyhole!' The word for keyhole is ", (None, '鍵穴'), ", built from 'key' and 'hole', exactly like English."]),
    (8, None, ["'Let's try the big key from the cedar box.' Kenji says ", (None, '試してみよう'), ": 'try' plus 'let's see', a handy chunk for testing anything new."]),
    (11, None, ["'Lift the handle first. Just like the front door!' Mio remembers the inn's oldest trick. The word for a door handle is ", (None, '取っ手'), ", literally the 'grab-hand'."]),
]

TRANSITION = "Now let's listen to the whole bookcase scene again."

OUTRO = 'The heavy bookcase is aside and the hidden lock turns cleanly on the first try. Lift, pull, turn, open: those action words fit together nicely. See you next time.'

CLOSING = ('yuka', 'じゃあね！')
