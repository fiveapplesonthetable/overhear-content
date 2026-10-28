# Authoring module for dix-pour-cent s04e02 scene 21 (cues 1036-1047).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-21.py --out out/dix-pour-cent/s04e02/scene-21.json

ID = "dix-pour-cent-s04e02-scene-21"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 21
TITLE = "Une trahison amère  (A Bitter Betrayal)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "elise": "emilie"}
LABELS = {"lea": "Andréa", "elise": "Élise"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1036-1047. Sipping her drink in Andrea's office, Elise Formain bitterly confesses that she was passed over "
    "for the leadership of StarMedia. Despite her superior competence, the board appointed Olivier Dimars simply because he is a man."
)

INTRO = (
    "Sipping her drink in Andrea's office, Elise Formain bitterly confesses that she was passed over for the leadership of StarMedia. "
    "Despite her superior competence, the board appointed Olivier Dimars simply because he is a man. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("elise", "J'étais sûre de te trouver ici.",
     "I was sure I would find you here.",
     [(1036, "J'étais sûr de te trouver ici")], "Expected to find Andrea working late"),
    ("lea", "Les heures supplémentaires ne s'arrangent jamais.",
     "Overtime hours never get any better.",
     [(1038, "les heures sup' ne s'arrangent pas")], "Noted the exhausting demands of leadership"),
    ("elise", "Ils ne m'ont pas choisie finalement.",
     "They did not choose me after all.",
     [(1040, "Ils ne m'ont pas choisie pour diriger StarMédia")], "Revealed her corporate defeat"),
    ("lea", "Pour la direction générale de StarMédia?",
     "For the general directorship of StarMedia?",
     [(1040, "diriger StarMédia")], "Clarified the high executive role"),
    ("elise", "Bréhier a nommé Olivier à ma place.",
     "Brehier appointed Olivier in my place.",
     [(1041, "Bréhier, ce crétin, a nommé Olivier Dimars à ma place")], "Named her unqualified successor"),
    ("lea", "Olivier Dimars n'a presque aucune expérience.",
     "Olivier Dimars has almost no experience.",
     [(1043, "Moins expérimenté")], "Questioned Olivier's qualifications"),
    ("elise", "Il est surtout bien moins compétent.",
     "He is above all much less competent.",
     [(1043, "bien moins compétent")], "Criticized his lack of skill"),
    ("lea", "C'est un choix totalement injuste, Élise.",
     "It is a totally unfair choice, Elise.",
     [(1045, "être la meilleure")], "Agreed that the choice was unfair"),
    ("elise", "Mais c'est un homme, évidemment.",
     "But he is a man, obviously.",
     [(1044, "Mais c'est un homme")], "Pointed out systemic gender bias"),
    ("lea", "Le sexisme dans ce milieu persiste.",
     "Sexism in this industry persists.",
     [(1044, "Mais c'est un homme")], "Acknowledged the deep-seated prejudice"),
    ("elise", "Je croyais qu'il suffisait d'être excellente.",
     "I thought it was enough to be excellent.",
     [(1045, "Je croyais qu'il suffisait d'être la meilleure")], "Lamented her naive dedication"),
    ("lea", "Tu as fait un travail remarquable.",
     "You did remarkable work.",
     [(1045, "la meilleure")], "Recognized her hard work and talent"),
    ("elise", "J'ai été bien trop naïve, apparemment.",
     "I was much too naive, apparently.",
     [(1046, "Je suis encore naïve, apparemment")], "Conceded her disillusionment"),
    ("lea", "Je suis vraiment désolée pour toi.",
     "I am really sorry for you.",
     [(1047, "Je suis désolée")], "Expressed heartfelt sympathy")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'I was sure I would find you here.' Elise speaks with tired resignation. "
     "The imperfect tense recalls her confident assumption."),
    (1, None,
     "'Overtime hours never get any better.' Andrea nods in mutual professional understanding. "
     "The reflexive verb describes their relentless workload."),
    (2, None,
     "'They did not choose me after all.' Elise delivers her heavy news. "
     "The negative compound past confirms her rejection."),
    (3, None,
     "'For the general directorship of StarMedia?' Andrea clarifies the prestigious position. "
     "The prepositional phrase names the targeted role."),
    (4, None,
     "'Brehier appointed Olivier in my place.' Elise grimaces with bitter disappointment. "
     "The prepositional phrase underscores the insult."),
    (5, None,
     "'Olivier Dimars has almost no experience.' Andrea evaluates the rival agent candidly. "
     "The negative adverbial phrase points out his shortcomings."),
    (6, None,
     "'He is above all much less competent.' Elise states the harsh reality directly. "
     "The comparative structure highlights the unfair decision."),
    (7, None,
     "'It is a totally unfair choice, Elise.' Andrea validates her anger with sympathy. "
     "The descriptive adjective condemns the corporate verdict."),
    (8, None,
     "'But he is a man, obviously.' Elise points out the unspoken institutional bias. "
     "The contrasting conjunction introduces the bitter truth."),
    (9, None,
     "'Sexism in this industry persists.' Andrea acknowledges the pervasive prejudice. "
     "The present tense verb deplores enduring corporate habits."),
    (10, None,
     "'I thought it was enough to be excellent.' Elise reflects on her shattered illusions. "
     "The impersonal imperfect construction conveys her lost faith."),
    (11, None,
     "'You did remarkable work.' Andrea honors her rival's undoubted talent. "
     "The encouraging phrase respects her accomplishments."),
    (12, None,
     "'I was much too naive, apparently.' Elise sighs as she swishes her drink. "
     "The adverbial modifier stresses her painful awakening."),
    (13, None,
     "'I am really sorry for you.' Andrea offers sincere solidarity. "
     "The empathetic adjective shows genuine human compassion.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Elise's revelation of sexism at StarMedia exposes the brutal reality of agency politics. When you watch the episode, listen out for the expressions meaning 'sure' and 'to find'. You'll catch them now. See you next time."
CLOSING = ("lea", "Je suis vraiment désolée pour toi.")
