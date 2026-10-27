ID = "domashniy-arest-s01e03-scene-32"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 32
TITLE = "Адвокатская тайна  (Legal Privilege)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "judge": "anja", "golovkin": "angelina"}
LABELS = {"anya": "Аркадий", "judge": "Судья Берг", "golovkin": "Головкин"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1072-1092. Long legal phrasing in cues 1074-1078 is simplified into short A1 sentences; the insult in cue "
    "1080 and the crude opening of cue 1081 are dropped, and '15' is written out as 'пятнадцать'. Outside the "
    "courthouse (cues 1084-1092), the police escort and reporters are narrated around Arkady's lines because of the "
    "three-role limit."
)

INTRO = (
    "Back in the courtroom. Last time, at Dimon's party, tipsy Lyolya blurted out in front of everyone that her ex "
    "had asked her to pretend to be Slavik's girlfriend. Now we return to the court hearing, just after Arkady's "
    "public defender Danila Golovkin has testified and the prosecution has presented the new evidence. Judge Berg "
    "rises to announce his decision. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("judge", "Прошу внимания. Открылись новые обстоятельства по другому делу.",
  "May I have your attention. New circumstances have come to light in another case.",
  [(1072, "Прошу внимания"), (1073, "Открылись новые обстоятельства по другому делу")], ""),
 ("judge", "Махинации с недвижимостью по программе «Доступное жильё».",
  "Property fraud in the 'Affordable Housing' programme.",
  [(1074, "Махинации с недвижимостью по программе «Доступное жильё»")], ""),
 ("judge", "Гражданин Аникеев подозревается в новом преступлении.",
  "Citizen Anikeev is suspected of a new crime.",
  [(1075, "гражданин Аникеев подозревается в")], "cues 1075-1077 simplified to A1"),
 ("judge", "Я вынужден отменить своё решение.",
  "I am forced to cancel my decision.",
  [(1078, "я вынужден отменить свое решение")], "'По совокупности открывшегося' dropped"),
 ("judge", "Мера пресечения остаётся прежней. Домашний арест!",
  "The preventive measure remains the same. House arrest!",
  [(1079, "Мера пресечения остается прежней")], "'Увести' -> 'Домашний арест!' for clarity"),
 ("anya", "Как? Ты?! А как же адвокатская тайна?",
  "How? You?! What about lawyer-client secrecy?",
  [(1080, "Как? Ты"), (1080, "А как же адвокатская тайна")], "insult in cue 1080 dropped"),
 ("golovkin", "Моя мама пятнадцать лет по этой программе стояла!",
  "My mum waited fifteen years in that programme!",
  [(1081, "Моя мама"), (1081, "лет по этой программе"), (1081, "стояла")],
  "crude opening of cue 1081 dropped; '15' written out as 'пятнадцать'"),
 ("golovkin", "Пятнадцать лет в очереди стояла! Забыли?",
  "She stood in the queue for fifteen years! Did you forget?",
  [(1081, "в очереди стояла")], "'Пятнадцать лет' repeated; 'Забыли?' added"),
 ("anya", "Илья Олегович! А как же Лютик?",
  "Ilya Olegovich! But what about Lyutik?",
  [(1082, "А как же Лютик")], "'Илья Олегович!' added"),
 ("anya", "Как же Лютик? Мы же договорились!",
  "What about Lyutik? We had a deal!",
  [(1082, "Как же Лютик")], "'Мы же договорились!' added"),
 ("judge", "Заседание суда объявляю закрытым.",
  "I declare the court session closed.",
  [(1083, "суда объявляю закрытым")], "'Соседание' (subtitle typo) -> 'Заседание'"),
 ("anya", "Оставьте меня в покое! Это какая-то ошибка!",
  "Leave me alone! This is some kind of mistake!",
  [(1085, "Оставьте меня в покое. Это какая-то ошибка")], "outside the courthouse, to the waiting reporters"),
 ("anya", "Отойдите! Без комментариев! Без комментариев!",
  "Step back! No comment! No comment!",
  [(1086, "Отойдите"), (1087, "Без комментариев. Без комментариев")], ""),
]

OPENER = (
    "Let's go through the courtroom showdown line by line. Judge Berg calls for quiet and reads out the new charge."
)

WALK = [
 (0, "Прошу внимания.",
  "'May I have your attention.' Literally, 'I ask of attention', with 'attention' in the genitive case after 'I ask'."),
 (0, "Открылись новые обстоятельства по другому делу.",
  "'New circumstances have come to light in another case.' Literally, 'opened themselves', using the reflexive plural "
  "past tense. And what is that other case?"),
 (1, None,
  "'Property fraud in the Affordable Housing programme.' It is the very programme under which Arkady handed out flats "
  "to Judge Berg's mother and to his own girlfriend Lyolya."),
 (2, None,
  "'Citizen Anikeev is suspected of a new crime.' In court and police language, people are called 'citizen' rather "
  "than 'mister'. With prosecutors and reporters watching, Judge Berg has no choice."),
 (3, None,
  "'I am forced to cancel my decision.' The word for 'forced' is a short masculine participle, followed by the "
  "infinitive 'to cancel'."),
 (4, None,
  "'The preventive measure remains the same. House arrest!' After 'remains', the adjective 'former, the same' takes "
  "the instrumental case ending. Arkady spins around to glare at his stuttering public defender."),
 (5, None,
  "'How? You?! What about lawyer-client secrecy?' The phrase 'and how about' is a classic Russian way to protest "
  "'what about...?' For the first time, timid Danila Golovkin does not stutter at all."),
 (6, None,
  "'My mum waited fifteen years in that programme!' After numbers from five upwards, 'years' becomes the special "
  "genitive plural word for summers, 'fifteen of summers'."),
 (7, None,
  "'She stood in the queue for fifteen years! Did you forget?' While Arkady gave flats to his friends and his "
  "girlfriend, Golovkin's late mother waited fifteen years in vain. Desperate, Arkady shouts to the judge about his "
  "stolen dog."),
 (8, None,
  "'Ilya Olegovich! But what about Lyutik?' Even in open court, he tries to remind the judge of their dog ransom "
  "bargain."),
 (9, None,
  "'What about Lyutik? We had a deal!' The reflexive plural past verb means 'we agreed with each other'. Judge Berg "
  "ignores him and bangs his gavel."),
 (10, None,
  "'I declare the court session closed.' Literally, 'the sitting of the court I declare closed', with 'closed' in the "
  "instrumental case. Outside the courthouse, guards lead Arkady back to the police van through a crowd of reporters."),
 (11, None,
  "'Leave me alone! This is some kind of mistake!' Literally, 'leave me in peace', a fixed everyday expression."),
 (12, None,
  "'Step back! No comment! No comment!' After the preposition 'without', 'comments' takes the genitive plural ending, "
  "and the guards put him back into the van to return to the communal flat."),
]

TRANSITION = "Now let's hear the whole scene once more, start to finish."

OUTRO = (
    "So Arkady's own public defender brought down his appeal, and Arkady is heading straight back to house arrest in "
    "the communal flat — where Judge Berg's stolen dog is still waiting. See you next time."
)
CLOSING = ("anya", "Без комментариев!")
