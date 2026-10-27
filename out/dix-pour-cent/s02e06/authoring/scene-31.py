# Authoring module for dix-pour-cent s02e06 scene 31 (cues 883-913).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-31.py --out out/dix-pour-cent/s02e06/scene-31.json

ID = "dix-pour-cent-s02e06-scene-31"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 31
TITLE = "Dans la piscine à Cannes  (In the Pool at Cannes)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 883-913. Season 2 finale. Andrea confesses to Gabriel that she is pregnant with Hicham's child. "
    "Hicham reveals his plan to acquire American agency UBA, and the team joyfully jumps into the pool together."
)

INTRO = (
    "Beside the illuminated swimming pool at Cannes, Andrea confides her biggest secret to Gabriel. "
    "When Hicham arrives with a vision for the agency's international future, the team seals their bond with a midnight leap. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Gabriel, je suis enceinte.", "Gabriel, I am pregnant.",
     [(883, "Je suis enceinte")], "Andrea makes a shocking confession to Gabriel"),
    ("lea", "C'est le bébé de Hicham.", "It is Hicham's baby.",
     [(884, "De Hicham")], ""),
    ("lea", "Et je ne sais pas quoi faire.", "And I don't know what to do.",
     [(885, "Et je sais pas quoi faire")], ""),
    ("gabriel", "C'est le truc dingue avec toi.", "That is the crazy thing about you.",
     [(886, "C'est ça le truc dingue avec toi")], ""),
    ("gabriel", "Tu as toujours un truc en plus.", "You always have something extra.",
     [(887, "T'as toujours ce petit quelque chose en plus")], ""),
    ("gabriel", "Tu es ma meilleure amie, Andréa.", "You are my best friend, Andrea.",
     [(890, "Tu es mon amie")], ""),
    ("lea", "Merci d'être là pour moi.", "Thank you for being there for me.",
     [(890, "Tu es mon amie")], ""),
    ("hicham", "Je veux racheter l'agence américaine UBA.", "I want to buy the American agency UBA.",
     [(895, "Je pensais peut-être la racheter")], "Hicham joins them by the pool"),
    ("hicham", "Une ouverture sur le marché international.", "An opening into the international market.",
     [(896, "Ouais, comme une ouverture sur le marché international")], "") ,
    ("gabriel", "C'est un projet très ambitieux!", "It is a very ambitious project!",
     [(897, "C'est bien d'être ambitieux, non")], ""),
    ("hicham", "J'aurai besoin de votre aide à tous.", "I will need help from all of you.",
     [(902, "Mais j'aurai besoin de votre aide")], ""),
    ("lea", "Nous formons une vraie équipe maintenant.", "We make a real team now.",
     [(905, "Vous n'avez pas tort")], ""),
    ("hicham", "Alors, tout le monde dans la piscine!", "So, everyone into the pool!",
     [(909, "Hé, les gars, c'est pas encore fini")], ""),
    ("gabriel", "On reste toujours soudés, d'accord?", "We always stick together, right?",
     [(911, "On reste soudés, d'accord")], ""),
    ("lea", "Oui, nous restons toujours ensemble!", "Yes, we are always staying together!",
     [(911, "On reste soudés, d'accord")], ""),
]

OPENER = "Let's walk through this unforgettable poolside season finale step by step."

WALK = [
    (0, None,
     "'Gabriel, I am pregnant.' Andrea reveals the secret that has weighed on her all weekend."),
    (1, None,
     "'It is Hicham's baby.' Andrea drops the second stunning revelation regarding paternity."),
    (2, None,
     "'And I don't know what to do.' Andrea openly shares her profound confusion and vulnerability."),
    (3, None,
     "'That is the crazy thing about you.' Gabriel reacts with disbelief mixed with deep affection."),
    (4, None,
     "'You always have something extra.' Gabriel acknowledges her uncanny ability to shock everyone."),
    (5, None,
     "'You are my best friend, Andrea.' Gabriel reaffirms their unbreakable bond across all crises."),
    (6, None,
     "'Thank you for being there for me.' Andrea expresses heartfelt gratitude for his loyalty."),
    (7, None,
     "'I want to buy the American agency UBA.' Hicham unveils his audacious expansion plan."),
    (8, None,
     "'An opening into the international market.' Hicham outlines a bold global vision for ASK."),
    (9, None,
     "'It is a very ambitious project!' Gabriel admires the bold scale of the endeavor."),
    (10, None,
     "'I will need help from all of you.' Hicham genuinely asks for the agents' professional partnership."),
    (11, None,
     "'We make a real team now.' Andrea embraces their collective strength heading into the future."),
    (12, None,
     "'So, everyone into the pool!' Hicham playfully calls for a celebratory midnight plunge."),
    (13, None,
     "'We always stick together, right?' Gabriel reminds everyone of their shared solidarity."),
    (14, None,
     "'Yes, we are always staying together!' Andrea seals the family pact as they leap into the water."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "As Andrea shares her life-changing secret with Gabriel, Hicham reveals his grand international ambitions before everyone dives into the pool together."
CLOSING = ("gabriel", "On reste toujours soudés, d'accord?")
