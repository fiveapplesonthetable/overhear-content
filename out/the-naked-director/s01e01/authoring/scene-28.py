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
    "Seeing Toshi's stack of unsold cassette tapes, Muranishi's salesman instincts suddenly wake up. "
    "He marches into a specialty shop, charms the owner into buying twenty tapes for sixty thousand yen cash, and proposes an ambitious partnership on the street outside. "
    "Listen to Muranishi work his magic."
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

OPENER = "Notice how Muranishi switches smoothly between silky customer flattery inside the shop and brisk business numbers outside."

WALK = [
    (1, None, "'They will not sell that easily.' \"Kantan ni\" means easily or simply, and \"urenai\" comes from \"ureru\", to sell well on the market—distinct from \"uru\", which is what the seller does."),
    (2, '買ってやるよ。', "'I will buy them from you.' Amused by Muranishi's pitch, the shopkeeper adds gruff \"te yaru\" onto \"kau\", to buy, doing the newcomer a favour."),
    (3, 'さすがオーナー様、お目が高い！', "'As expected of you, Owner, you have a keen eye!' Every salesperson in Japan knows \"sasuga\", 'true to your reputation!', and the classic flattery \"ome ga takai\"—literally 'your eyes are high', meaning refined taste!"),
    (4, None, "'They sold! At three thousand yen apiece, that is sixty thousand yen.' Long cylindrical or spooled items like tapes, bottles, and umbrellas count with \"hon\" (or \"ippon\" for one): \"ippon sanzen-en\" totals \"rokuman-en\", sixty thousand yen."),
    (5, None, "'Wait, were you a salesman?' \"Eigyouman\" blends Japanese \"eigyou\", sales, with English 'man'—the everyday word for a sales rep."),
    (6, None, "'Roughly how many of these sell per day?' Asking \"nanbon gurai\" combines \"nanbon\", how many tapes, with \"gurai\", approximately."),
    (7, None, "'Well, two a day at most.' \"Ookute\" comes from \"ooi\", many, and at the start of an estimate it means 'at the very most'."),
    (8, 'じゃあ他の店も行こう。', "'Then let us hit other shops too.' \"Hoka no mise\" means other shops, and \"ikou\" is the energetic 'let us go!' form of \"iku\"."),
    (8, '一日の目標は六十本だ。', "'Our daily target is sixty.' Where Toshi sells two, Muranishi calmly sets \"mokuhyou\", target or goal, at \"rokujuppon\", sixty tapes!"),
    (9, 'ちょっと待てよ。', "'Hold on a second.' \"Chotto mate yo\" turns \"matsu\", to wait, into 'hey, wait a minute!'"),
    (11, None, "'Do you really have the resolve to step into this world?' \"Kakugo\" means mental readiness to face consequences—'are you truly prepared for what comes next?'"),
]

TRANSITION = "Now let's listen to Muranishi's sixty-thousand-yen triumph again."

OUTRO = (
    "Remember \"kantan ni\" for easily, \"ome ga takai\" when complimenting someone's good taste, "
    "\"mokuhyou\" for a goal, and \"chotto mate\" to say hold on! "
    "One final scene concludes Episode One."
)

CLOSING = ('owner', 'また会いましょう。')
