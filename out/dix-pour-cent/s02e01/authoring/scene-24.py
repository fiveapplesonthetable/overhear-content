# Authoring module for dix-pour-cent s02e01 scene 24 (cues 727-762).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-24.py --out out/dix-pour-cent/s02e01/scene-24.json

ID = "dix-pour-cent-s02e01-scene-24"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 24
TITLE = "La décision de Catherine  (Catherine's Decision)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 727-762. Mathias visits his estranged wife Catherine at their apartment, "
    "hoping for reconciliation after his past scandal. But Catherine has reached "
    "her limit and firmly asks for a divorce. Adapted for A1 French."
)

INTRO = (
    "At Catherine's apartment, Mathias Barneville arrives hoping for a calm conversation "
    "and a chance to repair their marriage. But Catherine has already made up her mind. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Quelle heure est-il?",
     "What time is it?",
     [(727, "Quelle heure est-il ?")], ""),
    ("mathias", "Neuf heures pile, comme convenu.",
     "Nine o'clock sharp, as agreed.",
     [(728, "9 heures pile, comme convenu.")], "Spelled out number 9"),
    ("mathias", "Je peux avoir un café?",
     "Can I have a coffee?",
     [(730, "Je peux avoir un café ?")], ""),
    ("lea", "Il n'en reste plus.",
     "There is none left.",
     [(731, "Il n'en reste plus.")], ""),
    ("mathias", "Ça va?",
     "Are you okay?",
     [(732, "Ça va ?")], ""),
    ("lea", "Prends ce que tu veux, je m'en fiche.",
     "Take whatever you want, I do not care.",
     [(735, "Prends ce que tu veux, je m'en fiche.")], ""),
    ("mathias", "Au téléphone, tu voulais parler.",
     "On the phone, you wanted to talk.",
     [(736, "au téléphone"), (738, "tu voulais parler.")], "Shortened dialogue"),
    ("lea", "Informe les gens de ta nouvelle adresse.",
     "Inform people of your new address.",
     [(740, "informe les gens de ta nouvelle adresse.")], ""),
    ("mathias", "Mais je ne change pas d'adresse!",
     "But I am not changing address!",
     [(741, "Mais je ne change pas d'adresse,")], ""),
    ("mathias", "J'ai commis une grave erreur il y a vingt-quatre ans.",
     "I made a serious mistake twenty-four years ago.",
     [(744, "J'ai commis une grave erreur il y a 24 ans.")], "Spelled out number 24"),
    ("lea", "Je ne veux pas t'empêcher de t'amuser.",
     "I do not want to stop you from having fun.",
     [(748, "Je ne veux pas t'empêcher de t'amuser.")], ""),
    ("mathias", "Je suis son agent, pas son amant.",
     "I am her agent, not her lover.",
     [(752, "Je suis son agent,"), (753, "pas son amant,")], ""),
    ("lea", "Qu'est-ce que j'en sais?",
     "What do I know about it?",
     [(754, "Qu'est-ce que j'en sais ?")], ""),
    ("mathias", "Elle a rompu avec Ramzy, c'est tout.",
     "She broke up with Ramzy, that is all.",
     [(756, "Elle a rompu avec Ramzy")], "Added c'est tout"),
    ("lea", "Tu vois, je ne te crois plus.",
     "You see, I do not believe you anymore.",
     [(757, "Tu vois, c'est ça le problème. Je ne te crois plus.")], "Shortened sentence"),
    ("mathias", "C'est la vérité, Catherine.",
     "It is the truth, Catherine.",
     [(758, "C'est la vérité, Catherine.")], ""),
    ("lea", "Je n'en peux plus. On divorce.",
     "I cannot take it anymore. We are getting a divorce.",
     [(761, "Je n'en peux plus."), (762, "On divorce.")], ""),
]

OPENER = "Let's examine how Mathias and Catherine express their painful separation."

WALK = [
    (0, None,
     "'What time is it?' An inverted question with the verb etre asking for the time."),
    (1, None,
     "'Nine o'clock sharp, as agreed.' The adverb pile means sharp or on the dot."),
    (2, None,
     "'Can I have a coffee?' The modal verb pouvoir expressing a polite request."),
    (3, None,
     "'There is none left.' The pronoun en replaces de cafe with the negative plus."),
    (4, None,
     "'Are you okay?' A standard familiar question using the pronoun ca."),
    (5, None,
     "'Take whatever you want, I do not care.' An imperative followed by an informal expression of indifference."),
    (6, None,
     "'On the phone, you wanted to talk.' The imperfect tense of vouloir expressing past intent."),
    (7, None,
     "'Inform people of your new address.' An imperative addressed to one person."),
    (8, None,
     "'But I am not changing address!' The present tense of changer with standard negation."),
    (9, None,
     "'I made a serious mistake twenty-four years ago.' The time expression il y a followed by a duration."),
    (10, None,
     "'I do not want to stop you from having fun.' The verb empecher followed by the preposition de and an infinitive."),
    (11, None,
     "'I am her agent, not her lover.' Mathias clarifies his professional relationship."),
    (12, None,
     "'What do I know about it?' The pronoun en refers back to his secret life."),
    (13, None,
     "'She broke up with Ramzy, that is all.' The compound past of the verb rompre."),
    (14, None,
     "'You see, I do not believe you anymore.' The verb croire with the negative adverb plus."),
    (15, None,
     "'It is the truth, Catherine.' Mathias pleads his honesty."),
    (16, "Je n'en peux plus.",
     "'I cannot take it anymore.' An idiomatic phrase expressing exhaustion."),
    (16, "On divorce.",
     "'We are getting a divorce.' The informal subject pronoun on used for we."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Catherine has drawn the line after years of betrayals and demands a divorce. "
    "Mathias must face the reality that his family life is slipping away."
)

CLOSING = ("lea", "On divorce.")
