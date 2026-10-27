# Authoring module for dix-pour-cent s03e05 scene 11 (cues 384-387).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-11.py --out out/dix-pour-cent/s03e05/scene-11.json

ID = "dix-pour-cent-s03e05-scene-11"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 11
TITLE = "Visite nocturne  (Nighttime Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Camille", "theo": "Valentin"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 384-387. Camille brings young actor Valentin into the quiet ASK offices after hours, "
               "asking him to keep his voice down as he explores the hallway. Adapted for A1 French.")

INTRO = ("Late in the evening, Camille brings young actor Valentin into the darkened ASK agency. "
         "Valentin looks around in awe, curious to discover where she works. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("lea", "Entre discrètement, il ne faut aucun bruit.",
  "Come in discreetly, we must not make noise.",
  [(384, "Ouais")], "Urging discretion"),
 ("theo", "C'est vraiment très impressionnant ici.",
  "It is truly very impressive here.",
  [(385, "Et ton bureau il est où là ?")], "Admiring agency"),
 ("lea", "Oui, c'est une grande agence artistique.",
  "Yes, it is a major talent agency.",
  [(385, "Et ton bureau il est où là ?")], "Describing workplace"),
 ("theo", "Et ton bureau, il est où exactement?",
  "And your office, where is it exactly?",
  [(385, "Et ton bureau il est où là ?")], "Inquiring about office"),
 ("lea", "Mon bureau est juste au bout du couloir.",
  "My office is right at the end of the hall.",
  [(386, "Il est là")], "Indicating direction"),
 ("theo", "Tu travailles ici depuis longtemps?",
  "Have you worked here for a long time?",
  [(385, "Et ton bureau il est où là ?")], "Asking about experience"),
 ("lea", "Depuis quelques mois seulement comme assistante.",
  "Only for a few months as an assistant.",
  [(385, "Et ton bureau il est où là ?")], "Explaining job role"),
 ("theo", "Mais tu veux devenir agent à part entière?",
  "But you want to become a full agent?",
  [(385, "Et ton bureau il est où là ?")], "Inquiring ambition"),
 ("lea", "Oui, c'est mon grand rêve professionnel.",
  "Yes, that is my great professional dream.",
  [(385, "Et ton bureau il est où là ?")], "Affirming dream"),
 ("theo", "Tu as beaucoup de talent pour cela.",
  "You have a lot of talent for that.",
  [(385, "Et ton bureau il est où là ?")], "Encouraging Camille"),
 ("lea", "Merci, Valentin, c'est gentil de le dire.",
  "Thank you, Valentin, that is kind to say.",
  [(385, "Et ton bureau il est où là ?")], "Polite response"),
 ("theo", "Alors montre-moi où tu travailles tous les jours.",
  "Then show me where you work every day.",
  [(385, "Et ton bureau il est où là ?")], "Asking for tour"),
 ("lea", "D'accord, avance lentement par ici.",
  "Okay, walk forward slowly this way.",
  [(386, "Il est là")], "Guiding forward"),
 ("theo", "Voilà, je te suis avec grand plaisir.",
  "There, I am following you with great pleasure.",
  [(387, "Voilà")], "Following eagerly"),
]

WALK = [
 (0, None,
  "'Come in discreetly, we must not make noise.' Camille welcomes Valentin after hours. "
  "The adverb 'discretement' counsels caution."),
 (1, None,
  "'It is truly very impressive here.' Valentin admires the agency premises. "
  "The adjective 'impressionnant' conveys awe."),
 (2, None,
  "'Yes, it is a major talent agency.' Camille explains the business. "
  "The adjective 'artistique' qualifies the agency."),
 (3, None,
  "'And your office, where is it exactly?' Valentin looks around curious. "
  "The noun 'bureau' refers to a workplace."),
 (4, None,
  "'My office is right at the end of the hall.' Camille indicates the layout. "
  "The noun 'couloir' designates a corridor."),
 (5, None,
  "'Have you worked here for a long time?' Valentin asks about her career history. "
  "The preposition 'depuis' expresses duration."),
 (6, None,
  "'Only for a few months as an assistant.' Camille clarifies her current position. "
  "The adverb 'seulement' limits the time frame."),
 (7, None,
  "'But you want to become a full agent?' Valentin inquires about her ambitions. "
  "The idiom 'a part entiere' means fully fledged."),
 (8, None,
  "'Yes, that is my great professional dream.' Camille shares her career goal. "
  "The adjective 'professionnel' relates to work."),
 (9, None,
  "'You have a lot of talent for that.' Valentin offers encouragement. "
  "The noun 'talent' praises her aptitude."),
 (10, None,
  "'Thank you, Valentin, that is kind to say.' Camille appreciates his support. "
  "The polite phrase 'c'est gentil' acknowledges a compliment."),
 (11, None,
  "'Then show me where you work every day.' Valentin urges a tour. "
  "The imperative 'montre-moi' asks for a demonstration."),
 (12, None,
  "'Okay, walk forward slowly this way.' Camille leads the way quietly. "
  "The adverb 'lentement' warns him to tread softly."),
 (13, None,
  "'There, I am following you with great pleasure.' Valentin follows her down the hallway. "
  "The verb 'suivre' means to follow."),
]

OUTRO = ("Camille leads Valentin deeper into the agency corridor toward the offices. "
         "Her young protege is intrigued by the glamorous setting and eager to learn more. "
         "Now, let's review the scene once more.")

CLOSING = ("theo", "Voilà, je te suis avec grand plaisir.")
