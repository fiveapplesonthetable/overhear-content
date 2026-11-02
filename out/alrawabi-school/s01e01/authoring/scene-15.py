# Authoring module for alrawabi-school-s01e01-scene-15.
ID = 'alrawabi-school-s01e01-scene-15'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 15
TITLE = "خطتنا كلنا  (All of Our Plan)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "dina": "دينا", "noaf": "نوف"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Later in a quiet corner of the hallway, Mariam pulls Dina and Noaf together after a careless remark nearly gives them away. Tension flares when Mariam calls the payback scheme \"my plan\", until Noaf challenges her on the spot. Listen to the whole conversation in Jordanian Arabic first."
OPENER = "Now let's unpack each line of that tense huddle."
TRANSITION = "Let's hear the whole hallway huddle once more."
OUTRO = "That single word shift from \"my plan\" to \"all of our plan\" keeps the three girls united. Listen out for \"khuttitna\", where a tiny ending changes ownership in an instant. See you next time."
CLOSING = ("mariam", "إلى اللقاء!")
STORY = [
    ('mariam', 'ممكن تضبي لسانك جوا حلقك شوي؟', 'Could you keep your tongue inside your mouth a little?', [(288, 'جوا حلقك')], 'natural feminine Jordanian تضبي لسانك'),
    ('mariam', 'كنتي رح تفضحينا قدام البنات.', 'You were going to expose us in front of the girls.', [(289, 'كنت')], 'restored تفضحينا from Whisper split'),
    ('dina', 'والله ما حكيت إشي يا مريم.', 'I swear I did not say anything, Mariam.', [(290, 'ما حكيت اشي')], ''),
    ('dina', 'شو قصدك بهاد الحكي هلأ؟', 'What do you mean by this talk now?', [(291, 'شو قصدك')], ''),
    ('mariam', 'قصدي بالمرة مش وقته هاد الحكي.', 'I mean now is not the time for this talk at all.', [(292, 'قصدي بالمرة مش')], 'clear Jordanian هاد الحكي'),
    ('mariam', 'مش لازم نلفت نظرهم إلنا هالفترة.', 'We must not draw their attention to us right now.', [(293, 'مش لازم نلفت نظرهم إلنا')], ''),
    ('mariam', 'في إشي مهم لازم نخلصه أول.', 'There is something important we have to finish first.', [(294, 'نخلصه')], 'clean Jordanian phrasing'),
    ('noaf', 'والله جد يا مريم؟', 'Oh really, Mariam?', [(295, 'والله')], 'restored جد from Whisper جاد'),
    ('noaf', 'ما كنت عارفة إني لازم أستأذنك بكل إشي.', 'I did not know I had to ask your permission for everything.', [(296, 'ما كنت عارفة'), (296, 'أستأذنك')], 'shortened A1 sentence'),
    ('mariam', 'اه يا نوف، لما الإشي يدخل بخطتي.', 'Yes Noaf, when something affects my plan.', [(297, 'نوف'), (298, 'يدخل بخطتي')], 'combined cues 297-298'),
    ('mariam', 'وقتها بتيجي وبتستأذني مني قبل.', 'Then you come and ask my permission beforehand.', [(299, 'وقتها بتيجي بتستأذني مني')], ''),
    ('noaf', 'عفواً، خطتك إنتي لحالك؟', 'Excuse me, your plan all by yourself?', [(300, 'خطتك')], ''),
    ('mariam', 'قصدي خطتنا كلنا مع بعض.', 'I mean all of our plan together.', [(301, 'كلنا')], 'clean Jordanian phrasing'),
    ('dina', 'خلص ما عليكم، المهم نضل إيد واحدة.', 'Alright never mind, what matters is staying united.', [(302, 'ما عليك')], 'warm peace-making turn'),
]
WALK = [
    (0, None, "'Could you keep your tongue inside your mouth a little?' \"Tdubbi lsaanik juwwa halqik\" literally says \"pack your tongue inside your throat\", a colorful Jordanian way to say \"hold your tongue\"."),
    (1, None, "'You were going to expose us in front of the girls.' Combining \"kunti\" with \"rah\" means \"you were about to\", and \"tifdaheena\" means giving away our secret."),
    (2, None, "'I swear I did not say anything, Mariam.' \"Ma hakeit ishi\" is the everyday three-word defense \"I didn't say a thing\"."),
    (3, None, "'What do you mean by this talk now?' Putting \"bi-\" onto \"haad\" gives \"bi-haad\", \"by this\" or \"with this\"."),
    (4, None, "'I mean now is not the time for this talk at all.' With a negative word like \"mish\", \"bil-marra\" means \"not at all\" or \"not in the slightest\"."),
    (5, None, "'We must not draw their attention to us right now.' \"Nilfit nazarhom\" literally says \"turn their sight\", and \"hal-fatra\" means \"during this period\"."),
    (6, None, "'There is something important we have to finish first.' \"Fi\" all by itself means \"there is\" in Levantine Arabic, built from the tiny word for \"in\"."),
    (7, None, "'Oh really, Mariam?' Saying \"wallah jadd\" with raised eyebrows is pure Amman sarcasm for \"oh, seriously?\"."),
    (8, None, "'I did not know I had to ask your permission for everything.' \"Asta'zinik\" comes from \"izn\", permission, with \"you\" tucked right onto the end."),
    (9, None, "'Yes Noaf, when something affects my plan.' \"Ah\" is the casual everyday \"yes\", and \"khuttiti\" means \"my plan\"—the exact word that sets Noaf off."),
    (10, None, "'Then you come and ask my permission beforehand.' \"Bteeji\" means \"you come\", which Jordanians often pair right alongside the next action."),
    (11, None, "'Excuse me, your plan all by yourself?' Swapping \"-i\" for \"-ik\" turns \"my plan\" into \"khuttitik\", \"your plan\", throwing Mariam's word right back at her."),
    (12, None, "'I mean all of our plan together.' Now the ending changes to \"-na\" in \"khuttitna\"—\"our plan\"—and \"kulna\" reinforces \"all of us\"."),
    (13, None, "'Alright never mind, what matters is staying united.' Literally \"eed waahde\" says \"one hand\", a warm Arabic idiom for standing united."),
]
