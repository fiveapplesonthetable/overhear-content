ID = "al-maktab-s01e01-scene-01"
SHOW, SEASON, EPISODE, SCENE = "al-maktab", 1, 1, 1
PAIR = "ar-en"
FORMAT = "taster"
TITLE = "اسمه راتب  (Taster: it's called a salary)"
LEVEL = "A1 — Duolingo Section 2"
LABELS = {"malik": "مالك", "colleague": "زميلة"}
SOURCE_NAME = "Al Maktab (Saudi, 2022), S1E1: four selected lines from the official MBC Shahid clip"
SOURCE_FILE = "sources/al-maktab/s01/e01.ar.srt"
SOURCE_NOTE = "Reviewed partial native transcript, not a full episode. Both independent unprompted large-v3 and large-v3-turbo source decodes agree on these words. Original media stays private; final native audio is synthesized and requires independent QA."
INTRO = "This is a short Arabic taster from Al Maktab, the Saudi office comedy set in a courier company. Malik, the manager, talks about his staff needing monthly money, and a colleague corrects his choice of word. Listen to four short lines in everyday Saudi Arabic first; you can follow the meaning afterwards."
STORY = [
    ("malik", "يعني قصدي.", "I mean.", [(1, "يعني قصدي")], "Punctuation added. A natural self-correction; the literal wording is closer to 'I mean, my intention'."),
    ("malik", "يحتاجون مصروف شهري.", "They need a monthly allowance.", [(2, "يحتاجون مصروف شهري")], "Verbatim words; a continuation of the previous line, separated for the learner."),
    ("colleague", "اسمه راتب.", "It's called a salary.", [(3, "اسمه راتب")], "The colleague's actual reply. Her specific character name is unverified; no invented name or male recasting."),
    ("malik", "أنا مسؤول عن كل الناس اللي برا.", "I'm responsible for all the people outside.", [(4, "أنا مسؤول عن كل الناس اللي برا")], "The preceding filler expression and later disputed continuation are not retained. Outside means beyond the meeting room, not necessarily outdoors."),
]
OPENER = "Let's take those lines one at a time."
WALK = [
    (0, None, "'I mean.' He is correcting himself. The second word literally means 'my intention', with a possessive ending that makes it his own intention. Here the whole phrase simply introduces what he meant to say."),
    (1, None, "'They need a monthly allowance.' The ending tells us that several people need something. The word meaning 'monthly' comes after the allowance it describes. It is built from the word for 'month'."),
    (2, None, "'It's called a salary.' Literally, 'its name is a salary'. The word for 'name' has a little ending that points back to the allowance. Her correction is pointed: these are employees' wages, rather than pocket money."),
    (3, None, "'I'm responsible for all the people outside.' Arabic places the first-person pronoun directly before the adjective meaning 'responsible'. This present statement needs no separate helping verb. The short linking word introduces a description of those people. Here, 'outside' means beyond the meeting room."),
]
TRANSITION = "Now listen to the same exchange again."
OUTRO = "You heard the difference between an allowance and a salary, and a way to say who you are responsible for. We'll leave Malik with his colleague's useful correction. See you next time."
CLOSING = ("colleague", "اسمه راتب.")
