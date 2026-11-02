# Authoring module for alrawabi-school-s01e01-scene-12.
ID = 'alrawabi-school-s01e01-scene-12'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "استراحة بالحمام  (A Breather in the Washroom)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"noaf": "نوف", "mariam": "مريم"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Shaken after the trouble in the courtyard, Mariam ducks into the school washroom and discovers Noaf is already inside. Startled at first, Mariam relaxes slightly when Noaf apologizes, tries to ease the tension, and promises to keep quiet. Listen to the whole scene in Jordanian Arabic first."
OPENER = "Let's walk through the washroom conversation line by line."
TRANSITION = "Now let's hear the whole washroom scene again."
OUTRO = "In that quiet moment by the washroom sinks, an unlikely trust starts forming between Mariam and Noaf. Listen out for \"alattif il-jaww\", a lovely phrase for lightening the mood. See you next time."
CLOSING = ("mariam", "أشوفك بعدين!")
STORY = [
    ('mariam', 'نوف، إنتي شو بتعملي هون؟', 'Noaf, what are you doing here?', [], 'Mariam startled in washroom'),
    ('noaf', 'ما حكيت إلك إني كنت بالحمام؟', 'Did I not tell you that I was in the washroom?', [(256, 'كنت في الحمام')], 'natural Jordanian adaptation of cue 256'),
    ('mariam', 'خوفتيني، فكرت ما في حدا هون.', 'You startled me, I thought nobody was here.', [], 'natural reaction'),
    ('noaf', 'طيب آسفة، ما كان قصدي أخوفك.', 'Alright sorry, I did not mean to scare you.', [(257, 'اسف')], 'feminine آسفة for Noaf'),
    ('noaf', 'كنت بس بحاول ألطف الجو شوي.', 'I was only trying to lighten the mood a little.', [(258, 'ألطف الجو')], 'natural Jordanian كنت بس بحاول'),
    ('mariam', 'اليوم كان صعب كتير علي.', 'Today was very hard on me.', [], 'Mariam opens up'),
    ('noaf', 'بعرف، شفت كيف البنات ضايقوكي.', 'I know, I saw how the girls bothered you.', [], 'Noaf shows empathy'),
    ('noaf', 'بتقدري تاخدي استراحة هون بهدوء.', 'You can take a break here in peace.', [(259, 'تاخدي')], 'replaced English loanword بريك with استراحة'),
    ('mariam', 'خايفة تحكي لحدا إني كنت ببكي.', 'I am afraid you will tell someone that I was crying.', [], 'vulnerability before cue 260'),
    ('noaf', 'والله ما رح أحكي لأي حدا.', 'I swear I will not tell anyone at all.', [(260, 'والله ما رح أحكي')], ''),
    ('noaf', 'بس اهدي وتصرفي بطبيعتك قدامهم.', 'Just calm down and act naturally in front of them.', [(260, 'تصرفت')], 'clean A1 adaptation of cue 260'),
    ('mariam', 'شكراً يا نوف، ارتحت هلأ شوي.', 'Thank you Noaf, I feel a little relieved now.', [], 'warm resolution'),
]
WALK = [
    (0, None, ["'Noaf, what are you doing here?' ", ('mariam', 'بتعملي'), ' asks one woman what she is doing right now, built from ', ('mariam', 'عمل'), ', doing or making.']),
    (1, None, ["'Did I not tell you that I was in the washroom?' Notice how Jordanian Arabic turns a statement into a yes-or-no question simply by lifting the voice at the end."]),
    (2, None, ["'You startled me, I thought nobody was here.' ", ('mariam', 'خوفتيني'), ' packs "you scared me" into one word, and ', ('mariam', 'فكرت'), ' means "I thought".']),
    (3, None, ["'Alright sorry, I did not mean to scare you.' Because Noaf is female, she says ", ('noaf', 'آسفة'), ' with a soft "-e" at the end rather than ', ('noaf', 'آسف'), '.']),
    (4, None, ["'I was only trying to lighten the mood a little.' Literally, ", ('noaf', 'ألطف الجو'), ' says "soften the weather", the exact everyday idiom for lightening a tense mood.']),
    (5, None, ["'Today was very hard on me.' ", ('mariam', 'صعب'), ' means "hard" or "difficult", and ', ('mariam', 'علي'), ' adds "on me" to show who carried the weight of the day.']),
    (6, None, ["'I know, I saw how the girls bothered you.' ", ('noaf', 'ضايقوكي'), ' comes from the root for tightness or narrowness—so bothering someone literally crowds their space.']),
    (7, None, ["'You can take a break here in peace.' ", ('noaf', 'استراحة'), ' comes from resting, and ', ('noaf', 'بهدوء'), ' means "quietly" or "in peace".']),
    (8, None, ["'I am afraid you will tell someone that I was crying.' Combining ", ('mariam', 'كنت'), ' with ', ('mariam', 'ببكي'), ' gives "I was crying", painting a scene still fresh in Mariam\'s mind.']),
    (9, None, ["'I swear I will not tell anyone at all.' ", ('noaf', 'لأي حدا'), ' strengthens "to anyone" into "to anyone whatsoever".']),
    (10, None, ["'Just calm down and act naturally in front of them.' ", ('noaf', 'بطبيعتك'), ' literally says "in your own nature", a warm way to say "just be yourself".']),
    (11, None, ["'Thank you Noaf, I feel a little relieved now.' ", ('mariam', 'ارتحت'), ' comes from the same comfort root as استراحة, so "I rested" naturally means "I feel relieved".']),
]
