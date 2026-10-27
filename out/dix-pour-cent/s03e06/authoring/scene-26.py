# Authoring module for dix-pour-cent s03e06 scene 26 (cues 1312-1313).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-26.py --out overhear-content/out/dix-pour-cent/s03e06/scene-26.json

ID = "dix-pour-cent-s03e06-scene-26"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 26
TITLE = "La vérité sur Philippe  (The Truth About Philippe)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 1312-1313. In the ASK agency lounge, Camille reveals to Herve that their secret "
               "client Philippe was Mathias Barneville all along.")

INTRO = ("In the quiet lounge of ASK, Camille finally decides to clear her conscience with Herve. "
         "She confesses the startling identity of their mysterious client Philippe, leaving Herve stunned by Mathias's secret maneuvers. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Hervé, je dois tout t'avouer.",
  "Herve, I must confess everything.",
  [(1313, "je suis en veille")], "Opening confession"),
 ("herve", "Vas-y, je suis en veille.",
  "Go ahead, I am on standby.",
  [(1313, "je suis en veille")], "Listening attentively"),
 ("lea", "Tu connais notre client Philippe?",
  "You know our client Philippe?",
  [(1313, "je suis en veille")], "Asking about client"),
 ("herve", "Oui, notre fameux client mystérieux.",
  "Yes, our famous mysterious client.",
  [(1313, "je suis en veille")], "Recalling mystery client"),
 ("lea", "Philippe, en fait, c'est Mathias.",
  "Philippe, in fact, is Mathias.",
  [(1313, "je suis en veille")], "Revealing identity"),
 ("herve", "Quoi? Ce n'est pas possible!",
  "What? That is not possible!",
  [(1313, "je suis en veille")], "Reacting with shock"),
 ("lea", "C'est la pure vérité, Hervé.",
  "It is the pure truth, Herve.",
  [(1313, "je suis en veille")], "Confirming reality"),
 ("herve", "Mathias nous a engagés nous?",
  "Mathias hired us?",
  [(1313, "je suis en veille")], "Questioning motive"),
 ("lea", "Il préparait son grand départ.",
  "He was preparing his big departure.",
  [(1313, "je suis en veille")], "Explaining plot"),
 ("herve", "Il nous a manipulés totalement!",
  "He manipulated us completely!",
  [(1313, "je suis en veille")], "Realizing manipulation"),
 ("lea", "Il avait confiance en nous.",
  "He had confidence in us.",
  [(1313, "je suis en veille")], "Defending father trust"),
 ("herve", "Tout s'explique enfin maintenant.",
  "Everything makes sense now.",
  [(1313, "je suis en veille")], "Pieces coming together"),
 ("lea", "Nous devons garder le secret.",
  "We must keep the secret.",
  [(1313, "je suis en veille")], "Pledging confidentiality"),
 ("herve", "Cette agence est complètement folle!",
  "This agency is completely crazy!",
  [(1313, "je suis en veille")], "Concluding with disbelief"),
]

WALK = [
 (0, None,
  "'Herve, I must confess everything.' Camille prepares to reveal the agency secret. "
  "The modal verb 'dois' expresses an obligation to speak."),
 (1, None,
  "'Go ahead, I am on standby.' Herve tells her he is ready to listen. "
  "The expression 'en veille' figuratively means on standby or waiting."),
 (2, None,
  "'You know our client Philippe?' Camille brings up their mystery assignment. "
  "The verb 'connaitre' means to know someone."),
 (3, None,
  "'Yes, our famous mysterious client.' Herve remembers the anonymous contract. "
  "The adjective 'mysterieux' describes someone secretive."),
 (4, None,
  "'Philippe, in fact, is Mathias.' Camille delivers the shocking truth. "
  "The locution 'en fait' means actually or in reality."),
 (5, None,
  "'What? That is not possible!' Herve reacts with utter bewilderment. "
  "The adjective 'possible' describes conceivable events."),
 (6, None,
  "'It is the pure truth, Herve.' Camille confirms that she is telling the truth. "
  "The feminine adjective 'pure' reinforces the noun verite."),
 (7, None,
  "'Mathias hired us?' Herve cannot believe their senior partner used them. "
  "The passe compose 'a engages' indicates a completed hiring action."),
 (8, None,
  "'He was preparing his big departure.' Camille explains Mathias's secret motive. "
  "The imperfect 'preparait' describes ongoing background planning."),
 (9, None,
  "'He manipulated us completely!' Herve feels exploited by the deception. "
  "The verb 'manipuler' means to manipulate someone."),
 (10, None,
  "'He had confidence in us.' Camille interprets Mathias's actions as a sign of trust. "
  "The verbal idiom 'avoir confiance' means to trust."),
 (11, None,
  "'Everything makes sense now.' Herve finally understands the strange clues. "
  "The reflexive verb 's'expliquer' means to become clear or make sense."),
 (12, None,
  "'We must keep the secret.' Camille urges discretion between the two assistants. "
  "The noun 'secret' refers to confidential knowledge."),
 (13, None,
  "'This agency is completely crazy!' Herve marvels at the daily drama of ASK. "
  "The feminine adjective 'folle' describes extreme eccentricity."),
]

OUTRO = ("Camille and Herve share a moment of stunned realization in the empty hallway. "
         "The truth about Mathias's covert hiring proves once again that ASK is filled with unpredictable twists. "
         "Now, let's review the scene one last time.")

CLOSING = ("herve", "Cette agence est complètement folle!")
