# Authoring module for dix-pour-cent s02e05 scene 22 (cues 675-696).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-22.py --out out/dix-pour-cent/s02e05/scene-22.json

ID = "dix-pour-cent-s02e05-scene-22"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 22
TITLE = "Refuser la promotion  (Turning Down the Promotion)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo"}
LABELS = {"lea": "Camille", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 675-696. Camille tells Hicham in his office that she wants to refuse the promotion to junior agent. "
    "Unwilling to accept her hesitation, Hicham gives her a blunt ultimatum to take the job or leave ASK."
)

INTRO = (
    "In Hicham's sleek office, Camille arrives determined to decline the offer of becoming a junior agent. "
    "Hoping to remain Andrea's assistant, Camille faces a ruthless ultimatum from the ambitious agency owner. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Je refuse le poste d'agent junior.",
     "I refuse the junior agent job.",
     [(675, "Je ne prends pas le poste d'agent junior.")], ""),
    ("hicham", "Répète un peu, je n'ai pas compris.",
     "Say that again, I did not understand.",
     [(676, "Répète, je n'ai pas compris.")], ""),
    ("lea", "Je refuse cette belle promotion.",
     "I refuse this fine promotion.",
     [(679, "Je refuse la promotion.")], ""),
    ("lea", "Je préfère rester assistante pour l'instant.",
     "I prefer to remain an assistant for now.",
     [(681, "de continuer à être l'assistante d'Andréa pour l'instant.")], ""),
    ("hicham", "Tu réalises vraiment ce que tu dis?",
     "Do you truly realize what you are saying?",
     [(683, "Tu réalises ce que tu dis ?")], ""),
    ("lea", "Je sais exactement où est ma place.",
     "I know exactly where my place is.",
     [(686, "Je sais où est ma place.")], ""),
    ("hicham", "Non, tu ne sais rien du tout.",
     "No, you know nothing at all.",
     [(687, "Non, visiblement pas.")], ""),
    ("lea", "Qu'est-ce que tu veux dire?",
     "What do you mean?",
     [(688, "Qu'est-ce que tu veux dire ?")], ""),
    ("hicham", "Une agence évolue comme une rivière.",
     "An agency evolves like a river.",
     [(691, "Une entreprise, c'est comme une rivière,")], ""),
    ("hicham", "On ne revient jamais en arrière.",
     "We never go backward.",
     [(689, "Il n'y a plus d'\"comme avant\"."), (692, "on ne se baigne jamais deux fois dans la même.")], ""),
    ("lea", "Mais j'adore mon travail actuel.",
     "But I love my current work.",
     [(680, "Je sens que c'est mieux pour moi")], ""),
    ("hicham", "Tu as le choix, ma chérie.",
     "You have the choice, my dear.",
     [(695, "Prends le poste, ma chérie,")], ""),
    ("hicham", "Prends ce poste ou prends la porte!",
     "Take this job or take the door!",
     [(695, "Prends le poste, ma chérie, ou prends la porte.")], ""),
    ("lea", "C'est un chantage inacceptable, Hicham.",
     "That is unacceptable blackmail, Hicham.",
     [(695, "Prends le poste, ma chérie, ou prends la porte.")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'I refuse the junior agent job.' Camille shocks Hicham by rejecting the promotion to agent. "
     "The verb refuse indicates a deliberate decision to decline an offer."),
    (1, None,
     "'Say that again, I did not understand.' Hicham asks her to repeat her unexpected declaration. "
     "The imperative repete commands someone to say something again."),
    (2, None,
     "'I refuse this fine promotion.' She reiterates her decision despite the status of the offer. "
     "The demonstrative cette agrees with the feminine noun promotion."),
    (3, None,
     "'I prefer to remain an assistant for now.' Camille values her current apprenticeship under Andrea. "
     "The time locution pour l'instant means for the time being or for now."),
    (4, None,
     "'Do you truly realize what you are saying?' Hicham questions her grasp of agency career stakes. "
     "The relative pronoun ce que means what or that which."),
    (5, None,
     "'I know exactly where my place is.' She asserts her comfort and confidence in her current role. "
     "The adverb exactement expresses precision."),
    (6, None,
     "'No, you know nothing at all.' Hicham dismisses her perspective as naive and shortsighted. "
     "The negation ne ... rien du tout means nothing at all."),
    (7, None,
     "'What do you mean?' Camille asks for clarification on his harsh assessment. "
     "The phrase vouloir dire means to mean or signify."),
    (8, None,
     "'An agency evolves like a river.' The boss uses a philosophical metaphor about corporate change. "
     "The comparison comme une riviere illustrates irreversible forward flow."),
    (9, None,
     "'We never go backward.' He insists that career steps cannot simply be reversed. "
     "The idiom en arriere means backward or in reverse."),
    (10, None,
     "'But I love my current work.' Camille pleads her passion for her daily tasks. "
     "The adjective actuel means current or present."),
    (11, None,
     "'You have the choice, my dear.' Hicham condescendingly frames the situation as an ultimatum. "
     "The affectionate term ma cherie sounds patronizing in this context."),
    (12, None,
     "'Take this job or take the door!' He delivers a ruthless career ultimatum to the young assistant. "
     "The idiom prendre la porte means to leave or be fired."),
    (13, None,
     "'That is unacceptable blackmail, Hicham.' Camille pushes back against the coercive pressure. "
     "The adjective inacceptable describes something that cannot be tolerated."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Stunned by Hicham's brutal ultimatum, Camille realizes she cannot easily step backward in her agency career. "
    "Remember the colloquial French idiom for leaving or being dismissed: prendre la porte."
)

CLOSING = ("hicham", "Prends ce poste ou prends la porte!")
