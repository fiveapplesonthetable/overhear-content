# Authoring module for dix-pour-cent s02e01 scene 11 (cues 285-303).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-11.py --out out/dix-pour-cent/s02e01/scene-11.json

ID = "dix-pour-cent-s02e01-scene-11"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 11
TITLE = "Andréa prépare son voyage  (Andréa Prepares Her Trip)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Andréa", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 285-303. In her office, Andréa complains to Camille about having to travel to her hometown "
               "of Couchey for her mother's honorary medal ceremony. She refuses to spend the night there and insists "
               "on a same-day return ticket to Paris. Adapted for A1 French.")

INTRO = ("In her office at ASK, Andrea is preparing for an unwelcome family obligation. "
         "Her mother is being awarded an honorary medal in her provincial hometown of Couchey. "
         "Andrea loathes returning home and refuses to sleep there under any circumstances. "
         "Let's listen to her conversation with Camille in French first.")

STORY = [
 ("lea", "Tu as mon billet pour demain?",
  "Do you have my ticket for tomorrow?",
  [(285, "Tu as mon billet pour demain ?")], ""),
 ("camille", "Oui, le voilà. Tu vas où?",
  "Yes, here it is. Where are you going?",
  [(285, "Ouais, tiens."), (286, "Tu vas où ?")], ""),
 ("lea", "À Couchey. Le village de mes parents.",
  "To Couchey. The village of my parents.",
  [(286, "À Couchey."), (288, "Le village de mes parents.")], ""),
 ("camille", "En huit ans, personne ne savait d'où tu venais.",
  "In eight years, nobody knew where you came from.",
  [(289, "En huit ans je n'ai jamais su d'où tu venais.")], "Adapted to general knowledge"),
 ("lea", "Moi non plus, j'aimerais oublier.",
  "Me neither, I would like to forget.",
  [(290, "Moi non plus.")], "Added humorous quip"),
 ("camille", "Qu'est-ce que tu vas faire à Couchey?",
  "What are you going to do in Couchey?",
  [(291, "Qu'est-ce que tu vas faire à Couchey ?")], ""),
 ("lea", "Ma mère reçoit la médaille de la ville.",
  "My mother is receiving the town medal.",
  [(291, "Elle reçoit la médaille de la ville.")], ""),
 ("camille", "C'est classe!",
  "That is classy!",
  [(292, "Classe.")], ""),
 ("lea", "Un calvaire, tu veux dire.",
  "An ordeal, you mean.",
  [(293, "Un calvaire, tu veux dire.")], ""),
 ("camille", "Tu as un rendez-vous avec Léa Seydoux?",
  "Do you have a meeting with Léa Seydoux?",
  [(295, "T'as dit à Léa Seydoux que je passerais sur le tournage ?")], "Simplified to A1"),
 ("lea", "Oui, sur son tournage à côté de Couchey.",
  "Yes, on her film shoot near Couchey.",
  [(296, "Ouais, à 45 minutes de Couchey.")], ""),
 ("camille", "J'ai réservé un hôtel pour la nuit.",
  "I booked a hotel for the night.",
  [(297, "pas dormir là-bas !")], "Inferred assistant action"),
 ("lea", "Je voulais faire l'aller-retour dans la journée!",
  "I wanted to make a round trip in a single day!",
  [(297, "je voulais faire l'aller-retour dans la journée")], "Cleaned vulgarity"),
 ("camille", "Mais le dernier train part très tôt.",
  "But the last train leaves very early.",
  [(298, "Mais tu dois changer deux fois dans le dernier train.")], "Simplified reason"),
 ("lea", "La maison de mes parents me déprime. Re-réserve un billet!",
  "My parents' house depresses me. Rebook a ticket!",
  [(299, "re-réserve."), (300, "La maison de mes parents me déprime.")], ""),
 ("camille", "D'accord, je m'en occupe tout de suite.",
  "All right, I am taking care of it right away.",
  [(302, "Merci. Changez ça !")], "Polite agreement"),
]

OPENER = "Let's follow the scene as Andrea dreads visiting her childhood home."

WALK = [
 (0, None,
  "'Do you have my ticket for tomorrow?' Andrea begins with a practical administrative question."),
 (1, None,
  "'Yes, here it is. Where are you going?' Camille hands over the travel document and asks about the destination."),
 (2, None,
  "'To Couchey. The village of my parents.' Andrea reveals the name of her small provincial hometown."),
 (3, None,
  "'In eight years, nobody knew where you came from.' A negative expression of time highlighting Andrea's secrecy."),
 (4, None,
  "'Me neither, I would like to forget.' A conditional verb expressing a strong wish to put the past behind her."),
 (5, None,
  "'What are you going to do in Couchey?' A standard near-future question with an interrogative pronoun."),
 (6, None,
  "'My mother is receiving the town medal.' The present tense describes an upcoming civic ceremony."),
 (7, None,
  "'That is classy!' Camille thinks an honorary medal sounds prestigious."),
 (8, None,
  "'An ordeal, you mean.' Andrea immediately contradicts her with a dramatic noun."),
 (9, None,
  "'Do you have a meeting with Lea Seydoux?' Camille mentions a major client filming nearby."),
 (10, None,
  "'Yes, on her film shoot near Couchey.' The prepositional phrase meaning next to or nearby."),
 (11, None,
  "'I booked a hotel for the night.' A compound past action using the auxiliary to have."),
 (12, None,
  "'I wanted to make a round trip in a single day!' An imperfect expression of original intention."),
 (13, None,
  "'But the last train leaves very early.' Camille explains the tight train schedule in Burgundy."),
 (14, "La maison de mes parents me déprime.",
  "'My parents' house depresses me.' A vivid present tense description of her family home."),
 (14, "Re-réserve un billet!",
  "'Rebook a ticket!' An imperative ordering an immediate change of plans."),
 (15, None,
  "'All right, I am taking care of it right away.' Camille agrees with a useful pronominal idiom."),
]

TRANSITION = "Let's listen to Andrea and Camille one more time."

OUTRO = ("Andrea will visit Couchey, but she is determined to sleep back in Paris that same night. "
         "In the next scene, we will join Virginie Efira's disastrous promotional interviews.")
CLOSING = ("lea", "Merci, Camille.")
