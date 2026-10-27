# Authoring module for dix-pour-cent s04e04 scene 07 (cues 469-491).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e04/authoring/scene-07.py --out overhear-content/out/dix-pour-cent/s04e04/scene-07.json

ID = "dix-pour-cent-s04e04-scene-07"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 7
TITLE = "La dernière prise d'Hervé  (Hervé's Last Take)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Valérie", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 469-491. Finishing his final take on set, Hervé is surprised by the director Valérie with white lilies and glowing praise. "
    "Deeply impressed by his performance, she offers him an additional day of shooting with a brand new scene written for his character."
)

INTRO = (
    "On the movie set, director Valerie calls cut on Herve's final scene to warm applause from the crew. "
    "Presenting him with white lilies, Valerie makes an unexpected offer that delights the aspiring actor. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's explore Valerie and Herve's warm conversation line by line."
TRANSITION = "Now let's listen to the full discussion once again from start to finish."

STORY = [
    ("lea", "Coupez, c'est dans la boîte!",
     "Cut, that is a wrap!",
     [(469, "Coupez !"), (471, "Super, on l'a !")], "Valérie calls cut on Hervé's final scene"),
    ("lea", "Dernière prise pour Hervé André-Jezak!",
     "Last take for Herve Andre-Jezak!",
     [(475, "C'était la dernière prise pour Hervé")], "Valérie announces the wrap to the crew"),
    ("herve", "Merci à toute l'équipe formidable!",
     "Thanks to the whole wonderful team!",
     [(477, "Merci.")], "Hervé receives warm applause"),
    ("lea", "Voici des lys blancs pour toi.",
     "Here are some white lilies for you.",
     [(478, "Oh, des lys blancs !")], "Valérie offers him his favorite flowers"),
    ("herve", "Oh, ce sont mes fleurs préférées!",
     "Oh, those are my favorite flowers!",
     [(478, "Mes fleurs préférées.")], "Hervé is deeply moved by the gift"),
    ("lea", "Ton jeu était tellement authentique aujourd'hui.",
     "Your acting was so authentic today.",
     [(481, "être aussi authentique.")], "Valérie praises his acting talent"),
    ("herve", "J'essaie simplement de rester naturel.",
     "I simply try to remain natural.",
     [(482, "je ne le remarque pas")], "Hervé responds with modest grace"),
    ("lea", "Es-tu libre pour un verre ce soir?",
     "Are you free for a drink tonight?",
     [(484, "Tu es libre pour un verre ?")], "Valérie invites him to celebrate"),
    ("herve", "Bien sûr, avec grand plaisir!",
     "Of course, with great pleasure!",
     [(485, "C'est juste que je")], "Hervé gladly accepts her invitation"),
    ("lea", "J'ai imaginé une nouvelle scène superbe.",
     "I imagined a superb new scene.",
     [(486, "Ça m'a donné une idée de nouvelle scène.")], "Valérie pitches an unexpected creative idea"),
    ("herve", "Une autre scène pour mon personnage?",
     "Another scene for my character?",
     [(487, "Une autre scène avec toi.")], "Hervé is pleasantly surprised"),
    ("lea", "Oui, un jour de tournage supplémentaire!",
     "Yes, an extra day of shooting!",
     [(488, "jour de tournage supplémentaire ?")], "Valérie confirms the extended shoot"),
    ("herve", "Je vais recevoir un autre bouquet?",
     "Will I receive another bouquet?",
     [(490, "Et un autre bouquet ?")], "Hervé jokes about receiving more flowers"),
    ("herve", "Je suis vraiment très heureux!",
     "I am really very happy!",
     [(491, "je suis trop content !")], "Hervé celebrates his expanded movie role"),
]

WALK = [
    (0, None,
     "'Cut, that is a wrap!' Valerie announces the completion of the scene."),
    (1, None,
     "'Last take for Herve Andre-Jezak!' The director announces the end of Herve's scheduled filming."),
    (2, None,
     "'Thanks to the whole wonderful team!' Herve graciously thanks the film crew for their support."),
    (3, None,
     "'Here are some white lilies for you.' Valerie presents him with a thoughtful floral gift."),
    (4, None,
     "'Oh, those are my favorite flowers!' Herve is touched that she remembered his personal preference."),
    (5, None,
     "'Your acting was so authentic today.' Valerie praises the emotional sincerity of his performance."),
    (6, None,
     "'I simply try to remain natural.' Herve humbly deflects her generous compliment."),
    (7, None,
     "'Are you free for a drink tonight?' Valerie invites him out to celebrate his success."),
    (8, None,
     "'Of course, with great pleasure!' Herve enthusiastically accepts her celebratory invitation."),
    (9, None,
     "'I imagined a superb new scene.' Valerie reveals an unexpected creative idea."),
    (10, None,
     "'Another scene for my character?' Herve is astonished by the chance to expand his role."),
    (11, None,
     "'Yes, an extra day of shooting!' Valerie confirms that production will extend his contract."),
    (12, None,
     "'Will I receive another bouquet?' Herve jokes playfully about receiving more flowers."),
    (13, None,
     "'I am really very happy!' Herve expresses pure joy at his growing acting prospects."),
]

OUTRO = (
    "Touched by the director's praise and thrilled by the promise of an expanded role, Herve celebrates his breakthrough on set. "
    "Let's review the key vocabulary from this scene."
)

CLOSING = ("herve", "Je suis vraiment très heureux!")
