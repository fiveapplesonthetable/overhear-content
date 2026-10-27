# Authoring module for dix-pour-cent s02e04 scene 24 (cues 676-735).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-24.py --out out/dix-pour-cent/s02e04/scene-24.json

ID = "dix-pour-cent-s02e04-scene-24"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 24
TITLE = "La visite de Noémie  (Noémie's Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 676-735. Noémie visits Mathias at his apartment after his difficult days at ASK. "
    "She gives him a relaxing massage to ease his stress and tight muscles."
)

INTRO = (
    "At his quiet Parisian apartment, an exhausted Mathias Barneville receives an unexpected visit from his devoted assistant Noemie. "
    "Noticing his overwhelming stress from agency battles, Noemie steps in to comfort him and ease his physical tension with a soothing massage. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Tout va bien, Mathias?",
     "Is everything going well, Mathias?",
     [(676, "Tout... va bien ?")], ""),
    ("lea", "Je peux entrer un instant?",
     "Can I come in for a moment?",
     [(677, "Je peux entrer ?")], ""),
    ("mathias", "Bien sûr, entre donc.",
     "Of course, do come in.",
     [(678, "Bien sûr.")], ""),
    ("mathias", "J'aurais rangé si j'avais su.",
     "I would have tidied up if I had known.",
     [(679, "J'aurais rangé si j'avais su.")], ""),
    ("mathias", "Je n'ai rien à t'offrir.",
     "I have nothing to offer you.",
     [(682, "En plus j'ai rien à t'offrir.")], ""),
    ("lea", "C'est une super nouvelle pour Adjani!",
     "That is great news for Adjani!",
     [(687, "super nouvelle pour Adjani.")], ""),
    ("mathias", "Oui, tout est bien réglé.",
     "Yes, everything is well sorted out.",
     [(688, "-C'est réglé, c'est super. -Oui.")], ""),
    ("mathias", "Je ne me sens pas bien.",
     "I do not feel well.",
     [(696, "Désolé, je me sens pas très bien.")], ""),
    ("lea", "Assieds-toi sur ce fauteuil.",
     "Sit down in this armchair.",
     [(702, "Assieds-toi.")], ""),
    ("mathias", "Je ne suis pas fan des massages.",
     "I am not a fan of massages.",
     [(703, "T'es gentil mais je suis pas fan des massages.")], ""),
    ("lea", "Laisse-moi éliminer toute cette tension.",
     "Let me eliminate all this tension.",
     [(706, "On va essayer d'éliminer la tension.")], ""),
    ("lea", "Respire calmement et détends-toi.",
     "Breathe calmly and relax.",
     [(706, "On va essayer d'éliminer la tension.")], ""),
    ("mathias", "Ah oui, c'est vraiment excellent.",
     "Oh yes, that is truly excellent.",
     [(714, "Ah, c'est bien."), (715, "C'est excellent.")], ""),
    ("lea", "Tu avais juste besoin de repos.",
     "You just needed some rest.",
     [(716, "C'est bien !")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Is everything going well, Mathias?' Noemie checks on her secret lover at his private apartment. "
     "The greeting tout va bien inquires about someone's general well-being."),
    (1, None,
     "'Can I come in for a moment?' She politely asks permission to cross the threshold. "
     "The modal verb peux expresses a courteous request."),
    (2, None,
     "'Of course, do come in.' Mathias warmly welcomes his assistant inside. "
     "The adverb donc adds gentle emphasis to the imperative entre."),
    (3, None,
     "'I would have tidied up if I had known.' He apologizes for the disorganized state of his flat. "
     "The past conditional aurais range combined with si j'avais su expresses regret about past circumstances."),
    (4, None,
     "'I have nothing to offer you.' Mathias laments his bare cupboards after moving out. "
     "The structure n'ai rien a followed by an infinitive indicates a lack of provisions."),
    (5, None,
     "'That is great news for Adjani!' Noemie rejoices over solving the major agency contract crisis. "
     "The feminine noun nouvelle means a piece of news."),
    (6, None,
     "'Yes, everything is well sorted out.' The senior agent confirms that the dispute with the star is resolved. "
     "The past participle regle means settled or resolved."),
    (7, None,
     "'I do not feel well.' Mathias admits that intense professional stress is taking a toll on his health. "
     "The reflexive expression se sentir bien describes physical well-being."),
    (8, None,
     "'Sit down in this armchair.' She gently directs him toward a comfortable seat. "
     "The reflexive imperative assieds-toi invites someone to sit down."),
    (9, None,
     "'I am not a fan of massages.' Mathias expresses initial reluctance about physical relaxation. "
     "The borrowed noun fan indicates enthusiasm for an activity."),
    (10, None,
     "'Let me eliminate all this tension.' Noemie begins massaging his stiff shoulders to relieve his knots. "
     "The imperative laisse-moi asks for permission to act."),
    (11, None,
     "'Breathe calmly and relax.' She instructs him to slow his breathing and let go of his worries. "
     "The reflexive imperative detends-toi tells someone to unwind."),
    (12, None,
     "'Oh yes, that is truly excellent.' Mathias sighs with deep relief as the soothing massage takes effect. "
     "The adverb vraiment emphasizes genuine appreciation."),
    (13, None,
     "'You just needed some rest.' Noemie lovingly observes the immediate benefits of stepping away from work. "
     "The imperfect phrase avais besoin de denotes an ongoing need."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "As the tension melts away under Noemie's touch, the bond between the two partners deepens outside the walls of ASK. "
    "Remember the useful French phrase for expressing regret about an unknown fact: si j'avais su."
)

CLOSING = ("lea", "Tu avais juste besoin de repos.")
