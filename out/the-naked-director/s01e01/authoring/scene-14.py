ID = 'the-naked-director-s01e01-scene-14'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = 'イングリッシュマスター  (An English Master)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'nakai': '中井', 'okusama': '中井の妻'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "One wrong word nearly got Muranishi thrown out of Nakai's mansion, so he thinks fast. "
    "He promises Nakai that practicing a handful of cheerful English words will make him an instant hit abroad—and soon both men are shouting at the top of their lungs. "
    "Listen to Muranishi close his very first sale."
)

STORY = [
    ('muranishi', 'めっそうもございません！お薦めする理由がもう一つあります。', 'Perish the thought! There is one more reason I recommend this.', [(288, 'めっそうもございません'), (290, 'お薦めする理由が もう')], 'Wrote 一つ in kanji.'),
    ('nakai', '何だ？', 'What is it?', [(291, '何だ')], ''),
    ('muranishi', '愛のコミュニケーションを取ることができます。', 'You can enjoy warm communication of love.', [(294, '愛のコミュニケーションを 取ることができます')], ''),
    ('muranishi', 'ここに書かれている言葉を覚えて使えば大丈夫です。', 'If you learn and use the words written here, you are all set.', [(299, 'ここに書かれている言葉を 覚えて使えば')], 'Completed clause cleanly with 大丈夫です.'),
    ('nakai', '例えば？', 'For example?', [(301, '例えば')], ''),
    ('muranishi', 'シンプルに、オー、グッド、グッド！', 'Simply say: oh, good, good!', [(310, 'シンプルに'), (312, 'オー グッド グッド')], ''),
    ('nakai', 'それだったら俺も言えるぜ。グッド！', 'If that is all, I can say it too. Good!', [(313, 'それだったら'), (313, '言えるぜ'), (317, 'グッド')], ''),
    ('muranishi', 'パーフェクトでございます！', 'That is absolute perfection!', [(327, 'パーフェクトでございます')], ''),
    ('nakai', 'ハロー！ラブ！グッド！', 'Hello! Love! Good!', [(335, 'ハロー ラブ'), (334, 'グッド')], ''),
    ('okusama', 'あんたたち！', 'Hey, you two!', [(339, 'あんたたち')], ''),
    ('muranishi', '奥様、明日からご主人はイングリッシュマスターになります。', 'Madam, starting tomorrow your husband becomes an English master.', [(340, '奥様'), (342, '明日から ご主人は イングリッシュマスターになります')], ''),
    ('nakai', '買ってもいい？', 'Can I buy it?', [(343, '買ってもいい')], ''),
]

OPENER = "From panicked humility to triumphant applause, Muranishi rides every emotional wave in Japanese. Let's look at the key expressions."

WALK = [
    (0, 'めっそうもございません！', [
        '"\'Perish the thought!\' Built around humble " Listen for ',
        ("muranishi", "めっそう"), ", this old-fashioned set expression waves away an accusation—'heaven forbid, I would never dream of looking down on you!'"
    ]),
    (0, 'お薦めする理由がもう一つあります。', [
        "'There is one more reason I recommend this.'  We can hear ",
        ("muranishi", "お薦め"), " this word means recommendation—the word printed on every restaurant menu's chef specials! ",
        ("muranishi", "もう一つ"), " adds 'one more'."
    ]),
    (3, None, [
        "'If you learn and use the words written here, you are all set.'  Listen for ",
        ("muranishi", "ここに書かれている"), " describes words 'written here'. Linking ",
        ("muranishi", "覚えて"), ", memorize, to ",
        ("muranishi", "使えば"), ", if you use, leads smoothly into reassuring ",
        ("muranishi", "大丈夫です")
    ]),
    (4, None, [
        '"\'For example?\' One word, " We can hear ',
        ("nakai", "例えば？"), ", works both to introduce your own example and, with a rising voice, to ask someone 'such as?'"
    ]),
    (6, 'それだったら俺も言えるぜ。', [
        "'If that is all, I can say it too.'  It features ",
        ("nakai", "それだったら"), " this word means 'if it is just that'. Turning the verb for 'to say' into ",
        ("nakai", "言える"), " builds 'can say', and masculine ",
        ("nakai", "ぜ"), " adds swagger."
    ]),
    (7, None, [
        '"\'That is absolute perfection!\' Muranishi dresses up English \'perfect\'—" Starting off with ',
        ("muranishi", "パーフェクト"), "—with grand ",
        ("muranishi", "でございます"), ", cheering his customer like a prize pupil."
    ]),
    (9, None, [
        '"\'Hey, you two!\' Hearing the commotion, Nakai\'s wife bursts in shouting " We can hear ',
        ("okusama", "あんたたち！"), ", and this word is built from casual ",
        ("okusama", "あんた"), ", you, plus group-marker ",
        ("okusama", "たち")
    ]),
    (10, None, [
        '"\'Madam, starting tomorrow your husband becomes an English master.\' Notice the respectful pair for someone else\'s marriage: " Focus on ',
        ("muranishi", "奥様"), " addresses a wife politely, while ",
        ("muranishi", "ご主人"), " refers to her husband."
    ]),
    (11, None, [
        '"\'Can I buy it?\' After acting like a tough boss all afternoon, Nakai meekly asks his wife " You can catch ',
        ("nakai", "買ってもいい"), ", literally 'is buying okay?'—the everyday pattern with ",
        ("nakai", "もいい"), " for asking permission!"
    ]),
]

TRANSITION = "Now let's listen to Muranishi's first victorious sale from start to finish."

OUTRO = (
    "Take away these expressions: the word for recommendations, the one for 'for example', "
    "and the phrase whenever you want to ask if it is okay to buy something. "
    "See you in scene fifteen."
)

CLOSING = ('muranishi', 'ありがとうございます、また会いましょう。')
