# Authoring module for dix-pour-cent s02e04 scene 14 (cues 374-394).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s02e04/authoring/scene-14.py --out overhear-content/out/dix-pour-cent/s02e04/scene-14.json

ID = "dix-pour-cent-s02e04-scene-14"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 14
TITLE = "L'interview à la radio  (Radio Interview)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sacha": "theo", "animateur": "marcel"}
LABELS = {"lea": "Camille", "sacha": "Sacha", "animateur": "L'animateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 374-394. Controversial German-French director Sacha Hartman finishes a lively radio interview "
    "about his award-winning film and prepares to leave with Camille."
)

INTRO = (
    "At a major Paris radio station, acclaimed director Sacha Hartman gives a live broadcast interview about his provocative film. "
    "Camille waits patiently in the sound booth to escort the guest director back to the agency. "
    "Listen to the scene in French first."
)

STORY = [
    ("animateur", "Bonjour, Sacha Hartman.",
     "Hello, Sacha Hartman.",
     [(374, "Bonjour, Sacha Hartman")], ""),
    ("animateur", "Merci d'être avec nous.",
     "Thank you for being with us.",
     [(375, "Merci d'être avec nous")], ""),
    ("animateur", "Vous parlez un français parfait.",
     "You speak perfect French.",
     [(375, "Vous parlez un français parfait")], ""),
    ("sacha", "J'ai fréquenté l'école française à Berlin.",
     "I attended the French school in Berlin.",
     [(376, "J'ai fréquenté l'école française à Berlin")], ""),
    ("sacha", "Mes parents ont toujours aimé la France.",
     "My parents have always loved France.",
     [(377, "Mes parents ont toujours aimé la France")], ""),
    ("animateur", "Votre premier film a remporté un prix.",
     "Your first movie won a prize.",
     [(379, "Votre premier film")], ""),
    ("animateur", "La Palme d'Or à Cannes!",
     "The Palme d'Or at Cannes!",
     [(379, "la Palme d'Or à Cannes")], ""),
    ("animateur", "Une association cherche à faire interdire votre film.",
     "An association is trying to ban your film.",
     [(380, "cherche à faire interdire")], ""),
    ("animateur", "Comment réagissez-vous à ces attaques?",
     "How do you react to these attacks?",
     [(381, "Comment réagissez-vous")], ""),
    ("sacha", "Je ne veux pas leur offrir une tribune.",
     "I do not want to give them a platform.",
     [(383, "je ne veux pas leur offrir une tribune")], ""),
    ("sacha", "Ni leur accorder la moindre attention.",
     "Nor give them the slightest attention.",
     [(384, "Ni même leur accorder la moindre attention")], ""),
    ("sacha", "Ils appartiennent à l'ancien monde.",
     "They belong to the old world.",
     [(386, "Ils appartiennent à l'ancien monde")], ""),
    ("lea", "L'interview est terminée, Sacha.",
     "The interview is over, Sacha.",
     [(394, "On y va")], "adapted for studio exit"),
    ("lea", "Nous devons y aller maintenant.",
     "We must go now.",
     [(394, "On y va")], ""),
    ("sacha", "D'accord, je te suis.",
     "All right, I am following you.",
     [(394, "On y va")], "closing agreement")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Hello, Sacha Hartman.' The radio presenter introduces the celebrated guest. "
     "The formal greeting addresses the visiting filmmaker directly."),
    (1, None,
     "'Thank you for being with us.' The polite opening welcomes him to the studio broadcast. "
     "The prepositional phrase uses an infinitive of state."),
    (2, None,
     "'You speak perfect French.' The host compliments the visiting director's fluency. "
     "The adjective follows the masculine language noun."),
    (3, None,
     "'I attended the French school in Berlin.' Sacha explains his early language immersion. "
     "The compound past verb governs the direct object school."),
    (4, None,
     "'My parents have always loved France.' He attributes his bilingualism to family ties. "
     "The plural possessive introduces maternal and paternal affinity."),
    (5, None,
     "'Your first movie won a prize.' The journalist recalls his striking artistic debut. "
     "The ordinal adjective precedes the masculine noun."),
    (6, None,
     "'The Palme d'Or at Cannes!' The host highlights the highest festival accolade. "
     "The prestigious festival prize carries international prestige."),
    (7, None,
     "'An association is trying to ban your film.' The question addresses conservative censorship. "
     "The semi-auxiliary construction indicates active attempts to suppress."),
    (8, None,
     "'How do you react to these attacks?' The host invites his comment on public controversy. "
     "The interrogative adverb structures an inquiry into feelings."),
    (9, None,
     "'I do not want to give them a platform.' Sacha refuses to amplify his loudest critics. "
     "The negative auxiliary governs an infinitive with indirect object pronoun."),
    (10, None,
     "'Nor give them the slightest attention.' He dismisses the protesters entirely. "
     "The negative coordinating conjunction reinforces total indifference."),
    (11, None,
     "'They belong to the old world.' The filmmaker views the opposition as outdated reactionaries. "
     "The third-person plural verb signifies cultural divergence."),
    (12, None,
     "'The interview is over, Sacha.' Camille signals that their broadcast segment has wrapped up. "
     "The feminine past participle indicates completion of work."),
    (13, None,
     "'We must go now.' Camille urges him toward the door before crowds gather. "
     "The modal verb devoir indicates practical urgency to depart."),
    (14, None,
     "'All right, I am following you.' Sacha calmly prepares to leave the premises. "
     "The present-tense verb follows the agreement formula.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "As Sacha Hartman wraps up his defiant interview, Camille must quickly guide him outside through brewing street protests. "
    "Listen to the entire scene once more in French."
)

CLOSING = ("sacha", "Où est notre voiture?")
