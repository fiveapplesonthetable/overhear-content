# Authoring module for dix-pour-cent s04e03 scene 14 (cues 654-665).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s04e03/scene-14.json

ID = "dix-pour-cent-s04e03-scene-14"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 14
TITLE = "Panique matinale  (Morning Panic)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "assistant": "theo"}
LABELS = {"lea": "Andréa", "assistant": "Chauffeur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 654-665. Andréa wakes up late in her apartment and discovers that José Garcia "
    "has disappeared before his shoot. When the driver calls looking for him, Andréa checks "
    "on baby Flora only to find her crib empty."
)

INTRO = (
    "Andrea Martel wakes up late in her apartment and discovers that her star client Jose Garcia is missing. "
    "When the film crew arrives to pick him up, Andrea runs to check on baby Flora only to find her crib completely empty. "
    "Let's listen to her morning panic in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Putain! Quelle heure est-il?",
     "Damn! What time is it?",
     [(654, "Putain")], "Andréa wakes up in a panic"),
    ("lea", "José? Il faut te lever maintenant!",
     "Jose? You have to get up now!",
     [(655, "José ?"), (656, "Il faut te lever")], "Andréa calls for José"),
    ("lea", "Dépêche-toi, on est en retard.",
     "Hurry up, we are late.",
     [(656, "on est en retard")], "Andréa urges him to get ready"),
    ("lea", "José, où es-tu passé?",
     "Jose, where did you go?",
     [(657, "José…")], "Andréa finds an empty bed"),
    ("assistant", "Allô Andréa? Je viens chercher José.",
     "Hello Andrea? I am coming to pick up Jose.",
     [(658, "Allô ?"), (658, "Je viens chercher José")], "The driver calls on the phone"),
    ("lea", "Écoute, je le cherche aussi.",
     "Listen, I am looking for him too.",
     [(659, "Je le cherche aussi")], "Andréa confesses she lost him"),
    ("assistant", "Il n'est pas avec toi?",
     "He is not with you?",
     [(661, "Il n'est pas avec toi ?")], "The driver is confused"),
    ("lea", "Non, il n'est plus là!",
     "No, he is no longer here!",
     [(660, "il n'est plus là")], "Andréa admits the disappearance"),
    ("assistant", "La production attend sur le plateau.",
     "Production is waiting on set.",
     [(658, "chercher José")], "The driver emphasizes the schedule"),
    ("lea", "Je te rappelle tout de suite.",
     "I call you back immediately.",
     [(662, "Je te rappelle")], "Andréa hangs up abruptly"),
    ("lea", "Mon cœur, il faut te réveiller.",
     "Sweetheart, you must wake up.",
     [(663, "Mon cœur, il faut te réveiller")], "Andréa enters the nursery"),
    ("lea", "On est en retard pour la crèche.",
     "We are late for the daycare.",
     [(664, "On est en retard pour la crèche")], "Andréa prepares to dress Flora"),
    ("lea", "Flora? Où est mon bébé?",
     "Flora? Where is my baby?",
     [(665, "Flora ?")], "Andréa sees the empty crib"),
    ("lea", "Non, ce n'est pas possible!",
     "No, this is not possible!",
     [(665, "Flora ?")], "Andréa gasps in horror"),
]

WALK = [
    (0, None,
     "'Damn! What time is it?' Andrea realizes that her alarm failed to ring. "
     "The swear word 'putain' is very common in informal French to express shock."),
    (1, None,
     "'Jose? You have to get up now!' Andrea calls out into the apartment to wake her client. "
     "The impersonal expression 'il faut' expresses necessity."),
    (2, None,
     "'Hurry up, we are late.' Andrea stresses the urgent schedule for the film set. "
     "The reflexive imperative 'depeche-toi' means hurry up."),
    (3, None,
     "'Jose, where did you go?' Andrea searches through the rooms and finds the couch empty. "
     "The interrogative 'ou' asks about location."),
    (4, None,
     "'Hello Andrea? I am coming to pick up Jose.' The production driver rings the doorbell from the street. "
     "The near-future phrase 'viens chercher' means coming to pick up."),
    (5, None,
     "'Listen, I am looking for him too.' Andrea confesses that her guest has vanished. "
     "The direct object pronoun 'le' replaces Jose."),
    (6, None,
     "'He is not with you?' The driver is astonished that the actor is missing. "
     "The negative structure 'ne ... pas' surrounds the verb."),
    (7, None,
     "'No, he is no longer here!' Andrea confirms that Jose disappeared without a word. "
     "The adverb 'plus' indicates that he was there before."),
    (8, None,
     "'Production is waiting on set.' The driver warns that the filming crew cannot afford delays. "
     "The noun 'plateau' refers to a film set."),
    (9, None,
     "'I call you back immediately.' Andrea ends the phone call to investigate the apartment. "
     "The idiom 'tout de suite' means right away."),
    (10, None,
     "'Sweetheart, you must wake up.' Andrea enters the nursery to get her baby daughter ready. "
     "The pet name 'mon coeur' is a loving term of endearment."),
    (11, None,
     "'We are late for the daycare.' Andrea rushes over to the small bed. "
     "The feminine noun 'creche' designates a daycare center for infants."),
    (12, None,
     "'Flora? Where is my baby?' Andrea stares at the unoccupied sheets in disbelief. "
     "The possessive adjective 'mon' agrees with the masculine noun 'bebe'."),
    (13, None,
     "'No, this is not possible!' Andrea panics when she realizes that both Jose and Flora are gone. "
     "The demonstrative phrase 'ce n'est pas possible' expresses utter disbelief."),
]

OUTRO = (
    "Andrea discovers that both her movie star client and her infant daughter have vanished from the apartment. "
    "Terrified that Jose took the baby without permission, she prepares to race across Paris. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "José est parti avec ma fille!")
