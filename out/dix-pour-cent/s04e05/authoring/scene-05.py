ID = "dix-pour-cent-s04e05-scene-05"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 5
TITLE = "Le contact de Monica  (Monica's Contact)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "gabriel": "theo", "elise": "emilie", "lea": "lucie"}
LABELS = {"gabriel": "Gabriel", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"

INTRO = ("In Gabriel's office, the new agent Elise Formain drops by with a very smooth request. "
         "We'll hear their conversation in French first, but don't worry about catching every word.")

STORY = [
 ("elise", "Je peux me permettre?", "Can I intrude?",
  [(250, "Je peux me permettre ?")], ""),
 ("gabriel", "Oui, bien sûr.", "Yes, of course.",
  [(251, "Oui, bien sûr.")], ""),
 ("elise", "Donnez-moi le contact de Monica Bellucci.", "Give me Monica Bellucci's contact.",
  [(252, "les coordonnées de Monica Bellucci ?")], "Simplified to A1"),
 ("gabriel", "Oui. Pour quoi faire?", "Yes. What for?",
  [(253, "Oui. Pour quoi faire ?")], ""),
 ("elise", "Pour organiser des rencontres.", "To organize meetings.",
  [(254, "organiser des rencontres")], "Simplified"),
 ("elise", "Il faut vraiment penser en équipe.", "We really have to think as a team.",
  [(257, "Il faut vraiment qu'on pense... en équipe")], "Simplified"),
 ("gabriel", "On le fait déjà.", "We already do that.",
  [(258, "On le fait déjà")], ""),
 ("elise", "Mais peut-être pas assez.", "But perhaps not enough.",
  [(259, "Mais peut-être pas assez.")], ""),
 ("gabriel", "OK, je vous envoie sa carte.", "OK, I will send you her card.",
  [(261, "OK"), (261, "je vous envoie sa carte.")], ""),
 ("elise", "Très bien. Et celle de Dujardin?", "Very good. And Dujardin's?",
  [(262, "Très bien. Oh, et celle de Dujardin aussi.")], "Simplified"),
 ("gabriel", "Jean est à Andréa.", "Jean is with Andrea.",
  [(263, "Jean"), (263, "est à Andréa.")], "Simplified"),
 ("elise", "Elle est débordée, ne l'embêtons pas.", "She is swamped, let's not bother her.",
  [(264, "elle est débordée, ne l'embêtons pas")], "Simplified"),
 ("elise", "Merci, Gaby!", "Thanks, Gaby!",
  [(265, "Merci, Gaby !")], "")
]

OPENER = "Let's walk through it. Elise walks in and asks a favor."

WALK = [
 (0, None,
  "'Can I intrude?' She asks for permission to interrupt his work."),
 (1, None,
  "'Yes, of course.' He welcomes her in without suspicion."),
 (2, None,
  "'Give me Monica Bellucci's contact.' She immediately asks for a major client's details."),
 (3, None,
  "'Yes. What for?' He is a bit surprised by the direct request."),
 (4, None,
  "'To organize meetings.' She explains that it is for the agency's benefit."),
 (5, None,
  "'We really have to think as a team.' She uses corporate teamwork language to manipulate him."),
 (6, None,
  "'We already do that.' He defends their current level of collaboration."),
 (7, None,
  "'But perhaps not enough.' She gently pushes back and insists they need to do more."),
 (8, None,
  "'OK, I will send you her card.' He gives in and agrees to share his star client."),
 (9, None,
  "'Very good. And Dujardin's?' She immediately pushes her luck and asks for another star."),
 (10, None,
  "'Jean is with Andrea.' He clarifies that Jean Dujardin is represented by his colleague."),
 (11, None,
  "'She is swamped, let's not bother her.' Elise quickly drops the subject to avoid dealing with Andrea."),
 (12, None,
  "'Thanks, Gaby!' She leaves with a cheerful, overly familiar goodbye.")
]

TRANSITION = "Now let's hear the scene once more."
OUTRO = "Elise just smoothly extracted a major client's contact from Gabriel. See you next time."
CLOSING = ("gabriel", "À bientôt!")
