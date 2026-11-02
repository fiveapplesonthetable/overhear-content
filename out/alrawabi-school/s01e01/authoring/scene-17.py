# Authoring module for alrawabi-school-s01e01-scene-17.
ID = 'alrawabi-school-s01e01-scene-17'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 17
TITLE = "إنتي كنتي هناك  (You Were There)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "noaf": "نوف", "layan": "ليان"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "In the episode's decisive moment at AlRawabi School, Mariam turns directly to Noaf—the one student outside Layan's clique who actually saw what happened—and begs her to tell the truth while Layan denies everything. Listen to the whole scene in Jordanian Arabic first."
OPENER = "Let's go back through the final scene of the episode line by line."
TRANSITION = "Now let's listen to the whole final scene one last time."
OUTRO = "That confrontation seals Episode 1 of AlRawabi School for Girls: when Layan's lies hold sway, Mariam realizes only her own plan with Noaf and Dina will bring the truth out. Thank you for listening, and see you next time."
CLOSING = ("mariam", "أشوفك قريب!")
STORY = [
    ('mariam', 'الواحد بيقدر يتحمل الظلم لمرحلة معينة.', 'A person can endure unfairness up to a certain point.', [(375, 'الواحد بيقدر'), (377, 'لمرحلة معينة')], 'tightened from merged montage cues'),
    ('noaf', 'وبعدين الواحد بيفقع وما بيسكت.', 'And after that a person bursts and does not stay quiet.', [(378, 'بعدين بيفقع')], ''),
    ('mariam', 'نوف، إنتي شفتي شو صار بالساحة.', 'Noaf, you saw what happened in the courtyard.', [], 'Mariam appeals to Noaf'),
    ('mariam', 'إنتي كنتي هناك، احكي إلهم الحقيقة.', 'You were there, tell them the truth.', [(398, 'كنتي هناك احكي لهم')], 'clear Jordanian احكي إلهم'),
    ('mariam', 'ليان إجت لعندي ومسكتني بالقوة.', 'Layan came up to me and grabbed me by force.', [(401, 'ومسكتني')], 'restored لعندي from Whisper لعيني'),
    ('layan', 'لا تصدقوها، مريم عم بتكذب!', 'Do not believe her, Mariam is lying!', [(402, 'عم')], 'restored عم بتكذب from Whisper عم بتكسب'),
    ('layan', 'ما حدا هون بيلعب معي بالمدرسة.', 'Nobody here messes with me at school.', [(383, 'ما حدا'), (383, 'يلعب')], 'from cue 383'),
    ('noaf', 'أنا شفت كل إشي بعيني يا ليان.', 'I saw everything with my own eyes, Layan.', [], 'Noaf backs Mariam'),
    ('layan', 'إنتي بنت جديدة وما بتعرفي إشي.', 'You are a new girl and you do not know anything.', [], 'Layan dismisses Noaf'),
    ('noaf', 'بعرف منيح مين عم بيحكي الصدق.', 'I know very well who is telling the truth.', [], 'Noaf stands firm'),
    ('mariam', 'مش كل إشي بتشوفه العين هو الحقيقة.', 'Not everything the eye sees is the truth.', [(390, 'بس مش كل إشي بتشوفه العين'), (391, 'هو الحقيقة')], ''),
    ('mariam', 'وإحنا ما رح نسكت بعد اليوم.', 'And we are not going to stay quiet after today.', [(413, 'بس مش بعد اليوم')], 'merged closing cue 413'),
]
WALK = [
    (0, None, ["'A person can endure unfairness up to a certain point.' The word ", ('mariam', 'الظلم'), ' means "unfairness" or "injustice", built from a root linked to darkness.']),
    (1, None, ["'And after that a person bursts and does not stay quiet.' Jordanians love the vivid word ", ('noaf', 'بيفقع'), '—literally "pops" or "bursts"—when someone finally loses patience.']),
    (2, None, ["'Noaf, you saw what happened in the courtyard.' The ending on ", ('mariam', 'شفتي'), ' means "you saw" when speaking to a woman.']),
    (3, None, ["'You were there, tell them the truth.' ", ('mariam', 'احكي'), ' means "tell", and ', ('mariam', 'إلهم'), ' adds "to them", urging Noaf to speak up in front of everyone.']),
    (4, None, ["'Layan came up to me and grabbed me by force.' The everyday word ", ('mariam', 'لعندي'), ' glues "to" and "by me" together to mean "right up to me".']),
    (5, None, ["'Do not believe her, Mariam is lying!' ", ('layan', 'لا تصدقوها'), ' is a command form telling the group "don\'t believe her", with "her" tucked onto the end.']),
    (6, None, ["'Nobody here messes with me at school.' Swapping معها for ", ('layan', 'معي'), ' changes "with her" into "with me".']),
    (7, None, ["'I saw everything with my own eyes, Layan.' Literally ", ('noaf', 'بعيني'), ' says "with my eye", giving personal eyewitness weight to Noaf\'s words.']),
    (8, None, ["'You are a new girl and you do not know anything.' ", ('layan', 'بنت جديدة'), ' puts the word for "girl" before "new", matching the soft "-e" ending on both words.']),
    (9, None, ["'I know very well who is telling the truth.' Saying ", ('noaf', 'عم بيحكي'), ' means "is speaking right now", spotlighting who is telling the truth in this moment.']),
    (10, None, ["'Not everything the eye sees is the truth.' The Arabic word ", ('mariam', 'العين'), ' can mean both a physical eye and a fresh water spring.']),
    (11, None, ["'And we are not going to stay quiet after today.' Here ", ('mariam', 'نسكت'), ' means "we stay quiet", closing the episode on steady resolve.']),
]
