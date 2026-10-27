ID = "fr-01-agence"
TITLE = "Épisode 1 : À l'agence  (At the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie"}
LABELS = {"lea": "Léa", "arlette": "Arlette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"

INTRO = ("This story is set in a talent agency in Paris, like the show you're watching. "
         "Léa is new, it's her first morning, and almost every line is one you'll hear in the first episode. "
         "As always, you'll hear the whole story in French first, then I'll take you back through it in English. "
         "Don't worry about catching every word.")

STORY = [
 ("lea", "Bonjour. Excusez-moi.", "Hello. Excuse me.", [(255, "Excusez-moi")], "'Bonjour.' new"),
 ("arlette", "Oui? Vous êtes?", "Yes? And you are?", [(255, "Oui ?"), (256, "Vous êtes ?")], "question marks attached to the word (app tokenising)"),
 ("lea", "Je m'appelle Léa. Je suis la nouvelle assistante.", "My name is Léa. I'm the new assistant.", [], ""),
 ("arlette", "Ah, d'accord. Bonjour, Léa. Moi, c'est Arlette.", "Ah, I see. Hello, Léa. I'm Arlette.", [(195, "Ah, d'accord")], "'Bonjour, Léa. Moi, c'est Arlette.' new"),
 ("lea", "Vous avez un stylo?", "Do you have a pen?", [(968, "Vous avez un stylo")], ""),
 ("arlette", "Tiens.", "Here.", [(237, "Tiens")], ""),
 ("lea", "Merci beaucoup!", "Thank you very much!", [(970, "Merci beaucoup")], ""),
 ("arlette", "Allez, c'est l'heure. Il y a une réunion.", "Come on, it's time. There's a meeting.",
  [(115, "Allez, c'est l'heure"), (118, "réunion")], "'Il y a une réunion.' new"),
 ("lea", "Je ne sais pas où c'est.", "I don't know where it is.", [(262, "Je ne sais pas")], "'où c'est' added"),
 ("arlette", "Ce n'est pas un problème. Viens!", "It's not a problem. Come on!", [(967, "Ce n'est pas un problème"), (659, "Viens là")], ""),
 ("arlette", "Ça va?", "Are you okay?", [(487, "Ça va")], ""),
 ("lea", "Oui, ça va. Je suis un peu stressée.", "Yes, I'm fine. I'm a bit stressed.", [(84, "Je suis complètement stressée")], "'complètement' -> 'un peu'; 'Oui, ça va.' new"),
 ("arlette", "Pas de souci. Prends ton temps.", "No worries. Take your time.", [(515, "Pas de souci"), (423, "Prends ton temps")], ""),
 ("arlette", "Tu peux compter sur nous.", "You can count on us.", [(498, "Tu peux compter sur nous")], ""),
 ("lea", "Merci, Arlette. Je suis contente d'être ici.", "Thank you, Arlette. I'm glad to be here.", [], ""),
 ("arlette", "Bienvenue parmi nous!", "Welcome to the team!", [], ""),
]

OPENER = "Right, let's go through it slowly. Léa walks into the agency and starts with the politest way to get someone's attention."

WALK = [
 (0, "Excusez-moi.",
  "'Excuse me.' You can use it to interrupt, to get past someone, or to say sorry. Arlette, behind the desk, asks who she is."),
 (1, "Vous êtes?",
  "'And you are?' It's a question with the second half left out, so it sounds quick and a bit brisk. It's polite because it uses the formal 'you'. Léa introduces herself."),
 (2, "Je m'appelle Léa.",
  "'My name is Léa.' Literally 'I call myself Léa'. Notice the little word for 'myself' loses its vowel and sticks to the verb, because the verb starts with a vowel. French does this all the time. Then she says what she is doing here."),
 (2, "Je suis la nouvelle assistante.",
  "'I'm the new assistant.' The word for 'new' ends differently because the assistant is a woman. Arlette smiles, and answers with a short sound of understanding."),
 (3, "Ah, d'accord.",
  "'Ah, I see.' Literally 'in agreement', and it's the most common way to say 'okay, got it'. Now Léa needs something."),
 (4, None,
  "'Do you have a pen?' This is the formal 'you' again, because Léa is talking to a colleague she has only just met. Arlette hands it over with one word."),
 (5, None,
  "'Here.' It's the casual 'you' command form of 'to hold'. Now that she knows who Léa is, Arlette switches to the casual 'you'. An older colleague can do that with a younger one."),
 (6, None,
  "'Thank you very much!' The second word is the one that makes it 'very much'. Then Arlette announces something."),
 (7, "Allez, c'est l'heure.",
  "'Come on, it's time.' The first word is the one the French use to get things moving. Then a bit more detail."),
 (7, "Il y a une réunion.",
  "'There's a meeting.' This 'there is' sounds like one word, and you'll hear it everywhere. Léa panics a little."),
 (8, None,
  "'I don't know where it is.' A very useful sentence for a new place. Arlette stays calm."),
 (9, None,
  "'It's not a problem. Come on!' Another casual command. Then she checks on Léa."),
 (10, None,
  "'Are you okay?' The same two words also mean 'how are you?' and 'hi, how's it going?'. Léa answers honestly."),
 (11, None,
  "'Yes, I'm fine. I'm a bit stressed.' The last word is feminine again. Arlette tries to reassure her."),
 (12, None,
  "'No worries. Take your time.' The second sentence is a command, in the casual form. Arlette adds something warm."),
 (13, None,
  "'You can count on us.' It means 'you can rely on us'. Léa, moved, thanks her."),
 (14, None,
  "'Thank you, Arlette. I'm glad to be here.' She uses Arlette's name, which makes it friendlier. And Arlette finishes."),
 (15, None,
  "'Welcome to the team!' The first word is what you hear when somebody arrives, and the end literally means 'among us'."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = ("That's it for today. When you watch the first episode, listen for the polite way to say excuse me, "
         "and for the little word that means 'here you go'. You'll catch them now. See you next time.")
CLOSING = ("lea", "À bientôt!")
