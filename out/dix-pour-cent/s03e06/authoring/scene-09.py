# Authoring module for dix-pour-cent s03e06 scene 09 (cues 462-489).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-09.py --out overhear-content/out/dix-pour-cent/s03e06/scene-09.json

ID = "dix-pour-cent-s03e06-scene-09"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 9
TITLE = "La négociation d'Arlette  (Arlette's Negotiation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "laurence": "emilie"}
LABELS = {"lea": "Arlette", "laurence": "Laurence"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 462-489. In a production office, Arlette persuades producer Laurence to endorse "
               "the homonym contract scheme, bargaining top agency talent to seal the agreement.")

INTRO = ("In a production office, veteran agent Arlette Azemar meets with respected producer Laurence. "
         "Arlette urgently needs Laurence to endorse a contract under a homonym name to protect the agency, "
         "prompting an intense negotiation over top French talent. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("laurence", "Votre histoire d'homonyme ne marchera jamais.",
  "Your lookalike scheme will never work.",
  [(463, "Ça marchera jamais, votre histoire d'homonyme.")], "Expressing deep skepticism"),
 ("lea", "Tu penses complètement à l'envers, Laurence.",
  "You are thinking completely backwards, Laurence.",
  [(466, "Tu penses à l'envers, Laurence.")], "Rebutting producer reasoning"),
 ("laurence", "Je ne connais pas cette dame.",
  "I do not know this lady.",
  [(468, "Arlette, je la connais pas, cette dame.")], "Disowning the unknown actress"),
 ("lea", "Elle sauvera toute notre agence aujourd'hui.",
  "She will save our entire agency today.",
  [(467, "C'est si tu cautionnes pas que ça peut pas marcher.")], "Highlighting high stakes"),
 ("laurence", "Je refuse de signer un faux contrat.",
  "I refuse to sign a fake contract.",
  [(469, "J'ai pas lu signer un faux contrat de travail.")], "Rejecting fraudulent paperwork"),
 ("lea", "Que veux-tu en échange de ton aide?",
  "What do you want in exchange for your help?",
  [(472, "C'est ce que tu veux ?")], "Initiating bargaining"),
 ("laurence", "Je veux Guillaume Canet pour mon film.",
  "I want Guillaume Canet for my film.",
  [(474, "On est en égo avec Guillaume Canet pour le film de Nicole Garcia ?")], "Demanding leading star"),
 ("lea", "Impossible, il est chez Barneville maintenant.",
  "Impossible, he is with Barneville now.",
  [(477, "Il est chez Barneville.")], "Explaining client assignment"),
 ("laurence", "Alors je ne signe rien du tout.",
  "Then I am not signing anything at all.",
  [(475, "Non, pas possible.")], "Holding ground"),
 ("lea", "Et si je te propose Cécile de France?",
  "And what if I offer you Cecile de France?",
  [(480, "Par contre, Cécile de France, dans l'institutrice...")], "Proposing star alternative"),
 ("laurence", "Pour le rôle principal de l'institutrice?",
  "For the leading role of the schoolteacher?",
  [(480, "dans l'institutrice")], "Showing immediate interest"),
 ("lea", "Exactement, avec un accord de principe rapide.",
  "Exactly, with a quick agreement in principle.",
  [(482, "Un accord de principe pour lancer le financement du film.")], "Offering firm commitment"),
 ("laurence", "Ajoute une participation de Balasko et j'accepte.",
  "Add an appearance by Balasko and I accept.",
  [(487, "Balasco, en participation exceptionnelle.")], "Making final counteroffer"),
 ("lea", "Marché conclu, signe ce papier maintenant.",
  "Deal done, sign this paper now.",
  [(489, "Allez, signe.")], "Sealing the agreement"),
]

WALK = [
 (0, None,
  "'Your lookalike scheme will never work.' Laurence dismisses the risky plan. "
  "The future tense 'marchera' combined with 'jamais' indicates absolute doubt."),
 (1, None,
  "'You are thinking completely backwards, Laurence.' Arlette challenges her colleague. "
  "The adverbial expression 'a l'envers' describes reverse logic."),
 (2, None,
  "'I do not know this lady.' Laurence points out that she has never met the woman. "
  "The verb 'connaitre' means to be acquainted with someone."),
 (3, None,
  "'She will save our entire agency today.' Arlette emphasizes how vital the scheme is. "
  "The future 'sauvera' expresses confident prediction."),
 (4, None,
  "'I refuse to sign a fake contract.' Laurence balks at committing fraud on paper. "
  "The verb 'refuser' followed by 'de' introduces an infinitive action."),
 (5, None,
  "'What do you want in exchange for your help?' Arlette opens commercial negotiations. "
  "The prepositional phrase 'en echange de' means in return for."),
 (6, None,
  "'I want Guillaume Canet for my film.' Laurence asks for a major French star. "
  "The verb 'vouloir' expresses a direct desire."),
 (7, None,
  "'Impossible, he is with Barneville now.' Arlette notes that Mathias represents the actor. "
  "The preposition 'chez' indicates professional representation."),
 (8, None,
  "'Then I am not signing anything at all.' Laurence threatens to walk away from the deal. "
  "The negative phrase 'rien du tout' means nothing at all."),
 (9, None,
  "'And what if I offer you Cecile de France?' Arlette plays an irresistible card. "
  "The hypothetical structure 'et si' introduces an attractive counteroffer."),
 (10, None,
  "'For the leading role of the schoolteacher?' Laurence pictures the casting immediately. "
  "The feminine noun 'institutrice' designates an elementary school teacher."),
 (11, None,
  "'Exactly, with a quick agreement in principle.' Arlette guarantees the backing. "
  "The noun phrase 'accord de principe' represents an agreement in principle."),
 (12, None,
  "'Add an appearance by Balasko and I accept.' Laurence drives a hard bargain. "
  "The imperative 'ajoute' demands an additional cast member."),
 (13, None,
  "'Deal done, sign this paper now.' Arlette clinches the contract on the spot. "
  "The idiom 'marche conclu' means deal agreed or settled."),
]

OUTRO = ("Arlette's legendary dealmaking skills win over a tough producer once again. "
         "By securing Laurence's signature with star casting, the agency buys precious time. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Marché conclu, signe ce papier maintenant.")
