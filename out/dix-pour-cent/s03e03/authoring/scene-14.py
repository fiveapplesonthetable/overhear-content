# Authoring module for dix-pour-cent s03e03 scene 14 (cues 592-736).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e03/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s03e03/scene-14.json

ID = "dix-pour-cent-s03e03-scene-14"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 14
TITLE = "Les essais de Samy  (Samy's Screen Test)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "theo", "samy": "marcel"}
LABELS = {"lea": "Emma", "gerard": "Gérard Lanvin", "samy": "Samy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 592-736. In the studio costume room, eager newcomer Samy arrives for a screen test with star Gérard Lanvin, "
    "while director Emma observes the pairing between the veteran and the newcomer."
)

INTRO = (
    "At the movie studio costume workshop, enthusiastic young actor Samy arrives for his first major audition. "
    "Meeting established star Gerard Lanvin, he hopes for a full costume, while director Emma watches their chemistry closely. "
    "Listen to the scene in French first."
)

STORY = [
    ("samy", "Bonjour, Gérard. Bonjour, madame.",
     "Hello, Gerard. Hello, ma'am.",
     [(620, "Bonjour, Gérard"), (621, "Bonjour, madame")], ""),
    ("samy", "Je suis venu passer des essais.",
     "I came to do some screen tests.",
     [(623, "Je suis venu passer des essais")], ""),
    ("lea", "Ne t'inquiète pas, on a tout.",
     "Do not worry, we have everything.",
     [(626, "On a tout ce qu'il faut")], ""),
    ("samy", "Excusez-moi, j'ai une question.",
     "Excuse me, I have a question.",
     [(629, "Excusez-moi, madame, juste une question")], ""),
    ("samy", "Est-ce possible d'avoir un costume?",
     "Is it possible to have a costume?",
     [(630, "possible d'avoir un costume")], ""),
    ("lea", "Ce n'est pas habituel pour des essais.",
     "That is not typical for an audition.",
     [(633, "ça se fait pas vraiment")], ""),
    ("samy", "Je ne connais personne dans le cinéma.",
     "I do not know anyone in cinema.",
     [(644, "je connais personne dans le milieu de cinéma")], ""),
    ("samy", "Je ne sais pas comment vous remercier.",
     "I do not know how to thank you.",
     [(645, "Je sais pas comment vous remercier")], ""),
    ("gerard", "Montre ton talent, mon grand.",
     "Show your talent, my boy.",
     [(646, "bon, mon grand")], ""),
    ("lea", "Gérard, restez pour les essais de Samy.",
     "Gerard, please stay for Samy's test.",
     [(654, "j'aimerais bien que vous restiez pour les essais de Samy")], ""),
    ("gerard", "D'accord, je peux rester un peu.",
     "Alright, I can stay for a bit.",
     [(655, "bon, ben oui, d'accord")], ""),
    ("lea", "Je veux voir si cela marche ensemble.",
     "I want to see if it works together.",
     [(656, "vous voir ensemble"), (657, "voir si ça marche")], ""),
    ("gerard", "Vous avez peur du contraste d'âge?",
     "Are you afraid of the age contrast?",
     [(658, "Vous avez peur")], ""),
    ("lea", "Non, j'adore l'expérience face à la vitalité.",
     "No, I love experience facing fresh energy.",
     [(663, "j'adore l'expérience face à la vitalité")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Hello, Gerard. Hello, ma'am.' Samy arrives at the screen test studio. "
     "The polite greetings address both the star and the director."),
    (1, None,
     "'I came to do some screen tests.' The newcomer introduces his purpose at the casting office. "
     "The compound past verb states his reason for arriving."),
    (2, None,
     "'Do not worry, we have everything.' Emma reassures the young actor about wardrobe preparations. "
     "The reassuring negative imperative puts him at ease."),
    (3, None,
     "'Excuse me, I have a question.' Samy asks for permission to make a special request. "
     "The polite formula prefaces his inquiry."),
    (4, None,
     "'Is it possible to have a costume?' He wonders if full wardrobe is available for an audition. "
     "The inversion question asks about equipment."),
    (5, None,
     "'That is not typical for an audition.' Emma clarifies standard casting procedures. "
     "The negative construction explains normal industry practice."),
    (6, None,
     "'I do not know anyone in cinema.' Samy confides his complete lack of insider connections. "
     "The negative verb emphasizes his humble background."),
    (7, None,
     "'I do not know how to thank you.' He expresses deep gratitude to Gerard for the audition. "
     "The modal statement reveals genuine appreciation."),
    (8, None,
     "'Show your talent, my boy.' Gerard encourages the nervous candidate to perform his best. "
     "The direct imperative offers seasoned advice."),
    (9, None,
     "'Gerard, please stay for Samy's test.' Emma requests the star's presence during the reading. "
     "The polite imperative asks for his cooperation."),
    (10, None,
     "'Alright, I can stay for a bit.' Gerard agrees to lend a hand to the young newcomer. "
     "The consenting response shows professional generosity."),
    (11, None,
     "'I want to see if it works together.' Emma explains her directorial intention for the camera test. "
     "The expression of purpose describes visual chemistry."),
    (12, None,
     "'Are you afraid of the age contrast?' Gerard asks whether the age difference seems problematic. "
     "The direct question seeks artistic clarification."),
    (13, None,
     "'No, I love experience facing fresh energy.' Emma praises the compelling dynamic between veteran and newcomer. "
     "The affirmative verb highlights creative contrast.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Pairing a veteran actor with a hungry newcomer brings sparks of creative tension to the audition stage. "
    "Listen to the conversation once more in French."
)

CLOSING = ("gerard", "On verra bien ce que ça donne.")
