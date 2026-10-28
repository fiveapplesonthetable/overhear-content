# Authoring module for dix-pour-cent s04e02 scene 20 (cue 1035).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-20.py --out out/dix-pour-cent/s04e02/scene-20.json

ID = "dix-pour-cent-s04e02-scene-20"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 20
TITLE = "Une visite inattendue  (An Unexpected Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 1035. Late at night in the empty ASK offices, Andrea pours herself a drink to unwind after a grueling day. "
    "Suddenly, rival StarMedia agent Elise Formain appears in her doorway and asks for a glass, startling Andrea."
)

INTRO = (
    "Late at night in the empty ASK offices, Andrea pours herself a drink to unwind after a grueling day. "
    "Suddenly, rival StarMedia agent Elise Formain appears in her doorway and asks for a glass, startling Andrea. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "La journée a été particulièrement épuisante.",
     "The day was particularly exhausting.",
     [(1035, "Tu m'en sers un")], "Poured a drink after a long day"),
    ("elise", "Tu m'en sers un verre aussi?",
     "Will you pour me a glass too?",
     [(1035, "Tu m'en sers un aussi ?")], "Asked for a drink in Andrea's doorway"),
    ("lea", "Élise? Que fais-tu encore ici?",
     "Elise? What are you still doing here?",
     [(1035, "Tu m'en sers un")], "Reacted with surprise to her presence"),
    ("elise", "La porte d'entrée était restée ouverte.",
     "The entrance door had remained open.",
     [(1035, "Tu m'en sers un")], "Explained how she got into the building"),
    ("lea", "Je ne m'attendais pas à toi.",
     "I was not expecting you.",
     [(1035, "Tu m'en sers un")], "Remarked on the unexpected visit"),
    ("elise", "J'ai besoin de boire un verre.",
     "I need to drink a glass.",
     [(1035, "Tu m'en sers un")], "Admitted her need to unwind"),
    ("lea", "Installe-toi, voici un verre pour toi.",
     "Sit down, here is a glass for you.",
     [(1035, "Tu m'en sers un")], "Offered a glass to her rival"),
    ("elise", "Merci Andréa, j'apprécie beaucoup ce geste.",
     "Thank you Andrea, I really appreciate this gesture.",
     [(1035, "Tu m'en sers un")], "Thanked Andrea for the drink"),
    ("lea", "Tu as l'air vraiment très troublée.",
     "You look really very troubled.",
     [(1035, "Tu m'en sers un")], "Observed her stressed demeanor"),
    ("elise", "J'ai passé une soirée absolument affreuse.",
     "I had an absolutely terrible evening.",
     [(1035, "Tu m'en sers un")], "Confessed that her evening was awful"),
    ("lea", "Un problème grave avec tes clients?",
     "A serious problem with your clients?",
     [(1035, "Tu m'en sers un")], "Inquired about the reason for her distress"),
    ("elise", "Non, c'est bien pire que ça.",
     "No, it is much worse than that.",
     [(1035, "Tu m'en sers un")], "Warned that the crisis is deeper"),
    ("lea", "Alors dis-moi ce qui se passe.",
     "So tell me what is going on.",
     [(1035, "Tu m'en sers un")], "Encouraged her to open up"),
    ("elise", "Prépare-toi à une sacrée surprise.",
     "Prepare yourself for quite a surprise.",
     [(1035, "Tu m'en sers un")], "Hinted at shocking news")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'The day was particularly exhausting.' Andrea pours herself a drink at her desk. "
     "The compound past emphasizes the long day."),
    (1, None,
     "'Will you pour me a glass too?' Elise asks from the office doorway. "
     "The adverbial pronoun en refers back to the drink."),
    (2, None,
     "'Elise? What are you still doing here?' Andrea looks up in utter surprise. "
     "The inverted question marks her shock."),
    (3, None,
     "'The entrance door had remained open.' Elise explains her quiet arrival. "
     "The pluperfect passive tense justifies her sudden presence."),
    (4, None,
     "'I was not expecting you.' Andrea sets down her bottle with caution. "
     "The reflexive imperfect conveys her complete surprise."),
    (5, None,
     "'I need to drink a glass.' Elise steps into the dim room. "
     "The common phrase avoir besoin de expresses urgent need."),
    (6, None,
     "'Sit down, here is a glass for you.' Andrea offers hospitality despite their rivalry. "
     "The imperative sets a cooperative tone."),
    (7, None,
     "'Thank you Andrea, I really appreciate this gesture.' Elise takes the tumbler. "
     "The polite verb acknowledges the small kindness."),
    (8, None,
     "'You look really very troubled.' Andrea studies the rival agent closely. "
     "The idiom avoir l'air describes her tense appearance."),
    (9, None,
     "'I had an absolutely terrible evening.' Elise takes a deep sip of alcohol. "
     "The strong descriptive adjective signals bad news."),
    (10, None,
     "'A serious problem with your clients?' Andrea tries to guess the crisis. "
     "The noun phrase investigates potential agency drama."),
    (11, None,
     "'No, it is much worse than that.' Elise shakes her head grimly. "
     "The comparative adverb highlights the gravity of the shock."),
    (12, None,
     "'So tell me what is going on.' Andrea leans across the desk attentively. "
     "The imperative verb invites an honest explanation."),
    (13, None,
     "'Prepare yourself for quite a surprise.' Elise leans forward with a weary smile. "
     "The expressive adjective foreshadows big news.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Elise's sudden arrival late at night sets the stage for an unexpected corporate confrontation. When you watch the episode, listen out for the expressions meaning 'been' and 'exhausting'. You'll catch them now. See you next time."
CLOSING = ("elise", "Prépare-toi à une sacrée surprise.")
