# Authoring module for dix-pour-cent s04e01 scene 07 (cues 487-505).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-07.py --out out/dix-pour-cent/s04e01/scene-07.json

ID = "dix-pour-cent-s04e01-scene-07"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 7
TITLE = "Le départ de Noémie  (Noémie's Departure)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie", "herve": "theo"}
LABELS = {"lea": "Camille", "noemie": "Noémie", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 487-505. Noemie prepares to leave ASK alongside Mathias, giving Herve her bonsai tree "
               "and making plans for a private farewell drink with Camille and Herve.")

INTRO = ("At the ASK agency reception, Noemie packs up her belongings following Mathias's departure. "
         "She entrusts her cherished bonsai tree to Herve and makes plans with the assistants for a friendly farewell drink. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Ça va Noémie? Tu as besoin d'aide?",
     "Are you okay Noemie? Do you need help?",
     [(487, "Ça va ?"), (489, "Je t'appelle un taxi ?")], "Camille checks on Noemie carrying her boxes"),
    ("noemie", "Non, ça ira très bien, merci Camille.",
     "No, I will be fine, thank you Camille.",
     [(490, "Non, ça ira, merci.")], "Noemie declines politely and manages her things"),
    ("herve", "Tu pars déjà avec tes cartons?",
     "Are you leaving already with your boxes?",
     [(491, "Oh, Hervé !")], "Herve arrives as Noemie prepares to step out"),
    ("noemie", "Hervé, j'ai mis le bonsaï sur ton bureau.",
     "Herve, I put the bonsai on your desk.",
     [(492, "J'ai mis le bonsaï sur ton bureau.")], "Noemie entrusts her plant to Herve"),
    ("noemie", "Je sais que tu en prendras grand soin.",
     "I know that you will take great care of it.",
     [(493, "Je suis sûr que tu en prendras bien soin.")], "Noemie places her trust in Herve's gentle nature"),
    ("herve", "Je vais l'arroser tous les jours.",
     "I am going to water it every day.",
     [(493, "bien soin")], "Herve promises to nurture the keepsake"),
    ("noemie", "Je ne pouvais pas partir sans vous saluer.",
     "I could not leave without greeting you.",
     [(495, "Je pouvais quand même pas partir sans dire au revoir, non ?")], "Noemie insists on a proper send-off with friends"),
    ("noemie", "Nous ne sommes pas des sauvages!",
     "We are not savages!",
     [(496, "On n'est pas des sauvages après tout.")], "Noemie jokes about workplace civility"),
    ("noemie", "J'espère que vous allez vous ennuyer sans moi.",
     "I hope that you will be bored without me.",
     [(497, "J'espère que vous allez vous ennuyer sans moi.")], "Noemie teases her fellow assistants affectionately"),
    ("herve", "Tu peux compter sur nous pour ça!",
     "You can count on us for that!",
     [(498, "Tu peux compter sur nous.")], "Herve reassures her of their lasting affection"),
    ("lea", "On pourrait prendre un verre ensemble ce soir?",
     "We could have a drink together tonight?",
     [(500, "On pourrait peut-être prendre un verre tout à l'heure ?")], "Camille suggests meeting outside the agency"),
    ("noemie", "Oui, un pot de départ entre nous!",
     "Yes, a farewell drink just between us!",
     [(502, "Genre un pot de départ rien qu'entre nous.")], "Noemie welcomes an intimate reunion"),
    ("herve", "C'est parfait, sans les patrons pénibles!",
     "That is perfect, without the annoying bosses!",
     [(503, "Sans les trucs pénibles.")], "Herve looks forward to relaxing without office politics"),
]

OPENER = "Let's explore Noemie's warm farewell with Camille and Herve line by line."

WALK = [
    (0, None,
     "'Are you okay Noemie? Do you need help?' Camille kindly asks if Noemie requires any assistance with her belongings. The informal 'you' form around 'goes' marks a direct, personal relationship."),
    (1, None,
     "'No, I will be fine, thank you Camille.' Noemie thanks Camille warmly while managing her boxes alone. The verb meaning 'will go' pairs naturally with the noun for 'thank you' in everyday conversation."),
    (2, None,
     "'Are you leaving already with your boxes?' Herve spots Noemie with her packed items in the hallway. Herve uses the casual singular 'you' with 'are leaving', showing close familiarity."),
    (3, None,
     "'Herve, I put the bonsai on your desk.' Noemie explains that she left a small desk plant as a parting gift. Notice how the short vowel drops before a vowel sound around 'I have', making the phrase flow smoothly as one unit."),
    (4, None,
     "'I know that you will take great care of it.' Noemie expresses full confidence in Herve's attentiveness. Notice how 'know' leads directly into the noun meaning 'care.'."),
    (5, None,
     "'I am going to water it every day.' Herve promises faithful dedication to keeping the plant alive. In spoken French, the little word before 'am going' drops its final vowel and attaches with an apostrophe."),
    (6, None,
     "'I could not leave without greeting you.' Noemie explains why she wanted to bid personal farewells to her friends. Notice the classic French sandwich negation wrapping right around 'could'."),
    (7, None,
     "'We are not savages!' Noemie quips that they have always shared real human warmth despite office rivalries. The key noun here means 'savages!', anchored by its matching French article."),
    (8, None,
     "'I hope that you will be bored without me.' Noemie playfully suggests the agency will lose its spark without her. The formal 'you' pronoun sets a courteous, professional distance around 'I hope'."),
    (9, None,
     "'You can count on us for that!' Herve jokes back that they will miss her presence dearly. The informal 'you' form around 'can' marks a direct, personal relationship."),
    (10, None,
     "'We could have a drink together tonight?' Camille invites Noemie to share a drink after working hours. Notice how 'could' leads directly into the noun meaning 'drink'."),
    (11, None,
     "'Yes, a farewell drink just between us!' Noemie eagerly embraces the proposal for an assistants' gathering. The key noun here means 'drink', anchored by its matching French article."),
    (12, None,
     "'That is perfect, without the annoying bosses!' Herve celebrates the idea of an evening free from agency drama. In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe."),
]

TRANSITION = "Now let's listen to the assistants' farewell exchange once more from start to finish."

OUTRO = ("Noemie says goodbye to Camille and Herve, leaving her bonsai in caring hands while promising to celebrate together. "
         "Let's review the key farewell vocabulary from this scene.")

CLOSING = ("herve", "C'est parfait, sans les patrons pénibles!")
