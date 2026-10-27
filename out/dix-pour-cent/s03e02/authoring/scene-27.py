# Authoring module for dix-pour-cent s03e02 scene 27 (cues 1177-1201).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-27.py --out overhear-content/out/dix-pour-cent/s03e02/scene-27.json

ID = "dix-pour-cent-s03e02-scene-27"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 27
TITLE = "Le pacte secret  (The Secret Pact)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1177-1201. Andrea and Gabriel plan their secret departure from ASK. "
    "Addressing fears of betrayal and leaks, Andrea insists that they prepare all legal groundwork in total secrecy before approaching their actors."
)

INTRO = (
    "As Andrea and Gabriel weigh the monumental consequences of breaking away from ASK, they debate whether their star actors and colleagues will stand by them in secret. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("gabriel", "Et Arlette, qu'est-ce qu'on fait?", "And Arlette, what do we do?",
     [(1177, "Arlette"), (1179, "qu'est-ce qu'on fait")], "Gabriel worries about their senior colleague"),
    ("lea", "Arlette comprendra très bien notre choix.", "Arlette will understand our choice very well.",
     [(1180, "Arlette, elle comprendra")], ""),
    ("gabriel", "Et on plante Mathias tout seul?", "And we leave Mathias completely behind?",
     [(1179, "On le plante")], ""),
    ("lea", "Mathias ne donne pas de leçons!", "Mathias does not give moral lessons!",
     [(1182, "donner les leçons de solidarité")], ""),
    ("gabriel", "Est-ce que les acteurs nous suivraient?", "Would the actors follow us?",
     [(1184, "Ils nous suivraient, tu crois")], "Gabriel paces nervously"),
    ("lea", "Bien sûr qu'ils vont nous suivre.", "Of course they are going to follow us.",
     [(1185, "Bien sûr")], ""),
    ("lea", "Il n'y a aucune raison d'hésiter.", "There is no reason to hesitate.",
     [(1186, "y a aucune raison")], ""),
    ("gabriel", "Il faut d'abord tâter le terrain.", "We must test the waters first.",
     [(1188, "Faut tâter le terrain")], ""),
    ("lea", "Non, surtout pas de sondage!", "No, absolutely no testing!",
     [(1191, "Surtout pas")], "Andrea shakes her head adamantly"),
    ("lea", "Il ne faut en parler à personne.", "We must not speak of it to anyone.",
     [(1193, "Faut en parler à personne")], ""),
    ("lea", "Sinon, tout cela va fuiter.", "Otherwise, all of this will leak.",
     [(1194, "sinon, ça va fuiter")], ""),
    ("gabriel", "On fait quoi dans ce cas?", "What do we do in that case?",
     [(1196, "On fait quoi, alors")], ""),
    ("lea", "On prépare toutes les démarches discrètement.", "We prepare all the paperwork discreetly.",
     [(1197, "On fait toutes les démarches")], ""),
    ("lea", "Quand tout est prêt, on annonce tout.", "When everything is ready, we announce everything.",
     [(1198, "Quand on est prêt, là, on en informe les acteurs")], ""),
    ("gabriel", "D'accord, alors là, on le fait!", "Agreed, so right now, we do it!",
     [(1199, "Là, on le fait")], "Gabriel shakes hands with Andrea to seal the pact"),
]

OPENER = "Let's walk through this strategic pact to launch a new talent agency step by step."

WALK = [
    (0, None,
     "'And Arlette, what do we do?' Gabriel immediately thinks of their beloved mentor at the agency."),
    (1, None,
     "'Arlette will understand our choice very well.' Andrea is confident that Arlette will bless their ambition."),
    (2, None,
     "'And we leave Mathias completely behind?' Gabriel raises concern about abandoning their senior colleague."),
    (3, None,
     "'Mathias does not give moral lessons!' Andrea dismisses Mathias as a ruthless self-interested operator."),
    (4, None,
     "'Would the actors follow us?' Gabriel ponders whether their prestigious roster of clients will defect."),
    (5, None,
     "'Of course they are going to follow us.' Andrea expresses absolute faith in their personal client loyalty."),
    (6, None,
     "'There is no reason to hesitate.' Andrea urges Gabriel to shake off his customary doubts."),
    (7, None,
     "'We must test the waters first.' Gabriel suggests cautiously sounding out a few reliable confidants."),
    (8, None,
     "'No, absolutely no testing!' Andrea vehemently rejects any premature inquiries that could expose them."),
    (9, None,
     "'We must not speak of it to anyone.' Andrea insists on absolute secrecy to protect their breakaway plan."),
    (10, None,
     "'Otherwise, all of this will leak.' Andrea warns that word will quickly get back to Hicham."),
    (11, None,
     "'What do we do in that case?' Gabriel seeks clarity on the exact steps they should execute."),
    (12, None,
     "'We prepare all the paperwork discreetly.' Andrea outlines the legal groundwork needed before the launch."),
    (13, None,
     "'When everything is ready, we announce everything.' Andrea plans a coordinated reveal once they are safe."),
    (14, None,
     "'Agreed, so right now, we do it!' Gabriel formally shakes hands on the secret agency rebellion."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Setting aside fear and hesitation, Andrea and Gabriel seal a secret pact to launch their own talent agency in complete defiance of Hicham."
CLOSING = ("gabriel", "D'accord, alors là, on le fait!")
