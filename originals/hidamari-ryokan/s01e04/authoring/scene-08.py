ID = 'hidamari-ryokan-s01e04-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = '階段の三段目の男の子  (The Boy on the Stairs)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kazuko': '和子', 'mio': '美央', 'haruto': '陽翔'}

INTRO = 'Stepping out into the sunlit courtyard, Kazuko tells Mio more about the two brothers from Keyaki Lane, unaware that Haruto has walked quietly down the outdoor stairs right behind them. Listen first.'

STORY = [
    ('mio', '和子さん、けやき通りの兄弟のことをもっと教えてください！', 'Kazuko, please tell me more about the brothers on Keyaki Lane!'),
    ('kazuko', 'お兄ちゃんは元気で声が大きくて、いつも音階を急いで弾いていたわ。', 'The older brother was energetic and loud, always rushing through his musical scales.'),
    ('mio', '木の汽車を持っていた弟さんの方はどうでしたか？', 'And how about the younger brother with the wooden train?'),
    ('kazuko', 'とても静かな子でね！階段の三段目に座って、一音残らずじっと聞いていたの。', 'Such a quiet child! He sat on the third step of the stairs listening closely to every single note.'),
    ('mio', '部屋の響きに耳を澄ませていた……あっ、ちょっと待ってください！', 'Listening closely to the sound of the room... wait a second!'),
    ('kazuko', '弾き終わるといつも、「どうして雨の日はピアノの音が温かいの？」って聞くのよ。', "Whenever I finished playing, he always asked, 'Why does the piano sound warmer on rainy days?'"),
    ('haruto', '雨で濡れた木の雨戸が、石畳からの反響を柔らかくするからです……', 'Because wooden shutters wet from the rain soften the echo off the paving stones...'),
    ('mio', '陽翔さん！そこに立っていたんですか！？', 'Haruto! Were you standing right there?!'),
    ('kazuko', 'まあ、なんてこと……その目！階段の三段目の、小さな陽翔くん！？', 'Goodness gracious... those eyes! Little Haruto from the third step?!'),
    ('haruto', '和子先生！？金曜日の、兄のピアノの先生ですか！？', "Miss Kazuko?! My older brother's Friday piano teacher?!"),
    ('mio', '待ってください……じゃあ月曜の夜に石段にあった、二つ目の青いスーツケースは……', 'Wait... then Monday night on our stone step, that second blue suitcase...'),
    ('haruto', 'はい、美央さん。あの青いスーツケースは私のです。お二人に全部本当のことを話します。', 'Yes, Mio. That blue suitcase is mine. I will tell you both the whole truth.'),
]

OPENER = "Childhood memories meet the present right under the courtyard tree. Let's walk through six lines."

WALK = [
    (0, None, ["'Kazuko, please tell me more about the brothers on Keyaki Lane!' Asking for extra detail starts with ", (None, 'もっと'), ", meaning 'more', paired with ", (None, '教えてください'), " for 'please tell me'."]),
    (1, None, ["'The older brother was energetic and loud, always rushing through his musical scales.' You may know ", (None, '元気'), " from greetings meaning 'healthy and spirited', here paired with ", (None, '声が大きく'), ", literally 'his voice was big'."]),
    (5, None, ["'Whenever I finished playing, he always asked, Why does the piano sound warmer on rainy days?' Notice ", (None, '雨の日'), ", 'rainy days', and ", (None, 'ピアノの音'), " for 'the sound of the piano'."]),
    (8, None, ["'Goodness gracious... those eyes! Little Haruto from the third step?!' Boys and younger men are addressed affectionately with ", (None, 'くん'), ' after their given name, right as Kazuko recognises ', (None, 'その目'), ", 'those eyes'."]),
    (9, None, ["'Miss Kazuko?! My older brother's Friday piano teacher?!' Any respected teacher, doctor, or mentor is honoured with ", (None, '先生'), ", which Haruto attaches directly to Kazuko's name."]),
    (11, None, ["'Yes, Mio. That blue suitcase is mine. I will tell you both the whole truth.' Claiming ownership is clean and direct with ", (None, '私のです'), ", meaning 'it is mine', before promising ", (None, '本当のこと'), ", 'the truth'."]),
]

TRANSITION = "Now let's listen to the courtyard recognition cliffhanger again."

OUTRO = 'Little Haruto from the third stair is standing face to face with his childhood piano teacher—and the blue suitcase belongs to him! Episode 4 is complete; see you in Episode 5.'

CLOSING = ('haruto', 'また会いましょう！')
