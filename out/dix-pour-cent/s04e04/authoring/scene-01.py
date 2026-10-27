# Authoring module for dix-pour-cent s04e04 scene 01 (cue 1).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-01.py --out out/dix-pour-cent/s04e04/scene-01.json

ID = "dix-pour-cent-s04e04-scene-01"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 1
TITLE = "Félicitations sur scène  (Congratulations on Stage)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sandrine", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = ("Cue 1. Following her theatrical performance, "
               "actress Sandrine Kiberlain receives enthusiastic congratulations backstage from her agent Gabriel.")

INTRO = ("After an acclaimed stage performance in Paris, actress Sandrine Kiberlain takes her curtain call to roaring applause. "
         "Backstage, her devoted talent agent Gabriel rushes to congratulate her on a triumphant evening in the theater. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("gabriel", "Félicitations pour cette belle soirée, Sandrine!",
     "Congratulations on this beautiful evening, Sandrine!",
     [(1, "Félicitations !")], "Gabriel greets Sandrine backstage with warm praise"),
    ("lea", "Merci Gabriel, je suis très émue.",
     "Thank you Gabriel, I am very moved.",
     [], "new: Sandrine catches her breath after the curtain call"),
    ("gabriel", "Le public a adoré la pièce.",
     "The audience loved the play.",
     [], "new: Gabriel describes the enthusiastic theater spectators"),
    ("lea", "C'était une représentation vraiment intense.",
     "It was a truly intense performance.",
     [], "new: Sandrine reflects on the emotional effort of the role"),
    ("gabriel", "Tu as joué avec tant d'énergie!",
     "You acted with so much energy!",
     [], "new: Gabriel commends her vibrant stage presence"),
    ("lea", "La fin de tournée approche déjà.",
     "The end of the tour is already approaching.",
     [], "new: Sandrine notes that their run is ending"),
    ("gabriel", "Demain soir sera la grande dernière.",
     "Tomorrow night will be the big finale.",
     [], "new: Gabriel reminds her of the closing performance"),
    ("lea", "Je ressens une étrange nostalgie.",
     "I feel a strange nostalgia.",
     [], "new: Sandrine admits feeling wistful about the play ending"),
    ("gabriel", "Tout le monde parlera de toi.",
     "Everyone will talk about you.",
     [], "new: Gabriel assures her of widespread critical acclaim"),
    ("lea", "Je suis épuisée mais très heureuse.",
     "I am exhausted but very happy.",
     [], "new: Sandrine balances physical weariness with artistic satisfaction"),
    ("gabriel", "Viens, tes admirateurs attendent aux loges.",
     "Come, your fans are waiting at the dressing rooms.",
     [], "new: Gabriel directs her toward the backstage reception"),
    ("lea", "J'arrive, laissons reposer le plateau.",
     "I am coming, let us let the stage rest.",
     [], "new: Sandrine steps off the stage toward the hallway"),
    ("gabriel", "Un grand bravo pour ton talent.",
     "A big bravo for your talent.",
     [], "new: Gabriel offers heartfelt congratulations once more"),
    ("lea", "Merci pour ton fidèle soutien, Gabriel.",
     "Thank you for your faithful support, Gabriel.",
     [], "new: Sandrine thanks her trusted agent warmly"),
]

OPENER = "Let's explore Gabriel and Sandrine's backstage conversation line by line."

WALK = [
    (0, None,
     "'Congratulations on this beautiful evening, Sandrine!' Gabriel applauds the star actress as she steps off the stage."),
    (1, None,
     "'Thank you Gabriel, I am very moved.' Sandrine shares her deep emotional gratitude with her agent."),
    (2, None,
     "'The audience loved the play.' Gabriel highlights the standing ovation from the packed auditorium."),
    (3, None,
     "'It was a truly intense performance.' Sandrine recalls the demanding energy demanded by her stage lines."),
    (4, None,
     "'You acted with so much energy!' Gabriel praises her expressive and dynamic comedic timing."),
    (5, None,
     "'The end of the tour is already approaching.' Sandrine realizes the long theatrical season is almost over."),
    (6, None,
     "'Tomorrow night will be the big finale.' Gabriel marks the final curtain call scheduled for the next evening."),
    (7, None,
     "'I feel a strange nostalgia.' Sandrine describes the bittersweet emotion of finishing a long-running show."),
    (8, None,
     "'Everyone will talk about you.' Gabriel guarantees that reviews in the Parisian press will be glowing."),
    (9, None,
     "'I am exhausted but very happy.' Sandrine acknowledges her fatigue while savoring the theatrical triumph."),
    (10, None,
     "'Come, your fans are waiting at the dressing rooms.' Gabriel guides the leading lady toward greeting her guests."),
    (11, None,
     "'I am coming, let us let the stage rest.' Sandrine takes a last look back at the quiet empty stage."),
    (12, None,
     "'A big bravo for your talent.' Gabriel reiterates his boundless admiration for her artistic dedication."),
    (13, None,
     "'Thank you for your faithful support, Gabriel.' Sandrine expresses deep appreciation for Gabriel's companionship."),
]

TRANSITION = "Now let's listen to Gabriel and Sandrine's exchange once more from start to finish."

OUTRO = ("Sandrine Kiberlain celebrates the success of her play while looking forward to her next career steps. "
         "Let's review the key theatrical, emotional, and congratulatory vocabulary introduced in this opening scene.")

CLOSING = ("lea", "Le rideau tombe sur ce succès.")
