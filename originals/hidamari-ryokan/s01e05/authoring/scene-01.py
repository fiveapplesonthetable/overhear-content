ID = 'hidamari-ryokan-s01e05-scene-01'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = '中庭での告白  (Truth in the Courtyard)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'haruto': '陽翔', 'mio': '美央', 'kazuko': '和子'}

INTRO = "Under the shade tree at the Hidamari Inn in Osaka, Haruto sits down with Mio and Kazuko to explain Monday night's suitcase mystery from the start. Listen first."

STORY = [
    ('kazuko', 'よく顔を見せてちょうだい、陽翔くん！ピアノよりずっと背が高くなったわね！', 'Let me get a proper look at you, Haruto! You grew much taller than the piano!'),
    ('haruto', '和子先生が、まさか同じ旅館に泊まっていたなんて信じられません。', 'I cannot believe you were staying in the exact same inn, Miss Kazuko.'),
    ('mio', '待ってください。月曜日に同じ電車に乗って、和子さんの鞄を持って行ったんですね？', "Wait: so you rode the same train on Monday and took Kazuko's bag?"),
    ('haruto', '完全な間違いだったんです！いとこの部屋で開けたら、楽譜と赤いリボンが見えて。', "It was a total accident! When I opened it at my cousin's flat, I saw sheet music and a red ribbon."),
    ('kazuko', 'どうして夜に私の鞄を石段に置いて、逃げてしまったの？', 'Why did you set my bag on the stone step at night and run away?'),
    ('haruto', '月曜の夜にここへ歩いて来た時、この通りを歩く兄の姿が見えたからです！', 'Because when I walked here Monday night, I spotted my older brother walking down this street!'),
    ('mio', 'お兄さんは、ここ大阪に住んでいるんですか？', 'Does your older brother live here in Osaka?'),
    ('haruto', 'はい。慌ててベルを鳴らし、金曜日のメモを持ち手に貼りました。', 'Yes. I panicked, rang the bell, and taped the Friday note onto the handle.'),
    ('kazuko', 'それなのに水曜の夜、本名でここにチェックインしたの？', 'And yet Wednesday night you checked in here under your real name?'),
    ('haruto', '金曜まで近くに静かな宿が必要で、私の鞄がここにあるのをすっかり忘れていたんです！', 'I needed a quiet inn nearby until Friday, and completely forgot you still had my bag!'),
    ('mio', '火曜日に電話をかけて、「白い包みを開けないで」と頼んだのにですか！？', 'Even though you called us on Tuesday asking us not to open the white parcel?!'),
    ('haruto', 'あの白い紙の中の物は、私ではなく兄の大輝の物なんです。', 'What is inside that white paper belongs to my older brother Daiki, not to me.'),
]

OPENER = "Family words, growing tall, and Monday's comedy of errors click into place. Let's walk through six lines."

WALK = [
    (0, None, ["'Let me get a proper look at you, Haruto! You grew much taller than the piano!' Describing height in Japanese literally says 'the back is high': ", (None, '背が高く'), " means 'tall'."]),
    (1, None, ["'I cannot believe you were staying in the exact same inn, Miss Kazuko.' Expressing amazement uses ", (None, '信じられません'), ", meaning 'I cannot believe it', right after ", (None, '同じ旅館'), ", 'the same inn'."]),
    (3, None, ["'It was a total accident! When I opened it at my cousin's flat, I saw sheet music and a red ribbon.' Family vocabulary adds ", (None, 'いとこ'), " for 'cousin' and ", (None, '楽譜'), " for 'musical score' or 'sheet music'."]),
    (6, None, ["'Does your older brother live here in Osaka?' Notice the difference: Haruto calls his own brother plain ", (None, '兄'), ' in the previous line, whereas Mio respectfully says ', (None, 'お兄さん'), " for someone else's older brother."]),
    (9, None, ["'I needed a quiet inn nearby until Friday, and completely forgot you still had my bag!' Pair ", (None, 'すっかり'), ", meaning 'completely', with ", (None, '忘れていた'), " for 'had forgotten'."]),
    (11, None, ["'What is inside that white paper belongs to my older brother Daiki, not to me.' Contrasting 'not A, rather B' is clean with ", (None, '私ではなく'), ", meaning 'not me'."]),
]

TRANSITION = "Now let's listen to Haruto's full confession again."

OUTRO = 'Every puzzle piece from Monday and Tuesday finally fits! Next time, Haruto explains why he and his brother Daiki have not spoken in three years.'

CLOSING = ('mio', 'またね！')
