# Authoring module for dix-pour-cent s02e06 scene 20 (cues 533-561).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-20.py --out out/dix-pour-cent/s02e06/scene-20.json

ID = "dix-pour-cent-s02e06-scene-20"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 20
TITLE = "Beauté féline  (Feline Beauty)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie"}
LABELS = {"lea": "Juliette", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 533-561. In her Cannes hotel suite, Juliette Binoche reads a predatory poem from billionaire Jean-Denis Gillières. "
    "Juliette refuses to board his yacht, but Andréa warns her about the risks to her film's budget and promises "
    "to accompany her every step of the way to guarantee her safety."
)

INTRO = (
    "In her Cannes hotel suite, Juliette Binoche receives an unwelcome poetic invitation from powerful sponsor Jean-Denis Gillières. "
    "Andréa works to protect her star client from predatory behavior while safeguarding her directorial debut. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Écoute ce poème ridicule envoyé par Gillières.",
     "Listen to this ridiculous poem sent by Gillières.",
     [(533, "« Ta beauté féline me hante.")], ""),
    ("lea", "Il écrit que ma beauté féline le hante.",
     "He writes that my feline beauty haunts him.",
     [(533, "« Ta beauté féline me hante.")], ""),
    ("andrea", "Cet homme ne lâche vraiment jamais l'affaire.",
     "This man really never drops the matter.",
     [(535, "Il ne lâche pas.")], ""),
    ("lea", "Il insiste pour m'inviter sur son bateau demain.",
     "He insists on inviting me onto his boat tomorrow.",
     [(534, "Je brûle d'impatience de te voir sur mon bateau demain. »")], ""),
    ("lea", "Je refuse catégoriquement de monter sur ce yacht.",
     "I categorically refuse to get on that yacht.",
     [(540, "On lui a dit que je n'y allais pas.")], ""),
    ("andrea", "La situation financière de ton film est délicate.",
     "The financial situation of your movie is delicate.",
     [(543, "C'est une situation compliquée.")], ""),
    ("lea", "Qu'est-ce que tu veux dire par là, Andréa?",
     "What do you mean by that, Andréa?",
     [(544, "Qu'est-ce que tu veux dire ?")], ""),
    ("andrea", "Gillières peut bloquer le budget de ton film.",
     "Gillières can block the budget of your movie.",
     [(546, "Il peut vraiment te pourrir pour ton film.")], ""),
    ("lea", "Je ne vais pas céder à un prédateur.",
     "I am not going to yield to a predator.",
     [(541, "Le mec est un psychopathe."), (558, "Moi je pense aux mains baladeuses de Gillières !")], ""),
    ("andrea", "Je comprends ta colère et je te soutiens.",
     "I understand your anger and I support you.",
     [(547, "C'est quelqu'un qu'il ne faut pas contrarier.")], ""),
    ("lea", "Alors trouve une solution pour annuler ce rendez-vous.",
     "Then find a solution to cancel this meeting.",
     [(548, "Dis-lui juste que je n'ai pas le temps.")], ""),
    ("andrea", "Nous pouvons y aller ensemble avec l'équipe.",
     "We can go there together with the team.",
     [(551, "Écoute, je viens avec toi."), (552, "On y va ensemble.")], ""),
    ("lea", "Tu me promets de ne pas me laisser seule?",
     "Do you promise not to leave me alone?",
     [(556, "Ton agent a raison.")], ""),
    ("andrea", "Je serai toujours à tes côtés sur le bateau.",
     "I will always be at your side on the boat.",
     [(560, "T'inquiète pas, on s'occupe de tout.")], ""),
    ("lea", "D'accord, mais nous partirons au bout d'une heure.",
     "Alright, but we will leave after an hour.",
     [(559, "Je vais gerber sur son pont.")], ""),
    ("andrea", "C'est promis, personne ne te touchera!",
     "It is promised, nobody will touch you!",
     [(560, "T'inquiète pas, on s'occupe de tout."), (561, "tu seras la princesse de Cannes.")], "")
]

OPENER = "Let's examine how Andréa protects Juliette from unwanted advances of Gillières."

WALK = [
    (0, None,
     "'Listen to this ridiculous poem sent by Gillières.' Juliette is appalled by the message. "
     "The imperative écoute directs attention to the text."),
    (1, None,
     "'He writes that my feline beauty haunts him.' Juliette reads the pretentious line out loud. "
     "The feminine adjective féline means cat-like."),
    (2, None,
     "'This man really never drops the matter.' Andréa notes his relentless pursuit. "
     "The phrase lâcher l'affaire means to give up or drop it."),
    (3, None,
     "'He insists on inviting me onto his boat tomorrow.' Juliette conveys the unwanted invitation. "
     "The verb insister pour indicates persistent urging."),
    (4, None,
     "'I categorically refuse to get on that yacht.' Juliette takes a firm stand. "
     "The infinitive monter sur means to board or get on."),
    (5, None,
     "'The financial situation of your movie is delicate.' Andréa reminds her of the production stakes. "
     "The adjective délicate indicates vulnerability."),
    (6, None,
     "'What do you mean by that, Andréa?' Juliette senses hesitation in her agent. "
     "The phrase vouloir dire par là asks for clarification."),
    (7, None,
     "'Gillières can block the budget of your movie.' Andréa explains the billionaire's influence. "
     "The masculine noun budget designates production funds."),
    (8, None,
     "'I am not going to yield to a predator.' Juliette refuses to compromise her boundaries. "
     "The masculine noun prédateur designates an abusive person."),
    (9, None,
     "'I understand your anger and I support you.' Andréa validates her client's emotions. "
     "The feminine noun colère denotes righteous anger."),
    (10, None,
     "'Then find a solution to cancel this meeting.' Juliette charges her agent with finding a way out. "
     "The imperative trouve seeks a diplomatic escape."),
    (11, None,
     "'We can go there together with the team.' Andréa suggests a protective compromise. "
     "The adverb ensemble means together as a group."),
    (12, None,
     "'Do you promise not to leave me alone?' Juliette demands guaranteed accompaniment. "
     "The construction promettre de requires an infinitive."),
    (13, None,
     "'I will always be at your side on the boat.' Andréa makes an absolute pledge of protection. "
     "The locution à tes côtés means by your side."),
    (14, None,
     "'Alright, but we will leave after an hour.' Juliette imposes a strict time boundary. "
     "The phrase au bout de indicates an elapsed duration."),
    (15, None,
     "'It is promised, nobody will touch you!' Andréa seals the protective pact firmly. "
     "The indefinite pronoun personne with ne expresses nobody.")
]

TRANSITION = "Now let's listen to the decisive conversation once more at normal pace."

OUTRO = (
    "In her Cannes suite, Juliette Binoche and Andréa form a united front against corporate harassment. "
    "Listen to the powerful dialogue once more in French."
)

CLOSING = ("andrea", "C'est promis, personne ne te touchera!")
