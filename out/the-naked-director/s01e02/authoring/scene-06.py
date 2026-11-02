ID = 'the-naked-director-s01e02-scene-06'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = '森刑事の検査  (Mori\'s Inspection)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kitamori': '北森', 'mori': '森', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E02'
SOURCE_FILE = 'sources/the-naked-director/s01/e02.ja.srt'

INTRO = (
    "Opening branches right beside police stations soon brings Detective Mori of the Hokkaido Police through the door. "
    "While Mori inspects the stock for rule violations, Muranishi answers every complaint with unshakable politeness. "
    "Listen to the Japanese confrontation first without worrying about catching every word."
)

STORY = [
    ('kitamori', 'どうされました？', 'How may I help you?', [(101, 'どうされました')], ''),
    ('mori', '道警の森だ。責任者はいるか？', 'I am Mori from the Hokkaido Police. Is the person in charge here?', [(102, '責任者いるか')], 'Added particle は.'),
    ('kitamori', '会長、警察の方が来ました。', 'Chairman, someone from the police has arrived.', [(106, '会長 警察の方が')], 'Completed trailing が with 来ました.'),
    ('muranishi', 'どうしましたか？', 'What seems to be the matter?', [(109, 'どうしましたか')], ''),
    ('mori', '警察の近くにばかり出しやがって。', 'Opening shops right near the police stations, of all places.', [(110, '警察の近くにばかり 出しやがって')], ''),
    ('muranishi', '一番近いところに出店したまでです。', 'We simply opened at the closest spot.', [(114, '一番近いところに出店したまで')], 'Added polite です.'),
    ('mori', 'この部分をよく見ろ。', 'Look closely at this part.', [(125, 'この部分をよく見ろ')], ''),
    ('muranishi', 'ちゃんと規定をクリアしてますね。', 'It clearly passes the regulations, does it not?', [(126, 'ちゃんと'), (123, '規定をクリアしてます')], 'Combined clean compliance phrasing from cues 123 & 126.'),
    ('mori', '違う！よく見ろ。', 'Wrong! Look closely.', [(127, '違う')], 'Normalized elongated よーく to よく.'),
    ('mori', '今日のところは勘弁してやる。', 'I will let it slide for today.', [(141, '勘弁してやる')], 'Expanded とこ to ところ.'),
    ('mori', 'お前らの顔は覚えたからな。', 'I have memorized your faces, understand?', [(146, 'お前らの顔は覚えたからな')], ''),
    ('muranishi', 'どうぞお持ち帰りください。', 'Please feel free to take these home with you.', [(147, 'どうぞお持ち帰りください')], ''),
]

OPENER = "Listen to the sharp contrast in register: Mori barks blunt commands while Muranishi treats him like an honored guest. Let's break down their lines."

WALK = [
    (0, None, "'How may I help you?' \"Dou saremashita\" is a respectful upgrade of \"dou shimashita\", asking a customer or visitor what happened or what they need."),
    (1, '道警の森だ。', "'I am Mori from the Hokkaido Police.' \"Doukei\" squeezes \"Hokkaidou Keisatsu\", Hokkaido Police, into a snappy two-part abbreviation."),
    (1, '責任者はいるか？', "'Is the person in charge here?' \"Sekininsha\" joins \"sekinin\", responsibility, with \"sha\", person—the manager or person accountable."),
    (2, None, "'Chairman, someone from the police has arrived.' Rather than saying \"hito\", person, Kitamori chooses respectful \"kata\" in \"keisatsu no kata\" to announce the officers politely."),
    (4, None, "'Opening shops right near the police stations, of all places.' \"Bakari\" means 'nothing but' or 'only', complaining that every branch pops up right next to \"keisatsu\", the police."),
    (5, None, "'We simply opened at the closest spot.' \"Ichiban chikai\" means closest of all, and ending with \"made desu\" shrugs it off modestly as 'we merely did that and nothing more'."),
    (6, None, "'Look closely at this part.' \"Bubun\" means section or part, and \"miro\" is the blunt command form of \"miru\", to look—used by tough bosses or detectives, never with strangers in polite company."),
    (8, '違う！', "'Wrong!' By itself, \"chigau\"—from the verb 'to differ'—is the everyday Japanese way to say 'no, that's wrong!' or 'not like that!'."),
    (9, None, "'I will let it slide for today.' \"Kyou no tokoro wa\" frames 'as far as today goes', and \"kanben shite yaru\" grants pardon from above with tough-guy \"te yaru\"."),
    (10, None, "'I have memorized your faces, understand?' \"Omaera\" is a rough plural 'you lot', while \"kao\", face, plus \"oboeta\", remembered, delivers a classic parting warning."),
    (11, None, "'Please feel free to take these home with you.' Wrapping \"mochikaeri\", takeout or carrying home, between \"o\" and \"kudasai\" sounds like a polite pastry shop—which makes Muranishi's parting shot hilarious."),
]

TRANSITION = "Now let's hear the whole inspection scene again."

OUTRO = (
    "Notice how \"douzo omochikaeri kudasai\" is actually a helpful everyday expression you will see at bakeries and restaurants for takeout, repurposed here with sly humor. "
    "See you next time."
)

CLOSING = ('muranishi', 'また明日。')
