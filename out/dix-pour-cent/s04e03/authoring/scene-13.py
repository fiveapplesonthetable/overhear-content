# Authoring module for dix-pour-cent s04e03 scene 13 (cues 540-562).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e03/authoring/scene-13.py --out overhear-content/out/dix-pour-cent/s04e03/scene-13.json

ID = "dix-pour-cent-s04e03-scene-13"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 13
TITLE = "La visite imprévue de José  (José's Unexpected Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jose": "theo"}
LABELS = {"lea": "Andréa", "jose": "José"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 540-562. Desperate over Colette's disappearance for twenty-four hours, Andrea is "
    "suddenly interrupted at home by an exuberant, drunken Jose Garcia. Jose boasts about having "
    "the wildest night of his life, while Andrea tries desperately to keep him quiet around the sleeping baby."
)

INTRO = (
    "Late at night in her apartment, Andrea Martel worries about Colette's sudden silence. "
    "Her anxious thoughts are shattered when actor Jose Garcia knocks loudly at her door in high spirits. "
    "Let's listen to their chaotic encounter in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("jose", "Andréa! Ouvre la porte, c'est moi!",
     "Andrea! Open the door, it is me!",
     [(541, "Andréa !"), (555, "C'est José !")], "José knocks loudly on the door"),
    ("lea", "José? Qu'est-ce que tu fais là?",
     "Jose? What are you doing here?",
     [(540, "Ah, José"), (542, "Qu'est-ce que tu fais là ?")], "Andréa opens the door in surprise"),
    ("jose", "Quelle nuit incroyable, Andréa!",
     "What an incredible night, Andrea!",
     [(547, "Mais quelle nuit, Andréa !"), (548, "C'était la nuit la plus folle")], "José boasts about his night"),
    ("lea", "Chut! Parle doucement, s'il te plaît.",
     "Hush! Speak softly, please.",
     [(548, "S'il te plaît"), (549, "Calme-toi")], "Andréa tells him to lower his voice"),
    ("lea", "Mon bébé dort dans la chambre.",
     "My baby is sleeping in the bedroom.",
     [(550, "Le bébé dort")], "Andréa explains the baby is asleep"),
    ("jose", "Oh pardon, je veux voir ta fille!",
     "Oh sorry, I want to see your daughter!",
     [(550, "Ta fille ?"), (551, "Je peux aller jeter un œil ?")], "José asks to see the baby"),
    ("lea", "Non, reste ici dans le salon.",
     "No, stay here in the living room.",
     [(560, "Reste là")], "Andréa stops him from entering the bedroom"),
    ("jose", "Tu es magnifique ce soir, Andréa!",
     "You are gorgeous tonight, Andrea!",
     [(558, "T'es magnifique, sérieusement")], "José compliments Andréa"),
    ("lea", "Mais tu as bu beaucoup d'alcool!",
     "But you drank a lot of alcohol!",
     [(545, "t'es bourré"), (546, "aussi bourré")], "Andréa points out his drunkenness"),
    ("jose", "Oui, j'ai passé la soirée avec Laurence.",
     "Yes, I spent the evening with Laurence.",
     [(610, "J'étais avec Laurence")], "José reveals who he was with"),
    ("lea", "Tu dois te reposer pour ton tournage.",
     "You must rest for your film shoot.",
     [(544, "Ça fait une éternité")], "Andréa reminds him of work tomorrow"),
    ("jose", "Je peux me servir à boire?",
     "Can I serve myself a drink?",
     [(561, "Je peux me servir à boire ?")], "José asks for a drink"),
    ("lea", "Bois seulement de l'eau fraîche maintenant.",
     "Drink only cold water now.",
     [(562, "sers-toi")], "Andréa offers water instead"),
    ("jose", "D'accord, je vais me calmer un peu.",
     "All right, I am going to calm down a bit.",
     [(549, "Calme-toi")], "José finally agrees to quiet down"),
]

WALK = [
    (0, None,
     "'Andrea! Open the door, it is me!' Jose calls out enthusiastically from the hallway. "
     "The familiar imperative 'ouvre' commands someone you know well."),
    (1, None,
     "'Jose? What are you doing here?' Andrea opens her door in complete bewilderment. "
     "The question structure 'qu'est-ce que' is the standard way to ask what in French."),
    (2, None,
     "'What an incredible night, Andrea!' Jose cannot contain his excitement after an evening out. "
     "The exclamative adjective 'incroyable' expresses overwhelming surprise."),
    (3, None,
     "'Hush! Speak softly, please.' Andrea immediately hushes the boisterous actor. "
     "The interjection 'chut' is the standard French sound used to request silence."),
    (4, None,
     "'My baby is sleeping in the bedroom.' Andrea explains why they must remain extremely quiet. "
     "The verb 'dormir' describes sleep in the present tense."),
    (5, None,
     "'Oh sorry, I want to see your daughter!' Jose expresses spontaneous affection for Andrea's infant. "
     "The feminine noun 'fille' means daughter or girl."),
    (6, None,
     "'No, stay here in the living room.' Andrea firmly directs him away from the nursery. "
     "The adverb 'ici' points to the immediate location."),
    (7, None,
     "'You are gorgeous tonight, Andrea!' Jose delivers a cheerful, drunken compliment to his agent. "
     "The temporal phrase 'ce soir' refers to this evening or tonight."),
    (8, None,
     "'But you drank a lot of alcohol!' Andrea notices Jose's inebriated state right away. "
     "The quantifier 'beaucoup de' takes an invariable 'de' before the noun."),
    (9, None,
     "'Yes, I spent the evening with Laurence.' Jose reveals that he spent hours reminiscing with Laurence. "
     "The past participle 'passe' combines with 'avoir' to describe spending time."),
    (10, None,
     "'You must rest for your film shoot.' Andrea reminds him that a demanding camera crew awaits tomorrow. "
     "The modal verb 'devoir' indicates duty or obligation."),
    (11, None,
     "'Can I serve myself a drink?' Jose heads toward the kitchen counter looking for refreshments. "
     "The reflexive verb 'se servir' means to help oneself."),
    (12, None,
     "'Drink only cold water now.' Andrea insists that alcohol is out of the question tonight. "
     "The restrictive adverb 'seulement' limits the choice to water."),
    (13, None,
     "'All right, I am going to calm down a bit.' Jose relents and agrees to quiet down for the night. "
     "The near-future construction 'vais me calmer' signals an immediate change in behavior."),
]

OUTRO = (
    "Andrea manages to steer Jose Garcia into her living room without waking baby Flora. "
    "Exhausted by his antics and worried about his morning shoot, she prepares to keep a close eye on him. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Dors bien sur le canapé!")
