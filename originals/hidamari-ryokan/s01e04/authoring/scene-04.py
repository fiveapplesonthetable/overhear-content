ID = 'hidamari-ryokan-s01e04-scene-04'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = '地下のボイラー室  (Down in the Cellar)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'mio': '美央'}

INTRO = 'Down in the brick cellar beneath the courtyard, Mio hands Kenji the new brass valve while shining a bright flashlight onto the silent boiler. Listen first.'

STORY = [
    ('mio', '真鍮のバルブ、両方とも見つけたわよ、健二さん！息を整える？とんでもない！', 'Here are both brass valves, 健二! Catch my breath? Never!'),
    ('kenji', 'よし、この懐中電灯でパイプの継ぎ目をまっすぐ照らしてくれ。', 'Good, shine this flashlight steady right on the pipe joint.'),
    ('mio', 'わかりました！元栓の水はもう止めてありますか？', 'Got it! Have you already turned off the main water valve?'),
    ('kenji', '止めて水も抜いた。左にある重いレンチを取ってくれ。', 'Turned off and drained. Pass me the heavy wrench on your left.'),
    ('mio', 'この大きな鉄のレンチですね？はい、どうぞ。', 'This big iron wrench? Here you go.'),
    ('kenji', '一回、二回……見ろ、新しい真鍮のネジ山が気持ちよくはまったぞ。', 'One turn, two turns... look how cleanly the new brass threads fit.'),
    ('mio', '水漏れは一滴もありません！もうボイラーに火をつけられますか？', 'Not a single drip leaking! Can we light the boiler now?'),
    ('kenji', '青いハンドルを左へゆっくり回せ。速すぎるなよ。', 'Turn the blue wheel slowly to the left. Not too fast.'),
    ('mio', 'ゆっくり回します……聞いてください！水が勢いよく入って来ました！', 'Turning slowly... listen! Water is rushing right in!'),
    ('kenji', 'よし、バーナーの火もついた。きれいな青い炎だ、これでいい。', 'Good, the burner lit too. A steady blue flame, right as it should be.'),
    ('mio', '銅のパイプを触ってください！もう温かくなって来ましたよ！', 'Touch the copper pipe! It is already warming up!'),
    ('kenji', '三分で三階まで届く。よく走ったな、相棒。', 'Three minutes to reach the third floor. Good run today, partner.'),
]

OPENER = "Short teamwork instructions in the cellar bring clear action words and a big compliment from Kenji. Let's walk through six lines."

WALK = [
    (1, None, ["'Good, shine this flashlight steady right on the pipe joint.' Literally 'pocket electric lamp', ", (None, '懐中電灯'), ' is the Japanese word for a handheld flashlight.']),
    (4, None, ["'This big iron wrench? Here you go.' Handing tools or everyday items to someone uses ", (None, 'はい、どうぞ'), ", 'here you go', right after naming ", (None, '鉄'), " for 'iron'."]),
    (7, None, ["'Turn the blue wheel slowly to the left. Not too fast.' Pair ", (None, 'ゆっくり'), ", meaning 'slowly', against ", (None, '速すぎる'), ", where the ending means 'too fast'."]),
    (9, None, ["'Good, the burner lit too. A steady blue flame, right as it should be.' Listen for ", (None, '火'), ", the basic word for 'fire', and ", (None, '青い炎'), " for 'a blue flame'."]),
    (10, None, ["'Touch the copper pipe! It is already warming up!' Adding 'come' after 'become warm' in ", (None, '温かくなって来ました'), ' shows a change gradually happening right before your eyes.']),
    (11, None, ["'Three minutes to reach the third floor. Good run today, partner.' Instead of calling Mio a rookie, Kenji upgrades her to ", (None, '相棒'), ", meaning 'partner' or 'trusted sidekick'."]),
]

TRANSITION = "Now let's replay the cellar repair scene from start to finish."

OUTRO = "Steady blue fire, hot copper pipes, and Mio officially promoted from 'rookie' to 'partner'! Let's head back upstairs next time as Haruto comes down for breakfast."

CLOSING = ('mio', 'またね！')
