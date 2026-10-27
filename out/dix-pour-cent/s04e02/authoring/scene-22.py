# Authoring module for dix-pour-cent s04e02 scene 22 (cues 1048-1094).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-22.py --out out/dix-pour-cent/s04e02/scene-22.json

ID = "dix-pour-cent-s04e02-scene-22"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 22
TITLE = "Le départ de Dany Boon  (Dany Boon's Departure)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1048-1094. Andrea questions Elise about the true motive behind her late-night visit, only for Elise to drop "
    "a devastating bombshell: Dany Boon is leaving ASK to join StarMedia. Mathias has orchestrated the defection, "
    "leaving Andrea reeling from the betrayal."
)

INTRO = (
    "Andrea questions Elise about the true motive behind her late-night visit, only for Elise to drop a devastating bombshell: Dany Boon is leaving ASK to join StarMedia. "
    "Mathias has orchestrated the defection, leaving Andrea reeling from the betrayal. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Tu n'es pas venue juste pour ça.",
     "You did not come just for that.",
     [(1048, "tu n'es pas venue pour me dire ça")], "Suspected a deeper ulterior motive"),
    ("elise", "Dany Boon a décidé de quitter ASK.",
     "Dany Boon has decided to leave ASK.",
     [(1049, "Dany Boon quitte ASK")], "Dropped the devastating bombshell"),
    ("lea", "Pardon? Qu'est-ce que tu viens d'annoncer?",
     "Excuse me? What did you just announce?",
     [(1050, "Pardon ?")], "Reacted with disbelief and alarm"),
    ("elise", "Il me rejoint directement chez StarMédia.",
     "He joins me directly at StarMedia.",
     [(1051, "Il me rejoint chez StarMédia")], "Confirmed his new representation"),
    ("lea", "Tu bluffes, c'est totalement faux!",
     "You are bluffing, that is totally false!",
     [(1052, "Tu bluffes")], "Refused to accept the painful claim"),
    ("elise", "Mathias Barneville a fait le nécessaire.",
     "Mathias Barneville did what was needed.",
     [(1053, "Mathias a fait le nécessaire")], "Revealed Mathias's secret maneuvering"),
    ("lea", "Mathias a négocié ce départ en cachette?",
     "Did Mathias negotiate this departure in secret?",
     [(1053, "Mathias a fait")], "Demanded details of the betrayal"),
    ("elise", "Toi aussi, tu t'es fait avoir.",
     "You were fooled too.",
     [(1055, "Toi aussi, tu t'es fait avoir")], "Pointed out their shared vulnerability"),
    ("lea", "Tu voulais voir ma tête bouleversée?",
     "Did you want to see my shocked face?",
     [(1056, "Voir ma tête")], "Accused Elise of petty malice"),
    ("elise", "Non, je veux te faire une proposition.",
     "No, I want to make you a proposal.",
     [(1057, "Je voulais te faire une proposition")], "Pivoted toward an unexpected offer"),
    ("lea", "Quelle sorte de proposition malhonnête?",
     "What kind of dishonest proposal?",
     [(1057, "proposition")], "Inquired with cold suspicion"),
    ("elise", "Nous devrions nous allier contre Mathias.",
     "We should ally ourselves against Mathias.",
     [(1057, "proposition")], "Suggested a tactical alliance"),
    ("lea", "Je ne te ferai jamais confiance.",
     "I will never trust you.",
     [(1057, "proposition")], "Flatly rejected an alliance with her"),
    ("elise", "Réfléchis bien avant de refuser, Andréa.",
     "Think carefully before refusing, Andrea.",
     [(1057, "proposition")], "Urged prudence before walking away")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'You did not come just for that.' Andrea looks at Elise with sharp suspicion. "
     "The negative compound past questions her real motive."),
    (1, None,
     "'Dany Boon has decided to leave ASK.' Elise drops the stunning announcement. "
     "The infinitive phrase conveys the major star defection."),
    (2, None,
     "'Excuse me? What did you just announce?' Andrea gasps in shock. "
     "The idiom venir de emphasizes her immediate disbelief."),
    (3, None,
     "'He joins me directly at StarMedia.' Elise explains the transfer matter-of-factly. "
     "The preposition chez identifies the rival firm."),
    (4, None,
     "'You are bluffing, that is totally false!' Andrea denies the painful reality. "
     "The present tense verb rejects the unbelievable news."),
    (5, None,
     "'Mathias Barneville did what was needed.' Elise reveals Mathias's secret maneuvering. "
     "The idiomatic phrase highlights his behind-the-scenes deal."),
    (6, None,
     "'Did Mathias negotiate this departure in secret?' Andrea realizes the full extent of the betrayal. "
     "The prepositional phrase points out the stealth."),
    (7, None,
     "'You were fooled too.' Elise points out their shared defeat. "
     "The familiar idiom se faire avoir describes being tricked."),
    (8, None,
     "'Did you want to see my shocked face?' Andrea accuses her of gloating. "
     "The descriptive adjective conveys emotional turmoil."),
    (9, None,
     "'No, I want to make you a proposal.' Elise leans across the desk calmly. "
     "The verb phrase introduces a surprising strategic offer."),
    (10, None,
     "'What kind of dishonest proposal?' Andrea responds with cold skepticism. "
     "The interrogative noun phrase challenges her intentions."),
    (11, None,
     "'We should ally ourselves against Mathias.' Elise suggests joining forces against the common rival. "
     "The conditional verb proposes a mutual pact."),
    (12, None,
     "'I will never trust you.' Andrea rejects any cooperation with a StarMedia agent. "
     "The future tense with negative adverbs establishes a firm refusal."),
    (13, None,
     "'Think carefully before refusing, Andrea.' Elise rises and warns her solemnly. "
     "The imperative verb urges prudence before rejecting the deal.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Elise's bombshell about Dany Boon leaves Andrea facing a dangerous new war on two fronts."
CLOSING = ("elise", "Réfléchis bien avant de refuser, Andréa.")
