# Authoring module for dix-pour-cent s04e01 scene 20 (cues 907-938).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-20.py --out out/dix-pour-cent/s04e01/scene-20.json

ID = "dix-pour-cent-s04e01-scene-20"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 20
TITLE = "La déception de Sophia  (Sophia's Disappointment)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sophia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 907-938. Seated in the middle of the auditorium, Sophia realizes from her seat placement "
    "that she won't win the César for Best Female Newcomer, and storms out of the hall when the winner is announced."
)

INTRO = (
    "Inside the grand auditorium of the Cesars, Sophia and Gabriel reach their seats in the middle of row D. "
    "Convinced by industry superstition that winners are always placed on the aisle, Sophia loses hope, and storms out when the award goes to someone else. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Nos places sont là, au milieu.",
     "Our seats are there, in the middle.",
     [(907, "juste ici")], "Gabriel spots their assigned row"),
    ("lea", "C'est réglé, je ne gagnerai pas.",
     "It is settled, I will not win.",
     [(909, "c'est réglé")], "Sophia gives in to superstitious dread"),
    ("gabriel", "Pourquoi dis-tu cela si vite, Sophia?",
     "Why do you say that so quickly, Sophia?",
     [(910, "Pourquoi")], "Gabriel questions her sudden gloom"),
    ("lea", "Parce que nous sommes au milieu!",
     "Because we are in the middle!",
     [(910, "au milieu")], "Sophia cites seating layout rules"),
    ("gabriel", "Cela ne change rien au vote.",
     "That changes nothing about the vote.",
     [(913, "Arrête de stresser")], "Gabriel rationalizes the situation"),
    ("lea", "Les gagnants sont toujours en bout!",
     "The winners are always on the end!",
     [(912, "en bout de rangée")], "Sophia insists on award ceremony habits"),
    ("gabriel", "Arrête de stresser et profite enfin.",
     "Stop stressing and just enjoy.",
     [(913, "Profite")], "Gabriel urges her to relax"),
    ("lea", "On annonce la révélation féminine maintenant.",
     "They are announcing female newcomer now.",
     [(935, "révélation féminine")], "Sophia turns toward the stage"),
    ("gabriel", "Écoute attentivement l'ouverture de l'enveloppe.",
     "Listen closely to the opening of the envelope.",
     [(934, "ouvrir l'enveloppe")], "Gabriel braces for the result"),
    ("lea", "Une autre actrice a remporté le trophée!",
     "Another actress won the trophy!",
     [(936, "est attribué à")], "Sophia hears the losing result"),
    ("gabriel", "Sophia, reste assise, ne pars pas!",
     "Sophia, stay seated, do not leave!",
     [(937, "ne pouvez pas quitter")], "Gabriel tries to stop her"),
    ("lea", "Je n'ai pas gagné, je pars.",
     "I did not win, I am leaving.",
     [(938, "Je n'ai pas gagné")], "Sophia refuses to stay"),
    ("gabriel", "C'est une réaction trop impulsive, attends!",
     "That is too impulsive a reaction, wait!",
     [(937, "quitter la cérémonie")], "Gabriel warns against a public scene"),
    ("lea", "Je refuse de rester assise ici!",
     "I refuse to sit here!",
     [(938, "Je n'ai pas gagné, alors")], "Sophia storms out in anguish")
]

WALK = [
    (0, None,
     "'Our seats are there, in the middle.' Gabriel directs Sophia to their assigned spots. "
     "The prepositional phrase 'au milieu' indicates location midway in the row."),
    (1, None,
     "'It is settled, I will not win.' Sophia jumps to a grim conclusion instantly. "
     "The idiom 'c'est regle' means the matter is settled or decided."),
    (2, None,
     "'Why do you say that so quickly, Sophia?' Gabriel tries to understand her sudden panic. "
     "The interrogative adverb 'pourquoi' inquires about her negative logic."),
    (3, None,
     "'Because we are in the middle!' Sophia points out the inconvenient seat positioning. "
     "The conjunction 'parce que' introduces an explanation for her superstition."),
    (4, None,
     "'That changes nothing about the vote.' Gabriel argues that seating does not dictate ballots. "
     "The negative structure 'ne... rien' means nothing at all."),
    (5, None,
     "'The winners are always on the end!' Sophia refers to traditional TV gala logistics. "
     "The phrase 'en bout' refers to aisle seating near the exits."),
    (6, None,
     "'Stop stressing and just enjoy.' Gabriel tries to calm her rising agitation. "
     "The imperative 'arrete de stresser' advises letting go of tension."),
    (7, None,
     "'They are announcing female newcomer now.' Sophia watches the podium presenter. "
     "The category 'revelation feminine' designates the Best Female Newcomer prize."),
    (8, None,
     "'Listen closely to the opening of the envelope.' Gabriel awaits the official verdict. "
     "The noun 'enveloppe' refers to the sealed award result."),
    (9, None,
     "'Another actress won the trophy!' Sophia realizes her defeat as applause erupts. "
     "The verb 'remporter' means to take home or win a prize."),
    (10, None,
     "'Sophia, stay seated, do not leave!' Gabriel urgently attempts to avoid a scandal. "
     "The negative imperative 'ne pars pas' urges remaining in place."),
    (11, None,
     "'I did not win, I am leaving.' Sophia refuses to witness the winner's victory speech. "
     "The present verb 'pars' asserts an immediate exit."),
    (12, None,
     "'That is too impulsive a reaction, wait!' Gabriel warns her about media optics. "
     "The adjective 'impulsive' describes acting without reflection."),
    (13, None,
     "'I refuse to sit here!' Sophia walks past the seated guests into the corridor. "
     "The verb 'refuser' followed by an infinitive indicates firm defiance.")
]

OUTRO = (
    "Devastated by losing the Cesar, Sophia flees the grand auditorium in heartbreak. "
    "As Gabriel rushes after his star client, ASK faces another sudden crisis on French cinema's biggest night. "
    "Now let's listen to the scene one last time in French."
)

CLOSING = ("lea", "Je refuse de rester assise ici!")
