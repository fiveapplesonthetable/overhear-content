ID = 'hidamari-ryokan-s01e04-scene-02'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = '青い木のドア  (The Blue Door)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'kenji': '健二'}

INTRO = 'Ten minutes later, Mio has crossed the river bridge in Osaka, yet two narrow lanes branch off past the pharmacy. She phones Kenji from beside a small stone fountain. Listen first.'

STORY = [
    ('mio', '健二さん、聞こえますか？今、緑の薬局を過ぎたところです！', 'Kenji, can you hear me? I just passed the green pharmacy!'),
    ('kenji', 'はっきり聞こえるぞ。小さな石の噴水の横に立っているか？', 'Loud and clear. Are you standing beside the small stone fountain?'),
    ('mio', 'はい！左に細い道が二本あります。どちらを行けばいいですか？', 'Yes! There are two narrow lanes on the left. Which one should I take?'),
    ('kenji', '狭い路地じゃなくて、花屋の横の二番目の道を行け。', 'Not the cramped alley—take the second street beside the flower shop.'),
    ('mio', '今歩いています……あっ、金色の鍵の看板と青いドアが見えました！', 'Walking now... oh, I can see the golden key sign and the blue door!'),
    ('kenji', 'よし！シャッターは開いているか？', 'Good! Is the shutter open?'),
    ('mio', '店主さんがちょうど今、鍵を開けています！一秒だけ電話を切らないで。', 'The shopkeeper is unlocking it right now! Stay on the line one second.'),
    ('kenji', '中の真鍮の輪が幅二十ミリか、必ず確かめろよ。', 'Make sure the brass ring inside is twenty millimetres wide.'),
    ('mio', '古いバルブと合わせてくれました！棚に残り二つだけあります！', 'He matched it against the old valve! There are two left on the shelf!'),
    ('kenji', '両方買え！予備があれば来年の冬も安心だ。', 'Buy both! Having a spare keeps us safe next winter too.'),
    ('mio', '現金で払いました！道具箱を開けて待っていてください、走って帰ります！', 'Paid in cash! Keep your toolbox open, I am running back now!'),
    ('kenji', '急げよ……たった今、二階の階段から足音が聞こえたぞ！', 'Hurry up... I just heard footsteps on the second-floor stairs!'),
]

OPENER = "Checking landmarks by phone and buying hardware in cash keep this scene brisk. Let's look at six lines."

WALK = [
    (0, None, ["'Kenji, can you hear me? I just passed the green pharmacy!' Saying an action finished moments ago uses ", (None, '過ぎたところです'), ', built around ', (None, 'ところ'), " for 'right at the moment of'."]),
    (3, None, ["'Not the cramped alley—take the second street beside the flower shop.' Everyday town shops add a friendly shop-ending: ", (None, '花屋'), " joins 'flower' and 'shop' for 'florist', right before ", (None, '二番目'), " for 'second'."]),
    (4, None, ["'Walking now... oh, I can see the golden key sign and the blue door!' When a landmark comes into view on its own, Japanese says ", (None, '見えました'), ", meaning 'came into sight'."]),
    (9, None, ["'Buy both! Having a spare keeps us safe next winter too.' Selecting all two of a pair uses one crisp word: ", (None, '両方'), ", meaning 'both', while ", (None, '来年の冬'), " means 'next winter'."]),
    (10, None, ["'Paid in cash! Keep your toolbox open, I am running back now!' Paying at the counter uses ", (None, '現金で払いました'), ", 'I paid in cash', and ", (None, '走って帰ります'), " joins 'run' with 'go home'."]),
    (11, None, ["'Hurry up... I just heard footsteps on the second-floor stairs!' Combining 'foot' and 'sound' creates ", (None, '足音'), ", the transparent compound for 'footsteps'."]),
]

TRANSITION = "Now let's replay Mio's call from across the bridge."

OUTRO = 'Two new brass valves in her pocket, and early risers already coming down the stairs! Next time, Yuka and Takashi launch a delicious distraction.'

CLOSING = ('kenji', 'じゃあね！')
