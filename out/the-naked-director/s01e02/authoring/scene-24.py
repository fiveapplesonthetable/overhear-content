ID = 'the-naked-director-s01e02-scene-24'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 24
TITLE = '誕生日プレゼントと警察  (Birthday Gift and Police at the Door)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'daisuke': '大輔', 'mayumi': '真由美', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Toru Muranishi comes home at last to surprise his young son Daisuke and wife Mayumi with a birthday gift. "
    "Their warm family reunion lasts only moments before Takei's investigators ring the front doorbell. "
    "Listen to the classic Japanese homecoming greetings first."
)

STORY = [
    ('muranishi', 'ただいま！', 'I am home!', [(662, 'ただいま')], ''),
    ('daisuke', 'おかえり、パパ！', 'Welcome home, Dad!', [(663, 'おかえり'), (663, 'パパ')], ''),
    ('muranishi', '元気にしてたか？会いたかったぞ。', 'Have you been well? I missed you.', [(665, '元気にしてたか'), (665, '会いたかったぞ')], 'Trimmed middle vocative.'),
    ('mayumi', '元気だよ。パパ、久しぶりだね。', 'We have been well. It has been a long time, Dad.', [(666, '元気だよ'), (666, '久しぶりだね')], ''),
    ('daisuke', 'おばあちゃん、パパが帰ってきたよ。', 'Grandma, Dad came home!', [(668, 'おばあちゃん'), (668, '帰ってきたよ')], 'Added subject marker が.'),
    ('muranishi', 'ほら、誕生日プレゼントだ。', 'Look, it is a birthday present.', [(675, '誕生日プレゼントだ')], ''),
    ('daisuke', 'やった！', 'Yay!', [(675, 'やった')], ''),
    ('daisuke', '廊下で遊んできていい？', 'Can I go play in the hallway?', [(679, '廊下で遊んできていい')], ''),
    ('muranishi', 'いいよ。', 'Sure.', [(679, 'いいよ')], ''),
    ('mayumi', 'これからもたまに会ってくれる？', 'Will you still come see us once in a while from now on?', [(681, 'これからも'), (681, 'たまに会ってくれる')], ''),
    ('muranishi', 'ああ、もちろんだ、真由美。', 'Yeah, of course, Mayumi.', [(682, 'もちろんだ'), (682, '真由美')], ''),
    ('mayumi', '新しい仕事、どう？', 'How is your new job?', [(683, '新しい仕事'), (683, 'どう')], ''),
    ('muranishi', '中に入っとけ！', 'Stay inside!', [(695, '入っとけ')], 'Added direction marker に.'),
]

OPENER = "Few scenes pack in so many everyday family essentials—from stepping through the front door to asking permission to play. Let's hear them up close."

WALK = [
    (0, None, "'I am home!' Stepping into the entryway, everyone in Japan calls out \"tadaima\"—short for 'just now, I have returned'. You say it to family, roommates, or even an empty house."),
    (1, None, "'Welcome home, Dad!' Whoever is already inside answers \"tadaima\" with \"okaeri\", short for \"okaerinasai\", welcome back. Young children often call their father \"papa\" at home."),
    (2, None, "'Have you been well? I missed you.' \"Genki ni shiteta ka\" checks warmly on someone's health since you last met. \"Aitakatta\" puts \"aitai\", want to see you, into the past—literally 'I wanted to see you', how Japanese says 'I missed you'."),
    (3, 'パパ、久しぶりだね。', "'It has been a long time, Dad.' \"Hisashiburi\" is the warm, all-purpose greeting when reuniting after a long gap. Soft \"da ne\" invites Muranishi to share that feeling."),
    (4, None, "'Grandma, Dad came home!' \"Obaachan\" means grandmother, and \"kaette kita\" chains \"kaeru\", return, with \"kita\", came, so you feel him arriving right here where Daisuke stands."),
    (5, None, "'Look, it is a birthday present.' The quick call \"hora\" says 'look here!' as you hand something over. \"Tanjoubi\", birthday, pairs right up with borrowed English \"purezento\"."),
    (6, None, "'Yay!' Literally \"yatta\" is the past form of \"yaru\", to do—'I did it!'. Kids and adults alike shout \"yatta\" whenever something awesome happens."),
    (7, None, "'Can I go play in the hallway?' \"Rouka\" is a corridor or hallway, marked by \"de\" as the spot for action. Ending an action in \"te ii\" with a rising tone—here \"asonde kite ii?\"—is the everyday way to ask 'can I?'."),
    (9, None, "'Will you still come see us once in a while from now on?' \"Kore kara mo\" means 'from now on too', and \"tama ni\" means 'once in a while'. Attaching \"kureru\" onto \"atte\", meeting, asks whether he will do that kindness for them."),
    (10, None, "'Yeah, of course, Mayumi.' Low, warm \"aa\" is a masculine 'yeah', and \"mochiron\" is the go-to word for 'of course'."),
    (11, None, "'How is your new job?' \"Atarashii shigoto\" pairs \"atarashii\", new, with \"shigoto\", job or work, then drops particles altogether before \"dou\", 'how is it?'—pure relaxed conversation."),
    (12, None, "'Stay inside!' Sensing police at the door, Muranishi barks \"naka ni haittoke\", contracting \"haitte oke\"—get inside and stay put."),
]

TRANSITION = "Now let's listen to the whole homecoming and cliffhanger ending again."

OUTRO = (
    "Homecoming pair \"tadaima\" and \"okaeri\", reunion favorite \"hisashiburi\", and \"aitakatta\" for 'I missed you' "
    "are four of the warmest everyday expressions in Japanese—even as Episode Two ends on a cliffhanger. "
    "Until next episode, see you tomorrow."
)

CLOSING = ('muranishi', 'また明日。')
