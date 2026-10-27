# Authoring module for dix-pour-cent s02e03 scene 12 (cues 284-309).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-12.py --out out/dix-pour-cent/s02e03/scene-12.json

ID = "dix-pour-cent-s02e03-scene-12"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 12
TITLE = "Elvis à l'agence  (Elvis at the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "emilie": "emilie"}
LABELS = {"lea": "Camille", "hicham": "Hicham", "emilie": "Sofia"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 284-309. Hicham introduces his London-based son Elvis to the reception team at ASK, "
               "offering match tickets to Camille while Sofia and Camille discuss their future career ambitions. "
               "Adapted for A1 French.")

INTRO = ("At the ASK reception desk, majority shareholder Hicham Janowski arrives with his young son Elvis. "
         "After introducing Elvis to Sofia and Camille, Hicham generously offers tickets to a big football match. "
         "Let's listen to the scene in French first.")

STORY = [
 ("hicham", "Voilà Sofia, elle est à l'accueil.",
  "Here is Sofia, she is at reception.",
  [(284, "Voilà. Ici c'est Sofia, elle est à l'accueil.")], "Simplified phrase"),
 ("emilie", "Bonjour! Tout va très bien aujourd'hui.",
  "Hello! Everything is going very well today.",
  [(285, "Tout va bien ?"), (285, "Très bien.")], "Combined cues"),
 ("hicham", "Voici mon fils Elvis, pour la semaine.",
  "Here is my son Elvis, for the week.",
  [(286, "Mon fils, Elvis. Il est là pour la semaine.")], "Shortened"),
 ("hicham", "Une semaine entre garçons à Paris!",
  "A week between boys in Paris!",
  [(287, "Une semaine entre garçons à Paris.")], ""),
 ("hicham", "Il va à l'école française à Londres.",
  "He goes to the French school in London.",
  [(291, "L'école française.")], "Added Il va à, à Londres"),
 ("hicham", "C'est vraiment une des meilleures écoles.",
  "It is really one of the best schools.",
  [(292, "Une des meilleures.")], "Added C'est vraiment, écoles"),
 ("hicham", "On sera dans mon bureau, à tout à l'heure.",
  "We will be in my office, see you later.",
  [(293, "On sera dans mon bureau, à tout à l'heure.")], ""),
 ("hicham", "J'ai des billets pour le match du PSG!",
  "I have tickets for the PSG match!",
  [(298, "J'ai des billets pour le match du PSG !")], ""),
 ("hicham", "Camille, tu veux venir avec nous?",
  "Camille, do you want to come with us?",
  [(298, "match")], "Adapted invitation"),
 ("lea", "Merci, monsieur Janowski, c'est très gentil.",
  "Thank you, Mr. Janowski, that is very kind.",
  [(300, "Paris.")], "Adapted polite reply"),
 ("emilie", "Tu as envie de devenir agent plus tard?",
  "Do you want to become an agent later on?",
  [(304, "une fois que je suis agent...")], "Adapted question"),
 ("lea", "Oui, j'aimerais beaucoup être agente un jour.",
  "Yes, I would very much like to be an agent one day.",
  [(304, "suis agent...")], "Adapted response"),
 ("emilie", "L'avenir du cinéma français est entre tes mains!",
  "The future of French cinema is in your hands!",
  [(305, "l'avenir du cinéma français est en bonnes mains.")], "Adapted"),
 ("emilie", "N'oublie pas que beaucoup d'acteurs sont des actrices.",
  "Do not forget that many actors are actresses.",
  [(306, "des acteurs sont des actrices.")], "Adapted percentage"),
 ("lea", "Tu ne veux pas que je postule?",
  "You do not want me to apply?",
  [(308, "Tu ne veux pas que je postule ?")], ""),
 ("emilie", "Bien sûr que si, j'y réfléchirai avec toi.",
  "Of course I do, I will think about it with you.",
  [(309, "J'y réfléchirai.")], "Adapted closing"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Here is Sofia, she is at reception.' Hicham introduces the receptionist to his son. "
  "The presentative 'voila' introduces the subject, followed by the spatial phrase 'a l'accueil'."),
 (1, None,
  "'Hello! Everything is going very well today.' Sofia greets them warmly with polite professionalism. "
  "The fixed idiom 'tout va tres bien' is standard for answering how things are."),
 (2, None,
  "'Here is my son Elvis, for the week.' Hicham proudly introduces his boy. "
  "The presentative 'voici' presents a person standing close by."),
 (3, None,
  "'A week between boys in Paris!' Hicham looks forward to male bonding in the capital. "
  "The preposition 'entre' denotes mutual companionship between peers."),
 (4, None,
  "'He goes to the French school in London.' Hicham shares his son's schooling location. "
  "The preposition 'a' indicates the city location 'a Londres'."),
 (5, None,
  "'It is really one of the best schools.' Hicham boasts about academic excellence. "
  "The superlative structure 'une des meilleures' uses the feminine plural adjective."),
 (6, None,
  "'We will be in my office, see you later.' Hicham announces their destination inside ASK. "
  "The parting formula 'a tout a l'heure' is customary when meeting again soon."),
 (7, None,
  "'I have tickets for the PSG match!' Hicham shares his exciting football plans. "
  "The plural noun phrase 'des billets pour' specifies admission tickets."),
 (8, None,
  "'Camille, do you want to come with us?' Hicham extends a spontaneous invitation. "
  "The verb 'vouloir' followed by 'venir' frames an informal invite."),
 (9, None,
  "'Thank you, Mr. Janowski, that is very kind.' Camille responds with gratitude. "
  "The courteous expression 'c'est tres gentil' acknowledges thoughtful generosity."),
 (10, None,
  "'Do you want to become an agent later on?' Sofia inquires about Camille's career dreams. "
  "The idiom 'avoir envie de' governs the infinitive 'devenir'."),
 (11, None,
  "'Yes, I would very much like to be an agent one day.' Camille confesses her ambition. "
  "The conditional 'j'aimerais' conveys a polite future aspiration."),
 (12, None,
  "'The future of French cinema is in your hands!' Sofia encourages her colleague playfully. "
  "The noun phrase 'l'avenir du cinema' evokes the cultural industry."),
 (13, None,
  "'Do not forget that many actors are actresses.' Sofia reminds her of gender representation. "
  "The negative imperative 'n'oublie pas' urges thoughtful awareness."),
 (14, None,
  "'You do not want me to apply?' Camille seeks clarification on agency training. "
  "The verb 'postuler' means to submit a job or training application."),
 (15, None,
  "'Of course I do, I will think about it with you.' Sofia pledges friendly career advice. "
  "The adverbial pronoun 'y' replaces the topic of career consideration."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Hicham introduces his son Elvis to the agency staff and generously hands out match tickets. "
         "Meanwhile, Camille and Sofia bond over their shared professional aspirations in the agency.")
CLOSING = ("emilie", "Bien sûr que si, j'y réfléchirai avec toi.")
