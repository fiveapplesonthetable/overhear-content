# Authoring module for dix-pour-cent s01e06 scene 29 (cues 740-763).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-29.py --out out/dix-pour-cent/s01e06/scene-29.json

ID = "dix-pour-cent-s01e06-scene-29"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 29
TITLE = "Le baiser d'adieu  (The Farewell Kiss)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "colette": "Colette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 740-763. Andréa catches Colette on the street outside ASK and begs her to teach her "
    "how to love; Colette kisses her goodbye as the agency watches from the balcony above. "
    "Noémie and Arlette's remarks on the balcony in cues 746-755 are folded into Gabriel's lines to stay within three voices; "
    "feminine adjective agreement ('douée', 'forte') is restored over the masculine subtitle typos in cues 741 and 743."
)

INTRO = (
    "Andréa has just sprinted out of the ASK conference room and down to the street to catch Colette "
    "Brancillon before she leaves forever, while Gabriel, Arlette, and the assistants watch from the "
    "upstairs balcony. Listen to the French first, without worrying about catching every word."
)

STORY = [
    ("lea", "Je peux te donner plus que mon corps, je peux aussi te donner mon cœur.",
     "I can give you more than my body, I can also give you my heart.",
     [(740, "Je peux te donner plus que mon corps, je peux aussi te donner mon cœur")], ""),
    ("lea", "Je sais que je ne suis pas très douée.",
     "I know that I'm not very good at it.",
     [(741, "Je sais que"), (741, "pas très doué")], "subtitle 'doué' corrected to feminine 'douée' for Andréa"),
    ("lea", "C'est parce que j'ai peur.",
     "It's because I am afraid.",
     [(741, "C'est parce que j'ai peur")], ""),
    ("lea", "Mais je veux apprendre.",
     "But I want to learn.",
     [(742, "Mais je veux apprendre")], ""),
    ("colette", "Je ne suis pas assez forte pour t'apprendre, Andréa.",
     "I am not strong enough to teach you, Andréa.",
     [(743, "pour t'apprendre, Andréa")], "subtitle 'fort' corrected to feminine 'forte' for Colette"),
    ("lea", "Non, je veux apprendre de toi. De toi et de personne d'autre.",
     "No, I want to learn from you. From you and from no one else.",
     [(744, "Non, je veux apprendre de toi. De toi et de personne d'autre")], ""),
    ("gabriel", "Mon Dieu! Elles sont ensemble! Non, non...",
     "My God! They're together! No, no...",
     [(745, "Mon Dieu"), (749, "Non, non")], "subtitle 'Ils sont ensemble' adapted to feminine 'Elles sont ensemble'"),
    ("colette", "Prends soin de toi, Andréa.",
     "Take care of yourself, Andréa.",
     [(750, "Prends soin de toi, Andréa")], ""),
    ("lea", "Pourquoi tu dis ça? Tu m'embrasses et tu t'en vas?",
     "Why do you say that? You kiss me and you leave?",
     [(751, "Pourquoi tu dis ça"), (752, "Tu m'embrasses et tu t'en vas")], ""),
    ("gabriel", "Non, je ne crois pas que je vais l'épouser. D'abord, parce qu'elle préfère les femmes.",
     "No, I don't think that I'm going to marry her. First, because she prefers women.",
     [(757, "Non, je ne crois pas que je vais l'épouser"), (758, "D'abord, parce que... elle préfère les femmes")], ""),
    ("gabriel", "Ensuite, parce qu'elle est ma collègue et mon amie.",
     "Second, because she is my colleague and my friend.",
     [(759, "Ensuite, parce qu'elle est ma collègue et mon amie")], ""),
    ("gabriel", "Et c'est compliqué de mélanger le travail et les sentiments. Surtout avec mes clients.",
     "And it's complicated to mix work and feelings. Especially with my clients.",
     [(760, "mélanger le travail et les sentiments"), (762, "Surtout avec mes clients")], "colloquial 'Tout fout le camp' in cue 761 omitted for A1"),
]

OPENER = "Let's walk through the scene line by line. Out on the pavement, Andréa answers Colette's accusation from the party."

WALK = [
    (0, None,
     "'I can give you more than my body, I can also give you my heart.' At the party, Colette told Andréa that all she knew how to give was her body."),
    (1, None,
     "'I know that I'm not very good at it.' Andréa admits her emotional vulnerabilities and fears."),
    (2, None,
     "'It's because I am afraid.' In French, one literally says that one has fear."),
    (3, None,
     "'But I want to learn.' Andréa drops her proud armor for the first time."),
    (4, None,
     "'I am not strong enough to teach you, Andréa.' Note how the French verb 'to learn' also means 'to teach' when followed by a person."),
    (5, None,
     "'No, I want to learn from you. From you and from no one else.' The phrase 'person other' means 'anyone else' or 'no one else'."),
    (6, None,
     "'My God! They're together! No, no...' Up on the balcony, the whole agency watches in shock as Colette pulls Andréa into a passionate kiss."),
    (7, None,
     "'Take care of yourself, Andréa.' The expression 'to take care of' uses the noun for 'care'."),
    (8, None,
     "'Why do you say that? You kiss me and you leave?' The reflexive expression 'to go oneself away from it' is the everyday way to say 'to leave'."),
    (9, None,
     "'No, I don't think that I'm going to marry her. First, because she prefers women.' Up on the balcony, Arlette teases Gabriel about Andréa's drunken marriage proposal from the night before."),
    (10, None,
     "'Second, because she is my colleague and my friend.' Even though 'friend' is feminine here, French uses the masculine form 'my' before a vowel sound so the words flow smoothly."),
    (11, None,
     "'And it's complicated to mix work and feelings. Especially with my clients.' Gabriel glances toward Sofia at reception as he realizes how true his own words are."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = (
    "Colette walks away in tears, leaving Andréa heartbroken on the street while the agency faces ruin. "
    "In our final scene of the season, the four agents gather after hours over a bottle of Samuel's whiskey. See you there."
)
CLOSING = ("colette", "Prends soin de toi, Andréa.")
