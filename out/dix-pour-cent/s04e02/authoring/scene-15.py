# Authoring module for dix-pour-cent s04e02 scene 15 (cues 834-836).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-15.py --out overhear-content/out/dix-pour-cent/s04e02/scene-15.json

ID = "dix-pour-cent-s04e02-scene-15"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 15
TITLE = "Quittes pour une gifle  (Even for a Slap)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "dylan": "theo"}
LABELS = {"lea": "Franck", "dylan": "Dylan"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 834-836. Outside the community center, Franck Dubosc catches up with Dylan "
    "and offers to let the young actor slap him in the face so they can settle their score."
)

INTRO = (
    "Outside the community center, veteran comedian Franck Dubosc catches up with young actor Dylan. "
    "Feeling guilty about their violent confrontation on set, Franck proposes an unusual and direct way to clear the air. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Hé! Dylan, attends un instant.",
     "Hey! Dylan, wait a moment.",
     [(834, "Hé")], "Franck calls Dylan"),
    ("dylan", "Qu'est-ce que tu fais là?",
     "What are you doing here?",
     [(835, "vas-y")], "Dylan turns around"),
    ("lea", "Okay, vas-y sans hésiter.",
     "Okay, go ahead without hesitating.",
     [(835, "Okay, vas-y")], "Franck steps forward"),
    ("dylan", "Vas-y quoi? Je ne comprends pas.",
     "Go ahead with what? I do not understand.",
     [(835, "vas-y")], "Dylan is confused"),
    ("lea", "Gifle-moi maintenant, vas-y!",
     "Slap me now, go ahead!",
     [(836, "Gifle-moi"), (835, "vas-y")], "Franck offers his face"),
    ("dylan", "Tu es sérieux? Tu es fou!",
     "Are you serious? You are crazy!",
     [(836, "Gifle-moi")], "Dylan steps back"),
    ("lea", "Donne-moi une bonne gifle.",
     "Give me a good slap.",
     [(836, "Gifle-moi")], "Franck insists"),
    ("dylan", "Je ne veux pas te frapper.",
     "I do not want to hit you.",
     [(836, "Gifle-moi")], "Dylan declines"),
    ("lea", "Comme ça, on sera quittes enfin.",
     "That way, we will be even finally.",
     [(836, "comme ça on sera quittes")], "Franck explains his reasoning"),
    ("dylan", "Une gifle ne règle rien du tout.",
     "A slap settles nothing at all.",
     [(836, "on sera quittes")], "Dylan points out the futility"),
    ("lea", "Et ensuite, on pourra parler calmement.",
     "And then, we will be able to speak calmly.",
     [(836, "Et ensuite")], "Franck proposes a fresh start"),
    ("dylan", "Tu es vraiment bizarre aujourd'hui.",
     "You are really strange today.",
     [(834, "Hé")], "Dylan observes Franck"),
    ("lea", "Je regrette mon geste stupide.",
     "I regret my stupid gesture.",
     [(836, "Gifle-moi")], "Franck expresses remorse"),
    ("dylan", "Oublions ça pour le moment.",
     "Let us forget that for now.",
     [(836, "on sera quittes")], "Dylan lowers his guard"),
]

WALK = [
    (0, None,
     "'Hey! Dylan, wait a moment.' Franck calls after Dylan in the quiet alleyway. "
     "The interjection 'he' serves to catch someone's attention."),
    (1, None,
     "'What are you doing here?' Dylan is surprised to see the older actor approach him alone. "
     "The interrogative 'qu'est-ce que' introduces an open question."),
    (2, None,
     "'Okay, go ahead without hesitating.' Franck encourages Dylan to release his pent-up anger. "
     "The imperative 'vas-y' urges immediate action."),
    (3, None,
     "'Go ahead with what? I do not understand.' Dylan does not grasp Franck's sudden request. "
     "The negative verb phrase 'ne comprends pas' signals confusion."),
    (4, None,
     "'Slap me now, go ahead!' Franck offers Dylan a free strike to balance out the violence on set. "
     "The compound imperative 'gifle-moi' attaches a hyphenated pronoun."),
    (5, None,
     "'Are you serious? You are crazy!' Dylan reacts with disbelief to the absurd proposal. "
     "The adjective 'serieux' asks about genuine intent."),
    (6, None,
     "'Give me a good slap.' Franck repeats his plea with sincere humility. "
     "The noun 'gifle' denotes a slap across the cheek."),
    (7, None,
     "'I do not want to hit you.' Dylan refuses to resort to physical violence. "
     "The modal verb 'vouloir' expresses intent or desire."),
    (8, None,
     "'That way, we will be even finally.' Franck argues that physical retaliation will restore balance. "
     "The idiom 'etre quittes' means to be even or square."),
    (9, None,
     "'A slap settles nothing at all.' Dylan recognizes that more violence will not heal the rift. "
     "The verb 'regler' means to settle or resolve an issue."),
    (10, None,
     "'And then, we will be able to speak calmly.' Franck hopes this gesture will open a genuine dialogue. "
     "The adverb 'calmement' indicates a peaceful manner."),
    (11, None,
     "'You are really strange today.' Dylan is struck by Franck's unconventional attempt at making peace. "
     "The adverb 'vraiment' reinforces the adjective 'bizarre'."),
    (12, None,
     "'I regret my stupid gesture.' Franck sincerely acknowledges his past bad behavior on the film set. "
     "The verb 'regretter' expresses remorse or regret."),
    (13, None,
     "'Let us forget that for now.' Dylan decides to let go of the grudge and move forward. "
     "The imperative 'oublions' invites mutual forgiveness."),
]

OUTRO = (
    "Franck Dubosc shows unexpected humility by offering Dylan a chance to retaliate for their fight on set. "
    "By refusing to strike back, Dylan opens the door to a calmer and more honest conversation. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Merci d'avoir écouté, Dylan.")
