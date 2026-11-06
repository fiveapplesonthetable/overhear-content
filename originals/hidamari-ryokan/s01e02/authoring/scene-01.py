ID = 'hidamari-ryokan-s01e02-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = '赤いリボン  (The Red Ribbon)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kazuko': '和子', 'kenji': '健二'}

INTRO = 'Tuesday morning dawns bright and clear at the Hidamari Inn. Kazuko hurries downstairs to the front desk, where Mio and Kenji are waiting with her returned suitcase. Listen to the whole scene first.'

STORY = [
    ('mio', 'おはようございます、和子さん！昨夜、門の前に届いた物を見てください。', 'Good morning, Kazuko! Look at what arrived outside our gate last night.'),
    ('kazuko', '私のスーツケース！上のポケットを開けますね……ああ、赤いリボンです！', 'My suitcase! Let me open the top pocket... yes, my red ribbon!'),
    ('kenji', '中のティーカップはどうですか？割れていませんか？', 'How is your teacup inside? Is it still unbroken?'),
    ('kazuko', 'ひび一つありません！どなたが届けてくださったんでしょう？', 'Not a single crack! Who could have brought it back?'),
    ('mio', 'わからないんです。誰かが石段に置いて、ベルを鳴らしました。', 'We do not know. Someone set it on the stone step and rang the bell.'),
    ('kazuko', '木の汽車が入ったご自分の鞄は、受け取らなかったんですか？', 'And he did not ask for his own suitcase with the wooden train?'),
    ('kenji', '金曜日まで預かってほしいと、短いメモがありました。', 'There was a short note asking us to keep it until Friday.'),
    ('kazuko', '不思議ですね！あの名札の字、なんだか見覚えがあったんです。', 'How curious! The handwriting on that tag felt strangely familiar to me.'),
    ('mio', '本当ですか？大阪にお知り合いがいるんですか？', 'Really? Do you know someone here in Osaka?'),
    ('kazuko', '二十五年前、この近くでピアノを教えていたの。もう遠い昔だけど。', 'Twenty-five years ago I taught piano near here, though that was long ago.'),
    ('kenji', 'とにかく、あの鞄は鍵をかけて大切に保管しておきます。', 'For now, we will keep that bag safely under lock and key.'),
    ('kazuko', '嬉しいです！さあ、朝ごはんをしっかりいただきますわ。', 'How wonderful! Now I am ready to enjoy a hearty breakfast.'),
]

OPENER = "Reuniting Kazuko with her teacup brings polite question words and memory phrases. Let's walk through six lines."

WALK = [
    (0, None, ["'Good morning, Kazuko! Look at what arrived outside our gate last night.' Listen for ", (None, '昨夜'), ", a compact two-character word meaning 'last night', right before ", (None, '門の前'), " for 'in front of the gate'."]),
    (3, None, ["'Not a single crack! Who could have brought it back?' Instead of the plain word for 'who', Kazuko chooses ", (None, 'どなた'), ", the graceful, polite version meaning 'which person'."]),
    (6, None, ["'There was a short note asking us to keep it until Friday.' Here ", (None, '短いメモ'), " pairs 'short' with borrowed English 'memo' for a quick written note."]),
    (7, None, ["'How curious! The handwriting on that tag felt strangely familiar to me.' Combining 'see' and 'remember' builds ", (None, '見覚え'), ', a lovely Japanese word for a visual memory or something that looks familiar.']),
    (9, None, ["'Twenty-five years ago I taught piano near here, though that was long ago.' Notice ", (None, '二十五年前'), " for 'twenty-five years ago', and ", (None, '教えていた'), " from the word meaning 'to teach'."]),
    (11, None, ["'How wonderful! Now I am ready to enjoy a hearty breakfast.' Before eating or accepting food in Japanese, ", (None, 'いただきます'), ' expresses humble gratitude for the meal.']),
]

TRANSITION = "Now let's hear the whole Tuesday morning reunion again."

OUTRO = 'Kazuko has her red ribbon and teacup back, and an old Osaka piano memory has begun to stir. Next time, an urgent problem hits the breakfast kitchen. See you next time.'

CLOSING = ('kazuko', 'また会いましょう！')
