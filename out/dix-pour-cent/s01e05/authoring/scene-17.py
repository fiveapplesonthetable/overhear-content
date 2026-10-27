ID = "dix-pour-cent-s01e05-scene-17"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 17
TITLE = "Surprise dans la chambre seize  (Surprise in Room Sixteen)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "colette": "Colette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"

INTRO = (
    "Back at the country hotel, Gabriel teases Andréa that the receptionist has a crush on her "
    "before agreeing to meet her for dinner in fifteen minutes. As she walks to Room Sixteen, "
    "Andréa calls Camille in Paris for her messages and wishes her a happy birthday. When she opens "
    "her hotel room door, she finds Colette Brancillon waiting inside. "
    "Let's listen to the scene in French first; don't worry about catching every word."
)

STORY = [
    ("colette", "Surprise! Je vérifie les notes de frais.",
     "What a surprise! I'm checking the expense reports.",
     [(303, "Surprise"), (305, "Je vérifie les notes de frais")], ""),
    ("lea", "Comment tu es entrée dans ma chambre? Ils t'ont laissé entrer?",
     "How did you get into my room? They let you in?",
     [(304, "comment"), (304, "dans ma chambre"), (306, "Ils t'ont laissé entrer")],
     "cue 304 expletive removed and 't'es entré' written in standard feminine 'tu es entrée'"),
    ("colette", "Oui, comme tu vois. Après avoir insisté.",
     "Yes, as you can see. After insisting.",
     [(306, "Oui, comme tu vois"), (307, "Après avoir insisté")], ""),
    ("lea", "Enfin, je travaille. Des trucs à régler pour le tournage.",
     "Well, I'm working. Things to sort out for the shoot.",
     [(309, "Enfin, je travaille"), (310, "Des trucs à régler pour le tournage")], ""),
    ("colette", "Dîner avec Gabriel?",
     "Dinner with Gabriel?",
     [(312, "Dîner avec Gabriel")], ""),
    ("lea", "Oui, c'est professionnel!",
     "Yes, it's for work!",
     [(312, "Oui, c'est professionnel")], ""),
    ("colette", "Je croyais... Tu n'es pas contente de me voir?",
     "I thought... You aren't happy to see me?",
     [(313, "Je croyais"), (313, "Tu n'es pas contente de me voir")], ""),
    ("lea", "Tu as de la chance que ce ne soit pas le coccyx. C'est horrible.",
     "You're lucky it isn't the tailbone. That's horrible.",
     [(325, "de la chance que ce"), (325, "pas le coccyx. C'est horrible")],
     "spoken 'T'as' and dropped 'ne' restored to standard French"),
    ("lea", "Tu dois te balader avec un coussin pour t'asseoir.",
     "You have to walk around with a cushion to sit on.",
     [(327, "Tu dois te balader avec un coussin pour t'asseoir")], ""),
    ("lea", "Tes jolies petites fesses ont amorti le choc.",
     "Your pretty little backside cushioned the shock.",
     [(328, "Tes jolies petites fesses ont amorti le choc")], ""),
    ("colette", "Merci, jolies petites fesses!",
     "Thank you, pretty little backside!",
     [(329, "Merci, jolies petites fesses")], ""),
    ("gabriel", "C'est Gabriel, tu viens?",
     "It's Gabriel, are you coming?",
     [(331, "C'est Gabriel, tu viens")], ""),
    ("lea", "J'arrive. Je dois y aller.",
     "I'm coming. I have to go.",
     [(332, "J'arrive"), (333, "Je dois y aller")], ""),
    ("colette", "Reviens vite.",
     "Come back soon.",
     [(333, "Reviens vite")], ""),
    ("lea", "Je te le promets. Attends-moi.",
     "I promise you. Wait for me.",
     [(334, "Je te le promets. Attends-moi")], ""),
    ("colette", "Je ne peux pas vraiment me sauver en courant!",
     "I can't really run away!",
     [(335, "peux pas vraiment me sauver en courant")],
     "negation particle restored"),
]

OPENER = "Let's go through it slowly. Andréa opens the door to Room Sixteen and sees Colette on the bed."

WALK = [
    (0, "Surprise!",
     "'What a surprise!' Same spelling as in English, pronounced the French way."),
    (0, "Je vérifie les notes de frais.",
     "'I'm checking the expense reports.' Literally 'notes of expenses': Colette is teasing Andréa about her job as a tax auditor."),
    (1, "Comment tu es entrée dans ma chambre?",
     "'How did you get into my room?' Literally 'how did you enter in my room'."),
    (1, "Ils t'ont laissé entrer?",
     "'They let you in?' Literally 'they let you enter'."),
    (2, "Oui, comme tu vois.",
     "'Yes, as you can see.' Literally 'as you see', a very natural everyday reply."),
    (2, "Après avoir insisté.",
     "'After insisting.' Literally 'after having insisted'."),
    (3, None,
     "'Well, I'm working. Things to sort out for the shoot.' The casual word for 'things' or 'stuff' is very common in spoken French."),
    (4, None,
     "'Dinner with Gabriel?' Colette spots Andréa's notes on the table."),
    (5, None,
     "'Yes, it's for work!' Literally 'it is professional'."),
    (6, None,
     "'I thought... You aren't happy to see me?' Before Andréa can reassure her, Colette slips in the bathroom and lands hard on her backside. Meanwhile in Paris, Camille phones her mother to sign an online petition to save Ryan's character. Back at the hotel, Andréa tends to Colette."),
    (7, None,
     "'You're lucky it isn't the tailbone. That's horrible.' Literally 'you have luck that it is not the coccyx'."),
    (8, None,
     "'You have to walk around with a cushion to sit on.' The reflexive verb here is an informal way to say 'stroll' or 'walk around with'."),
    (9, None,
     "'Your pretty little backside cushioned the shock.' The verb at the end means 'absorbed' or 'cushioned'."),
    (10, None,
     "'Thank you, pretty little backside!' Colette laughs despite the pain."),
    (11, None,
     "'It's Gabriel, are you coming?' Gabriel knocks on the hotel room door."),
    (12, "J'arrive.",
     "'I'm coming.' Literally 'I arrive'—the standard French reply when someone calls for you."),
    (12, "Je dois y aller.",
     "'I have to go.' Literally 'I must go there'."),
    (13, None,
     "'Come back soon.' Literally 'come back quickly' to the room."),
    (14, None,
     "'I promise you. Wait for me.' The little words before the verb mean 'to you it'."),
    (15, None,
     "'I can't really run away!' Literally 'save myself by running'."),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = (
    "As Andréa steps into the hallway to meet Gabriel for dinner, she smiles to herself and admits "
    "she has really grown to love this tax audit. See you in the next scene."
)
CLOSING = ("lea", "J'ai vraiment fini par adorer ce contrôle fiscal!")
