ID = 'hidamari-ryokan-s01e01-scene-04'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = '二階の四号室  (Room Four on the Second Floor)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kazuko': '和子', 'kenji': '健二'}

INTRO = "At the front desk, retired piano teacher Kazuko steps in from her taxi pulling a large dark-blue suitcase. Mio greets her very first guest while Kenji steps forward to carry the bag. Let's hear how it goes."

STORY = [
    ('mio', 'いらっしゃいませ！おはようございます。', 'Welcome! Good morning, madam.'),
    ('kazuko', 'おはよう、お嬢さん。リサの名前で予約しています。', 'Good morning, my dear. I have a booking for 和子.'),
    ('mio', 'はい、二階の四号室ですね！電車の旅はいかがでしたか？', 'Yes, room four on the second floor! How was your train trip?'),
    ('kazuko', '静かで快適でしたよ。でも今日、このスーツケースがとても重いんです。', 'It was quiet and pleasant, though this suitcase feels very heavy today.'),
    ('kenji', 'お持ちしますよ。おや、中に石でも入っていますか？', 'Allow me to carry it. Goodness, are there stones inside here?'),
    ('kazuko', 'ワンピースと楽譜と、お気に入りのティーカップだけですわ！', 'Only dresses, sheet music, and my favourite teacup!'),
    ('mio', 'こちらが四番の鍵です。朝ごはんは七時半から十時までです。', 'Here is key number four. Breakfast is from seven thirty to ten.'),
    ('kazuko', '素敵ですね。窓は通り側ですか、それとも中庭側ですか？', 'Wonderful. Does the window face the street side or the courtyard side?'),
    ('mio', '中庭側です。大きな木のすぐ上で、とても静かですよ。', 'The courtyard side. Right above the big tree, and it is very quiet.'),
    ('kazuko', 'ちょうど理想的です。階段はどこですか？', 'Just what I hoped for. Where are the stairs?'),
    ('kenji', 'この奥です。青い鞄は私が上まで運びますよ。', 'Right through here. I will carry the blue bag upstairs for you.'),
    ('kazuko', 'お二人とも、どうもありがとうございます。', 'Thank you both very much.'),
]

OPENER = "Mio shines at her first real check-in with warm, courteous Japanese. Let's replay the key moments."

WALK = [
    (0, None, ["'Welcome! Good morning, madam.' Walk through the doorway of any inn, café, or shop in Osaka and the staff will greet you with ", (None, 'いらっしゃいませ'), ', the classic hospitality welcome.']),
    (2, None, ["'Yes, room four on the second floor! How was your train trip?' Here ", (None, '電車'), " means 'train' — literally 'electric car' — and ", (None, 'いかがでしたか'), " is the polite way to ask 'how was it?'."]),
    (3, None, ["'It was quiet and pleasant, though this suitcase feels very heavy today.' Kazuko describes the ride with ", (None, '静か'), ", meaning 'quiet', and notes that ", (None, 'スーツケース'), ' feels ', (None, '重い'), ", meaning 'heavy'."]),
    (6, None, ["'Here is key number four. Breakfast is from seven thirty to ten.' Notice the super-useful time pair ", (None, 'から'), " for 'from' and ", (None, 'まで'), " for 'until', framing ", (None, '七時半'), ", 'seven thirty'."]),
    (7, None, ["'Wonderful. Does the window face the street side or the courtyard side?' When offering a choice between two options, ", (None, 'それとも'), " bridges the two questions just like English 'or'."]),
    (10, None, ["'Right through here. I will carry the blue bag upstairs for you.' Kenji points to ", (None, '青い鞄'), ", 'the blue bag', and promises ", (None, '運びます'), ", meaning 'I will carry it'."]),
]

TRANSITION = "Now let's listen to Kazuko's check-in again all the way through."

OUTRO = 'Mio handled her first guest smoothly, though Kenji noticed that dark-blue suitcase weighed a ton. See you next time to discover what is inside.'

CLOSING = ('kazuko', 'さようなら！')
