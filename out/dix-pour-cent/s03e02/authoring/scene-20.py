# Authoring module for dix-pour-cent s03e02 scene 20 (cues 902-914).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-20.py --out out/dix-pour-cent/s03e02/scene-20.json

ID = "dix-pour-cent-s03e02-scene-20"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 20
TITLE = "Une cigarette dehors  (A Cigarette Outside)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 902-914. Overwhelmed by her constant screen nudity, Sofia steps out into the cinema foyer. "
               "Gabriel joins her outside to comfort and reassure her. "
               "Adapted for A1 French.")

INTRO = ("Feeling overwhelmed by her constant screen nudity, Sofia slips out of the premiere screening into the theater foyer. "
         "Gabriel joins her outside for an honest and comforting conversation. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Ah, je me sens plus libre ici!",
  "Ah, I feel more free here!",
  [(904, "je me sens libre.")], "Sofia steps outside"),
 ("gabriel", "Tu fumes une cigarette maintenant, Sofia?",
  "Are you smoking a cigarette now, Sofia?",
  [(905, "Tu fumes toi maintenant ?")], "Gabriel is surprised"),
 ("lea", "Non, j'ai juste demandé cette cigarette.",
  "No, I just asked for this cigarette.",
  [(906, "Non, mais j'ai taxé une clope")], "Sofia explains herself"),
 ("lea", "Elle me fait tourner la tête.",
  "It makes my head spin.",
  [(907, "ça me fait tourner la tête.")], "Sofia feels dizzy"),
 ("gabriel", "Passe-moi la cigarette, s'il te plaît.",
  "Pass me the cigarette, please.",
  [(908, "Passe s'il te plaît.")], "Gabriel takes it"),
 ("gabriel", "C'est vrai qu'elle est très forte!",
  "It is true that it is very strong!",
  [(909, "c'est vrai que c'est fort.")], "Gabriel reacts to the smoke"),
 ("lea", "Pardon d'être sortie de la salle.",
  "Sorry for having left the theater.",
  [(910, "je suis sorti de la salle,")], "Sofia apologizes for leaving"),
 ("gabriel", "Tu n'aimes pas le film de Julien?",
  "Do you not like Julien's movie?",
  [(910, "le film était pas bien")], "Gabriel inquires gently"),
 ("lea", "Si, le film est très beau.",
  "Yes, the movie is very beautiful.",
  [(910, "le film")], "Sofia defends the aesthetic"),
 ("lea", "Mais je suis nue tout le temps!",
  "But I am naked all the time!",
  [(911, "je suis à poil tout le temps.")], "Sofia explains her embarrassment"),
 ("lea", "C'est une expérience très difficile, Gabriel.",
  "It is a very difficult experience, Gabriel.",
  [(913, "C'est horrible.")], "Sofia admits her vulnerability"),
 ("gabriel", "Tu es magnifique sur ce grand écran.",
  "You are magnificent on this big screen.",
  [(914, "C'est pas vraiment le mot.")], "Gabriel offers praise"),
 ("gabriel", "Le public adore ton immense talent!",
  "The audience loves your immense talent!",
  [(914, "le mot.")], "Gabriel reassures her"),
 ("lea", "Merci Gabriel, tu sais me rassurer.",
  "Thank you Gabriel, you know how to reassure me.",
  [(912, "Voilà.")], "Sofia feels supported"),
]

OPENER = "Let's examine how Gabriel comforts Sofia step by step during the movie premiere."

WALK = [
 (0, None,
  "'Ah, I feel more free here!' Sofia breathes easily after escaping the cinema hall. The reflexive pronoun sits right in front of the verb for 'feel', turning the action back onto the subject."),
 (1, None,
  "'Are you smoking a cigarette now, Sofia?' Gabriel is surprised to find her holding a cigarette. In everyday spoken French, rising intonation on 'smoke' at the end is enough to turn the sentence into a question."),
 (2, None,
  "'No, I just asked for this cigarette.' Sofia explains she took one to calm her nerves. The verb meaning 'have' pairs naturally with the noun for 'cigarette' in everyday conversation."),
 (3, None,
  "'It makes my head spin.' Sofia admits the strong tobacco makes her dizzy. Notice how 'makes' leads directly into the noun meaning 'head'."),
 (4, None,
  "'Pass me the cigarette, please.' Gabriel takes the cigarette to help her relax. The verb meaning 'pass me' pairs naturally with the noun for 'cigarette' in everyday conversation."),
 (5, None,
  "'It is true that it is very strong!' Gabriel confirms the tobacco's harsh strength with a cough. The adverb meaning 'very' gives the reply its conversational emphasis."),
 (6, None,
  "'Sorry for having left the theater.' Sofia apologizes for stepping out during the premiere. Notice how 'having' leads directly into the noun meaning 'room'."),
 (7, None,
  "'Do you not like Julien's movie?' Gabriel wonders if she dislikes the artistic direction. Notice how 'like' leads directly into the noun meaning 'film'."),
 (8, None,
  "'Yes, the movie is very beautiful.' Sofia affirms the aesthetic quality of the work. The descriptive adjective for 'beautiful' agrees in gender and number with its noun."),
 (9, None,
  "'But I am naked all the time!' Sofia confesses her deep embarrassment at her constant screen nudity. The key noun here means 'time', anchored by its matching French article."),
 (10, None,
  "'It is a very difficult experience, Gabriel.' Sofia shares the vulnerability of exposing herself. The descriptive adjective for 'difficult' agrees in gender and number with its noun."),
 (11, None,
  "'You are magnificent on this big screen.' Gabriel reassures her of her poise and beauty. The informal 'you' form around 'screen' marks a direct, personal relationship."),
 (12, None,
  "'The audience loves your immense talent!' Gabriel reminds her of the crowd's warm admiration. Dropping the subject pronoun turns the verb for 'adores' into a direct, punchy command."),
 (13, None,
  "'Thank you Gabriel, you know how to reassure me.' Sofia appreciates her agent's sensitive encouragement. The clause hinges on the everyday verb meaning 'know'."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Gabriel reassures Sofia about her performance and body on screen, strengthening their deep bond of trust as actress and agent. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("lea", "Merci Gabriel, tu sais me rassurer.")
