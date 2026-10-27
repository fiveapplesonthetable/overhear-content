# Authoring module for dix-pour-cent s02e03 scene 09 (cues 225-241).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-09.py --out out/dix-pour-cent/s02e03/scene-09.json

ID = "dix-pour-cent-s02e03-scene-09"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 9
TITLE = "Limites professionnelles  (Professional Boundaries)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 225-241. In the hallway, Andréa strictly warns Gabriel never to flirt with clients, "
               "especially her promising new talent Aymeline Val. "
               "Adapted for A1 French.")

INTRO = ("In the hallway at ASK, Andrea confronts Gabriel after catching him flirting with her new client. "
         "She lays down the firm's strict rules regarding professional boundaries and client relationships. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Voilà la règle numéro un ici.",
  "Here is rule number one here.",
  [(225, "voilà la règle numéro un.")], "Added ici"),
 ("lea", "On ne drague jamais les clients. Jamais.",
  "We never flirt with clients. Never.",
  [(226, "On ne drague jamais les clients. Jamais.")], ""),
 ("theo", "J'offrais juste un accueil très chaleureux.",
  "I was just offering a very warm welcome.",
  [(227, "J'offrais juste un accueil chaleureux.")], "Added très"),
 ("theo", "Quel mal ça peut faire?",
  "What harm can it do?",
  [(229, "Quel mal ça peut faire ?")], ""),
 ("lea", "C'est un talent brut magnifique.",
  "She is a magnificent raw talent.",
  [(230, "C'est un talent brut.")], "Added magnifique"),
 ("lea", "Il m'a fallu des mois pour obtenir ce rendez-vous.",
  "It took me months to get this meeting.",
  [(231, "Il m'a fallu des mois pour obtenir un rendez-vous.")], "Adapted un to ce"),
 ("lea", "Tous les agents de Paris la veulent.",
  "Every agent in Paris wants her.",
  [(233, "Tous les agents de Paris la veulent.")], ""),
 ("lea", "J'ai fait tout le travail parce que je crois en elle.",
  "I did all the work because I believe in her.",
  [(234, "J'ai fait tout le travail"), (234, "parce que je crois en elle.")], ""),
 ("lea", "Je ne veux pas que tu fasses tout rater.",
  "I do not want you to ruin everything.",
  [(235, "Je ne veux pas que tu fasses tout rater.")], ""),
 ("theo", "Tu dragues aussi tes clients, Andréa.",
  "You flirt with your clients too, Andrea.",
  [(236, "Tu dragues aussi")], "Added tes clients, Andréa"),
 ("theo", "Dis-moi que tu n'es pas attirée par elle.",
  "Tell me you are not attracted to her.",
  [(238, "Dis-moi que tu n'es pas attiré par elle.")], "Adapted agreement"),
 ("lea", "Bien sûr que si, sinon je ne voudrais pas la représenter.",
  "Of course I am, otherwise I would not want to represent her.",
  [(239, "Bien sûr que si, sinon je ne voudrais pas la représenter.")], ""),
 ("lea", "Mais je ne veux pas coucher avec elle.",
  "But I do not want to sleep with her.",
  [(240, "Mais je ne veux pas coucher avec elle.")], ""),
 ("lea", "C'est la grande différence entre toi et moi.",
  "That is the big difference between you and me.",
  [(241, "C'est la différence entre toi et moi.")], "Added grande"),
 ("theo", "Je fais attention, ne t'inquiète pas.",
  "I am being careful, do not worry.",
  [(228, "Du calme.")], "Adapted reassurance"),
 ("lea", "Reste loin d'elle, c'est tout ce que je te demande.",
  "Stay away from her, that is all I ask of you.",
  [(235, "Je ne veux pas")], "Adapted closing warning"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Here is rule number one here.' Andrea establishes the fundamental agency principle. "
  "The presentative 'voila' introduces 'la regle numero un' with authority."),
 (1, None,
  "'We never flirt with clients. Never.' Andrea states the ethical boundary emphatically. "
  "The pronoun 'on' stands for we, negated by 'ne ... jamais' around the slang verb 'draguer'."),
 (2, None,
  "'I was just offering a very warm welcome.' Gabriel minimizes his playful charm. "
  "The imperfect tense 'j'offrais' describes an ongoing polite intention."),
 (3, None,
  "'What harm can it do?' Gabriel questions the strict prohibition casually. "
  "The interrogative determiner 'quel' agrees with the masculine noun 'mal'."),
 (4, None,
  "'She is a magnificent raw talent.' Andrea defends her new client's artistic promise. "
  "The adjective 'brut' describes unpolished potential, paired with 'magnifique'."),
 (5, None,
  "'It took me months to get this meeting.' Andrea emphasizes her patient effort. "
  "The impersonal expression 'il m'a fallu' conveys the time required."),
 (6, None,
  "'Every agent in Paris wants her.' Andrea underscores the intense competition. "
  "The plural determiner 'tous les' precedes the noun 'agents'."),
 (7, None,
  "'I did all the work because I believe in her.' Andrea asserts her professional dedication. "
  "The verb 'croire en' means to believe in someone's potential."),
 (8, None,
  "'I do not want you to ruin everything.' Andrea warns against reckless interference. "
  "The verb 'vouloir que' triggers the subjunctive verb form 'tu fasses'."),
 (9, None,
  "'You flirt with your clients too, Andrea.' Gabriel deflects the criticism playfully. "
  "The adverb 'aussi' adds a touch of reciprocal accusation."),
 (10, None,
  "'Tell me you are not attracted to her.' Gabriel challenges her personal motives. "
  "The imperative 'dis-moi' introduces a negative subordinate clause."),
 (11, None,
  "'Of course I am, otherwise I would not want to represent her.' Andrea readily concedes. "
  "The affirmative response 'bien sur que si' contradicts a negative question."),
 (12, None,
  "'But I do not want to sleep with her.' Andrea draws a sharp line between attraction and action. "
  "The colloquial infinitive 'coucher avec' denotes sleeping with someone."),
 (13, None,
  "'That is the big difference between you and me.' Andrea summarizes her professional discipline. "
  "The preposition 'entre' connects the two stressed pronouns 'toi' and 'moi'."),
 (14, None,
  "'I am being careful, do not worry.' Gabriel attempts to reassure his colleague. "
  "The negative reflexive imperative 'ne t'inquiete pas' urges calm."),
 (15, None,
  "'Stay away from her, that is all I ask of you.' Andrea delivers her final firm instruction. "
  "The relative structure 'ce que' functions as the object of 'je te demande'."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Andrea lays down the law on agency conduct: romantic entanglements with clients are strictly forbidden. "
         "Gabriel promises to behave, but his romantic impulses remain hard to tame.")
CLOSING = ("lea", "C'est la grande différence entre toi et moi.")
