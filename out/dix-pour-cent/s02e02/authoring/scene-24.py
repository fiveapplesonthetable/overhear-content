# Authoring module for dix-pour-cent s02e02 scene 24 (cues 801-833).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-24.py --out out/dix-pour-cent/s02e02/scene-24.json

ID = "dix-pour-cent-s02e02-scene-24"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 24
TITLE = "L'interruption de Bréhier  (Bréhier's Interruption)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "brehier": "marcel", "fabrice": "theo"}
LABELS = {"lea": "Andréa", "brehier": "Bréhier", "fabrice": "Fabrice"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 801-833. Rival agent François Bréhier corners Fabrice and Andréa at the restaurant. "
    "He reveals that the James Bond casting audition was a fake scheme created by ASK, triggering a furious clash between Andréa and Bréhier."
)

INTRO = (
    "Rival talent agent Francois Brehier ambushes Andrea Martel and Fabrice Luchini at their dinner table. "
    "Hoping to steal Luchini back, Brehier reveals that the coveted James Bond audition was an elaborate trick orchestrated by ASK. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("brehier", "Ne te laisse pas avoir, Fabrice!",
     "Do not let yourself be fooled, Fabrice!",
     [(801, "Ne te laisse pas avoir par elle")], ""),
    ("brehier", "Cette femme est très dangereuse.",
     "This woman is very dangerous.",
     [(802, "-Elle est dangereuse")], ""),
    ("fabrice", "Pardon? De quoi est-ce que tu parles?",
     "Excuse me? What are you talking about?",
     [(802, "-Pardon ?")], ""),
    ("brehier", "L'histoire du film Bond était du bidon!",
     "The Bond film story was total nonsense!",
     [(803, "L'histoire du film Bond, c'était du bidon")], ""),
    ("brehier", "C'est Andréa qui a tout manigancé.",
     "It is Andréa who engineered everything.",
     [(805, "-C'est toi qui as tout manigancé")], ""),
    ("lea", "Je n'ai pas le pouvoir d'inventer ça.",
     "I do not have the power to make that up.",
     [(806, "Je suis flatté que tu me croies")], ""),
    ("brehier", "Ce n'était pas la vraie directrice de casting.",
     "It was not the real casting director.",
     [(807, "Ce n'était pas Debbie MacWilliams que tu as rencontrée")], ""),
    ("fabrice", "Mais alors, qui était cette femme?",
     "Well then, who was this woman?",
     [(808, "C'était qui, alors ?")], ""),
    ("brehier", "Elle voulait se venger de notre agence.",
     "She wanted to get revenge on our agency.",
     [(810, "Elle veut juste se venger pour l'affaire Ramzy-Efira")], ""),
    ("lea", "C'est vous qui avez appelé le fisc!",
     "It is you who called the tax inspectors!",
     [(814, "Vous nous avez dénoncés au fisc !")], ""),
    ("brehier", "Votre agence est complètement ruinée!",
     "Your agency is completely ruined!",
     [(815, "Maintenant qu'ils sont ruinés")], ""),
    ("lea", "Crois ce que tu veux, Fabrice.",
     "Believe what you want, Fabrice.",
     [(817, "Crois ce que tu veux, Fabrice")], ""),
    ("fabrice", "Vous êtes vraiment bizarres, vous les agents!",
     "You agents are really strange!",
     [(821, "Vous êtes vraiment bizarres, vous les agents")], ""),
    ("lea", "Fiche-moi la paix, François!",
     "Leave me alone, François!",
     [(831, "Fiche-moi la paix, maintenant !")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Do not let yourself be fooled, Fabrice!' Brehier barges into the dinner with an urgent warning. "
     "The reflexive structure ne te laisse pas avoir warns against deception."),
    (1, None,
     "'This woman is very dangerous.' The rival agent attacks Andrea's integrity directly. "
     "The feminine adjective dangereuse describes a serious threat."),
    (2, None,
     "'Excuse me? What are you talking about?' Fabrice is taken aback by the sudden aggressive outburst. "
     "The question de quoi est-ce que asks for clarification."),
    (3, None,
     "'The Bond film story was total nonsense!' Brehier drops the bombshell about the fraudulent audition. "
     "The colloquial phrase du bidon means completely fake."),
    (4, None,
     "'It is Andrea who engineered everything.' He points fingers directly at her manipulative tactics. "
     "The past participle manigance describes plotting behind the scenes."),
    (5, None,
     "'I do not have the power to make that up.' Andrea calmly tries to deflect the damaging accusation. "
     "The infinitive inventer means to fabricate or invent."),
    (6, None,
     "'It was not the real casting director.' Brehier exposes the impostor who conducted the fake meeting. "
     "The adjective vraie comes before the noun."),
    (7, None,
     "'Well then, who was this woman?' Fabrice begins to suspect that he was indeed tricked. "
     "The connector mais alors questions the identity of the stranger."),
    (8, None,
     "'She wanted to get revenge on our agency.' Brehier explains the bitter motive behind the scheme. "
     "The reflexive verb se venger expresses retaliating."),
    (9, None,
     "'It is you who called the tax inspectors!' Andrea hits back with Brehier's own underhanded sabotage. "
     "The noun fisc refers to the government tax audit office."),
    (10, None,
     "'Your agency is completely ruined!' He sneers at ASK's desperate financial state. "
     "The past participle ruinee describes total economic ruin."),
    (11, None,
     "'Believe what you want, Fabrice.' She refuses to grovel or debate further in front of her rival. "
     "The imperative crois invites independent judgment."),
    (12, None,
     "'You agents are really strange!' Fabrice is disgusted by the vicious pettiness of talent agents. "
     "The plural adjective bizarres highlights their absurd rivalry."),
    (13, None,
     "'Leave me alone, Francois!' Andrea finishes the confrontation by dismissing Brehier completely. "
     "The colloquial imperative fiche-moi la paix orders him to back off."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Francois Brehier exposes the James Bond audition ruse, leaving Fabrice thoroughly bewildered. "
    "Remember the forceful conversational French phrase for telling someone to back off: fiche-moi la paix."
)

CLOSING = ("lea", "Fiche-moi la paix, François!")
