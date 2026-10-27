# Authoring module for dix-pour-cent s04e01 scene 09 (cue 511).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-09.py --out overhear-content/out/dix-pour-cent/s04e01/scene-09.json

ID = "dix-pour-cent-s04e01-scene-09"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 9
TITLE = "Le départ de Mathias  (Mathias's Departure)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cue 511. As Mathias Barneville steps toward the elevator with his belongings, "
               "Andrea asks him to surrender his office keys, leaving him deeply stung by the swift eviction.")

INTRO = ("At the elevator doors of ASK, former managing partner Mathias Barneville prepares to leave the agency for good. "
         "Holding his box of personal belongings, he is confronted by Andrea, who firmly asks him to return his office keys. "
         "Let's listen to their farewell conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Mathias, attends une seconde s'il te plaît.",
  "Mathias, wait a second please.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Calling Mathias back"),
 ("mathias", "Oui Andréa? Qu'est-ce qu'il y a?",
  "Yes Andrea? What is the matter?",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Turning around patiently"),
 ("lea", "Tu dois nous rendre tes clés d'agence.",
  "You must give back your agency keys.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Requesting office keys"),
 ("mathias", "Vous me traitez comme un voleur maintenant?",
  "Are you treating me like a thief now?",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Reacting with hurt indignity"),
 ("lea", "Noémie a déjà rendu les siennes ce matin.",
  "Noemie already gave back hers this morning.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Citing administrative consistency"),
 ("mathias", "J'ai dirigé cette agence pendant trente ans!",
  "I ran this agency for thirty years!",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Invoking three decades of leadership"),
 ("lea", "Nous voulons simplement protéger nos nouveaux contrats.",
  "We simply want to protect our new contracts.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Justifying protective measures"),
 ("mathias", "Vous avez peur de ma concurrence future?",
  "Are you afraid of my future competition?",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Challenging agency security"),
 ("lea", "Nous voulons éviter de changer les serrures.",
  "We want to avoid changing the locks.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Giving practical explanation"),
 ("mathias", "Prends ces clés, je n'en veux plus.",
  "Take these keys, I do not want them anymore.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Surrendering keys abruptly"),
 ("lea", "Merci Mathias, bonne chance pour tes projets.",
  "Thank you Mathias, good luck with your projects.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Offering professional send-off"),
 ("mathias", "Au revoir. Vraiment, je n'en reviens pas.",
  "Goodbye. Seriously, I cannot believe it.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Expressing lingering disbelief"),
 ("lea", "Une nouvelle histoire commence pour nous tous.",
  "A new story begins for all of us.",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Marking a fresh agency chapter"),
 ("mathias", "Bonne chance avec vos nouveaux problèmes quotidiens!",
  "Good luck with your new daily problems!",
  [(511, "Au revoir. Vraiment, j'en reviens pas.")], "Delivering parting cynical jab"),
]

WALK = [
 (0, None,
  "'Mathias, wait a second please.' Andrea stops Mathias before he reaches the lift. "
  "The imperative 'attends' urges someone to pause briefly."),
 (1, None,
  "'Yes Andrea? What is the matter?' Mathias wonders what further request remains. "
  "The phrase 'qu'est-ce qu'il y a' inquires about an unexpected issue."),
 (2, None,
  "'You must give back your agency keys.' Andrea requests the surrender of his keys. "
  "The verb 'rendre' means to return or give back an item."),
 (3, None,
  "'Are you treating me like a thief now?' Mathias feels insulted by the demand. "
  "The noun 'voleur' denotes a thief or burglar."),
 (4, None,
  "'Noemie already gave back hers this morning.' Andrea mentions Noemie's compliance. "
  "The possessive pronoun 'les siennes' refers to feminine plural objects."),
 (5, None,
  "'I ran this agency for thirty years!' Mathias recalls his long-standing authority. "
  "The passe compose 'ai dirige' marks his executive career."),
 (6, None,
  "'We simply want to protect our new contracts.' Andrea defends client confidentiality. "
  "The verb 'proteger' expresses preservation and defense."),
 (7, None,
  "'Are you afraid of my future competition?' Mathias suspects fear of his new firm. "
  "The idiom 'avoir peur de' expresses fear or apprehension."),
 (8, None,
  "'We want to avoid changing the locks.' Andrea provides a pragmatic financial reason. "
  "The noun 'serrure' refers to a door lock."),
 (9, None,
  "'Take these keys, I do not want them anymore.' Mathias gives in with irritation. "
  "The pronoun 'en' replaces the prepositional phrase de ces cles."),
 (10, None,
  "'Thank you Mathias, good luck with your projects.' Andrea offers civil farewell wishes. "
  "The phrase 'bonne chance' wishes someone good fortune."),
 (11, None,
  "'Goodbye. Seriously, I cannot believe it.' Mathias shakes his head in disbelief. "
  "The colloquial expression 'ne pas en revenir' means to be unable to believe something."),
 (12, None,
  "'A new story begins for all of us.' Andrea looks forward to leading the agency. "
  "The verb 'commencer' signifies the start of a new chapter."),
 (13, None,
  "'Good luck with your new daily problems!' Mathias delivers a sardonic parting remark. "
  "The adjective 'quotidien' describes routine or daily occurrences."),
]

OUTRO = ("Mathias hands over his keys and steps into the closing elevator, bringing thirty years at ASK to an end. "
         "Andrea watches him depart, knowing that the agency now rests entirely on her shoulders. "
         "Now, let's review the scene one last time.")

CLOSING = ("mathias", "Au revoir. Vraiment, je n'en reviens pas.")
