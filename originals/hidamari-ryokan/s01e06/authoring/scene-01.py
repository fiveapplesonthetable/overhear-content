ID = 'hidamari-ryokan-s01e06-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = '鉄の門の前で  (At the Iron Gate)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'haruto': '陽翔', 'daiki': '大輝', 'mio': '美央'}

INTRO = 'Out under the shade tree at the Hidamari Inn in Osaka, older brother Daiki stands stiffly in his dark grey coat across from Haruto as Mio sets down a hot teapot and steps politely aside. Listen to the whole scene first.'

STORY = [
    ('daiki', 'やっぱり「祖父の物を預けた誰か」はお前だったんだな、陽翔。', "So 'somebody with something of Grandfather's' really was you all along, Haruto."),
    ('haruto', 'こんにちは、大輝兄さん。今日は来てくれてありがとう。', 'Hello, big brother Daiki. Thank you for coming today.'),
    ('daiki', 'あのハガキの几帳面な四角い字、二秒でお前の字だとわかったよ。', 'That neat square handwriting on the postcard—I knew it was yours in two seconds.'),
    ('haruto', 'えっ……私からだとわかっていて、それでも来てくれたの？', 'Wait... you knew it was from me and came anyway?'),
    ('daiki', '当たり前だろ。どうして謎のメモなんかに隠れたんだ？', 'Of course I came. Why did you hide behind a mystery note?'),
    ('haruto', '兄さんがまだ怒っていると思って怖かったんだ。この三年間、ずっと会いたかった。', 'Because I was afraid you were still angry. All these three years, I missed you.'),
    ('daiki', '意地を張った三年間だな……正直に言うと、俺もお前に会いたかったよ。', 'Three stubborn years... to tell the truth, I missed you too.'),
    ('mio', '失礼いたします。温かいお茶でございます。焼きたてのレモンケーキもすぐ参りますね。', 'Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on its way right now.'),
    ('daiki', 'レモンケーキ？待てよ……どうしてこの人が金曜日のレモンケーキを知っているんだ？', 'Lemon cake? Hold on... how does she know about Friday lemon cake?'),
    ('haruto', '座ってよ、兄さん。重いコートを脱いで、この青いスーツケースを見て。', 'Have a seat, brother. Take off your heavy coat and look at this blue suitcase.'),
    ('daiki', 'それ、おじいちゃんの作業場にあった古い紺色の鞄じゃないか？', "Isn't that the old dark-blue bag from Grandpa's workshop?"),
    ('mio', 'どうぞごゆっくりお過ごしください。中庭はお二人だけの貸し切りです。', 'Please take all the time you need. The courtyard is all yours.'),
]

OPENER = "Listen to how warm brotherly speech contrasts with Mio's polished guesthouse courtesy. Let's walk through six lines."

WALK = [
    (0, None, ["'So somebody with something of Grandfather's really was you all along, Haruto.' Confirming a hunch uses ", (None, 'やっぱり'), ", 'just as I thought!', while Daiki calls his younger brother ", (None, 'お前'), ", a rough, affectionate 'you' used only with someone very close."]),
    (2, None, ["'That neat square handwriting on the postcard—I knew it was yours in two seconds.' Handwritten characters are called ", (None, '字'), ', and ', (None, 'わかった'), " means 'I recognised' or 'I knew right away'."]),
    (4, None, ["'Of course I came. Why did you hide behind a mystery note?' Saying something goes without saying uses ", (None, '当たり前'), ", meaning 'natural' or 'of course'."]),
    (5, None, ["'Because I was afraid you were still angry. All these three years, I missed you.' Feeling scared or nervous uses ", (None, '怖かった'), ", 'was afraid', paired with ", (None, 'まだ怒っている'), " for 'still angry'."]),
    (7, None, ["'Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on its way right now.' In formal inn service, humble 'is coming' becomes ", (None, '参ります'), '.']),
    (9, None, ["'Have a seat, brother. Take off your heavy coat and look at this blue suitcase.' Putting a coat on is one word, and taking it off is ", (None, '脱いで'), ", from 'to take off clothing or shoes'."]),
]

TRANSITION = "Now let's hear the brothers' first conversation in three years again."

OUTRO = "Daiki recognised Haruto's neat handwriting in two seconds and came anyway! Next time, they unwrap the white paper parcel under the courtyard tree."

CLOSING = ('mio', 'またね！')
