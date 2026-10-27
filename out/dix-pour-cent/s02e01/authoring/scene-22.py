# Authoring module for dix-pour-cent s02e01 scene 22 (cues 661-680).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-22.py --out out/dix-pour-cent/s02e01/scene-22.json

ID = "dix-pour-cent-s02e01-scene-22"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 22
TITLE = "Soirée confidences  (Evening Confidences)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Virginie", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 661-680. Taking shelter in Gabriel's messy apartment, Virginie opens up about her strained relationship with Ramzy. "
    "Overcome with anger at the photographers gathered on the street below, she opens the window and screams at them."
)

INTRO = (
    "Inside Gabriel's apartment, Virginie finds a temporary sanctuary from the media circus outside. "
    "As night falls, she confides her genuine guilt about her breakup with Ramzy before losing her temper at the paparazzi waiting below. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("lea", "Ce tournage était une grande erreur.",
     "This shoot was a big mistake.",
     [(661, "Ce film était une erreur")], ""),
    ("gabriel", "Pourquoi est-ce que tu dis ça?",
     "Why do you say that?",
     [(662, "Pourquoi ?")], ""),
    ("lea", "Jouer le couple idéal n'a aucun sens.",
     "Playing the ideal couple makes no sense.",
     [(663, "Ça n'a aucun sens, jouer le couple idéal")], ""),
    ("lea", "On ne parle jamais de nos vrais soucis.",
     "We never talk about our real worries.",
     [(664, "alors qu'on n'arrive même pas à parler de nos problèmes")], ""),
    ("gabriel", "Vous avez des soucis entre vous?",
     "Do you have worries between you two?",
     [(665, "Vous avez des problèmes ?")], ""),
    ("lea", "Il fait comme si tout allait bien.",
     "He acts as though everything were fine.",
     [(668, "Il fait comme si ça n'existait pas")], ""),
    ("lea", "Il veut toujours plaisanter avec tout le monde.",
     "He always wants to joke with everyone.",
     [(668, "il veut plaisanter")], ""),
    ("lea", "Moi, je préfère parler des vraies choses.",
     "Me, I prefer to speak about real things.",
     [(669, "Moi j'aime bien parler des problèmes")], ""),
    ("lea", "Alors après cinq mois, la tension a explosé.",
     "So after five months, the tension exploded.",
     [(670, "Alors après quatre mois de tournage, ça a explosé"), (672, "Cinq ! C'est beaucoup")], ""),
    ("gabriel", "Tu as des nouvelles de lui aujourd'hui?",
     "Do you have news from him today?",
     [(673, "Tu as des nouvelles de lui ?")], ""),
    ("lea", "Non, il refuse encore de me parler.",
     "No, he still refuses to speak to me.",
     [(675, "Il refuse encore de me parler")], ""),
    ("lea", "Ça me pèse de lui faire du mal.",
     "It weighs on me to hurt him.",
     [(677, "Ça me pèse de lui avoir fait du mal comme ça")], ""),
    ("lea", "Regarde par la fenêtre, ils sont encore là!",
     "Look through the window, they are still there!",
     [(678, "Sales cons !")], "Cleaned outburst"),
    ("lea", "Laissez-moi tranquille, partez d'ici!",
     "Leave me alone, go away from here!",
     [(680, "Bande de voyeurs ! Lâchez-moi !")], "Cleaned vulgar outburst"),
]

OPENER = "Now let's break down the scene step by step. Listen to each line, followed by its meaning and a short explanation."

WALK = [
    (0, None,
     "'This shoot was a big mistake.' Virginie reflects on the romantic comedy they filmed together. "
     "The adjective grande comes before the noun to emphasize its importance."),
    (1, None,
     "'Why do you say that?' Gabriel asks her to explain her sudden regret. "
     "The question phrase pourquoi est-ce que is a standard way to ask why."),
    (2, None,
     "'Playing the ideal couple makes no sense.' Pretending on screen felt completely false to her. "
     "The infinitive jouer acts as the subject of the sentence."),
    (3, None,
     "'We never talk about our real worries.' Deep communication issues were constantly ignored. "
     "The negative adverb jamais follows the verb directly in present tense."),
    (4, None,
     "'Do you have worries between you two?' Gabriel inquires gently about their personal relationship. "
     "The preposition entre means between two people or things."),
    (5, None,
     "'He acts as though everything were fine.' Ramzy avoided confronting any unpleasant truth. "
     "The conjunction phrase comme si takes the imperfect tense to describe a condition."),
    (6, None,
     "'He always wants to joke with everyone.' Humor became a constant defense mechanism. "
     "The adverb toujours sits right after the conjugated modal verb."),
    (7, None,
     "'Me, I prefer to speak about real things.' Virginie needs emotional honesty and open dialogue. "
     "The emphatic pronoun moi highlights her own personal contrast."),
    (8, None,
     "'So after five months, the tension exploded.' The prolonged pressure on set finally reached a breaking point. "
     "The preposition apres indicates time that has elapsed."),
    (9, None,
     "'Do you have news from him today?' Gabriel wonders if Ramzy has tried to get in touch. "
     "The expression avoir des nouvelles de means to hear from someone."),
    (10, None,
     "'No, he still refuses to speak to me.' Ramzy remains hurt and completely unreachable. "
     "The adverb encore expresses the ongoing continuation of an action."),
    (11, None,
     "'It weighs on me to hurt him.' She carries a heavy emotional burden from their breakup. "
     "The impersonal construction expresses a feeling of being weighed down with guilt."),
    (12, None,
     "'Look through the window, they are still there!' She spots the persistent paparazzi waiting outside on the street. "
     "The imperative regarde draws direct attention to the outside scene."),
    (13, None,
     "'Leave me alone, go away from here!' She vents her anger and frustration into the night air. "
     "The polite imperative form laissez-moi asks for immediate personal space."),
]

TRANSITION = "Now let's listen to the entire exchange once more from beginning to end."

OUTRO = (
    "Virginie pours out her complicated feelings before shouting down at the relentless press. "
    "Remember the common expression for hearing from someone: avoir des nouvelles de."
)

CLOSING = ("lea", "Laissez-moi tranquille, partez d'ici!")
