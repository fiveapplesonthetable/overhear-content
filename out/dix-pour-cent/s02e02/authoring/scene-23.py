# Authoring module for dix-pour-cent s02e02 scene 23 (cues 780-800).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-23.py --out out/dix-pour-cent/s02e02/scene-23.json

ID = "dix-pour-cent-s02e02-scene-23"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 23
TITLE = "Dîner après le théâtre  (Dinner After the Theatre)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "fabrice": "theo"}
LABELS = {"lea": "Andréa", "fabrice": "Fabrice"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 780-800. Following his stage performance, Fabrice Luchini joins Andréa for dinner at a bistro. "
    "They praise each other's talents and discuss romance, right before a rival agent approaches their table."
)

INTRO = (
    "Following his brilliant theatrical performance, acclaimed actor Fabrice Luchini meets Andrea Martel for a late dinner. "
    "The pair exchange warm compliments and playful relationship advice in high spirits before their evening is interrupted. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("fabrice", "Bonsoir Andréa! Tu es très élégante.",
     "Good evening Andrea! You look very elegant.",
     [(783, "-Salut ! -Tu es très élégante")], ""),
    ("lea", "Merci Fabrice. Bravo pour ton spectacle!",
     "Thank you Fabrice. Bravo on your show!",
     [(784, "Merci. Et bravo ! C'était magnifique")], ""),
    ("lea", "C'était vraiment une pièce magnifique.",
     "It was truly a magnificent play.",
     [(784, "C'était magnifique")], ""),
    ("fabrice", "Tu as aimé ma prestation?",
     "Did you like my performance?",
     [(785, "-Tu as aimé ? -J'ai adoré")], ""),
    ("lea", "J'ai absolument adoré ton jeu.",
     "I absolutely loved your acting.",
     [(785, "-Tu as aimé ? -J'ai adoré")], ""),
    ("fabrice", "Et cette jeune femme blonde d'hier?",
     "And that young blonde woman from yesterday?",
     [(788, "Ta copine blonde d'hier soir ?")], ""),
    ("lea", "Non, ce n'est pas mon genre.",
     "No, she is not my type.",
     [(789, "Non, ce n'est pas elle")], ""),
    ("fabrice", "Elle te plaît beaucoup. Fonce!",
     "You like her very much. Go for it!",
     [(790, "Elle te plaît pourtant. Fonce !")], ""),
    ("lea", "Tu crois vraiment que ça marcherait?",
     "Do you really think that would work?",
     [(791, "Tu crois ?")], ""),
    ("fabrice", "C'est tout à fait évident!",
     "It is completely obvious!",
     [(792, "C'est évident")], ""),
    ("lea", "Je ne sais pas par où commencer.",
     "I do not know where to start.",
     [(795, "Je ne saurais pas par où commencer")], ""),
    ("fabrice", "Fais-moi confiance pour l'amour.",
     "Trust me when it comes to love.",
     [(796, "Fais-moi confiance, alors")], ""),
    ("fabrice", "On mange quelque chose maintenant?",
     "Shall we eat something now?",
     [(797, "-On mange ? -Oui")], ""),
    ("lea", "Oui, commandons un bon dîner.",
     "Yes, let us order a good dinner.",
     [(797, "-On mange ? -Oui")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Good evening Andrea! You look very elegant.' Fabrice greets Andrea warmly as they meet at the restaurant table. "
     "The adverb tres intensifies the adjective."),
    (1, None,
     "'Thank you Fabrice. Bravo on your show!' She immediately congratulates him on his stage performance. "
     "The interjection bravo expresses enthusiastic praise."),
    (2, None,
     "'It was truly a magnificent play.' Andrea highlights the beauty and depth of the production. "
     "The adverb vraiment adds genuine conviction."),
    (3, None,
     "'Did you like my performance?' The actor seeks her candid artistic reaction. "
     "The compound past tense tu as aime asks about past experience."),
    (4, None,
     "'I absolutely loved your acting.' She expresses unbounded admiration for his theatrical craft. "
     "The verb adorer indicates passionate enjoyment."),
    (5, None,
     "'And that young blonde woman from yesterday?' Fabrice turns the conversation to her romantic life. "
     "The noun phrase femme blonde describes the person in question."),
    (6, None,
     "'No, she is not my type.' Andrea brushes off the inquiry with a casual denial. "
     "The negative phrase ce n'est pas rejects the assumption."),
    (7, None,
     "'You like her very much. Go for it!' The actor playfully encourages her to take a bold chance on romance. "
     "The colloquial imperative fonce means go for it."),
    (8, None,
     "'Do you really think that would work?' She questions whether taking such an initiative is wise. "
     "The verb croire expresses personal belief."),
    (9, None,
     "'It is completely obvious!' Fabrice insists that the romantic connection is undeniable. "
     "The phrase tout a fait means completely or entirely."),
    (10, None,
     "'I do not know where to start.' Andrea admits feeling completely at a loss with dating. "
     "The interrogative phrase par ou asks which route or approach to take."),
    (11, None,
     "'Trust me when it comes to love.' He poses as an experienced philosopher of romantic relationships. "
     "The imperative fais-moi confiance asks for complete reliance."),
    (12, None,
     "'Shall we eat something now?' He suggests turning their attention to ordering food. "
     "The pronoun on is used colloquially for we."),
    (13, None,
     "'Yes, let us order a good dinner.' Andrea agrees happily to start their meal. "
     "The first-person plural imperative commandons proposes action together."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Fabrice Luchini and Andrea bond over theatrical art and romantic advice over dinner. "
    "Remember the colloquial French encouragement for seizing an opportunity: fonce."
)

CLOSING = ("lea", "Oui, commandons un bon dîner.")
