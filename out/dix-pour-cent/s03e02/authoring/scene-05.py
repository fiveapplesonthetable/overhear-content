# Authoring module for dix-pour-cent s03e02 scene 05 (cues 358-429).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-05.py --out out/dix-pour-cent/s03e02/scene-05.json

ID = "dix-pour-cent-s03e02-scene-05"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 5
TITLE = "Une soirée incognito  (An Incognito Evening)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Monica", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 358-429. Gabriel takes movie star Monica Bellucci incognito to a party hosted by his brother's friends. "
               "Under the pseudonym Chantal, Monica experiences everyday social life. Adapted for A1 French.")

INTRO = ("Talent agent Gabriel Sarda takes glamorous Italian actress Monica Bellucci to a casual flat party hosted by his brother's friends. "
         "Hoping to meet ordinary people without celebrity attention, Monica attends incognito under the pseudonym Chantal. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Je ne suis pas très sûre de moi.",
  "I am not very sure of myself.",
  [(371, "Je suis pas sûre.")], "Monica feels nervous outside the party"),
 ("gabriel", "Tu es vraiment parfaite comme ça!",
  "You are really perfect like that!",
  [(372, "T'es super bien comme ça.")], "Gabriel reassures her about the disguise"),
 ("gabriel", "Tu n'es jamais sortie incognito?",
  "Have you never gone out incognito?",
  [(373, "Mais t'as jamais fait ça, sorti le réconito ?")], "Gabriel asks about past experiences"),
 ("lea", "Non, je n'ai jamais fait cela.",
  "No, I have never done that.",
  [(374, "Mais non, jamais.")], "Monica admits it is her first time"),
 ("gabriel", "Nous allons bien nous amuser ce soir.",
  "We are going to have fun tonight.",
  [(375, "Tu vas voir, on va se marrer.")], "Gabriel promises an entertaining evening"),
 ("gabriel", "Ce sont tous des amis de mon frère.",
  "They are all friends of my brother.",
  [(378, "C'est des potes de mon frère.")], "Gabriel explains who is hosting"),
 ("gabriel", "Il y a beaucoup de personnes célibataires.",
  "There are many single people.",
  [(379, "Il y a plein de célibataires.")], "Gabriel highlights the guests"),
 ("gabriel", "Je te présente mon amie Chantal.",
  "I introduce to you my friend Chantal.",
  [(385, "Je suis venu avec une amie."), (386, "Chantal.")], "Gabriel introduces Monica at the door"),
 ("lea", "Bonsoir à tous, enchantée de vous rencontrer.",
  "Good evening everyone, delighted to meet you.",
  [(389, "Salut, Chantal."), (394, "Bonsoir.")], "Monica greets the host warmly"),
 ("gabriel", "Pourquoi as-tu choisi le prénom Chantal?",
  "Why did you choose the first name Chantal?",
  [(396, "Et pourquoi Chantal ?")], "Gabriel asks about the pseudonym"),
 ("lea", "J'ai trouvé cela assez normal pour moi.",
  "I found that normal enough for me.",
  [(397, "Bah, j'ai trouvé ça assez femme normale, non ?")], "Monica explains her disguise persona"),
 ("gabriel", "Veux-tu boire un bon mojito avec moi?",
  "Do you want to drink a nice mojito with me?",
  [(419, "Tu veux un mojito ?")], "Gabriel offers a fresh drink"),
 ("lea", "Oui avec plaisir, je m'amuse beaucoup!",
  "Yes with pleasure, I am having a lot of fun!",
  [(421, "Bah, oui."), (427, "Je suis chargé."), (429, "Mais tout va bien.")], "Monica accepts cheerfully"),
]

OPENER = "Let's examine how Gabriel helps Monica to navigate her incognito party entrance line by line."

WALK = [
 (0, None,
  "'I am not very sure of myself.' Monica admits her hesitation before entering the party in disguise. Notice the classic French sandwich negation wrapping right around 'the verb'."),
 (1, None,
  "'You are really perfect like that!' Gabriel reassures Monica that her casual disguise looks completely natural. Gabriel uses the casual singular 'you' with 'this line', showing close familiarity."),
 (2, None,
  "'Have you never gone out incognito?' Gabriel wonders if the world-famous actress has ever hidden her identity. The clause hinges on the everyday verb meaning 'gone out'."),
 (3, None,
  "'No, I have never done that.' Monica confesses that attending normal social gatherings is entirely new to her. In spoken French, the little word before 'have' drops its final vowel and attaches with an apostrophe."),
 (4, None,
  "'We are going to have fun tonight.' Gabriel encourages her to relax and enjoy being treated like anyone else. French forms the near future by pairing the present tense of 'to go' directly with 'to have fun'."),
 (5, None,
  "'They are all friends of my brother.' Gabriel clarifies that the hosts belong to his brother's casual circle. The key noun here means 'friends', anchored by its matching French article."),
 (6, None,
  "'There are many single people.' Gabriel playfully mentions that the gathering includes unattached guests. Notice how 'has' leads directly into the noun meaning 'people'."),
 (7, None,
  "'I introduce to you my friend Chantal.' Gabriel introduces Monica to the hosts under her chosen false identity. Notice how 'introduce' leads directly into the noun meaning 'friend'."),
 (8, None,
  "'Good evening everyone, delighted to meet you.' Monica greets the hosts politely as she steps inside the flat. The formal 'you' pronoun sets a courteous, professional distance around 'to meet.'."),
 (9, None,
  "'Why did you choose the first name Chantal?' Gabriel inquires about the humorous origin of her chosen pseudonym. This conversational past tense combines a helper verb with the past participle for 'chosen'."),
 (10, None,
  "'I found that normal enough for me.' Monica explains that the name sounded pleasantly down-to-earth. Notice how the short vowel drops before a vowel sound around 'I have', making the phrase flow smoothly as one unit."),
 (11, None,
  "'Do you want to drink a nice mojito with me?' Gabriel gets drinks from the improvised kitchen bar. The verb meaning 'do you want' pairs naturally with the noun for 'mojito' in everyday conversation."),
 (12, None,
  "'Yes with pleasure, I am having a lot of fun!' Monica accepts the cocktail and enjoys her incognito adventure. Notice how 'amuse myself' leads directly into the noun meaning 'pleasure'."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Gabriel successfully introduces Monica to ordinary Parisian nightlife under the amusing persona of Chantal. "
         "Let's review the key conversational expressions and social vocabulary from this scene.")

CLOSING = ("lea", "Oui avec plaisir, je m'amuse beaucoup!")
