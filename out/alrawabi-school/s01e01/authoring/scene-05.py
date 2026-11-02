# Authoring module for alrawabi-school-s01e01-scene-05.
ID = 'alrawabi-school-s01e01-scene-05'
SHOW = 'alrawabi-school'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = "مش كل إشي بتشوفه العين  (Not Everything the Eye Sees)"
LEVEL = "A1 — beginner"
PAIR = 'ar-en'
LABELS = {"mariam": "مريم", "layan": "ليان", "faten": "مس فاتن"}
SOURCE_NAME = 'مدرسة الروابي للبنات (AlRawabi School for Girls) S1.01'
SOURCE_FILE = 'sources/alrawabi-school/s01/e01.ar.srt'
INTRO = "Back inside Principal Ms. Faten's office at AlRawabi School, Layan plays completely innocent when questioned about a hurt classmate, trying to shift suspicion onto Mariam. Listen to the whole scene in Jordanian Arabic first."
OPENER = "Let's go back over those lines one at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ["Layan knows how to look blameless in front of authority, yet Mariam reminds us that appearances at AlRawabi can be deceiving. Listen out for ", ("layan", "ممكن"), " when asking politely or saying something might happen. See you next time."]
CLOSING = ("mariam", "أشوفك بكرة!")
STORY = [
    ('mariam', 'هاي مدرسة الروابي للبنات.', 'This is AlRawabi School for Girls.', [(38, 'هاي'), (39, 'مدرسة الروابي')], ''),
    ('mariam', 'وهاي ليان اللي ما حدا بيلعب معها.', 'And this is Layan, whom nobody messes with.', [(40, 'وهاي'), (41, 'يلعب معها')], 'simplified A1 phrasing'),
    ('mariam', 'وصحباتها دايماً بيدافعوا عنها.', 'And her friends always defend her.', [(42, 'صحباتها اللي بيدافعوا عنها')], ''),
    ('mariam', 'ويا ويل البنت اللي بتوقف بطريقها.', 'And woe to the girl who stands in her way.', [(43, 'البنات اللي بيوقفوا')], 'natural Jordanian idiom'),
    ('layan', 'ممكن أعرف أنا ليش هون يا مس؟', 'May I know why I am here, Miss?', [(45, 'ممكن أعرف أنا ليش هون')], ''),
    ('faten', 'إنتي عارفة منيح ليش ناديتك.', 'You know very well why I called you.', [], 'Ms. Faten pushes back'),
    ('faten', 'كيف ممكن حدا يأذي زميلته زي هيك؟', 'How could anyone hurt their classmate like that?', [(46, 'كيف ممكن'), (46, 'زي هيك')], 'natural Jordanian adaptation'),
    ('faten', 'أنا مش قادرة أستوعب اللي صار.', 'I cannot wrap my head around what happened.', [(46, 'أستوعب')], 'split cue 46 cleanly'),
    ('layan', 'اسألي البنت اللي لقتها بالصدفة.', 'Ask the girl who found her by coincidence.', [(47, 'البنت اللي'), (47, 'لقتها بالصدفة')], ''),
    ('layan', 'أنا ما عملت إلها أي إشي.', 'I did not do anything to her.', [], 'Layan denies blame'),
    ('mariam', 'بس مش كل إشي بتشوفه العين هو الحقيقة.', 'But not everything the eye sees is the truth.', [(48, 'بس مش كل إشي بتشوفه العين'), (49, 'هو الحقيقة')], ''),
    ('mariam', 'ومرات البنت القوية ممكن تخسر كل إشي.', 'And sometimes the strong girl can lose everything.', [(44, 'اللي ممكن تخسر كل')], 'adapted cue 44'),
]
WALK = [
    (0, None, ["'This is AlRawabi School for Girls.' In Jordanian speech, ", ("mariam", "هاي"), " means \"this\" for female words like ", ("mariam", "مدرسة"), ", \"school\"."]),
    (1, None, ["'And this is Layan, whom nobody messes with.' Literally ", ("mariam", "بيلعب معها"), " says \"plays with her\", which in Arabic also means messing with someone you shouldn't."]),
    (2, None, ["'And her friends always defend her.' ", ("mariam", "بيدافعوا عنها"), " pairs \"defend\" with ", ("mariam", "عنها"), ", literally \"from her\", as if shielding trouble away from her."]),
    (3, None, ["'And woe to the girl who stands in her way.' ", ("mariam", "ويا ويل"), " is a dramatic everyday warning, like \"watch out for\" or \"heaven help\"."]),
    (4, None, ["'May I know why I am here, Miss?' Starting a question with ", ("layan", "ممكن"), ", \"possible\", is the smoothest polite way to say \"may I\" or \"can I\"."]),
    (5, None, ["'You know very well why I called you.' Jordanians say ", ("faten", "منيح"), " for both \"good\" and \"well\"—it is one of the first local words visitors notice in Amman."]),
    (6, None, ["'How could anyone hurt their classmate like that?' ", ("faten", "زي هيك"), " glues \"like\" and \"this\" together into an everyday chunk for \"like that\"."]),
    (7, None, ["'I cannot wrap my head around what happened.' ", ("faten", "مش قادرة"), " means \"unable\" when a woman is speaking, and ", ("faten", "أستوعب"), " means taking an idea in completely."]),
    (8, None, ["'Ask the girl who found her by coincidence.' Layan says ", ("layan", "بالصدفة"), ", \"by chance\", dropping a sarcastic hint that Mariam was not there by accident."]),
    (9, None, ["'I did not do anything to her.' ", ("layan", "إلها"), " bundles \"to\" and \"her\" into one short word, and ", ("layan", "أي إشي"), " means \"anything at all\"."]),
    (10, None, ["'But not everything the eye sees is the truth.' Arabic puts ", ("mariam", "هو"), ", literally \"he\", between the two halves of the sentence to act like a bold \"is\"."]),
    (11, None, ["'And sometimes the strong girl can lose everything.' ", ("mariam", "مرات"), " literally means \"times\" and works on its own as \"sometimes\", while ", ("mariam", "تخسر"), " means \"lose\"."]),
]
