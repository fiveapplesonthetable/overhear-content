# Authoring module for dix-pour-cent s03e01 scene 09 (cues 173-174).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-09.py --out out/dix-pour-cent/s03e01/scene-09.json

ID = "dix-pour-cent-s03e01-scene-09"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 9
TITLE = "La nouvelle affiche  (The New Movie Poster)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Sofia", "theo": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 173-174. At the ASK agency, Sofia arrives excited to show Gabriel "
               "the stunning new promotional poster for her upcoming film. Adapted for A1 French.")

INTRO = ("At the talent agency, Sofia arrives full of excitement to share a major milestone with Gabriel. "
         "The creative team has completed the striking official poster for her upcoming feature film. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Bonjour Gabriel! Tu as une minute?",
  "Hello Gabriel! Do you have a minute?",
  [(173, "Il faut que je vous montre.")], "Adapted greeting"),
 ("theo", "Bonjour Sofia! Oui, bien sûr.",
  "Hello Sofia! Yes, of course.",
  [(174, "Qu'est-ce que c'est ?")], "Adapted greeting"),
 ("lea", "Il faut que je vous montre.",
  "I have to show you something.",
  [(173, "Il faut que je vous montre.")], ""),
 ("theo", "Qu'est-ce que c'est?",
  "What is it?",
  [(174, "Qu'est-ce que c'est ?")], ""),
 ("lea", "C'est la nouvelle affiche de mon film.",
  "It is the new poster for my movie.",
  [(173, "Il faut que je vous montre.")], "Adapted explanation"),
 ("theo", "L'affiche est déjà prête?",
  "The poster is already ready?",
  [(174, "Qu'est-ce que c'est ?")], "Adapted query"),
 ("lea", "Oui, l'équipe a travaillé très vite.",
  "Yes, the team worked very quickly.",
  [(173, "Il faut que je vous montre.")], "Adapted explanation"),
 ("theo", "Montre-moi ça tout de suite.",
  "Show me that right away.",
  [(173, "Il faut que je vous montre.")], "Adapted request"),
 ("lea", "Regarde, je l'ai sur ma tablette.",
  "Look, I have it on my tablet.",
  [(173, "Il faut que je vous montre.")], "Adapted presentation"),
 ("theo", "Elle est vraiment magnifique!",
  "It is really magnificent!",
  [(174, "Qu'est-ce que c'est ?")], "Adapted praise"),
 ("lea", "Tu trouves? J'avais un peu peur.",
  "You think so? I was a little afraid.",
  [(173, "Il faut que je vous montre.")], "Adapted reaction"),
 ("theo", "Pourquoi avais-tu peur?",
  "Why were you afraid?",
  [(174, "Qu'est-ce que c'est ?")], "Adapted inquiry"),
 ("lea", "J'avais peur que ce soit trop sombre.",
  "I was afraid it would be too dark.",
  [(173, "Il faut que je vous montre.")], "Adapted concern"),
 ("theo", "Non, les couleurs sont très belles.",
  "No, the colors are very beautiful.",
  [(174, "Qu'est-ce que c'est ?")], "Adapted reassurance"),
 ("lea", "Je suis très heureuse du résultat.",
  "I am very happy with the result.",
  [(173, "Il faut que je vous montre.")], "Adapted joy"),
 ("theo", "C'est un grand succès pour toi.",
  "It is a great success for you.",
  [(173, "Il faut que je vous montre.")], "Adapted conclusion"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Hello Gabriel! Do you have a minute?' Sofia greets her agent upon arriving. "
  "The question 'tu as une minute' asks casually for brief availability."),
 (1, None,
  "'Hello Sofia! Yes, of course.' Gabriel welcomes his client warmly. "
  "The adverbial phrase 'bien sur' signals immediate willingness to listen."),
 (2, None,
  "'I have to show you something.' Sofia announces her surprise. "
  "The impersonal necessity structure 'il faut que' takes subjunctive."),
 (3, None,
  "'What is it?' Gabriel asks with curiosity. "
  "The standard question formula 'qu'est-ce que c'est' asks for identification."),
 (4, None,
  "'It is the new poster for my movie.' Sofia reveals the exciting project deliverable. "
  "The feminine noun 'affiche' refers to a printed film poster."),
 (5, None,
  "'The poster is already ready?' Gabriel expresses pleasant surprise at the timeline. "
  "The temporal adverb 'deja' highlights prompt completion."),
 (6, None,
  "'Yes, the team worked very quickly.' Sofia compliments the production crew. "
  "The compound past 'a travaille' describes completed past action."),
 (7, None,
  "'Show me that right away.' Gabriel encourages her with an imperative. "
  "The adverbial phrase 'tout de suite' indicates immediacy."),
 (8, None,
  "'Look, I have it on my tablet.' Sofia pulls up the digital image. "
  "The imperative 'regarde' directs attention to the screen."),
 (9, None,
  "'It is really magnificent!' Gabriel admires the striking visual artwork. "
  "The intensifying adverb 'vraiment' reinforces high aesthetic praise."),
 (10, None,
  "'You think so? I was a little afraid.' Sofia admits her initial nervousness. "
  "The imperfect tense 'avais peur' conveys past emotional apprehension."),
 (11, None,
  "'Why were you afraid?' Gabriel gently probes her self-doubt. "
  "The interrogative adverb 'pourquoi' opens an inquiry into her reasons."),
 (12, None,
  "'I was afraid it would be too dark.' Sofia explains her creative hesitation. "
  "The subjunctive 'soit' follows the expression of fear."),
 (13, None,
  "'No, the colors are very beautiful.' Gabriel validates the visual palette. "
  "The feminine plural adjective 'belles' agrees with 'couleurs'."),
 (14, None,
  "'I am very happy with the result.' Sofia expresses genuine creative satisfaction. "
  "The feminine adjective 'heureuse' expresses deep joy."),
 (15, None,
  "'It is a great success for you.' Gabriel validates her achievement. "
  "The masculine noun phrase 'un grand succes' celebrates her milestone."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Sofia shows Gabriel the finished poster for her new film at the agency. "
         "Reassured by Gabriel's warm enthusiasm, she feels proud of the creative result.")
CLOSING = ("theo", "C'est un grand succès pour toi.")
