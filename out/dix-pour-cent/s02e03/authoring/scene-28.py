# Authoring module for dix-pour-cent s02e03 scene 28 (cues 722-732).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-28.py --out out/dix-pour-cent/s02e03/scene-28.json

ID = "dix-pour-cent-s02e03-scene-28"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 28
TITLE = "Sofia en studio  (Sofia Sings)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julien": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Sofia", "julien": "Julien", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 722-732. In the recording studio, Sofia Leprince performs alongside pop singer Julien Doré. "
    "Julien is astonished by her breathtaking vocal talent and agrees enthusiastically to record a song "
    "with her, while Gabriel looks on with pride. Adapted for A1 French."
)

INTRO = (
    "In a professional music studio, Sofia Leprince steps up to the microphone with Julien Dore. "
    "Her stunning singing voice leaves the famous musician completely amazed. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("julien", "C'est beau, non?",
     "It is beautiful, is it not?",
     [(722, "C'est beau, non ?")], ""),
    ("lea", "Oui, c'est vraiment très beau.",
     "Yes, it is really very beautiful.",
     [(723, "Oui, c'est beau.")], "Added vraiment très"),
    ("julien", "Tu as une voix magnifique.",
     "You have a magnificent voice.",
     [], "Julien praising voice"),
    ("lea", "Merci, c'est gentil.",
     "Thank you, that is kind.",
     [(724, "Merci.")], "Added c'est gentil"),
    ("julien", "Bravo, c'était vraiment bien.",
     "Bravo, that was really good.",
     [(726, "Bravo !"), (727, "Vraiment bien.")], "Combined lines"),
    ("lea", "Merci beaucoup, Julien.",
     "Thank you very much, Julien.",
     [(725, "Merci beaucoup.")], "Added Julien"),
    ("julien", "C'est génial, j'adore cette mélodie.",
     "It is awesome, I love this melody.",
     [(728, "Génial.")], "Added j'adore cette mélodie"),
    ("gabriel", "La voix de Sofia est incroyable.",
     "Sofia's voice is incredible.",
     [(730, "La voix de Sofia est incroyable.")], ""),
    ("julien", "Oui, elle a un timbre unique.",
     "Yes, she has a unique timbre.",
     [(731, "Ouais.")], "Added timbre unique"),
    ("gabriel", "Je vous l'avais dit!",
     "I had told you so!",
     [(731, "Je vous l'avais dit.")], ""),
    ("julien", "Je suis époustouflé par sa prestation.",
     "I am blown away by her performance.",
     [(732, "Je suis époustouflé.")], "Added par sa prestation"),
    ("lea", "Je suis très heureuse de chanter avec vous.",
     "I am very happy to sing with you.",
     [], "Sofia grateful response"),
    ("julien", "Nous allons faire un disque formidable.",
     "We are going to make a wonderful record.",
     [], "Julien future project"),
    ("gabriel", "C'est le début d'un grand succès.",
     "It is the beginning of a great success.",
     [], "Gabriel conclusion"),
]

OPENER = "Let's examine how Julien and Gabriel are praising Sofia's musical performance."

WALK = [
    (0, None,
     "'It is beautiful, is it not?' A short tag question inviting confirmation."),
    (1, None,
     "'Yes, it is really very beautiful.' An enthusiastic affirmative response."),
    (2, None,
     "'You have a magnificent voice.' A direct compliment on her vocal ability."),
    (3, None,
     "'Thank you, that is kind.' A modest and gracious response to praise."),
    (4, None,
     "'Bravo, that was really good.' An exclamation followed by an imperfect description."),
    (5, None,
     "'Thank you very much, Julien.' A polite formula including the musician's name."),
    (6, None,
     "'It is awesome, I love this melody.' The adjective genial followed by a verb of affection."),
    (7, None,
     "'Sofia's voice is incredible.' Gabriel points out Sofia's unique talent."),
    (8, None,
     "'Yes, she has a unique timbre.' A musical observation regarding vocal tone."),
    (9, None,
     "'I had told you so!' The pluperfect tense recalling an earlier prediction."),
    (10, None,
     "'I am blown away by her performance.' The colourful adjective epoustoufle meaning astonished."),
    (11, None,
     "'I am very happy to sing with you.' An expression of happiness followed by de and an infinitive."),
    (12, None,
     "'We are going to make a wonderful record.' The near future tense announcing a joint album."),
    (13, None,
     "'It is the beginning of a great success.' Gabriel predicts a bright future."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Sofia has dazzled Julien Dore in the recording studio, opening the door to a music career. "
    "Gabriel watches with joy as Sofia's artistic dream begins to take flight."
)

CLOSING = ("lea", "Merci à tous les deux!")
