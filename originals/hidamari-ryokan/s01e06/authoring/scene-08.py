ID = 'hidamari-ryokan-s01e06-scene-08'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 6
SCENE = 8
TITLE = '九号室の箱  (Room Nine)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kenji': '健二', 'mio': '美央', 'takashi': '隆'}

INTRO = 'Late Friday night after the courtyard empties, Mio and Takashi are closing the front desk when Kenji climbs up from the back cellar carrying spare café chairs—and a dusty wooden chest. Listen first.'

STORY = [
    ('mio', '健二さん、ボイラー室の奥に折りたたみ椅子は三脚ありましたか？', 'Kenji, did you find the three folding chairs behind the boiler room?'),
    ('kenji', '椅子はあったぞ。それと古いレンガの仕切りの裏で、これを見つけた。', 'Found the chairs. And behind an old brick partition, I found this.'),
    ('takashi', '小さな杉の木の箱ですか？ここに十五年いますが、一度も見たことがありません！', 'A small cedar chest? I have been here fifteen years and have never seen it once!'),
    ('mio', '上の真鍮プレートのほこりを払ってみましょう……あっ、この番号を読んでください！', "Let's brush the dust off the brass plate on top... wait, read this number!"),
    ('takashi', 'おでこから眼鏡を下ろしますね……えっ、「九号室」！？', "Let me pull my glasses down from my forehead... wait, 'Room Nine'?!"),
    ('mio', '健二さん、後ろの木の鍵掛けを見てください。一、二、三、四、五、六、七、八！', 'Kenji, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!'),
    ('takashi', 'この旅館は昔からずっと八室だけですよ！一体どこに九号室があるんですか！？', 'This inn has always had only eight rooms! Where on earth is Room Nine?!'),
    ('kenji', '箱を傾けると音がするぞ。中で何か金属が滑った。', 'Listen when I tilt the box: something metal slid inside.'),
    ('mio', '前の留め金に小さな鍵穴があります！それに底を見て、テープで古い真鍮の鍵が貼ってあります！', 'There is a tiny keyhole on the front latch! And look underneath: an old brass key is taped to the bottom!'),
    ('takashi', '九本目の真鍮の鍵ですか！？今夜開けますか、それとも朝まで待ちますか！？', 'A ninth brass key?! Do we open it tonight, or wait until morning?!'),
    ('kenji', '蝶番に挟まっている折りたたまれた設計図を見ろ……この一階に、隠し扉が描いてあるぞ！', 'Look at the folded blueprint tucked in the hinge... there is a hidden door drawn on this first floor!'),
    ('mio', '二人とも懐中電灯を持ってください！私の二週目は、たった今から始まりますよ！', 'Grab the flashlight, both of you! My second week starts right this second!'),
]

OPENER = "Numbers one through nine, never-before-seen discoveries, and a mysterious blueprint wrap up Season 1. Let's walk through six lines."

WALK = [
    (2, None, ["'A small cedar chest? I have been here fifteen years and have never seen it once!' Talking about something you have never experienced uses ", (None, '一度も見たことがありません'), ", 'have never seen it even once'."]),
    (4, None, ["'Let me pull my glasses down from my forehead... wait, Room Nine?!' Room numbers attach the same suffix every time: ", (None, '九号室'), " means 'Room Nine'."]),
    (5, None, ["'Kenji, look at the wooden key board behind us: one, two, three, four, five, six, seven, eight!' Counting straight from one to eight in one breath gives you ", (None, '一、二、三、四、五、六、七、八'), ', the backbone of every date, floor, and price in Japanese.']),
    (6, None, ["'This inn has always had only eight rooms! Where on earth is Room Nine?!' Adding emphasis to a baffled question uses ", (None, '一体どこに'), ", meaning 'where on earth?'."]),
    (10, None, ["'Look at the folded blueprint tucked in the hinge... there is a hidden door drawn on this first floor!' Architectural drawings are ", (None, '設計図'), ", 'blueprints', revealing ", (None, '隠し扉'), ", 'a hidden door'."]),
    (11, None, ["'Grab the flashlight, both of you! My second week starts right this second!' Mio launches the next chapter with ", (None, '二週目'), ", 'week two', and ", (None, '始まります'), ", 'begins!'."]),
]

TRANSITION = "Now let's replay the Season 1 finale cliffhanger from start to finish."

OUTRO = "A ninth brass key, a dusty cedar chest stamped 'Room Nine', and an old blueprint pointing to a hidden ground-floor door! Season 1 of Hidamari Inn is complete—thank you for listening, and see you in Season 2!"

CLOSING = ('kenji', 'また会いましょう！')
