# Authoring module for dix-pour-cent s02e04 scene 11 (cues 313-340).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-11.py --out out/dix-pour-cent/s02e04/scene-11.json

ID = "dix-pour-cent-s02e04-scene-11"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 11
TITLE = "Le sabotage d'Eugénie  (Sabotaging Eugenie)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "emilie": "emilie", "theo": "theo"}
LABELS = {"lea": "Camille", "emilie": "Noémie", "theo": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 313-340. At the agency, Camille stresses over her interview for the assistant position. "
               "Noémie spots a qualified rival, Eugénie, and plots to sabotage her. "
               "Adapted for A1 French.")

INTRO = ("At the ASK offices, Camille is terrified by the impressive resumes of outside applicants for the junior agent post. "
         "Her friends Noemie and Herve spot a top contender and consider dirty tricks to help Camille. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Attends, viens là, Camille.",
  "Wait, come over here, Camille.",
  [(313, "Attends... viens là.")], "Added Camille"),
 ("theo", "Imiter Hicham à ton entretien? Tu ne devrais pas être toi-même?",
  "Imitate Hicham at your interview? Shouldn't you be yourself?",
  [(326, "Imiter Hicham à ton entretien ?"), (327, "Tu ne devrais pas être toi-même ?")], ""),
 ("lea", "J'ai la tête qui tourne.",
  "My head is spinning.",
  [(328, "J'ai la tête qui tourne.")], ""),
 ("lea", "Les CV des candidats, c'est du niveau Harvard!",
  "The candidates' resumes are Harvard level!",
  [(329, "Les CV des candidats, c'est du niveau Harvard !")], ""),
 ("emilie", "Tu as l'avantage de travailler ici.",
  "You have the advantage of working here.",
  [(336, "Tu as l'avantage de travailler ici.")], ""),
 ("emilie", "Regarde, c'est Eugénie Léon-Brun.",
  "Look, that is Eugénie Léon-Brun.",
  [(330, "C'est Eugénie Léon-Brun.")], "Added Regarde"),
 ("emilie", "Droit, spécialisée en propriété intellectuelle.",
  "Law school, specialized in intellectual property.",
  [(331, "Droit, spécialisée en propriété intellectuelle.")], ""),
 ("emilie", "Trois ans en production, puis deux chez VMA.",
  "Three years in production, then two at VMA.",
  [(332, "Trois ans en production, puis deux chez VMA.")], ""),
 ("emilie", "Et en plus elle est mignonne, Hicham va adorer.",
  "And plus she is pretty, Hicham is going to love her.",
  [(333, "Et en plus elle est mignonne, Hicham va adorer.")], ""),
 ("emilie", "Je peux la déstabiliser si tu veux.",
  "I can destabilize her if you want.",
  [(334, "Je peux la déstabiliser si tu veux.")], ""),
 ("lea", "Tu ne peux pas faire ça, ça ne se fait pas!",
  "You cannot do that, it is not done!",
  [(335, "Tu ne peux pas faire ça, ça ne se fait pas !")], ""),
 ("emilie", "Oui, ce serait ignoble. Quand même...",
  "Yes, that would be disgraceful. Still...",
  [(337, "Oui, ce serait ignoble."), (338, "Quand même...")], ""),
 ("theo", "Allez, Noémie, démolis la rivale!",
  "Go on, Noémie, crush the rival!",
  [(339, "Allez, Noémie")], "Adapted cheering"),
 ("emilie", "Je vais lui parler de la PNL et du langage corporel.",
  "I will talk to her about NLP and body language.",
  [(316, "langage corporel"), (322, "c'est la PNL.")], ""),
 ("lea", "Tu as vraiment fait une formation?",
  "Did you really take a training course?",
  [(324, "j'ai fait une formation.")], "Adapted question"),
 ("emilie", "C'est comme ça que j'ai appris à contrôler mes émotions.",
  "That is how I learned to control my emotions.",
  [(325, "C'est comme ça que j'ai appris à contrôler mes émotions.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Wait, come over here, Camille.' Herve calls Camille over to discuss her interview. "
  "The imperative 'viens la' invites someone closer to have a private conversation."),
 (1, None,
  "'Imitate Hicham at your interview? Shouldn't you be yourself?' Herve questions the psychological tactic. "
  "The conditional 'tu ne devrais pas' offers gentle, friendly advice."),
 (2, None,
  "'My head is spinning.' Camille confesses her mounting panic. "
  "The idiom 'avoir la tete qui tourne' indicates dizziness or anxiety."),
 (3, None,
  "'The candidates' resumes are Harvard level!' Camille marvels at the fierce competition. "
  "The acronym 'CV' stands for curriculum vitae, modified by the prepositional phrase 'du niveau'."),
 (4, None,
  "'You have the advantage of working here.' Noemie reminds Camille of her insider status. "
  "The noun 'avantage' is followed by the preposition 'de' plus infinitive 'travailler'."),
 (5, None,
  "'Look, that is Eugenie Leon-Brun.' Noemie identifies the most formidable rival. "
  "The imperative 'regarde' directs attention toward the newly arrived applicant."),
 (6, None,
  "'Law school, specialized in intellectual property.' Noemie recites Eugenie's stellar academic qualifications. "
  "The past participle 'specialisee' functions as an adjective agreeing with the feminine candidate."),
 (7, None,
  "'Three years in production, then two at VMA.' Noemie details Eugenie's extensive industry experience. "
  "The preposition 'chez' indicates employment at a specific company or agency."),
 (8, None,
  "'And plus she is pretty, Hicham is going to love her.' Noemie points out Eugenie's obvious appeal. "
  "The informal connective 'et en plus' introduces an added advantage."),
 (9, None,
  "'I can destabilize her if you want.' Noemie offers to take matters into her own hands. "
  "The conditional clause 'si tu veux' makes a polite or conspiratorial suggestion."),
 (10, None,
  "'You cannot do that, it is not done!' Camille refuses to win through dirty tricks. "
  "The impersonal expression 'ca ne se fait pas' denotes socially unacceptable behavior."),
 (11, None,
  "'Yes, that would be disgraceful. Still...' Noemie wavers between professional ethics and agency loyalty. "
  "The conditional 'ce serait' pairs with the strong evaluative adjective 'ignoble'."),
 (12, None,
  "'Go on, Noemie, crush the rival!' Herve enthusiastically encourages the sabotage. "
  "The imperative interjection 'allez' encourages direct action."),
 (13, None,
  "'I will talk to her about NLP and body language.' Noemie devises a psychological scheme. "
  "The near future 'je vais lui parler' indicates imminent action."),
 (14, None,
  "'Did you really take a training course?' Camille asks skeptically about Noemie's qualifications. "
  "The passe compose 'tu as fait' combines with the adverb 'vraiment'."),
 (15, None,
  "'That is how I learned to control my emotions.' Noemie claims newfound emotional mastery. "
  "The verb 'apprendre a' takes an infinitive complement 'controler'."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Facing stiff outside competition for the junior agent post, Camille feels inadequate next to Eugenie's credentials. "
         "Despite Camille's moral objections, Noemie sets out to sabotage the applicant's interview.")
CLOSING = ("emilie", "C'est comme ça que j'ai appris à contrôler mes émotions.")
