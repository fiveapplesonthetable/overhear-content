# Authoring module for dix-pour-cent s02e03 scene 13 (cues 310-352).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e03/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s02e03/scene-13.json

ID = "dix-pour-cent-s02e03-scene-13"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 13
TITLE = "L'échange de date  (Swapping Test Dates)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "norman": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Violaine", "norman": "Norman", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 310-352. Gabriel arranges for a fan named Violaine to swap her driving test date with Norman Thavaud in exchange for selfies."
)

INTRO = (
    "At the agency, Gabriel finds a creative solution for client Norman Thavaud, who desperately needs an earlier driving test date. "
    "A fan named Violaine agrees to swap slots in exchange for meeting the star and taking photos. "
    "Listen to the conversation in French first."
)

STORY = [
    ("gabriel", "J'ai trouvé quelqu'un pour échanger.",
     "I found someone to swap with you.",
     [(311, "J'ai trouvé quelqu'un pour échanger")], ""),
    ("norman", "Comment elle s'appelle?",
     "What is her name?",
     [(315, "Comment elle s'appelle")], ""),
    ("gabriel", "Elle s'appelle Violaine.",
     "Her name is Violaine.",
     [(315, "Violaine")], ""),
    ("norman", "Elle veut de l'argent?",
     "Does she want money?",
     [(316, "Elle veut de l'argent")], ""),
    ("gabriel", "Non, juste un selfie.",
     "No, just a selfie.",
     [(317, "Non, juste un selfie")], ""),
    ("norman", "Je passe le test quand?",
     "When do I take the test?",
     [(318, "Je passe le test quand")], ""),
    ("gabriel", "Demain, après qu'on voit Audiard.",
     "Tomorrow, after we see Audiard.",
     [(319, "Demain, après qu'on voit Audiard")], ""),
    ("norman", "Parfait. C'est une bonne nouvelle.",
     "Perfect. That is good news.",
     [(320, "Parfait")], ""),
    ("lea", "Salut Norman! C'est le plus beau jour de ma vie.",
     "Hi Norman! This is the best day of my life.",
     [(321, "Salut, Norman"), (323, "C'est le plus beau jour de ma vie")], ""),
    ("norman", "C'est gentil. Merci beaucoup.",
     "That is kind. Thank you very much.",
     [(324, "C'est gentil"), (326, "merci")], ""),
    ("lea", "On fait cette photo ensemble?",
     "Shall we take this photo together?",
     [(327, "on fait cette photo")], ""),
    ("lea", "Souriez pour la photo!",
     "Smile for the photo!",
     [(328, "Souriez")], ""),
    ("gabriel", "Violaine, c'est terminé. Merci!",
     "Violaine, we are done. Thank you!",
     [(341, "Violaine, c'est terminé. Merci")], ""),
    ("norman", "Il y a un problème?",
     "Is there a problem?",
     [(348, "Il y a un problème")], ""),
    ("gabriel", "Elle veut quelque chose de plus personnel.",
     "She wants something more personal.",
     [(349, "elle veut juste un souvenir"), (352, "quelque chose de plus personnel")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'I found someone to swap with you.' Gabriel announces his successful negotiation. "
     "The verb expresses swapping examination slots."),
    (1, None,
     "'What is her name?' Norman asks about the helpful volunteer. "
     "The pronominal verb s'appeler asks for a person's name."),
    (2, None,
     "'Her name is Violaine.' Gabriel introduces the fan by name. "
     "The third-person form elle s'appelle identifies the candidate."),
    (3, None,
     "'Does she want money?' Norman wonders what compensation she requires. "
     "The partitive article de l' precedes the noun argent."),
    (4, None,
     "'No, just a selfie.' Gabriel explains the simple terms of the agreement. "
     "The adverb juste limits the request to a digital photo."),
    (5, None,
     "'When do I take the test?' Norman checks his new examination slot. "
     "The interrogative adverb quand asks for timing."),
    (6, None,
     "'Tomorrow, after we see Audiard.' Gabriel confirms the convenient timing. "
     "The temporal conjunction introduces the subsequent action."),
    (7, None,
     "'Perfect. That is good news.' Norman breathes a sigh of relief. "
     "The adjective parfait conveys total satisfaction."),
    (8, None,
     "'Hi Norman! This is the best day of my life.' Violaine arrives completely starstruck. "
     "The superlative le plus beau marks an unforgettable milestone."),
    (9, None,
     "'That is kind. Thank you very much.' Norman responds warmly to his devoted fan. "
     "The demonstrative phrase c'est gentil expresses polite gratitude."),
    (10, None,
     "'Shall we take this photo together?' She eagerly pulls out her camera phone. "
     "The pronoun on is used colloquially for a collective suggestion."),
    (11, None,
     "'Smile for the photo!' She prepares to capture the memorable moment. "
     "The imperative souriez addresses the star respectfully."),
    (12, None,
     "'Violaine, we are done. Thank you!' Gabriel gently steps in to conclude the visit. "
     "The past participle signals that time has run out."),
    (13, None,
     "'Is there a problem?' Norman senses an awkward hitch in the plan. "
     "The fixed expression il y a is used in question form."),
    (14, None,
     "'She wants something more personal.' Gabriel hints that she expects an unusual keepsake. "
     "The comparative structure de plus personnel indicates an odd souvenir.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "With Norman's exam safely rescheduled, Gabriel must now manage an overenthusiastic fan who refuses to leave without a lock of hair. "
    "Listen to the French dialogue one more time."
)

CLOSING = ("gabriel", "Elle veut une mèche de cheveux!")
