# Authoring module for dix-pour-cent s02e02 scene 17 (cues 575-623).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-17.py --out out/dix-pour-cent/s02e02/scene-17.json

ID = "dix-pour-cent-s02e02-scene-17"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 17
TITLE = "Une proposition délicate  (A Delicate Proposal)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 575-623. Gabriel and Sofia discuss a promising comedy script. Worried about mixing their romantic relationship "
    "with work, Gabriel delicately tests whether Sofia would consider being represented by Camille."
)

INTRO = (
    "In the quiet corners of ASK, Gabriel and his girlfriend, actress Sofia Leprince, discuss "
    "a fantastic new film script discovered by Camille. Gabriel tentatively raises a delicate "
    "question about separating their romance from their professional careers. Listen to the scene in French first."
)

STORY = [
    ("gabriel", "On passe à l'attaque avec Luchini.",
     "We're going on the attack with Luchini.",
     [(575, "On passe à l'attaque avec Luchini")], ""),
    ("lea", "Ce serait incroyable! C'est bien?",
     "That would be amazing! Is it good?",
     [(576, "Ce serait incroyable"), (578, "C'est bien")], ""),
    ("gabriel", "Vraiment drôle, avec de très beaux rôles.",
     "Really funny, with very fine roles.",
     [(579, "Vraiment drôle"), (580, "Avec plus de rôles")], ""),
    ("lea", "C'est Camille qui pensait que c'était bien pour moi.",
     "It was Camille who thought it was good for me.",
     [(583, "C'est Camille qui pensait que c'était bien pour moi")], ""),
    ("lea", "C'est tellement gentil de sa part. Quelle fille adorable.",
     "It's so kind of her. What an adorable girl.",
     [(584, "C'est tellement gentil de sa part. Quelle fille adorable")], ""),
    ("lea", "Elle ferait une excellente agente.",
     "She would make an excellent agent.",
     [(585, "Elle ferait une excellente agente")], ""),
    ("gabriel", "Alors... tu la laisserais te représenter?",
     "So... would you let her represent you?",
     [(589, "Alors... tu la laisserais te représenter")], ""),
    ("lea", "Tu es fou? Tu es mon agent.",
     "Are you crazy? You are my agent.",
     [(590, "T'es fou ? T'es mon agent")], "Restored 'tu es'"),
    ("gabriel", "Hypothétiquement parlant, je veux dire.",
     "Hypothetically speaking, I mean.",
     [(591, "Hypothétiquement parlant, je veux dire")], ""),
    ("lea", "Tu ne veux plus être mon agent?",
     "You don't want to be my agent anymore?",
     [(592, "Tu veux plus être mon agent")], "Restored 'ne'"),
    ("gabriel", "Bien sûr que si! C'est juste que travailler ensemble, c'est parfois difficile.",
     "Of course I do! It's just that working together is sometimes difficult.",
     [(592, "Bien sûr que si"), (593, "C'est juste que travailler ensemble, c'est parfois difficile")], ""),
    ("gabriel", "Ils disent que c'est dur de tout mélanger.",
     "They say it's hard to mix everything up.",
     [(598, "Ils disent que c'est dur de tout mélanger")], ""),
    ("gabriel", "Ça peut te faire du mal.",
     "It can hurt you.",
     [(599, "Ça peut te faire du mal")], ""),
    ("lea", "Non, je ne changerais jamais d'agent.",
     "No, I would never change agents.",
     [(600, "Non, je ne changerais jamais d'agent")], ""),
    ("lea", "Tu m'as trouvée, tu me connais, défends-moi!",
     "You found me, you know me, defend me!",
     [(601, "Tu m'as trouvée, tu me connais, défends-moi")], ""),
    ("lea", "Je ne veux personne d'autre que toi.",
     "I don't want anyone else but you.",
     [(602, "Je ne veux personne d'autre que toi")], ""),
]

OPENER = "Let's explore this tender and complicated conversation line by line."

WALK = [
    (0, None,
     "'We're going on the attack with Luchini.' Gabriel shares agency strategy. "
     "The idiom passer à l'attaque means to launch an offensive or make a move."),
    (1, None,
     "'That would be amazing! Is it good?' Sofia is enthusiastic about the project. "
     "The conditional form ce serait expresses wonder."),
    (2, None,
     "'Really funny, with very fine roles.' Gabriel praises the new comedy screenplay. "
     "The adverb vraiment intensifies the adjective drôle."),
    (3, None,
     "'It was Camille who thought it was good for me.' Sofia credits the young assistant. "
     "Notice the cleft construction c'est qui highlighting the subject."),
    (4, None,
     "'It's so kind of her. What an adorable girl.' Sofia shows genuine appreciation. "
     "The phrase de sa part means on her part."),
    (5, None,
     "'She would make an excellent agent.' Sofia sees natural talent in Camille. "
     "The conditional ferait expresses potential."),
    (6, None,
     "'So... would you let her represent you?' Gabriel tests the waters carefully. "
     "The verb laisser followed by an infinitive means to let someone do something."),
    (7, None,
     "'Are you crazy? You are my agent.' Sofia reacts with shocked loyalty. "
     "The question is direct and affectionate."),
    (8, None,
     "'Hypothetically speaking, I mean.' Gabriel tries to soften his awkward suggestion. "
     "The phrase je veux dire clarifies intent."),
    (9, None,
     "'You don't want to be my agent anymore?' Sofia worries that Gabriel is backing away. "
     "The negative structure ne ... plus means no longer."),
    (10, None,
     "'Of course I do! It's just that working together is sometimes difficult.' Gabriel reassures her quickly. "
     "The emphatic French response bien sûr que si contradicts a negative question."),
    (11, None,
     "'They say it's hard to mix everything up.' Gabriel repeats the partners' warnings. "
     "The impersonal phrase c'est dur describes difficulty."),
    (12, None,
     "'It can hurt you.' He worries about her professional career. "
     "The expression faire du mal means to cause harm or pain."),
    (13, None,
     "'No, I would never change agents.' Sofia refuses to let him step aside. "
     "The conditional ne changerais jamais emphasizes total loyalty."),
    (14, None,
     "'You found me, you know me, defend me!' She demands his unwavering support. "
     "The imperative défends-moi carries strong emotional urgency."),
    (15, None,
     "'I don't want anyone else but you.' Sofia closes the debate with devotion. "
     "The structure ne ... personne d'autre que means no one else but."),
]

TRANSITION = "Now let's listen to the whole exchange once again without interruption."

OUTRO = (
    "Gabriel wanted to protect Sofia from agency politics, but Sofia's loyalty to him is absolute. "
    "Remember the key expression for defending someone: défendre quelqu'un."
)

CLOSING = ("lea", "Je ne veux personne d'autre que toi.")
