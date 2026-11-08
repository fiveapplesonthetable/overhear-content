# Authoring module for linden-courtyard-ja-s01e05-scene-08.
ID = 'linden-courtyard-ja-s01e05-scene-08'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'The Red-Stamped Letter  (赤い判の手紙)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = '外の中庭ではケイレブとオーウェンが木の下で向かい合っています。その頃フロントでは、アーサーが大家からの手紙を開封し、顔色を失いました。建物が事務所用に売りに出され、三十日後には買い手の下見があるというのです。それではこの話の最後の場面を英語で聴いてみましょう。'
OPENER = 'では、喜びから一転する衝撃の展開を、一行ずつたどっていきましょう。'
TRANSITION = 'それでは場面全体を、もう一度自然なスピードで聴いてください。'
OUTRO = 'アーサーたちは兄弟の再会を邪魔しないよう、ひとまず不安を胸にしまいました。けれども通知の裏には、折りたたまれた二枚目の紙がまだ残っています。続きは次の話、いよいよ最終話です。それではまた。'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('tessa', 'Hannah, look through the glass. They are standing face to face under the tree!', 'ハンナ、ガラス越しに見て。二人が木の下で向かい合って立っているわ！'),
    ('hannah', 'Neither of them walked away! Caleb is pointing at the two chairs right now!', 'どちらも立ち去らなかった！ケイレブが今、二つの椅子を指さしてる！'),
    ('arthur', 'Wonderful... let me just glance at this landlord letter while we wait.', 'すばらしい……待っている間に、この大家からの手紙にちょっと目を通しておこう。'),
    ('tessa', 'Probably a boring notice about painting the street shutters.', 'どうせ通りのよろい戸の塗り替えについての退屈なお知らせですよ。'),
    ('arthur', 'Oh... oh no. Where is my chair? My knees feel weak.', 'ああ……なんてことだ。椅子はどこだ？膝に力が入らない。'),
    ('hannah', 'Arthur! Your face went completely white! Sit down, what does the letter say?', 'アーサー！顔が真っ青ですよ！座ってください、手紙には何て書いてあるんですか？'),
    ('arthur', 'Read the top line for me, Hannah. Tell me my glasses are playing tricks again!', '一番上の行を読んでくれ、ハンナ。また眼鏡が私をからかっているだけだと言ってくれ！'),
    ('hannah', "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", '「不動産譲渡のお知らせ：中庭八番地ビルを商業用事務所として売却に出します」'),
    ('tessa', 'Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!', '商業用事務所として売却？！うちのゲストハウスと厨房を灰色の事務所にするっていうの？！'),
    ('arthur', 'They give us thirty days before new buyers inspect the building!', '新しい買い手が建物を下見するまで、三十日しかないそうだ！'),
    ('hannah', 'Wait, there is a second folded page clipped to the back of this notice...', '待って、この通知の裏に、折りたたまれた二枚目の紙がクリップで留めてあります……'),
    ('arthur', 'Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!', '外の人にはまだ一言も言うな！まずは兄弟二人に金曜日の午後を楽しませてあげよう！'),
]
WALK = [
    (0, None, ["'ハンナ、ガラス越しに見て。二人が木の下で向かい合って立っているわ！' 前置詞を使った", (None, 'look through the glass'), 'は、透明なものを通して向こう側を見ることです。また', (None, 'face to face'), 'は同じ名詞を前置詞でつないだ慣用句で、日本語の「顔と顔を合わせて」にぴったり重なります。']),
    (1, None, ["'どちらも立ち去らなかった！ケイレブが今、二つの椅子を指さしてる！' 否定の代名詞を主語にした", (None, 'Neither of them walked away'), 'は、二人のうち一人も去らなかったことを表します。句動詞の副詞は「離れて」の意味を添えています。']),
    (2, None, ["'すばらしい……待っている間に、この大家からの手紙にちょっと目を通しておこう。' 動詞を使った", (None, 'glance at'), 'は、じっくりではなく短く見ることを表します。前に置かれた許可の表現は、自分の行動を控えめに切り出す言い方です。']),
    (3, None, ["'どうせ通りのよろい戸の塗り替えについての退屈なお知らせですよ。' 推量の副詞で始まる", (None, 'Probably a boring notice'), 'は、主語と動詞を省いた会話らしい省略文です。形容詞は「うんざりさせるような」という意味です。']),
    (4, None, ["'ああ……なんてことだ。椅子はどこだ？膝に力が入らない。' 感覚を表す動詞と形容詞を組み合わせた", (None, 'My knees feel weak'), 'は、ショックで体から力が抜ける様子を表す典型的な言い方です。']),
    (5, None, ["'アーサー！顔が真っ青ですよ！座ってください、手紙には何て書いてあるんですか？' 変化を表す動詞の過去形を使った", (None, 'Your face went completely white'), 'では、英語では驚きや恐怖で血の気が引いた顔を「白」で表します。日本語の「青ざめる」との色の違いに注目しましょう。']),
    (6, None, ["'一番上の行を読んでくれ、ハンナ。また眼鏡が私をからかっているだけだと言ってくれ！' 慣用句の", (None, 'playing tricks again'), 'は、目や記憶が自分をだまして見間違いをさせるときに使う表現です。']),
    (7, None, ["'「不動産譲渡のお知らせ：中庭八番地ビルを商業用事務所として売却に出します」' 公式文書らしい堅い名詞句", (None, 'Notice of Property Transfer'), 'は、前置詞で名詞をつなぐ見出しの形です。さらに', (None, 'offered for commercial office sale'), 'は、過去分詞で受け身の意味を短く表しています。']),
    (8, None, ["'商業用事務所として売却？！うちのゲストハウスと厨房を灰色の事務所にするっていうの？！' 動詞と前置詞を組み合わせた", (None, 'Turn our guesthouse and kitchen into'), 'は、あるものを別のものへ作り変えることを表す重要な型です。']),
    (9, None, ["'新しい買い手が建物を下見するまで、三十日しかないそうだ！' 期限を示す", (None, 'thirty days before new buyers inspect'), 'では、接続詞の後で未来のことを現在形で表しています。動詞は「細かく調べる、点検する」という意味です。']),
    (10, None, ["'待って、この通知の裏に、折りたたまれた二枚目の紙がクリップで留めてあります……' 過去分詞を形容詞として使った", (None, 'a second folded page'), 'では、序数と分詞が名詞の前に並びます。続く', (None, 'clipped to the back'), 'も過去分詞で、後ろから名詞を説明しています。']),
    (11, None, ["'外の人にはまだ一言も言うな！まずは兄弟二人に金曜日の午後を楽しませてあげよう！' 動詞の後に目的語と原形を続けた", (None, 'Let the two brothers have'), 'は、相手が望むことを許したり見守ったりする使役の形です。冒頭の名詞句だけの命令も、口止めの定番表現です。']),
]
