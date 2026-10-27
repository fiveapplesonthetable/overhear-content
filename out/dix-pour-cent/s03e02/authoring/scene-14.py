# Authoring module for dix-pour-cent s03e02 scene 14 (cues 757-775).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-14.py --out out/dix-pour-cent/s03e02/scene-14.json

ID = "dix-pour-cent-s03e02-scene-14"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 14
TITLE = "La panique de Gabriel  (Gabriel's Panic)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie"}
LABELS = {"lea": "Gabriel", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 757-775. After fleeing Monica Bellucci's apartment in a panic, Gabriel calls Andréa from a taxi "
    "to confess his distress and his feelings of inadequacy in front of the world-famous star."
)

INTRO = (
    "In a Parisian taxi late at night, talent agent Gabriel Sarda frantically calls his colleague Andrea Martel. "
    "Gabriel has just fled dinner at Monica Bellucci's apartment after panicking over her romantic interest in him. "
    "Listen to their conversation in French first."
)

STORY = [
    ("lea", "Andréa, j'ai besoin de te parler!",
     "Andrea, I need to talk to you!",
     [(759, "Non, mais Andréa, c'est la faute d'Hicham, putain.")], ""),
    ("andrea", "Où es-tu à cette heure tardive?",
     "Where are you at this late hour?",
     [(757, "Je vais faire pipi.")], ""),
    ("lea", "Je suis dans un taxi parisien.",
     "I am in a Parisian taxi.",
     [(780, "y a votre taxi qui est arrivé, là.")], ""),
    ("andrea", "Tu as quitté le dîner chez Monica?",
     "You left the dinner at Monica's?",
     [(762, "par Monica Bellucci.")], ""),
    ("lea", "Oui, c'est la faute d'Hicham!",
     "Yes, it is Hicham's fault!",
     [(759, "c'est la faute d'Hicham, putain.")], ""),
    ("andrea", "Pourquoi accuses-tu notre patron cette nuit?",
     "Why do you accuse our boss tonight?",
     [(760, "Il me fout une pression de ouf, aussi.")], ""),
    ("lea", "Il me met une pression énorme.",
     "He puts enormous pressure on me.",
     [(760, "Il me fout une pression de ouf, aussi.")], ""),
    ("andrea", "Monica Bellucci s'intéresse à toi, Gabriel!",
     "Monica Bellucci is interested in you, Gabriel!",
     [(761, "y a quand même pire que de se faire emballer"), (762, "par Monica Bellucci.")], ""),
    ("lea", "Il faut avoir confiance en soi.",
     "One must have confidence in oneself.",
     [(765, "Faut avoir bien confiance en soi.")], ""),
    ("andrea", "Ce n'est pas un drame affreux.",
     "That is not an awful drama.",
     [(761, "y a quand même pire")], ""),
    ("lea", "Pour moi, c'était un vrai cauchemar!",
     "For me, it was a real nightmare!",
     [(769, "C'était horrible.")], ""),
    ("andrea", "Que cherchait cette femme extraordinaire?",
     "What was this extraordinary woman looking for?",
     [(771, "cette femme, il lui faut un loup, quoi.")], ""),
    ("lea", "Il lui faut un animal sauvage!",
     "She needs a wild animal!",
     [(772, "Il lui faut un animal sauvage.")], ""),
    ("andrea", "Et comment te sentais-tu devant elle?",
     "And how did you feel in front of her?",
     [(773, "Et moi, j'étais là, là.")], "")
]

OPENER = "Let us examine how Gabriel confesses his panic to Andrea from the taxi."

WALK = [
    (0, None,
     "'Andrea, I need to talk to you!' Gabriel seeks immediate emotional comfort. "
     "The verbal idiom avoir besoin de expresses necessity."),
    (1, None,
     "'Where are you at this late hour?' Andrea wonders about his location. "
     "The interrogative adverb où asks where."),
    (2, None,
     "'I am in a Parisian taxi.' Gabriel reveals he is traveling alone. "
     "The masculine adjective parisien agrees with taxi."),
    (3, None,
     "'You left the dinner at Monica's?' Andrea expresses mild surprise. "
     "The compound past as quitté comes from quitter."),
    (4, None,
     "'Yes, it is Hicham's fault!' Gabriel shifts blame to his demanding boss. "
     "The noun phrase la faute de assigns responsibility."),
    (5, None,
     "'Why do you accuse our boss tonight?' Andrea questions his frantic reasoning. "
     "The interrogative adverb pourquoi asks why."),
    (6, None,
     "'He puts enormous pressure on me.' Gabriel explains his ongoing workplace stress. "
     "The feminine adjective énorme modifies pression."),
    (7, None,
     "'Monica Bellucci is interested in you, Gabriel!' Andrea highlights the flattering reality. "
     "The reflexive construction s'intéresser à means to be interested in."),
    (8, None,
     "'One must have confidence in oneself.' Gabriel admits his personal self-doubt. "
     "The reflexive pronoun soi functions as an impersonal referent."),
    (9, None,
     "'That is not an awful drama.' Andrea attempts to downplay the crisis. "
     "The negative structure ce n'est pas negates the noun phrase."),
    (10, None,
     "'For me, it was a real nightmare!' Gabriel describes his overwhelming anxiety. "
     "The masculine noun cauchemar means nightmare."),
    (11, None,
     "'What was this extraordinary woman looking for?' Andrea prompts him for details. "
     "The interrogative pronoun que asks what in inversion."),
    (12, None,
     "'She needs a wild animal!' Gabriel imagines her ideal partner. "
     "The masculine adjective sauvage describes wild beasts."),
    (13, None,
     "'And how did you feel in front of her?' Andrea inquires about his self-perception. "
     "The preposition devant denotes physical presence.")
]

TRANSITION = "Now let us listen to the phone conversation once more at normal pace."

OUTRO = (
    "In the quiet of a nighttime taxi, Gabriel confesses his deep insecurities about intimacy and romance. "
    "Listen to the dialogue once more in French."
)

CLOSING = ("lea", "Il lui faut un animal sauvage!")
