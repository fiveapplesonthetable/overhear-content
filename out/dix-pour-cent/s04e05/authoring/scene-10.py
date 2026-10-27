# Authoring module for dix-pour-cent s04e05 scene 10 (cues 434-438).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s04e05/scene-10.json

ID = "dix-pour-cent-s04e05-scene-10"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 10
TITLE = "Message pour Colette  (A Message for Colette)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 434-438. Late in the evening, Andrea calls Colette and leaves a gentle, concerned voicemail asking for news. "
    "Soon after, rival agent Elise Formain sends a surprising message offering her own niece as a full-time nanny."
)

INTRO = (
    "Alone in her quiet apartment, Andrea Martel dials Colette Brancillon's phone number. "
    "Reaching voicemail, she leaves a gentle message expressing her worry and yearning for news. "
    "Moments later, rival agent Elise Formain sends an unexpected message with a timely solution for baby Flora. "
    "Let's listen to their words in French first."
)

OPENER = "Let's examine the messages line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Colette, c'est moi au téléphone.",
     "Colette, it is me on the phone.",
     [(434, "Colette, c'est moi.")], "Andrea begins her voicemail message"),
    ("lea", "Je voulais savoir comment tu vas.",
     "I wanted to know how you are doing.",
     [(435, "Je voulais juste savoir comment tu allais")], "Andrea asks tenderly about Colette"),
    ("lea", "Tu ne réponds plus à mes messages.",
     "You no longer answer my messages.",
     [(435, "parce que je...")], "Andrea remarks on the painful silence"),
    ("lea", "Je m'inquiète beaucoup pour toi.",
     "I worry a lot about you.",
     [(436, "Je m'inquiète.")], "Andrea admits her deep concern"),
    ("lea", "Flora et moi, on pense à toi.",
     "Flora and I, we think of you.",
     [(436, "Je m'inquiète.")], "Andrea mentions their shared daughter"),
    ("lea", "Rappelle-moi vite, s'il te plaît.",
     "Call me back soon, please.",
     [(437, "Rappelle-moi, donne-moi de tes nouvelles.")], "Andrea asks for a quick phone call"),
    ("lea", "Prends bien soin de toi.",
     "Take good care of yourself.",
     [(437, "Prends soin de toi.")], "Andrea ends her message with affectionate advice"),
    ("lea", "Le silence est très lourd ce soir.",
     "The silence is very heavy tonight.",
     [(437, "Prends soin de toi.")], "Andrea sighs as she hangs up"),
    ("elise", "Andréa, j'ai une bonne nouvelle!",
     "Andrea, I have good news!",
     [(438, "Ma nièce peut garder Flora jour et nuit.")], "Elise texts with unexpected cheerfulness"),
    ("elise", "Ma nièce cherche un nouveau travail.",
     "My niece is looking for new work.",
     [(438, "Ma nièce peut garder Flora")], "Elise introduces her relative's availability"),
    ("elise", "Elle peut garder Flora jour et nuit.",
     "She can babysit Flora day and night.",
     [(438, "jour et nuit. De rien!")], "Elise offers twenty-four hour childcare"),
    ("lea", "C'est une offre tout à fait inattendue.",
     "It is a completely unexpected offer.",
     [(438, "De rien!")], "Andrea reacts with surprise to the gesture"),
    ("lea", "Cela sauve ma semaine de travail!",
     "That saves my work week!",
     [(438, "De rien!")], "Andrea recognizes the immense relief"),
]

WALK = [
    (0, None,
     "'Colette, it is me on the phone.' Andrea begins her voicemail message. "
     "The emphatic pronoun 'moi' indicates identity."),
    (1, None,
     "'I wanted to know how you are doing.' Andrea inquires softly after Colette's well-being. "
     "The verb form 'voulais' comes from 'vouloir' in the imperfect tense."),
    (2, None,
     "'You no longer answer my messages.' Andrea notes the absence of communication. "
     "The negative structure 'ne... plus' expresses no longer."),
    (3, None,
     "'I worry a lot about you.' Andrea confesses her anxiety. "
     "The pronominal verb 's'inquieter' means to worry."),
    (4, None,
     "'Flora and I, we think of you.' Andrea highlights their shared family bond. "
     "The verb phrase 'pense a' means to think of someone."),
    (5, None,
     "'Call me back soon, please.' Andrea requests an answer without demanding. "
     "The imperative 'rappelle-moi' comes from 'rappeler'."),
    (6, None,
     "'Take good care of yourself.' Andrea closes with a warm expression of care. "
     "The idiom 'prendre soin de' translates to take care of."),
    (7, None,
     "'The silence is very heavy tonight.' Andrea reflects on the loneliness of her home. "
     "The adjective 'lourd' means heavy."),
    (8, None,
     "'Andrea, I have good news!' Elise sends an enthusiastic message. "
     "The adjective 'bonne' qualifies the feminine noun 'nouvelle'."),
    (9, None,
     "'My niece is looking for new work.' Elise presents her niece's job search. "
     "The noun 'niece' indicates a sibling's daughter."),
    (10, None,
     "'She can babysit Flora day and night.' Elise proposes round-the-clock childcare. "
     "The temporal phrase 'jour et nuit' means day and night."),
    (11, None,
     "'It is a completely unexpected offer.' Andrea marvels at the convenient timing. "
     "The adjective 'inattendue' means unexpected."),
    (12, None,
     "'That saves my work week!' Andrea feels a huge burden lifted from her shoulders. "
     "The verb 'sauve' comes from 'sauver', to save."),
]

OUTRO = (
    "Although Andrea misses Colette deeply, Elise's surprising generosity solves her immediate childcare dilemma. "
    "With Flora taken care of, Andrea can now dedicate all her energy to her actors. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Merci pour cette aide précieuse, Élise!")
