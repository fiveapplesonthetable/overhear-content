# Authoring module for dix-pour-cent s03e04 scene 21 (cues 1117-1186).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-21.py --out out/dix-pour-cent/s03e04/scene-21.json

ID = "dix-pour-cent-s03e04-scene-21"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 21
TITLE = "Une semaine d'interruption  (A Week of Shutdown)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1117-1186. Gabriel receives a distressing call from Isabelle Huppert, who has completely lost her voice. "
    "With the American shoot shut down for a week, Andrea warns Gabriel that insurance investigators will uncover their illegal double shoot."
)

INTRO = (
    "Gabriel receives a distressing call from Isabelle Huppert, who has completely lost her voice. "
    "With the American shoot shut down for a week, Andrea warns Gabriel that insurance investigators will uncover their illegal double shoot. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("gabriel", "Allô Isabelle, comment vous sentez-vous ce matin?",
     "Hello Isabelle, how are you feeling this morning?",
     [(1132, "c'est Isabelle"), (1139, "Ça va, Isabelle")], "Checked on her health status"),
    ("gabriel", "Comment ça, vous n'avez plus de voix?",
     "What do you mean, you have no voice left?",
     [(1145, "Comment ça, plus de voix")], "Reacted with disbelief to her whisper"),
    ("gabriel", "La cortisone n'a donc fait aucun effet?",
     "Did the cortisone have no effect then?",
     [(1146, "Et la cortisone"), (1147, "Plus aucun effet")], "Inquired about the medication failure"),
    ("gabriel", "Le médecin vous arrête pendant une semaine?",
     "Is the doctor stopping you for a week?",
     [(1150, "Elle est arrêtée pendant une semaine")], "Learned about the medical leave order"),
    ("lea", "Le tournage américain va s'arrêter aussi?",
     "Is the American shoot going to stop too?",
     [(1151, "Du coup, le tournage américain aussi")], "Asked about the international production"),
    ("gabriel", "Oui Andréa, le film est totalement suspendu.",
     "Yes Andrea, the film is totally suspended.",
     [(1151, "le tournage américain aussi")], "Confirmed the complete work stoppage"),
    ("lea", "Une interruption coûte des millions de dollars.",
     "A shutdown costs millions of dollars.",
     [(1158, "ça coûte un paquet de pognon"), (1159, "quelques millions de dollars")], "Highlighted the immense financial losses"),
    ("gabriel", "Les assurances remboursent généralement ces frais imprévus.",
     "Insurances generally reimburse these unforeseen costs.",
     [(1155, "Les assurances prennent en charge les frais")], "Relied on standard insurance coverage"),
    ("lea", "Les compagnies adorent chercher la petite bête.",
     "The companies love to nitpick.",
     [(1162, "aiment bien chercher la petite bête")], "Warned about aggressive claims adjusters"),
    ("gabriel", "Pourquoi devraient-elles s'inquiéter de cette grippe?",
     "Why should they worry about this flu?",
     [(1156, "des acteurs qui tombent malades")], "Questioned why an illness would raise suspicion"),
    ("lea", "Isabelle tournait un second film la nuit!",
     "Isabelle was shooting a second film at night!",
     [(1167, "avec nos deux films")], "Reminded him of the secret night shoot"),
    ("lea", "Ils peuvent nous faire porter le chapeau.",
     "They can pin the blame on us.",
     [(1169, "nous faire porter le chapeau")], "Feared massive liability for the agency"),
    ("gabriel", "Ne paniquons pas avant de savoir.",
     "Let us not panic before knowing.",
     [(1170, "arrêtez d'élucubrer")], "Urged calm and patience"),
    ("gabriel", "Les assurances feront simplement leur travail normal.",
     "The insurances will simply do their normal work.",
     [(1171, "les assurances feront leur boulot")], "Downplayed the risk of investigation")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Hello Isabelle, how are you feeling this morning?' Gabriel picks up the phone with concern. "
     "The polite greeting opens the urgent telephone call."),
    (1, None,
     "'What do you mean, you have no voice left?' Gabriel reacts with sheer shock to her hoarse whisper. "
     "The negative partitive expression indicates total voice loss."),
    (2, None,
     "'Did the cortisone have no effect then?' Gabriel asks about the prescribed anti-inflammatory drugs. "
     "The negative compound past verb expresses surprise at medical failure."),
    (3, None,
     "'Is the doctor stopping you for a week?' Gabriel hears the medical verdict with dismay. "
     "The transitive verb denotes official sick leave from filming."),
    (4, None,
     "'Is the American shoot going to stop too?' Andrea immediately grasps the catastrophic consequences. "
     "The near-future verbal construction anticipates an immediate work freeze."),
    (5, None,
     "'Yes Andrea, the film is totally suspended.' Gabriel confirms the grim reality. "
     "The passive past participle indicates an indefinite pause on set."),
    (6, None,
     "'A shutdown costs millions of dollars.' Andrea calculates the staggering financial damages. "
     "The present tense verb introduces the huge monetary stakes."),
    (7, None,
     "'Insurances generally reimburse these unforeseen costs.' Gabriel tries to reassure Andrea. "
     "The present verb describes typical indemnification policies."),
    (8, None,
     "'The companies love to nitpick.' Andrea points out that insurers scrutinize claims. "
     "The colorful French idiom describes finding fault in minor details."),
    (9, None,
     "'Why should they worry about this flu?' Gabriel struggles to see any immediate suspicion. "
     "The interrogative modal construction questions the risk of an audit."),
    (10, None,
     "'Isabelle was shooting a second film at night!' Andrea exposes their blatant contractual fraud. "
     "The imperfect verb highlights the exhausting concurrent nocturnal production."),
    (11, None,
     "'They can pin the blame on us.' Andrea warns that ASK will be held fully liable. "
     "The idiomatic causative phrase expresses scapegoating and financial ruin."),
    (12, None,
     "'Let us not panic before knowing.' Gabriel desperately appeals for rational composure. "
     "The first-person plural imperative urges emotional self-control."),
    (13, None,
     "'The insurances will simply do their normal work.' Gabriel clings to hope that the audit stays routine. "
     "The future tense verb anticipates a standard claim settlement.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "With Isabelle silenced by acute laryngitis, Gabriel and Andrea face the terrifying threat of an insurance investigation. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("gabriel", "Les assurances feront simplement leur travail normal.")
