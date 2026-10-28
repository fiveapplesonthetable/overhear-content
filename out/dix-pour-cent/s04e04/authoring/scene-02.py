# Authoring module for dix-pour-cent s04e04 scene 02 (cues 2-92).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-02.py --out out/dix-pour-cent/s04e04/scene-02.json

ID = "dix-pour-cent-s04e04-scene-02"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 2
TITLE = "Confidences en coulisses  (Backstage Confidences)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sandrine", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 2-92. In her dressing room and later at a comedy club, "
               "Sandrine expresses deep career frustration and drags Gabriel out for a drink.")

INTRO = ("Surrounded by floral bouquets and gifts in her dressing room, Sandrine Kiberlain admits to feeling artistically restless. "
         "When Gabriel urges her to accept an upcoming prestigious historical biopic, Sandrine insists on escaping to a comedy club, "
         "confiding that she secretly yearns to reinvent herself as a stand-up comedian. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("gabriel", "Toujours merveilleuse, toujours la meilleure, Sandrine!",
     "Always marvelous, always the best, Sandrine!",
     [(7, "Toujours merveilleuse, toujours la meilleure !")], "Gabriel praises Sandrine inside her dressing room"),
    ("lea", "C'est très gentil de ta part.",
     "That is very kind of you.",
     [(8, "C'est très gentil")], "Sandrine smiles modestly while sorting through post-show gifts"),
    ("lea", "Demain, c'est la dernière de Barillet.",
     "Tomorrow is the final performance of Barillet.",
     [(16, "Demain, c'est la dernière.")], "Sandrine remarks on the end of the theatrical run"),
    ("gabriel", "Alors, qu'est-ce qu'on fait maintenant?",
     "So, what do we do now?",
     [(38, "qu'est-ce qu'on fait maintenant ?")], "Gabriel brings up the immediate future schedule"),
    ("gabriel", "Maintenant, nous préparons le prochain film.",
     "Now, we prepare the next movie.",
     [(39, "Maintenant on fait le film")], "Gabriel suggests focusing on their major film contract"),
    ("gabriel", "C'est le biopic sur la Comtesse.",
     "It is the biopic on the Countess.",
     [(39, "La Comtesse")], "Gabriel reminds her of Daniele Thompson's upcoming project"),
    ("lea", "Je parle de là, maintenant, sortons!",
     "I am talking about right now, let us go out!",
     [(40, "Je parle de là, maintenant. On sort ?")], "Sandrine declines business talk and urges an evening out"),
    ("gabriel", "Mais il faut parler du film.",
     "But we must discuss the movie.",
     [(42, "il faut qu'on parle du film.")], "Gabriel stresses the urgency of giving producers an answer"),
    ("lea", "Tu n'as rien de mieux?",
     "Do you have nothing better?",
     [(44, "tu ne pouvais pas trouver mieux pour moi")], "Sandrine expresses boredom with another costume drama"),
    ("gabriel", "Les producteurs veulent une réponse rapide.",
     "The producers want a quick answer.",
     [], "new: Gabriel warns her about the production deadline"),
    ("lea", "Allons plutôt dans un club comique.",
     "Let us go instead to a comedy club.",
     [], "new: Sandrine suggests exploring the Parisian stand-up scene"),
    ("gabriel", "D'accord, mais restons très raisonnables ce soir.",
     "All right, but let us stay very sensible tonight.",
     [], "new: Gabriel relents to her spontaneous suggestion"),
    ("lea", "J'ai complètement raté ma carrière comique!",
     "I have completely missed out on my comedic career!",
     [(92, "j'ai complètement raté ma carrière.")], "Sandrine watches the young comics with envious admiration"),
    ("gabriel", "Tu es une immense comédienne, Sandrine.",
     "You are an immense actress, Sandrine.",
     [], "new: Gabriel reaffirms his absolute faith in her versatile talent"),
]

OPENER = "Let's explore Sandrine and Gabriel's intimate conversation line by line."

WALK = [
    (0, None,
     "'Always marvelous, always the best, Sandrine!' Gabriel showers the actress with affectionate compliments in her dressing room. The adjective meaning 'marvelous' takes its feminine form here to match the noun it describes."),
    (1, None,
     "'That is very kind of you.' Sandrine responds with gentle humor to Gabriel's unreserved flattery. The informal 'you' form around 'part' marks a direct, personal relationship."),
    (2, None,
     "'Tomorrow is the final performance of Barillet.' Sandrine notes that the long stage engagement is drawing to a close. The adjective meaning 'final' takes its feminine form here to match the noun it describes."),
    (3, None,
     "'So, what do we do now?' Gabriel turns the conversation toward their subsequent professional commitments. The clause hinges on the everyday verb meaning 'do'."),
    (4, None,
     "'Now, we prepare the next movie.' Gabriel underscores the importance of transitioning promptly from stage to screen. The descriptive adjective for 'next' agrees in gender and number with its noun."),
    (5, None,
     "'It is the biopic on the Countess.' Gabriel points to the prestigious period piece awaiting her signature. The key noun here means 'biopic', anchored by its matching French article."),
    (6, None,
     "'I am talking about right now, let us go out!' Sandrine brushes aside serious career planning in favor of immediate fun. The clause hinges on the everyday verb meaning 'am talking'."),
    (7, None,
     "'But we must discuss the movie.' Gabriel insists that the filmmakers need an official confirmation. Notice how 'is necessary' leads directly into the noun meaning 'movie'."),
    (8, None,
     "'Do you have nothing better?' Sandrine laments that conventional biopics feel uninspired and stale. In everyday spoken French, rising intonation on 'have' at the end is enough to turn the sentence into a question."),
    (9, None,
     "'The producers want a quick answer.' Gabriel reminds her that financiers cannot hold production schedules indefinitely. Notice how 'want' leads directly into the noun meaning 'producers'."),
    (10, None,
     "'Let us go instead to a comedy club.' Sandrine pushes Gabriel toward discovering fresh comedic talent. The descriptive adjective for 'comedic' agrees in gender and number with its noun."),
    (11, None,
     "'All right, but let us stay very sensible tonight.' Gabriel agrees to accompany her while urging moderation. The verb meaning 'let us remain' pairs naturally with the noun for 'agreement' in everyday conversation."),
    (12, None,
     "'I have completely missed out on my comedic career!' Sandrine confesses her secret longing to perform raw stand-up comedy. This conversational past tense combines a helper verb with the past participle for 'missed out on'."),
    (13, None,
     "'You are an immense actress, Sandrine.' Gabriel reassures her that her theatrical stature remains beyond question. The informal 'you' form around 'actress' marks a direct, personal relationship."),
]

TRANSITION = "Now let's listen to Sandrine and Gabriel's full discussion once more from start to finish."

OUTRO = ("Sandrine Kiberlain reveals her unexpected passion for comedic experimentation, leaving Gabriel facing a tricky negotiation. "
         "Let's review the key vocabulary of cinema, comedy, and artistic ambitions from this scene.")

CLOSING = ("lea", "J'ai envie de nouveauté.")
