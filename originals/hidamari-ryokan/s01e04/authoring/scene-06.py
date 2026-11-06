ID = 'hidamari-ryokan-s01e04-scene-06'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 4
SCENE = 6
TITLE = '音の建築家  (The Acoustic Architect)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'haruto': '陽翔', 'mio': '美央', 'yuka': '由香'}

INTRO = 'Out under the old shade tree in the courtyard, Haruto opens his brown leather notebook for Mio and Yuka while morning birds sing in the branches. Listen first.'

STORY = [
    ('haruto', 'このページをよく見てください。ホテルの星じゃなくて、デシベルと静けさを測っているんです！', 'Look closely at this page: it measures decibels and quietness, not hotel stars!'),
    ('mio', 'デシベルですか？じゃあ「九点」は、私の受付の点数じゃなかったんですね？', "Decibels? So 'nine points' was not a score for my check-in?"),
    ('haruto', '受付なら十点満点ですよ！実は私、音響の建築家なんです。', 'Your check-in deserves a full ten! Actually, I am an acoustic architect.'),
    ('yuka', '音響の建築家！コンサートホールを設計するの？', 'An acoustic architect! Do you design concert halls?'),
    ('haruto', '主に小さな図書館や中庭です。古い石の壁が通りの騒音をどう防ぐか調べています。', 'Mostly small libraries and courtyards. I study how old stone walls block street noise.'),
    ('mio', 'だから昨夜、屋根裏部屋で車の音を聞いていたんですね！', 'That explains why you listened for car sounds up in the attic last night!'),
    ('haruto', 'ええ。表の大通りはにぎやかなのに、この中庭では葉っぱと鳥の声だけが聞こえます。', 'Yes. The main street out front is lively, yet inside this courtyard you only hear leaves and birds.'),
    ('yuka', 'デシベルのことで一晩じゅう慌てていたなんて、隆さんが聞いたらびっくりするよ！', 'Takashi will be stunned when he hears he panicked all night over decibels!'),
    ('haruto', '本当を言うと、この町を選んだのには昔の家族の理由もあるんです。', 'To tell the truth, I also chose this neighbourhood for an old family reason.'),
    ('mio', 'えっ？昔、ご家族がこの近くに住んでいたんですか？', 'Oh? Did your family live near here once?'),
    ('haruto', '小さい頃、二つ先の通りに。金曜日は……私にとって大切な日なんです。', 'When I was small, two streets over. Friday is... an important day for me.'),
    ('yuka', 'ちょっと待って……今、金曜日って言った！？', 'Hold on... did he just say Friday?!'),
]

OPENER = "Jobs, city sounds versus courtyard quiet, and a sudden Friday clue connect two storylines. Let's walk through six lines."

WALK = [
    (2, None, ["'Your check-in deserves a full ten! Actually, I am an acoustic architect.' Combining 'building' and 'person' gives ", (None, '建築家'), ", 'architect', paired with ", (None, '音響'), " for 'acoustics'."]),
    (4, None, ["'Mostly small libraries and courtyards. I study how old stone walls block street noise.' Every town map marks ", (None, '図書館'), ", literally 'book-drawing hall' for 'library', a haven away from ", (None, '騒音'), ", 'noise'."]),
    (5, None, ["'That explains why you listened for car sounds up in the attic last night!' Connecting a cause you just realised uses ", (None, 'だから'), " right at the start of the sentence for 'that is why!'."]),
    (6, None, ["'Yes. The main street out front is lively, yet inside this courtyard you only hear leaves and birds.' Contrast ", (None, 'にぎやかな'), ", meaning 'bustling and lively', with gentle ", (None, '鳥の声'), ", literally 'voices of birds' for birdsong."]),
    (9, None, ["'Oh? Did your family live near here once?' Talking politely about someone else's relatives adds an honorific prefix in ", (None, 'ご家族'), ", 'your family', paired with ", (None, '住んでいた'), " for 'used to live'."]),
    (10, None, ["'When I was small, two streets over. Friday is... an important day for me.' Talking about childhood uses ", (None, '小さい頃'), ", literally 'when I was small'."]),
]

TRANSITION = "Now let's replay Haruto's courtyard revelation without stops."

OUTRO = "Haruto designs quiet courtyards—and his mention of 'two streets over' and 'Friday' made Mio and Yuka trade a wide-eyed look! See you next time."

CLOSING = ('yuka', 'じゃあね！')
