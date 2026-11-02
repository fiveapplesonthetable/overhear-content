# Authoring module for alrawabi-school-s01e01-scene-10.
ID = 'alrawabi-school-s01e01-scene-10'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 10
TITLE = "والله ما كان قصدي  (I Swear I Did Not Mean To)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "layan": "ليان", "faten": "مس فاتن"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "After a heated clash in the schoolyard leaves Layan hurt, Mariam stands trembling before Principal Ms. Faten to explain her side of the story. Mariam insists she only tried to push Layan off her, while Layan furiously accuses Mariam of attacking her. Hear the whole scene in Jordanian Arabic first."
OPENER = "Now let's go through each line of the confrontation."
TRANSITION = "Let's listen to the whole confrontation again from start to finish."
OUTRO = ["Mariam pleads from the heart, yet Layan's sharp accusation turns the room against her once more. Notice how ", ("mariam", "والله"), " adds urgency both to Mariam's plea and to Layan's counterattack. See you next time."]
CLOSING = ("faten", "مع السلامة!")
STORY = [
    ('faten', 'احكيلي بالضبط شو عملتي بالساحة يا مريم؟', 'Tell me exactly what you did in the courtyard, Mariam?', [(242, 'فعلت'), (231, 'الساحة')], 'natural Jordanian adaptation of formal Whisper cues'),
    ('mariam', 'ما عرفت شو أعمل وقتها يا مس.', 'I did not know what to do at the time, Miss.', [(228, 'أعرف')], 'natural Jordanian rendering of cue 228'),
    ('mariam', 'ضليت ساكتة لإني كنت كتير خايفة.', 'I stayed quiet because I was very scared.', [(229, 'ساكتة'), (229, 'خائفة')], 'natural Jordanian rendering of cue 229'),
    ('mariam', 'لما نزلت عالساحة تصرفت بشكل طبيعي.', 'When I went down to the courtyard, I acted in a normal way.', [(231, 'الساحة'), (232, 'طبيعي')], 'natural Jordanian rendering'),
    ('mariam', 'فجأة ليان إجت ومسكتني من ورا.', 'Suddenly Layan came and grabbed me from behind.', [(233, 'ومسكتني')], 'Jordanian من ورا for من خلفه'),
    ('mariam', 'أنا بس كنت بدي أبعدها عني.', 'I only wanted to push her away from me.', [(234, 'أبعدها عني')], 'natural Jordanian كنت بدي'),
    ('mariam', 'والله ما كان قصدي أأذيها.', 'I swear it was not my intention to hurt her.', [(235, 'والله'), (235, 'قصدي')], 'Jordanian ما كان قصدي'),
    ('mariam', 'لازم تصدقوني يا مس فاتن.', 'You have to believe me, Ms. Faten.', [(237, 'تصدقوني')], ''),
    ('layan', 'والله كذابة يا مس!', 'I swear she is a liar, Miss!', [(238, 'والله كذابة')], ''),
    ('layan', 'هي اللي بلشت وضربتني قدام الكل.', 'She is the one who started it and hit me in front of everyone.', [(239, 'ضربتني')], 'natural Jordanian هي اللي'),
    ('faten', 'اهدوا هلأ، بدي أفهم القصة كلها.', 'Calm down now, I want to understand the whole story.', [], 'Ms. Faten steps in'),
    ('mariam', 'أنا حكيت كل اللي صار معي.', 'I told everything that happened with me.', [], 'quiet closing line'),
]
WALK = [
    (0, None, ["'Tell me exactly what you did in the courtyard, Mariam?' ", ("faten", "بالضبط"), " means \"exactly\" or \"precisely\", and ", ("faten", "احكيلي"), " tacks \"to me\" straight onto \"tell\"."]),
    (1, None, ["'I did not know what to do at the time, Miss.' ", ("mariam", "وقتها"), " glues \"time\" and \"her\" together to mean \"at that moment\" or \"back then\"."]),
    (2, None, ["'I stayed quiet because I was very scared.' ", ("mariam", "ضليت ساكتة"), " means \"I kept silent\", and ", ("mariam", "خايفة"), " is how a woman says she feels afraid."]),
    (3, None, ["'When I went down to the courtyard, I acted in a normal way.' ", ("mariam", "طبيعي"), " comes from \"nature\", so ", ("mariam", "بشكل طبيعي"), " literally says \"in a natural shape\"."]),
    (4, None, ["'Suddenly Layan came and grabbed me from behind.' ", ("mariam", "فجأة"), " means \"all of a sudden\", while ", ("mariam", "ومسكتني"), " packs \"and she grabbed me\" into a single word."]),
    (5, None, ["'I only wanted to push her away from me.' Notice ", ("mariam", "كنت بدي"), "—combining \"I was\" with \"I want\" is the smooth everyday way Jordanians say \"I wanted\"."]),
    (6, None, ["'I swear it was not my intention to hurt her.' ", ("mariam", "والله"), " literally swears \"by God\", and ", ("mariam", "ما كان قصدي"), " is the classic heartfelt apology \"I didn't mean to\"."]),
    (7, None, ["'You have to believe me, Ms. Faten.' Even though she addresses Ms. Faten, Mariam says ", ("mariam", "تصدقوني"), "—\"believe me, all of you\"—pleading with the whole room."]),
    (8, None, ["'I swear she is a liar, Miss!' ", ("layan", "كذابة"), " is the strong word for a female liar, stretching the middle sound for extra punch."]),
    (9, None, ["'She is the one who started it and hit me in front of everyone.' ", ("layan", "بلشت"), " is the everyday Levantine word for \"she started\", and ", ("layan", "وضربتني"), " means \"and she hit me\"."]),
    (10, None, ["'Calm down now, I want to understand the whole story.' ", ("faten", "اهدوا"), " tells more than one person to calm down, built from the root for quietness."]),
    (11, None, ["'I told everything that happened with me.' Saying ", ("mariam", "صار معي"), ", literally \"happened with me\", is how Jordanians talk about what they personally went through."]),
]
