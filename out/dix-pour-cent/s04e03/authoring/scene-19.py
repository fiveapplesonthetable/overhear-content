# Authoring module for dix-pour-cent s04e03 scene 19 (cues 918-988).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-19.py --out out/dix-pour-cent/s04e03/scene-19.json

ID = "dix-pour-cent-s04e03-scene-19"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 19
TITLE = "Une plaidoirie passionnée  (A Passionate Defense)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "igor": "theo"}
LABELS = {"lea": "Noemie", "igor": "Igor"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 918-950. At dinner, producer Igor de Serisy criticizes Xavier Beauvois's screenplay "
    "for being excessively violent and dark. Noemie boldly interjects to deliver a brilliant literary "
    "defense of the script, leaving Igor deeply impressed by her passion and intellect."
)

INTRO = (
    "At the dinner table, producer Igor de Serisy expresses serious reservations about Xavier Beauvois's screenplay, "
    "complaining that it is far too dark and violent. Noemie steps forward with unexpected eloquence, "
    "delivering a passionate artistic defense of the film that leaves the producer astonished. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "J'ai lu le scénario de Xavier.",
     "I read Xavier's screenplay.",
     [(918, "moi aussi j'ai lu le scénario")], "Introduced her perspective on the project"),
    ("igor", "Il est beaucoup trop violent et sombre.",
     "It is much too violent and dark.",
     [(926, "C'est très violent"), (905, "c'est sombre")], "Stated his primary artistic objection"),
    ("lea", "Mais cette violence a un sens profond.",
     "But this violence has a deep meaning.",
     [(929, "montrer de façon réaliste"), (931, "Sa cruauté profonde")], "Argued for the film's dramatic purpose"),
    ("igor", "Pourquoi montrer une telle cruauté à l'écran?",
     "Why show such cruelty on screen?",
     [(931, "Sa cruauté profonde"), (941, "Où est la vraie violence")], "Questioned the necessity of graphic brutality"),
    ("lea", "Elle montre la dureté de cette époque.",
     "It shows the harshness of that era.",
     [(930, "la violence même de l'époque")], "Contextualized the historical setting"),
    ("igor", "Le public risque de rejeter ce film.",
     "The public risks rejecting this film.",
     [(899, "de sérieuses réserves")], "Expressed commercial anxiety"),
    ("lea", "Ce n'est pas de la violence gratuite.",
     "This is not gratuitous violence.",
     [(934, "Ce n'est pas gratuit")], "Emphasized the artistic integrity"),
    ("igor", "Les personnages prennent les armes sans hésiter.",
     "The characters take up arms without hesitating.",
     [(938, "ils prennent les armes")], "Pointed out the extreme character actions"),
    ("lea", "Ils réagissent aux contraintes de la société.",
     "They react to society's constraints.",
     [(936, "contraintes qui leur sont imposées")], "Explained the psychological motivations"),
    ("igor", "On les traite pourtant de barbares.",
     "Yet they are treated as barbarians.",
     [(939, "On les traite de barbares")], "Echoed the common judgment of them"),
    ("lea", "Qui sont les vrais barbares aujourd'hui?",
     "Who are the real barbarians today?",
     [(940, "qui sont les vrais barbares")], "Quoted the film's central moral query"),
    ("igor", "Tu défends ce projet avec beaucoup d'ardeur.",
     "You defend this project with great passion.",
     [(949, "pas été aussi impressionné")], "Acknowledged her passionate advocacy"),
    ("lea", "Je crois vraiment en ce grand film.",
     "I truly believe in this great film.",
     [(932, "il a réussi son pari")], "Reaffirmed her artistic faith"),
    ("igor", "Je suis très impressionné par ton analyse.",
     "I am very impressed by your analysis.",
     [(949, "pas été aussi impressionné"), (950, "profondément en désaccord")], "Paid a sincere compliment to her intellect"),
]

WALK = [
    (0, None,
     "'I read Xavier's screenplay.' Noemie enters the discussion with authority. "
     "The compound past introduces her preparation."),
    (1, None,
     "'It is much too violent and dark.' Igor reiterates his reservations. "
     "The adverbs beaucoup trop emphasize his hesitation."),
    (2, None,
     "'But this violence has a deep meaning.' Noemie counters with artistic conviction. "
     "The adjective profond highlights the script's substance."),
    (3, None,
     "'Why show such cruelty on screen?' Igor questions the creative choice. "
     "The interrogative adverb opens a debate on storytelling."),
    (4, None,
     "'It shows the harshness of that era.' Noemie provides historical context. "
     "The noun 'durete' captures the grim reality."),
    (5, None,
     "'The public risks rejecting this film.' Igor worries about audience reception. "
     "The verb phrase risque de rejeter expresses caution."),
    (6, None,
     "'This is not gratuitous violence.' Noemie defends the screenplay's narrative honesty. "
     "The negative construction dismisses sensationalism."),
    (7, None,
     "'The characters take up arms without hesitating.' Igor points out the drastic actions of the protagonists. "
     "The phrase sans hésiter underscores their resolve."),
    (8, None,
     "'They react to society's constraints.' Noemie explains their underlying oppression. "
     "The noun contraintes identifies the systemic pressure."),
    (9, None,
     "'Yet they are treated as barbarians.' Igor echoes the judgment cast upon them. "
     "The adverb pourtant signals contrast."),
    (10, None,
     "'Who are the real barbarians today?' Noemie delivers the central philosophical question. "
     "The interrogative pronounces the moral theme."),
    (11, None,
     "'You defend this project with great passion.' Igor notes her remarkable conviction. "
     "The prepositional phrase avec beaucoup d'ardeur admires her fervor."),
    (12, None,
     "'I truly believe in this great film.' Noemie reaffirms her confidence. "
     "The adverb vraiment shows complete dedication."),
    (13, None,
     "'I am very impressed by your analysis.' Igor pays tribute to her unexpected insight. "
     "The participle impressionné concludes their debate on high respect."),
]

OUTRO = "Igor and Mathias look at Noemie with newfound respect, struck by her intellectual depth and passion for cinema. When you watch the episode, listen out for the expressions meaning 'read' and 'screenplay'. You'll catch them now. See you next time."
CLOSING = ("igor", "Je suis très impressionné par ton analyse.")
