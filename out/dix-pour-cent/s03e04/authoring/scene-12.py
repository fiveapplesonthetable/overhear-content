# Authoring module for dix-pour-cent s03e04 scene 12 (cues 699-738).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e04/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s03e04/scene-12.json

ID = "dix-pour-cent-s03e04-scene-12"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 12
TITLE = "Les répliques coupées  (Cut Lines)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sharon": "emilie", "mathias": "theo"}
LABELS = {"lea": "Isabelle Huppert", "sharon": "Sharon", "mathias": "Mathias Barneville"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 699-738. Arriving on the American film set, Isabelle Huppert discovers that director Gary "
    "has heavily trimmed her scene to make it more dynamic. Refusing to be treated as an extra, "
    "Isabelle furiously rejects Mathias's attempts to pacify her and demands an immediate confrontation with Gary. "
    "Adapted for A1 French."
)

INTRO = (
    "Upon arriving on the American film set late at night, Isabelle is handed a freshly revised script by assistant Sharon. "
    "To her outrage, Gary has cut nearly all of her dialogue to speed up the scene. "
    "Let's listen to her fiery reaction in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("sharon", "Bonsoir Isabelle, voici la scène d'aujourd'hui.",
     "Good evening Isabelle, here is today's scene.",
     [(704, "Bonsoir, Isabelle"), (707, "c'est la scène d'aujourd'hui")], "Handing over script"),
    ("lea", "Mais je connais déjà mon texte.",
     "But I already know my lines.",
     [(708, "je connais mon texte")], "Asserting preparation"),
    ("lea", "Attendez, ce n'est pas du tout pareil!",
     "Wait, this is not at all the same!",
     [(710, "attendez, attendez"), (711, "c'est pas du tout pareil")], "Noticing drastic changes"),
    ("lea", "Ce nouveau texte est beaucoup plus court.",
     "This new text is much shorter.",
     [(712, "C'est beaucoup plus court")], "Observing cut dialogue"),
    ("sharon", "Le réalisateur Gary veut une scène plus dynamique.",
     "Director Gary wants a more dynamic scene.",
     [(714, "Gary pense que c'est mieux"), (715, "plus dynamique")], "Explaining directorial choice"),
    ("lea", "Mais il a coupé toutes mes répliques!",
     "But he cut all my lines!",
     [(716, "il m'a coupé toutes mes répliques")], "Protesting drastic cuts"),
    ("mathias", "Isabelle, le dynamisme est très important aujourd'hui.",
     "Isabelle, dynamism is very important today.",
     [(717, "c'est important, le dynamisme"), (719, "Surtout aujourd'hui")], "Trying to appease client"),
    ("lea", "Mathias, je ne fais pas de la figuration!",
     "Mathias, I do not do background work!",
     [(721, "Je ne suis pas venue ici")], "Refusing minor role"),
    ("mathias", "Je peux regarder votre texte une minute?",
     "Can I look at your script for a minute?",
     [(723, "Je peux jeter un oeil sur votre texte")], "Asking to inspect script"),
    ("mathias", "Mais il vous reste encore de belles répliques.",
     "But you still have fine lines left.",
     [(724, "très bien, cette scène"), (725, "Il vous en reste pas mal, des répliques")], "Attempting reassurance"),
    ("lea", "Il a supprimé tout mon grand monologue.",
     "He deleted my entire big monologue.",
     [(727, "Il y avait tout un monologue dont il reste quasiment plus rien")], "Detailing lost speech"),
    ("lea", "Cette séquence est maintenant vide de substance.",
     "This sequence is now empty of substance.",
     [(728, "complètement vide de sa substance")], "Criticizing empty scene"),
    ("lea", "Où est Gary, je veux lui parler!",
     "Where is Gary, I want to talk to him!",
     [(730, "il est où, Gary ?"), (732, "Il faut qu'on parle de ça")], "Demanding confrontation"),
    ("sharon", "D'accord, je vais appeler Gary immédiatement.",
     "Alright, I will call Gary immediately.",
     [(733, "Pouvez-vous envoyer Gary ici ?"), (735, "Maintenant, s'il vous plaît")], "Calling the director"),
]

WALK = [
    (0, None,
     "'Good evening Isabelle, here is today's scene.' Sharon presents the revised pages for the night shoot. "
     "The adverb 'aujourd'hui' means today."),
    (1, None,
     "'But I already know my lines.' Isabelle reminds everyone of her thorough preparation. "
     "The adverb 'deja' means already."),
    (2, None,
     "'Wait, this is not at all the same!' Isabelle spots unexpected script changes. "
     "The negative idiom 'pas du tout' means not at all."),
    (3, None,
     "'This new text is much shorter.' Isabelle notices substantial trims to her part. "
     "The comparative 'plus court' means shorter."),
    (4, None,
     "'Director Gary wants a more dynamic scene.' Sharon relays the creative reasoning behind the rewrite. "
     "The adjective 'dynamique' means lively or energetic."),
    (5, None,
     "'But he cut all my lines!' Isabelle objects to having her speaking part gutted. "
     "The theatrical noun 'replique' denotes an actor's line or cue."),
    (6, None,
     "'Isabelle, dynamism is very important today.' Mathias steps in to prevent an on-set fight. "
     "The masculine noun 'dynamisme' means drive or momentum."),
    (7, None,
     "'Mathias, I do not do background work!' Isabelle indignantly rejects being sidelined. "
     "The noun 'figuration' refers to being an extra or background performer."),
    (8, None,
     "'Can I look at your script for a minute?' Mathias asks to examine the revised draft himself. "
     "The temporal expression 'une minute' means for a minute or briefly."),
    (9, None,
     "'But you still have fine lines left.' Mathias tries to downplay the severity of the cuts. "
     "The adverbial pronoun 'en' refers back to the lines."),
    (10, None,
     "'He deleted my entire big monologue.' Isabelle laments the loss of her centerpiece speech. "
     "The verb 'supprimer' means to delete or remove."),
    (11, None,
     "'This sequence is now empty of substance.' Isabelle critiques the artistic value of the shortened scene. "
     "The feminine noun 'substance' means depth or substance."),
    (12, None,
     "'Where is Gary, I want to talk to him!' Isabelle demands an immediate face-to-face showdown. "
     "The indirect pronoun 'lui' means to him."),
    (13, None,
     "'Alright, I will call Gary immediately.' Sharon yields to the star's firm demand. "
     "The adverb 'immediatement' means right away."),
]

OUTRO = (
    "Isabelle refuses to compromise her craft or let a director trim away her artistic essence. "
    "With Mathias caught in the middle, Gary must face an uncompromising movie star. "
    "Now let's listen to the scene once more."
)

CLOSING = ("lea", "Où est Gary, je veux lui parler!")
