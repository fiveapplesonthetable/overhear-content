# Authoring module for linden-courtyard-ja-s01e02-scene-08.
ID = 'linden-courtyard-ja-s01e02-scene-08'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = 'Two Names, One Room  (一つの部屋に二つの名前)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '雨の降る火曜日の夕方、フロントの予約台帳を見つめていたアーサーが真っ青になりました。眼鏡をかけずにタブレットで電話予約を受けたせいで、満室の夜に七号室へ二人のお客さまを重複して予約してしまったのです。まずは第二話のクライマックスを聴いてみましょう。'
OPENER = 'それでは大ピンチの場面を、一行ずつ確かめていきましょう。'
TRANSITION = 'ではもう一度、緊迫のやり取りを最初から通して聴いてみましょう。'
OUTRO = '外は雨、近隣のホテルもすべて満室という絶体絶命の中、ハンナとグレアムは階段の上の三階にある古い屋根裏の書斎へと駆け上がります。続きは次のエピソードをお楽しみに。それではまた明日！'
CLOSING = ('arthur', 'See you tomorrow!')
STORY = [
    ('arthur', 'Graham... Hannah... please tell me room six is free tonight.', 'グレアム…ハンナ…どうか今夜六号室が空いていると言ってくれ。'),
    ('hannah', 'No, Arthur, the couple from the south checked into room six an hour ago.', 'いいえ、アーサー、一時間前に南部から来たご夫婦が六号室にチェックインされました。'),
    ('graham', 'Every key from one to seven is taken, and room eight has wet paint.', '一番から七番までの鍵はすべてふさがっているし、八号室はペンキが塗りたてだ。'),
    ('arthur', 'Oh, disaster! Yesterday I took a phone booking on the tablet without my glasses!', 'ああ、なんてことだ！昨日、眼鏡をかけずにタブレットで電話予約を受けてしまったんだ！'),
    ('hannah', 'Wait, let me look at the tablet screen and the paper book together.', '待って、タブレットの画面と紙の台帳を一緒に見比べさせてください。'),
    ('graham', 'Let me guess. You promised somebody a room we do not have?', '当ててみようか。うちにない部屋を誰かに約束してしまったんだね？'),
    ('hannah', 'Arthur! Room seven is already occupied, and you booked a second guest into room seven!', 'アーサー！七号室はすでにふさがっているのに、七号室に二人目のお客さまを予約していますよ！'),
    ('arthur', "And he arrives on the eight o'clock evening train, in forty minutes!", 'しかもその方は、あと四十分で、八時の夜行列車で到着されるんだ！'),
    ('graham', 'Told you that tablet is a trap.', 'あのタブレットは落とし穴だって言っただろう。'),
    ('arthur', 'It is raining outside and every hotel on our street is full! What do we do?', '外は雨が降っているし、この通りのホテルはどこも満室だ！いったいどうしよう？'),
    ('hannah', 'Wait, what is on the third floor above the stairs?', '待って、階段の上の三階には何があるんですか？'),
    ('graham', 'The old sunny attic study... follow me, quickly!', '日当たりの良い古い屋根裏の書斎だ…急いで私について来て！'),
]
WALK = [
    (0, None, ["'グレアム…ハンナ…どうか今夜六号室が空いていると言ってくれ。' 部屋に予約がなく空室であることを", (None, 'room six is free tonight'), 'と祈るように尋ねています。']),
    (1, None, ["'いいえ、アーサー、一時間前に南部から来たご夫婦が六号室にチェックインされました。' 宿に入って手続きを終えたことを", (None, 'checked into room six'), 'と言い、黙字を含む時間の表現で', (None, 'an hour ago'), 'と後ろに続けます。']),
    (2, None, ["'一番から七番までの鍵はすべてふさがっているし、八号室はペンキが塗りたてだ。' 部屋や席がすでに使用中であることを", (None, 'Every key from one to seven is taken'), 'と言い、乾いていない塗装を', (None, 'wet paint'), 'と簡潔に表します。']),
    (3, None, ["'ああ、なんてことだ！昨日、眼鏡をかけずにタブレットで電話予約を受けてしまったんだ！' 完了した過去の時点を表す", (None, 'Yesterday I took a phone booking'), 'に、眼鏡なしでという', (None, 'without my glasses'), 'が後ろに続きます。']),
    (4, None, ["'待って、タブレットの画面と紙の台帳を一緒に見比べさせてください。' 二つのものを並べて確認するために文末へ", (None, 'the tablet screen and the paper book together'), 'とまとめています。']),
    (5, None, ["'当ててみようか。うちにない部屋を誰かに約束してしまったんだね？' 状況を見抜いたときの前置き", (None, 'Let me guess'), 'に続けて、後ろから関係節を省略して説明する', (None, 'a room we do not have'), 'を使っています。']),
    (6, None, ["'アーサー！七号室はすでにふさがっているのに、七号室に二人目のお客さまを予約していますよ！' 先客が入室済みであることを", (None, 'already occupied'), 'と言い、もう一人の予約を', (None, 'booked a second guest'), 'と伝えています。']),
    (7, None, ["'しかもその方は、あと四十分で、八時の夜行列車で到着されるんだ！' 時刻表通りの到着予定には現在形の", (None, "he arrives on the eight o'clock evening train"), 'を使い、今から何分後かを', (None, 'in forty minutes'), 'という形で表します。']),
    (8, None, ["'あのタブレットは落とし穴だって言っただろう。' ほら言わんこっちゃないと親しい相手に軽く言うときは主語を省いた口語の", (None, 'Told you that tablet is a trap'), 'がよく使われます。']),
    (9, None, ["'外は雨が降っているし、この通りのホテルはどこも満室だ！いったいどうしよう？' 今まさに降っている雨を", (None, 'It is raining outside'), 'と表し、対応を相談する定番の疑問文', (None, 'What do we do'), 'をすぐ後ろに続けます。']),
    (10, None, ["'待って、階段の上の三階には何があるんですか？' 建物の階数を表す表現と上方の前置詞を組み合わせて", (None, 'on the third floor above the stairs'), 'とひらめきの質問を投げかけています。']),
    (11, None, ["'日当たりの良い古い屋根裏の書斎だ…急いで私について来て！' 解決の糸口を見つけて案内する頼もしい一言", (None, 'follow me, quickly'), 'で次の物語へとつながります。']),
]
