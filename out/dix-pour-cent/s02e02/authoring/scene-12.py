# Authoring module for dix-pour-cent s02e02 scene 12 (cues 355-395).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-12.py --out out/dix-pour-cent/s02e02/scene-12.json

ID = "dix-pour-cent-s02e02-scene-12"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 12
TITLE = "Rencontre à la salle de sport  (Meeting at the Gym)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Fabrice"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 355-395. Andréa approaches Fabrice Luchini at his workout gym to recruit him for ASK. "
               "Luchini politely yet firmly rebuffs her pitch, affirming his thirty-five-year loyalty to rival agent Bréhier. "
               "Adapted for A1 French.")

INTRO = ("At an exclusive Parisian fitness club, Andrea tracks down renowned actor Fabrice Luchini on the workout machines. "
         "She delivers a passionate pitch to poach him for the ASK agency, but Luchini has his own unique philosophy. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Bonjour, Fabrice! Tu viens souvent ici?",
  "Hello, Fabrice! Do you come here often?",
  [(355, "Bonjour, Fabrice !"), (357, "Tu viens souvent ?")], "Added ici"),
 ("theo", "Je vous connais, vous êtes agent, non?",
  "I know you, you are an agent, right?",
  [(359, "Je vous connais, vous êtes agent, non ?")], ""),
 ("lea", "Andréa Martel, je travaille chez ASK.",
  "Andréa Martel, I work at ASK.",
  [(360, "Andréa Martel, je travaille chez ASK.")], ""),
 ("theo", "Vous ne devriez pas être au bureau?",
  "Should you not be at the office?",
  [(362, "Vous ne devriez pas être au bureau ?")], ""),
 ("lea", "En fait, je suis au travail là.",
  "In fact, I am at work right now.",
  [(363, "En fait, je suis au travail là.")], ""),
 ("lea", "Je suis là pour vous. Vous êtes un talent rare.",
  "I am here for you. You are a rare talent.",
  [(364, "Je suis là pour vous."), (365, "Vous êtes un talent rare.")], ""),
 ("theo", "Qu'est-ce que vous proposez exactement?",
  "What are you offering exactly?",
  [(368, "Qu'est-ce que vous proposez ?")], "Added exactement"),
 ("lea", "Je propose un nouvel élan artistique.",
  "I offer a new artistic impetus.",
  [(369, "Un nouvel élan.")], "Expanded with Je propose and artistique"),
 ("theo", "Tout ça est un peu bizarre.",
  "All of this is a bit strange.",
  [(376, "Tout ça est un peu bizarre,")], ""),
 ("theo", "Débarquer dans une salle de sport pour me parler!",
  "Turning up in a gym to speak to me!",
  [(377, "débarquer dans une salle de sport")], "Added pour me parler"),
 ("theo", "Je suis chez Bréhier depuis trente-cinq ans.",
  "I have been with Bréhier for thirty-five years.",
  [(379, "je suis chez Bréhier, ça fait 35 ans.")], "Spelled out number 35"),
 ("theo", "On est un vieux couple. Je l'aime bien.",
  "We are an old couple. I like him.",
  [(380, "On est un vieux couple. Je l'aime bien.")], ""),
 ("theo", "La nouveauté est un concept qui ne m'intéresse pas.",
  "Novelty is a concept that does not interest me.",
  [(383, "La nouveauté est un concept qui ne m'intéresse pas.")], ""),
 ("lea", "Peut-être que vous voulez juste vous ennuyer.",
  "Maybe you just want to be bored.",
  [(385, "Peut-être que vous voulez juste vous ennuyer.")], ""),
 ("theo", "Ne dites pas du mal de l'ennui.",
  "Do not speak ill of boredom.",
  [(386, "Ne dites pas du mal de l'ennui.")], ""),
 ("lea", "Je vous laisse donc vous ennuyer avec Bréhier.",
  "I leave you then to be bored with Bréhier.",
  [(389, "Je vous laisse donc vous ennuyer avec Bréhier.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Hello, Fabrice! Do you come here often?' Andrea initiates conversation with casual charm. "
  "The temporal adverb 'souvent' modifies the present tense question about routine attendance."),
 (1, None,
  "'I know you, you are an agent, right?' Luchini spots her professional identity immediately. "
  "The verb 'connaitre' is used for recognizing or being acquainted with a person."),
 (2, None,
  "'Andrea Martel, I work at ASK.' Andrea introduces herself with professional pride. "
  "The preposition 'chez' denotes working at a particular company or agency."),
 (3, None,
  "'Should you not be at the office?' Luchini raises an ironic eyebrow at her fitness location. "
  "The conditional verb 'devriez' expresses expectation or obligation in a polite register."),
 (4, None,
  "'In fact, I am at work right now.' Andrea asserts that scouting him is official business. "
  "The discourse marker 'en fait' signals an unexpected clarification."),
 (5, None,
  "'I am here for you. You are a rare talent.' Andrea delivers her direct flatteries. "
  "The adjective 'rare' follows the masculine noun 'talent' to convey exceptional distinction."),
 (6, None,
  "'What are you offering exactly?' Luchini invites her specific commercial proposal. "
  "The interrogative phrase 'qu'est-ce que' asks what she proposes, sharpened by 'exactement'."),
 (7, None,
  "'I offer a new artistic impetus.' Andrea pitches fresh creative energy for his career. "
  "The masculine noun phrase 'un nouvel elan' uses the special masculine form 'nouvel' before a vowel."),
 (8, None,
  "'All of this is a bit strange.' Luchini comments on the theatrical ambush. "
  "The demonstrative pronoun 'tout ca' is modified by the adjective 'bizarre'."),
 (9, None,
  "'Turning up in a gym to speak to me!' Luchini notes the comical unorthodoxy of the setting. "
  "The informal infinitive 'debarquer' evokes showing up suddenly and unannounced."),
 (10, None,
  "'I have been with Brehier for thirty-five years.' Luchini reveals his deep agency history. "
  "The temporal preposition 'depuis' indicates an ongoing state that started in the past."),
 (11, None,
  "'We are an old couple. I like him.' Luchini describes his relationship with his agent. "
  "The verb 'aimer bien' expresses warm affection or fondness without romantic love."),
 (12, None,
  "'Novelty is a concept that does not interest me.' Luchini rejects trendy career shifts. "
  "The relative clause 'qui ne m'interesse pas' negates personal appeal emphatically."),
 (13, None,
  "'Maybe you just want to be bored.' Andrea challenges his resistance with witty sarcasm. "
  "The reflexive infinitive 'vous ennuyer' denotes experiencing boredom or dullness."),
 (14, None,
  "'Do not speak ill of boredom.' Luchini defends existential boredom as a creative state. "
  "The negative imperative 'ne dites pas du mal de' forbids criticizing something."),
 (15, None,
  "'I leave you then to be bored with Brehier.' Andrea concludes her exit with sharp wit. "
  "The verb 'laisser' governs the reflexive infinitive 'vous ennuyer' in a graceful departure."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Andrea's bold fitness ambush ends with Luchini standing loyal to his long-time agent Brehier. "
         "Her pitch was spirited, but Luchini's love of familiar routine proved unshakeable.")
CLOSING = ("theo", "Ne dites pas du mal de l'ennui.")
