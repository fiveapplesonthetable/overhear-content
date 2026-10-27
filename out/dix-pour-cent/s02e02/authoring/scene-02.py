# Authoring module for dix-pour-cent s02e02 scene 02 (cues 38-104).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-02.py --out out/dix-pour-cent/s02e02/scene-02.json

ID = "dix-pour-cent-s02e02-scene-02"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 2
TITLE = "L'ordre d'Hicham  (Hicham's Order)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel", "mathias": "theo"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 38-104. Hicham learns that Ramzy and Virginie left for StarMedia and orders "
               "the agents to poach Fabrice Luchini in retaliation. Adapted for A1 French.")

INTRO = ("In the executive office, the celebration is cut short as Hicham discovers that ASK just lost two huge stars. "
         "Infuriated by rival agency StarMedia, he demands an immediate counterattack: poaching iconic actor Fabrice Luchini. "
         "Let's listen to the tense confrontation in French first.")

STORY = [
 ("hicham", "C'est quoi cette histoire avec Ramzy et Virginie Efira?",
  "What is this story about Ramzy and Virginie Efira?",
  [(38, "C'est quoi cette histoire avec Ramzy"), (39, "et Virginie Efira qui partent ?")], ""),
 ("mathias", "Ils ont rompu, et François Bréhier en a profité.",
  "They broke up, and Francois Brehier took advantage of it.",
  [(49, "Ils ont rompu,"), (50, "François Bréhier en a profité.")], ""),
 ("mathias", "Bréhier dirige notre agence concurrente, StarMedia.",
  "Brehier runs our rival agency, StarMedia.",
  [(51, "Il dirige StarMedia.")], "Adapted pronoun 'il' to 'Bréhier' and added context"),
 ("hicham", "Ils nous ont volé nos acteurs!",
  "They stole our actors from us!",
  [(61, "Ils nous ont volé nos acteurs,")], ""),
 ("hicham", "Alors prenons leur plus grande star, Fabrice Luchini.",
  "So let us take their biggest star, Fabrice Luchini.",
  [(62, "alors prenons leur plus grande star : Fabrice Luchini.")], ""),
 ("mathias", "Vous ne pouvez pas nous demander de voler un client.",
  "You cannot ask us to steal a client.",
  [(63, "Vous ne pouvez pas nous demander de voler un client.")], ""),
 ("hicham", "Pourquoi pas? Eux, ils l'ont fait.",
  "Why not? They did it.",
  [(64, "Pourquoi pas ? Eux, ils l'ont fait.")], ""),
 ("lea", "Luchini est chez Bréhier depuis trente-cinq ans!",
  "Luchini has been with Brehier for thirty-five years!",
  [(66, "Luchini est chez Bréhier depuis 35 ans.")], "Spelled out number 35"),
 ("lea", "Il ne partira jamais de chez eux.",
  "He will never leave them.",
  [(67, "Il ne partira jamais.")], "Added destination phrase"),
 ("hicham", "Je veux Luchini chez ASK avant la fin du mois.",
  "I want Luchini at ASK before the end of the month.",
  [(77, "Je veux Luchini chez ASK avant la fin du mois.")], ""),
 ("hicham", "Sinon, je peux vendre mes parts à StarMedia.",
  "Otherwise, I can sell my shares to StarMedia.",
  [(75, "je pourrais vendre mes parts à StarMedia.")], "Changed conditional to present"),
 ("mathias", "C'est une vengeance ridicule!",
  "It is a ridiculous revenge!",
  [(100, "cette vengeance ridicule !")], "Framed as independent sentence"),
 ("lea", "Un talent, il faut se battre pour lui.",
  "A talent, you have to fight for them.",
  [(96, "Un talent, c'est comme une femme,"), (97, "il faut se battre pour")], "Adapted pronoun"),
 ("lea", "Je vais chercher Luchini!",
  "I am going to get Luchini!",
  [(99, "Je vais chercher Luchini !")], ""),
]

OPENER = "Let's examine how Hicham pushes his agents to take extreme risks."

WALK = [
 (0, None,
  "'What is this story about Ramzy and Virginie Efira?' Hicham inquires about the sudden loss of two marquee talents."),
 (1, None,
  "'They broke up, and Francois Brehier took advantage of it.' Mathias explains the marital crisis that enabled the rival move."),
 (2, None,
  "'Brehier runs our rival agency, StarMedia.' A clarification of the competitor who orchestrated the raid."),
 (3, None,
  "'They stole our actors from us!' A direct exclamation accusing the rival agency of theft."),
 (4, None,
  "'So let us take their biggest star, Fabrice Luchini.' Hicham proposes an aggressive retaliatory strike."),
 (5, None,
  "'You cannot ask us to steal a client.' Mathias raises a professional objection based on agency ethics."),
 (6, None,
  "'Why not? They did it.' A pragmatic retort arguing that ruthlessness should be met with ruthlessness."),
 (7, None,
  "'Luchini has been with Brehier for thirty-five years!' Andrea emphasizes the deep loyalty between the actor and his agent."),
 (8, None,
  "'He will never leave them.' A future tense prediction asserting that poaching is impossible."),
 (9, None,
  "'I want Luchini at ASK before the end of the month.' An ultimatum setting a strict deadline for the partners."),
 (10, None,
  "'Otherwise, I can sell my shares to StarMedia.' A financial threat to pull out and ruin the agency."),
 (11, None,
  "'It is a ridiculous revenge!' Mathias protests the irrationality of attacking an established star."),
 (12, None,
  "'A talent, you have to fight for them.' Andrea expresses her instinct to take on impossible challenges."),
 (13, None,
  "'I am going to get Luchini!' A near-future declaration accepting the high-stakes mission."),
]

TRANSITION = "Now let's listen to the argument about Fabrice Luchini again at natural speed."

OUTRO = ("Hicham has made his ultimatum clear: sign Fabrice Luchini or risk losing the entire agency. "
         "While Mathias panics, Andrea prepares to make contact with the great actor.")

CLOSING = ("lea", "Trouvez tout sur Luchini.")
