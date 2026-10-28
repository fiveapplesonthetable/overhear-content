# Authoring module for dix-pour-cent s03e02 scene 23 (cues 1007-1056).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-23.py --out out/dix-pour-cent/s03e02/scene-23.json

ID = "dix-pour-cent-s03e02-scene-23"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 23
TITLE = "Il tient à vous  (He Cares About You)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "catherine": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 1007-1056. Mathias and Catherine visit Noémie's apartment after her hospital stay. "
               "Catherine gently questions Noémie's decision to leave ASK and reveals how deeply Mathias cares about her. Adapted for A1 French.")

INTRO = ("Recovering at home after a traumatic accident, assistant Noemie welcomes Mathias Barneville and his wife Catherine into her apartment. "
         "While Mathias tries to minimize the awkwardness, Catherine directly brings up Noemie's career plans and reveals Mathias's true devotion. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("mathias", "Je vous pose ce sac sur la table.",
  "I put this bag on the table for you.",
  [(1012, "Je vous pose ça où ?"), (1015, "Sur la table.")], "Set down groceries on table"),
 ("lea", "Merci Mathias, c'est très gentil à vous.",
  "Thank you Mathias, that is very kind of you.",
  [(1016, "Mathias, merci.")], "Expressed gratitude for visit"),
 ("catherine", "Voulez-vous manger une bonne soupe chaude, Noémie?",
  "Do you want to eat a good hot soup, Noemie?",
  [(1020, "Vous voulez qu'on vous prépare quelque chose"), (1022, "faire des soupes")], "Offered hot soup"),
 ("lea", "Non merci Catherine, ne vous embêtez pas.",
  "No thank you Catherine, do not trouble yourself.",
  [(1023, "Non, non, ça va."), (1024, "Vous embêtez pas.")], "Declined offer politely"),
 ("mathias", "Nous allons te laisser te reposer maintenant.",
  "We are going to let you rest now.",
  [(1027, "On va y aller."), (1028, "On va laisser Noémie se reposer")], "Proposed leaving apartment"),
 ("lea", "Je ne suis pas paralysée non plus!",
  "I am not paralyzed either!",
  [(1034, "Je suis pas paralysée, non plus.")], "Joked about physical condition"),
 ("catherine", "Mathias m'a tout raconté aux urgences.",
  "Mathias told me everything at the emergency room.",
  [(1039, "Quand on était aux urgences, Mathias m'a tout raconté.")], "Disclosed hospital talk"),
 ("lea", "Qu'est-ce qu'il vous a raconté exactement?",
  "What did he tell you exactly?",
  [(1040, "Noémie")], "Inquired about disclosed facts"),
 ("catherine", "Vous voulez vraiment quitter l'agence ASK?",
  "Do you really want to leave agency ASK?",
  [(1044, "quitter ASK")], "Asked about career departure"),
 ("lea", "Un chasseur de têtes m'a contactée.",
  "A headhunter contacted me.",
  [(1047, "c'est un chasseur de têtes.")], "Explained job inquiry"),
 ("mathias", "Noémie est très demandée pour son talent.",
  "Noemie is in high demand for her talent.",
  [(1049, "Noémie est très compétente.")], "Defended assistant professional value"),
 ("catherine", "Ce n'est peut-être pas le bon moment.",
  "This is perhaps not the right time.",
  [(1052, "c'est peut-être pas le moment, Noémie,")], "Suggested patient timing"),
 ("lea", "Je vais réfléchir à toute cette situation.",
  "I am going to think about this whole situation.",
  [(1057, "Je vais réfléchir.")], "Promised careful reflection"),
 ("catherine", "Mathias tient énormément à vous, Noémie.",
  "Mathias cares enormously about you, Noemie.",
  [(1056, "Noémie, moi, je sais à quel point il tient à vous.")], "Affirmed husband deep devotion"),
]

OPENER = "Let's see how Catherine gently challenges Noemie while revealing the profound loyalty of Mathias."

WALK = [
 (0, None,
  "'I put this bag on the table for you.' A considerate announcement setting down groceries. Notice how 'place' leads directly into the noun meaning 'bag'."),
 (1, None,
  "'Thank you Mathias, that is very kind of you.' A polite acknowledgment expressing domestic gratitude. Notice how the short vowel drops before a vowel sound around 'it is', making the phrase flow smoothly as one unit."),
 (2, None,
  "'Do you want to eat a good hot soup, Noemie?' The adjective meaning 'good' takes its feminine form here to match the noun it describes."),
 (3, None,
  "'No thank you Catherine, do not trouble yourself.' The two-part French negation brackets the verb for 'trouble' on both sides. The two-part French negation brackets the verb for 'trouble' on both sides."),
 (4, None,
  "'We are going to let you rest now.' French forms the near future by pairing the present tense of 'to go' directly with 'to rest'. French forms the near future by pairing the present tense of 'to go' directly with 'to rest'."),
 (5, None,
  "'I am not paralyzed either!' This conversational past tense combines a helper verb with the past participle for 'paralyzed'. This conversational past tense combines a helper verb with the past participle for 'paralyzed'."),
 (6, None,
  "'Mathias told me everything at the emergency room.' A candid disclosure revealing hospital confidences. Notice how 'has' leads directly into the noun meaning 'emergency room'."),
 (7, None,
  "'What did he tell you exactly?' The standard spoken question formula at the front turns the statement about 'has' into a natural inquiry."),
 (8, None,
  "'Do you really want to leave agency ASK?' The verb meaning 'want' pairs naturally with the noun for 'the agency' in everyday conversation."),
 (9, None,
  "'A headhunter contacted me.' An objective explanation explaining external recruitment. This conversational past tense combines a helper verb with the past participle for 'contacted'."),
 (10, None,
  "'Noemie is in high demand for her talent.' This conversational past tense combines a helper verb with the past participle for 'sought-after'. This conversational past tense combines a helper verb with the past participle for 'sought-after'."),
 (11, None,
  "'This is perhaps not the right time.' A cautious opinion advising patient deliberation. The descriptive adjective for 'good' agrees in gender and number with its noun."),
 (12, None,
  "'I am going to think about this whole situation.' A thoughtful concession promising careful reflection. Notice how 'am going' leads directly into the noun meaning 'situation'."),
 (13, None,
  "'Mathias cares enormously about you, Noemie.' A profound revelation affirming deep professional loyalty. Catherine uses the polite 'you' form alongside 'cares' to keep a respectful professional tone."),
]

TRANSITION = "Now let's listen to Catherine, Mathias, and Noemie again at natural pace."

OUTRO = ("Moved by Catherine's compassionate insight and Mathias's quiet devotion, Noemie reconsiders her hasty departure from ASK. "
         "Beneath the rivalries and chaos, profound human bonds remain the heartbeat of the agency.")

CLOSING = ("catherine", "Prenez bien soin de vous, Noémie.")
