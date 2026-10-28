# Authoring module for dix-pour-cent s04e01 scene 23 (cues 979-993).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-23.py --out out/dix-pour-cent/s04e01/scene-23.json

ID = "dix-pour-cent-s04e01-scene-23"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 23
TITLE = "Le coup de théâtre  (The Dramatic Twist)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "xavier": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "xavier": "Xavier"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 979-993. Director Xavier Beauvois takes the stage to accept the Cesar for Best Director and makes a stunning "
    "announcement about his next film. Sitting in the audience, Andrea and Gabriel are struck dumb when Xavier reveals "
    "his producer is none other than Mathias Barneville."
)

INTRO = (
    "Director Xavier Beauvois takes the stage to accept the Cesar for Best Director and makes a stunning announcement about his next film. "
    "Sitting in the audience, Andrea and Gabriel are struck dumb when Xavier reveals his producer is none other than Mathias Barneville. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("xavier", "Je partage ce prix avec mon équipe.",
     "I share this prize with my team.",
     [(983, "Je voudrais d'abord partager ce prix avec mon formidable équipe")], "Dedicated his award to the film crew"),
    ("lea", "Xavier Beauvois a remporté le grand prix.",
     "Xavier Beauvois won the big prize.",
     [(984, "C'est mon deuxième César")], "Commented on the prestigious victory"),
    ("gabriel", "Il va présenter son prochain projet ambitieux.",
     "He is going to present his next ambitious project.",
     [(986, "lancer mon prochain projet")], "Anticipated an exciting movie announcement"),
    ("xavier", "Ce projet sera un film totalement fou.",
     "This project will be a totally crazy film.",
     [(987, "un film fou, comme on n'en fait plus")], "Described the unique creative spirit of his film"),
    ("lea", "Il cherche sans doute un producteur solide.",
     "He is probably looking for a solid producer.",
     [(988, "travailler avec un producteur")], "Speculated about the production needs"),
    ("gabriel", "Écoute bien ce qu'il va annoncer.",
     "Listen carefully to what he will announce.",
     [(988, "C'est pourquoi je vais travailler avec un producteur")], "Urged Andrea to focus on the speech"),
    ("xavier", "Je vais travailler avec un producteur fou.",
     "I am going to work with a crazy producer.",
     [(988, "travailler avec un producteur"), (989, "fou")], "Teased his choice of production partner"),
    ("lea", "De qui parle-t-il devant tout le monde?",
     "Whom is he talking about before everyone?",
     [(990, "Où est-il ?")], "Wondered about the unnamed filmmaker"),
    ("xavier", "Mathias Barneville, mon cher ami producteur!",
     "Mathias Barneville, my dear producer friend!",
     [(990, "Mathias Barneville !"), (991, "Mon ami")], "Revealed his new producing partner"),
    ("lea", "Qu'est-ce qu'il vient de dire là?",
     "What did he just say there?",
     [(992, "Qu'est-ce qu'il a dit ?")], "Reacted in sheer shock and confusion"),
    ("gabriel", "Il a prononcé le nom de Mathias!",
     "He spoke the name of Mathias!",
     [(990, "Mathias Barneville !"), (992, "Qu'est-ce qu'il a dit ?")], "Confirmed the astonishing announcement"),
    ("lea", "Mathias a trahi notre accord en secret?",
     "Did Mathias secretly betray our agreement?",
     [(990, "Mathias Barneville !")], "Confronted the reality of betrayal"),
    ("gabriel", "Il s'associe directement avec les réalisateurs.",
     "He partners directly with directors.",
     [(991, "travailler ensemble")], "Analyzed Mathias's aggressive new strategy"),
    ("lea", "Cette trahison change absolument toute la donne.",
     "This betrayal changes the game completely.",
     [(992, "Qu'est-ce qu'il a dit ?")], "Realized the huge stakes for ASK")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'I share this prize with my team.' Xavier Beauvois addresses the hall from the podium. "
     "The present tense verb expresses heartfelt generosity."),
    (1, None,
     "'Xavier Beauvois won the big prize.' Andrea whispers to Gabriel in the auditorium. "
     "The compound past highlights the director's major triumph."),
    (2, None,
     "'He is going to present his next ambitious project.' Gabriel leans forward attentively. "
     "The near future verb introduces the upcoming pitch."),
    (3, None,
     "'This project will be a totally crazy film.' Xavier describes the daring aesthetic of his script. "
     "The simple future promises an unconventional movie."),
    (4, None,
     "'He is probably looking for a solid producer.' Andrea evaluates the financial needs of the project. "
     "The adverbial phrase weighs the business side."),
    (5, None,
     "'Listen carefully to what he will announce.' Gabriel gestures for quiet as the director speaks. "
     "The imperative verb calls for sharp attention."),
    (6, None,
     "'I am going to work with a crazy producer.' Xavier smiles broadly into the spotlights. "
     "The repetitive adjective builds suspense on stage."),
    (7, None,
     "'Whom is he talking about before everyone?' Andrea frowns in growing curiosity. "
     "The interrogative phrase anticipates the dramatic reveal."),
    (8, None,
     "'Mathias Barneville, my dear producer friend!' Xavier calls out the familiar name with enthusiasm. "
     "The affectionate noun phrase stuns the room."),
    (9, None,
     "'What did he just say there?' Andrea gasps in utter astonishment. "
     "The idiom venir de with infinitive conveys her immediate disbelief."),
    (10, None,
     "'He spoke the name of Mathias!' Gabriel turns to her with wide eyes. "
     "The compound past confirms the unexpected bombshell."),
    (11, None,
     "'Did Mathias secretly betray our agreement?' Andrea grasps the full weight of the move. "
     "The adverb en secret underlines the deceit."),
    (12, None,
     "'He partners directly with directors.' Gabriel recognizes the tactical threat to the agency. "
     "The reflexive verb describes his independent venture."),
    (13, None,
     "'This betrayal changes the game completely.' Andrea stares grimly toward the stage. "
     "The colloquial idiom marks a radical shift in power.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Mathias's surprise announcement as an independent producer leaves Andrea and Gabriel reeling. When you watch the episode, listen out for the expressions meaning 'share' and 'prize'. You'll catch them now. See you next time."
CLOSING = ("lea", "Cette trahison change absolument toute la donne.")
