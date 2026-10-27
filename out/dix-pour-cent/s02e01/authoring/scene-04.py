# Authoring module for dix-pour-cent s02e01 scene 04 (cues 92-123).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-04.py --out out/dix-pour-cent/s02e01/scene-04.json

ID = "dix-pour-cent-s02e01-scene-04"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 4
TITLE = "Mathias et Camille au café  (Mathias and Camille at the Café)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Camille", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 92-123. Mathias meets Camille and suggests revealing their father-daughter "
               "relationship to the agency, but she is terrified of losing her friends and her job. "
               "Adapted for A1 French.")

INTRO = ("Mathias meets his secret daughter Camille at a quiet cafe across town. "
         "After his wife Catherine kicked him out for his years of lies, Mathias wants to come clean to everyone at ASK. "
         "However, Camille is horrified by the prospect of being exposed. Let's listen to their conversation in French first.")

STORY = [
 ("mathias", "Tu es sûre d'avoir assez mangé?",
  "Are you sure you have eaten enough?",
  [(92, "assez mangé ?")], "Normalized 'T'es' to 'Tu es'"),
 ("lea", "Alors, tu as quelque chose à me dire.",
  "So, you have something to tell me.",
  [(94, "Alors,"), (95, "Tu as quelque chose à me dire.")], ""),
 ("mathias", "J'ai fait du mal en cachant la vérité pendant des années.",
  "I caused harm by hiding the truth for years.",
  [(97, "j'ai fait beaucoup de mal"), (98, "pendant des années.")], "Replaced 'les choses' with 'la vérité'"),
 ("mathias", "Catherine m'a mis à la porte.",
  "Catherine threw me out.",
  [(99, "Catherine m'a mis à la porte,")], ""),
 ("mathias", "Elle pense que je suis un menteur.",
  "She thinks I am a liar.",
  [(100, "elle pense que je suis"), (100, "menteur.")], ""),
 ("mathias", "Je veux réparer ça et dire la vérité.",
  "I want to fix that and tell the truth.",
  [(102, "Je veux réparer ça."), (104, "dire la vérité,")], ""),
 ("mathias", "Je veux dire à tout le monde que tu es ma fille.",
  "I want to tell everyone that you are my daughter.",
  [(104, "dire que tu es ma fille."), (107, "je veux dire à tout le monde.")], ""),
 ("lea", "À l'agence? Mais maintenant j'ai peur.",
  "At the agency? But now I am afraid.",
  [(108, "À l'agence..."), (113, "maintenant j'ai peur.")], ""),
 ("mathias", "Peur de quoi, Camille?",
  "Afraid of what, Camille?",
  [(115, "Peur de quoi ?")], "Added address name"),
 ("lea", "J'ai peur de perdre la confiance de mes collègues.",
  "I am afraid of losing the trust of my colleagues.",
  [(116, "De perdre la confiance des gens,")], "Adapted 'des gens' to 'de mes collègues'"),
 ("lea", "Tu crois qu'Andréa veut de ta fille comme assistante?",
  "Do you think Andréa wants your daughter as an assistant?",
  [(118, "Tu crois qu'Andréa veut de ta fille comme assistante ?")], ""),
 ("lea", "Hervé et Noémie sont mes amis maintenant.",
  "Hervé and Noémie are my friends now.",
  [(119, "Ce sont mes amis maintenant.")], "Named the colleagues explicitly"),
 ("lea", "Ils vont penser que je suis une menteuse.",
  "They will think that I am a liar.",
  [(120, "comme une sorte de")], "Simplified traitor metaphor to liar"),
 ("lea", "Je suis très heureuse ici, je ne veux pas gâcher ça.",
  "I am very happy here, I do not want to ruin that.",
  [(121, "je ne veux pas gâcher ça.")], "Adapted gender and tense to present"),
]

OPENER = "Let's examine how Mathias and Camille discuss their hidden family secret."

WALK = [
 (0, None,
  "'Are you sure you have eaten enough?' Mathias shows fatherly care using the compound past infinitive."),
 (1, None,
  "'So, you have something to tell me.' Camille prompts him directly with an indefinite pronoun construction."),
 (2, None,
  "'I caused harm by hiding the truth for years.' A gerund form expressing the continuous cause of distress."),
 (3, None,
  "'Catherine threw me out.' An idiomatic past expression literally meaning put to the door."),
 (4, None,
  "'She thinks I am a liar.' A verb of opinion governing a subordinate clause with a predicate noun."),
 (5, None,
  "'I want to fix that and tell the truth.' Two infinitives joined by a conjunction after a modal verb."),
 (6, None,
  "'I want to tell everyone that you are my daughter.' Mathias states his wish to acknowledge his child publicly."),
 (7, None,
  "'At the agency? But now I am afraid.' Camille reacts with shock followed by an expression of fear."),
 (8, None,
  "'Afraid of what, Camille?' Mathias asks for clarification with a preposition and interrogative pronoun."),
 (9, None,
  "'I am afraid of losing the trust of my colleagues.' The verb to lose followed by an abstract quality noun."),
 (10, None,
  "'Do you think Andrea wants your daughter as an assistant?' A question highlighting professional vulnerability."),
 (11, None,
  "'Herve and Noemie are my friends now.' Camille describes her newly built personal and professional bonds."),
 (12, None,
  "'They will think that I am a liar.' The near-future tense expressing Camille's fear of social rejection."),
 (13, None,
  "'I am very happy here, I do not want to ruin that.' A heartfelt appeal to preserve her current happiness."),
]

TRANSITION = "Now let's listen to their conversation at the cafe again without interruptions."

OUTRO = ("Camille desperately wants to protect her independent life at the agency. "
         "Mathias agrees to keep quiet for now, but keeping such a major secret is never easy.")

CLOSING = ("lea", "On y va?")
