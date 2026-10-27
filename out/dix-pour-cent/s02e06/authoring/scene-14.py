# Authoring module for dix-pour-cent s02e06 scene 14 (cues 327-373).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e06/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s02e06/scene-14.json

ID = "dix-pour-cent-s02e06-scene-14"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 14
TITLE = "Tout est complet  (Fully Booked)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie"}
LABELS = {"lea": "Noémie", "catherine": "Catherine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 327-373. In the Paris office, Mathias's wife Catherine asks Noémie to help her travel to Cannes "
    "to surprise Mathias, forcing Noémie to surrender her own train reservation."
)

INTRO = (
    "At the agency office in Paris, Mathias's wife Catherine arrives unexpectedly, hoping to travel down to Cannes to surprise her husband. "
    "Desperate to book a ticket when all flights are sold out, Catherine turns to Noemie, unaware that the assistant must sacrifice her own secret ticket. "
    "Listen to the scene in French first."
)

STORY = [
    ("catherine", "Bonjour, Noémie, vous partez?",
     "Hello, Noemie, are you leaving?",
     [(334, "Bonjour, Noémie"), (335, "Vous partez")], ""),
    ("catherine", "Vous rejoignez Mathias à Cannes?",
     "Are you joining Mathias in Cannes?",
     [(337, "Vous rejoignez Mathias")], ""),
    ("catherine", "Je veux lui faire la surprise!",
     "I want to surprise him!",
     [(341, "Je veux lui faire la surprise")], ""),
    ("catherine", "J'ai besoin de son programme.",
     "I need his schedule.",
     [(342, "besoin de son programme")], ""),
    ("catherine", "Vous pourriez me réserver un vol?",
     "Could you book a flight for me?",
     [(343, "me réserver un vol")], ""),
    ("lea", "Mais tout est complet aujourd'hui.",
     "But everything is fully booked today.",
     [(344, "tout est complet")], ""),
    ("catherine", "Les choses vont beaucoup mieux entre nous.",
     "Things are going much better between us.",
     [(347, "beaucoup mieux entre nous")], ""),
    ("lea", "Je vais imprimer le programme de Mathias.",
     "I will print Mathias's schedule.",
     [(356, "imprimer le programme de Mathias")], ""),
    ("lea", "Tous les vols sont complets, madame.",
     "All flights are fully booked, madam.",
     [(357, "Tous les vols sont complets")], ""),
    ("catherine", "Et pour le train?",
     "What about the train?",
     [(358, "Et le train")], ""),
    ("lea", "Une place reste dans le train de nuit.",
     "One seat remains on the night train.",
     [(359, "une place dans le train de nuit")], ""),
    ("catherine", "Je peux lui apporter des croissants!",
     "I can bring him croissants!",
     [(361, "apporter des croissants")], ""),
    ("catherine", "Tu es mon sauveur, Noémie!",
     "You are my savior, Noemie!",
     [(362, "Tu es mon sauveur, Noémie")], ""),
    ("catherine", "Merci pour votre aide précieuse.",
     "Thank you for your valuable help.",
     [(363, "Merci")], "adapted polite closure"),
    ("catherine", "Mathias ne peut pas se passer de toi.",
     "Mathias cannot manage without you.",
     [(364, "ne peut pas se passer de toi")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Hello, Noemie, are you leaving?' Catherine greets Mathias's dedicated assistant in the office. "
     "The polite inquiry notices her packed bags."),
    (1, None,
     "'Are you joining Mathias in Cannes?' Catherine asks about Mathias's schedule at the festival. "
     "The proper noun phrase specifies the film festival city."),
    (2, None,
     "'I want to surprise him!' Mathias's wife reveals her secret romantic plan. "
     "The infinitive verb expresses her spontaneous intention."),
    (3, None,
     "'I need his schedule.' Catherine asks for her husband's festival agenda. "
     "The fixed idiomatic expression denotes necessity."),
    (4, None,
     "'Could you book a flight for me?' She requests assistant help with travel bookings. "
     "The polite conditional verb asks for a booking service."),
    (5, None,
     "'But everything is fully booked today.' Noemie explains that festival flights are unavailable. "
     "The predicate adjective describes total lack of seats."),
    (6, None,
     "'Things are going much better between us.' Catherine confides that their marital relationship has improved. "
     "The adverbial comparative emphasizes positive change."),
    (7, None,
     "'I will print Mathias's schedule.' Noemie cooperates despite her hidden affair with Mathias. "
     "The near-future verb form indicates immediate action."),
    (8, None,
     "'All flights are fully booked, madam.' She confirms the complete lack of airplane seats. "
     "The universal quantifier emphasizes zero availability."),
    (9, None,
     "'What about the train?' Catherine refuses to give up on traveling down south. "
     "The elliptical question proposes a rail alternative."),
    (10, None,
     "'One seat remains on the night train.' Noemie reluctantly gives up her own reserved sleeper berth. "
     "The noun phrase designates the overnight rail service."),
    (11, None,
     "'I can bring him croissants!' Catherine excitedly imagines breakfast with her husband. "
     "The modal verb introduces a cheerful romantic gesture."),
    (12, None,
     "'You are my savior, Noemie!' Catherine warmly hugs the conflicted assistant. "
     "The predicate noun expresses enthusiastic gratitude."),
    (13, None,
     "'Thank you for your valuable help.' She expresses heartfelt appreciation for the booking. "
     "The polite formula acknowledges office support."),
    (14, None,
     "'Mathias cannot manage without you.' Catherine praises Noemie's indispensable role, unaware of their secret romance. "
     "The idiomatic verb phrase denotes complete reliance.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Heartbroken and conflicted, Noemie gives up her own overnight train ticket so that Mathias's wife can surprise him in Cannes. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "Bon voyage à Cannes, madame.")
