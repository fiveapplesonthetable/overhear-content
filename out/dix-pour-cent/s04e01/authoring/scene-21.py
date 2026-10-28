# Authoring module for dix-pour-cent s04e01 scene 21 (cue 939).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-21.py --out out/dix-pour-cent/s04e01/scene-21.json

ID = "dix-pour-cent-s04e01-scene-21"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 21
TITLE = "Départ précipité  (A Hasty Departure)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 939. After losing the Cesar for Best Female Newcomer, a heartbroken Sofia rushes out of the ceremony hall. "
    "Gabriel follows her into the lobby, confronting the security staff and comforting Sofia as she struggles with disappointment."
)

INTRO = (
    "After losing the Cesar for Best Female Newcomer, a heartbroken Sofia rushes out of the ceremony hall. "
    "Gabriel follows her into the lobby, confronting the security staff and comforting Sofia as she struggles with disappointment. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Je n'ai pas gagné ce prix.",
     "I did not win this prize.",
     [(939, "Elle n'a pas gagné")], "Announced that she did not win"),
    ("gabriel", "Attends Sofia, ne pars pas si vite.",
     "Wait Sofia, do not leave so quickly.",
     [(939, "partir comme ça")], "Urged her not to run away in haste"),
    ("lea", "La sécurité veut nous bloquer ici.",
     "Security wants to block us here.",
     [(939, "partir comme ça")], "Noticed the guards at the exit"),
    ("gabriel", "Elle n'a pas gagné ce soir!",
     "She did not win tonight!",
     [(939, "Elle n'a pas gagné")], "Intervened firmly with security staff"),
    ("lea", "Je veux juste sortir de là.",
     "I just want to get out of there.",
     [(939, "partir comme ça")], "Expressed her urgent desire to leave"),
    ("gabriel", "Tu as fait un travail formidable.",
     "You did a wonderful job.",
     [(939, "Elle n'a pas gagné")], "Praised her acclaimed performance"),
    ("lea", "Tout le monde me regarde fuir.",
     "Everyone is watching me flee.",
     [(939, "partir comme ça")], "Felt self-conscious in the bright lobby"),
    ("gabriel", "Personne ne te juge, respire un coup.",
     "Nobody is judging you, take a breath.",
     [(939, "Elle n'a pas gagné")], "Reassured her against embarrassment"),
    ("lea", "J'ai vraiment honte de cet échec.",
     "I am really ashamed of this failure.",
     [(939, "Elle n'a pas gagné")], "Expressed painful shame over the loss"),
    ("gabriel", "Une nomination est déjà une victoire.",
     "A nomination is already a victory.",
     [(939, "Elle n'a pas gagné")], "Reminded her of the prestige of nomination"),
    ("lea", "Mais j'espérais tellement remporter ce trophée.",
     "But I was hoping so much to win this trophy.",
     [(939, "Elle n'a pas gagné")], "Confessed her secret hopes"),
    ("gabriel", "Tu auras d'autres rôles magnifiques.",
     "You will have other magnificent roles.",
     [(939, "Elle n'a pas gagné")], "Promised great opportunities ahead"),
    ("lea", "Merci d'être là avec moi, Gabriel.",
     "Thank you for being here with me, Gabriel.",
     [(939, "Elle n'a pas gagné")], "Thanked him for his comforting presence"),
    ("gabriel", "On rentre ensemble, la tête haute.",
     "We are going home together, heads held high.",
     [(939, "partir comme ça")], "Led her out with quiet dignity")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'I did not win this prize.' Sofia steps into the corridor and announces her loss. "
     "The compound past highlights the immediate outcome of the vote."),
    (1, None,
     "'Wait Sofia, do not leave so quickly.' Gabriel catches up to her near the exit. "
     "The negative imperative warns her against a hasty flight."),
    (2, None,
     "'Security wants to block us here.' She gestures toward the guards posted in the hall. "
     "The verb expresses unwanted restraint from the staff."),
    (3, None,
     "'She did not win tonight!' Gabriel confronts the usher firmly so they can pass. "
     "The short exclamation cuts through the protocol."),
    (4, None,
     "'I just want to get out of there.' Sofia pulls her wrap tighter around her shoulders. "
     "The modal verb conveys her emotional urgency."),
    (5, None,
     "'You did a wonderful job.' Gabriel reassures her with steady warmth. "
     "The encouraging phrase honors her fine screen acting."),
    (6, None,
     "'Everyone is watching me flee.' Sofia glances nervously toward the crowded foyer. "
     "The infinitive verb emphasizes her sense of exposure."),
    (7, None,
     "'Nobody is judging you, take a breath.' Gabriel places a reassuring hand on her arm. "
     "The familiar colloquial idiom offers quick comfort."),
    (8, None,
     "'I am really ashamed of this failure.' Sofia confesses her painful feelings of inadequacy. "
     "The expression avoir honte conveys vulnerable sorrow."),
    (9, None,
     "'A nomination is already a victory.' Gabriel points out her impressive achievement. "
     "The encouraging noun frames the event positively."),
    (10, None,
     "'But I was hoping so much to win this trophy.' Sofia admits her secret longing for the prize. "
     "The imperfect tense recalls her high expectations."),
    (11, None,
     "'You will have other magnificent roles.' Gabriel speaks with absolute professional confidence. "
     "The future tense pledges exciting future projects."),
    (12, None,
     "'Thank you for being here with me, Gabriel.' Sofia looks up at him with grateful eyes. "
     "The polite expression shows her deep appreciation."),
    (13, None,
     "'We are going home together, heads held high.' Gabriel guides her toward the outer doors. "
     "The proud idiomatic expression restores her dignity.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Sofia and Gabriel leave the ceremony together, ready to focus on new cinematic opportunities. When you watch the episode, listen out for the expressions meaning 'prize' and 'wait'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "On rentre ensemble, la tête haute.")
