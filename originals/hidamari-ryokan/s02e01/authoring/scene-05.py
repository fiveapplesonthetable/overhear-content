ID = 'hidamari-ryokan-s02e01-scene-05'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 5
TITLE = 'サンルームを測る  (Measuring the Sunroom)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'haruto': '陽翔', 'daiki': '大輝', 'mio': '美央'}

INTRO = 'Ten minutes later, Haruto hurries downstairs with his leather notebook alongside his older brother Daiki, who walked over early from his flat in Osaka after their Friday reunion. Mio meets them at the sunroom door. Listen first.'

STORY = [
    ('haruto', '美央さん、由香さんから聞きました。隠れた九番目の部屋を開けたんですね！', 'Mio, Yuka told us! You opened a hidden ninth room!'),
    ('daiki', '弟はトーストも食べないで、メジャーを持って来ましたよ。', "My little brother didn't even eat his toast. He just grabbed his tape measure."),
    ('mio', 'お二人とも、どうぞ中へ！この部屋を開けても安全か、教えてください。', 'Come in, both of you! Please tell us if this room is safe to open.'),
    ('haruto', '幅四メートル、長さ六メートル。左はレンガの壁、上は木の天井です。', 'Four metres wide, six metres long. A brick wall on the left, a wooden ceiling above.'),
    ('daiki', '手を一回たたいてみてください。外の音がほとんど聞こえないでしょう？', 'Try clapping your hands once. You can hardly hear the street, can you?'),
    ('haruto', 'エコーがありません！木の天井のおかげで、音楽も声もやわらかいです。', 'No echo! Thanks to the wooden ceiling, music and voices both sound soft.'),
    ('mio', 'じゃあ、由香さんのカフェも和子さんのピアノも、上のお客さまを起こしませんか？', "So Yuka's café and Kazuko's piano won't wake the guests upstairs?"),
    ('haruto', '大丈夫です。厚いレンガの壁が、階段への音を全部止めます。', 'Not at all. The thick brick wall stops every sound toward the stairs.'),
    ('daiki', 'この週末は、市役所の仕事が休みです。美央さん、私たちを使ってください！', "I'm off from City Hall this weekend. Mio, put us both to work!"),
    ('mio', 'お昼のあとで、地下室のテーブルを運んでもらえますか？', 'Could you carry the cellar tables in after lunch?'),
    ('daiki', '喜んで。役所の机に座っているより、陽翔と働くほうがずっといいです。', 'Gladly. Working with Haruto beats sitting at an office desk by far.'),
    ('haruto', 'まず、窓の留め金をスケッチさせてください。中庭からきれいな空気が入るように。', 'First let me sketch the window latches, so fresh air comes in from the courtyard.'),
]

OPENER = "An architect brings his measuring tape and his brother. Let's walk through six lines."

WALK = [
    (1, None, ["'My little brother didn't even eat his toast. He just grabbed his tape measure.' Daiki's ", (None, 'メジャー'), " is the tape measure, a word Japanese took from English 'measure'."]),
    (3, None, ["'Four metres wide, six metres long. A brick wall on the left, a wooden ceiling above.' Haruto's numbers are easy to borrow: ", (None, '幅'), " means 'width', and ", (None, 'メートル'), " is simply 'metre'."]),
    (4, None, ["'Try clapping your hands once. You can hardly hear the street, can you?' Daiki uses ", (None, 'ほとんど'), ", 'almost', with a 'can't hear' ending, so together they mean 'hardly'."]),
    (5, None, ["'No echo! Thanks to the wooden ceiling, music and voices both sound soft.' Haruto credits the ceiling with ", (None, 'おかげで'), ", 'thanks to'. Put any helper before it, like 'thanks to you'."]),
    (8, None, ["'I'm off from City Hall this weekend. Mio, put us both to work!' The word for City Hall is ", (None, '市役所'), ", literally 'city-service-place'. A moment later Daiki shortens it to just 'service-place'."]),
    (9, None, ["'Could you carry the cellar tables in after lunch?' Mio's polite way to ask a favour is ", (None, '運んでもらえますか'), ": 'carry' plus 'could I receive', so literally 'could I get you to carry?'"]),
]

TRANSITION = "Now let's replay the whole measuring scene from start to finish."

OUTRO = 'Haruto approves the acoustics, and Daiki volunteers a pair of strong hands for the weekend. See you next time.'

CLOSING = ('haruto', 'またね！')
