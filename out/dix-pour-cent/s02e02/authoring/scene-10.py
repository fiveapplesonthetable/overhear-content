# Authoring module for dix-pour-cent s02e02 scene 10 (cues 290-335).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-10.py --out out/dix-pour-cent/s02e02/scene-10.json

ID = "dix-pour-cent-s02e02-scene-10"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 10
TITLE = "Un secret au bar  (A Secret at the Bar)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo", "emilie": "emilie"}
LABELS = {"lea": "Camille", "theo": "Hervé", "emilie": "Sofia"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 290-335. Camille, Hervé, and Sofia share drinks at a Parisian bar. "
               "Hervé lets slip the agency rumor that Camille is Christophe Lambert's secret daughter, "
               "and Sofia enthusiastically promises to keep the secret. "
               "Adapted for A1 French.")

INTRO = ("At a Parisian bar after work, Camille, Hervé, and Sofia relax over drinks. "
         "The conversation turns playful until Hervé blabs a huge agency secret about Camille's parentage. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Santé à tout le monde!",
  "Cheers to everyone!",
  [(293, "Santé.")], "Expanded with à tout le monde"),
 ("emilie", "Comment tu vas ce soir, Camille?",
  "How are you doing tonight, Camille?",
  [(298, "Comment tu vas ?")], "Added ce soir, Camille"),
 ("lea", "Ça va très bien, merci beaucoup.",
  "I am doing very well, thank you very much.",
  [(298, "Comment tu vas ?")], "Adapted greeting response"),
 ("emilie", "Pourquoi tu ne sors pas avec Hippolyte?",
  "Why don't you go out with Hippolyte?",
  [(307, "Pourquoi tu ne sors pas avec Hippolyte")], "Shortened name"),
 ("lea", "Ne dis pas n'importe quoi, Sofia.",
  "Do not say foolish things, Sofia.",
  [(308, "ne dis pas n'importe quoi.")], "Added Sofia"),
 ("lea", "On est amis, c'est tout.",
  "We are friends, that is all.",
  [(310, "On est amis, c'est tout.")], ""),
 ("theo", "Tu plaisantes? Vous êtes faits l'un pour l'autre!",
  "Are you kidding? You are made for each other!",
  [(311, "Tu plaisantes ?"), (312, "faits l'un pour l'autre !")], "Combined cues"),
 ("lea", "Non, on se ressemble trop.",
  "No, we are too similar.",
  [(313, "Non, on se ressemble trop.")], ""),
 ("lea", "Non, je vais juste aux toilettes.",
  "No, I am just going to the restroom.",
  [(316, "Non, je vais juste aux toilettes.")], ""),
 ("theo", "Leurs pères se connaissent très bien.",
  "Their fathers know each other very well.",
  [(322, "Leurs pères se connaissent bien.")], "Added très"),
 ("emilie", "Pourquoi elle ne le dit pas?",
  "Why does she not say it?",
  [(326, "Pourquoi elle ne le dit pas ?")], ""),
 ("theo", "C'est un grand secret de famille.",
  "It is a big family secret.",
  [(327, "C'est un secret de famille.")], "Added grand"),
 ("emilie", "Qui est son vrai père?",
  "Who is her real father?",
  [(328, "Qui est son père ?")], "Added vrai"),
 ("theo", "Christophe Lambert! C'est son père!",
  "Christophe Lambert! That is her father!",
  [(331, "Christophe Lambert !")], "Added C'est son père"),
 ("emilie", "Sérieux? C'est incroyable!",
  "Seriously? That is incredible!",
  [(332, "Sérieux !")], "Added C'est incroyable"),
 ("theo", "Elle lui ressemble beaucoup, tu trouves aussi?",
  "She looks a lot like him, do you think so too?",
  [(333, "Elle lui ressemble."), (333, "Tu trouves aussi ?")], "Combined cues"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Cheers to everyone!' Hervé raises his glass to toast the group. "
  "The noun 'sante' is the standard French toast, literally meaning health."),
 (1, None,
  "'How are you doing tonight, Camille?' Sofia checks in with her colleague warmly. "
  "The interrogative 'comment tu vas' is a common conversational way to ask how someone is."),
 (2, None,
  "'I am doing very well, thank you very much.' Camille replies politely. "
  "The adverbial intensifier 'tres bien' pairs with 'merci beaucoup' in everyday social exchanges."),
 (3, None,
  "'Why don't you go out with Hippolyte?' Sofia innocently brings up the handsome young actor. "
  "The negative question 'pourquoi tu ne sors pas' uses the verb 'sortir avec' for dating."),
 (4, None,
  "'Do not say foolish things, Sofia.' Camille deflects the awkward question instantly. "
  "The idiom 'dire n'importe quoi' means to talk nonsense or speak recklessly."),
 (5, None,
  "'We are friends, that is all.' Camille firmly sets the record straight. "
  "The informal pronoun 'on' pairs with 'est amis', ended by the conclusive idiom 'c'est tout'."),
 (6, None,
  "'Are you kidding? You are made for each other!' Hervé teases them enthusiastically. "
  "The expression 'etre faits l'un pour l'autre' means to be made for each other."),
 (7, None,
  "'No, we are too similar.' Camille explains her hesitation. "
  "The reflexive verb 'se ressembler' expresses mutual resemblance, modified by the adverb 'trop'."),
 (8, None,
  "'No, I am just going to the restroom.' Camille excuses herself from the table. "
  "The phrase 'aller aux toilettes' is the customary French way to say going to the restroom."),
 (9, None,
  "'Their fathers know each other very well.' Hervé drops a mysterious family hint. "
  "The possessive determiner 'leurs' agrees with the plural noun 'peres'."),
 (10, None,
  "'Why does she not say it?' Sofia wonders why the family connection is kept quiet. "
  "The direct object pronoun 'le' replaces the unspoken fact before the verb 'dit'."),
 (11, None,
  "'It is a big family secret.' Hervé explains the air of mystery. "
  "The noun phrase 'secret de famille' describes a confidential household matter."),
 (12, None,
  "'Who is her real father?' Sofia asks with intense curiosity. "
  "The interrogative pronoun 'qui' asks for an identity, qualified by 'vrai pere'."),
 (13, None,
  "'Christophe Lambert! That is her father!' Hervé dramatically reveals the star name. "
  "The exclamation pairs the famous actor's name with the presentative 'c'est'."),
 (14, None,
  "'Seriously? That is incredible!' Sofia reacts with genuine astonishment. "
  "The adjective 'incroyable' expresses disbelief, following the informal exclamation 'serieux'."),
 (15, None,
  "'She looks a lot like him, do you think so too?' Hervé seeks agreement on the likeness. "
  "The phrase 'ressembler a quelqu'un' takes the indirect pronoun 'lui'."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Hervé shares the outrageous agency rumor about Camille's parentage, while Sofia reacts with total surprise. "
         "Camille's cover story remains intact for now.")
CLOSING = ("emilie", "Sérieux? C'est incroyable!")
