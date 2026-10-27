# Authoring module for dix-pour-cent s03e03 scene 16 (cues 910-1047).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-16.py --out out/dix-pour-cent/s03e03/scene-16.json

ID = "dix-pour-cent-s03e03-scene-16"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 16
TITLE = "Le casting de Samy  (Samy's Casting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 910-1047. On set after a screen test with Gérard Lanvin, newcomer Samy freezes. "
    "While Camille passionately defends him, Mathias insists on protecting the production. "
    "Camille leaves Samy a supportive voicemail."
)

INTRO = (
    "After a tense screen test with Gerard Lanvin, young actor Samy panics and fails to impress the production team. "
    "While Camille fights passionately to protect her new client, Mathias insists on cutting losses to preserve the film. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("mathias", "Samy a complètement raté ses essais.",
     "Samy completely failed his screen tests.",
     [(986, "il s'est complètement crashé")], "Mathias delivers the harsh verdict"),
    ("lea", "Il a juste eu le trac!",
     "He just had stage fright!",
     [(985, "le traque")], "Camille defends the young actor"),
    ("mathias", "Gérard veut un partenaire plus solide.",
     "Gerard wants a more solid partner.",
     [(996, "partenaire plus solide")], "Mathias explains the lead actor's demand"),
    ("lea", "Pourtant, Samy a un talent unique!",
     "Yet, Samy has a unique talent!",
     [(1010, "un truc quand il joue")], "Camille highlights his genuine gift"),
    ("lea", "Il a une grande sensibilité artistique.",
     "He has a great artistic sensitivity.",
     [(1012, "une fragilité")], "Camille describes his emotional depth"),
    ("mathias", "Il ne sait pas encore jouer.",
     "He does not know how to act yet.",
     [(1006, "Il sait pas se comporter")], "Mathias points out the lack of experience"),
    ("mathias", "Nous devons penser à ce film.",
     "We must think about this film.",
     [(1027, "que le film se fasse")], "Mathias prioritizes the whole project"),
    ("lea", "C'est vraiment injuste pour lui!",
     "It is really unfair to him!",
     [(1004, "C'est dégueulasse")], "Camille protests the sudden decision"),
    ("mathias", "Il faut savoir faire des choix.",
     "One must know how to make choices.",
     [(1028, "pour gagner la bataille")], "Mathias justifies tough agency decisions"),
    ("mathias", "Appelle Samy pour lui annoncer.",
     "Call Samy to break the news to him.",
     [(1032, "tomber direct sur sa boîte vocale")], "Mathias instructs Camille to make the call"),
    ("lea", "Allô Samy, c'est Camille, ton agent.",
     "Hello Samy, it is Camille, your agent.",
     [(1035, "C'est Camille, ton agent")], "Camille reaches his voicemail"),
    ("lea", "Je suis désolée pour ce rôle.",
     "I am sorry about this role.",
     [(1036, "je suis vraiment désolée")], "Camille breaks the sad news gently"),
    ("lea", "Mais nous allons continuer ensemble.",
     "But we are going to continue together.",
     [(1042, "On va pas s'arrêter là")], "Camille reassures her client of her loyalty"),
    ("lea", "L'avenir est grand devant nous!",
     "The future is big ahead of us!",
     [(1044, "L'avenir est devant nous")], "Camille ends with an encouraging message")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Samy completely failed his screen tests.' Mathias evaluates the unsuccessful audition. "
     "The compound past verb indicates a completed negative outcome."),
    (1, None,
     "'He just had stage fright!' Camille explains his momentary nervousness. "
     "The compound past verb with an adverbial minimizer softens the failure."),
    (2, None,
     "'Gerard wants a more solid partner.' Mathias states the seasoned actor's requirement. "
     "The comparative adjective denotes a need for greater reliability."),
    (3, None,
     "'Yet, Samy has a unique talent!' Camille insists on his rare artistic ability. "
     "The coordinating adverb introduces an opposing defense."),
    (4, None,
     "'He has a great artistic sensitivity.' Camille praises his emotional resonance. "
     "The feminine adjective describes his nuanced acting style."),
    (5, None,
     "'He does not know how to act yet.' Mathias highlights the newcomer's technical limits. "
     "The negative present verb with an adverb expresses lack of professional mastery."),
    (6, None,
     "'We must think about this film.' Mathias focuses on overall production success. "
     "The modal verb expresses collective professional duty."),
    (7, None,
     "'It is really unfair to him!' Camille voices her deep frustration. "
     "The presentative phrase with an intensifier emphasizes injustice."),
    (8, None,
     "'One must know how to make choices.' Mathias shares hard-nosed industry realism. "
     "The impersonal construction expresses a general business necessity."),
    (9, None,
     "'Call Samy to break the news to him.' Mathias assigns the difficult phone task. "
     "The imperative verb directs immediate action."),
    (10, None,
     "'Hello Samy, it is Camille, your agent.' Camille starts her voicemail recording. "
     "The presentative formula introduces her identity and professional bond."),
    (11, None,
     "'I am sorry about this role.' Camille conveys her heartfelt regrets. "
     "The adjective with an intensifier expresses sympathetic sorrow."),
    (12, None,
     "'But we are going to continue together.' Camille promises ongoing support. "
     "The near future construction commits to long-term collaboration."),
    (13, None,
     "'The future is big ahead of us!' Camille shares an optimistic vision. "
     "The spatial prepositional phrase inspires hope and ambition.")
]

TRANSITION = "Now listen to the scene again at normal speed and see how much you understand."

OUTRO = (
    "Caught between loyalty to a promising young talent and the harsh realities of film production, Camille delivers tough news to Samy. "
    "Listen to the conversation one last time in French."
)

CLOSING = ("lea", "L'avenir est grand devant nous!")
