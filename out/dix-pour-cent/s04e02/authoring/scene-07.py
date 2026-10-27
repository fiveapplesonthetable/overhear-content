# Authoring module for dix-pour-cent s04e02 scene 07 (cues 372-408).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-07.py --out out/dix-pour-cent/s04e02/scene-07.json

ID = "dix-pour-cent-s04e02-scene-07"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 7
TITLE = "Le savon de Gabriel  (Gabriel's Lecture)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "franck": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "franck": "Franck"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 372-408. Franck Dubosc confronts Gabriel over a press interview, but Gabriel challenges "
               "him to embrace serious drama, earning Franck's respect and loyalty as an agent.")

INTRO = ("At ASK, comedy star Franck Dubosc angrily confronts Gabriel about an interview in Telerama for a serious drama. "
         "Gabriel delivers a passionate speech challenging him to conquer his fears, convincing Franck to trust him completely. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("franck", "C'est quoi cette interview dans Télérama?",
     "What is this interview in Telerama?",
     [(373, "C'est quoi cette histoire avec Télérama ?")], "Franck arrives demanding an explanation about press coverage"),
    ("gabriel", "C'est une excellente nouvelle pour toi, Franck!",
     "It is excellent news for you, Franck!",
     [(375, "félicitations !")], "Gabriel celebrates the prestigious cultural opportunity"),
    ("franck", "Tu n'es même pas mon agent officiel!",
     "You are not even my official agent!",
     [(377, "Tu n'es pas mon agent.")], "Franck challenges Gabriel's authority"),
    ("franck", "Je veux abandonner ce film dramatique!",
     "I want to abandon this dramatic movie!",
     [(378, "un projet que je suis prêt à lâcher !")], "Franck declares his intention to walk away from the production"),
    ("gabriel", "Tu as peur de sortir de ton confort!",
     "You are afraid to leave your comfort zone!",
     [(384, "T'es dans ta zone de confort.")], "Gabriel identifies the actor's inner fear"),
    ("franck", "Moi? Je n'ai peur de rien!",
     "Me? I am not afraid of anything!",
     [(385, "T'as la trouille !")], "Franck bristles defensively at the accusation"),
    ("gabriel", "J'ai vu ta répétition, c'était sublime!",
     "I saw your rehearsal, it was sublime!",
     [(387, "C'était beau, sublime.")], "Gabriel praises Franck's dramatic depth and sincerity"),
    ("gabriel", "Montre à tout le monde ton vrai talent!",
     "Show everyone your true talent!",
     [(392, "ce dont t'es capable !")], "Gabriel urges him to prove his range as an artist"),
    ("franck", "Tu crois vraiment que j'en suis capable?",
     "Do you really believe that I am capable of it?",
     [(393, "Tu te fous de qui ?")], "Franck softens as he hears Gabriel's conviction"),
    ("lea", "Bonjour messieurs, tout se passe bien ici?",
     "Hello gentlemen, is everything going well here?",
     [(397, "Bonjour, Franck.")], "Andrea walks into the office hallway"),
    ("franck", "Oui, je discute avec mon nouvel agent.",
     "Yes, I am talking with my new agent.",
     [(400, "Avec mon agent.")], "Franck proudly confirms Gabriel's role"),
    ("gabriel", "Je viens de passer un savon à Dubosc!",
     "I just gave Dubosc a proper lecture!",
     [(403, "Je viens de passer un savon à Dubosc !")], "Gabriel celebrates his triumphant assertiveness"),
    ("lea", "Bravo Gabriel, c'est comme ça qu'ils avancent!",
     "Bravo Gabriel, that is how they make progress!",
     [(408, "C'est ce qu'il faut faire.")], "Andrea validates his agenting technique"),
]

OPENER = "Let's explore Gabriel and Franck Dubosc's intense confrontation line by line."

WALK = [
    (0, None,
     "'What is this interview in Telerama?' Franck demands to know why Gabriel pitched him to an intellectual film magazine."),
    (1, None,
     "'It is excellent news for you, Franck!' Gabriel insists that highbrow press attention validates Franck as a serious dramatic actor."),
    (2, None,
     "'You are not even my official agent!' Franck attempts to dismiss Gabriel's initiative on technical grounds."),
    (3, None,
     "'I want to abandon this dramatic movie!' Franck confesses his desire to quit the film due to insecurity."),
    (4, None,
     "'You are afraid to leave your comfort zone!' Gabriel directly challenges Franck's reliance on familiar comic routines."),
    (5, None,
     "'Me? I am not afraid of anything!' Franck retorts with hurt pride, refusing to look weak."),
    (6, None,
     "'I saw your rehearsal, it was sublime!' Gabriel speaks with heartfelt emotion about Franck's authentic dramatic performance."),
    (7, None,
     "'Show everyone your true talent!' Gabriel calls on Franck to demonstrate his artistic maturity to the industry."),
    (8, None,
     "'Do you really believe that I am capable of it?' Franck reveals the vulnerable self-doubt underlying his anger."),
    (9, None,
     "'Hello gentlemen, is everything going well here?' Andrea steps into the corridor to check on the loud voices."),
    (10, None,
     "'Yes, I am talking with my new agent.' Franck announces his loyalty to Gabriel in front of the agency head."),
    (11, None,
     "'I just gave Dubosc a proper lecture!' Gabriel tells Andrea with immense pride how he stood up to the star."),
    (12, None,
     "'Bravo Gabriel, that is how they make progress!' Andrea encourages Gabriel's newfound boldness in guiding talent."),
]

TRANSITION = "Now let's listen to Gabriel and Franck's conversation once more from start to finish."

OUTRO = ("Gabriel wins Franck Dubosc's trust by delivering honest, fearless feedback about artistic potential. "
         "Let's review the key dramatic and professional vocabulary from this scene.")

CLOSING = ("lea", "Bravo Gabriel, c'est comme ça qu'ils avancent!")
