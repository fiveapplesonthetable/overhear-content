# Authoring module for dix-pour-cent s04e04 scene 19 (cues 1034-1143).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-19.py --out out/dix-pour-cent/s04e04/scene-19.json

ID = "dix-pour-cent-s04e04-scene-19"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 19
TITLE = "Le désastre du stand-up  (The Stand-Up Disaster)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sandrine", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1034-1143. Paralyzed by stage fright before performing stand-up comedy, Sandrine Kiberlain takes "
    "the stage and bombs with absurd jokes about vegetables. Backstage, she furiously blames Gabriel for pushing "
    "her into comedy and forces him to sign her up for her beloved costume drama."
)

INTRO = (
    "At a Parisian comedy club, Sandrine Kiberlain endures a catastrophic stand-up performance before an unimpressed crowd. "
    "Retreating backstage to the bar with Gabriel, Sandrine unleashes her fury, holding her agent entirely responsible for the fiasco. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "J'ai un trac fou ce soir.",
     "I have crazy stage fright tonight.",
     [(1045, "Je n'arrive pas à respirer"), (1061, "Pas trop le trac ?")], "Expressed extreme backstage anxiety"),
    ("gabriel", "Respire, le public va t'adorer.",
     "Breathe, the audience will love you.",
     [(1048, "On peut annuler")], "Offered reassuring encouragement"),
    ("lea", "Mes blagues sur les légumes étaient nulles!",
     "My jokes about vegetables were terrible!",
     [(1081, "les légumes d'autrefois"), (1094, "Je pensais au rutabaga")], "Admitted her stand-up set was awful"),
    ("gabriel", "C'était ta toute première scène.",
     "It was your very first stage.",
     [(1068, "C'est sa première fois")], "Reminded her that comedy takes practice"),
    ("lea", "Personne n'a ri dans la salle.",
     "Nobody laughed in the room.",
     [(1089, "Quittez la scène")], "Lamented the total lack of laughs"),
    ("gabriel", "Tu as fait preuve de grand courage.",
     "You showed great courage.",
     [(1113, "Il y avait une énergie")], "Praised her bravery in stepping up"),
    ("lea", "C'est entièrement de ta faute, Gabriel!",
     "It is entirely your fault, Gabriel!",
     [(1118, "c'est sa faute")], "Turned her frustration directly onto her agent"),
    ("gabriel", "Pourquoi m'accuses-tu de cet échec?",
     "Why do you accuse me of this failure?",
     [(1117, "Pardon ?")], "Defended himself against her blame"),
    ("lea", "Tu as insisté pour ce spectacle.",
     "You insisted on this show.",
     [(1118, "Il a insisté pour que je fasse")], "Reminded him who pushed her into comedy"),
    ("gabriel", "Je voulais juste élargir tes horizons.",
     "I just wanted to broaden your horizons.",
     [(1122, "Beaucoup d'actrices se lancent")], "Explained his well-meaning intentions"),
    ("lea", "Je veux faire ce film en costumes!",
     "I want to do this costume film!",
     [(1126, "faire ce film en costumes")], "Demanded her preferred historical drama role"),
    ("gabriel", "D'accord, tu as gagné, Sandrine.",
     "All right, you won, Sandrine.",
     [(1130, "Tu gagnes. Voilà !")], "Conceded defeat to his star client"),
    ("lea", "Tu promets de signer ce contrat?",
     "Do you promise to sign this contract?",
     [(1131, "Faisons La Comtesse de Ségur")], "Sought a definitive commitment"),
    ("gabriel", "Je t'appelle le producteur dès demain.",
     "I will call the producer for you tomorrow.",
     [(1131, "Faisons La Comtesse")], "Agreed to finalize the period movie deal"),
]

WALK = [
    (0, None,
     "'I have crazy stage fright tonight.' Sandrine shivers backstage before going on. "
     "The idiomatic noun phrase un trac fou conveys acute performance anxiety."),
    (1, None,
     "'Breathe, the audience will love you.' Gabriel tries to calm her nerves. "
     "The imperative verb respire encourages steady composure."),
    (2, None,
     "'My jokes about vegetables were terrible!' Sandrine groans after coming off stage. "
     "The adjective nulles reflects her harsh self-assessment."),
    (3, None,
     "'It was your very first stage.' Gabriel puts the rocky debut in perspective. "
     "The adjective phrase toute première softens the blow."),
    (4, None,
     "'Nobody laughed in the room.' Sandrine recalls the icy silence of the club. "
     "The negative pronoun personne underscores the absence of humor."),
    (5, None,
     "'You showed great courage.' Gabriel praises her daring attempt at stand-up. "
     "The expression faire preuve de acknowledges genuine bravery."),
    (6, None,
     "'It is entirely your fault, Gabriel!' Sandrine directs her frustration at her agent. "
     "The adverb entièrement places full blame on him."),
    (7, None,
     "'Why do you accuse me of this failure?' Gabriel protests her sudden hostility. "
     "The interrogative verb phrase m'accuses-tu questions her reaction."),
    (8, None,
     "'You insisted on this show.' Sandrine reminds him who orchestrated the comedy booking. "
     "The compound past verb insisté recalls his pressure."),
    (9, None,
     "'I just wanted to broaden your horizons.' Gabriel explains his artistic motives. "
     "The infinitive phrase élargir tes horizons justifies his advice."),
    (10, None,
     "'I want to do this costume film!' Sandrine states her true artistic desire. "
     "The noun phrase en costumes specifies the period genre."),
    (11, None,
     "'All right, you won, Sandrine.' Gabriel surrenders to her demand. "
     "The compound past verb as gagné signals his concession."),
    (12, None,
     "'Do you promise to sign this contract?' Sandrine secures her victory. "
     "The present verb promets demands immediate confirmation."),
    (13, None,
     "'I will call the producer for you tomorrow.' Gabriel pledges to close the deal. "
     "The temporal phrase dès demain guarantees prompt action."),
]

OUTRO = "Sandrine sips her drink with a triumphant smile, while Gabriel accepts that some actors are meant for drama. When you watch the episode, listen out for the expressions meaning 'stage fright' and 'crazy'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "Je t'appelle le producteur dès demain.")
