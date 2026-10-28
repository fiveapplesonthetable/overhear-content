# Authoring module for dix-pour-cent s04e06 scene 14 (cues 659-674).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-14.py --out out/dix-pour-cent/s04e06/scene-14.json

ID = "dix-pour-cent-s04e06-scene-14"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 14
TITLE = "La vérité brutale  (The Brutal Truth)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 659-674. In her office with Jean Reno, Andrea cuts through Gabriel's polite evasions and reveals the unvarnished truth: "
    "ASK is bankrupt, the film lacks six million euros, and the agency is sinking."
)

INTRO = (
    "Sitting down with Jean Reno in her office, Andrea listens as the famous actor praises Xavier Beauvois's powerful screenplay. "
    "Rather than disguising the agency's desperate financial distress, Andrea decides to lay all their cards on the table. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Andrea choosing complete honesty with Jean Reno step by step."

STORY = [
    ("jean", "C'est un scénario très intense, puissant.",
     "It is a very intense, powerful script.",
     [(659, "très intense, puissant")], "Jean praises the script's raw artistic energy"),
    ("lea", "C'est un projet magnifique et rare.",
     "It is a magnificent and rare project.",
     [(660, "C'est un beau scénario")], "Andrea highlights the unique quality of the film"),
    ("jean", "Où en êtes-vous pour le financement?",
     "How are you coming along with financing?",
     [(661, "le financement"), (662, "Où en êtes-vous")], "Jean asks about the budget situation"),
    ("lea", "Jean, je refuse de vous mentir.",
     "Jean, I refuse to lie to you.",
     [(661, "le financement")], "Andrea chooses courage and frankness"),
    ("jean", "Dites-moi tout en toute franchise.",
     "Tell me everything with complete candor.",
     [(662, "Où en êtes-vous")], "Jean welcomes her straightforward approach"),
    ("lea", "Il nous manque six millions d'euros.",
     "We are missing six million euros.",
     [(667, "Il nous manque")], "Andrea reveals the massive budget deficit"),
    ("jean", "Six millions? C'est une grosse somme.",
     "Six million? That is a large sum.",
     [(667, "Il nous manque")], "Jean acknowledges the huge financial gap"),
    ("lea", "Notre agence a déposé le bilan.",
     "Our agency has filed for bankruptcy.",
     [(668, "a déposé le bilan")], "Delivers the shocking financial reality"),
    ("jean", "Vous n'avez donc aucune garantie financière?",
     "You therefore have no financial guarantee?",
     [(669, "garanties sur le film")], "Jean clarifies their lack of backing"),
    ("lea", "Non, notre agence est en train de couler.",
     "No, our agency is sinking.",
     [(670, "en train de couler")], "Admits that ASK is collapsing"),
    ("jean", "Vous me parlez avec grand courage.",
     "You speak to me with great courage.",
     [(670, "en train de couler")], "Jean admires her fearless transparency"),
    ("lea", "Je préfère la vérité aux faux espoirs.",
     "I prefer truth to false hopes.",
     [(670, "en train de couler")], "Andrea rejects misleading business talk"),
    ("jean", "Votre honnêteté est tout à fait admirable.",
     "Your honesty is entirely admirable.",
     [(670, "en train de couler")], "Jean honors her moral integrity"),
    ("lea", "Merci d'écouter la réalité, Jean.",
     "Thank you for listening to reality, Jean.",
     [(670, "en train de couler")], "Andrea thanks him for his patient listening"),
]

WALK = [
    (0, None,
     "'It is a very intense, powerful script.' Jean gives his glowing initial impression of the screenplay. The descriptive adjective for 'intense' agrees in gender and number with its noun."),
    (1, None,
     "'It is a magnificent and rare project.' Andrea agrees on the film's artistic worth. The key noun here means 'project', anchored by its matching French article."),
    (2, None,
     "'How are you coming along with financing?' Jean asks about the state of production funds. Inverting the verb and pronoun around 'financing' creates a crisp, polished question."),
    (3, None,
     "'Jean, I refuse to lie to you.' Andrea resolves not to hide behind false assurances. The clause hinges on the everyday verb meaning 'refuse'."),
    (4, None,
     "'Tell me everything with complete candor.' Jean invites her to be completely open. The verb meaning 'tell me' pairs naturally with the noun for 'frankness' in everyday conversation."),
    (5, None,
     "'We are missing six million euros.' Andrea states the exact size of the shortfall. Notice how 'is missing' leads directly into the noun meaning 'millions'."),
    (6, None,
     "'Six million? That is a large sum.' Jean grasps the severity of the financial deficit. The adjective meaning 'large' takes its feminine form here to match the noun it describes."),
    (7, None,
     "'Our agency has filed for bankruptcy.' Andrea confesses that ASK is in legal liquidation. This conversational past tense combines a helper verb with the past participle for 'filed'."),
    (8, None,
     "'You therefore have no financial guarantee?' Jean confirms that no safety net exists. The verb meaning 'have' pairs naturally with the noun for 'guarantee' in everyday conversation."),
    (9, None,
     "'No, our agency is sinking.' Andrea uses a vivid maritime metaphor for their crisis. Notice how 'sink' leads directly into the noun meaning 'agency'."),
    (10, None,
     "'You speak to me with great courage.' Jean commends her uncommon professional bravery. Jean uses the polite 'you' form alongside 'speak' to keep a respectful professional tone."),
    (11, None,
     "'I prefer truth to false hopes.' Andrea explains her core moral stance. The verb meaning 'prefer' pairs naturally with the noun for 'truth' in everyday conversation."),
    (12, None,
     "'Your honesty is entirely admirable.' Jean shows deep respect for her candor. The descriptive adjective for 'admirable' agrees in gender and number with its noun."),
    (13, None,
     "'Thank you for listening to reality, Jean.' Andrea thanks the star for hearing her out."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Refusing to spin illusions for Jean Reno, Andrea boldly confesses that ASK is bankrupt, lacking six million euros to produce Xavier Beauvois's film, earning the actor's deepest respect. When you watch the episode, listen out for the expressions meaning 'script' and 'intense'. You'll catch them now. See you next time."
CLOSING = ("lea", "Je préfère la vérité aux faux espoirs.")
