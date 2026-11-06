ID = 'hidamari-ryokan-s01e06-scene-06'
SHOW = 'hidamari-ryokan'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = '正式な鍵  (Permanent Keys)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'takashi': '隆', 'yuka': '由香', 'mio': '美央'}

INTRO = 'In the sunlit café corner, Takashi stands tall in front of Yuka and Mio holding page two of the letter with a beaming smile on his face. Listen first.'

STORY = [
    ('takashi', '由香さん、そのオーブンでは毎朝いくつシナモンロールとレモンケーキが焼けますか？', 'Yuka, how many cinnamon rolls and lemon cakes can that oven bake each morning?'),
    ('yuka', '今の二倍は焼けるよ！本当に中庭カフェを通りのみんなに開くの？', 'Double what I bake now! Are we really opening the courtyard café to everyone on our street?'),
    ('takashi', '明日の朝八時からです！店内に四テーブル、木の下に三テーブルです！', 'Starting tomorrow morning at eight! Four tables inside, and three tables under the tree!'),
    ('yuka', '夢だった自分たちのカフェが、この中庭に！市場のパン仲間に早く教えたい！', 'My dream café, right here in our own courtyard! I cannot wait to tell my baker friends at the market!'),
    ('takashi', 'そして美央さん、今日は金曜日……五日間の試用期間の最終日ですね。', 'And now, Mio, today is Friday—the final day of your five-day trial week.'),
    ('mio', 'あっ！スーツケースやボイラーや手紙の騒ぎで、すっかり忘れていました！', 'Oh! With all the commotion over suitcases, the boiler, and the letter, I completely forgot!'),
    ('takashi', '月曜日に固いドアを開けて以来、部屋もパイプも朝ごはんも、宿の契約まで救ってくれました。', 'Since opening our sticking door on Monday, you saved rooms, pipes, breakfast, and even our lease.'),
    ('yuka', 'もし隆さんが正社員にしないなら、私がキッチンで雇うからね！', 'If Takashi does not hire you full-time, I am hiring you in my kitchen!'),
    ('takashi', '渡しませんよ、由香さん！美央さん、当館の正式なフロントマネージャーとして残っていただけますか？', 'Hands off, Yuka! Mio, will you stay on as our permanent front-desk manager?'),
    ('mio', '皆さんと一緒にここでですか？はい、百回でも「はい」と言います！', "Here together with all of you? Yes—I say 'yes' a hundred times over!"),
    ('takashi', '素晴らしい！健二さんの大きな紙の帳面に、消えないインクで名前を書きましょう！', "Wonderful! Let's write your name in Kenji's big paper ledger in permanent ink!"),
    ('mio', '人生で一番素敵な最初の一週間になりました！', 'This has turned into the very best first week of my life!'),
]

OPENER = "Opening a neighbourhood café and turning a five-day trial into a permanent job call for celebration. Let's walk through six lines."

WALK = [
    (0, None, ["'Yuka, how many cinnamon rolls and lemon cakes can that oven bake each morning?' Counting general items without choosing a special counter is easy with ", (None, 'いくつ'), ", meaning 'how many?'."]),
    (2, None, ["'Starting tomorrow morning at eight! Four tables inside, and three tables under the tree!' Contrast ", (None, '店内'), ", literally 'inside the shop' for 'indoors', with ", (None, '木の下'), ' outside under the tree.']),
    (4, None, ["'And now, Mio, today is Friday—the final day of your five-day trial week.' Counting five days uses native Japanese numbers in ", (None, '五日間'), ', followed by ', (None, '最終日'), " for 'final day'."]),
    (7, None, ["'If Takashi does not hire you full-time, I am hiring you in my kitchen!' Workplace conversations often contrast trial work with ", (None, '正社員'), ', a permanent full-time employee.']),
    (9, None, ["'Here together with all of you? Yes—I say yes a hundred times over!' Counting occurrences adds a crisp counter onto ", (None, '百回'), ", meaning 'one hundred times'."]),
    (11, None, ["'This has turned into the very best first week of my life!' Looking at your whole life story uses ", (None, '人生'), ", literally 'person's life', paired with ", (None, '一週間'), " for 'one week'."]),
]

TRANSITION = "Now let's replay the big café celebration from start to finish."

OUTRO = 'Yuka gets her neighbourhood courtyard café at 8:00 AM tomorrow, and Mio stays permanently behind the front desk! Next time, golden lanterns glow across the evening courtyard.'

CLOSING = ('takashi', 'また会いましょう！')
