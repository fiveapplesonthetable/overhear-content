# Authoring module for dix-pour-cent s02e05 scene 16 (cues 445-473).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e05/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s02e05/scene-16.json

ID = "dix-pour-cent-s02e05-scene-16"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 16
TITLE = "La dame de France 2  (The France 2 Lady)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "guy": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Élisabeth", "guy": "Guy Marchand", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 445-473. On the movie set, Guy and Gabriel meet Elisabeth Lecoeur from France 2 Cinéma. "
    "Learning that the network decides tomorrow on funding Julien Doré's film, Gabriel invites her to lunch."
)

INTRO = (
    "On the movie set, veteran actor Guy Marchand finishes a take and meets Elisabeth Lecoeur, an executive from France 2 Cinema. "
    "When Elisabeth reveals that a committee meets tomorrow to decide on funding Julien Dore's project, Gabriel seizes the opportunity to invite her to lunch. "
    "Listen to the scene in French first."
)

STORY = [
    ("guy", "Tout va très bien, merci!",
     "Everything is going very well, thanks!",
     [(445, "Oui, très bien")], ""),
    ("lea", "Bravo Guy, quel beau rôle!",
     "Bravo Guy, what a wonderful role!",
     [(449, "Bravo, Guy ! Quel beau rôle")], ""),
    ("lea", "Élisabeth Lecœur, de France 2 Cinéma.",
     "Elisabeth Lecoeur, from France 2 Cinema.",
     [(450, "Élisabeth Lecœur, France 2 Cinéma")], ""),
    ("guy", "Enchanté! Gabriel Sarda est mon agent.",
     "Delighted! Gabriel Sarda is my agent.",
     [(450, "Enchanté"), (451, "Gabriel Sarda, mon agent")], ""),
    ("lea", "France 2 finance ce beau film.",
     "France 2 is financing this fine film.",
     [(453, "France 2 finance le film")], ""),
    ("guy", "C'est normal, c'est votre argent!",
     "It is normal, it is your money!",
     [(455, "c'est votre argent")], ""),
    ("gabriel", "Voilà, vous connaissez Guy Marchand!",
     "There, you know Guy Marchand!",
     [(458, "vous avez rencontré Guy Marchand")], ""),
    ("lea", "J'ai vraiment adoré le scénario.",
     "I really loved the screenplay.",
     [(460, "J'ai adoré le scénario")], ""),
    ("gabriel", "Et notre réalisateur est très talentueux.",
     "And our director is very talented.",
     [(462, "un jeune réalisateur très talentueux")], ""),
    ("lea", "Et comment va Julien Doré?",
     "And how is Julien Dore doing?",
     [(463, "comment va Julien Doré")], ""),
    ("lea", "La commission se réunit demain.",
     "The committee meets tomorrow.",
     [(466, "La commission se réunit demain")], ""),
    ("lea", "On décide si on finance son film.",
     "We decide whether we finance his film.",
     [(467, "si on finance son film")], ""),
    ("gabriel", "Là, je stresse beaucoup!",
     "Now, I am stressing a lot!",
     [(468, "Là je stresse")], ""),
    ("gabriel", "Vous êtes pressée ce midi?",
     "Are you in a hurry this noon?",
     [(472, "Vous êtes pressée")], ""),
    ("gabriel", "Je peux vous inviter à déjeuner?",
     "Can I invite you to lunch?",
     [(473, "Je pourrais peut-être vous inviter à déjeuner")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Everything is going very well, thanks!' Guy reassures everyone on set after finishing his take. "
     "The adverbial phrase indicates optimal condition."),
    (1, None,
     "'Bravo Guy, what a wonderful role!' Elisabeth praises the actor's performance on the soundstage. "
     "The exclamatory adjective expresses high admiration."),
    (2, None,
     "'Elisabeth Lecoeur, from France 2 Cinema.' She introduces herself as a key television financing executive. "
     "The proper noun phrase specifies her network branch."),
    (3, None,
     "'Delighted! Gabriel Sarda is my agent.' Guy introduces Gabriel to the executive. "
     "The polite greeting formula acknowledges an introduction."),
    (4, None,
     "'France 2 is financing this fine film.' Elisabeth confirms the television network's financial backing. "
     "The transitive verb denotes capital support."),
    (5, None,
     "'It is normal, it is your money!' Guy delivers a witty quip about television funding. "
     "The possessive determiner highlights financial contribution."),
    (6, None,
     "'There, you know Guy Marchand!' Gabriel smiles at his client's dry humor. "
     "The demonstrative adverb concludes the introduction."),
    (7, None,
     "'I really loved the screenplay.' Elisabeth compliments the writing of the movie. "
     "The evaluative verb expresses enthusiastic approval."),
    (8, None,
     "'And our director is very talented.' Gabriel praises the creative team behind the camera. "
     "The qualifying adjective underlines artistic skill."),
    (9, None,
     "'And how is Julien Dore doing?' Elisabeth asks about the quirky singer-turned-director. "
     "The interrogative adverb inquires after personal wellbeing."),
    (10, None,
     "'The committee meets tomorrow.' She reveals the timing of the funding decision. "
     "The temporal adverb indicates imminent review."),
    (11, None,
     "'We decide whether we finance his film.' The commission will vote on Julien's project. "
     "The conditional conjunction introduces the funding question."),
    (12, None,
     "'Now, I am stressing a lot!' Gabriel feels immediate agent anxiety over the verdict. "
     "The reflexive verb conveys acute pressure."),
    (13, None,
     "'Are you in a hurry this noon?' Gabriel looks for an opening to lobby her informally. "
     "The temporal noun phrase targets the lunch hour."),
    (14, None,
     "'Can I invite you to lunch?' Gabriel seizes the chance to pitch and connect over food. "
     "The polite modal verb proposes a midday meeting.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "After introducing Guy Marchand to Elisabeth Lecoeur, Gabriel uses the chance encounter to invite the television executive to lunch. "
    "Listen to the conversation once more in French."
)

CLOSING = ("gabriel", "Je connais un très bon bistrot juste à côté.")
