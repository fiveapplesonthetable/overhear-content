# Authoring module for dix-pour-cent s04e05 scene 03 (cues 56-63).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-03.py --out out/dix-pour-cent/s04e05/scene-03.json

ID = "dix-pour-cent-s04e05-scene-03"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 3
TITLE = "Une carte pour Mathias  (A Card for Mathias)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Camille", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 56-63. Camille and Gabriel look through get-well cards for Mathias, "
               "debating whether visiting him in the hospital would trigger too much awkward tension.")

INTRO = ("At the ASK agency, Camille and Gabriel browse through various get-well cards for their former colleague Mathias Barneville. "
         "Having learned that Mathias recently suffered a heart attack, the two agents deliberate over appropriate card designs and discuss visiting him in person. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Regarde cette carte de bon rétablissement.",
     "Look at this get-well card.",
     [(56, "BON RÉTABLISSEMENT")], "Camille shows Gabriel a floral greeting card"),
    ("gabriel", "Je ne suis pas sûr de ce choix.",
     "I am not sure about this choice.",
     [(57, "Je ne suis pas sûr.")], "Gabriel examines the card design with skepticism"),
    ("gabriel", "Ça ne ressemble pas beaucoup à Mathias.",
     "That does not really look like Mathias.",
     [(57, "Ça ne me crie pas « Mathias ».")], "Gabriel doubts their former boss would appreciate it"),
    ("lea", "Sinon, il y a un joli trèfle.",
     "Otherwise, there is a pretty clover.",
     [(58, "un trèfle à quatre feuilles")], "Camille suggests an alternative lucky symbol"),
    ("gabriel", "Le petit chien est bien plus sympa!",
     "The little dog is much friendlier!",
     [(59, "Le labrador est plus sympa")], "Gabriel points toward an amusing animal card"),
    ("lea", "On ne devrait pas lui rendre visite?",
     "Should we not go pay him a visit?",
     [(60, "aller lui rendre visite?")], "Camille suggests visiting Mathias at the clinic"),
    ("gabriel", "On a travaillé des années avec lui.",
     "We worked for years with him.",
     [(61, "On a travaillé avec lui pendant des années.")], "Gabriel acknowledges their long professional bond"),
    ("lea", "Mais cela va le mettre mal à l'aise.",
     "But that will make him feel uncomfortable.",
     [(62, "mettre mal à l'aise")], "Camille worries about causing emotional strain"),
    ("gabriel", "Nous ne nous sommes pas quittés amis.",
     "We did not part ways as friends.",
     [(62, "On ne s'est pas quittés en très bons termes.")], "Gabriel recalls the bitter circumstances of Mathias's departure"),
    ("lea", "Il sort tout juste d'un infarctus.",
     "He just came through a heart attack.",
     [(63, "un deuxième infarctus après le premier.")], "Camille reminds him of Mathias's fragile medical state"),
    ("gabriel", "Un choc supplémentaire serait dangereux pour lui.",
     "An additional shock would be dangerous for him.",
     [], "new: Gabriel agrees that hospital confrontation is risky"),
    ("lea", "Envoyons simplement un mot très chaleureux.",
     "Let us simply send a very warm note.",
     [], "new: Camille recommends keeping things polite and distant"),
    ("gabriel", "Oui, signons tous ensemble cette carte.",
     "Yes, let us all sign this card together.",
     [], "new: Gabriel approves the collective agency gesture"),
    ("lea", "Je vais la faire signer à l'agence.",
     "I will have it signed at the agency.",
     [], "new: Camille volunteers to gather everyone's signature"),
]

OPENER = "Let's explore Camille and Gabriel's thoughtful discussion line by line."

WALK = [
    (0, None,
     "'Look at this get-well card.' Camille presents a selection of recovery stationery on her desk."),
    (1, None,
     "'I am not sure about this choice.' Gabriel hesitates over the sentimental imagery."),
    (2, None,
     "'That does not really look like Mathias.' Gabriel remarks that Mathias's austere taste clashes with cheesy cards."),
    (3, None,
     "'Otherwise, there is a pretty clover.' Camille points to a traditional four-leaf clover motif."),
    (4, None,
     "'The little dog is much friendlier!' Gabriel favors a charming and lighthearted canine illustration."),
    (5, None,
     "'Should we not go pay him a visit?' Camille wonders whether an in-person hospital visit would show proper respect."),
    (6, None,
     "'We worked for years with him.' Gabriel recalls their shared professional history building the agency together."),
    (7, None,
     "'But that will make him feel uncomfortable.' Camille cautions that an uninvited delegation might upset Mathias."),
    (8, None,
     "'We did not part ways as friends.' Gabriel admits that their bitter split left lingering resentment."),
    (9, None,
     "'He just came through a heart attack.' Camille stresses the absolute necessity of avoiding sudden cardiac excitement."),
    (10, None,
     "'An additional shock would be dangerous for him.' Gabriel acknowledges that stress could provoke a dangerous relapse."),
    (11, None,
     "'Let us simply send a very warm note.' Camille proposes sending considerate wishes through a thoughtful message."),
    (12, None,
     "'Yes, let us all sign this card together.' Gabriel suggests collecting signatures from all senior partners."),
    (13, None,
     "'I will have it signed at the agency.' Camille takes charge of circulating the card among colleagues."),
]

TRANSITION = "Now let's listen to Camille and Gabriel's discussion once more from start to finish."

OUTRO = ("Camille and Gabriel navigate the delicate balance between professional history and personal distance. "
         "Let's review the key vocabulary of health, friendship, and office diplomacy from this scene.")

CLOSING = ("lea", "Mathias reste dans nos pensées.")
