# Authoring module for dix-pour-cent s03e04 scene 11 (cues 694-698).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e04/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s03e04/scene-11.json

ID = "dix-pour-cent-s03e04-scene-11"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 11
TITLE = "Après le direct  (After the Live Show)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Isabelle Huppert", "mathias": "Mathias Barneville"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 694-698. Rushing out of the Radio France studio after her live interview with Laure Adler, "
    "Isabelle checks with Mathias on how her performance went. Mathias hurries her through the corridors "
    "to get back to the car before the American film set notices their absence. Adapted for A1 French."
)

INTRO = (
    "Directly after finishing her live radio interview with Laure Adler, Isabelle and Mathias hurry through the labyrinth of corridors. "
    "As Mathias rushes toward the exit, Isabelle wants to know how her performance came across. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
    ("mathias", "Dépêchez-vous, nous devons partir vite!",
     "Hurry up, we must leave quickly!",
     [(694, "Je passe devant")], "Urging swift exit"),
    ("mathias", "Je passe devant pour ouvrir la porte.",
     "I am going ahead to open the door.",
     [(694, "Je passe devant")], "Leading through corridors"),
    ("lea", "Alors, comment était mon interview en direct?",
     "So, how was my live interview?",
     [(696, "Ça allait ? J'étais bien ?")], "Asking about broadcast"),
    ("lea", "Est-ce que ça allait bien?",
     "Did it go well?",
     [(696, "Ça allait ?")], "Checking performance"),
    ("lea", "J'étais bien au micro ce soir?",
     "Was I good on the microphone tonight?",
     [(696, "J'étais bien ?")], "Inquiring about delivery"),
    ("mathias", "Sans doute, vous étiez très brillante.",
     "No doubt, you were very brilliant.",
     [(697, "Sans doute")], "Reassuring client"),
    ("lea", "C'est formidable, Laure a adoré.",
     "That is wonderful, Laure loved it.",
     [(698, "C'est formidable")], "Expressing satisfaction"),
    ("mathias", "Mais maintenant, le tournage américain nous attend.",
     "But now, the American shoot is waiting for us.",
     [(699, "Il est où, Gary ?")], "Reminding of movie set"),
    ("mathias", "Le réalisateur Gary va perdre patience.",
     "Director Gary is going to lose patience.",
     [(699, "Gary")], "Warning about director"),
    ("lea", "Ne paniquez pas, nous avons du temps.",
     "Do not panic, we have time.",
     [(696, "Ça allait ?")], "Dismissing anxiety"),
    ("mathias", "La voiture est garée juste en bas.",
     "The car is parked right downstairs.",
     [(694, "Je passe devant")], "Pointing to vehicle"),
    ("mathias", "Isabelle, montez vite à l'arrière!",
     "Isabelle, get quickly into the back!",
     [(694, "Je passe devant")], "Directing into car"),
    ("lea", "Allons-y, je suis prête pour Gary.",
     "Let us go, I am ready for Gary.",
     [(699, "Il est où, Gary ?")], "Heading to set"),
]

WALK = [
    (0, None,
     "'Hurry up, we must leave quickly!' Mathias urges Isabelle to move fast. "
     "The imperative 'depechez-vous' commands prompt action."),
    (1, None,
     "'I am going ahead to open the door.' Mathias takes the lead through the studio hallways. "
     "The phrase 'passer devant' means to go in front or take the lead."),
    (2, None,
     "'So, how was my live interview?' Isabelle seeks immediate feedback on her appearance. "
     "The interrogative adverb 'comment' asks for an opinion or manner."),
    (3, None,
     "'Did it go well?' Isabelle wonders whether the broadcast ran smoothly. "
     "The imperfect form 'allait' describes past ongoing status."),
    (4, None,
     "'Was I good on the microphone tonight?' Isabelle focuses on her personal delivery. "
     "The adjective 'bien' acts adverbially here to mean effective or skilled."),
    (5, None,
     "'No doubt, you were very brilliant.' Mathias reassures her with quick praise. "
     "The phrase 'sans doute' means without doubt or probably."),
    (6, None,
     "'That is wonderful, Laure loved it.' Isabelle rejoices in the successful broadcast. "
     "The adjective 'formidable' means wonderful or tremendous."),
    (7, None,
     "'But now, the American shoot is waiting for us.' Mathias pivots back to their primary obligation. "
     "The noun 'tournage' denotes a film shoot."),
    (8, None,
     "'Director Gary is going to lose patience.' Mathias warns about tensions on the movie set. "
     "The idiom 'perdre patience' means to lose one's temper or become impatient."),
    (9, None,
     "'Do not panic, we have time.' Isabelle remains calm under pressure. "
     "The negative imperative 'ne paniquez pas' soothes someone's worry."),
    (10, None,
     "'The car is parked right downstairs.' Mathias guides her toward their transport. "
     "The past participle 'garee' means parked."),
    (11, None,
     "'Isabelle, get quickly into the back!' Mathias hurries her inside the vehicle. "
     "The phrase 'a l'arriere' specifies the back seat."),
    (12, None,
     "'Let us go, I am ready for Gary.' Isabelle embraces the next challenge of the night. "
     "The imperative 'allons-y' urges departure."),
]

OUTRO = (
    "Mathias successfully bundles Isabelle into the car, racing across the night to reach the American production on time. "
    "Next stop: Gary's film set. "
    "Now let's listen to the scene once more."
)

CLOSING = ("lea", "Allons-y, je suis prête pour Gary.")
