# Authoring module for dix-pour-cent s04e04 scene 10 (cues 836-860).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s04e04/scene-10.json

ID = "dix-pour-cent-s04e04-scene-10"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 10
TITLE = "Une mafia de nounous  (A Nanny Mafia)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 836-860. Élise visits Andréa's office and notices her extreme fatigue from bringing baby Flora to work. "
    "Élise offers maternal advice and promises to bypass impossible nanny waitlists by tapping into Paris's elite nanny network."
)

INTRO = (
    "After losing her daycare spot, Andrea Martel is exhausted from bringing baby Flora to the ASK agency every day. "
    "Rival agent Elise Formain steps into her office and observes her colleague's mounting distress. "
    "Rather than exploiting Andrea's weakness, Elise offers unexpected maternal advice and a surprising solution. "
    "Let's listen to their exchange in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("elise", "C'est quoi tout ce va-et-vient ici?",
     "What is all this coming and going here?",
     [(836, "C'est quoi tout ce va-et-vient ?")], "Élise asks about the hallway traffic"),
    ("lea", "Je cherche une nounou pour ma fille.",
     "I am looking for a nanny for my daughter.",
     [(832, "il me faut une nounou cette année")], "Andréa explains her search"),
    ("elise", "Tu amènes Flora au bureau depuis lundi.",
     "You bring Flora to the office since Monday.",
     [(840, "Ça fait une semaine que vous amenez votre fille")], "Élise observes the child"),
    ("lea", "Nous avons perdu notre place en crèche.",
     "We lost our place at daycare.",
     [(844, "Un malentendu avec la crèche")], "Andréa shares her childcare crisis"),
    ("elise", "Tu as l'air complètement épuisée, Andréa.",
     "You seem completely exhausted, Andrea.",
     [(841, "Tu as l'air… Complètement stressé.")], "Élise notes her burnout"),
    ("lea", "Les crèches demandent deux ans d'attente!",
     "Daycare centers ask two years of waiting!",
     [(830, "Septembre 2022 ?"), (845, "avant la conception")], "Andréa laments the waitlists"),
    ("elise", "Tu peux me parler en toute confiance.",
     "You can talk to me in full confidence.",
     [(842, "Tu peux me parler, tu sais.")], "Élise offers a sympathetic ear"),
    ("lea", "J'ai l'impression de tout faire mal.",
     "I feel like I do everything wrong.",
     [(857, "J'ai l'impression que tout ce que je fais est faux")], "Andréa confesses her guilt"),
    ("elise", "J'ai eu trois enfants toute seule.",
     "I had three children all alone.",
     [(850, "J'ai eu trois enfants de trois pères différents.")], "Élise shares her experience"),
    ("lea", "Comment fais-tu pour tout organiser?",
     "How do you manage to organize everything?",
     [(851, "donner des conseils")], "Andréa asks for guidance"),
    ("elise", "Pour rendre Flora heureuse, sois heureuse.",
     "To make Flora happy, be happy.",
     [(852, "si tu veux que ton enfant soit heureux,"), (853, "tu dois l'être toi-même.")], "Élise shares a golden rule"),
    ("lea", "J'ai juste besoin d'une bonne nounou.",
     "I just need a good nanny.",
     [(856, "Si j'avais quelqu'un pour s'occuper de Flora")], "Andréa returns to the practical issue"),
    ("elise", "Les nounous à Paris, c'est une mafia!",
     "Nannies in Paris are a mafia!",
     [(859, "Les nounous, c'est une mafia.")], "Élise describes the private market"),
    ("elise", "Laisse-moi faire, je connais du monde.",
     "Leave it to me, I know people.",
     [(858, "Tu veux que je te trouve une nounou ?"), (860, "Moi, oui.")], "Élise promises to help"),
]

WALK = [
    (0, None,
     "'What is all this coming and going here?' Elise asks about the steady stream of candidates outside Andrea's door. "
     "The expression 'va-et-vient' means coming and going."),
    (1, None,
     "'I am looking for a nanny for my daughter.' Andrea explains that she has been conducting interviews all morning. "
     "The feminine noun 'nounou' is a common informal term for nanny."),
    (2, None,
     "'You bring Flora to the office since Monday.' Elise points out that the baby has been sleeping by Andrea's desk. "
     "The verb 'amener' means to bring a person."),
    (3, None,
     "'We lost our place at daycare.' Andrea explains her sudden child care emergency. "
     "The feminine noun 'creche' refers to an infant daycare center."),
    (4, None,
     "'You seem completely exhausted, Andrea.' Elise recognizes the signs of maternal burnout. "
     "The adjective 'epuisee' means completely drained or exhausted."),
    (5, None,
     "'Daycare centers ask two years of waiting!' Andrea complains about absurd registration delays in Paris. "
     "The feminine noun 'creche' designates a daycare center."),
    (6, None,
     "'You can talk to me in full confidence.' Elise offers a rare moment of genuine vulnerability and support. "
     "The feminine noun 'confiance' means trust or confidence."),
    (7, None,
     "'I feel like I do everything wrong.' Andrea admits her deep feelings of maternal guilt and inadequacy. "
     "The noun 'impression' means feeling or impression."),
    (8, None,
     "'I had three children all alone.' Elise shares her experience raising children from three previous marriages. "
     "The irregular verb 'eu' is the past participle of avoir."),
    (9, None,
     "'How do you manage to organize everything?' Andrea asks for practical advice on balancing work and family. "
     "The verb 'organiser' means to organize or arrange."),
    (10, None,
     "'To make Flora happy, be happy.' Elise offers wise perspective on prioritizing personal well-being. "
     "The subjunctive 'sois' serves as an encouraging imperative."),
    (11, None,
     "'I just need a good nanny.' Andrea focuses on her immediate practical obstacle. "
     "The phrase 'avoir besoin de' expresses necessity."),
    (12, None,
     "'Nannies in Paris are a mafia!' Elise jokes about the hyper-competitive and secretive nanny market. "
     "The noun 'mafia' metaphorically denotes an exclusive syndicate."),
    (13, None,
     "'Leave it to me, I know people.' Elise promises to unlock her secret contact list to find the ideal caregiver. "
     "The idiom 'connaitre du monde' means to have connections."),
]

OUTRO = (
    "Grateful for Elise's surprising warmth and support, Andrea feels a glimmer of hope amidst her chaotic week. "
    "With the promise of an elite nanny on the horizon, the two rival agents discover an unexpected bond in motherhood. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("elise", "Je vais te trouver la meilleure nounou!")
