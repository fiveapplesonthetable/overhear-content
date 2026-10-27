# Authoring module for dix-pour-cent s03e03 scene 07 (cues 367-373).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-07.py --out out/dix-pour-cent/s03e03/scene-07.json

ID = "dix-pour-cent-s03e03-scene-07"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 7
TITLE = "Erreur de casting  (Casting Mistake)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 367-373. At the ASK agency, Gabriel panics after realizing he mixed up the names "
               "Bassem and Baptiste for a major role opposite Gerard Lanvin. Adapted for A1 French.")

INTRO = ("At the ASK agency, Gabriel suddenly realizes he made a catastrophic blunder with the casting names. "
         "He rushes to Andrea to explain that he reached Mathias's voicemail after confusing two candidates. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("theo", "Andréa, on a un gros problème avec le casting.",
  "Andrea, we have a big problem with the casting.",
  [(367, "Le casting.")], "Problem statement"),
 ("lea", "Qu'est-ce qui se passe avec le film?",
  "What is going on with the film?",
  [(367, "Le casting.")], "Asking for details"),
 ("theo", "J'ai fait une énorme bêtise.",
  "I made a huge mistake.",
  [(368, "Bassem, c'est pas Baptiste.")], "Confessing mistake"),
 ("theo", "Bassem, ce n'est pas Baptiste.",
  "Bassem is not Baptiste.",
  [(368, "Bassem, c'est pas Baptiste.")], "Name confusion"),
 ("lea", "Comment ça? Baptiste a quarante-cinq ans!",
  "What do you mean? Baptiste is forty-five years old!",
  [(369, "Baptiste, il a 45 ans.")], "Character age"),
 ("theo", "Oui, c'est un rôle très important.",
  "Yes, it is a very important role.",
  [(370, "C'est un énorme rôle.")], "Role significance"),
 ("theo", "C'est le partenaire principal de Gérard Lanvin.",
  "He is the main partner of Gerard Lanvin.",
  [(371, "C'est le partenaire de l'an 20.")], "Lead co-star"),
 ("lea", "Mais comment tu as pu confondre les deux?",
  "But how could you confuse the two?",
  [(372, "C'est interdit aussi de choisir des noms de personnages aussi proches.")], "Incredulity"),
 ("theo", "Les deux prénoms se ressemblent trop.",
  "The two first names sound too much alike.",
  [(372, "C'est interdit aussi de choisir des noms de personnages aussi proches.")], "Similarity of names"),
 ("lea", "Tu as essayé d'appeler Mathias?",
  "Did you try calling Mathias?",
  [(366, "Mathias ?")], "Inquiring about Mathias"),
 ("theo", "Oui, je suis tombé sur sa messagerie.",
  "Yes, I reached his voicemail.",
  [(373, "Messagerie.")], "Voicemail result"),
 ("lea", "Il faut trouver une solution tout de suite.",
  "We must find a solution right away.",
  [(373, "Messagerie.")], "Urgent call to action"),
 ("theo", "Je vais essayer de réparer mon erreur.",
  "I am going to try to fix my mistake.",
  [(373, "Messagerie.")], "Promise to fix it"),
 ("lea", "Dépêche-toi, le casting commence maintenant.",
  "Hurry up, the casting is starting now.",
  [(373, "Messagerie.")], "Urging speed"),
]

WALK = [
 (0, None,
  "'Andrea, we have a big problem with the casting.' Gabriel breaks the bad news to Andrea. "
  "The masculine noun phrase 'un gros probleme' signals an urgent complication."),
 (1, None,
  "'What is going on with the film?' Andrea asks what happened. "
  "The expression 'qu'est-ce qui se passe' inquires about the situation."),
 (2, None,
  "'I made a huge mistake.' Gabriel admits his serious blunder. "
  "The passe compose 'j'ai fait' expresses a completed past action."),
 (3, None,
  "'Bassem is not Baptiste.' Gabriel explains the mix-up between two similar names. "
  "The negative structure 'ce n'est pas' corrects the mistaken identity."),
 (4, None,
  "'What do you mean? Baptiste is forty-five years old!' Andrea reacts in shock. "
  "French expresses age using the verb 'avoir'."),
 (5, None,
  "'Yes, it is a very important role.' Gabriel acknowledges the importance of the part. "
  "The adjective 'important' follows the masculine noun 'role'."),
 (6, None,
  "'He is the main partner of Gerard Lanvin.' Gabriel names the major movie star. "
  "The adjective 'principal' indicates the primary co-star role."),
 (7, None,
  "'But how could you confuse the two?' Andrea demands an explanation. "
  "The compound tense 'tu as pu' questions his decision-making."),
 (8, None,
  "'The two first names sound too much alike.' Gabriel explains the confusion. "
  "The reciprocal verb 'se ressembler' indicates mutual resemblance."),
 (9, None,
  "'Did you try calling Mathias?' Andrea asks whether Mathias was alerted. "
  "The infinitive 'appeler' follows the verb 'essayer de'."),
 (10, None,
  "'Yes, I reached his voicemail.' Gabriel explains that Mathias did not answer. "
  "The idiom 'tomber sur' means to end up at or encounter."),
 (11, None,
  "'We must find a solution right away.' Andrea urges prompt action. "
  "The impersonal verb 'il faut' expresses strong necessity."),
 (12, None,
  "'I am going to try to fix my mistake.' Gabriel vows to make amends. "
  "The near future 'je vais essayer' announces his immediate effort."),
 (13, None,
  "'Hurry up, the casting is starting now.' Andrea gives urgent marching orders. "
  "The reflexive imperative 'depeche-toi' instructs someone to hurry."),
]

OUTRO = ("Gabriel rushes off after alerting Andrea about the casting catastrophe. "
         "With Gerard Lanvin's film on the line, resolving the blunder will test the agency to its limits. "
         "Now, let's review the scene once more.")

CLOSING = ("theo", "Je vais essayer de réparer mon erreur.")
