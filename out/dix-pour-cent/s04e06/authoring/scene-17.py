# Authoring module for dix-pour-cent s04e06 scene 17 (cues 823-827).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e06/authoring/scene-17.py --out overhear-content/out/dix-pour-cent/s04e06/scene-17.json

ID = "dix-pour-cent-s04e06-scene-17"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 17
TITLE = "La visite surprise  (The Surprise Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 823-827. Colette arrives outside the ASK agency with baby Flora in a stroller. "
    "Andrea is deeply moved by the unexpected visit and takes her daughter into her arms before they walk to the park."
)

INTRO = (
    "Outside the ASK agency, Andrea Martel receives an unexpected visit from Colette Brancillon, who brings baby Flora in a stroller. "
    "Surprised and deeply touched, Andrea takes her daughter into her arms for a joyful reunion. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Colette! Qu'est-ce que tu fais là?",
     "Colette! What are you doing here?",
     [(823, "Qu'est-ce que tu fais là ?")], "Andrea greets Colette with surprise"),
    ("colette", "On se promenait dans le quartier.",
     "We were taking a walk in the neighborhood.",
     [(824, "On était dans le coin et je me suis dit que même si tu étais occupée...")], "Colette explains their stroll"),
    ("lea", "Tu as amené Flora avec toi?",
     "You brought Flora with you?",
     [(825, "Tu serais contente de voir ta fille.")], "Andrea notices the baby stroller"),
    ("colette", "Oui, elle voulait voir sa mère.",
     "Yes, she wanted to see her mother.",
     [(825, "Tu serais contente de voir ta fille.")], "Colette shares Flora's wish"),
    ("lea", "C'est une très belle surprise!",
     "It is a very wonderful surprise!",
     [(826, "Bien sûr...")], "Andrea smiles warmly with emotion"),
    ("colette", "Je sais que tu travailles beaucoup.",
     "I know that you work a lot.",
     [(824, "même si tu étais occupée...")], "Colette acknowledges Andrea's schedule"),
    ("lea", "Oui, mais vous me manquez tellement.",
     "Yes, but I miss you both so much.",
     [(826, "Bien sûr...")], "Andrea admits her deep longing"),
    ("colette", "Prends-la dans tes bras maintenant.",
     "Take her in your arms now.",
     [(827, "Viens avec maman.")], "Colette offers to unbuckle the baby"),
    ("lea", "Viens avec maman, mon petit trésor.",
     "Come with mommy, my little treasure.",
     [(827, "Viens avec maman.")], "Andrea lifts Flora tenderly"),
    ("colette", "Elle te sourit avec bonheur.",
     "She smiles at you with happiness.",
     [(827, "Viens avec maman.")], "Colette watches the baby's joy"),
    ("lea", "Tu es si douce, ma Flora.",
     "You are so sweet, my Flora.",
     [(827, "Viens avec maman.")], "Andrea hugs her daughter close"),
    ("colette", "Allons faire un tour au parc.",
     "Let us take a walk in the park.",
     [(824, "On était dans le coin")], "Colette suggests a peaceful location"),
    ("lea", "Oui, avec grand plaisir, Colette.",
     "Yes, with great pleasure, Colette.",
     [(826, "Bien sûr...")], "Andrea agrees happily"),
    ("colette", "Prenons le temps de nous poser.",
     "Let us take the time to pause.",
     [(824, "On était dans le coin")], "Colette leads the way toward the bench"),
]

WALK = [
    (0, None,
     "'Colette! What are you doing here?' Andrea is stunned to see Colette outside ASK. "
     "The question phrase 'qu'est-ce que' asks what."),
    (1, None,
     "'We were taking a walk in the neighborhood.' Colette explains why she is nearby. "
     "The reflexive verb 'se promener' means to take a walk."),
    (2, None,
     "'You brought Flora with you?' Andrea looks down happily at the stroller. "
     "The compound past 'as amene' comes from 'amener', to bring someone."),
    (3, None,
     "'Yes, she wanted to see her mother.' Colette smiles warmly at the baby. "
     "The verb form 'voulait' comes from 'vouloir' in the imperfect."),
    (4, None,
     "'It is a very wonderful surprise!' Andrea feels a wave of relief and joy. "
     "The feminine noun 'surprise' designates an unexpected event."),
    (5, None,
     "'I know that you work a lot.' Colette acknowledges Andrea's busy schedule. "
     "The adverb 'beaucoup' indicates a large amount."),
    (6, None,
     "'Yes, but I miss you both so much.' Andrea expresses her heartfelt longing. "
     "The structure 'vous me manquez' literally translates to you are missing to me."),
    (7, None,
     "'Take her in your arms now.' Colette gently unbuckles Flora from the stroller. "
     "The plural noun 'bras' means arms."),
    (8, None,
     "'Come with mommy, my little treasure.' Andrea lifts baby Flora into her arms. "
     "The noun 'tresor' is an affectionate term of endearment."),
    (9, None,
     "'She smiles at you with happiness.' Colette observes the tender reunion. "
     "The verb 'sourit' comes from 'sourire', to smile."),
    (10, None,
     "'You are so sweet, my Flora.' Andrea holds her daughter close against her chest. "
     "The feminine adjective 'douce' means gentle or sweet."),
    (11, None,
     "'Let us take a walk in the park.' Colette suggests stepping away from the office. "
     "The imperative 'allons' invites shared action."),
    (12, None,
     "'Yes, with great pleasure, Colette.' Andrea agrees gladly to spend time together. "
     "The noun 'plaisir' means pleasure or delight."),
    (13, None,
     "'Let us take the time to pause.' Colette leads the way toward the park bench. "
     "The reflexive verb 'se poser' means to settle down or rest."),
]

OUTRO = (
    "Reunited in the peaceful Parisian sunshine, Andrea and Colette set off together toward the nearby park. "
    "Holding Flora in her arms, Andrea feels grounded after weeks of intense workplace pressure. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "C'est si bon d'être réunies!")
