# Authoring module for dix-pour-cent s03e01 scene 05 (cues 71-84).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-05.py --out out/dix-pour-cent/s03e01/scene-05.json

ID = "dix-pour-cent-s03e01-scene-05"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 5
TITLE = "Le deal pour Guillaume  (The Canet Deal)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "mathias": "marcel"}
LABELS = {"lea": "Camille", "gabriel": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 71-84. At ASK, Mathias boasts about closing a major contract for Guillaume Canet. "
               "Gabriel counters with his deal for Jean Dujardin, but Camille spots a strange signature. "
               "Adapted for A1 French.")

INTRO = ("At the ASK agency, Mathias proudly tells Gabriel about signing a lucrative contract for star actor Guillaume Canet. "
         "Gabriel brags about his own massive deal for Jean Dujardin, until Camille notices a bizarre name on the document. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Le contrat pour Guillaume Canet est signé!",
  "The contract for Guillaume Canet is signed!",
  [(71, "Le deal pour Guillaume Canet, ça y est, c'est fait.")], "Mathias shares good news"),
 ("mathias", "Je suis très content pour mon client.",
  "I am very happy for my client.",
  [(72, "Je dois te dire que je suis assez content.")], "Mathias smiles proudly"),
 ("gabriel", "Tu vas encore faire de l'ombre aux collègues.",
  "You will overshadow your colleagues once again.",
  [(76, "tu vas faire de l'ombre à tes collègues.")], "Gabriel teases him"),
 ("mathias", "J'ai le meilleur chiffre d'affaires depuis dix ans.",
  "I have had the highest revenue for ten years.",
  [(78, "que j'ai toujours le meilleur chiffre d'affaires de l'agence.")], "Mathias highlights his record"),
 ("gabriel", "Mais un Jean Dujardin égale deux Canet!",
  "But one Jean Dujardin equals two Canets!",
  [(79, "sauf qu'un du jardin égale deux Canets.")], "Gabriel counters with humor"),
 ("gabriel", "J'ai son contrat signé de sa propre main.",
  "I have his contract signed in his own hand.",
  [(80, "C'est le contrat du jardin, signé, de sa main.")], "Gabriel shows off the file"),
 ("gabriel", "Cette année, c'est moi qui gagne le plus.",
  "This year, I am the one making the most.",
  [(81, "c'est moi qui vais faire le plus gros chiffre.")], "Gabriel boasts about numbers"),
 ("lea", "Bonjour les garçons, vous allez bien aujourd'hui?",
  "Hello boys, are you doing well today?",
  [(82, "Salut, les mecs.")], "Camille enters cheerfully"),
 ("lea", "C'est quoi cette lettre B sur la signature?",
  "What is this letter B on the signature?",
  [(83, "Le B, le B, c'est quoi, ce B ?")], "Camille points to the page"),
 ("gabriel", "Quelle lettre B sur mon contrat?",
  "What letter B on my contract?",
  [(83, "c'est quoi, ce B ?")], "Gabriel looks puzzled"),
 ("lea", "Regarde ici, il est écrit Émile Berthier.",
  "Look here, it says Emile Berthier.",
  [(84, "Émile Berthier.")], "Camille reads the unexpected name"),
 ("mathias", "Qui est donc cet Émile Berthier, Gabriel?",
  "Who then is this Emile Berthier, Gabriel?",
  [(84, "Émile Berthier.")], "Mathias questions the mysterious name"),
 ("gabriel", "Je ne comprends absolument rien à cette signature!",
  "I understand absolutely nothing about this signature!",
  [(84, "Émile Berthier.")], "Gabriel panics over the paper"),
]

OPENER = "Let's examine how Mathias and Gabriel compare their major star contracts step by step to explore office rivalry."

WALK = [
 (0, None,
  "'The contract for Guillaume Canet is signed!' Mathias announces that he has finalized the deal for his client. Dropping the subject pronoun turns the verb for 'signed!' into a direct, punchy command."),
 (1, None,
  "'I am very happy for my client.' Mathias expresses personal satisfaction with the financial agreement. The descriptive adjective for 'pleased' agrees in gender and number with its noun."),
 (2, None,
  "'You will overshadow your colleagues once again.' Gabriel jokes about Mathias dominating agency billings. Gabriel uses the casual singular 'you' with 'are going', showing close familiarity."),
 (3, None,
  "'I have had the highest revenue for ten years.' Mathias reminds Gabriel of his longstanding top ranking. In spoken French, the little word before 'I have' drops its final vowel and attaches with an apostrophe."),
 (4, None,
  "'But one Jean Dujardin equals two Canets!' Gabriel retorts that his own A-list star brings in twice as much. The clause hinges on the everyday verb meaning 'equals'."),
 (5, None,
  "'I have his contract signed in his own hand.' Gabriel proudly claims that his deal is legally completed. The verb meaning 'I have' pairs naturally with the noun for 'contract' in everyday conversation."),
 (6, None,
  "'This year, I am the one making the most.' Gabriel expects to top the agency leaderboard for the first time. Notice how 'it is' leads directly into the noun meaning 'year'."),
 (7, None,
  "'Hello boys, are you doing well today?' Camille walks into the office and greets her colleagues warmly. Camille uses the polite 'you' form alongside 'are doing' to keep a respectful professional tone."),
 (8, None,
  "'What is this letter B on the signature?' Camille notices an unexpected initial on the signed document. In spoken French, the little word before 'is it' drops its final vowel and attaches with an apostrophe."),
 (9, None,
  "'What letter B on my contract?' Gabriel looks down in confusion at the contract lines. In everyday spoken French, rising intonation on 'letter' at the end is enough to turn the sentence into a question."),
 (10, None,
  "'Look here, it says Emile Berthier.' Camille reads out the completely unfamiliar alias written on the page. The clause hinges on the everyday verb meaning 'look'."),
 (11, None,
  "'Who then is this Emile Berthier, Gabriel?' Mathias immediately questions the validity of the contract. In everyday spoken French, rising intonation on 'the key idea' at the end is enough to turn the sentence into a question."),
 (12, None,
  "'I understand absolutely nothing about this signature!' Gabriel realizes with dread that something is very wrong. Notice how 'understand' leads directly into the noun meaning 'signature!'."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Friendly office bragging turns into sudden confusion as Gabriel discovers an unknown name on his prized movie contract. "
         "Let's review the key business and conversational vocabulary from this scene.")

CLOSING = ("gabriel", "Je ne comprends absolument rien à cette signature!")
