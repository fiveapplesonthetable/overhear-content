# Authoring module for dix-pour-cent s04e03 scene 06 (cues 195-202).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-06.py --out out/dix-pour-cent/s04e03/scene-06.json

ID = "dix-pour-cent-s04e03-scene-06"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 6
TITLE = "L'ennemie dans nos murs  (The Enemy in Our Walls)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Camille", "herve": "Hervé", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 195-202. Panic spreads through ASK reception as star competitor Elise Formain "
               "strides into the building, raising alarm over a potential hostile takeover.")

INTRO = ("At ASK reception, Camille and Herve spot rival super-agent Elise Formain striding through the lobby. "
         "Fearing an aggressive buyout by competitor StarMedia, they alert Gabriel as tension peaks. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Qui est cette femme élégante à l'accueil?",
     "Who is this elegant woman at reception?",
     [(196, "C'est qui ?")], "Camille spots an imposing stranger in the foyer"),
    ("herve", "Tu ne connais pas Élise Formain?",
     "You do not know Elise Formain?",
     [(197, "Vous ne connaissez pas Elise Formain ?")], "Herve expresses disbelief at her question"),
    ("herve", "C'est la plus grande agente de StarMédia!",
     "She is the biggest agent of StarMedia!",
     [(198, "La plus grande agent de StarMédia.")], "Herve identifies their foremost rival"),
    ("herve", "Elle nous a pris nos meilleurs clients!",
     "She took our best clients from us!",
     [(199, "soufflé")], "Herve recalls past poachings with bitterness"),
    ("lea", "Nathalie Baye et Dany Boon, c'est elle?",
     "Nathalie Baye and Dany Boon, that is her?",
     [(199, "Nathalie Baye et Dany Boon.")], "Camille connects the name to recent high-profile departures"),
    ("herve", "Oui, elle nous a tout soufflé sans pitié!",
     "Yes, she snatched everything from us without mercy!",
     [(199, "Elle nous a soufflé Nathalie Baye")], "Herve stresses her ruthless effectiveness"),
    ("lea", "Que fait-elle ici dans notre agence?",
     "What is she doing here in our agency?",
     [(200, "Qu'est-ce qu'elle fait là ?")], "Camille wonders about the purpose of her visit"),
    ("herve", "StarMédia veut peut-être nous racheter?",
     "Does StarMedia perhaps want to buy us out?",
     [(201, "StarMédia va racheter ASK ?")], "Herve voices the terrifying rumor of a hostile buyout"),
    ("lea", "Ce serait une catastrophe pour nous tous!",
     "That would be a catastrophe for all of us!",
     [(201, "racheter ASK ?")], "Camille reacts with alarm at the prospect of a corporate takeover"),
    ("gabriel", "Gabriel arrive enfin, viens vite voir!",
     "Gabriel is finally arriving, come see quickly!",
     [(202, "Gabriel !")], "Herve flags down Gabriel in the hallway"),
    ("gabriel", "Qu'est-ce qui se passe ici, les amis?",
     "What is happening here, friends?",
     [(202, "Gabriel !")], "Gabriel asks why the assistants are whispering in agitation"),
    ("herve", "Regarde dans le couloir, Élise Formain approche!",
     "Look in the hallway, Elise Formain is approaching!",
     [(200, "Qu'est-ce qu'elle fait là ?")], "Herve points toward the approaching executive"),
    ("gabriel", "Mon Dieu, que vient faire cette concurrente?",
     "My God, what is this competitor coming to do?",
     [(201, "StarMédia va racheter ASK ?")], "Gabriel gasps as he realizes who has entered the premises"),
]

OPENER = "Let's explore Camille, Herve, and Gabriel's panicked discovery line by line."

WALK = [
    (0, None,
     "'Who is this elegant woman at reception?' Camille asks about the sophisticated newcomer walking past the front desk. The adjective meaning 'elegant' takes its feminine form here to match the noun it describes."),
    (1, None,
     "'You do not know Elise Formain?' Herve is shocked that Camille does not recognize Paris's most ruthless agent. Notice the classic French sandwich negation wrapping right around 'know'."),
    (2, None,
     "'She is the biggest agent of StarMedia!' Herve explains that Elise is the leading power player at their rival company. Dropping the subject pronoun turns the verb for 'she is' into a direct, punchy command."),
    (3, None,
     "'She took our best clients from us!' Herve reminds Camille of the severe talent losses ASK has suffered recently. Notice how 'has' leads directly into the noun meaning 'clients!'."),
    (4, None,
     "'Nathalie Baye and Dany Boon, that is her?' Camille realizes Elise orchestrated those major defections. In everyday spoken French, rising intonation on 'it is' at the end is enough to turn the sentence into a question."),
    (5, None,
     "'Yes, she snatched everything from us without mercy!' Herve underscores Elise's predatory deal-making skills. Dropping the subject pronoun turns the verb for 'has' into a direct, punchy command."),
    (6, None,
     "'What is she doing here in our agency?' Camille questions why their fierce rival would set foot in their building. Inverting the verb and pronoun around 'is she doing' creates a crisp, polished question."),
    (7, None,
     "'Does StarMedia perhaps want to buy us out?' Herve dreads that StarMedia is preparing a full buyout of ASK. The clause hinges on the everyday verb meaning 'wants'."),
    (8, None,
     "'That would be a catastrophe for all of us!' Camille shares her fear of being swallowed by corporate competitors. Notice how 'would be' leads directly into the noun meaning 'catastrophe'."),
    (9, None,
     "'Gabriel is finally arriving, come see quickly!' Herve calls Gabriel over to witness the situation. The clause hinges on the everyday verb meaning 'arrives'."),
    (10, None,
     "'What is happening here, friends?' Gabriel asks what has caused such sudden panic near reception. The verb meaning 'happens' pairs naturally with the noun for 'friends?' in everyday conversation."),
    (11, None,
     "'Look in the hallway, Elise Formain is approaching!' Herve directs Gabriel's attention to the corridor. Notice how 'look' leads directly into the noun meaning 'hallway'."),
    (12, None,
     "'My God, what is this competitor coming to do?' Gabriel stares in astonishment at their rival's bold entrance. In everyday spoken French, rising intonation on 'comes' at the end is enough to turn the sentence into a question."),
]

TRANSITION = "Now let's listen to the assistants' alert once more from start to finish."

OUTRO = ("The unexpected arrival of Elise Formain sends shockwaves through the ASK agency corridors. "
         "Let's review the key agency competition terms from this scene.")

CLOSING = ("gabriel", "Mon Dieu, que vient faire cette concurrente?")
