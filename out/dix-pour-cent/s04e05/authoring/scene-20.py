# Authoring module for dix-pour-cent s04e05 scene 20 (cues 774-806).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-20.py --out overhear-content/out/dix-pour-cent/s04e05/scene-20.json

ID = "dix-pour-cent-s04e05-scene-20"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 20
TITLE = "Le déjeuner improvisé  (The Impromptu Lunch)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "distributeur": "theo"}
LABELS = {"lea": "Sigourney", "distributeur": "Le distributeur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 774-806. Sigourney Weaver and Guillaume confront the reluctant distributor at his regular restaurant "
    "table, winning over the entire dining room to prove that a romance between an older woman and a younger man "
    "is completely credible."
)

INTRO = (
    "Sigourney Weaver and Guillaume track down the film's distributor during his family lunch at a busy restaurant. "
    "When he claims no one will believe a romance between an older woman and a younger man, Sigourney rallies the whole dining room. "
    "Let's listen to their lively confrontation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Il déjeune ici tous les jours!",
     "He has lunch here every day!",
     [(774, "Il déjeune ici tous les jours")], "Sigourney spots the distributor in the restaurant"),
    ("distributeur", "Miss Weaver? Que faites-vous ici?",
     "Miss Weaver? What are you doing here?",
     [(780, "Miss Weaver ? Que faites-vous ici")], "The distributor looks up in shock"),
    ("distributeur", "J'ai signé pour un autre film.",
     "I signed on for a different movie.",
     [(782, "J'ai signé pour un film")], "The distributor defends his withdrawal"),
    ("lea", "Mais non, c'est le même film!",
     "Of course not, it is the same movie!",
     [(784, "C'est le même film")], "Sigourney counters firmly"),
    ("lea", "On a juste inversé deux rôles.",
     "We just switched two roles.",
     [(784, "On a juste inversé deux rôles")], "Sigourney explains the change"),
    ("distributeur", "Désolé, mais je n'y crois plus.",
     "Sorry, but I do not believe in it anymore.",
     [(785, "je n'y crois plus")], "The distributor shakes his head"),
    ("lea", "Qu'est-ce que vous ne croyez pas?",
     "What do you not believe?",
     [(786, "Qu'est-ce que vous ne croyez pas")], "Sigourney challenges him directly"),
    ("lea", "C'est une belle histoire d'amour!",
     "It is a beautiful love story!",
     [(790, "C'est une histoire d'amour")], "Sigourney appeals to the dining room"),
    ("lea", "Un homme jeune aime une femme mûre.",
     "A young man loves a mature woman.",
     [], "Sigourney describes the plot to the guests"),
    ("distributeur", "Personne ne va croire à cette histoire!",
     "Nobody is going to believe this story!",
     [], "The distributor objects"),
    ("lea", "Regardez, tout le restaurant adore l'idée!",
     "Look, the whole restaurant loves the idea!",
     [], "The other diners applaud in support"),
    ("distributeur", "Bon, d'accord, c'est très crédible!",
     "Well, all right, it is very credible!",
     [(801, "crédible")], "The distributor gives in to the crowd"),
    ("lea", "Attendez, d'abord on signe les contrats!",
     "Wait, first we sign the contracts!",
     [(803, "Attendez"), (804, "D'abord, on signe les contrats")], "Sigourney pulls out the paperwork"),
    ("distributeur", "Oui, bien sûr, c'est une bonne idée.",
     "Yes, of course, that is a good idea.",
     [(805, "Bonne idée"), (806, "Bien sûr")], "The distributor agrees to sign"),
]

WALK = [
    (0, None,
     "'He has lunch here every day!' Sigourney enters the restaurant and spots their target immediately. "
     "The phrase 'tous les jours' means every day."),
    (1, None,
     "'Miss Weaver? What are you doing here?' The distributor is stunned to see the Hollywood star at his table. "
     "The formal question 'que faites-vous' asks what are you doing."),
    (2, None,
     "'I signed on for a different movie.' He complains that the project has changed since his original agreement. "
     "The past tense 'j'ai signe' comes from 'signer'."),
    (3, None,
     "'Of course not, it is the same movie!' Sigourney insists that the core story remains unchanged. "
     "The expression 'le meme' means the same."),
    (4, None,
     "'We just switched two roles.' She explains that only the ages of the two lovers were reversed. "
     "The past participle 'inverse' means switched or inverted."),
    (5, None,
     "'Sorry, but I do not believe in it anymore.' The distributor expresses doubt about the new setup. "
     "The negative structure 'ne ... plus' means no longer."),
    (6, None,
     "'What do you not believe?' Sigourney challenges him to explain his objection out loud. "
     "The verb 'croire' means to believe."),
    (7, None,
     "'It is a beautiful love story!' Sigourney pitches the romance to the nearby tables. "
     "The compound noun 'histoire d'amour' means love story."),
    (8, None,
     "'A young man loves a mature woman.' She summarizes the premise to the curious diners around them. "
     "The adjective 'mure' means mature."),
    (9, None,
     "'Nobody is going to believe this story!' The distributor argues that audiences will find it unrealistic. "
     "The negative pronoun 'personne ne' means nobody."),
    (10, None,
     "'Look, the whole restaurant loves the idea!' Several guests share their own age-gap romances in support. "
     "The verb 'adorer' means to love or adore."),
    (11, None,
     "'Well, all right, it is very credible!' Outnumbered by the enthusiastic diners, the distributor relents. "
     "The adjective 'credible' means believable."),
    (12, None,
     "'Wait, first we sign the contracts!' Sigourney makes sure to lock in the deal on the spot. "
     "The adverb 'd'abord' means first of all."),
    (13, None,
     "'Yes, of course, that is a good idea.' The distributor takes out his pen to sign the agreement. "
     "The feminine noun 'idee' means idea."),
]

OUTRO = (
    "With the entire restaurant cheering her on, Sigourney Weaver convinces the distributor to sign the new contracts right at his table. "
    "The film is officially saved thanks to her bold charm. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Vive le cinéma français!")
