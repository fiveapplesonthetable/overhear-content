# Authoring module for dix-pour-cent s02e03 scene 10 (cues 242-258).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-10.py --out out/dix-pour-cent/s02e03/scene-10.json

ID = "dix-pour-cent-s02e03-scene-10"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 10
TITLE = "La dispersion  (Overdiversification)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo", "mathias": "marcel"}
LABELS = {"lea": "Sofia", "theo": "Gabriel", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 242-258. In Gabriel's office, Mathias warns Sofia against trying to be both a singer "
               "and an actress, advising strict career focus. Gabriel encourages her versatile talents. "
               "Adapted for A1 French.")

INTRO = ("Inside Gabriel's office, Mathias confronts Sofia about her audition with pop singer Julien Dore. "
         "Mathias insists that novice performers must focus narrowly on acting rather than diluting their image with music. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Qu'est-ce que tu faisais avec Julien Doré?",
  "What were you doing with Julien Dore?",
  [(245, "Qu'est-ce que tu faisais avec Julien Doré ?")], ""),
 ("lea", "Julien cherche une chanteuse pour son film.",
  "Julien is looking for a singer for his film.",
  [(246, "Julien cherche une chanteuse pour son film.")], ""),
 ("mathias", "Tu veux être chanteuse ou actrice?",
  "Do you want to be a singer or an actress?",
  [(247, "Tu veux être chanteuse ou actrice ?")], ""),
 ("lea", "Je veux être actrice, bien sûr.",
  "I want to be an actress, of course.",
  [(248, "Actrice.")], "Expanded to complete sentence"),
 ("theo", "Mais elle chante très bien aussi!",
  "But she sings very well too!",
  [(248, "Mais elle chante aussi.")], "Added très bien"),
 ("lea", "C'est l'occasion de me faire connaître.",
  "It is a chance to get myself known.",
  [(249, "C'est l'occasion de me faire connaître.")], ""),
 ("mathias", "Ou de brouiller les pistes avant de commencer.",
  "Or to muddy the waters before starting.",
  [(250, "Ou de brouiller les pistes")], "Adapted clause"),
 ("mathias", "Ce milieu déteste les gens qui font trop de choses.",
  "This industry hates people who do too many things.",
  [(251, "Ce milieu déteste les gens qui font trop de choses")], ""),
 ("mathias", "Gabriel est amoureux, il te croit capable de tout.",
  "Gabriel is in love, he thinks you are capable of anything.",
  [(252, "Gabriel est amoureux, il te croit capable de tout.")], ""),
 ("mathias", "Soyons réalistes et évitons la dispersion.",
  "Let us be realistic and avoid scattering our efforts.",
  [(253, "Soyons réalistes et évitons la dispersion.")], ""),
 ("mathias", "Concentre-toi uniquement sur le jeu.",
  "Focus solely on acting.",
  [(254, "Concentre-toi sur le jeu.")], "Added uniquement"),
 ("theo", "Mathias est un agent pragmatique qui manque d'imagination.",
  "Mathias is a pragmatic agent who lacks imagination.",
  [(255, "Mathias est un agent pragmatique qui manque d'imagination.")], ""),
 ("theo", "Il est fort avec les contrats, mais il n'a découvert personne.",
  "He is good with contracts, but he has discovered nobody.",
  [(256, "Il est très fort avec les contrats mais il n'a jamais découvert personne.")], ""),
 ("theo", "Alors restons curieux, intelligents, ouverts.",
  "So let us stay curious, intelligent, open.",
  [(257, "Alors restons curieux, intelligents, ouverts")], ""),
 ("theo", "Et voyons ce que Julien a à proposer.",
  "And let us see what Julien has to offer.",
  [(258, "et voyons ce que Julien a à proposer.")], ""),
 ("lea", "D'accord, je vais l'écouter avec attention.",
  "All right, I am going to listen to him with care.",
  [(258, "proposer.")], "Adapted closing reply"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'What were you doing with Julien Dore?' Mathias demands an explanation about the meeting. "
  "The imperfect tense 'faisais' asks about an ongoing past activity."),
 (1, None,
  "'Julien is looking for a singer for his film.' Sofia clarifies the artistic opportunity. "
  "The verb 'chercher' takes a direct object without requiring any preposition."),
 (2, None,
  "'Do you want to be a singer or an actress?' Mathias forces a career choice. "
  "The disjunctive conjunction 'ou' presents two mutually exclusive vocational paths."),
 (3, None,
  "'I want to be an actress, of course.' Sofia affirms her primary dedication. "
  "The adverbial expression 'bien sur' adds confident certainty to her answer."),
 (4, None,
  "'But she sings very well too!' Gabriel enthusiastically praises her dual talent. "
  "The adverb 'aussi' highlights additional artistic capability."),
 (5, None,
  "'It is a chance to get myself known.' Sofia explains her practical promotional motive. "
  "The reflexive causative structure 'se faire connaitre' means to become known."),
 (6, None,
  "'Or to muddy the waters before starting.' Mathias counters with a pragmatic warning. "
  "The idiom 'brouiller les pistes' literally means to confuse the tracks or trail."),
 (7, None,
  "'This industry hates people who do too many things.' Mathias describes industry prejudice. "
  "The noun 'milieu' refers to the film and show business world."),
 (8, None,
  "'Gabriel is in love, he thinks you are capable of anything.' Mathias points out Gabriel's bias. "
  "The adjective 'capable de tout' describes unlimited belief in someone."),
 (9, None,
  "'Let us be realistic and avoid scattering our efforts.' Mathias calls for professional discipline. "
  "The first-person plural imperatives 'soyons' and 'evitons' rally common sense."),
 (10, None,
  "'Focus solely on acting.' Mathias gives direct advice on craft. "
  "The reflexive imperative 'concentre-toi sur' directs attention to dramatic performance."),
 (11, None,
  "'Mathias is a pragmatic agent who lacks imagination.' Gabriel dismisses Mathias's conservative caution. "
  "The relative clause 'qui manque d'imagination' critiques rigid predictability."),
 (12, None,
  "'He is good with contracts, but he has discovered nobody.' Gabriel questions Mathias's creative track record. "
  "The negative pronoun 'personne' follows the compound past auxiliary and participle."),
 (13, None,
  "'So let us stay curious, intelligent, open.' Gabriel champions artistic experimentation. "
  "The series of adjectives 'curieux, intelligents, ouverts' encourages bold exploration."),
 (14, None,
  "'And let us see what Julien has to offer.' Gabriel keeps the creative door open. "
  "The imperative 'voyons ce que' invites examining the upcoming proposal."),
 (15, None,
  "'All right, I am going to listen to him with care.' Sofia agrees to keep an open mind. "
  "The near future 'je vais l'ecouter' expresses immediate intention."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Mathias advocates strict professional focus, while Gabriel champions Sofia's versatile artistic talents. "
         "Sofia decides to hear what Julien Dore has in mind before making up her mind.")
CLOSING = ("theo", "Et voyons ce que Julien a à proposer.")
