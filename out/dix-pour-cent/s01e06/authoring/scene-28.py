ID = "dix-pour-cent-s01e06-scene-28"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 28
TITLE = "Menace de faillite chez ASK  (Threat of Bankruptcy at ASK)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "mathias": "marcel"}
LABELS = {"lea": "Hélène", "gabriel": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"

INTRO = (
    "Following the devastating conclusion of the tax audit, Colette leaves the agency with a "
    "heavy fine and a court summons. In the conference room, Samuel's widow Hélène Kerr "
    "confronts Mathias about whether his wealthy father-in-law will still buy her shares, "
    "and the partners realize the entire agency is facing bankruptcy. "
    "Let's listen to the scene in French first; don't worry about catching every word."
)

STORY = [
    ("lea", "Votre femme et votre beau-père étaient au courant de ce contrôle fiscal?",
     "Did your wife and your father-in-law know about this tax audit?",
     [(720, "Votre femme et votre beau-père étaient"), (720, "au courant de ce contrôle fiscal")],
     "inversion simplified to declarative question"),
    ("mathias", "Oui.",
     "Yes.",
     [(721, "Oui")], ""),
    ("lea", "Ça n'affectera pas leur intention de racheter mes parts?",
     "Won't that affect their intention to buy out my shares?",
     [(722, "affectera pas leur intention de racheter mes parts")], ""),
    ("mathias", "Je ne sais pas, Hélène.",
     "I don't know, Hélène.",
     [(723, "Je ne sais pas, Hélène")], ""),
    ("lea", "C'est incroyable! Comment je vais les vendre?",
     "It's unbelievable! How am I going to sell them?",
     [(724, "C'est incroyable"), (724, "Comment je vais les vendre")], ""),
    ("lea", "S'il n'y a pas de nouveaux fonds, ASK ne survivra pas à ce contrôle fiscal.",
     "If there are no new funds, ASK will not survive this tax audit.",
     [(725, "s'il n'y a pas de nouveaux fonds"), (726, "ASK ne survivra pas à ce contrôle fiscal")], ""),
    ("lea", "Vous comprenez tous ça?",
     "Do you all understand that?",
     [(727, "Vous comprenez tous ça")], ""),
    ("gabriel", "Quoi alors? On fait faillite?",
     "What then? Are we going bankrupt?",
     [(728, "Quoi alors"), (728, "On fait faillite")], ""),
    ("gabriel", "Je vous pose la question! Comment ça, vous ne savez pas?",
     "I'm asking you the question! What do you mean, you don't know?",
     [(729, "Je vous pose la question"), (730, "Comment ça, vous ne savez pas")], ""),
    ("mathias", "Je ne sais pas, Gabriel!",
     "I don't know, Gabriel!",
     [(731, "Je ne sais pas, Gabriel")], ""),
    ("gabriel", "Tu sais toujours tout, toi!",
     "You always know everything!",
     [(732, "Tu sais toujours tout, toi")], ""),
    ("gabriel", "Appelle ta femme, maintenant. Il faut qu'on sache.",
     "Call your wife, now. We have to know.",
     [(733, "Appelle ta femme, maintenant. Il faut qu'on sache")], ""),
    ("mathias", "Ça ne servira à rien. Elle ne me parlera pas.",
     "That won't do any good. She won't speak to me.",
     [(734, "Ça ne servira à rien. Elle ne me parlera pas")], ""),
    ("mathias", "Ça ressemble à un divorce.",
     "It looks like a divorce.",
     [(735, "Ça ressemble à un divorce")], ""),
    ("gabriel", "Qu'est-ce qu'elle fait? Andréa part en courant!",
     "What is she doing? Andréa is running off!",
     [(736, "Qu'est-ce qu'elle fait")],
     "second half describes Andréa rushing after Colette, omitting expletives in 738-739"),
]

OPENER = "Let's go through it slowly. In the conference room, Hélène Kerr questions Mathias."

WALK = [
    (0, None,
     "'Did your wife and your father-in-law know about this tax audit?' Being in the current of something is the French idiom for being informed or in the loop."),
    (1, None,
     "'Yes.' Mathias answers quietly to the group."),
    (2, None,
     "'Won't that affect their intention to buy out my shares?' The verb is in the future tense with the negative words wrapped around it."),
    (3, None,
     "'I don't know, Hélène.' Mathias avoids making any promises."),
    (4, "C'est incroyable!",
     "'It's unbelievable!' The prefix turns the adjective into its opposite."),
    (4, "Comment je vais les vendre?",
     "'How am I going to sell them?' The little word for 'them' sits directly before the infinitive verb."),
    (5, None,
     "'If there are no new funds, ASK will not survive this tax audit.' The future tense indicates that the agency's very existence is now at stake."),
    (6, None,
     "'Do you all understand that?' Hélène looks around the table at Gabriel and Arlette."),
    (7, None,
     "'What then? Are we going bankrupt?' The everyday idiom for going bust or declaring bankruptcy."),
    (8, "Je vous pose la question!",
     "'I'm asking you the question!' Gabriel demands an immediate answer from Mathias."),
    (8, "Comment ça, vous ne savez pas?",
     "'What do you mean, you don't know?' Literally 'how that, you do not know'."),
    (9, None,
     "'I don't know, Gabriel!' Mathias loses his cool under Gabriel's shouting."),
    (10, None,
     "'You always know everything!' Gabriel adds the disjunctive pronoun at the end for emphasis."),
    (11, "Appelle ta femme, maintenant.",
     "'Call your wife, now.' Gabriel insists that Mathias contact Catherine."),
    (11, "Il faut qu'on sache.",
     "'We have to know.' The subjunctive form of the verb 'to know' after the impersonal expression."),
    (12, "Ça ne servira à rien.",
     "'That won't do any good.' Literally 'that will serve to nothing'."),
    (12, "Elle ne me parlera pas.",
     "'She won't speak to me.'"),
    (13, None,
     "'It looks like a divorce.' The verb followed by the preposition means 'looks like' or 'resembles'."),
    (14, None,
     "'What is she doing? Andréa is running off!' While the partners argue, Andréa suddenly bolts out of the conference room and sprints down the stairs after Colette."),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = (
    "As Mathias admits his marriage is over and the agency stares into the abyss of bankruptcy, "
    "Andréa dashes onto the street outside ASK to find Colette. See you in the next scene."
)
CLOSING = ("gabriel", "On fait faillite?")
