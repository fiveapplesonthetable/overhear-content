ID = 'hidamari-ryokan-s01e01-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = '取っ手を上げて  (Lift the Handle)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kenji': '健二'}

INTRO = 'Mio arrives early for her very first morning at the Hidamari Inn in Osaka. Behind the front desk, veteran handyman Kenji is already pouring hot green tea. Listen to the scene first without worrying about catching every word.'

STORY = [
    ('mio', 'おはようございます！すみません、ドアに鍵がかかっていますか？', 'Good morning! Excuse me, is the door locked?'),
    ('kenji', 'おはよう。いや、まず取っ手を上げて、それから押すんだ。', 'Morning. No, lift the handle first, then push.'),
    ('mio', 'あ、開きました！ありがとうございます。新しい受付の美央です。', 'Oh, it opened! Thank you. I am Mio, the new receptionist.'),
    ('kenji', '俺は健二だ。十分も早いね。', 'I am Kenji. You are a whole ten minutes early.'),
    ('mio', '初日はいつも早く歩きます。パソコンはどこですか？', 'I always walk fast on my first day. Where is the computer?'),
    ('kenji', '引き出しの中だよ。ここではこの大きな紙の帳面と鉛筆を使う。', 'Inside the drawer. Here we use this big paper ledger and a pencil.'),
    ('mio', '紙の帳面ですか？本当に？', 'A paper ledger? Really?'),
    ('kenji', '紙なら、雨の日でも部屋の予定が消えないからね。', 'With paper, the room list never disappears even on a rainy day.'),
    ('mio', 'なるほど！それで、これが鍵ですか？', 'Fair enough! And are these the keys?'),
    ('kenji', 'ああ、部屋は八室、真鍮の鍵も八つだ。今日は四号室にお客さんが来る。', 'Yeah, eight rooms and eight brass keys. A guest is arriving for room four today.'),
    ('mio', 'わかりました。大事なことを全部教えてください。', 'Got it. Please tell me everything I need to know.'),
    ('kenji', 'ルールその一。まず温かいお茶を飲んで、それからベルに出ること。', 'Rule number one: drink hot tea first, then answer the bell.'),
]

OPENER = "Mio uses crisp polite speech on her first morning, while Kenji answers in relaxed veteran style. Let's hear the key lines again."

WALK = [
    (0, None, ["'Good morning! Excuse me, is the door locked?' Starting her shift brightly, Mio uses ", (None, 'おはようございます'), ', the full polite morning greeting, and then asks about ', (None, '鍵'), ', the everyday Japanese word for a key or lock.']),
    (1, None, ["'Morning. No, lift the handle first, then push.' Kenji drops the polite ending for casual ", (None, 'おはよう'), ' and sequences the trick with ', (None, 'まず'), ", which means 'first of all', followed by ", (None, 'それから'), " for 'after that'."]),
    (2, None, ["'Oh, it opened! Thank you. I am Mio, the new receptionist.' Here ", (None, '新しい'), " means 'new', and ", (None, '受付'), " literally joins 'receive' and 'attach' to name the reception desk."]),
    (4, None, ["'I always walk fast on my first day. Where is the computer?' Japanese shortens 'personal computer' into ", (None, 'パソコン'), ', and ', (None, 'どこですか'), ' is the handy question chunk for asking where anything is.']),
    (5, None, ["'Inside the drawer. Here we use this big paper ledger and a pencil.' Listen for ", (None, '紙'), ", meaning 'paper', paired with ", (None, '鉛筆'), ", the word for 'pencil'."]),
    (11, None, ["'Rule number one: drink hot tea first, then answer the bell.' Kenji pairs ", (None, '温かい'), ", meaning 'warm', with ", (None, 'お茶'), ", where the polite prefix softens the word for 'tea'."]),
]

TRANSITION = "Now let's listen to the whole conversation again from start to finish."

OUTRO = "Mio is inside, the eight brass keys are on the board, and her first morning has begun. Don't worry if a few words went past quickly; they come back all week. See you next time."

CLOSING = ('mio', 'またね！')
