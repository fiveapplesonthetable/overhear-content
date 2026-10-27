# Authoring module for dix-pour-cent s02e04 scene 09 (cues 231-250).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-09.py --out out/dix-pour-cent/s02e04/scene-09.json

ID = "dix-pour-cent-s02e04-scene-09"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 9
TITLE = "La cabine d'enregistrement  (Recording Booth)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo", "marcel": "marcel"}
LABELS = {"lea": "Sofia", "theo": "Julien", "marcel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 231-250. At the recording studio, Julien Doré greets Sofia and Gabriel. "
               "Julien asks Gabriel to wait outside so the vocal booth remains intimate and focused. "
               "Adapted for A1 French.")

INTRO = ("At the music studio, Julien Dore welcomes Sofia to record their duet while Gabriel accompanies her. "
         "Julien gently asks Gabriel to wait outside so the vocal booth stays intimate and focused. "
         "Let's listen to the scene in French first.")

STORY = [
 ("marcel", "Salut Julien. Mathias n'a pas pu venir.",
  "Hi Julien. Mathias could not make it.",
  [(231, "Salut."), (232, "Mathias n'a pas pu venir.")], "Added Julien"),
 ("theo", "D'accord, pas de problème.",
  "Okay, no problem.",
  [(233, "pas de problème.")], ""),
 ("theo", "Bienvenue, Sofia. Ça va?",
  "Welcome, Sofia. How are you?",
  [(235, "Bienvenue."), (234, "Ça va ?")], "Added Sofia"),
 ("lea", "Salut, ça va très bien.",
  "Hi, I am doing very well.",
  [(235, "Salut.")], "Added ça va très bien"),
 ("theo", "J'ai fait quelques arrangements différents pour la chanson.",
  "I made a few different arrangements for the song.",
  [(236, "J'ai fait quelques arrangements différents pour la chanson.")], ""),
 ("theo", "Ta voix m'a tellement inspiré...",
  "Your voice inspired me so much...",
  [(237, "Ta voix m'a tellement inspiré...")], ""),
 ("lea", "Ah oui? Merci beaucoup.",
  "Oh really? Thank you very much.",
  [(238, "Merci.")], "Added beaucoup"),
 ("theo", "Par ici, venez.",
  "This way, come along.",
  [(238, "Par ici.")], "Added venez"),
 ("theo", "Désolé, Gabriel, je préfère que la cabine ne soit pas pleine de monde.",
  "Sorry, Gabriel, I prefer that the booth is not full of people.",
  [(240, "Désolé, Gabriel, je préfère que la cabine ne soit pas pleine de monde.")], ""),
 ("marcel", "D'accord, à tout à l'heure.",
  "All right, see you in a bit.",
  [(241, "À tout à l'heure.")], "Added D'accord"),
 ("theo", "Voilà, c'est la pièce la plus importante du studio.",
  "Here we are, this is the most important room in the studio.",
  [(242, "Voilà."), (243, "C'est la pièce la plus importante du studio.")], ""),
 ("theo", "La plus intime. Je vous laisse entrer.",
  "The most intimate. I will let you go in.",
  [(244, "La plus intime."), (245, "Je vous laisse entrer.")], ""),
 ("lea", "Merci, c'est très impressionnant.",
  "Thank you, it is very impressive.",
  [(245, "Merci.")], "Added c'est très impressionnant"),
 ("theo", "Voici votre casque.",
  "Here are your headphones.",
  [(246, "Voici votre casque.")], ""),
 ("theo", "Détendez-vous, tout va bien. Quand vous êtes prête.",
  "Relax, everything is fine. Whenever you are ready.",
  [(249, "Détendez-vous, tout va bien."), (248, "Quand vous êtes prête.")], ""),
 ("lea", "D'accord, je suis prête.",
  "Okay, I am ready.",
  [(250, "D'accord.")], "Added je suis prête"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Hi Julien. Mathias could not make it.' Gabriel announces Mathias's absence casually. "
  "The compound tense 'n'a pas pu venir' uses the past participle of pouvoir followed by an infinitive."),
 (1, None,
  "'Okay, no problem.' Julien accepts the situation smoothly. "
  "The negative phrase 'pas de probleme' is the standard conversational way to dismiss an inconvenience."),
 (2, None,
  "'Welcome, Sofia. How are you?' Julien greets Sofia warmly. "
  "The interjection 'bienvenue' welcomes a guest, paired with the familiar question 'ca va'."),
 (3, None,
  "'Hi, I am doing very well.' Sofia returns the friendly greeting. "
  "The adverbial intensifier 'tres bien' indicates that she is feeling enthusiastic and ready."),
 (4, None,
  "'I made a few different arrangements for the song.' Julien reveals his creative work. "
  "The indefinite plural determiner 'quelques' modifies the plural noun 'arrangements'."),
 (5, None,
  "'Your voice inspired me so much...' Julien compliments Sofia's musical talent. "
  "The adverb 'tellement' underscores how deeply her singing influenced his composition."),
 (6, None,
  "'Oh really? Thank you very much.' Sofia responds with modest gratitude. "
  "The conversational reaction 'ah oui' conveys pleasant surprise followed by thanks."),
 (7, None,
  "'This way, come along.' Julien directs Sofia toward the recording area. "
  "The spatial locution 'par ici' guides a visitor politely through the studio."),
 (8, None,
  "'Sorry, Gabriel, I prefer that the booth is not full of people.' Julien gently excludes Gabriel. "
  "The verb 'preferer que' governs the subjunctive form 'ne soit pas'."),
 (9, None,
  "'All right, see you in a bit.' Gabriel steps back politely. "
  "The temporal idiom 'a tout a l'heure' promises a reunion later in the day."),
 (10, None,
  "'Here we are, this is the most important room in the studio.' Julien highlights the sacred space. "
  "The superlative 'la plus importante' emphasizes the central value of the vocal booth."),
 (11, None,
  "'The most intimate. I will let you go in.' Julien ushers Sofia into the vocal chamber. "
  "The factitive verb 'laisser entrer' means to permit someone to step inside."),
 (12, None,
  "'Thank you, it is very impressive.' Sofia admires the professional setting. "
  "The adjective 'impressionnant' describes the awe-inspiring acoustic equipment."),
 (13, None,
  "'Here are your headphones.' Julien hands her the audio gear. "
  "The presentative 'voici' presents an object directly to the listener."),
 (14, None,
  "'Relax, everything is fine. Whenever you are ready.' Julien offers warm reassurance. "
  "The reflexive imperative 'detendez-vous' encourages calm concentration before singing."),
 (15, None,
  "'Okay, I am ready.' Sofia collects herself to perform. "
  "The feminine adjective 'prete' agrees in gender with Sofia as the speaker."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Julien Dore establishes an intimate recording environment for Sofia, isolating her from Gabriel's watchful agency eye. "
         "Sofia steps up to the microphone, ready to launch her musical career.")
CLOSING = ("lea", "D'accord, je suis prête.")
