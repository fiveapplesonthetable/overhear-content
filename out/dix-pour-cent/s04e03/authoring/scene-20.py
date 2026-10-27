# Authoring module for dix-pour-cent s04e03 scene 20 (cues 989-993).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-20.py --out out/dix-pour-cent/s04e03/scene-20.json

ID = "dix-pour-cent-s04e03-scene-20"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 20
TITLE = "Mon agent  (My Agent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 989-993. In his quiet hotel suite after an exhausting shoot, Jose Garcia begins to call Andrea his love "
    "before quickly correcting himself to 'my agent'. Andrea laughs off the slip of the tongue as room service knocks at the door."
)

INTRO = (
    "In his quiet hotel suite after an exhausting shoot, Jose Garcia begins to call Andrea his love before quickly correcting himself to 'my agent'. "
    "Andrea laughs off the slip of the tongue as room service knocks at the door. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("jose", "Allô, mon am-- Allô, mon agent.",
     "Hello, my lo-- Hello, my agent.",
     [(989, "Allô, mo--"), (991, "Mon agent")], "Caught himself on the phone slip"),
    ("lea", "Tu as failli dire mon amour!",
     "You almost said my love!",
     [(992, "Ça commence pareil")], "Teased him about his near slip"),
    ("jose", "Ça commence par la même lettre.",
     "It starts with the same letter.",
     [(992, "Ça commence pareil")], "Offered an amusing playful excuse"),
    ("lea", "Tu es vraiment incorrigible ce soir.",
     "You are really incorrigible tonight.",
     [(992, "Ça commence")], "Pointed out his habitual charm"),
    ("jose", "La journée de tournage était épuisante.",
     "The day of filming was exhausting.",
     [(993, "Entrez")], "Sighed about the heavy shoot schedule"),
    ("lea", "Nous avons évité une vraie catastrophe.",
     "We avoided a real catastrophe.",
     [(993, "Entrez")], "Recalled the averted set disaster"),
    ("jose", "Grâce à toi, tout s'est arrangé.",
     "Thanks to you, everything worked out.",
     [(993, "Entrez")], "Credited her with fixing the problem"),
    ("lea", "C'est mon rôle d'agent protecteur.",
     "It is my role as a protective agent.",
     [(991, "Mon agent")], "Affirmed her protective duty"),
    ("jose", "On frappe à la porte maintenant.",
     "Someone is knocking on the door now.",
     [(993, "Entrez")], "Heard a knock at the hotel door"),
    ("lea", "C'est sans doute le room service.",
     "It is probably room service.",
     [(993, "Entrez")], "Anticipated the arrival of their food"),
    ("jose", "Entrez, s'il vous plaît!",
     "Come in, please!",
     [(993, "Entrez")], "Called out to let the server enter"),
    ("lea", "Installez le plateau sur la table.",
     "Set the tray on the table.",
     [(993, "Entrez")], "Directed the hotel attendant"),
    ("jose", "Merci beaucoup pour ce service rapide.",
     "Thank you very much for this quick service.",
     [(993, "Excusez-moi")], "Thanked the attendant politely"),
    ("lea", "Nous allons enfin pouvoir décompresser ensemble.",
     "We are finally going to be able to unwind together.",
     [(993, "Entrez")], "Welcomed the moment of relaxation")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'Hello, my lo-- Hello, my agent.' Jose catches himself on the phone in his suite. "
     "The slip of the tongue highlights their affectionate bond."),
    (1, None,
     "'You almost said my love!' Andrea teases him with a knowing smile. "
     "The verb faillir with infinitive marks a near slip."),
    (2, None,
     "'It starts with the same letter.' Jose laughs off the mistake playfully. "
     "The prepositional phrase offers an amusing excuse."),
    (3, None,
     "'You are really incorrigible tonight.' Andrea relaxes on the sofa. "
     "The expressive adjective points out his unrepentant charm."),
    (4, None,
     "'The day of filming was exhausting.' Jose leans back in his chair. "
     "The descriptive noun phrase recalls the demanding set."),
    (5, None,
     "'We avoided a real catastrophe.' Andrea reflects on the near-disaster on set. "
     "The compound past marks the successful save."),
    (6, None,
     "'Thanks to you, everything worked out.' Jose credits her skill as an agent. "
     "The idiomatic phrase honors her decisive intervention."),
    (7, None,
     "'It is my role as a protective agent.' Andrea claims her duty with pride. "
     "The descriptive adjective defines her professional devotion."),
    (8, None,
     "'Someone is knocking on the door now.' Jose turns toward the foyer. "
     "The impersonal pronoun on announces an arrival."),
    (9, None,
     "'It is probably room service.' Andrea stands up to answer. "
     "The adverbial expression anticipates their ordered dinner."),
    (10, None,
     "'Come in, please!' Jose calls out cheerfully toward the hall. "
     "The polite imperative welcomes the hotel staff."),
    (11, None,
     "'Set the tray on the table.' Andrea guides the attendant into the room. "
     "The imperative verb directs the food service."),
    (12, None,
     "'Thank you very much for this quick service.' Jose tips the server generously. "
     "The polite formula acknowledges prompt hospitality."),
    (13, None,
     "'We are finally going to be able to unwind together.' Andrea breathes a sigh of relief. "
     "The modal verbs convey welcome relaxation.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Jose and Andrea settle into the hotel room, grateful to have survived a chaotic day of filming."
CLOSING = ("lea", "Nous allons enfin pouvoir décompresser ensemble.")
