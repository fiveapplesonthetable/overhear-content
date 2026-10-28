# Authoring module for dix-pour-cent s03e05 scene 04 (cues 59-116).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-04.py --out out/dix-pour-cent/s03e05/scene-04.json

ID = "dix-pour-cent-s03e05-scene-04"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 4
TITLE = "La réclamation américaine  (The American Claim)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Hicham", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 59-116. Hicham receives a letter from American producers demanding two million dollars over Isabelle Huppert's double booking. Adapted for A1 French.")

INTRO = ("In the executive office, director Hicham Janowski receives an explosive legal demand from abroad. "
         "American film producers are suing ASK for two million dollars after discovering Isabelle Huppert's secret double filming schedule. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Une lettre recommandée très grave vient d'arriver.",
  "A very serious registered letter just arrived.",
  [(65, "J'ai un recommandé qui est arrivé")], "Announced arrival of legal letter"),
 ("mathias", "De quelle société provient ce courrier?",
  "Which company does this mail come from?",
  [(66, "Moss et Dunning, les producteurs américains")], "Inquired about origin"),
 ("lea", "Les producteurs américains nous attaquent en justice.",
  "American producers are suing us in court.",
  [(67, "Ils nous attaquent pour rupture de contrat")], "Disclosed breach of contract suit"),
 ("mathias", "Que réclament ces producteurs exactement?",
  "What do these producers claim exactly?",
  [(69, "Ils réclament 2 millions de dollars")], "Asked about damages"),
 ("lea", "Ils réclament deux millions de dollars!",
  "They are claiming two million dollars!",
  [(69, "Ils réclament 2 millions de dollars")], "Revealed claimed amount"),
 ("mathias", "Deux millions? C'est une somme énorme!",
  "Two million? That is an enormous sum!",
  [(71, "2 millions ?"), (72, "Mais c'est beaucoup, ça !")], "Voiced shock at sum"),
 ("lea", "C'est à cause de l'interruption de tournage.",
  "It is because of the production shutdown.",
  [(73, "la semaine d'interruption")], "Explained root of damages"),
 ("mathias", "Leur assurance ne couvre pas ces frais?",
  "Does their insurance not cover these costs?",
  [(80, "Ils sont couverts par l'assurance, non ?")], "Asked about insurance"),
 ("lea", "L'assurance a formellement rejeté leur dossier.",
  "The insurance formally rejected their claim.",
  [(83, "L'assurance a rejeté leur dossier")], "Confirmed claim denial"),
 ("mathias", "Nous devons négocier avec leurs avocats.",
  "We must negotiate with their lawyers.",
  [(95, "C'est pour mieux négocier")], "Urged negotiation approach"),
 ("lea", "Pour négocier, il faut un levier solide.",
  "To negotiate, one needs solid leverage.",
  [(98, "pour négocier, il faut un levier")], "Pointed out lack of leverage"),
 ("mathias", "Pouvons-nous utiliser les fonds de réserve?",
  "Can we use reserve funds?",
  [(100, "on a les fonds, non ?")], "Suggested capital reserves"),
 ("lea", "Je refuse de perdre tout mon argent!",
  "I refuse to lose all my money!",
  [(102, "Tu veux dire, j'ai les fonds ?")], "Rejected financial liability"),
 ("mathias", "Nous allons trouver une solution ensemble.",
  "We are going to find a solution together.",
  [(100, "on a les fonds, non ?")], "Promised cooperative resolution"),
]

OPENER = "Let's observe as Hicham informs Mathias of the disastrous lawsuit."

WALK = [
 (0, None,
  "'A very serious registered letter just arrived.' An alarming announcement delivering urgent legal correspondence. The verb meaning 'comes' pairs naturally with the noun for 'letter' in everyday conversation."),
 (1, None,
  "'Which company does this mail come from?' Notice how 'comes from' leads directly into the noun meaning 'company'. Notice how 'comes from' leads directly into the noun meaning 'company'."),
 (2, None,
  "'American producers are suing us in court.' The verb meaning 'attack' pairs naturally with the noun for 'producers' in everyday conversation."),
 (3, None,
  "'What do these producers claim exactly?' The verb meaning 'claim' pairs naturally with the noun for 'producers' in everyday conversation."),
 (4, None,
  "'They are claiming two million dollars!' The verb meaning 'claim' pairs naturally with the noun for 'millions' in everyday conversation."),
 (5, None,
  "'Two million? That is an enormous sum!' The key noun here means 'millions', anchored by its matching French article. The key noun here means 'millions', anchored by its matching French article."),
 (6, None,
  "'It is because of the production shutdown.' The key noun here means 'cause', anchored by its matching French article. The key noun here means 'cause', anchored by its matching French article."),
 (7, None,
  "'Does their insurance not cover these costs?' Notice the classic French sandwich negation wrapping right around 'covers'. Notice the classic French sandwich negation wrapping right around 'covers'."),
 (8, None,
  "'The insurance formally rejected their claim.' A categorical denial ending hopes of coverage. This conversational past tense combines a helper verb with the past participle for 'rejected'."),
 (9, None,
  "'We must negotiate with their lawyers.' A pragmatic recommendation urging settlement talks. Notice how 'must' leads directly into the noun meaning 'lawyers'."),
 (10, None,
  "'To negotiate, one needs solid leverage.' A realistic tactical assessment evaluating bargaining power. Notice how 'to negotiate' leads directly into the noun meaning 'leverage'."),
 (11, None,
  "'Can we use reserve funds?' In everyday spoken French, rising intonation on 'can we' at the end is enough to turn the sentence into a question. In everyday spoken French, rising intonation on 'can we' at the end is enough to turn the sentence into a question."),
 (12, None,
  "'I refuse to lose all my money!' An angry executive outburst rejecting personal financial sacrifice. The verb meaning 'refuse' pairs naturally with the noun for 'money' in everyday conversation."),
 (13, None,
  "'We are going to find a solution together.' Notice how 'let us go' leads directly into the noun meaning 'solution'. Notice how 'let us go' leads directly into the noun meaning 'solution'."),
]

TRANSITION = "Now let's listen to Hicham and Mathias again at full speed."

OUTRO = ("Furious over the impending multi-million dollar disaster, Hicham orders Mathias to contain the American fallout immediately. "
         "Mathias ponders their legal options, acutely aware that ASK's very financial survival hangs in the balance.")

CLOSING = ("lea", "Réglez ce dossier au plus vite.")
