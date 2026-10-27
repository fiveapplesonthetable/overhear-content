# Authoring module for dix-pour-cent s04e04 scene 08 (cues 492-519).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-08.py --out overhear-content/out/dix-pour-cent/s04e04/scene-08.json

ID = "dix-pour-cent-s04e04-scene-08"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 8
TITLE = "Panique à la photocopieuse  (Panic at the Photocopier)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 492-519. Gabriel confides to Andréa his deep anxiety regarding Sandrine Kiberlain's decision to drop her film role for comedy. "
    "Andréa attempts to reassure him while describing the hectic life of a solo parent, only to realize with a gasp that she left baby Flora unattended by the copier."
)

INTRO = (
    "In the quiet hallway at ASK, Gabriel Sarda confides his panic to Andrea Martel. "
    "His star client Sandrine Kiberlain is jeopardizing a major movie role to pursue a risky career in comedy. "
    "Andrea tries to soothe Gabriel while reflecting on her own stressful routine as a working mother, with sudden consequences. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Tout va très mal avec Sandrine Kiberlain.",
     "Everything goes very badly with Sandrine Kiberlain.",
     [(494, "Juste un petit contretemps sur le film")], "Gabriel shares his distress"),
    ("lea", "Qu'est-ce qui se passe sur son tournage?",
     "What is happening on her shoot?",
     [(496, "Qu'est-ce qui se passe ?")], "Andréa asks for details"),
    ("gabriel", "Elle veut abandonner le film de Thompson.",
     "She wants to abandon Thompson's film.",
     [(496, "Sandrine veut se retirer ?")], "Gabriel reveals the crisis"),
    ("lea", "Ne panique pas, tu vas arranger ça.",
     "Do not panic, you will fix that.",
     [(495, "je vais arranger ça"), (498, "T'inquiète pas. Respire.")], "Andréa offers calm reassurance"),
    ("gabriel", "Elle veut faire du stand-up maintenant!",
     "She wants to do stand-up now!",
     [(499, "je suis un peu à cran")], "Gabriel explains the bizarre turn"),
    ("lea", "Respire Gabriel, tout va bien se passer.",
     "Breathe Gabriel, everything will go well.",
     [(498, "Respire")], "Andréa tells him to take a breath"),
    ("gabriel", "Et toi, comment se passe ta vie?",
     "And you, how is your life going?",
     [(500, "Et, tu sais, la vie ?")], "Gabriel asks about her situation"),
    ("lea", "Je gère ma vie toute seule.",
     "I manage my life all alone.",
     [(515, "Comme un parent solo")], "Andréa describes her daily grind"),
    ("gabriel", "Ce n'est pas trop dur avec Flora?",
     "Is it not too hard with Flora?",
     [(517, "Flora semble bien s'adapter")], "Gabriel sympathizes with her duties"),
    ("lea", "C'est comme faire une randonnée en tongs!",
     "It is like hiking in flip-flops!",
     [(516, "C'est comme randonner en tongs")], "Andréa makes a colorful comparison"),
    ("gabriel", "Mais le bébé va bien ici?",
     "But the baby is doing well here?",
     [(517, "Flora semble bien s'adapter")], "Gabriel checks on the infant"),
    ("lea", "Oui, elle est très calme aujourd'hui.",
     "Yes, she is very calm today.",
     [(517, "Mais je m'en sors")], "Andréa praises her quiet daughter"),
    ("lea", "Attends, où est passée ma fille?",
     "Wait, where did my daughter go?",
     [(518, "Qu'est-ce qu'il y a ?")], "Andréa pauses in sudden worry"),
    ("lea", "Merde, je l'ai oubliée à la photocopieuse!",
     "Damn, I forgot her at the photocopier!",
     [(518, "Je l'ai oubliée à la photocopieuse !"), (519, "Merde !")], "Andréa panics and dashes away"),
]

WALK = [
    (0, None,
     "'Everything goes very badly with Sandrine Kiberlain.' Gabriel shares his mounting stress regarding his unpredictable star client. "
     "The adverb 'mal' means badly."),
    (1, None,
     "'What is happening on her shoot?' Andrea inquires about the production problems. "
     "The pronominal verb 'se passer' means to happen or take place."),
    (2, None,
     "'She wants to abandon Thompson's film.' Gabriel reveals that Sandrine plans to walk away from the prestigious project. "
     "The verb 'abandonner' means to leave or abandon."),
    (3, None,
     "'Do not panic, you will fix that.' Andrea encourages her distressed partner to stay grounded. "
     "The near-future phrase 'vas arranger' expresses positive expectation."),
    (4, None,
     "'She wants to do stand-up now!' Gabriel explains that the dramatic actress has suddenly fallen in love with comedy. "
     "The adverb 'maintenant' means now."),
    (5, None,
     "'Breathe Gabriel, everything will go well.' Andrea urges him to regulate his breathing and composure. "
     "The imperative 'respire' comes from the verb 'respirer'."),
    (6, None,
     "'And you, how is your life going?' Gabriel changes the subject to ask about Andrea's domestic situation. "
     "The interrogative 'comment' asks how."),
    (7, None,
     "'I manage my life all alone.' Andrea explains her exhausting daily schedule since Colette's departure. "
     "The adjective 'seule' describes living independently."),
    (8, None,
     "'Is it not too hard with Flora?' Gabriel gently asks about Andrea's infant daughter. "
     "The adjective 'dur' means difficult or hard."),
    (9, None,
     "'It is like hiking in flip-flops!' Andrea humorously summarizes the struggle of balancing baby care and agency work. "
     "The noun 'randonnee' designates a hike."),
    (10, None,
     "'But the baby is doing well here?' Gabriel observes that the child seems surprisingly quiet at the office. "
     "The adverb 'bien' means well."),
    (11, None,
     "'Yes, she is very calm today.' Andrea proudly notes that her baby has been well-behaved. "
     "The adjective 'calme' describes peaceful behavior."),
    (12, None,
     "'Wait, where did my daughter go?' Andrea suddenly stops in her tracks with rising unease. "
     "The past participle 'passee' indicates disappearance."),
    (13, None,
     "'Damn, I forgot her at the photocopier!' Andrea rushes frantically down the corridor to retrieve her child. "
     "The feminine noun 'photocopieuse' refers to a copying machine."),
]

OUTRO = (
    "Startled by her own distraction, Andrea sprints across the office to rescue baby Flora from the copy room. "
    "Gabriel watches in amazement as his fellow agent juggles career crises and motherhood in the chaotic agency halls. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Flora dort tranquillement à côté du papier!")
