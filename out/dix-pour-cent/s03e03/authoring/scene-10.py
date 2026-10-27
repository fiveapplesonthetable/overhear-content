# Authoring module for dix-pour-cent s03e03 scene 10 (cues 413-432).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s03e03/scene-10.json

ID = "dix-pour-cent-s03e03-scene-10"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 10
TITLE = "L'essayage de costumes  (The Costume Fitting)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "theo", "mathias": "marcel"}
LABELS = {"lea": "Emma", "gerard": "Gérard Lanvin", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 413-432. In the costume workshop, star Gérard Lanvin gets fitted for trousers "
    "while agent Mathias worries on the phone about an inexperienced newcomer auditioning for a huge role."
)

INTRO = (
    "During a costume fitting for his upcoming feature film, star actor Gerard Lanvin has his waist measured by the costume designer. "
    "Meanwhile, agent Mathias panics over the phone when he hears that an unknown newcomer was put forward for a major part. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Surtout, ne rentrez pas le ventre!",
     "Above all, do not suck in your stomach!",
     [(413, "rentrez pas le ventre")], ""),
    ("lea", "Après, le pantalon sera trop serré.",
     "Afterwards, the trousers will be too tight.",
     [(414, "le pantalon")], ""),
    ("gerard", "Je ne rentre pas mon ventre.",
     "I am not sucking in my stomach.",
     [(415, "Je rentre pas")], ""),
    ("lea", "Relâchez vos muscles, s'il vous plaît.",
     "Relax your muscles, please.",
     [(416, "Relâchez")], ""),
    ("lea", "Très bien, c'est parfait comme ça.",
     "Very good, it is perfect like that.",
     [(418, "Très bien")], ""),
    ("mathias", "Mais c'est vraiment n'importe quoi!",
     "But that is truly ridiculous!",
     [(421, "c'est n'importe quoi")], ""),
    ("mathias", "Le rôle prévu était très modeste.",
     "The intended role was very modest.",
     [(423, "le rôle prévu")], ""),
    ("mathias", "Il n'avait que trois répliques!",
     "He only had three lines!",
     [(424, "trois répliques")], ""),
    ("mathias", "C'est un rôle beaucoup trop gros pour lui.",
     "It is a role way too big for him.",
     [(425, "rôle beaucoup trop gros")], ""),
    ("mathias", "Il n'a jamais rien fait auparavant.",
     "He has never done anything before.",
     [(426, "Il n'a jamais rien fait")], ""),
    ("mathias", "Il va se planter complètement!",
     "He is going to crash and burn completely!",
     [(427, "Il va se planter")], ""),
    ("mathias", "C'est moi qui l'ai présenté au réalisateur.",
     "I am the one who introduced him to the director.",
     [(428, "c'est moi qui l'ai présenté")], ""),
    ("mathias", "Rappelle-moi dès que tu as des nouvelles.",
     "Call me back as soon as you have news.",
     [(429, "tu me rappelles")], ""),
    ("gerard", "Emma, je peux vous voir deux minutes?",
     "Emma, can I see you for two minutes?",
     [(431, "Emma, je peux vous voir")], ""),
    ("lea", "Oui, bien sûr, Gérard, je viens tout de suite.",
     "Yes, of course, Gérard, I am coming right away.",
     [(431, "je peux vous voir")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Above all, do not suck in your stomach!' The costumer gives practical advice during fitting. "
     "The negative imperative warns against unnatural posture."),
    (1, None,
     "'Afterwards, the trousers will be too tight.' She explains the physical consequence. "
     "The future tense verb predicts discomfort."),
    (2, None,
     "'I am not sucking in my stomach.' Gerard defends his natural physique. "
     "The present negative verb asserts honest measurement."),
    (3, None,
     "'Relax your muscles, please.' Emma gently insists on a relaxed stance. "
     "The polite imperative guides the client."),
    (4, None,
     "'Very good, it is perfect like that.' She completes the waist measurement. "
     "The approving adjective confirms accurate sizing."),
    (5, None,
     "'But that is truly ridiculous!' Mathias reacts with shock over the phone. "
     "The colloquial idiom denotes utter absurdity."),
    (6, None,
     "'The intended role was very modest.' Mathias recalls the original casting plan. "
     "The past participle describes a small character."),
    (7, None,
     "'He only had three lines!' He stresses how minor the part was supposed to be. "
     "The restrictive negation highlights minimal dialogue."),
    (8, None,
     "'It is a role way too big for him.' Mathias fears the audition is out of proportion. "
     "The comparative adverb emphasizes overwhelming difficulty."),
    (9, None,
     "'He has never done anything before.' He points out the newcomer's total lack of experience. "
     "The negative past construction underscores professional novelty."),
    (10, None,
     "'He is going to crash and burn completely!' Mathias worries about a devastating failure. "
     "The near future pronominal verb anticipates catastrophe."),
    (11, None,
     "'I am the one who introduced him to the director.' Mathias worries about his own reputation. "
     "The cleft sentence stresses personal professional responsibility."),
    (12, None,
     "'Call me back as soon as you have news.' He demands prompt updates on the audition results. "
     "The imperative verb requests immediate communication."),
    (13, None,
     "'Emma, can I see you for two minutes?' Gerard calls over the designer for a private word. "
     "The modal question politely requests attention."),
    (14, None,
     "'Yes, of course, Gerard, I am coming right away.' Emma readily agrees to step aside with the star. "
     "The present motion verb confirms prompt availability.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Balancing wardrobe measurements with casting emergencies, Gerard Lanvin and Mathias navigate the unpredictable world of film production. "
    "Listen to the conversation once more in French."
)

CLOSING = ("mathias", "J'espère qu'il ne fera pas d'erreur.")
