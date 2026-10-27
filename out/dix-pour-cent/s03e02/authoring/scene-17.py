# Authoring module for dix-pour-cent s03e02 scene 17 (cues 826-850).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-17.py --out out/dix-pour-cent/s03e02/scene-17.json

ID = "dix-pour-cent-s03e02-scene-17"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 17
TITLE = "Le mot de Monica  (Monica's Note)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 826-850. Gabriel arrives at ASK and finds his personal things dropped off by Monica Bellucci "
    "with a reproachful note, while Mathias asks him about Noémie's sudden resignation."
)

INTRO = (
    "Gabriel arrives late and exhausted at the ASK offices after sleeping on Andrea's sofa. "
    "He finds a package left by Monica Bellucci and faces questions from senior partner Mathias Barneville. "
    "Listen to their conversation in French first."
)

STORY = [
    ("lea", "Qui a déposé ces affaires ici?",
     "Who dropped off these things here?",
     [(826, "Antoine, qui a mis mes affaires dans mon bureau, là ?")], ""),
    ("mathias", "Monica Bellucci est passée ce matin.",
     "Monica Bellucci came by this morning.",
     [(828, "Monica est venue les déposer ce matin.")], ""),
    ("lea", "Elle est venue en personne ici?",
     "She came in person here?",
     [(828, "Monica est venue les déposer ce matin.")], ""),
    ("mathias", "Oui, elle a laissé ce mot.",
     "Yes, she left this note.",
     [(839, "Elle a laissé un mot pour toi, lis-le.")], ""),
    ("lea", "Que dit ce message pour moi?",
     "What does this message say for me?",
     [(839, "Elle a laissé un mot pour toi, lis-le.")], ""),
    ("mathias", "Elle demande si elle a un agent!",
     "She asks if she has an agent!",
     [(840, "Gabrielle, est-ce que j'ai encore un agent ?")], ""),
    ("lea", "Je suis tellement épuisé ce matin.",
     "I am so exhausted this morning.",
     [(844, "Parce que là, je suis fatigué.")], ""),
    ("mathias", "Tu as commis une grave erreur.",
     "You made a serious mistake.",
     [(843, "si tu veux me virer")], ""),
    ("lea", "Si tu veux me renvoyer, renvoie-moi!",
     "If you want to fire me, fire me!",
     [(843, "si tu veux me virer, voilà, vire-moi tout de suite")], ""),
    ("mathias", "Je dois te poser une question.",
     "I must ask you a question.",
     [(842, "moi, ma question, c'est")], ""),
    ("lea", "De quoi s'agit-il maintenant, Mathias?",
     "What is it about now, Mathias?",
     [(845, "Est-ce que Noémie t'a parlé d'une proposition d'embauche")], ""),
    ("mathias", "Noémie t'a parlé d'un nouveau travail?",
     "Did Noémie tell you about a new job?",
     [(845, "Est-ce que Noémie t'a parlé d'une proposition d'embauche à Boulogne")], ""),
    ("lea", "Non, je ne savais rien du tout!",
     "No, I did not know anything at all!",
     [(846, "Hein ? Ah non, pas du tout ?")], ""),
    ("mathias", "Elle quitte notre agence ce matin.",
     "She is leaving our agency this morning.",
     [(845, "Est-ce que Noémie t'a parlé d'une proposition d'embauche")], "")
]

OPENER = "Let us discover how Gabriel faces the consequences of his dramatic night."

WALK = [
    (0, None,
     "'Who dropped off these things here?' Gabriel spots his personal belongings. "
     "The interrogative pronoun qui asks who."),
    (1, None,
     "'Monica Bellucci came by this morning.' Mathias explains the package arrival. "
     "The compound past est passée uses être as auxiliary."),
    (2, None,
     "'She came in person here?' Gabriel reacts with shocked embarrassment. "
     "The phrase en personne indicates personal presence."),
    (3, None,
     "'Yes, she left this note.' Mathias points out the written letter. "
     "The compound past a laissé comes from laisser."),
    (4, None,
     "'What does this message say for me?' Gabriel inquires about the contents. "
     "The verb dit comes from dire."),
    (5, None,
     "'She asks if she has an agent!' Mathias reveals her ironic question. "
     "The conjunction si introduces an indirect question."),
    (6, None,
     "'I am so exhausted this morning.' Gabriel confesses his lack of sleep. "
     "The adjective épuisé agrees with the masculine speaker."),
    (7, None,
     "'You made a serious mistake.' Mathias reproaches his handling of the star. "
     "The feminine adjective grave precedes or follows erreur."),
    (8, None,
     "'If you want to fire me, fire me!' Gabriel lashes out under stress. "
     "The imperative renvoie-moi demands decisive action."),
    (9, None,
     "'I must ask you a question.' Mathias pivots the conversation to agency business. "
     "The phrase poser une question means to ask a question."),
    (10, None,
     "'What is it about now, Mathias?' Gabriel braces for another crisis. "
     "The impersonal construction s'agir de means to be about."),
    (11, None,
     "'Did Noémie tell you about a new job?' Mathias checks for office rumors. "
     "The past tense t'a parlé addresses Gabriel directly."),
    (12, None,
     "'No, I did not know anything at all!' Gabriel is blindsided by the news. "
     "The negative phrase rien du tout means nothing at all."),
    (13, None,
     "'She is leaving our agency this morning.' Mathias breaks the unsettling development. "
     "The verb quitte denotes permanent departure.")
]

TRANSITION = "Now let us listen to the tense agency discussion once more at normal pace."

OUTRO = (
    "Gabriel deals with the fallout from his disastrous dinner with Monica Bellucci while ASK faces a staff crisis. "
    "Listen to the dialogue once more in French."
)

CLOSING = ("mathias", "Elle quitte notre agence ce matin.")
