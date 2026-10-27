# Authoring module for dix-pour-cent s03e02 scene 13 (cues 735-756).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s03e02/scene-13.json

ID = "dix-pour-cent-s03e02-scene-13"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 13
TITLE = "Chez Monica Bellucci  (At Monica Bellucci's)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "marcel"}
LABELS = {"lea": "Monica Bellucci", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 735-756. At Monica Bellucci's home, Monica and Gabriel review heavily retouched ad photos; "
    "Monica confides how much she cherishes Gabriel's kind look, while Gabriel maintains professional boundaries."
)

INTRO = (
    "At her Parisian apartment, Italian cinema star Monica Bellucci reviews proofs of a high-end advertising campaign with agent Gabriel Sarda. "
    "She criticizes the excessive digital retouching, while warmly praising Gabriel's gentle and supportive presence. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Alors, que penses-tu de ces photos?",
     "So, what do you think of these photos?",
     [(735, "Alors")], ""),
    ("gabriel", "La publicité, ce n'est pas le cinéma.",
     "Advertising is not cinema.",
     [(736, "la pub, c'est pas le cinéma")], ""),
    ("gabriel", "Ce sont des codes très différents.",
     "These are very different codes.",
     [(737, "d'autres codes")], ""),
    ("lea", "Tu sais très bien ce qui te plaît.",
     "You know very well what pleases you.",
     [(738, "ce qui te plaît")], ""),
    ("lea", "Ici, ce n'est pas du tout excitant.",
     "Here, this is not exciting at all.",
     [(740, "pas du tout excitant")], ""),
    ("gabriel", "Si, c'est quand même un peu excitant!",
     "Well, it is still a little bit exciting!",
     [(741, "un peu quand même")], ""),
    ("lea", "Franchement, c'est qui cette femme?",
     "Honestly, who is this woman?",
     [(742, "c'est qui, cette dame")], ""),
    ("lea", "Cette image est tellement retouchée!",
     "This image is so heavily retouched!",
     [(743, "C'est tellement retouché")], ""),
    ("lea", "Je n'ai plus aucune expression naturelle.",
     "I no longer have any natural expression.",
     [(743, "J'ai pas d'expression")], ""),
    ("lea", "Regarde, je n'ai même plus de coudes!",
     "Look, I do not even have elbows anymore!",
     [(745, "plus des coudes, regarde")], ""),
    ("gabriel", "C'est rare qu'on te regarde les coudes.",
     "People rarely look at your elbows.",
     [(746, "dans les coudes")], ""),
    ("lea", "Moi, j'aime bien comment tu me regardes.",
     "Personally, I really like how you look at me.",
     [(747, "comment toi, tu me regardes")], ""),
    ("lea", "Ton regard est toujours bon et doux.",
     "Your gaze is always kind and gentle.",
     [(749, "bon et doux")], ""),
    ("lea", "Avec toi, je me sens en confiance.",
     "With you, I feel confident and safe.",
     [(750, "j'ai confiance")], ""),
    ("gabriel", "Je suis archi-flatté, mais c'est tabou.",
     "I am extremely flattered, but it is taboo.",
     [(752, "archi-flaté"), (755, "Juste tabou")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'So, what do you think of these photos?' Monica asks for Gabriel's honest professional feedback. "
     "The interrogative phrase opens the review."),
    (1, None,
     "'Advertising is not cinema.' Gabriel distinguishes commercial promo aesthetics from films. "
     "The negative copula defines separate media."),
    (2, None,
     "'These are very different codes.' He notes that advertising operates by artificial standards. "
     "The plural demonstrative clause describes marketing conventions."),
    (3, None,
     "'You know very well what pleases you.' Monica challenges him to judge purely as an observer. "
     "The relative clause addresses his personal perception."),
    (4, None,
     "'Here, this is not exciting at all.' She expresses dissatisfaction with the clinical studio shots. "
     "The negative adverbial phrase stresses complete indifference."),
    (5, None,
     "'Well, it is still a little bit exciting!' Gabriel gently disagrees with her harsh self-critique. "
     "The contradictory affirmative particle qualifies her statement."),
    (6, None,
     "'Honestly, who is this woman?' Monica feels alienated by the synthetic marketing image. "
     "The rhetorical question highlights identity disconnection."),
    (7, None,
     "'This image is so heavily retouched!' She decries the aggressive digital post-production. "
     "The intensifying adverb emphasizes synthetic alteration."),
    (8, None,
     "'I no longer have any natural expression.' Monica laments the erasure of authentic human facial traits. "
     "The negative adverb denotes complete loss."),
    (9, None,
     "'Look, I do not even have elbows anymore!' She points out ridiculous anatomical airbrushing. "
     "The imperative verb draws attention to the flaw."),
    (10, None,
     "'People rarely look at your elbows.' Gabriel offers humor to lighten her frustration. "
     "The impersonal construction brings amusing perspective."),
    (11, None,
     "'Personally, I really like how you look at me.' Monica pivots to an intimate personal compliment. "
     "The emphatic pronoun phrase signals emotional warmth."),
    (12, None,
     "'Your gaze is always kind and gentle.' She appreciates his sincere, non-predatory attention. "
     "The coordinated adjectives describe comforting affection."),
    (13, None,
     "'With you, I feel confident and safe.' Monica expresses profound trust in her dedicated agent. "
     "The prepositional phrase reinforces emotional security."),
    (14, None,
     "'I am extremely flattered, but it is taboo.' Gabriel acknowledges her affection while upholding professional ethics. "
     "The contrasting conjunction sets a firm moral limit.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Sharing an intimate conversation over photo proofs, Monica Bellucci and Gabriel bond over the contrast between glamour and authenticity. "
    "Listen to the conversation once more in French."
)

CLOSING = ("gabriel", "Restons de simples partenaires professionnels.")
