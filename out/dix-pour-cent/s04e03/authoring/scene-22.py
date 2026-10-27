# Authoring module for dix-pour-cent s04e03 scene 22 (cues 996-1023).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-22.py --out out/dix-pour-cent/s04e03/scene-22.json

ID = "dix-pour-cent-s04e03-scene-22"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 22
TITLE = "Le pacte des profiteroles  (The Profiterole Pact)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 996-1023. Over late-night dessert in the hotel room, Andrea confesses that Colette left her because she "
    "always puts her actors before her family. Touched by her sorrow, Jose proposes a mutual pact to stop acting "
    "rashly and reclaim their lives, sealing the promise over a bowl of profiteroles."
)

INTRO = (
    "Over late-night dessert in the hotel room, Andrea confesses that Colette left her because she always puts her actors before her family. "
    "Touched by her sorrow, Jose proposes a mutual pact to stop acting rashly and reclaim their lives, sealing the promise over a bowl of profiteroles. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("jose", "Tu as des nouvelles de Colette?",
     "Do you have any news from Colette?",
     [(996, "Des nouvelles de Colette ?")], "Asked gently about Andrea's partner"),
    ("lea", "J'ai merdé, je l'ai laissée partir.",
     "I messed up, I let her leave.",
     [(997, "J'ai merdé, je l'ai laissée partir")], "Admitted her painful personal mistake"),
    ("jose", "On était destinés à cette soirée.",
     "We were destined for this evening.",
     [(998, "destinés à passer cette soirée ensemble")], "Accepted their shared evening together"),
    ("lea", "Je ferais n'importe quoi pour mes acteurs.",
     "I would do anything for my actors.",
     [(1006, "Je ferais n'importe quoi pour mes acteurs")], "Reflected on her extreme work devotion"),
    ("jose", "Mais tu négliges ta propre famille?",
     "But you neglect your own family?",
     [(1006, "mais pas pour ma famille")], "Identified her distorted priorities"),
    ("lea", "Quand Colette m'appelle, je ne rentre pas.",
     "When Colette calls me, I do not come home.",
     [(1004, "quand ma femme me demande de rentrer")], "Regretted missing dinner with her wife"),
    ("jose", "Ça devrait être totalement l'inverse.",
     "It should be totally the reverse.",
     [(1007, "Ça devrait être l'inverse")], "Pointed out what truly matters in life"),
    ("lea", "J'ai peut-être le cerveau mal câblé.",
     "Maybe my brain is wired wrong.",
     [(1008, "J'ai peut-être le cerveau mal câblé")], "Blamed her stubborn professional drive"),
    ("jose", "Tu sais quoi? Faisons un pacte!",
     "You know what? Let us make a pact!",
     [(1012, "Tu sais quoi ? Faisons un pacte")], "Proposed an important mutual promise"),
    ("lea", "Quel genre de pacte sérieux?",
     "What kind of serious pact?",
     [(1012, "Faisons un pacte")], "Inquired about the nature of the deal"),
    ("jose", "On va reprendre nos vies en main.",
     "We are going to take our lives back in hand.",
     [(1014, "On va reprendre nos vies en main")], "Outlined a pledge for personal change"),
    ("lea", "Et on arrête les décisions impulsives?",
     "And we stop impulsive decisions?",
     [(1016, "arrêter de prendre des décisions à la légère")], "Formulated the core resolution"),
    ("jose", "Exactement, sauf pour ces bonnes profiteroles!",
     "Exactly, except for these delicious profiteroles!",
     [(1020, "Les profiteroles"), (1022, "dernière décision impulsive")], "Made a playful exception for dessert"),
    ("lea", "Ces profiteroles étaient une urgence absolue!",
     "These profiteroles were an absolute emergency!",
     [(1023, "C'était une urgence")], "Sealed the pact with cheerful humor")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Do you have any news from Colette?' Jose asks gently across the table. "
     "The partitive noun phrase investigates her relationship troubles."),
    (1, None,
     "'I messed up, I let her leave.' Andrea confesses her painful guilt. "
     "The colloquial verb merder conveys deep self-reproach."),
    (2, None,
     "'We were destined for this evening.' Jose reflects on their shared solitary night. "
     "The passive construction accepts their situation."),
    (3, None,
     "'I would do anything for my actors.' Andrea acknowledges her distorted priorities. "
     "The conditional verb reveals her career dedication."),
    (4, None,
     "'But you neglect your own family?' Jose questions her life balance candidly. "
     "The present tense verb highlights the costly trade-off."),
    (5, None,
     "'When Colette calls me, I do not come home.' Andrea details her recurring failure. "
     "The negative present tense marks her regret."),
    (6, None,
     "'It should be totally the reverse.' Jose points out the proper order of priorities. "
     "The conditional verb prescribes emotional balance."),
    (7, None,
     "'Maybe my brain is wired wrong.' Andrea blames her own stubborn nature. "
     "The colloquial adjective phrase humorously conveys self-doubt."),
    (8, None,
     "'You know what? Let us make a pact!' Jose leans forward with sudden determination. "
     "The imperative verb proposes a joint commitment."),
    (9, None,
     "'What kind of serious pact?' Andrea looks up with curious interest. "
     "The interrogative phrase invites his constructive idea."),
    (10, None,
     "'We are going to take our lives back in hand.' Jose outlines a new resolution. "
     "The idiomatic phrase pledges personal reform."),
    (11, None,
     "'And we stop impulsive decisions?' Andrea checks the terms of the promise. "
     "The present tense verb affirms a thoughtful approach."),
    (12, None,
     "'Exactly, except for these delicious profiteroles!' Jose laughs as dessert arrives. "
     "The prepositional phrase creates a comical exception."),
    (13, None,
     "'These profiteroles were an absolute emergency!' Andrea laughs as she takes a spoon. "
     "The expressive noun phrase playfully seals the pact.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Sealing their pact over profiteroles, Jose and Andrea find comforting friendship in the midst of turmoil."
CLOSING = ("lea", "Ces profiteroles étaient une urgence absolue!")
