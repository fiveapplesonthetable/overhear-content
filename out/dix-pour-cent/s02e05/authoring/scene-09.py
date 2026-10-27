# Authoring module for dix-pour-cent s02e05 scene 09 (cues 258-276).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-09.py --out out/dix-pour-cent/s02e05/scene-09.json

ID = "dix-pour-cent-s02e05-scene-09"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 9
TITLE = "La nouvelle junior  (The New Junior)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "emilie": "emilie", "theo": "theo"}
LABELS = {"lea": "Camille", "emilie": "Andréa", "theo": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 258-276. In the agency conference room, Hicham surprises everyone by appointing "
               "Camille as the new junior agent. Adapted for A1 French.")

INTRO = ("In the ASK conference room, Hicham interrupts the partners meeting to deliver a major announcement. "
         "Without consulting the other agents, he reveals his choice for the new junior agent position. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Et maintenant, que diriez-vous d'accueillir officiellement notre nouveau junior?",
  "And now, what would you say to officially welcoming our new junior?",
  [(259, "que diriez-vous d'accueillir officiellement notre nouveau junior ?")], ""),
 ("emilie", "Vous auriez dû nous consulter avant.",
  "You should have consulted us beforehand.",
  [(260, "Vous auriez dû nous consulter.")], "Added avant"),
 ("theo", "Je me suis consulté moi-même. Et j'ai décidé.",
  "I consulted myself. And I decided.",
  [(261, "Je me suis consulté moi-même."), (262, "Et j'ai décidé.")], ""),
 ("theo", "Notre nouveau junior est une femme.",
  "Our new junior is a woman.",
  [(263, "Notre nouveau junior est une femme.")], ""),
 ("theo", "Et elle s'appelle Camille Valentini.",
  "And her name is Camille Valentini.",
  [(264, "Et elle s'appelle Camille..."), (265, "Valentini.")], ""),
 ("emilie", "Quoi? Camille?",
  "What? Camille?",
  [(265, "Quoi ?")], "Added Camille"),
 ("theo", "Il y avait des candidats qui savaient très bien se vendre.",
  "There were candidates who knew very well how to sell themselves.",
  [(266, "Il y avait des candidats qui savaient très bien se vendre.")], ""),
 ("theo", "Elle, elle n'a pas parlé, elle a agi.",
  "She did not talk, she acted.",
  [(267, "Elle, elle n'a pas parlé, elle a agi.")], ""),
 ("emilie", "Camille, vous étiez candidate?",
  "Camille, were you a candidate?",
  [(268, "Vous étiez candidate ?")], "Added Camille"),
 ("lea", "Non, pas du tout.",
  "No, not at all.",
  [(268, "Non, pas du tout.")], ""),
 ("theo", "Non, elle ne l'était pas, mais elle est venue seule à Paris.",
  "No, she was not, but she came to Paris alone.",
  [(269, "Non, elle ne l'était pas, mais elle est venue seule à Paris,")], ""),
 ("theo", "Elle s'y est fait une place sans révéler qui était son père.",
  "She made a place for herself there without revealing who her father was.",
  [(270, "elle s'y est fait une place,"), (271, "sans révéler qui était son père...")], ""),
 ("theo", "Serrer les dents, ne se confier à personne.",
  "Gritting your teeth, confiding in no one.",
  [(272, "Serrer les dents, ne se confier à personne,")], ""),
 ("theo", "Ce sont les qualités qu'il faut dans ce métier.",
  "Those are the qualities you need in this business.",
  [(274, "Ce sont les qualités qu'il faut dans ce métier.")], ""),
 ("theo", "Alors bienvenue, Camille, notre nouvelle agente.",
  "So welcome, Camille, our new agent.",
  [(275, "Alors bienvenue, Camille, notre nouvelle agente.")], ""),
 ("lea", "Merci, je ferai de mon mieux.",
  "Thank you, I will do my best.",
  [(276, "Je vois.")], "Adapted acceptance"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'And now, what would you say to officially welcoming our new junior?' Hicham opens the floor dramatically. "
  "The polite formula 'que diriez-vous de' invites opinions using the conditional form of dire."),
 (1, None,
  "'You should have consulted us beforehand.' Andrea objects to the unilateral move. "
  "The past conditional 'vous auriez du' expresses reproach for an omitted duty."),
 (2, None,
  "'I consulted myself. And I decided.' Hicham asserts his autocratic authority boldly. "
  "The reflexive passe compose 'je me suis consulte' emphasizes his sole decision-making."),
 (3, None,
  "'Our new junior is a woman.' Hicham begins unveiling his choice. "
  "The noun phrase 'notre nouveau junior' is followed by the predicate noun 'une femme'."),
 (4, None,
  "'And her name is Camille Valentini.' Hicham drops the bombshell announcement. "
  "The reflexive verb 's'appeler' is conjugated in the 3rd person singular."),
 (5, None,
  "'What? Camille?' Andrea gasps in shock. "
  "The interrogative pronoun 'quoi' conveys disbelief at the unexpected choice."),
 (6, None,
  "'There were candidates who knew very well how to sell themselves.' Hicham explains his reasoning. "
  "The imperfect 'savaient' introduces the pronominal reflexive infinitive 'se vendre'."),
 (7, None,
  "'She did not talk, she acted.' Hicham praises Camille's quiet initiative. "
  "The contrast between 'n'a pas parle' and 'a agi' uses the passe compose."),
 (8, None,
  "'Camille, were you a candidate?' Andrea questions Camille directly. "
  "The imperfect form 'etiez' asks about an ongoing status during the search."),
 (9, None,
  "'No, not at all.' Camille answers honestly. "
  "The emphatic negative idiom 'pas du tout' denies any prior ambition."),
 (10, None,
  "'No, she was not, but she came to Paris alone.' Hicham defends her independent spirit. "
  "The verb 'venir' takes the auxiliary etre in 'est venue seule'."),
 (11, None,
  "'She made a place for herself there without revealing who her father was.' Hicham admires her discretion. "
  "The preposition 'sans' governs the infinitive 'reveler' followed by an indirect question."),
 (12, None,
  "'Gritting your teeth, confiding in no one.' Hicham lists the qualities of resilience. "
  "The idiomatic infinitive 'serrer les dents' represents quiet perseverance under pressure."),
 (13, None,
  "'Those are the qualities you need in this business.' Hicham summarizes the agency virtues. "
  "The impersonal expression 'il faut' signifies essential requirements."),
 (14, None,
  "'So welcome, Camille, our new agent.' Hicham concludes his promotion speech. "
  "The interjection 'bienvenue' greets the newly elevated colleague warmly."),
 (15, None,
  "'Thank you, I will do my best.' Camille accepts the daunting challenge. "
  "The idiom 'faire de son mieux' promises wholehearted effort."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Hicham stuns the agency partners by appointing Camille as the new junior agent. "
         "Despite Andrea's surprise, Hicham praises Camille's tenacity, discretion, and quiet courage.")
CLOSING = ("theo", "Alors bienvenue, Camille, notre nouvelle agente.")
