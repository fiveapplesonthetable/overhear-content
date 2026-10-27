"""Scene 35 — The Candidate's Fight (s01e11, 01:05:34–01:07:47)."""

ID = "domashniy-arest-s01e11-scene-35"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 35
TITLE = "Драка кандидата  (The Candidate's Fight)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "samson": "anja",
    "misha": "angelina",
}

LABELS = {
    "anya": "Нина",
    "samson": "Самсон",
    "misha": "Миша",
}

INTRO = (
    "Outside on the street, Ivan Samsonov gets into a heated physical fight. His distressed wife Nina "
    "rushes out to pull him away, escorting him back into the apartment where their curious son Misha "
    "asks what happened. Let's listen to the family argument in Russian first; don't worry if you don't "
    "catch every word right away."
)

STORY = [
    ("anya", "Ваня, ты в полном порядке?",
     "Vanya, are you completely alright?",
     [(1087, "ты в порядке?")], ""),
    ("samson", "Да, всё нормально, не волнуйся.",
     "Yes, everything is fine, don't worry.",
     [(1089, "в порядке?")], ""),
    ("anya", "Прекратите эту драку прямо сейчас!",
     "Stop this fight right now!",
     [(1091, "он же бьет")], ""),
    ("anya", "Пойдём скорее домой, пожалуйста.",
     "Let's go home quickly, please.",
     [(1094, "Пойдем"), (1101, "Пожалуйста, пойдем!")], ""),
    ("samson", "Хорошо, успокойся, пойдём скорее.",
     "Fine, calm down, let's go quickly.",
     [(1103, "Все, тихо, успокойся")], ""),
    ("misha", "Мама, что там на улице случилось?",
     "Mom, what happened out there on the street?",
     [(1115, "Мам, что случилось-то?")], ""),
    ("anya", "Твой папа снова сильно подрался.",
     "Your dad had a big fight again.",
     [(1116, "Папа с дядей Даней подрался")], ""),
    ("misha", "Папа, тебя кто-то побил?",
     "Dad, did someone beat you up?",
     [(1117, "тебя дядя Даня побил?")], ""),
    ("samson", "Никто меня не побил, сынок.",
     "Nobody beat me up, son.",
     [(1117, "дядя Даня побил")], ""),
    ("samson", "Я просто защищал нашу честь.",
     "I was simply defending our honor.",
     [(1119, "драться нельзя")], ""),
    ("anya", "Ваня, тебе нельзя драться на улице!",
     "Vanya, you must not fight on the street!",
     [(1119, "драться нельзя")], ""),
    ("anya", "Ты ведь будущий мэр города!",
     "You are the future mayor of the city after all!",
     [(1120, "Я же кандидат")], ""),
    ("samson", "Ты права, я же кандидат!",
     "You are right, I am a candidate after all!",
     [(1120, "Я же кандидат")], ""),
    ("anya", "Тогда веди себя спокойно, Ваня.",
     "Then behave calmly, Vanya.",
     [(1119, "Миша, драться нельзя")], ""),
]

OPENER = "Now let's walk through the street brawl aftermath line by line."

WALK = [
    (0, None,
     "'Vanya, are you completely alright?' Nina asks her husband anxiously after the physical confrontation."),
    (1, None,
     "'Yes, everything is fine, don't worry.' Samsonov attempts to downplay his bruises with a reassurance."),
    (2, None,
     "'Stop this fight right now!' Nina demands an end to the brawl using an imperative phrase."),
    (3, None,
     "'Let's go home quickly, please.' Nina urges her husband to leave the street before spectators gather."),
    (4, None,
     "'Fine, calm down, let's go quickly.' Samsonov relents and agrees to walk back inside."),
    (5, None,
     "'Mom, what happened out there on the street?' Young Misha asks about the commotion outside."),
    (6, None,
     "'Your dad had a big fight again.' Nina explains the fight to her son with a reflexive past verb."),
    (7, None,
     "'Dad, did someone beat you up?' Misha questions his father with genuine childlike concern."),
    (8, None,
     "'Nobody beat me up, son.' Samsonov defends his pride with a negative pronoun construction."),
    (9, None,
     "'I was simply defending our honor.' Samsonov justifies his aggressive behavior as domestic duty."),
    (10, None,
     "'Vanya, you must not fight on the street!' Nina scolds him with an impersonal negative modal structure."),
    (11, None,
     "'You are the future mayor of the city after all!' Nina reminds him of his political ambitions."),
    (12, None,
     "'You are right, I am a candidate after all!' Samsonov proudly acknowledges his civic status."),
    (13, None,
     "'Then behave calmly, Vanya.' Nina commands him to show restraint and dignity."),
]

TRANSITION = "Now let's listen to the entire conversation once again from start to finish."

OUTRO = (
    "Samsonov returns from a street brawl bruised and defensive, while Nina reminds him that a "
    "mayoral candidate cannot afford public fights."
)

CLOSING = ("samson", "Ты права, я же кандидат!")
