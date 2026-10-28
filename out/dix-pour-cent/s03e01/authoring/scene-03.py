# Authoring module for dix-pour-cent s03e01 scene 03 (cue 57).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-03.py --out out/dix-pour-cent/s03e01/scene-03.json

ID = "dix-pour-cent-s03e01-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 3
TITLE = "Un verre d'eau  (A Glass of Water)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cue 57. Gabriel returns with a glass of water for Andréa as her contraction passes, "
               "urging her to slow down her work pace for her health. Adapted for A1 French.")

INTRO = ("Catching her breath in her office chair, pregnant agent Andrea receives a glass of water from loyal colleague Gabriel. "
         "As her physical discomfort subsides, Gabriel urges her to moderate her intense working schedule for her child's sake. "
         "Let's listen to their intimate conversation in French first.")

STORY = [
 ("gabriel", "Voici ton verre d'eau fraîche, Andréa.",
  "Here is your glass of fresh water, Andrea.",
  [(55, "Je reviens tout de suite.")], "Offered fresh water"),
 ("lea", "C'est bon, la contraction est passée.",
  "It is fine, the contraction has passed.",
  [(57, "C'est bon, c'est passé.")], "Confirmed pain subsided"),
 ("gabriel", "Bois un peu d'eau, doucement.",
  "Drink a little water, gently.",
  [(53, "juste un verre d'eau.")], "Advised gentle drinking"),
 ("lea", "Merci Gabriel, je me sens déjà mieux.",
  "Thank you Gabriel, I already feel better.",
  [(57, "C'est bon, c'est passé.")], "Expressed physical relief"),
 ("gabriel", "Tu as souvent de telles douleurs?",
  "Do you often have such pains?",
  [(52, "des fois, j'ai des contractions.")], "Inquired about pain frequency"),
 ("lea", "Parfois, quand je marche trop vite.",
  "Sometimes, when I walk too fast.",
  [(52, "des fois, j'ai des contractions.")], "Attributed pain to rushing"),
 ("gabriel", "Tu devrais vraiment ralentir le rythme.",
  "You should really slow down the pace.",
  [(61, "c'est pas une raison pas de te reposer, là.")], "Recommended slowing pace"),
 ("lea", "Impossible avec tous mes rendez-vous importants!",
  "Impossible with all my important meetings!",
  [(42, "fait bien partie des comptes de l'année ?")], "Defended busy agenda"),
 ("gabriel", "La santé de ton bébé passe avant.",
  "The health of your baby comes first.",
  [(61, "pas de te reposer, là.")], "Prioritized baby health"),
 ("lea", "Je le sais bien, mon cher Gabriel.",
  "I know it well, my dear Gabriel.",
  [(57, "C'est bon, c'est passé.")], "Conceded friendly point"),
 ("gabriel", "Promets-moi de te reposer ce soir.",
  "Promise me to rest tonight.",
  [(61, "te reposer, là.")], "Asked for rest promise"),
 ("lea", "D'accord, je vais rentrer plus tôt.",
  "All right, I am going to go home earlier.",
  [(60, "Ouais, moi non plus.")], "Agreed to leave early"),
 ("gabriel", "Je surveillerai ton départ du bureau.",
  "I will keep an eye on your departure from the office.",
  [(61, "te reposer")], "Offered protective oversight"),
 ("lea", "Tu es vraiment un ami formidable!",
  "You are truly a wonderful friend!",
  [(56, "Ouais, super.")], "Celebrated close friendship"),
]

OPENER = "Let's observe how Gabriel expresses protective concern for Andrea's wellbeing."

WALK = [
 (0, None,
  "'Here is your glass of fresh water, Andrea.' A helpful presentative introducing refreshing water. The key noun here means 'drinking glass', anchored by its matching French article."),
 (1, None,
  "'It is fine, the contraction has passed.' The verb meaning 'passed' pairs naturally with the noun for 'uterine contraction' in everyday conversation."),
 (2, None,
  "'Drink a little water, gently.' Notice how 'drink' leads directly into the noun meaning 'drinking water'. Notice how 'drink' leads directly into the noun meaning 'drinking water'."),
 (3, None,
  "'Thank you Gabriel, I already feel better.' The reflexive pronoun sits right in front of the verb for 'feel', turning the action back onto the subject."),
 (4, None,
  "'Do you often have such pains?' The informal 'you' form around 'have' marks a direct, personal relationship. The informal 'you' form around 'have' marks a direct, personal relationship."),
 (5, None,
  "'Sometimes, when I walk too fast.' The clause hinges on the everyday verb meaning 'walk'."),
 (6, None,
  "'You should really slow down the pace.' A conditional modal advising professional restraint. The informal 'you' form around 'should' marks a direct, personal relationship."),
 (7, None,
  "'Impossible with all my important meetings!' The descriptive adjective for 'impossible' agrees in gender and number with its noun. The descriptive adjective for 'impossible' agrees in gender and number with its noun."),
 (8, None,
  "'The health of your baby comes first.' Notice how 'passes' leads directly into the noun meaning 'health'. Notice how 'passes' leads directly into the noun meaning 'health'."),
 (9, None,
  "'I know it well, my dear Gabriel.' A concession acknowledging sincere advice. The descriptive adjective for 'dear' agrees in gender and number with its noun."),
 (10, None,
  "'Promise me to rest tonight.' Notice how 'promise me' leads directly into the noun meaning 'evening hours'. Notice how 'promise me' leads directly into the noun meaning 'evening hours'."),
 (11, None,
  "'All right, I am going to go home earlier.' An agreeing near-future commitment to rest. Notice how 'am going' leads directly into the noun meaning 'agreement'."),
 (12, None,
  "'I will keep an eye on your departure from the office.' Notice how 'will watch over' leads directly into the noun meaning 'leaving'. Notice how 'will watch over' leads directly into the noun meaning 'leaving'."),
 (13, None,
  "'You are truly a wonderful friend!' The descriptive adjective for 'wonderful' agrees in gender and number with its noun. The descriptive adjective for 'wonderful' agrees in gender and number with its noun."),
]

TRANSITION = "Now let's listen to Gabriel and Andrea again at full speed."

OUTRO = ("Gabriel secures a promise from Andrea to head home early, showing how deep friendship endures beneath agency rivalries. "
         "Andrea recovers her strength, ready to tackle the rest of the day with renewed care.")

CLOSING = ("gabriel", "Prends bien soin de toi, Andréa.")
