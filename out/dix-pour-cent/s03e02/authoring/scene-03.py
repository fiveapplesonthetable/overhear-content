# Authoring module for dix-pour-cent s03e02 scene 03 (cues 198-229).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-03.py --out out/dix-pour-cent/s03e02/scene-03.json

ID = "dix-pour-cent-s03e02-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 3
TITLE = "L'eau à température ambiante  (Room-Temperature Water)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Monica", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 198-229. Monica requests room-temperature water at a café, sparking Gabriel's "
               "teasing about her diva habits before they explore a local bookstore. Adapted for A1 French.")

INTRO = ("At a sunny Parisian street cafe, Monica Bellucci enjoys a drink with her agent Gabriel Sarda. "
         "When Monica requests room-temperature water for her vocal cords, Gabriel playfully challenges her claims of living an ordinary life. "
         "Let's listen to their amusing exchange in French first.")

STORY = [
 ("lea", "Pardon mademoiselle, cette eau est trop froide.",
  "Excuse me miss, this water is too cold.",
  [(198, "Mademoiselle, excusez-moi, mais cette eau, elle est vraiment très froide.")], "Rejected cold water politely"),
 ("gabriel", "L'eau froide est mauvaise pour ta gorge?",
  "Is cold water bad for your throat?",
  [(199, "Trop agressive pour ma gorge.")], "Inquired about throat sensitivity"),
 ("lea", "Oui, elle est beaucoup trop agressive pour moi.",
  "Yes, it is much too harsh for me.",
  [(199, "Trop agressive pour ma gorge.")], "Confirmed throat vulnerability"),
 ("lea", "Je voudrais de l'eau à température ambiante.",
  "I would like room-temperature water.",
  [(200, "Est-ce que je pourrais avoir de l'eau à température ambiante, s'il vous plaît ?")], "Requested room temperature water"),
 ("gabriel", "Voilà une demande typique de grande star!",
  "There is a typical request of a big star!",
  [(202, "Tu vois, typiquement, normal, c'est pas le premier mot.")], "Teased diva habit"),
 ("lea", "Pas du tout, c'est juste une précaution.",
  "Not at all, it is just a precaution.",
  [(204, "t'es une femme puissante, accomplie, célèbre.")], "Defended vocal precaution"),
 ("gabriel", "Tu vois bien que tu n'es pas normale!",
  "You see clearly that you are not normal!",
  [(202, "normal, c'est pas le premier mot.")], "Challenged claims of normalcy"),
 ("lea", "Je suis une femme tout à fait ordinaire.",
  "I am a completely ordinary woman.",
  [(204, "femme puissante")], "Insisted on being ordinary"),
 ("gabriel", "Tu es une femme célèbre et très élégante.",
  "You are a famous and very elegant woman.",
  [(204, "t'es une femme puissante, accomplie, célèbre.")], "Noted unavoidable glamour"),
 ("lea", "Regarde cette belle librairie juste en face.",
  "Look at this lovely bookstore right opposite.",
  [(226, "dans la pièce du fond sur la table au rayon tourisme.")], "Spotted bookstore across street"),
 ("gabriel", "Tu veux acheter un livre maintenant?",
  "You want to buy a book now?",
  [(225, "Vous avez des guides pour célibataires à Paris ?")], "Questioned sudden shopping impulse"),
 ("lea", "Ils ont des guides pour les célibataires.",
  "They have guides for singles.",
  [(225, "Vous avez des guides pour célibataires à Paris ?")], "Noted singles travel guides"),
 ("gabriel", "Tu vas chercher l'amour dans un guide?",
  "You are going to look for love in a guide?",
  [(227, "Je cherche quelque chose d'inspirant qui sort de l'ordinaire")], "Wondered about guidebook romance"),
 ("lea", "Pourquoi pas, allons voir ce rayon ensemble!",
  "Why not, let us go see this section together!",
  [(228, "Vous pouvez m'aider ?")], "Led way to bookstore"),
]

OPENER = "Let's explore how Gabriel teases Monica about her diva habits before they explore a bookstore."

WALK = [
 (0, None,
  "'Excuse me miss, this water is too cold.' A courteous request to a waitress rejecting chilled water."),
 (1, None,
  "'Is cold water bad for your throat?' An inquiry asking about vocal care precautions."),
 (2, None,
  "'Yes, it is much too harsh for me.' An intensified adjective describing physical throat sensitivity."),
 (3, None,
  "'I would like room-temperature water.' A polite conditional request for specific beverage temperature."),
 (4, None,
  "'There is a typical request of a big star!' A humorous presentative teasing diva habits."),
 (5, None,
  "'Not at all, it is just a precaution.' A defensive disclaimer explaining professional vocal hygiene."),
 (6, None,
  "'You see clearly that you are not normal!' A friendly teasing assertion highlighting star mannerisms."),
 (7, None,
  "'I am a completely ordinary woman.' An earnest affirmation claiming everyday normalcy."),
 (8, None,
  "'You are a famous and very elegant woman.' A balanced compliment pointing out undeniable glamour."),
 (9, None,
  "'Look at this lovely bookstore right opposite.' An imperative drawing attention to a nearby shop."),
 (10, None,
  "'You want to buy a book now?' A spontaneous question clarifying immediate shopping intentions."),
 (11, None,
  "'They have guides for singles.' A practical observation noting relationship literature."),
 (12, None,
  "'You are going to look for love in a guide?' An amused question wondering about guidebook matchmaking."),
 (13, None,
  "'Why not, let us go see this section together!' An inviting imperative welcoming spontaneous exploration."),
]

TRANSITION = "Now let's listen to Monica and Gabriel again at full speed."

OUTRO = ("Gabriel playfully exposes the contrast between Monica's glamorous habits and her yearning for an ordinary life. "
         "Intrigued by singles guidebooks, Monica leads Gabriel into the bookstore on an impromptu romantic quest.")

CLOSING = ("lea", "Suis-moi, c'est par ici!")
