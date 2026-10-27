ID = "dix-pour-cent-s01e01-scene-04"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = "Un nouveau caprice?  (Another Whim?)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "noemie": "emilie"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Back at reception, Camille told Sofia she wasn't an actress, she just wanted to see Mathias, and that he "
         "knew her. Sofia, sceptical, rang his office anyway. "
         "Now Mathias comes to fetch her and takes her into his office. His assistant Noémie brings drinks. Watch how "
         "he speaks to Camille in front of others, and how he speaks once the door is closed. Camille is in fact "
         "Mathias's daughter, a secret nobody at the agency knows, and he intends to keep it that way. "
         "We'll hear it in French first; relax and listen for the tone.")

STORY = [
 ("mathias", "Bonjour, Camille. Entrez.", "Hello, Camille. Come in.",
  [(123, "Bonjour, Camille"), (124, "Entrez")], ""),
 ("lea", "Un café, s'il vous plaît.", "A coffee, please.",
  [(125, "Un café, s'il vous plaît")], "speaker not certain from the subtitles; given to Camille, the guest"),
 ("noemie", "Très bien. Et vous? Un thé?", "Very well. And you? Tea?",
  [(126, "Très bien. Et vous ?"), (126, "Un thé ?")], ""),
 ("mathias", "D'accord. Merci.", "Fine. Thank you.",
  [(127, "D'accord"), (127, "Merci")], ""),
 ("mathias", "Pourquoi tu n'as pas appelé?", "Why didn't you call?",
  [(128, "Pourquoi tu n'as pas appelé ?")], ""),
 ("lea", "Je ne sais pas. Je voulais te faire la surprise.", "I don't know. I wanted to surprise you.",
  [(129, "Je sais pas"), (129, "Je voulais te faire la surprise")], "'ne' added"),
 ("lea", "C'est sympa ici. Des sucettes gratuites!", "It's nice here. Free lollipops!",
  [(133, "C'est sympa ici"), (134, "Des sucettes gratuites")], ""),
 ("mathias", "C'est du sucre pour le café.", "It's sugar for the coffee.",
  [(135, "C'est du sucre pour le café")], ""),
 ("mathias", "Qu'est-ce que tu fais à Paris? Tu es en vacances?", "What are you doing in Paris? Are you on holiday?",
  [(137, "Qu'est-ce que tu fais à Paris ? Tu es en vacances ?")], ""),
 ("lea", "En quelque sorte. Ça fait trois semaines que je suis là.", "Sort of. I've been here for three weeks.",
  [(138, "En quelque sorte"), (139, "Ça fait trois semaines que je suis là")], ""),
 ("mathias", "Tu n'aimais pas Mandelieu? C'est un bel endroit.", "Didn't you like Mandelieu? It's a lovely place.",
  [(141, "Tu n'aimais pas"), (141, "Mandelieu"), (142, "C'est un bel endroit")], "'à Mandelieu' -> 'Mandelieu'"),
 ("lea", "J'ai un petit loft. Et je cherche du boulot.", "I've got a little loft. And I'm looking for work.",
  [(150, "un petit loft"), (151, "Et je cherche du boulot")], "'J'ai' added"),
 ("lea", "Tu connais beaucoup de monde dans le cinéma. Tu pourrais m'aider.",
  "You know lots of people in film. You could help me.",
  [(152, "tu connais beaucoup de monde dans le cinéma"), (153, "tu pourrais m'aider")], "'Alors je me suis dit que, comme' dropped"),
 ("mathias", "Un nouveau caprice?", "Another whim?",
  [(154, "Un nouveau caprice ?")], ""),
 ("lea", "Je suis sérieuse. J'ai toujours adoré le cinéma.", "I'm serious. I've always loved films.",
  [(155, "je suis sérieuse"), (156, "J'ai toujours adoré le cinéma")], ""),
 ("mathias", "Écoute, c'est une industrie, et elle est pleine de requins.",
  "Listen, it's an industry, and it's full of sharks.",
  [(161, "Écoute"), (163, "C'est une industrie"), (164, "et elle est pleine de requins")], ""),
 ("mathias", "Désolé, c'est tout ce que je peux faire.", "Sorry, that's all I can do.",
  [(170, "Désolé, c'est tout ce que je peux faire")], ""),
]

OPENER = ("Let's go through it. Mathias greets her in the doorway, in front of his assistant, and he is very proper "
          "about it.")

WALK = [
 (0, "Bonjour, Camille.",
  "'Hello, Camille.' Polite and cool, the way you greet a visitor."),
 (0, "Entrez.",
  "'Come in.' This command is in the formal form, as if she were a stranger. Remember that, because it won't last."),
 (1, None,
  "'A coffee, please.' The last part literally means 'if it pleases you', with the formal 'you'; it's the standard "
  "way to say please to anyone you don't know."),
 (2, None,
  "'Very well. And you? Tea?' Noémie turns to her boss; she knows how he takes his drinks."),
 (3, None,
  "'Fine. Thank you.' The first word literally means 'in agreement', the everyday way to say okay. Noémie leaves, the "
  "door closes, and the tone changes at once."),
 (4, None,
  "'Why didn't you call?' Now he uses the casual 'you'. Behind a closed door Mathias talks to his daughter like the father he is. "
  "The negative wraps around the helper verb of the past tense."),
 (5, "Je voulais te faire la surprise.",
  "'I wanted to surprise you.' Camille answers with the casual 'you' too; the small word for 'you' sits right before "
  "the verb."),
 (6, None,
  "'It's nice here. Free lollipops!' She has spotted a bowl of sticks on the reception desk. The word for 'nice' here "
  "is a friendly, informal one."),
 (7, None,
  "'It's sugar for the coffee.' They are sugar sticks, not sweets. Mathias is not amused."),
 (8, None,
  "'What are you doing in Paris? Are you on holiday?' The first part is the most common way to ask 'what' in a "
  "question. The word for holiday is always plural in French."),
 (9, "Ça fait trois semaines que je suis là.",
  "'I've been here for three weeks.' French uses the present tense for this: literally 'it makes three weeks that I "
  "am here'. She has moved to Paris without telling him."),
 (10, None,
  "'Didn't you like Mandelieu? It's a lovely place.' Mandelieu is a seaside town on the Riviera, near Cannes, where "
  "Camille used to live. He knows exactly where she comes from."),
 (11, None,
  "'I've got a little loft. And I'm looking for work.' The word for work here is a casual one, like 'a job'."),
 (12, "Tu pourrais m'aider.",
  "'You could help me.' This is the gentle, polite 'could'. She hopes he'll use his contacts in the film business."),
 (13, None,
  "'Another whim?' A cutting question. He seems to think she changes her plans all the time."),
 (14, "Je suis sérieuse.",
  "'I'm serious.' The word for 'serious' takes a feminine ending, because Camille is a woman. The man's version ends "
  "differently."),
 (14, "J'ai toujours adoré le cinéma.",
  "'I've always loved films.' She even offers to fetch coffee and hold actors' umbrellas, anything at all."),
 (15, None,
  "'Listen, it's an industry, and it's full of sharks.' He means that in this world you eat or you get eaten. Then he "
  "jokes that if she loves films so much, she should buy a cinema pass."),
 (16, None,
  "'Sorry, that's all I can do.' The answer is no. Camille has come all the way from the coast, and Mathias won't "
  "help her."),
]

TRANSITION = "Now listen to the whole conversation one more time."

OUTRO = ("Did you notice the switch from the formal 'you' to the casual one as soon as the door closed? That small "
         "change gives away a father and daughter. See you next time.")
CLOSING = ("lea", "Salut, Mathias!")
