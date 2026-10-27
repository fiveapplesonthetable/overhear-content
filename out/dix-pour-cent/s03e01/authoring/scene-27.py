# Authoring module for dix-pour-cent s03e01 scene 27 (cues 1034-1107).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e01/authoring/scene-27.py --out overhear-content/out/dix-pour-cent/s03e01/scene-27.json

ID = "dix-pour-cent-s03e01-scene-27"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 27
TITLE = "Le bilan annuel et le sursis  (Annual Review and Probation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1034-1107. During the ASK annual review, Hicham praises Andrea, Mathias, and Arlette, "
    "then threatens to fire Gabriel for serious misconduct. Andrea steps in to defend Gabriel, "
    "and Hicham grants him a second chance under Andrea's supervision."
)

INTRO = (
    "In the ASK conference room, Hicham holds the agency's end-of-year review meeting. "
    "After complimenting the team, he drops a bombshell about Gabriel's future at the agency. "
    "Listen to the dramatic confrontation in French first. Don't worry about catching every word."
)

STORY = [
    ("hicham", "Vous vous êtes tous battus comme des chiens.", "You all fought like dogs.",
     [(1039, "Vous vous êtes tous battus comme des chiens")], "Hicham paces before the assembled team"),
    ("hicham", "Andréa, c'est le pitbull.", "Andrea, she is the pitbull.",
     [(1041, "Andrea, c'est le pitbull")], ""),
    ("hicham", "Tu n'as rien lâché toute l'année.", "You never gave up all year.",
     [(1043, "T'as rien lâché toute l'année")], ""),
    ("hicham", "Mathias, c'est le chien de chasse.", "Mathias, he is the hunting dog.",
     [(1045, "Mathias, c'est le chien de chasse")], ""),
    ("hicham", "Un flair exceptionnel.", "An exceptional instinct.",
     [(1047, "Un flair exceptionnel")], ""),
    ("hicham", "Arlette, c'est Jean Gabin.", "Arlette, she is Jean Gabin.",
     [(1054, "c'est Jean Gabin")], ""),
    ("hicham", "Elle vous emmène toujours où elle veut.", "She always takes you where she wants.",
     [(1056, "et elle vous emmène toujours où elle veut")], ""),
    ("hicham", "Elle aurait été excellente sans un naufrage.", "It could have been excellent without a disaster.",
     [(1066, "Elle aurait même pu être excellente sans un naufrage inattendu")], "Hicham turns his cold gaze to Gabriel"),
    ("hicham", "Pour virer un associé, il faut une faute.", "To fire a partner, you must prove misconduct.",
     [(1073, "Pour virer un associé, il faut prouver une faute grave")], ""),
    ("lea", "Attendez, qu'est-ce que c'est?", "Wait, what is going on here?",
     [(1075, "Attendez, qu'est-ce que c'est")], "Andrea speaks up with outrage"),
    ("hicham", "La faute grave, c'est d'avoir menti.", "The serious misconduct is having lied.",
     [(1080, "c'est d'avoir menti")], ""),
    ("gabriel", "J'ai compris, je m'en vais.", "I understand, I am leaving.",
     [(1086, "J'ai compris. Je m'en vais")], "Gabriel stands up in humiliation"),
    ("lea", "Une décision pareille se prend entre nous!", "Such a decision is made between us!",
     [(1091, "Une décision pareille, ça se prend entre nous")], ""),
    ("hicham", "Tout le monde a le droit à une chance?", "Does everyone deserve a second chance?",
     [(1095, "Tout le monde a le droit à une deuxième chance")], ""),
    ("lea", "À partir de maintenant, on fait tout ensemble!", "From now on, we do everything together!",
     [(1106, "À partir de maintenant, je vais tout faire avec toi")], "Andrea looks firmly at Gabriel"),
]

OPENER = "Let's walk through this intense confrontation in the agency meeting step by step."

WALK = [
    (0, None,
     "'You all fought like dogs.' Hicham praises the relentless effort of the team."),
    (1, None,
     "'Andrea, she is the pitbull.' Hicham highlights Andrea for her fierce tenacity."),
    (2, None,
     "'You never gave up all year.' Hicham commends her unwavering dedication to her stars."),
    (3, None,
     "'Mathias, he is the hunting dog.' Hicham compares Mathias to an elite hunter."),
    (4, None,
     "'An exceptional instinct.' Hicham praises the sharp business nose of Mathias."),
    (5, None,
     "'Arlette, she is Jean Gabin.' Hicham honors the legendary veteran status of Arlette."),
    (6, None,
     "'She always takes you where she wants.' Hicham explains how Arlette always wins her negotiations."),
    (7, None,
     "'It could have been excellent without a disaster.' Hicham suddenly darkens the celebratory mood."),
    (8, None,
     "'To fire a partner, you must prove misconduct.' Hicham states the legal standard to remove someone."),
    (9, None,
     "'Wait, what is going on here?' Andrea immediately stands up to defend her colleague."),
    (10, None,
     "'The serious misconduct is having lied.' Hicham accuses Gabriel of hiding behind deceit."),
    (11, None,
     "'I understand, I am leaving.' Gabriel feels completely humiliated and prepares to walk out."),
    (12, None,
     "'Such a decision is made between us!' Andrea fiercely asserts the collective agency rules."),
    (13, None,
     "'Does everyone deserve a second chance?' Hicham hesitates after recalling his conversation with Arlette."),
    (14, None,
     "'From now on, we do everything together!' Andrea promises to stay by Gabriel's side through probation."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After threatening to fire Gabriel for hiding his failures, Hicham agrees to keep him at ASK on the condition that Andrea supervises his work."
CLOSING = ("lea", "À partir de maintenant, on fait tout ensemble!")
