# Authoring module for dix-pour-cent s04e01 scene 02 (cues 31-73).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-02.py --out out/dix-pour-cent/s04e01/scene-02.json

ID = "dix-pour-cent-s04e01-scene-02"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 2
TITLE = "L'enthousiasme de Charlotte  (Charlotte's Enthusiasm)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "charlotte": "emilie", "oscar": "theo"}
LABELS = {"lea": "Andréa", "charlotte": "Charlotte", "oscar": "Oscar"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 31-73. Charlotte asks Andrea about Oscar Rondo's script. Andrea lies and praises it, right before Oscar arrives. Adapted for A1 French.")

INTRO = ("At the airport arrival terminal, Andrea Martel greets internationally acclaimed actress Charlotte Gainsbourg after an eleven-hour flight. "
         "When Charlotte inquires about the artistic merit of her lifelong friend Oscar Rondo's screenplay, Andrea bluffs and lavishes it with praise. "
         "Just as Camille sends a text warning that the script is unwatchable, Oscar himself walks up to seal the deal. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Tu restes magnifique après ce long voyage.",
  "You remain gorgeous after this long journey.",
  [(31, "11 h d'avion")], "Complimented star's appearance after flight"),
 ("charlotte", "J'ai dormi pendant tout le vol.",
  "I slept during the whole flight.",
  [(31, "11 h d'avion")], "Attributed fresh looks to onboard rest"),
 ("charlotte", "Je refuse ce rôle si c'est mauvais.",
  "I refuse this role if it is bad.",
  [(41, "si ce n'est pas bien")], "Conditioned acceptance on project quality"),
 ("charlotte", "Dis-moi, tu as lu le scénario d'Oscar?",
  "Tell me, did you read Oscar's script?",
  [(46, "Tu l'as lu")], "Pressed agent for direct editorial assessment"),
 ("lea", "Oui, je l'ai lu ce matin.",
  "Yes, I read it this morning.",
  [(47, "Oui, je l'ai lu")], "Bluffed about reviewing manuscript"),
 ("lea", "C'est vraiment une histoire formidable.",
  "It is really a wonderful story.",
  [(49, "C'est vraiment bien")], "Praised unread script generously"),
 ("charlotte", "Je suis tellement soulagée de ton avis!",
  "I am so relieved by your opinion!",
  [(50, "Je suis tellement soulagée")], "Expressed immense relief at favorable verdict"),
 ("lea", "Camille m'écrit que c'est une catastrophe.",
  "Camille texts me that it is a disaster.",
  [(51, "C'EST NAZE")], "Silently panicked over harsh verdict"),
 ("oscar", "Charlotte, quelle joie de te retrouver ici!",
  "Charlotte, what a joy to meet you here!",
  [(60, "mon meilleur ami")], "Greeted leading actress enthusiastically"),
 ("charlotte", "Voici Oscar, mon ami d'enfance.",
  "Here is Oscar, my childhood friend.",
  [(60, "mon meilleur ami")], "Introduced director to talent agent"),
 ("charlotte", "Mon agent adore ton nouveau scénario.",
  "My agent loves your new script.",
  [(68, "elle a adoré")], "Passed on enthusiastic endorsement to director"),
 ("oscar", "C'est un honneur immense pour moi.",
  "It is an immense honor for me.",
  [(68, "elle a adoré")], "Expressed heartfelt gratitude for praise"),
 ("charlotte", "Nous allons faire ce beau film ensemble!",
  "We are going to make this beautiful film together!",
  [(70, "On fait un film ensemble")], "Officially confirmed commitment to movie project"),
 ("lea", "Je me retrouve dans un piège terrible.",
  "I find myself in a terrible trap.",
  [(51, "C'EST NAZE")], "Recognized perilous dilemma"),
]

OPENER = "Let's observe as Andrea bluffs about the script just as director Oscar arrives."

WALK = [
 (0, None,
  "'You remain gorgeous after this long journey.' The informal 'you' form around 'remain' marks a direct, personal relationship. The informal 'you' form around 'remain' marks a direct, personal relationship."),
 (1, None,
  "'I slept during the whole flight.' A simple explanation crediting good rest for defying jet lag. The verb meaning 'I have' pairs naturally with the noun for 'flight' in everyday conversation."),
 (2, None,
  "'I refuse this role if it is bad.' A clear professional boundary insisting on script quality despite personal friendship. Notice how the short vowel drops before a vowel sound around 'refuse', making the phrase flow smoothly as one unit."),
 (3, None,
  "'Tell me, did you read Oscar's script?' A direct probe seeking honest feedback from her trusted agent. Notice how 'tell me' leads directly into the noun meaning 'screenplay'."),
 (4, None,
  "'Yes, I read it this morning.' A reckless falsehood pretending to have reviewed the manuscript. This conversational past tense combines a helper verb with the past participle for 'read'."),
 (5, None,
  "'It is really a wonderful story.' In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe. In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe."),
 (6, None,
  "'I am so relieved by your opinion!' Charlotte uses the casual singular 'you' with 'opinion', showing close familiarity. Charlotte uses the casual singular 'you' with 'opinion', showing close familiarity."),
 (7, None,
  "'Camille texts me that it is a disaster.' An internal panic reacting to the incoming devastating text message. Notice how the short vowel drops before a vowel sound around 'composed', making the phrase flow smoothly as one unit."),
 (8, None,
  "'Charlotte, what a joy to meet you here!' An affectionate surprise arrival catching both women off guard. The verb meaning 'to meet' pairs naturally with the noun for 'joy' in everyday conversation."),
 (9, None,
  "'Here is Oscar, my childhood friend.' An affectionate introduction highlighting their lifelong creative bond. The key noun here means 'friend', anchored by its matching French article."),
 (10, None,
  "'My agent loves your new script.' The informal 'you' form around 'adore' marks a direct, personal relationship. The informal 'you' form around 'adore' marks a direct, personal relationship."),
 (11, None,
  "'It is an immense honor for me.' The verb meaning 'it is' pairs naturally with the noun for 'honor' in everyday conversation."),
 (12, None,
  "'We are going to make this beautiful film together!' The verb meaning 'let us go' pairs naturally with the noun for 'movie' in everyday conversation."),
 (13, None,
  "'I find myself in a terrible trap.' A horrified realization acknowledging the disastrous consequences of a hasty bluff. The descriptive adjective for 'terrible' agrees in gender and number with its noun."),
]

TRANSITION = "Now let's listen to Andrea, Charlotte, and Oscar again at full speed."

OUTRO = ("Having endorsed a script that she has not read and that Camille considers dreadful, Andrea is trapped in her own lie. "
         "She must now find a delicate way to extract Charlotte from the project without alienating her star client.")

CLOSING = ("lea", "La situation devient intenable.")
