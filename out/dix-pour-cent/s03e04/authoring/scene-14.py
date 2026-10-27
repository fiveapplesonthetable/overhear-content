# Authoring module for dix-pour-cent s03e04 scene 14 (cues 803-839).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e04/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s03e04/scene-14.json

ID = "dix-pour-cent-s03e04-scene-14"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 14
TITLE = "Panique sur le plateau américain  (Panic on the American Set)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "sharon": "emilie"}
LABELS = {"lea": "Isabelle", "mathias": "Mathias", "sharon": "Sharon"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 803-839. On the set of the American production, star Ben Stiller refuses to leave his trailer "
    "because his dialogue was cut in the rewrite, throwing Mathias and Isabelle into a panic against the clock."
)

INTRO = (
    "On the bustling American movie set in Paris, star actress Isabelle Huppert and agent Mathias race against time. "
    "Disaster strikes when co-star Ben Stiller refuses to leave his trailer after script revisions, threatening the entire evening schedule. "
    "Listen to the scene in French first."
)

STORY = [
    ("mathias", "Tout va bien pour le tournage?",
     "Is everything going well for the shoot?",
     [(803, "Tout va bien")], ""),
    ("lea", "Oui, il faut aller très vite.",
     "Yes, we must go very quickly.",
     [(809, "très vite")], ""),
    ("mathias", "Avez-vous besoin de quelque chose?",
     "Do you need anything?",
     [(806, "besoin de quelque chose")], ""),
    ("lea", "Non, merci, tout est prêt.",
     "No, thank you, everything is ready.",
     [(807, "Non, merci")], ""),
    ("mathias", "Sharon, avez-vous vu Ben Stiller?",
     "Sharon, have you seen Ben Stiller?",
     [(811, "vu Ben"), (817, "Ben Stiller")], ""),
    ("sharon", "Ben ne sort pas de sa loge.",
     "Ben is not leaving his trailer.",
     [(820, "not coming out of his trailer"), (824, "Ben n'aime pas")], ""),
    ("sharon", "Il n'aime pas la nouvelle version.",
     "He does not like the new version.",
     [(824, "dernière version")], ""),
    ("sharon", "Il dit que son texte est coupé.",
     "He says his lines were cut.",
     [(826, "coupé tout son texte")], ""),
    ("lea", "Moi, je suis prête à tourner!",
     "As for me, I am ready to shoot!",
     [(827, "starting blocks")], ""),
    ("mathias", "Qu'est-ce qu'il nous fait là?",
     "What is he doing to us now?",
     [(828, "Qu'est-ce qu'il nous fait")], ""),
    ("lea", "Ben est un véritable perfectionniste.",
     "Ben is a true perfectionist.",
     [(829, "Control freak")], ""),
    ("mathias", "Nous n'arriverons jamais à temps.",
     "We will never make it on time.",
     [(833, "jamais être arrivé à temps")], ""),
    ("mathias", "C'est dur si près du but.",
     "It is hard so close to the goal.",
     [(835, "Si près du but, c'est dur")], ""),
    ("mathias", "Franchement, nous n'avons pas le choix.",
     "Frankly, we have no choice.",
     [(837, "on n'a pas le choix")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Is everything going well for the shoot?' Mathias checks on the production schedule. "
     "The polite question inquires about progress."),
    (1, None,
     "'Yes, we must go very quickly.' Isabelle urges immediate action on set. "
     "The modal phrase stresses urgency."),
    (2, None,
     "'Do you need anything?' Mathias asks if his star requires assistance. "
     "The inverted question offers help."),
    (3, None,
     "'No, thank you, everything is ready.' She confirms her full preparedness. "
     "The polite negative reassures her agent."),
    (4, None,
     "'Sharon, have you seen Ben Stiller?' Mathias searches for the American co-star. "
     "The inquiry asks after the missing actor."),
    (5, None,
     "'Ben is not leaving his trailer.' The assistant delivers bad news from the trailer. "
     "The negative verb describes an impasse."),
    (6, None,
     "'He does not like the new version.' Sharon explains his dissatisfaction with the rewrite. "
     "The negative statement conveys creative tension."),
    (7, None,
     "'He says his lines were cut.' The co-star complains about reduced dialogue. "
     "The reported speech identifies the complaint."),
    (8, None,
     "'As for me, I am ready to shoot!' Isabelle emphasizes her immediate availability. "
     "The exclamation declares her readiness."),
    (9, None,
     "'What is he doing to us now?' Mathias panics over the unexpected complication. "
     "The colloquial question expresses exasperation."),
    (10, None,
     "'Ben is a true perfectionist.' Isabelle wryly comments on his controlling nature. "
     "The descriptive phrase characterizes his demanding style."),
    (11, None,
     "'We will never make it on time.' Mathias fears missing their tight schedule. "
     "The negative future verb predicts delays."),
    (12, None,
     "'It is hard so close to the goal.' He laments a setback right before completion. "
     "The temporal expression highlights frustration."),
    (13, None,
     "'Frankly, we have no choice.' Mathias realizes drastic measures are required. "
     "The definitive statement signals resignation.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Creative egos and impossible deadlines clash under the studio lights as agents scramble to save the day. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "Il faut trouver une solution rapidement.")
