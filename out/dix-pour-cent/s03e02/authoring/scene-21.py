# Authoring module for dix-pour-cent s03e02 scene 21 (cue 909).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-21.py --out out/dix-pour-cent/s03e02/scene-21.json

ID = "dix-pour-cent-s03e02-scene-21"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 21
TITLE = "Une cigarette forte  (A Strong Smoke)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Hervé", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cue 909. Outside the cinema, Hervé bums a strong cigarette to calm his nerves after a stressful "
               "screening, sharing a smoke with Gabriel on the pavement. Adapted for A1 French.")

INTRO = ("Outside the cinema on the pavement, Herve panics after watching the screening of his new auteur film. "
         "Trying to calm his racing anxiety, he borrows a heavy cigarette from the ticket clerk, which he shares with agent Gabriel. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("gabriel", "Tu fumes une cigarette maintenant, Hervé?",
  "You smoke a cigarette now, Herve?",
  [(905, "Tu fumes toi maintenant ?")], "Inquired about smoking habit"),
 ("lea", "J'ai taxé une clope pour déstresser.",
  "I bummed a smoke to de-stress.",
  [(906, "taxé une clope")], "Admitted borrowing a cigarette"),
 ("gabriel", "Tu as l'air vraiment très troublé.",
  "You seem really very troubled.",
  [(907, "tourner la tête")], "Observed intense anxiety"),
 ("lea", "Elle me fait tourner la tête!",
  "It is making my head spin!",
  [(907, "tourner la tête.")], "Complained of tobacco dizziness"),
 ("gabriel", "Passe cette cigarette, s'il te plaît.",
  "Pass that cigarette, please.",
  [(908, "Passe s'il te plaît.")], "Asked to share cigarette"),
 ("lea", "Tiens, prends-la si tu veux.",
  "Here, take it if you want.",
  [(908, "Passe")], "Handed over cigarette"),
 ("gabriel", "C'est vrai que c'est fort!",
  "It is true that it is strong!",
  [(909, "c'est vrai que c'est fort.")], "Confirmed tobacco strength"),
 ("lea", "Je me sens tellement angoissé, Gabriel.",
  "I feel so anxious, Gabriel.",
  [(907, "tourner la tête")], "Confessed inner panic"),
 ("gabriel", "Respire calmement au lieu de fumer.",
  "Breathe calmly instead of smoking.",
  [(909, "c'est fort.")], "Advised deep breathing"),
 ("lea", "Le film m'a complètement bouleversé.",
  "The film completely shook me.",
  [(910, "Pardon, je suis sorti")], "Expressed shock at screening"),
 ("gabriel", "Nous allons en parler tranquillement ensemble.",
  "We are going to talk about it calmly together.",
  [(910, "je suis sorti")], "Offered supportive conversation"),
 ("lea", "J'ai besoin de prendre l'air.",
  "I need to get fresh air.",
  [(907, "tourner la tête")], "Requested moment outdoors"),
 ("gabriel", "Je reste juste ici avec toi.",
  "I stay right here with you.",
  [(908, "Passe")], "Promised constant presence"),
 ("lea", "Merci Gabriel, tu es un vrai ami.",
  "Thank you Gabriel, you are a true friend.",
  [(909, "c'est vrai")], "Thanked for loyal friendship"),
]

OPENER = "Let's observe how Gabriel comforts Herve during a sudden wave of panic on the pavement."

WALK = [
 (0, None,
  "'You smoke a cigarette now, Herve?' An inquisitive question expressing gentle surprise."),
 (1, None,
  "'I bummed a smoke to de-stress.' A casual explanation using colloquial vocabulary."),
 (2, None,
  "'You seem really very troubled.' An empathetic observation on visible emotional distress."),
 (3, None,
  "'It is making my head spin!' An idiomatic expression describing dizziness from strong tobacco."),
 (4, None,
  "'Pass that cigarette, please.' A polite request asking to share the smoke."),
 (5, None,
  "'Here, take it if you want.' A generous presentative handing over the cigarette."),
 (6, None,
  "'It is true that it is strong!' An agreement exclaiming astonishment at the cigarette's strength."),
 (7, None,
  "'I feel so anxious, Gabriel.' A vulnerable confession sharing internal emotional turmoil."),
 (8, None,
  "'Breathe calmly instead of smoking.' A sensible imperative advising calm relaxation."),
 (9, None,
  "'The film completely shook me.' A direct statement explaining intense emotional reaction."),
 (10, None,
  "'We are going to talk about it calmly together.' A reassuring commitment to supportive discussion."),
 (11, None,
  "'I need to get fresh air.' An expression of physical necessity using avoir besoin de."),
 (12, None,
  "'I stay right here with you.' A comforting promise of faithful companionship."),
 (13, None,
  "'Thank you Gabriel, you are a true friend.' A heartfelt expression of deep personal gratitude."),
]

TRANSITION = "Now let's listen to Gabriel and Herve again at full speed."

OUTRO = ("Sharing a strong cigarette in the evening breeze, Gabriel helps Herve regain his composure after a harrowing screening. "
         "Their bond proves once again that solidarity thrives outside the agency walls.")

CLOSING = ("gabriel", "Prends une grande inspiration, Hervé.")
