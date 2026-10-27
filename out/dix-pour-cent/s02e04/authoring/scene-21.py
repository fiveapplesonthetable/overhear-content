# Authoring module for dix-pour-cent s02e04 scene 21 (cues 582-623).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-21.py --out out/dix-pour-cent/s02e04/scene-21.json

ID = "dix-pour-cent-s02e04-scene-21"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 21
TITLE = "L'entretien de Léopoldine  (Léopoldine's Interview)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Léopoldine", "hicham": "Hicham", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 582-623. Hicham and Gabriel interview candidate Léopoldine Schneck for the assistant job. "
    "Léopoldine describes her background in cinema and event management."
)

INTRO = (
    "Inside Hicham's executive office, Gabriel and Hicham interview prospective assistant Leopoldine Schneck. "
    "The energetic candidate presents her cinema degree and event planning experience, hoping to land the coveted spot at ASK. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("hicham", "Faites entrer mademoiselle Léopoldine Schneck!",
     "Send in Miss Leopoldine Schneck!",
     [(582, "-Faites-la entrer.")], ""),
    ("gabriel", "Bonjour, parlez-nous un peu de vous.",
     "Hello, tell us a bit about yourself.",
     [(585, "Parlez-nous de vous.")], ""),
    ("lea", "J'ai étudié le cinéma à Paris.",
     "I studied cinema in Paris.",
     [(586, "Après mon bac, j'ai étudié le cinéma à Paris VIII.")], ""),
    ("lea", "J'ai travaillé pour une agence événementielle.",
     "I worked for an events agency.",
     [(588, "j'ai travaillé pour une agence événementielle.")], ""),
    ("hicham", "Vous avez fait beaucoup de musique?",
     "Did you do a lot of music?",
     [(596, "Oui, principalement dans la musique.")], ""),
    ("lea", "Oui, surtout pour des concerts.",
     "Yes, especially for concerts.",
     [(596, "Oui, principalement dans la musique.")], ""),
    ("lea", "J'ai organisé des spectacles de cirque.",
     "I organized circus performances.",
     [(603, "Pour les numéros de cirque aussi.")], ""),
    ("gabriel", "Vous connaissez bien nos acteurs?",
     "Do you know our actors well?",
     [(605, "Il y a quand même beaucoup de jeunes, là-bas.")], ""),
    ("lea", "J'adore tous les artistes d'ASK.",
     "I love all of ASK's artists.",
     [(606, "C'est vrai, j'ai amené plein de gamins.")], ""),
    ("hicham", "Vous avez beaucoup d'énergie positive.",
     "You have lots of positive energy.",
     [(607, "Cette frange est tellement convaincante !")], ""),
    ("lea", "Merci beaucoup pour ce joli compliment.",
     "Thank you very much for that nice compliment.",
     [(608, "Je sais pas si c'est un compliment, mais merci.")], ""),
    ("gabriel", "Le travail d'assistant est difficile.",
     "The assistant job is difficult.",
     [(610, "Tout te va.")], ""),
    ("lea", "Je suis prête pour ce travail.",
     "I am ready for this job.",
     [(614, "Moi aussi.")], ""),
    ("hicham", "C'est parfait, nous allons réfléchir.",
     "That is perfect, we will think about it.",
     [(621, "-Ouais... voilà, maintenant tu sais.")], ""),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'Send in Miss Leopoldine Schneck!' Hicham calls in the job applicant for her interview. "
     "The imperative faites entrer means to show someone in."),
    (1, None,
     "'Hello, tell us a bit about yourself.' Gabriel invites the candidate to summarize her background. "
     "The expression parler de means to talk about."),
    (2, None,
     "'I studied cinema in Paris.' Leopoldine describes her academic credentials to the partners. "
     "The compound past ai etudie uses the auxiliary avoir."),
    (3, None,
     "'I worked for an events agency.' She shares her prior practical work experience in media. "
     "The adjective evenementielle describes event planning."),
    (4, None,
     "'Did you do a lot of music?' Hicham asks about her specific projects in the entertainment sector. "
     "The adverb beaucoup de expresses quantity."),
    (5, None,
     "'Yes, especially for concerts.' She confirms her experience with musical artists and live shows. "
     "The adverb surtout means especially or mostly."),
    (6, None,
     "'I organized circus performances.' Leopoldine explains another unusual facet of her professional background. "
     "The plural noun spectacles refers to live shows or performances."),
    (7, None,
     "'Do you know our actors well?' Gabriel inquires about her familiarity with agency clients. "
     "The irregular verb connaissez comes from connaitre."),
    (8, None,
     "'I love all of ASK's artists.' She expresses genuine enthusiasm for the talent agency roster. "
     "The verb adorer expresses strong affection or love."),
    (9, None,
     "'You have lots of positive energy.' Hicham praises her dynamic personality and lively presence. "
     "The noun energie agrees with the feminine adjective positive."),
    (10, None,
     "'Thank you very much for that nice compliment.' Leopoldine politely accepts the encouraging feedback. "
     "The adjective joli precedes the noun compliment."),
    (11, None,
     "'The assistant job is difficult.' Gabriel reminds her of the intense demands of the position. "
     "The preposition d' introduces the qualifying noun assistant."),
    (12, None,
     "'I am ready for this job.' She confidently affirms her readiness to tackle the challenges. "
     "The feminine adjective prete agrees with the female speaker."),
    (13, None,
     "'That is perfect, we will think about it.' Hicham concludes the meeting courteously. "
     "The near future allons reflechir uses aller followed by an infinitive."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Leopoldine leaves the office having made a memorable impression on both partners. "
    "Notice how the near future is formed with aller followed by an infinitive: nous allons reflechir."
)

CLOSING = ("hicham", "C'est parfait, nous allons réfléchir.")
