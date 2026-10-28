# Authoring module for dix-pour-cent s03e01 scene 23 (cues 955-1001).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-23.py --out out/dix-pour-cent/s03e01/scene-23.json

ID = "dix-pour-cent-s03e01-scene-23"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 23
TITLE = "Le réconfort d'Andréa  (Andréa's Comfort)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 987-1001. After Jean Dujardin's breakdown on set, Andrea visits him. "
               "Despite the lost commission, Andrea comforts Jean and admits she should have protected him better. "
               "Adapted for A1 French.")

INTRO = ("Following his bizarre breakdown on the movie set, Jean Dujardin feels deep remorse about costing ASK a major commission. "
         "But Andrea arrives with empathy and understanding to comfort her star client. "
         "Let's listen to the scene in French first.")

STORY = [
 ("jean", "Je t'ai causé beaucoup d'ennuis.",
  "I caused you a lot of trouble.",
  [(987, "Je t'ai mis dans une merde noire, hein.")], "Jean regrets the trouble"),
 ("lea", "Tu as surtout mordu ce chien!",
  "You mostly bit that dog!",
  [(989, "mordu le chien")], "Andrea teases him gently"),
 ("jean", "Tout le monde en parle déjà?",
  "Is everyone already talking about it?",
  [(991, "tout Paris en rêvait,")], "Jean worries about gossip"),
 ("lea", "Tout Paris adore cette folle histoire!",
  "All of Paris loves this crazy story!",
  [(991, "Jean Dujardin l'a fait.")], "Andrea reassures him"),
 ("jean", "Je te fais perdre ton argent.",
  "I make you lose your money.",
  [(994, "perdre de l'argent,")], "Jean frets over the commission"),
 ("jean", "Je suis vraiment désolé pour toi.",
  "I am really sorry for you.",
  [(994, "je suis désolé.")], "Jean offers sincere apologies"),
 ("lea", "Non Jean, c'est moi la responsable.",
  "No Jean, I am the one responsible.",
  [(995, "c'est moi qui suis désolée.")], "Andrea takes responsibility"),
 ("jean", "Pourquoi dis-tu une chose pareille?",
  "Why do you say such a thing?",
  [(996, "Pourquoi ?")], "Jean is surprised"),
 ("lea", "J'ai pensé aux affaires avant tout.",
  "I thought about business above all.",
  [(997, "j'ai pensé à mes affaires")], "Andrea reflects critically"),
 ("lea", "Je n'ai pas assez pensé à toi.",
  "I did not think enough about you.",
  [(997, "pas assez à toi.")], "Andrea regrets neglecting his feelings"),
 ("lea", "Ce rôle était trop difficile pour toi.",
  "This role was too difficult for you.",
  [(1000, "ce rôle était en train de te bouleverser.")], "Andrea recognizes the strain"),
 ("jean", "Ce personnage m'a complètement transformé.",
  "This character completely transformed me.",
  [(1000, "ce rôle")], "Jean explains the emotional toll"),
 ("lea", "J'aurais dû mieux te protéger, Jean.",
  "I should have protected you better, Jean.",
  [(1001, "J'aurais dû mieux te protéger.")], "Andrea vows better protection"),
 ("jean", "Merci Andréa, tu es une vraie amie.",
  "Thank you Andrea, you are a true friend.",
  [(992, "je pense que")], "Jean expresses gratitude"),
]

OPENER = "Let's examine how Andrea and Jean reconcile step by step."

WALK = [
 (0, None,
  "'I caused you a lot of trouble.' Jean expresses remorse for his disruptive behavior on set. Notice how 'have' leads directly into the noun meaning 'troubles'."),
 (1, None,
  "'You mostly bit that dog!' Andrea brings up the most bizarre incident with irony. The informal 'you' form around 'have' marks a direct, personal relationship."),
 (2, None,
  "'Is everyone already talking about it?' Jean wonders about the public reaction in Paris. The verb meaning 'is talking' pairs naturally with the noun for 'world' in everyday conversation."),
 (3, None,
  "'All of Paris loves this crazy story!' Andrea assures him that the industry finds it hilarious. Dropping the subject pronoun turns the verb for 'adores' into a direct, punchy command."),
 (4, None,
  "'I make you lose your money.' Jean worries about the heavy financial fallout for his agent. The reflexive pronoun sits right in front of the verb for 'make', turning the action back onto the subject."),
 (5, None,
  "'I am really sorry for you.' Jean apologizes sincerely to his devoted representative. The descriptive adjective for 'sorry' agrees in gender and number with its noun."),
 (6, None,
  "'No Jean, I am the one responsible.' Andrea refuses to let him shoulder all the blame. The key noun here means 'one responsible', anchored by its matching French article."),
 (7, None,
  "'Why do you say such a thing?' Jean is surprised by her generous and self-critical attitude. Inverting the verb and pronoun around 'do you say' creates a crisp, polished question."),
 (8, None,
  "'I thought about business above all.' Andrea admits she focused excessively on contracts. The verb meaning 'have' pairs naturally with the noun for 'business' in everyday conversation."),
 (9, None,
  "'I did not think enough about you.' Andrea regrets neglecting the human emotional toll on her actor. This conversational past tense combines a helper verb with the past participle for 'thought'."),
 (10, None,
  "'This role was too difficult for you.' Andrea recognizes how deeply the extreme part affected him. Notice how 'was' leads directly into the noun meaning 'role'."),
 (11, None,
  "'This character completely transformed me.' Jean explains how lost he felt inside the role. The verb meaning 'has' pairs naturally with the noun for 'character' in everyday conversation."),
 (12, None,
  "'I should have protected you better, Jean.' Andrea acknowledges her protective duty as an agent. The reflexive pronoun sits right in front of the verb for 'would have', turning the action back onto the subject."),
 (13, None,
  "'Thank you Andrea, you are a true friend.' Jean deeply appreciates her understanding and support. The adjective meaning 'true' takes its feminine form here to match the noun it describes."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea puts her personal bond with Jean ahead of financial concerns and vows to protect him more carefully. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("jean", "Merci Andréa, tu es une vraie amie.")
