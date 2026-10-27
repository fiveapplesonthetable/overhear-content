# Authoring module for dix-pour-cent s03e03 scene 09 (cues 391-412).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-09.py --out out/dix-pour-cent/s03e03/scene-09.json

ID = "dix-pour-cent-s03e03-scene-09"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 9
TITLE = "L'audition imprévue  (The Unexpected Audition)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Assistante de casting", "theo": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 391-412. In a casting studio, Camille auditions for the role in Gerard Lanvin's film "
               "while the wardrobe assistant takes his costume measurements. Adapted for A1 French.")

INTRO = ("At the casting studio, Camille takes the stage to pitch himself despite having zero acting experience. "
         "While the casting team reacts with amusement and skepticism, an assistant measures him for costume fitting. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("theo", "Voilà, je me présente à vous.",
  "Here I am, let me introduce myself to you.",
  [(391, "Donc, voilà, je me présente.")], "Introduction"),
 ("theo", "Je n'ai pas d'expérience dans ce métier.",
  "I have no experience in this profession.",
  [(392, "J'ai aucune expérience dans le métier.")], "No experience"),
 ("theo", "Mais je veux être comédien depuis toujours.",
  "But I have always wanted to be an actor.",
  [(393, "je sais que je vais être comédien.")], "Ambition"),
 ("theo", "J'ai beaucoup de charisme naturel.",
  "I have a lot of natural charisma.",
  [(396, "impressionné par mon charisme.")], "Claiming charisma"),
 ("lea", "On le voit vraiment pour le rôle de Baptiste?",
  "Are we really seeing him for the role of Baptiste?",
  [(401, "On le voit pour Baptiste, lui ?")], "Casting team skepticism"),
 ("theo", "Je peux vous raconter une histoire drôle.",
  "I can tell you a funny story.",
  [(394, "D'ailleurs, je peux vous raconter une petite anecdote")], "Offering joke"),
 ("lea", "C'est une blague, ce garçon?",
  "Is this boy a joke?",
  [(402, "C'est une blague.")], "Disbelief"),
 ("lea", "Je sais, c'est une idée de Gérard.",
  "I know, it is an idea from Gerard.",
  [(403, "Je sais, mais c'est une idée de Gérard.")], "Mentioning Gerard Lanvin"),
 ("lea", "Quelle est votre pointure de chaussures?",
  "What is your shoe size?",
  [(405, "La taille en chaussures, c'est bien 42, hein ?")], "Asking shoe size"),
 ("theo", "Ma taille est quarante-deux en France.",
  "My size is forty-two in France.",
  [(405, "La taille en chaussures, c'est bien 42, hein ?"), (406, "Oui.")], "Confirming size"),
 ("lea", "Veuillez baisser les bras, s'il vous plaît.",
  "Please lower your arms.",
  [(408, "Baisser les bras.")], "Posing direction"),
 ("lea", "Je prends vos mesures rapidement.",
  "I am taking your measurements quickly.",
  [(411, "Je prends la taille et je vous libère.")], "Measuring"),
 ("lea", "Ne rentrez pas le ventre pendant la mesure.",
  "Do not suck in your stomach during the measurement.",
  [(413, "Alors, rentrez pas le ventre.")], "Measurement advice"),
 ("theo", "Merci beaucoup pour votre accueil.",
  "Thank you very much for your welcome.",
  [(412, "Merci.")], "Thanking the team"),
]

WALK = [
 (0, None,
  "'Here I am, let me introduce myself to you.' The candidate opens his audition. "
  "The reflexive verb 'se presenter' is standard when introducing oneself."),
 (1, None,
  "'I have no experience in this profession.' The candidate admits his amateur background. "
  "The noun 'experience' is introduced by the partitive with negation."),
 (2, None,
  "'But I have always wanted to be an actor.' The candidate expresses his lifelong passion. "
  "The prepositional phrase 'depuis toujours' means since always or all along."),
 (3, None,
  "'I have a lot of natural charisma.' The candidate brags about his presence. "
  "The adverb 'beaucoup de' quantifies the masculine noun 'charisme'."),
 (4, None,
  "'Are we really seeing him for the role of Baptiste?' The casting assistant whispers in disbelief. "
  "The verb 'voir' refers to auditioning a candidate."),
 (5, None,
  "'I can tell you a funny story.' The candidate offers to entertain the room. "
  "The adjective 'drole' describes an amusing tale."),
 (6, None,
  "'Is this boy a joke?' The assistant questions whether the audition is serious. "
  "The feminine noun 'blague' denotes a joke or prank."),
 (7, None,
  "'I know, it is an idea from Gerard.' The colleague explains who suggested the candidate. "
  "The preposition 'de' indicates origin."),
 (8, None,
  "'What is your shoe size?' The assistant turns to wardrobe details. "
  "The noun 'pointure' specifically designates shoe size."),
 (9, None,
  "'My size is forty-two in France.' The candidate states his measurements. "
  "The cardinal number 'quarante-deux' indicates standard European shoe sizing."),
 (10, None,
  "'Please lower your arms.' The assistant gives posing directions. "
  "The polite formula 'veuillez' followed by the infinitive softens an order."),
 (11, None,
  "'I am taking your measurements quickly.' The assistant works efficiently with the measuring tape. "
  "The feminine plural noun 'mesures' denotes body dimensions."),
 (12, None,
  "'Do not suck in your stomach during the measurement.' The assistant instructs him on natural posture. "
  "The negative imperative 'ne rentrez pas' prevents inaccurate sizing."),
 (13, None,
  "'Thank you very much for your welcome.' The candidate concludes politely. "
  "The masculine noun 'accueil' refers to reception or hospitality."),
]

OUTRO = ("Camille finishes his offbeat audition and measurement session with good humor. "
         "Whether his natural charm will convince the director remains to be seen. "
         "Now, let's review the scene once more.")

CLOSING = ("theo", "Merci beaucoup pour votre accueil.")
