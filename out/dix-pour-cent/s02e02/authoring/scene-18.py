# Authoring module for dix-pour-cent s02e02 scene 18 (cues 624-676).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-18.py --out out/dix-pour-cent/s02e02/scene-18.json

ID = "dix-pour-cent-s02e02-scene-18"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 18
TITLE = "Une pause agent  (An Agent Break)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "luchini": "theo"}
LABELS = {"lea": "Andréa", "luchini": "Luchini"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 624-676. Andréa visits Fabrice Luchini at his apartment. Though he announces he is leaving Bréhier "
    "to take a break from all agents, the two eccentric personalities bond deeply over life and theatre."
)

INTRO = (
    "Determined to sign iconic actor Fabrice Luchini, Andréa visits him at his Paris apartment. "
    "Luchini admits he has quit his rival agent Bréhier, but unexpectedly reveals that he plans "
    "to manage his own career without any agency. Listen to their conversation in French first."
)

STORY = [
    ("luchini", "C'est ouvert! Tu veux du thé?",
     "It's open! Would you like tea?",
     [(625, "C'est ouvert"), (627, "Tu veux du thé")], ""),
    ("lea", "Non merci, ça va.",
     "No thanks, I'm fine.",
     [(628, "Non merci, ça va")], ""),
    ("luchini", "Comment tu vas? Tu as l'air dans tous tes états.",
     "How are you? You seem in a state.",
     [(629, "Comment tu vas ? T'as l'air dans tous tes états")], "Restored 'tu as'"),
    ("luchini", "Moi, je suis plutôt déprimé. J'ai raté un film de James Bond.",
     "Me, I'm pretty depressed. I missed out on a James Bond movie.",
     [(630, "Non, je suis plutôt déprimée"), (631, "J'ai raté un film de James Bond")], "Masculine agreement for Luchini"),
    ("luchini", "Alors j'ai quitté Bréhier.",
     "So I left Bréhier.",
     [(633, "Alors j'ai quitté Bréhier")], ""),
    ("lea", "C'est bien!",
     "That's good!",
     [(634, "C'est bien")], ""),
    ("luchini", "Ne t'emballe pas. Je vais faire une pause agent.",
     "Don't get carried away. I am going to take an agent break.",
     [(635, "Ne t'emballe pas"), (637, "Je vais faire une pause agent")], ""),
    ("lea", "C'est-à-dire?",
     "Meaning?",
     [(638, "C'est-à-dire")], ""),
    ("luchini", "Je n'ai aucun film de prévu.",
     "I have no films planned.",
     [(639, "J'ai aucun film de prévu")], "Restored 'ne'"),
    ("luchini", "Je fais du théâtre, je n'ai besoin de personne.",
     "I'm doing theatre, I don't need anyone.",
     [(640, "je fais du théâtre"), (641, "je n'ai besoin de personne")], ""),
    ("luchini", "Je suis désolé, je t'aimais vraiment bien, Andréa.",
     "I am sorry, I really liked you, Andréa.",
     [(642, "Je suis désolée, je t'aimais vraiment bien, Andréa")], "Masculine agreement"),
    ("lea", "C'est comme se faire larguer alors qu'on n'a jamais été ensemble.",
     "It's like getting dumped when you were never even together.",
     [(643, "C'est comme se faire larguer alors qu'on n'a jamais été ensemble")], ""),
    ("luchini", "Oui, c'est un peu ça.",
     "Yes, that's kind of it.",
     [(644, "Ouais, c'est un peu ça")], "'Ouais' -> 'Oui'"),
    ("lea", "Je l'ai perdue pour toujours.",
     "I lost her forever.",
     [(671, "Je l'ai perdue pour toujours")], ""),
    ("luchini", "Et si on allait au théâtre ce soir, puis dîner?",
     "What if we went to the theatre tonight, then had dinner?",
     [(672, "Et si on allait au théâtre ce soir, puis dîner")], ""),
    ("lea", "Ça me plairait.",
     "I would like that.",
     [(675, "Ça me plairait")], ""),
]

OPENER = "Let's explore how Andréa connects with Luchini on a deeply personal level."

WALK = [
    (0, None,
     "'It's open! Would you like tea?' Luchini welcomes Andréa into his chaotic apartment. "
     "The partitive article du introduces the beverage."),
    (1, None,
     "'No thanks, I'm fine.' Andréa politely declines refreshment. "
     "The everyday phrase ça va means I'm fine."),
    (2, None,
     "'How are you? You seem in a state.' Luchini notices her agitated expression. "
     "The French idiom être dans tous ses états means to be completely flustered."),
    (3, None,
     "'Me, I'm pretty depressed. I missed out on a James Bond movie.' The star shares his disappointment. "
     "The verb rater means to miss out on or fail."),
    (4, None,
     "'So I left Bréhier.' Luchini drops the bombshell about firing his agent. "
     "The connector alors introduces a logical consequence."),
    (5, None,
     "'That's good!' Andréa can barely contain her excitement for ASK. "
     "The short phrase c'est bien expresses approval."),
    (6, None,
     "'Don't get carried away. I am going to take an agent break.' Luchini immediately dampens her hopes. "
     "The reflexive idiom s'emballer means to get ahead of oneself."),
    (7, None,
     "'Meaning?' Andréa asks him to clarify his strange decision. "
     "The set expression c'est-à-dire asks for an explanation."),
    (8, None,
     "'I have no films planned.' Luchini explains his schedule. "
     "The negative determiner aucun takes the particle ne."),
    (9, None,
     "'I'm doing theatre, I don't need anyone.' The actor boasts of his theatrical independence. "
     "The phrase avoir besoin de means to need someone or something."),
    (10, None,
     "'I am sorry, I really liked you, Andréa.' Luchini expresses genuine fondness for her. "
     "The imperfect tense j'aimais describes a continuing feeling."),
    (11, None,
     "'It's like getting dumped when you were never even together.' Andréa laments the strange situation. "
     "The informal verb se faire larguer means to get dumped."),
    (12, None,
     "'Yes, that's kind of it.' Luchini chuckles at her candid observation. "
     "The phrase un peu ça confirms a playful analogy."),
    (13, None,
     "'I lost her forever.' Andréa opens up about her heartbreak over Colette. "
     "The direct object pronoun l' takes feminine agreement on the past participle perdue."),
    (14, None,
     "'What if we went to the theatre tonight, then had dinner?' Luchini offers a platonic evening out. "
     "The construction et si followed by an imperfect makes a friendly suggestion."),
    (15, None,
     "'I would like that.' Andréa accepts the warm invitation. "
     "The conditional ça me plairait expresses polite enthusiasm."),
]

TRANSITION = "Now let's listen to the full conversation between Andréa and Luchini once again."

OUTRO = (
    "Although Luchini refuses to sign immediately, Andréa has built a genuine friendship with him. "
    "Remember the everyday idiom for getting carried away: s'emballer."
)

CLOSING = ("luchini", "Et si on allait au théâtre ce soir, puis dîner?")
