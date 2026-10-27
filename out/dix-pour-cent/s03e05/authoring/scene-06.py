# Authoring module for dix-pour-cent s03e05 scene 06 (cues 120-151).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-06.py --out out/dix-pour-cent/s03e05/scene-06.json

ID = "dix-pour-cent-s03e05-scene-06"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 6
TITLE = "Garder Flora  (Watching Flora)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 120-151. Andrea begs Colette to watch their newborn daughter Flora so she can "
               "rush to Beatrice Dalle's troubled movie set, but Colette has her own work commitments. Adapted for A1 French.")

INTRO = ("At their Paris apartment, Andrea Martel is caring for newborn Flora while worrying about star client Beatrice Dalle. "
         "Andrea tries to convince Colette to take over babysitting for the afternoon so she can visit the film set. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Je n'ai rien mangé de la matinée.",
     "I have not eaten anything all morning.",
     [(121, "J'ai rien bouffé de la matinée")], "Andrea expresses her physical exhaustion"),
    ("lea", "Tu pourrais garder Flora cet après-midi?",
     "Could you watch Flora this afternoon?",
     [(122, "tu pourrais pas garder Flora, cet après-midi ?")], "Andrea asks for urgent babysitting"),
    ("colette", "Pourquoi me demandes-tu ça maintenant?",
     "Why do you ask me that now?",
     [(123, "Pourquoi ?")], "Colette is caught off guard"),
    ("lea", "Béatrice tourne avec un réalisateur très compliqué.",
     "Beatrice is shooting with a very difficult director.",
     [(124, "elle tourne avec un réel hyper compliqué")], "Andrea explains the client emergency"),
    ("lea", "J'ai très peur que ça dégénère là-bas.",
     "I am very afraid things will degenerate there.",
     [(125, "j'ai très peur que ça dégénère")], "Andrea fears an on-set crisis"),
    ("colette", "Je suis désolée, mais j'ai une réunion importante.",
     "I am sorry, but I have an important meeting.",
     [(126, "j'ai une réunion hyper importante")], "Colette cites her professional obligations"),
    ("lea", "Je vais devoir trouver quelqu'un d'autre.",
     "I will have to find someone else.",
     [(128, "je vais trouver quelqu'un")], "Andrea searches for alternative childcare"),
    ("colette", "On ne laisse pas la petite avec un inconnu!",
     "We do not leave the baby with a stranger!",
     [(130, "On va pas laisser la petite comme ça")], "Colette strongly opposes outside sitters"),
    ("lea", "La vieille voisine pourrait s'en occuper.",
     "The old neighbor could look after her.",
     [(131, "la voisine, elle l'a vue")], "Andrea suggests the lady next door"),
    ("colette", "C'est n'importe quoi, Andréa!",
     "That makes no sense, Andrea!",
     [(136, "C'est n'importe quoi")], "Colette rejects the idea instantly"),
    ("lea", "Je ne peux plus rester enfermée vingt-quatre heures!",
     "I cannot stay locked up twenty-four hours!",
     [(138, "j'en peux plus d'être assignée à résidence")], "Andrea vents her cabin fever"),
    ("colette", "Un bébé a besoin d'être avec sa maman.",
     "A baby needs to be with her mother.",
     [(140, "un bébé a besoin d'être avec sa maman")], "Colette highlights maternal bonding"),
    ("lea", "Ce n'est pas humain d'être seule toujours!",
     "It is not human to always be alone!",
     [(149, "c'est pas humain")], "Andrea pushes back against maternal isolation"),
]

OPENER = "Let's examine how Andrea and Colette negotiate parenting and career demands line by line."

WALK = [
    (0, None,
     "'I have not eaten anything all morning.' Andrea complains about being exhausted from baby care."),
    (1, None,
     "'Could you watch Flora this afternoon?' Andrea asks Colette to take over looking after their infant daughter."),
    (2, None,
     "'Why do you ask me that now?' Colette is surprised by the sudden last-minute request."),
    (3, None,
     "'Beatrice is shooting with a very difficult director.' Andrea explains that her movie star client needs urgent assistance on set."),
    (4, None,
     "'I am very afraid things will degenerate there.' Andrea worries about a blowup on the movie set."),
    (5, None,
     "'I am sorry, but I have an important meeting.' Colette points out her own busy work schedule."),
    (6, None,
     "'I will have to find someone else.' Andrea refuses to abandon her professional responsibilities."),
    (7, None,
     "'We do not leave the baby with a stranger!' Colette objects to hiring an unknown babysitter."),
    (8, None,
     "'The old neighbor could look after her.' Andrea proposes asking the woman next door for help."),
    (9, None,
     "'That makes no sense, Andrea!' Colette dismisses the idea of trusting a strange neighbor."),
    (10, None,
     "'I cannot stay locked up twenty-four hours!' Andrea expresses her frustration with maternity isolation."),
    (11, None,
     "'A baby needs to be with her mother.' Colette reminds Andrea of maternal duties during the early months."),
    (12, None,
     "'It is not human to always be alone!' Andrea argues that complete isolation is unhealthy for parents."),
]

TRANSITION = "Now let's listen to the domestic conversation once more to solidify your understanding."

OUTRO = ("Andrea and Colette clash over balancing maternal responsibilities with high-stakes agency emergencies. "
         "Let's review the key vocabulary from this parenting and workplace discussion.")

CLOSING = ("colette", "Un bébé a besoin d'être avec sa maman.")
