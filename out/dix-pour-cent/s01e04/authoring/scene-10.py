# Authoring module for dix-pour-cent s01e04 scene 10 (cues 262-290).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-10.py --out out/dix-pour-cent/s01e04/scene-10.json

ID = "dix-pour-cent-s01e04-scene-10"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 10
TITLE = "Je vois tout dans vos notes  (I See Everything in Your Bills)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "colette": "Colette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("The next morning at ASK, the tax audit is getting personal. "
         "Colette Brancillon is still furious with Andréa after recognising her from the dating site, and she is checking every single receipt the agents have ever claimed. "
         "After a frantic warning from Gabriel at the office, Andréa spots Colette in a clothes shop and tries one more time to charm her. "
         "Listen to the French first without worrying about catching every word.")

STORY = [
 ("gabriel", "Andréa! Brancillon est venue chez moi à sept heures du matin!", "Andréa! Brancillon came to my place at seven in the morning!",
  [(263, "Andréa ! Brancillon"), (263, "chez moi à sept heures du matin")], "'a débarqué' -> 'est venue'"),
 ("lea", "Quoi? Chez toi?", "What? To your place?",
  [(264, "Quoi ? Chez toi")], ""),
 ("gabriel", "Pour vérifier mes costumes et mes notes de frais. Bonne chance!", "To check my suits and my expense claims. Good luck!",
  [(265, "Pour vérifier"), (265, "mes costumes"), (266, "mes notes de frais"), (267, "Bonne chance")], "omits 'Merde !' in 267"),
 ("lea", "Colette? Bonjour! Cette veste est très belle.", "Colette? Hello! This jacket is very nice.",
  [(271, "Colette"), (272, "Bonjour")], "simplifies idiom 'ne paie pas de mine' in 273"),
 ("lea", "Vous voulez dîner avec moi ce soir?", "Do you want to have dinner with me tonight?",
  [(275, "ce soir")], "'Vous pourriez la voir ce soir au dîner' simplified to A1"),
 ("colette", "Arrête, Andréa. Je sais qui tu es.", "Stop it, Andréa. I know who you are.",
  [(275, "Arrête, Andréa"), (276, "Je sais qui tu es")], ""),
 ("lea", "Ah bon?", "Really?",
  [(277, "Ah bon")], ""),
 ("colette", "Oui. Je vois tout dans tes factures.", "Yes. I see everything in your bills.",
  [(277, "Oui"), (278, "Je vois tout dans tes factures")], ""),
 ("lea", "Quoi?", "What?",
  [(279, "Quoi")], ""),
 ("colette", "Tout. Tu manges très mal, et tu ne prends jamais de vacances.", "Everything. You eat very badly, and you never take a holiday.",
  [(279, "Tout")], "retells 280-281 in A1 verbs"),
 ("colette", "Tu paies une salle de sport très chère, mais tu n'y vas jamais.", "You pay for a very expensive gym, but you never go there.",
  [(282, "d'une salle de sport très chère, mais tu n'y vas jamais")], "'Tu es membre d'une' -> 'Tu paies une'"),
 ("colette", "Et tu as un problème avec tes cheveux.", "And you have a problem with your hair.",
  [(283, "Et tu as un problème avec tes cheveux")], ""),
 ("lea", "Non!", "No!",
  [(284, "Non")], ""),
 ("colette", "Si. Toujours un coiffeur différent.", "Yes, you do. Always a different hairdresser.",
  [(284, "Si. Toujours un coiffeur différent")], ""),
 ("colette", "Et tu as beaucoup de petites amies.", "And you have lots of girlfriends.",
  [(286, "Et tu as beaucoup de petites amies")], ""),
 ("lea", "C'est faux. Je suis souvent seule.", "That's false. I'm often alone.",
  [(286, "Faux"), (290, "Je suis souvent")], "feminine 'seule' for Andréa"),
 ("colette", "De toute façon, tu n'es pas quelqu'un pour moi.", "Anyway, you're not someone for me.",
  [(287, "De toute façon, tu n'es pas quelqu'un pour moi")], ""),
]

OPENER = "Let's break that down together. First, Gabriel bursts into Andréa's office in a panic."

WALK = [
 (0, None,
  "'Andréa! Brancillon came to my place at seven in the morning!' The verb 'to come' uses 'to be' in the past tense, so 'came' has a feminine ending for Brancillon."),
 (1, None,
  "'What? To your place?' The little preposition for 'at someone's home' followed by 'you'."),
 (2, None,
  "'To check my suits and my expense claims. Good luck!' Literally 'notes of expenses'. Gabriel warns her that she's next."),
 (3, None,
  "'Colette? Hello! This jacket is very nice.' Later, in a clothes shop, Andréa approaches Colette by the racks."),
 (4, None,
  "'Do you want to have dinner with me tonight?' Andréa stays on the polite 'you' and invites her out."),
 (5, None,
  "'Stop it, Andréa. I know who you are.' Colette switches straight to the informal 'you'."),
 (6, None,
  "'Really?' Two short words that mean 'oh really?' or 'is that so?'."),
 (7, None,
  "'Yes. I see everything in your bills.' Every restaurant receipt and shop bill is sitting in Colette's audit file."),
 (8, None,
  "'What?' Andréa is caught off guard."),
 (9, None,
  "'Everything. You eat very badly, and you never take a holiday.' The negative wraps around 'take' with the word for 'never'."),
 (10, None,
  "'You pay for a very expensive gym, but you never go there.' Literally 'a room of sport', and the tiny word before 'go' means 'there'."),
 (11, None,
  "'And you have a problem with your hair.' Plural possessive before 'hair', because 'hair' on your head is plural in French."),
 (12, None,
  "'No!' Andréa protests."),
 (13, None,
  "'Yes, you do. Always a different hairdresser.' Once again, the special word for 'yes' contradicts Andréa's 'no'."),
 (14, None,
  "'And you have lots of girlfriends.' Literally 'little friends' in the feminine."),
 (15, None,
  "'That's false. I'm often alone.' For once, Andréa drops her tough act and speaks honestly."),
 (16, None,
  "'Anyway, you're not someone for me.' The three-word phrase at the start means 'in any case' or 'anyway'."),
]

TRANSITION = "Now let's listen to the whole scene again."

OUTRO = ("Just as Andréa tries to show her softer side, someone from her past is about to ruin everything outside the shop. "
         "Until next time!")
CLOSING = ("colette", "Je vois tout dans tes factures.")
