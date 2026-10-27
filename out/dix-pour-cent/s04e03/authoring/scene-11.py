# Authoring module for dix-pour-cent s04e03 scene 11 (cues 454-486).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s04e03/scene-11.json

ID = "dix-pour-cent-s04e03-scene-11"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 11
TITLE = "La rivale aux Césars  (The César Rival)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Sofia", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 454-486. At a high-profile photoshoot, Sofia discovers she is scheduled "
    "right after Melanie Meyer, the actress who beat her to the Cesar award. "
    "Sofia vents her frustration to Camille, who encourages her to shine on her own merits."
)

INTRO = (
    "At a high-profile photoshoot, Sofia prepares for her turn in front of the cameras. "
    "She discovers that Melanie Meyer, who won the Cesar award over her, just finished shooting. "
    "Frustrated by constantly feeling second, Sofia shares her doubts with Camille. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Camille, tu peux m'aider un peu?",
     "Camille, can you help me a bit?",
     [(454, "Vous pouvez m'aider")], "Sofia asks Camille for assistance"),
    ("camille", "Bien sûr! Tu es tellement belle aujourd'hui.",
     "Of course! You are so beautiful today.",
     [(456, "Tu es tellement belle")], "Camille compliments Sofia"),
    ("lea", "C'est enfin mon tour maintenant?",
     "Is it finally my turn now?",
     [(460, "C'est ton tour")], "Sofia asks about the schedule"),
    ("camille", "Oui, Mélanie vient de terminer.",
     "Yes, Melanie has just finished.",
     [(461, "Mélanie a terminé")], "Camille confirms Melanie finished"),
    ("lea", "Mélanie Meyer? L'actrice du César?",
     "Melanie Meyer? The actress of the Cesar?",
     [(462, "Mélanie Meyer"), (463, "C'est elle")], "Sofia identifies her rival"),
    ("camille", "Oui, le Meilleur Espoir Féminin.",
     "Yes, the Most Promising Actress.",
     [(463, "Meilleur Espoir Féminin")], "Camille mentions the award"),
    ("lea", "Tu le savais déjà, Camille?",
     "Did you already know, Camille?",
     [(464, "Tu le savais")], "Sofia suspects Camille knew"),
    ("camille", "Je te jure que non, Sofia.",
     "I swear to you no, Sofia.",
     [(465, "Je te jure, non")], "Camille swears she did not know"),
    ("lea", "Elle m'a pris le César!",
     "She took the Cesar from me!",
     [(466, "qui m'a pris le César")], "Sofia vents her frustration"),
    ("lea", "Je vais toujours arriver deuxième?",
     "Am I always going to come in second?",
     [(467, "Je vais toujours arriver deuxième")], "Sofia fears always being second"),
    ("camille", "Ne pense plus à ce prix.",
     "Do not think about that award anymore.",
     [(476, "ton César")], "Camille urges her to move on"),
    ("camille", "Tu as un talent immense, Sofia.",
     "You have an immense talent, Sofia.",
     [(472, "mon agent")], "Camille reassures her client"),
    ("lea", "Je veux donner le meilleur aujourd'hui.",
     "I want to give the best today.",
     [(457, "cette femme")], "Sofia regains determination"),
    ("camille", "Montre-leur ta force devant la caméra!",
     "Show them your strength in front of the camera!",
     [(485, "boulot")], "Camille encourages her for the shoot"),
]

WALK = [
    (0, None,
     "'Camille, can you help me a bit?' Sofia asks her agent for a helping hand with her dress. "
     "The modal verb 'pouvoir' expresses polite ability in questions."),
    (1, None,
     "'Of course! You are so beautiful today.' Camille warmly praises Sofia's appearance. "
     "The intensifier 'tellement' means so or very."),
    (2, None,
     "'Is it finally my turn now?' Sofia wonders if the studio photographer is ready for her. "
     "The adverb 'enfin' marks relief after a waiting period."),
    (3, None,
     "'Yes, Melanie has just finished.' Camille lets Sofia know that the preceding session wrapped up. "
     "The recent past construction uses 'venir de' followed by an infinitive."),
    (4, None,
     "'Melanie Meyer? The actress of the Cesar?' Sofia recognizes the name of the rival actress who won the film prize. "
     "The masculine noun 'Cesar' refers to the French film academy trophy."),
    (5, None,
     "'Yes, the Most Promising Actress.' Camille specifies the official category of the award. "
     "The adjective 'meilleur' signifies best or foremost."),
    (6, None,
     "'Did you already know, Camille?' Sofia asks if her agent had withheld information about the schedule. "
     "The direct object pronoun 'le' stands for the situation."),
    (7, None,
     "'I swear to you no, Sofia.' Camille insists on her complete honesty and innocence. "
     "The verb 'jurer' means to swear or promise firmly."),
    (8, None,
     "'She took the Cesar from me!' Sofia vents her lingering bitterness over losing the trophy. "
     "The indirect pronoun 'me' indicates who was affected by the action."),
    (9, None,
     "'Am I always going to come in second?' Sofia fears that she will constantly remain in the shadow of her rival. "
     "The ordinal numeral 'deuxieme' means second."),
    (10, None,
     "'Do not think about that award anymore.' Camille encourages Sofia to focus on the present photoshoot. "
     "The negative structure 'ne ... plus' means no longer or not anymore."),
    (11, None,
     "'You have an immense talent, Sofia.' Camille reminds her of her unique charisma and acting gifts. "
     "The adjective 'immense' emphasizes great artistic power."),
    (12, None,
     "'I want to give the best today.' Sofia finds her determination to shine for the photographer. "
     "The expression 'donner le meilleur' means to do one's very best."),
    (13, None,
     "'Show them your strength in front of the camera!' Camille gives a final boost of confidence before the flashbulbs fire. "
     "The imperative verb 'montre' commands bold action on set."),
]

OUTRO = (
    "Sofia overcomes her disappointment and steps onto the photoshoot set with renewed confidence. "
    "With Camille cheering her on from the sidelines, she is ready to capture the spotlight. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("camille", "Tu es une grande actrice!")
