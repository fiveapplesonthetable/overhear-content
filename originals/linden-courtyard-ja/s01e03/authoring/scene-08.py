# Authoring module for linden-courtyard-ja-s01e03-scene-08.
ID = 'linden-courtyard-ja-s01e03-scene-08'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Ice-Cold Pipes  (氷のように冷たい配管)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = '地下室から上がってきたグレアムが、受付で待つハンナとアーサーに悪い知らせを伝えます。古いボイラーの真鍮の弁が壊れてしまったのです。英語の会話を最後までじっくり聴いてみましょう。'
OPENER = 'では、ボイラーをめぐる緊迫したやり取りを一文ずつ追っていきます。'
TRANSITION = '最後に、この場面の英語をもう一度ひと続きで聴いて仕上げましょう。'
OUTRO = '明日の朝のシャワーが冷水になるという大ピンチに、ハンナたちは早起きして金物屋へ向かう作戦を立てました。第三話はここまでです。次の話でまたお会いしましょう。'
CLOSING = ('graham', 'See you tomorrow!')
STORY = [
    ('arthur', 'Tell me it was just a tiny air bubble, Graham! Please!', 'ただの小さな空気の泡だったと言ってくれ、グレアム！頼む！'),
    ('graham', 'Bad news. The brass pressure valve on the old boiler just gave up.', '悪い知らせだ。古いボイラーの真鍮の圧力弁が、とうとういかれちまった。'),
    ('hannah', 'Does that mean no radiators tonight, or no hot water too?', 'それって、今夜は暖房が止まるってこと？それともお湯も出ないの？'),
    ('graham', 'The rooms will stay warm until morning, Hannah, because the brick walls hold heat.', '部屋は朝まで暖かいままだよ、ハンナ。レンガの壁が熱をためてくれるからね。'),
    ('arthur', 'Thank heavens! And the morning showers?', 'ありがたい！で、朝のシャワーは？'),
    ('graham', 'By tomorrow morning, the shower water will be ice cold.', '明日の朝までには、シャワーの水は氷のように冷たくなる。'),
    ('arthur', 'Ice cold showers?! With the Portland Travel Guide inspector on the third floor?!', '氷みたいに冷たいシャワーだって？！三階にはポートランド旅行ガイドの調査員がいるのに？！'),
    ('hannah', 'Do you have a spare brass valve in your toolbox?', '道具箱に予備の真鍮の弁はある？'),
    ('graham', 'Used my last one in winter. Only the old hardware shop past the bridge sells this size.', '最後の一つは冬に使っちまった。この大きさを売っているのは、橋の向こうの古い金物屋だけだ。'),
    ('hannah', 'What time does that hardware shop open?', 'その金物屋は何時に開くの？'),
    ('graham', 'Seven sharp, half an hour before breakfast.', '七時ちょうど、朝食の三十分前だ。'),
    ('hannah', 'Set your alarm, Graham. Tomorrow morning we beat the cold showers!', '目覚ましをかけておいて、グレアム。明日の朝は冷たいシャワーに先手を打つわよ！'),
]
WALK = [
    (0, None, ["'ただの小さな空気の泡だったと言ってくれ、グレアム！頼む！' すがるような願いを表す", (None, 'Tell me it was just'), 'は、命令形を使って「そうであってほしい」という気持ちを伝えています。']),
    (1, None, ["'悪い知らせだ。古いボイラーの真鍮の圧力弁が、とうとういかれちまった。' 機械が壊れたことを人にたとえた", (None, 'just gave up'), 'は、「あきらめる」という句動詞を使って、長年の働きの末に力尽きた様子を表します。']),
    (2, None, ["'それって、今夜は暖房が止まるってこと？それともお湯も出ないの？' 話の意味を確かめる", (None, 'Does that mean'), 'は、聞いた知らせの具体的な影響を尋ねる定番の言い方です。']),
    (3, None, ["'部屋は朝まで暖かいままだよ、ハンナ。レンガの壁が熱をためてくれるからね。' 熱を逃がさない性質を表す", (None, 'hold heat'), 'は、持つという動詞を使って「蓄えておく」という意味を表しています。']),
    (4, None, ["'ありがたい！で、朝のシャワーは？' 安堵の叫び", (None, 'Thank heavens'), 'は、天に感謝するという昔ながらの言い回しで、宗教色の薄い驚きの表現として使われます。']),
    (5, None, ["'明日の朝までには、シャワーの水は氷のように冷たくなる。' 冷たさを強調する", (None, 'ice cold'), 'は、名詞を形容詞の前に置いて「〜のように」という比喩を一語で表す形です。']),
    (6, None, ["'氷みたいに冷たいシャワーだって？！三階にはポートランド旅行ガイドの調査員がいるのに？！' 状況を付け加える前置詞", (None, 'With'), 'を文頭に置くと、「〜という状況で」という意味になり、慌てる理由を示しています。']),
    (7, None, ["'道具箱に予備の真鍮の弁はある？' 取っておきの部品を表す形容詞", (None, 'spare'), 'は、名詞の前に置いて「替えの」という意味で使います。予備の鍵やタイヤにも使える単語です。']),
    (8, None, ["'最後の一つは冬に使っちまった。この大きさを売っているのは、橋の向こうの古い金物屋だけだ。' 場所を表す", (None, 'past the bridge'), 'は、「通り過ぎて」という意味の前置詞を使って道案内のように位置を示します。']),
    (9, None, ["'その金物屋は何時に開くの？' お店の営業時間を尋ねる", (None, 'What time does that hardware shop open'), 'では、決まった予定を表すために現在形が使われています。']),
    (10, None, ["'七時ちょうど、朝食の三十分前だ。' 時刻の後ろに置く", (None, 'sharp'), 'は、本来「鋭い」という意味ですが、時間に添えると一分の遅れもないことを表します。']),
    (11, None, ["'目覚ましをかけておいて、グレアム。明日の朝は冷たいシャワーに先手を打つわよ！' 早起きの準備を表す", (None, 'Set your alarm'), 'と、相手より先に動くことを表す動詞', (None, 'beat'), 'の使い方を覚えておきましょう。']),
]
