ID = 'hidamari-ryokan-s01e03-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'あと三十五分  (Thirty-Five Minutes)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'mio': '美央', 'kenji': '健二'}

INTRO = 'Rain taps against the lobby windows of the Hidamari Inn in Osaka. With a second Room 7 guest arriving in thirty-five minutes, Takashi, Mio, and Kenji hurry toward the stairs. Listen first.'

STORY = [
    ('takashi', 'あと三十五分です！ひどい一つ星の口コミを書かれてしまいます！', 'Thirty-five minutes left! He will write a terrible one-star review!'),
    ('mio', '深呼吸してください、隆さん。まだ誰も何も書いていませんよ。', 'Take a deep breath, Takashi. Nobody has written anything yet.'),
    ('kenji', 'ほら、これが三階の屋根裏部屋を開ける小さな銀の鍵だ。', 'Here is the small silver key that opens the third-floor attic room.'),
    ('takashi', '屋根裏部屋に、ちゃんとしたベッドはあるんですか？', 'Does the attic room even have a proper bed?'),
    ('kenji', 'ああ、丈夫な木のベッドと、きれいな机と、この宿で一番の眺めがある。', 'Yeah, a sturdy wooden bed, a clean desk, and the best view in the inn.'),
    ('mio', 'じゃあ、どうして普段はお客さんに貸さないんですか？', 'Then why do we never rent it out to guests normally?'),
    ('kenji', '階段が狭いし、隆さんが古いランプの箱を置いているからさ。', 'Because the stairs are narrow and Takashi keeps old lamp boxes up there.'),
    ('takashi', '小さい箱が三つだけですよ！たぶん四つかな！', 'Only three small boxes! Maybe four!'),
    ('mio', '四つの箱なら五分で運べます。今すぐ見に行きましょう！', "We can move four boxes in five minutes. Let's go look right now!"),
    ('kenji', '階段を上がって、踊り場を左に曲がった一番奥のドアだ。', 'Go up the stairs, turn left at the landing, and it is the farthest door.'),
    ('takashi', '私はリネン棚から真っ白で清潔なシーツを持って行きます！', 'I will bring crisp white sheets from the linen cupboard!'),
    ('mio', '行きましょう、三階まで競争ですよ！', 'Come on, race you up to the third floor!'),
]

OPENER = "Furniture, directions up the stairs, and calming an anxious boss lead off Episode 3. Let's walk through six lines."

WALK = [
    (0, None, ["'Thirty-five minutes left! He will write a terrible one-star review!' Online ratings in Japanese are called ", (None, '口コミ'), ", literally 'mouth-to-mouth' word of mouth, paired here with ", (None, '一つ星'), " for 'one star'."]),
    (2, None, ["'Here is the small silver key that opens the third-floor attic room.' Kenji holds up ", (None, '銀の鍵'), ", 'the silver key', for ", (None, '屋根裏部屋'), ", literally the 'room under the roof'."]),
    (4, None, ["'Yeah, a sturdy wooden bed, a clean desk, and the best view in the inn.' Calling something number one uses ", (None, '一番'), ', so ', (None, '一番の眺め'), " means 'the very best view'."]),
    (6, None, ["'Because the stairs are narrow and Takashi keeps old lamp boxes up there.' Listen for ", (None, '狭い'), ", meaning 'narrow' or 'cramped', describing ", (None, '階段'), ', the stairs.']),
    (8, None, ["'We can move four boxes in five minutes. Let's go look right now!' Linking 'look' to 'go' forms ", (None, '見に行きましょう'), ", a super-handy pattern for 'let's go and see'."]),
    (9, None, ["'Go up the stairs, turn left at the landing, and it is the farthest door.' Direction words appear everywhere: ", (None, '左に曲がった'), ' comes from turning ', (None, '左'), ", 'left'."]),
]

TRANSITION = "Now let's hear the whole rush toward the staircase again."

OUTRO = "Thirty-five minutes left and four cardboard boxes to clear—let's head up to the attic room next time."

CLOSING = ('mio', 'またね！')
