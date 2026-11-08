# Authoring module for linden-courtyard-ja-s01e03-scene-03.
ID = 'linden-courtyard-ja-s01e03-scene-03'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Left at the Landing  (踊り場を左へ)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'hannah': 'Hannah', 'tessa': 'Tessa', 'arthur': 'Arthur'}
INTRO = '屋根裏部屋では、ハンナ、テッサ、アーサーがベッドを整え、丸い鏡を掛け、グレアムの真鍮のランプに明かりをともします。ちょうどその時、中庭の門のベルが八時ちょうどを告げるように鳴りました。まずは英語のまま、場面を通して聴いてみましょう。'
OPENER = 'ここからは、仕上げに追われる三人の言葉を一つずつ確かめていきます。'
TRANSITION = 'では、仕上げの場面を始めから終わりまで続けて聴きましょう。'
OUTRO = '部屋はすっかり整い、ハンナは落ち着いた足取りでお客さんを迎えに階段を下りていきます。次の場面では、雨の中からついにお客さんが現れます。'
CLOSING = ('hannah', 'Bye for now!')
STORY = [
    ('tessa', 'Tuck that sheet corner tight, Hannah! Here go the two soft pillows.', 'シーツの角をきっちり折り込んで、ハンナ！ふかふかの枕を二つ置くわよ。'),
    ('hannah', 'Done! And the blue rug fits right beside the bed.', 'できた！それに青いラグもベッドのすぐ横にぴったり収まったわ。'),
    ('arthur', 'Where should I hang this round mirror? Left of the window or right?', 'この丸い鏡はどこに掛けましょう？窓の左ですか、右ですか？'),
    ('hannah', 'Right beside the desk, where the light is good.', '机のすぐ横がいいわ、明るいところだから。'),
    ('tessa', "Plug in Graham's brass lamp... oh, look how warm that yellow light is!", 'グレアムの真鍮のランプをつけて…まあ、見て、なんて温かい黄色の光！'),
    ('arthur', 'Honestly, I almost want to sleep up here myself tonight!', '正直、今夜は僕がここで寝たいくらいですよ！'),
    ('hannah', 'Wait, what discount should we offer him for changing rooms?', '待って、部屋を替えてもらうお詫びに、どんな割引をしたらいいかしら？'),
    ('arthur', 'Half price for tonight, and free breakfast all week!', '今夜は半額、それに一週間ずっと朝食無料にしましょう！'),
    ('tessa', 'Generous! Did you just hear the courtyard gate bell downstairs?', '太っ腹ね！今、下で中庭の門のベルが鳴ったのが聞こえた？'),
    ('hannah', "Eight o'clock on the dot! Our guest is here!", '八時きっかり！お客さんが着いたわ！'),
    ('arthur', 'My heart is pounding! Hannah, you explain it, you sound calm and honest!', '心臓がどきどきしてます！ハンナ、説明はお願いします、落ち着いていて誠実に聞こえますから！'),
    ('hannah', 'Leave it to me. Let us go down and welcome him.', '任せて。下りていって、お迎えしましょう。'),
]
WALK = [
    (0, None, ["'シーツの角をきっちり折り込んで、ハンナ！ふかふかの枕を二つ置くわよ。' 布の端をすき間に押し込む動作を", (None, 'Tuck that sheet corner tight'), 'と言い、最後の語は副詞のように働いて固く締める様子を表します。']),
    (1, None, ["'できた！それに青いラグもベッドのすぐ横にぴったり収まったわ。' 大きさや場所が合うことを", (None, 'fits'), 'という動詞で表し、続く', (None, 'right beside the bed'), 'の最初の語は位置をちょうどと強める働きをしています。']),
    (2, None, ["'この丸い鏡はどこに掛けましょう？窓の左ですか、右ですか？' 助言を求める疑問文", (None, 'Where should I hang'), 'は、助動詞を使って自分がどうすべきかを尋ねる丁寧な形です。']),
    (3, None, ["'机のすぐ横がいいわ、明るいところだから。' ここでは場所を補足する関係副詞を使った", (None, 'where the light is good'), 'が、前の場所の説明を後ろから付け加えています。']),
    (4, None, ["'グレアムの真鍮のランプをつけて…まあ、見て、なんて温かい黄色の光！' 電化製品をコンセントにつなぐ動作は", (None, 'Plug in'), 'です。感嘆を表す', (None, 'look how warm that yellow light is'), 'では、疑問詞の後に形容詞が続きます。']),
    (5, None, ["'正直、今夜は僕がここで寝たいくらいですよ！' 本音を打ち明ける前置きの", (None, 'Honestly'), 'という前置きに続けて、', (None, 'I almost want to sleep up here myself'), 'では、ほとんどという副詞が気持ちの度合いをやわらげています。']),
    (6, None, ["'待って、部屋を替えてもらうお詫びに、どんな割引をしたらいいかしら？' 理由を表す前置詞の後に動名詞を続けた", (None, 'for changing rooms'), 'では、部屋が複数形になっている点に注意しましょう。一つの部屋から別の部屋へ移るので二つの部屋が関わるからです。']),
    (7, None, ["'今夜は半額、それに一週間ずっと朝食無料にしましょう！' 料金の割引を表す", (None, 'Half price'), 'と、期間全体を表す', (None, 'all week'), 'はどちらも冠詞なしで使われる決まった言い方です。']),
    (8, None, ["'太っ腹ね！今、下で中庭の門のベルが鳴ったのが聞こえた？' 気前のよさをほめる", (None, 'Generous'), 'とほめた後の問いかけ', (None, 'Did you just hear'), 'では副詞がたった今という意味を加えています。']),
    (9, None, ["'八時きっかり！お客さんが着いたわ！' 時刻がぴったりであることを強調する", (None, 'on the dot'), 'は、時計の針が目盛りの点に重なる様子から生まれた慣用句です。']),
    (10, None, ["'心臓がどきどきしてます！ハンナ、説明はお願いします、落ち着いていて誠実に聞こえますから！' 激しく脈打つ様子は", (None, 'My heart is pounding'), 'と言い、印象を伝える', (None, 'you sound calm and honest'), 'では動詞の後に形容詞が続きます。']),
    (11, None, ["'任せて。下りていって、お迎えしましょう。' 頼もしく引き受けるときの決まり文句が", (None, 'Leave it to me'), 'です。さらに後半の', (None, 'welcome him'), 'の動詞は、歓迎の挨拶だけでなく、迎え入れる行為そのものも表します。']),
]
