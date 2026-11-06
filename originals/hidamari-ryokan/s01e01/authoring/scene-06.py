ID = 'hidamari-ryokan-s01e01-scene-06'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = '鞄の名札  (The Luggage Tag)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kazuko': '和子', 'takashi': '隆'}

INTRO = 'Back downstairs at the front desk, Mio, Kazuko, and owner Takashi lean over the blue suitcase under the lamp. Takashi finally puts his reading glasses to good use. Listen to the scene first.'

STORY = [
    ('takashi', 'なんと大変な間違いでしょう！眼鏡をかけて名札を見ますね。', 'What a mix-up! Let me put on my glasses and read the tag.'),
    ('kazuko', '名前か電話番号は書いてありますか？', 'Is a name or a phone number written on it?'),
    ('takashi', '残念ながら電話番号はありません。イニシャルが二つと、古い通りの名前だけです。', 'Unfortunately there is no phone number. Only two initials and an old street name.'),
    ('mio', 'あ、待ってください！その通りはここから歩いて五分の近所ですよ！', 'Oh, wait! That street is right in this neighbourhood, a five-minute walk from here!'),
    ('kazuko', '不思議ですね！今朝、同じ電車で同じ町へ来たんですね。', 'How strange! We rode the same train this morning to the same neighbourhood.'),
    ('takashi', '美央さん、今すぐ駅の忘れ物センターに電話してください。', 'Mio, please call the station lost-and-found office right away.'),
    ('mio', '今かけます……もしもし？青いスーツケースの取り違えは届いていますか？', 'Dialling now... Hello? Has anyone reported a swapped blue suitcase?'),
    ('kazuko', '私の鞄には、上のポケットに赤いリボンが入っていると伝えてください！', 'Please tell them my bag has a red ribbon inside the top pocket!'),
    ('mio', 'まだですか？では宿の電話番号と住所をお願いします。ありがとうございます！', "Not yet? Then please take our inn's phone number and address. Thank you!"),
    ('takashi', 'まだ連絡はないそうです、和子さん。本当に申し訳ありません。', 'They have no word yet, Kazuko. I am truly sorry.'),
    ('kazuko', '宿のせいじゃありませんよ。でも、今着ているコートしかありませんわ！', "It is not the inn's fault. Still, I only have the coat I am wearing right now!"),
    ('mio', 'あ、ちょっと待ってください！カフェから由香さんが手を振っています！', 'Oh, wait one moment! Yuka is waving from the café with an idea!'),
]

OPENER = "Phone calls, addresses, and polite apologies fill the front desk. Let's listen closely to six key lines."

WALK = [
    (1, None, ["'Is a name or a phone number written on it?' Kazuko links ", (None, '名前'), ", 'name', with ", (None, '電話番号'), ", which literally joins 'telephone' and 'number'."]),
    (2, None, ["'Unfortunately there is no phone number. Only two initials and an old street name.' Opening bad news gently is easy with ", (None, '残念ながら'), ", meaning 'unfortunately' or 'sad to say'."]),
    (3, None, ["'Oh, wait! That street is right in this neighbourhood, a five-minute walk from here!' Mio combines ", (None, '歩いて五分'), ", literally 'walking five minutes', with ", (None, '近所'), " for 'neighbourhood'."]),
    (6, None, ["'Dialling now... Hello? Has anyone reported a swapped blue suitcase?' Answering or starting a phone call in Japanese almost always uses ", (None, 'もしもし'), ", the dedicated telephone 'hello'."]),
    (7, None, ["'Please tell them my bag has a red ribbon inside the top pocket!' Listen for ", (None, '赤いリボン'), ", 'red ribbon', and ", (None, '伝えてください'), " meaning 'please pass on the message'."]),
    (9, None, ["'They have no word yet, Kazuko. I am truly sorry.' In guest service, Takashi reaches for ", (None, '申し訳ありません'), ", a sincere formal apology literally saying 'I have no excuse'."]),
]

TRANSITION = "Now let's hear the whole front-desk investigation again."

OUTRO = "No report at the station yet, and the mystery traveller knows a street five minutes away. Next time, Yuka steps in to rescue Kazuko's first evening."

CLOSING = ('takashi', 'また会いましょう！')
