ID = 'hidamari-ryokan-s01e03-scene-02'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = '屋根裏の部屋  (The Sunny Attic)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'mio': '美央', 'yuka': '由香'}

INTRO = "Up under the wooden eaves on the third floor, Kenji unlocks the attic room for Mio while Yuka climbs up with fresh towels. Let's listen to the whole scene first."

STORY = [
    ('mio', 'わあ、この部屋を見てください！太い木の梁と、中庭が見える窓です！', 'Wow, look at this room! Thick wooden beams and a window overlooking the courtyard!'),
    ('yuka', '屋根に当たる雨の音を聞いて。すごく居心地がいいね！', 'Listen to the sound of rain on the roof—it feels so cosy!'),
    ('kenji', '乾いているし、暖かいし、静かだ。さあ、足りない物を言ってみろ。', 'It is dry, warm, and quiet. Now tell me what is missing.'),
    ('mio', 'ええと、ベッドと机と椅子はありますが、枕元のランプがありません。', "Let's see: there are a bed, a desk, and a chair, yet there is no bedside lamp."),
    ('yuka', '壁に鏡もないし、床にラグがないから少し寂しいね。', 'There is no mirror on the wall either, and the floor feels bare without a rug.'),
    ('kenji', '下の作業場に、真鍮の読書ランプが一つあるぞ。', 'There is one brass reading lamp down in my workshop.'),
    ('yuka', '倉庫に柔らかい枕が二つと、青い織物のラグがあるよ！', 'And I have two soft pillows and a woven blue rug in the storeroom!'),
    ('mio', '隣の小さな洗面所はどうですか？電気はつきますか？', 'What about the small washroom next door? Does the light turn on?'),
    ('kenji', '先週、新しい電球に替えたし、石鹸もお湯もばっちりだ。', 'I put in a new lightbulb last week, and soap and hot water are all set.'),
    ('yuka', '十五分あれば、七号室より素敵な部屋になるよ！', 'Give us fifteen minutes and this will beat room seven!'),
    ('mio', '健二さん、その段ボール箱を持って！階段を下りましょう！', "Kenji, grab those cardboard boxes! Let's head down the stairs!"),
    ('kenji', '曲がり角に気をつけろよ、壁にぶつけるな！', 'Watch the corner on the stairs, do not bump the wall!'),
]

OPENER = "Checking furniture in a Japanese room teaches 'there is' alongside 'there is not'. Let's walk through six lines."

WALK = [
    (1, None, ["'Listen to the sound of rain on the roof—it feels so cosy!' Notice ", (None, '雨の音'), ", literally 'sound of rain', and ", (None, '居心地がいい'), ", a wonderful phrase meaning 'comfortable to stay in'."]),
    (3, None, ["'Let's see: there are a bed, a desk, and a chair, yet there is no bedside lamp.' Mio buys thinking time with ", (None, 'ええと'), ", 'let's see', then contrasts ", (None, 'ありますが'), ", 'there is', against ", (None, 'ありません'), ", 'there is not'."]),
    (4, None, ["'There is no mirror on the wall either, and the floor feels bare without a rug.' Room surfaces are easy to picture here: ", (None, '壁'), " means 'wall', ", (None, '鏡'), " means 'mirror', and ", (None, '床'), " means 'floor'."]),
    (6, None, ["'And I have two soft pillows and a woven blue rug in the storeroom!' Sleep vocabulary starts with ", (None, '柔らかい枕'), ", pairing 'soft' with 'pillow'."]),
    (7, None, ["'What about the small washroom next door? Does the light turn on?' In Japanese, ", (None, '電気'), ' covers both electricity and electric room lights, paired with ', (None, 'つきますか'), " to ask 'does it switch on?'."]),
    (8, None, ["'I put in a new lightbulb last week, and soap and hot water are all set.' When everything is spot-on and ready, casual speech loves ", (None, 'ばっちり'), ", meaning 'all set' or 'perfect'."]),
]

TRANSITION = "Now let's hear the whole attic inspection again."

OUTRO = "With timber beams and rain pattering overhead, the room only needs a brass lamp, two pillows, and a blue rug. See you next time as eight o'clock approaches."

CLOSING = ('yuka', 'じゃあね！')
