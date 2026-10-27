# Authoring module for dix-pour-cent s02e06 scene 01 (cues 1-56).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-01.py --out out/dix-pour-cent/s02e06/scene-01.json

ID = "dix-pour-cent-s02e06-scene-01"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 1
TITLE = "Le smoking Armani  (The Armani Tuxedo)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie", "eva": "theo"}
LABELS = {"lea": "Juliette", "andrea": "Andréa", "eva": "Eva"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-56. Juliette Binoche tries on a sophisticated Cannes gown, but opts for an "
               "Armani tuxedo instead for elegance and comfort. Adapted for A1 French.")

INTRO = ("At a Parisian fashion salon, movie star Juliette Binoche tries on elaborate designer gowns for the Cannes Film Festival. "
         "Her agent Andrea Martel arrives late due to heavy traffic, joining artistic producer Eva to inspect the wardrobe options. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Je suis en plein essayage pour Cannes.",
  "I am in the middle of a fitting for Cannes.",
  [(2, "Je suis en essayage pour Cannes.")], "Expressed present continuous fitting"),
 ("andrea", "Désolée Juliette, mon taxi était bloqué.",
  "Sorry Juliette, my taxi was stuck.",
  [(7, "Désolée, mon taxi est resté bloqué place de la Concorde.")], "Simplified traffic excuse"),
 ("eva", "Bonjour Andréa, nous parlions de la cérémonie.",
  "Hello Andrea, we were talking about the ceremony.",
  [(9, "productrice artistique de la cérémonie d'ouverture.")], "Added friendly greeting"),
 ("andrea", "Juliette sera une maîtresse de cérémonie parfaite.",
  "Juliette will be a perfect mistress of ceremonies.",
  [(12, "Nous sommes ravis que Juliette soit la maîtresse de cérémonie cette année.")], "Affirmed festival role"),
 ("lea", "Cette robe est vraiment très compliquée!",
  "This dress is really very complicated!",
  [(20, "Comment fonctionne cette robe ?")], "Expresses garment complexity"),
 ("eva", "Il faut juste vous y habituer.",
  "You just have to get used to it.",
  [(21, "Il faut juste s'y abandonner.")], "Simplified advice"),
 ("lea", "Je crois qu'elle est trop serrée.",
  "I think that it is too tight.",
  [(27, "Un peu serré ?")], "Noted tightness"),
 ("andrea", "Pourtant, tu es tout simplement divine!",
  "Yet, you are simply divine!",
  [(30, "Vous êtes divine !")], "Complimented appearance"),
 ("lea", "C'est beaucoup trop sophistiqué pour moi.",
  "It is much too sophisticated for me.",
  [(39, "Je trouve que c'est trop sophistiqué pour moi.")], "Stated personal taste"),
 ("eva", "Cette robe demande mille heures de travail.",
  "This dress requires a thousand hours of work.",
  [(40, "Cette robe, c'est mille heures de travail.")], "Emphasized couture craft"),
 ("lea", "Je préfère porter le smoking Armani.",
  "I prefer to wear the Armani tuxedo.",
  [(51, "Pour moi, c'est le smoking Armani.")], "Stated outfit preference"),
 ("andrea", "Tu te sens mieux en smoking?",
  "Do you feel better in a tuxedo?",
  [(52, "Je me sentirais plus élégante, plus libre.")], "Asked about comfort"),
 ("lea", "Oui, je me sens plus libre.",
  "Yes, I feel freer.",
  [(52, "Je me sentirais plus élégante, plus libre.")], "Affirmed freedom of movement"),
 ("eva", "Très bien, va pour le smoking Armani!",
  "Very well, let us go with the Armani tuxedo!",
  [(54, "Très bien, alors. Nous sommes tous d'accord."), (55, "Le smoking Armani.")], "Confirmed final choice"),
]

OPENER = "Let's explore how Juliette explains her costume choice to Andrea and Eva."

WALK = [
 (0, None,
  "'I am in the middle of a fitting for Cannes.' An idiomatic prepositional phrase indicating an ongoing dress fitting."),
 (1, None,
  "'Sorry Juliette, my taxi was stuck.' A polite apology followed by a common urban traffic excuse."),
 (2, None,
  "'Hello Andrea, we were talking about the ceremony.' A courtesy greeting and imperfect verb establishing ongoing conversation."),
 (3, None,
  "'Juliette will be a perfect mistress of ceremonies.' A future tense compliment affirming festive responsibilities."),
 (4, None,
  "'This dress is really very complicated!' An intensified demonstrative phrase critiquing garment comfort."),
 (5, None,
  "'You just have to get used to it.' An impersonal modal verb advising adaptation to high fashion."),
 (6, None,
  "'I think that it is too tight.' A cognitive opinion verb introducing a physical discomfort complaint."),
 (7, None,
  "'Yet, you are simply divine!' An adversative adverb reinforcing sincere visual admiration."),
 (8, None,
  "'It is much too sophisticated for me.' An intensified adjective expressing personal aesthetic preference."),
 (9, None,
  "'This dress requires a thousand hours of work.' A cardinal numeral emphasizing artisanal couture labor."),
 (10, None,
  "'I prefer to wear the Armani tuxedo.' A decisive preference verb proposing an alternative outfit."),
 (11, None,
  "'Do you feel better in a tuxedo?' An inverted pronominal question checking bodily comfort."),
 (12, None,
  "'Yes, I feel freer.' A comparative adjective highlighting physical and artistic ease."),
 (13, None,
  "'Very well, let us go with the Armani tuxedo!' An agreeable colloquial consensus confirming the wardrobe decision."),
]

TRANSITION = "Now let's listen to Juliette, Andrea, and Eva again at full speed."

OUTRO = ("Juliette Binoche rejects the restrictive dress in favor of a sleek Armani tuxedo, choosing comfort and independence. "
         "Her agent Andrea and producer Eva respect her decision as preparations for the Cannes festival continue.")

CLOSING = ("lea", "Merci pour votre aide, Eva.")
