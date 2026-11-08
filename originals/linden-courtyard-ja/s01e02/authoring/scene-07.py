# Authoring module for linden-courtyard-ja-s01e02-scene-07.
ID = 'linden-courtyard-ja-s01e02-scene-07'
SHOW = 'linden-courtyard-ja'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = 'How Regulars Order  (常連さんの頼み方)'
LEVEL = 'A1 — 初級'
PAIR = 'en-ja'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = '昼下がりの静かなひととき、カフェコーナーではテッサがハンナに温かいコーヒーを勧めています。隅の方ではグレアムがドライバーを取り出して緩んだ椅子のねじを締め直しています。まずは午後の穏やかな会話を英語で聴いてみましょう。'
OPENER = 'それではくつろいだ同僚同士のやり取りを、一行ずつ見ていきましょう。'
TRANSITION = 'ではもう一度、自然な会話のやり取りを通して聴いてみましょう。'
OUTRO = 'すっかり仲間の輪に溶け込んだハンナですが、夕方になるとフロントでアーサーが青ざめた顔をして立ち尽くしていました。それではまた後で。'
CLOSING = ('tessa', 'See you later!')
STORY = [
    ('tessa', 'Sit down, Hannah! You ran half the city this morning, drink some coffee.', '座りなさいよ、ハンナ！今朝は街の半分を走り回ったんだから、コーヒーを少し飲んで。'),
    ('hannah', 'Gladly! With milk and a little sugar, please.', '喜んで！ミルクと、お砂糖を少し入れてお願いします。'),
    ('graham', 'Watch that corner chair, wait ten seconds while I tighten this screw.', 'その隅の椅子には気をつけて、私がこのねじを締める間、十秒待ってくれ。'),
    ('hannah', 'Done already? You carry a screwdriver everywhere, Graham!', 'もう終わったんですか？グレアムはどこへでもドライバーを持ち歩いているんですね！'),
    ('graham', 'Old houses loosen one screw every Tuesday. Now sit.', '古い建物は毎週火曜日にねじが一本緩むんだよ。さあ座りなさい。'),
    ('tessa', 'Look, you survived the breakfast rush and the mystery phone call!', 'ほら、朝食のラッシュも謎の電話も、ちゃんと乗り切ったじゃない！'),
    ('hannah', 'Honestly, I like it here much better than my old gray office.', '正直に言って、前の灰色のオフィスよりここの方がずっと好きです。'),
    ('tessa', 'Wait until Friday at noon, I want a front row seat when the suitcase man walks in!', '金曜日の正午まで待ってて、あのスーツケースの男が入ってくるときは最前列の席で見たいわ！'),
    ('graham', 'Nobody stares at guests. We hand over the bag and mind our business.', '誰もお客さまをじろじろ見たりしないよ。鞄を引き渡して、余計な詮索はしないんだ。'),
    ('tessa', 'Listen to him! Graham is twice as curious as we are!', 'ちょっと聞いてよ！グレアムったら私たちの二倍も好奇心旺盛なくせに！'),
    ('graham', 'I am simply checking security. That is my job.', '私はただ防犯の確認をしているだけだよ。それが私の仕事だからね。'),
    ('hannah', 'Sure, Graham, your secret is safe with us!', 'はいはい、グレアム、あなたの秘密は私たちがちゃんと守りますからね！'),
]
WALK = [
    (0, None, ["'座りなさいよ、ハンナ！今朝は街の半分を走り回ったんだから、コーヒーを少し飲んで。' 街中を駆け回った働きぶりを", (None, 'You ran half the city'), 'と労い、温かく', (None, 'drink some coffee'), 'と勧めています。']),
    (1, None, ["'喜んで！ミルクと、お砂糖を少し入れてお願いします。' 相手の申し出を明るく受ける一言の", (None, 'Gladly'), 'に続けて、数えられない砂糖の少量を', (None, 'With milk and a little sugar'), 'と丁寧に頼みます。']),
    (2, None, ["'その隅の椅子には気をつけて、私がこのねじを締める間、十秒待ってくれ。' 足元や家具に注意を促す", (None, 'Watch that corner chair'), 'と、作業の間の', (None, 'while I tighten this screw'), 'の組み合わせです。']),
    (3, None, ["'もう終わったんですか？グレアムはどこへでもドライバーを持ち歩いているんですね！' 予想以上の早さに驚く", (None, 'Done already'), 'と、ねじ回しを表す英語ならではの単語', (None, 'carry a screwdriver everywhere'), 'に注目しましょう。']),
    (4, None, ["'古い建物は毎週火曜日にねじが一本緩むんだよ。さあ座りなさい。' 毎週繰り返されるお決まりの現象として現在形の", (None, 'loosen one screw every Tuesday'), 'と冗談めかして言っています。']),
    (5, None, ["'ほら、朝食のラッシュも謎の電話も、ちゃんと乗り切ったじゃない！' 大変な時間帯を無事に切り抜けたことを", (None, 'you survived the breakfast rush'), 'と笑顔で称えています。']),
    (6, None, ["'正直に言って、前の灰色のオフィスよりここの方がずっと好きです。' 本音を切り出す文頭の", (None, 'Honestly'), 'と、比較級をさらに強める', (None, 'much better than'), 'の組み合わせです。']),
    (7, None, ["'金曜日の正午まで待ってて、あのスーツケースの男が入ってくるときは最前列の席で見たいわ！' 一番よく見える特等席を", (None, 'a front row seat'), 'と呼び、歩いて入ってくる瞬間を', (None, 'when the suitcase man walks in'), 'と表しています。']),
    (8, None, ["'誰もお客さまをじろじろ見たりしないよ。鞄を引き渡して、余計な詮索はしないんだ。' じっと見つめることを否定する", (None, 'Nobody stares at guests'), 'と、自分の務めに専念する慣用句', (None, 'mind our business'), 'の落ち着いた一言です。']),
    (9, None, ["'ちょっと聞いてよ！グレアムったら私たちの二倍も好奇心旺盛なくせに！' 二倍という語を同等の比較に組み合わせた", (None, 'twice as curious as we are'), 'はとても英語らしい表現です。']),
    (10, None, ["'私はただ防犯の確認をしているだけだよ。それが私の仕事だからね。' ただ単にそれだけだとすまして答える", (None, 'I am simply checking security'), 'と、決め台詞の', (None, 'That is my job'), 'の組み合わせです。']),
    (11, None, ["'はいはい、グレアム、あなたの秘密は私たちがちゃんと守りますからね！' 誰にもばらさないよと温かくからかう決まり文句の", (None, 'your secret is safe with us'), 'で楽しく締めくくっています。']),
]
