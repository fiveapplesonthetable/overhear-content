ID = 'hidamari-ryokan-s01e06-scene-03'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = '紙の上の三十日  (Thirty Days on Paper)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'kenji': '健二'}

INTRO = 'Behind the front desk, Takashi sits slumped beside the wooden key board while Kenji and Mio lean across the counter speaking quietly. Listen first.'

STORY = [
    ('takashi', '十五年間、真鍮の鍵を磨いてネクタイを整えて来たのに……三十日で終わりです！', 'Fifteen years of polishing brass keys and straightening ties... all over in thirty days!'),
    ('kenji', '書類を最後まで読む前に、勝手に宿を終わらせるなよ、隆さん。', 'Stop burying the inn before we even read the document to the end, Takashi.'),
    ('mio', 'そうですよ！さっき、表紙の裏に二枚目の紙が留めてあるのに気づきました。', "That's right! Earlier I noticed a second page clipped behind the cover sheet."),
    ('takashi', '法律の細かい文章は、眼鏡を二つかけても頭が痛くなります！', 'Fine-print legal sentences give me a headache even with two pairs of glasses!'),
    ('kenji', 'この建物は八十回の冬と、昨日の壊れたボイラーバルブを乗り越えたんだぞ。', "This building survived eighty winters and yesterday's broken boiler valve."),
    ('mio', 'あっ、待ってください！今、十メートル先の中庭に誰が座っていますか？', 'Oh, wait a second! Who is sitting ten metres away in our courtyard right now?'),
    ('takashi', 'レモンケーキを食べているご兄弟ですか？', 'Two brothers eating lemon cake?'),
    ('mio', '大阪じゅうの歴史ある中庭建築を専門にしている建築家ですよ！', 'An architect who specialises in historic courtyard buildings all across Osaka!'),
    ('kenji', 'いいところに気づいたな、美央。陽翔さんなら毎週、市の建築規則を読んでいるはずだ。', 'Sharp catch, Mio. Haruto must read municipal building rules every single week.'),
    ('takashi', 'いやあ、大切なお客さまにうちの大家さんの悩みを相談するなんてできません！', 'Oh, I could never trouble a valued guest with our landlord worries!'),
    ('mio', '一週間も青いスーツケースを守ったんですよ？きっと力になってくれます！', 'After we guarded his blue suitcase all week? He will gladly lend a hand!'),
    ('kenji', '待て……ちょうど今、由香があのテーブルから戻って来たぞ。', 'Hold on... Yuka is walking back from their table right now.'),
]

OPENER = "Headaches over legal fine print give way to a bright idea from Mio. Let's walk through six lines."

WALK = [
    (1, None, ["'Stop burying the inn before we even read the document to the end, Takashi.' Reading or listening right to the finish uses ", (None, '最後まで'), ", meaning 'all the way to the end'."]),
    (3, None, ["'Fine-print legal sentences give me a headache even with two pairs of glasses!' Telling a doctor or friend you have a headache uses the natural clause ", (None, '頭が痛くなります'), ", built from 'head' and 'painful'."]),
    (4, None, ["'This building survived eighty winters and yesterday's broken boiler valve.' Look at ", (None, '建物'), ", literally 'built thing' for 'building'."]),
    (7, None, ["'An architect who specialises in historic courtyard buildings all across Osaka!' Adding 'have' after 'history' gives ", (None, '歴史ある'), ', describing buildings rich in history.']),
    (9, None, ["'Oh, I could never trouble a valued guest with our landlord worries!' Asking someone for advice or talking a problem over is ", (None, '相談する'), '.']),
    (10, None, ["'After we guarded his blue suitcase all week? He will gladly lend a hand!' Literally 'become someone's strength', ", (None, '力になってくれます'), ' is a warm Japanese idiom for helping someone out.']),
]

TRANSITION = "Now let's replay the front-desk brainstorm again."

OUTRO = "Mio remembered they have an expert on historic Osaka courtyards sitting ten metres away! Next time, Yuka serves the lemon cake and Daiki's sharp eyes spot the worried faces inside."

CLOSING = ('kenji', 'またね！')
