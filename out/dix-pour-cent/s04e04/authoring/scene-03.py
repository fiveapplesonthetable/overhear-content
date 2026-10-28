# Authoring module for dix-pour-cent s04e04 scene 03 (cue 93).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-03.py --out out/dix-pour-cent/s04e04/scene-03.json

ID = "dix-pour-cent-s04e04-scene-03"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 3
TITLE = "Matinée à l'agence  (Morning at the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = ("Cue 93. Arriving at ASK the morning after an exhausting late night with Sandrine, "
               "Gabriel updates Andrea on Sandrine's surprising reluctance to sign the film contract.")

INTRO = ("The morning after a long night out in Paris, Gabriel arrives at the ASK agency looking visibly worn out. "
         "Andrea notices his weary appearance and inquires about his meeting with Sandrine Kiberlain, "
         "only to learn that the star actress has developed unexpected second thoughts about her next major film role. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Bonjour Gabriel, tu as bonne mine!",
     "Hello Gabriel, you look well!",
     [(93, "Bonjour.")], "Andrea greets Gabriel with teasing irony as he walks into the agency"),
    ("gabriel", "Bonjour Andréa, je suis rentré tard.",
     "Hello Andrea, I got home late.",
     [(93, "Bonjour.")], "Gabriel admits to getting very little sleep the night before"),
    ("lea", "Comment s'est passée ta longue soirée?",
     "How did your long evening go?",
     [], "new: Andrea asks for news about Sandrine Kiberlain"),
    ("gabriel", "Sandrine Kiberlain a été tout simplement remarquable.",
     "Sandrine Kiberlain was simply remarkable.",
     [], "new: Gabriel praises the actress's theatrical success"),
    ("lea", "Elle signe pour le film historique?",
     "Is she signing for the historical movie?",
     [], "new: Andrea checks whether the contract was finalized"),
    ("gabriel", "Non, elle hésite beaucoup à signer.",
     "No, she hesitates a lot about signing.",
     [], "new: Gabriel reveals Sandrine's surprising hesitation"),
    ("lea", "Que veut-elle faire à la place?",
     "What does she want to do instead?",
     [], "new: Andrea wonders what alternative project Sandrine envisions"),
    ("gabriel", "Elle rêve maintenant de faire du stand-up.",
     "She now dreams of doing stand-up comedy.",
     [], "new: Gabriel confesses her bizarre new artistic ambition"),
    ("lea", "Tu plaisantes? Elle adore le théâtre!",
     "Are you joking? She loves theater!",
     [], "new: Andrea reacts with skeptical disbelief"),
    ("gabriel", "Elle veut faire rire le public.",
     "She wants to make the audience laugh.",
     [], "new: Gabriel explains her urgent desire for comedy"),
    ("lea", "Nous devons la convaincre rapidement.",
     "We must convince her quickly.",
     [], "new: Andrea emphasizes the crucial importance of the movie contract"),
    ("gabriel", "Je vais la revoir aujourd'hui.",
     "I am going to see her again today.",
     [], "new: Gabriel promises to meet with her before her last show"),
    ("lea", "Rassure-la sur son immense talent.",
     "Reassure her about her immense talent.",
     [], "new: Andrea advises a supportive managerial approach"),
    ("gabriel", "Je ferai de mon mieux, Andréa.",
     "I will do my best, Andrea.",
     [], "new: Gabriel commits to salvaging the partnership"),
]

OPENER = "Let's explore Andrea and Gabriel's morning discussion line by line."

WALK = [
    (0, None,
     "'Hello Gabriel, you look well!' Andrea teases Gabriel about his tired and rumpled morning look. The adjective meaning 'good' takes its feminine form here to match the noun it describes."),
    (1, None,
     "'Hello Andrea, I got home late.' Gabriel confesses that his client kept him out until the early morning hours. This conversational past tense combines a helper verb with the past participle for 'returned'."),
    (2, None,
     "'How did your long evening go?' Andrea asks how negotiations went over dinner after the play. The adjective meaning 'long' takes its feminine form here to match the noun it describes."),
    (3, None,
     "'Sandrine Kiberlain was simply remarkable.' Gabriel enthusiastically describes the actress's extraordinary performance on stage. This conversational past tense combines a helper verb with the past participle for 'been'."),
    (4, None,
     "'Is she signing for the historical movie?' Andrea focuses directly on closing the lucrative film deal. Notice how 'signs' leads directly into the noun meaning 'movie'."),
    (5, None,
     "'No, she hesitates a lot about signing.' Gabriel shares the unexpected obstacle delaying the production contract. The clause hinges on the everyday verb meaning 'hesitates'."),
    (6, None,
     "'What does she want to do instead?' Andrea seeks clarification about what other roles Sandrine is considering. Inverting the verb and pronoun around 'wants' creates a crisp, polished question."),
    (7, None,
     "'She now dreams of doing stand-up comedy.' Gabriel reveals Sandrine's newfound obsession with live comedy stages. The verb meaning 'dreams' pairs naturally with the noun for 'stand-up comedy' in everyday conversation."),
    (8, None,
     "'Are you joking? She loves theater!' Andrea expresses pure shock at the prospect of an established dramatic star doing stand-up. Notice how 'are joking' leads directly into the noun meaning 'theater'."),
    (9, None,
     "'She wants to make the audience laugh.' Gabriel explains her visceral need for direct, unfiltered audience laughter. The verb meaning 'wants' pairs naturally with the noun for 'audience' in everyday conversation."),
    (10, None,
     "'We must convince her quickly.' Andrea urges Gabriel to guide their valuable star back to prestigious cinematic roles. The clause hinges on the everyday verb meaning 'must'."),
    (11, None,
     "'I am going to see her again today.' Gabriel confirms he will speak with her once more before the final curtain. Notice how the short vowel drops before a vowel sound around 'am going', making the phrase flow smoothly as one unit."),
    (12, None,
     "'Reassure her about her immense talent.' Andrea encourages Gabriel to rebuild Sandrine's confidence gently. The descriptive adjective for 'immense' agrees in gender and number with its noun."),
    (13, None,
     "'I will do my best, Andrea.' Gabriel promises to give his all to keep the agency on track. The clause hinges on the everyday verb meaning 'will do'."),
]

TRANSITION = "Now let's listen to Andrea and Gabriel's conversation once more from start to finish."

OUTRO = ("Gabriel and Andrea confront an unexpected artistic crisis with one of their most celebrated clients. "
         "Let's review the key professional, managerial, and entertainment vocabulary from this morning exchange.")

CLOSING = ("lea", "La journée s'annonce agitée.")
