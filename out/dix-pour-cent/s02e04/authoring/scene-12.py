# Authoring module for dix-pour-cent s02e04 scene 12 (cues 341-352).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-12.py --out out/dix-pour-cent/s02e04/scene-12.json

ID = "dix-pour-cent-s02e04-scene-12"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 12
TITLE = "L'entretien d'Eugénie  (Eugenie's Interview)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "emilie": "emilie", "theo": "theo"}
LABELS = {"lea": "Noémie", "emilie": "Eugénie", "theo": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 341-352. At the agency, Gabriel guides applicant Eugénie toward the interview. "
               "Noémie confesses her trick to Gabriel: she told Eugénie that Arlette is the real boss and completely deaf. "
               "Eugénie loudly greets Arlette. Adapted for A1 French.")

INTRO = ("In the hallway at ASK, Gabriel welcomes job applicant Eugenie while Noemie watches closely. "
         "Noemie reveals the mischievous advice she gave the candidate to disrupt her chances. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Par ici, mademoiselle, s'il vous plaît.",
  "This way, miss, please.",
  [(341, "Par ici, s'il vous plaît.")], "Added mademoiselle"),
 ("emilie", "Merci beaucoup. Bonjour.",
  "Thank you very much. Hello.",
  [(343, "Bonjour.")], "Added Merci beaucoup"),
 ("theo", "Qu'est-ce que vous lui avez dit, Noémie?",
  "What did you say to her, Noemie?",
  [(342, "Qu'est-ce que vous avez dit ?")], "Adapted phrasing"),
 ("lea", "Je lui ai donné un petit conseil pour réussir.",
  "I gave her a little tip to succeed.",
  [(344, "Je lui ai dit")], "Adapted phrase"),
 ("theo", "Quel genre de conseil?",
  "What kind of tip?",
  [(342, "Qu'est-ce que vous avez dit ?")], "Adapted question"),
 ("lea", "Je lui ai dit que la vraie patronne ici c'était Arlette Azémar.",
  "I told her that the real boss here was Arlette Azemar.",
  [(344, "Je lui ai dit que la vraie patronne ici"), (345, "c'était Arlette Azémar")], ""),
 ("lea", "Et que c'est elle qu'il fallait convaincre.",
  "And that she was the one who had to be convinced.",
  [(345, "et que c'est elle qu'il fallait convaincre.")], ""),
 ("theo", "Arlette? Mais ce n'est pas elle qui recrute!",
  "Arlette? But she is not the one hiring!",
  [(345, "Arlette Azémar")], "Adapted reaction"),
 ("lea", "Je lui ai dit d'y aller, de parler très fort.",
  "I told her to go for it, to speak very loudly.",
  [(347, "Je lui ai dit d'y aller, de parler très fort")], ""),
 ("theo", "Et pourquoi parler très fort?",
  "And why speak very loudly?",
  [(347, "parler très fort")], "Adapted question"),
 ("lea", "Parce qu'elle est sourde.",
  "Because she is deaf.",
  [(348, "parce qu'elle est sourde.")], ""),
 ("theo", "Mais Arlette n'est pas sourde du tout!",
  "But Arlette is not deaf at all!",
  [(348, "elle est sourde.")], "Adapted protest"),
 ("emilie", "Bonjour, madame!",
  "Hello, ma'am!",
  [(349, "Bonjour, madame !")], ""),
 ("emilie", "Tellement heureuse de vous rencontrer!",
  "So happy to meet you!",
  [(350, "Tellement heureuse de vous rencontrer !")], ""),
 ("emilie", "Travailler à vos côtés est un rêve pour tout jeune agent!",
  "Working alongside you is a dream for any young agent!",
  [(351, "Travailler à vos côtés"), (352, "est un rêve pour tout jeune agent !")], ""),
 ("lea", "Voilà, sa carrière chez ASK commence très bien.",
  "There, her career at ASK is off to a great start.",
  [(344, "ici")], "Adapted closing irony"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'This way, miss, please.' Gabriel politely guides Eugenie toward the office. "
  "The polite formula 's'il vous plait' concludes the directional invitation 'par ici'."),
 (1, None,
  "'Thank you very much. Hello.' Eugenie replies courteously. "
  "The polite opening greeting is preceded by warm thanks."),
 (2, None,
  "'What did you say to her, Noemie?' Gabriel questions Noemie's suspicious interference. "
  "The interrogative 'qu'est-ce que' introduces a question in the passe compose."),
 (3, None,
  "'I gave her a little tip to succeed.' Noemie innocently disguises her sabotage. "
  "The preposition 'pour' takes the infinitive 'reussir' to state the intended goal."),
 (4, None,
  "'What kind of tip?' Gabriel presses for clarification. "
  "The interrogative adjective 'quel' agrees with the masculine noun 'genre'."),
 (5, None,
  "'I told her that the real boss here was Arlette Azemar.' Noemie reveals her fabricated hierarchy. "
  "The superlative adjective 'vraie' emphasizes the supposed true leader of ASK."),
 (6, None,
  "'And that she was the one who had to be convinced.' Noemie explains her misleading instruction. "
  "The impersonal imperfect 'il fallait' expresses an obligation in the past."),
 (7, None,
  "'Arlette? But she is not the one hiring!' Gabriel protests the absurd misdirection. "
  "The verb 'recruter' means to hire or recruit new personnel."),
 (8, None,
  "'I told her to go for it, to speak very loudly.' Noemie describes her outrageous delivery advice. "
  "The idiom 'y aller' encourages bold action, paired with 'parler tres fort'."),
 (9, None,
  "'And why speak very loudly?' Gabriel asks with growing disbelief. "
  "The interrogative adverb 'pourquoi' questions the reason for speaking loudly."),
 (10, None,
  "'Because she is deaf.' Noemie delivers the punchline of her prank. "
  "The causal conjunction 'parce que' introduces the explanation with the adjective 'sourde'."),
 (11, None,
  "'But Arlette is not deaf at all!' Gabriel points out the obvious flaw. "
  "The negative locution 'pas ... du tout' expresses complete negation."),
 (12, None,
  "'Hello, ma'am!' Eugenie shouts enthusiastically across the reception area. "
  "The title 'madame' is used here to address the senior agent with utmost respect."),
 (13, None,
  "'So happy to meet you!' Eugenie bellows her eager admiration. "
  "The feminine adjective 'heureuse' expresses joy, intensified by 'tellement'."),
 (14, None,
  "'Working alongside you is a dream for any young agent!' Eugenie yells her flattery loudly. "
  "The prepositional phrase 'a vos cotes' means by your side or alongside you."),
 (15, None,
  "'There, her career at ASK is off to a great start.' Noemie watches the unfolding chaos with satisfaction. "
  "The presentative 'voila' marks a humorous summary of the situation."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Noemie pulls off a hilarious office prank by convincing applicant Eugenie that senior agent Arlette is completely deaf. "
         "Eugenie shouts her greeting at the top of her lungs, confusing everyone in the agency.")
CLOSING = ("lea", "Voilà, sa carrière chez ASK commence très bien.")
