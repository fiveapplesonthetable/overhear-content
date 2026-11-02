# Authoring module for alrawabi-school-s01e01-scene-08.
ID = 'alrawabi-school-s01e01-scene-08'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = "أول وآخر مرة  (First and Last Time)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "dina": "دينا", "abeer": "مس عبير"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Out in the courtyard of AlRawabi School between classes, Mariam and Dina talk quietly about how Layan never goes anywhere without her loyal inner circle. Before they finish, strict floor supervisor Ms. Abeer catches them lingering outside. Listen to the whole exchange in Jordanian Arabic first."
OPENER = "Let's go back through the courtyard lines one by one."
TRANSITION = "Now let's hear the whole courtyard scene again from start to finish."
OUTRO = "Ms. Abeer sends the girls hurrying back to class, though Dina's warning about Layan's inseparable group lingers. Keep an ear out for \"awwal\" and \"aakhir\" paired together in strict warnings. See you next time."
CLOSING = ("dina", "مع السلامة!")
STORY = [
    ('mariam', 'ما في مكان تاني زي هاد المكان.', 'There is no other place like this place.', [(216, 'هذا المكان'), (217, 'زي هذا المكان')], 'natural Jordanian هاد'),
    ('dina', 'لازم الوحدة تشوفه بعينها قبل ما تحكم.', 'A girl has to see it with her own eyes before judging.', [(218, 'لازم تيجي'), (218, 'بتحكمي')], 'adapted cue 218'),
    ('mariam', 'اطلعي هناك عند باب الساحة.', 'Look over there by the courtyard gate.', [], 'sets up spotting Layan and Ms. Abeer'),
    ('dina', 'ليان واقفة مع رانيا ورقية كالعادة.', 'Layan is standing with Rania and Roqayya as usual.', [], 'names Layan clique'),
    ('mariam', 'البنات دايماً ماشيين وراها بالمدرسة.', 'The girls are always walking behind her at school.', [(223, 'تستبع')], 'natural Jordanian adaptation of cue 223'),
    ('dina', 'وهي ما بتتحرك خطوة بدونهم.', 'And she does not move a step without them.', [(224, 'وما بتتحرك بدونهم')], ''),
    ('abeer', 'شو بتعملوا هون بنص الساحة؟', 'What are you doing here in the middle of the courtyard?', [], 'Ms. Abeer arrives'),
    ('mariam', 'كنا رايحين عالصف هلأ يا مس عبير.', 'We were heading to class right now, Ms. Abeer.', [], 'polite excuse'),
    ('abeer', 'هاي أول وآخر مرة بشوفكم متأخرين.', 'This is the first and last time I see you late.', [(220, 'هاي أول وآخر مرة')], ''),
    ('dina', 'أكيد يا مس، حقك علينا.', 'Of course Miss, our apologies.', [(219, 'أكيد')], 'restored مس from Whisper نس'),
    ('abeer', 'يلا، ارجعوا عالصف بسرعة.', 'Come on, go back to class quickly.', [(221, 'صفك')], 'natural plural command'),
    ('dina', 'أحسن إلنا نروح قبل ما تعصب.', 'It is better for us to go before she gets angry.', [(222, 'أحسن لك')], 'clean Jordanian adaptation'),
]
WALK = [
    (0, None, "'There is no other place like this place.' \"Ma fi\" is the everyday Levantine way to say \"there is not\", and \"taani\" means \"other\" or \"second\"."),
    (1, None, "'A girl has to see it with her own eyes before judging.' Literally \"bi-einha\" says \"with her single eye\", which is how Arabic expresses \"with her own eyes\"."),
    (2, None, "'Look over there by the courtyard gate.' \"Ittallai\" tells one girl to look, while \"hunaak\" points \"over there\"."),
    (3, None, "'Layan is standing with Rania and Roqayya as usual.' \"Waaqfe\" describes a woman standing right now, and \"kal-aade\" neatly packs \"like the habit\" into one word for \"as usual\"."),
    (4, None, "'The girls are always walking behind her at school.' \"Waraaha\" glues \"behind\" and \"her\" together, showing how Layan's clique trails her everywhere."),
    (5, None, "'And she does not move a step without them.' \"bidoonhom\" combines \"without\" and \"them\"—swap in \"bidooni\" for \"without me\" or \"bidoonak\" for \"without you\"."),
    (6, None, "'What are you doing here in the middle of the courtyard?' \"Bi-nuss\" literally means \"in half of\", which Jordanians use every day for \"in the middle of\"."),
    (7, None, "'We were heading to class right now, Ms. Abeer.' Saying \"kunna raayheen\" pairs \"we were\" with \"going\", a handy way to explain what you were just about to do."),
    (8, None, "'This is the first and last time I see you late.' Pairing \"awwal\" for \"first\" with \"aakhir\" for \"last\" gives teachers everywhere that classic final warning."),
    (9, None, "'Of course Miss, our apologies.' \"Haqqik alayna\" literally says \"your right is upon us\", a warm, respectful Jordanian way to say \"my bad\" or \"our apologies\"."),
    (10, None, "'Come on, go back to class quickly.' \"Irjaau\" tells a group to go back, and \"bi-suraa\" adds \"with speed\" for \"quickly\"."),
    (11, None, "'It is better for us to go before she gets angry.' Starting with \"ahsan ilna\" means \"better for us\", and \"taassib\" is the everyday Levantine word for losing your temper."),
]
