ID = 'the-naked-director-s01e01-scene-28'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 28
TITLE = '一日の目標は六十本だ  (The Daily Goal Is Sixty)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'muranishi': '村西', 'owner': 'オーナー', 'toshi': 'トシ'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Seeing a stack of unsold cassette tapes, our protagonist's salesman instincts suddenly wake up. "
    "He marches into a specialty shop, charms the owner into buying twenty tapes for sixty thousand yen cash, and proposes an ambitious partnership on the street outside. "
    "Listen to him work his magic."
)

STORY = [
    ('muranishi', '俺がこれを売るよ。', 'I will sell these.', [(662, '売るよ')], 'Added が and を for clear A1 sentence.'),
    ('toshi', 'そう簡単に売れないよ。', 'They will not sell that easily.', [(663, 'そう簡単に売れ')], 'Standardised 売れねえよ to 売れないよ.'),
    ('owner', 'あんた、面白いね。買ってやるよ。', 'You are a funny guy. I will buy them from you.', [(666, 'あんた'), (667, '買ってやるよ')], 'Standardised おもしれえな to 面白いね.'),
    ('muranishi', 'ありがとうございます。さすがオーナー様、お目が高い！', 'Thank you very much. As expected of you, Owner, you have a keen eye!', [(667, 'ありがとうございます'), (668, 'さすがオーナー様 お目が高い')], ''),
    ('toshi', '売れた！一本三千円で六万円だ。', 'They sold! At three thousand yen apiece, that is sixty thousand yen.', [(670, '売れた'), (671, '万円')], 'Wrote 一本三千円 and 六万円 in kanji.'),
    ('toshi', 'あんた営業マンだったのかよ？', 'Wait, were you a salesman?', [(673, 'あんた営業マンだったのかよ')], ''),
    ('muranishi', 'そうだ。これ、一日何本ぐらい売れてるんだ？', 'That is right. Roughly how many of these sell per day?', [(674, 'そうだ これ'), (674, '何本ぐらい売れて')], 'Wrote 一日 in kanji.'),
    ('toshi', 'まあ、多くて一日二本だな。', 'Well, two a day at most.', [(675, 'まあ 多くて')], 'Wrote 一日二本 in kanji.'),
    ('muranishi', 'じゃあ他の店も行こう。一日の目標は六十本だ。', 'Then let us hit other shops too. Our daily target is sixty.', [(676, 'じゃあ 他の店も行こう'), (677, '目標')], 'Wrote 一日 and 六十本 in kanji.'),
    ('toshi', 'ちょっと待てよ。俺と組むってことか？', 'Hold on a second. Does that mean teaming up with me?', [(678, 'ちょっと待てよ'), (679, '俺と組むってことか')], ''),
    ('muranishi', 'だめか？', 'Is that a problem?', [(680, 'ダメか')], 'Wrote だめ in hiragana.'),
    ('toshi', 'あんた、この世界に入る覚悟はあるのか？', 'Do you really have the resolve to step into this world?', [(681, 'あんた この世界に入る覚悟')], 'Standardised あんのかよ to あるのか.'),
]

OPENER = "Notice how the protagonist switches smoothly between silky customer flattery inside the shop and brisk business numbers outside."

WALK = [
    (1, None, [
        "'They will not sell that easily.'  Check out ",
        (None, "簡単に"), " this word means easily or simply, and ",
        (None, "売れない"), " comes from the verb for selling well on the market—distinct from what the seller does."
    ]),
    (2, '買ってやるよ。', [
        '"\'I will buy them from you.\' Amused by the pitch, the shopkeeper uses " Check out ',
        (None, "買ってやるよ"), ", doing the newcomer a favour."
    ]),
    (3, 'さすがオーナー様、お目が高い！', [
        '"\'As expected of you, Owner, you have a keen eye!\' Every salesperson in Japan knows " It features ',
        (None, "さすが"), ", 'true to your reputation!', and the classic flattery ",
        (None, "お目が高い"), "—literally 'your eyes are high', meaning refined taste!"
    ]),
    (4, None, [
        '"\'They sold! At three thousand yen apiece, that is sixty thousand yen.\' Long cylindrical or spooled items like tapes, bottles, and umbrellas count with the counter for long things: " Check out ',
        (None, "一本三千円"), " totals ",
        (None, "六万円"), ", sixty thousand yen."
    ]),
    (5, None, [
        "'Wait, were you a salesman?'  They are saying ",
        (None, "営業マン"), " blends the Japanese word for sales with the English word 'man'—the everyday word for a sales rep."
    ]),
    (6, None, [
        '"\'Roughly how many of these sell per day?\' Asking " Check out ',
        (None, "何本ぐらい"), " combines the word for how many tapes with the word for approximately."
    ]),
    (7, None, [
        "'Well, two a day at most.'  It features ",
        (None, "多くて"), " comes from the word for many, and at the start of an estimate it this word means 'at the very most'."
    ]),
    (8, 'じゃあ他の店も行こう。', [
        '"It means \'Then let us hit other shops too.\' " In this sentence, ',
        (None, "他の店"), " this word means other shops, and ",
        (None, "行こう"), " this word is the energetic 'let us go!' form of the verb to go."
    ]),
    (8, '一日の目標は六十本だ。', [
        '"\'Our daily target is sixty.\' Where the young hustler sells two, our protagonist calmly sets " Notice how ',
        (None, "目標"), ", target or goal, at ",
        (None, "六十本"), ", sixty tapes!"
    ]),
    (9, 'ちょっと待てよ。', [
        "'Hold on a second.'  Starting off with ",
        (None, "ちょっと待てよ"), " turns the verb to wait into 'hey, wait a minute!'"
    ]),
    (11, None, [
        "'Do you really have the resolve to step into this world?'  Focus on ",
        (None, "覚悟"), " this word means mental readiness to face consequences—'are you truly prepared for what comes next?'"
    ]),
]

TRANSITION = "Now let's listen to this sixty-thousand-yen triumph again."

OUTRO = (
    "Remember the expression for easily, the phrase for complimenting someone's good taste, "
    "the word for a goal, and the command to say hold on! "
    "One final scene concludes Episode One."
)
CLOSING = ('owner', 'また会いましょう。')
