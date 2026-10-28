# Authoring module for dix-pour-cent s04e03 scene 07 (cues 203-239).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e03/authoring/scene-07.py --out out/dix-pour-cent/s04e03/scene-07.json

ID = "dix-pour-cent-s04e03-scene-07"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 3
SCENE = 7
TITLE = "L'arrivée d'Élise  (Élise's Arrival)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E03"
SOURCE_FILE = "sources/dix-pour-cent/s04/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 203-239. In the boardroom, Hicham reveals that rival super-agent Elise Formain "
               "is joining ASK with her entire client list, forcing a desperate partners' vote to stave off bankruptcy.")

INTRO = ("Behind closed doors at ASK, Andrea confronts Hicham about Elise Formain's presence in the building. "
         "Hicham reveals that Elise is joining the agency with her roster, forcing a high-stakes partners' vote. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Que fait Élise Formain dans nos bureaux?",
     "What is Elise Formain doing in our offices?",
     [(204, "Qu'est-ce qu'Elise Formain fait ici ?")], "Andrea demands an immediate explanation"),
    ("lea", "Fermez la porte avant cette réunion urgente.",
     "Close the door before this urgent meeting.",
     [(205, "La porte, s'il vous plaît.")], "Andrea insists on total privacy"),
    ("gabriel", "StarMédia essaie-t-il de racheter notre agence?",
     "Is StarMedia trying to buy out our agency?",
     [(214, "racheter ASK.")], "Gabriel voices fears of a takeover"),
    ("hicham", "Personne ne nous rachète, nous la recrutons!",
     "Nobody is buying us, we are hiring her!",
     [(215, "On recrute.")], "Hicham announces a startling reversal of expectations"),
    ("hicham", "Élise Formain nous rejoint avec ses clients.",
     "Elise Formain is joining us with her clients.",
     [(216, "Elise Formain nous rejoint chez ASK.")], "Hicham confirms the recruitment package"),
    ("lea", "C'est une mauvaise blague, j'espère?",
     "This is a bad joke, I hope?",
     [(218, "C'est une plaisanterie ?")], "Andrea expresses disbelief at the plan"),
    ("lea", "Cette femme est un monstre sans scrupules!",
     "This woman is a monster without scruples!",
     [(226, "ce n'est pas un monstre")], "Andrea denounces Elise's ruthless methods"),
    ("gabriel", "Elle possède pourtant un portefeuille de stars impressionnant.",
     "She possesses an impressive portfolio of stars though.",
     [(221, "portefeuille de clients impressionnant")], "Gabriel points out the commercial advantages"),
    ("hicham", "Je n'ai plus aucune trésorerie disponible.",
     "I have no available cash left.",
     [(232, "liquidité disponible.")], "Hicham lays bare the financial crisis facing the agency"),
    ("hicham", "Sans elle, notre agence est ruinée.",
     "Without her, our agency is ruined.",
     [(233, "c'est terminé.")], "Hicham presents the stark reality of bankruptcy"),
    ("lea", "Il faut voter entre associés maintenant.",
     "We must vote between partners now.",
     [(228, "Et si on votait ?")], "Andrea calls for a democratic ballot"),
    ("hicham", "Qui vote pour sauver nos emplois?",
     "Who votes to save our jobs?",
     [(238, "payer le loyer, les salaires")], "Hicham frames the vote as survival"),
    ("gabriel", "Je vote pour accueillir Élise chez nous.",
     "I vote to welcome Elise into our firm.",
     [(237, "Qui est pour recruter Elise")], "Gabriel casts a decisive pragmatic ballot"),
]

OPENER = "Let's explore Andrea, Hicham, and Gabriel's tense boardroom confrontation line by line."

WALK = [
    (0, None,
     "'What is Elise Formain doing in our offices?' Andrea asks angrily why their fiercest competitor has appeared. The verb meaning 'is doing' pairs naturally with the noun for 'offices?' in everyday conversation."),
    (1, None,
     "'Close the door before this urgent meeting.' Andrea orders the boardroom doors shut to avoid office eavesdropping. Notice how 'close' leads directly into the noun meaning 'door'."),
    (2, None,
     "'Is StarMedia trying to buy out our agency?' Gabriel questions whether StarMedia intends to swallow ASK whole. Inverting the verb and pronoun around 'is it trying' creates a crisp, polished question."),
    (3, None,
     "'Nobody is buying us, we are hiring her!' Hicham shocks the agents by stating that ASK is hiring Elise instead. The two-part French negation brackets the verb for 'buys out' on both sides."),
    (4, None,
     "'Elise Formain is joining us with her clients.' Hicham explains that her lucrative client roster comes along with her. Notice how 'is joining' leads directly into the noun meaning 'clients.'."),
    (5, None,
     "'This is a bad joke, I hope?' Andrea reacts with disgust, refusing to believe Hicham's announcement. Notice how the short vowel drops before a vowel sound around 'it is', making the phrase flow smoothly as one unit."),
    (6, None,
     "'This woman is a monster without scruples!' Andrea warns that Elise represents everything toxic in talent representation. The key noun here means 'woman', anchored by its matching French article."),
    (7, None,
     "'She possesses an impressive portfolio of stars though.' Gabriel weighs the indisputable revenue her star clients bring. Notice how 'possesses' leads directly into the noun meaning 'portfolio'."),
    (8, None,
     "'I have no available cash left.' Hicham bluntly confesses that the agency's bank reserves are entirely depleted. Notice the classic French sandwich negation wrapping right around 'have'."),
    (9, None,
     "'Without her, our agency is ruined.' Hicham makes it clear that without Elise's revenues, ASK will collapse. The verb meaning 'ruined.' pairs naturally with the noun for 'agency' in everyday conversation."),
    (10, None,
     "'We must vote between partners now.' Andrea insists that the managing partners must decide together by formal vote. Notice how 'is necessary' leads directly into the noun meaning 'partners'."),
    (11, None,
     "'Who votes to save our jobs?' Hicham asks who is prepared to vote for survival over personal pride. In everyday spoken French, rising intonation on 'votes' at the end is enough to turn the sentence into a question."),
    (12, None,
     "'I vote to welcome Elise into our firm.' Gabriel reluctantly votes yes to protect the company's financial future. The clause hinges on the everyday verb meaning 'vote'."),
]

TRANSITION = "Now let's listen to the partners' crucial vote once more from start to finish."

OUTRO = ("The ASK partners make a reluctant choice to recruit their fiercest rival to rescue the agency from ruin. "
         "Let's review the key boardroom and voting vocabulary from this scene.")

CLOSING = ("gabriel", "Je vote pour accueillir Élise chez nous.")
