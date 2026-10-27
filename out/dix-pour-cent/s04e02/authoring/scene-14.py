# Authoring module for dix-pour-cent s04e02 scene 14 (cues 809-833).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s04e02/scene-14.json

ID = "dix-pour-cent-s04e02-scene-14"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 14
TITLE = "L'orthophoniste secret  (The Secret Speech Therapist)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "dylan": "theo", "franck": "marcel"}
LABELS = {"lea": "Gabriel", "dylan": "Dylan", "franck": "Franck"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 809-833. Outside the community center, Gabriel tries to pressure Dylan "
    "into dropping his complaint against Franck Dubosc, but Franck reveals the man Dylan met "
    "was really his speech therapist."
)

INTRO = (
    "Outside the community center, Gabriel confronts young actor Dylan to salvage Franck Dubosc's reputation. "
    "Desperate to make Dylan drop his complaint, Gabriel resorts to clumsy accusations until Franck steps in with a surprising discovery. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Dylan! Attends une seconde, s'il te plaît.",
     "Dylan! Wait a second, please.",
     [(809, "Dylan ?"), (813, "S'il te plaît")], "Gabriel calls out to Dylan"),
    ("dylan", "Qu'est-ce que tu veux de moi?",
     "What do you want from me?",
     [(810, "Qu'est-ce que tu veux")], "Dylan responds defensively"),
    ("lea", "Franck n'a rien à voir là-dedans.",
     "Franck has nothing to do with it.",
     [(812, "Franck n'a rien à voir là-dedans")], "Gabriel defends his client"),
    ("lea", "S'il te plaît, retire ta plainte.",
     "Please, withdraw your complaint.",
     [(813, "retire ta plainte")], "Gabriel pleads with Dylan"),
    ("dylan", "Non, je ne retire rien du tout.",
     "No, I am withdrawing nothing at all.",
     [(814, "je retire rien du tout")], "Dylan refuses firmly"),
    ("lea", "Tu files du fric à tes amis?",
     "Do you hand out cash to your friends?",
     [(817, "Tu files du fric à tes amis")], "Gabriel questions the transaction"),
    ("dylan", "Pourquoi tu me cherches des histoires?",
     "Why are you picking fights with me?",
     [(819, "Pourquoi tu me cherches")], "Dylan bristles at the suspicion"),
    ("lea", "Voilà ce que je te propose.",
     "Here is what I offer you.",
     [(820, "voilà ce que je te propose")], "Gabriel makes an offer"),
    ("lea", "Tu ramènes ton dealer sur le tournage?",
     "Are you bringing your dealer on set?",
     [(821, "ton dealer sur le tournage")], "Gabriel makes a wild accusation"),
    ("dylan", "C'est un beau stéréotype ridicule.",
     "That is a nice ridiculous stereotype.",
     [(823, "Beau stéréotype")], "Dylan calls out the bias"),
    ("dylan", "Vas-y, fais ce que tu veux!",
     "Go ahead, do what you want!",
     [(826, "Ouais, vas-y")], "Dylan walks away angrily"),
    ("lea", "Quel connard, je n'y crois pas!",
     "What an idiot, I do not believe it!",
     [(827, "Quel connard")], "Gabriel vents his frustration"),
    ("franck", "Je crois que tu te trompes.",
     "I think you are mistaken.",
     [(827, "Je crois que tu te trompes")], "Franck intervenes"),
    ("franck", "C'était son orthophoniste, pas un dealer.",
     "It was his speech therapist, not a dealer.",
     [(828, "C'était son orthophoniste")], "Franck reveals the truth"),
]

WALK = [
    (0, None,
     "'Dylan! Wait a second, please.' Gabriel tries to stop the young actor before he walks away. "
     "The polite formula 's'il te plait' is used with friends or peers."),
    (1, None,
     "'What do you want from me?' Dylan reacts defensively to being cornered outside. "
     "The question phrase 'qu'est-ce que' asks for a direct object."),
    (2, None,
     "'Franck has nothing to do with it.' Gabriel insists that Franck Dubosc is completely innocent in this conflict. "
     "The expression 'n'avoir rien a voir' means to have nothing to do with something."),
    (3, None,
     "'Please, withdraw your complaint.' Gabriel urges Dylan to drop the formal legal action against his client. "
     "The imperative verb 'retire' comes from 'retirer'."),
    (4, None,
     "'No, I am withdrawing nothing at all.' Dylan firmly refuses to drop the charges against Franck. "
     "The negative structure 'ne ... rien du tout' strengthens the refusal."),
    (5, None,
     "'Do you hand out cash to your friends?' Gabriel probes Dylan about the money he just handed over. "
     "The colloquial verb 'filer' means to give or hand over."),
    (6, None,
     "'Why are you picking fights with me?' Dylan challenges Gabriel's hostile and intrusive questions. "
     "The idiom 'chercher des histoires' means to look for trouble."),
    (7, None,
     "'Here is what I offer you.' Gabriel attempts to lay down an ultimatum to settle the issue. "
     "The demonstrative phrase 'voila ce que' presents a proposal."),
    (8, None,
     "'Are you bringing your dealer on set?' Gabriel recklessly accuses Dylan of illegal drug dealings. "
     "The noun 'tournage' refers to a film shoot."),
    (9, None,
     "'That is a nice ridiculous stereotype.' Dylan points out the insulting bias behind Gabriel's accusation. "
     "The noun 'stereotype' denotes a cliche or prejudice."),
    (10, None,
     "'Go ahead, do what you want!' Dylan dismisses Gabriel and dares him to carry out his threat. "
     "The imperative 'vas-y' encourages someone to proceed."),
    (11, None,
     "'What an idiot, I do not believe it!' Gabriel vents his irritation once Dylan turns his back. "
     "The exclamative adjective 'quel' introduces a strong emotional reaction."),
    (12, None,
     "'I think you are mistaken.' Franck Dubosc steps in to correct Gabriel's hasty conclusion. "
     "The reflexive verb 'se tromper' means to make a mistake."),
    (13, None,
     "'It was his speech therapist, not a dealer.' Franck clarifies the true identity of the man Dylan met. "
     "The noun 'orthophoniste' designates a speech-language therapist."),
]

OUTRO = (
    "Gabriel tries every trick to protect his client, even making baseless accusations against Dylan. "
    "However, Franck Dubosc discovers that the young actor was merely meeting his speech therapist. "
    "Now let's listen to their confrontation one last time."
)

CLOSING = ("lea", "Mais pourquoi a-t-il besoin d'un orthophoniste?")
