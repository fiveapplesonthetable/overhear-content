# Authoring module for dix-pour-cent s02e05 scene 11 (cues 309-340).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-11.py --out out/dix-pour-cent/s02e05/scene-11.json

ID = "dix-pour-cent-s02e05-scene-11"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 11
TITLE = "L'accusation d'Hervé  (Herve's Accusation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Camille", "theo": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 309-340. At the agency, Hervé confronts Camille with biblical fury, "
               "accusing her of being a traitor who stole the junior agent position through nepotism. "
               "Adapted for A1 French.")

INTRO = ("In the hallway at ASK, Herve confronts Camille after her sudden promotion to junior agent. "
         "Feeling deeply betrayed and suspecting nepotism, Herve bitterly accuses her of stealing the job behind his back. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Voici, et celui qu'on appelait Judas!",
  "Here it is, and he that was called Judas!",
  [(309, "Voici"), (310, "et celui qu'on appelait Judas,")], ""),
 ("theo", "Judas Barneville, fille de Mathias!",
  "Judas Barneville, daughter of Mathias!",
  [(317, "Judas Barneville,"), (318, "fille de Mathias")], ""),
 ("lea", "Hervé, arrête... Je suis désolée.",
  "Herve, stop... I am sorry.",
  [(314, "Hervé"), (322, "Je suis désolée.")], ""),
 ("theo", "Laisse-moi finir! Tu as trahi tes amis.",
  "Let me finish! You betrayed your friends.",
  [(315, "Laisse-moi finir.")], "Added Tu as trahi tes amis"),
 ("lea", "C'était Hicham. Je ne l'ai jamais cherché.",
  "It was Hicham. I never asked for it.",
  [(323, "C'était Hicham. Je ne l'ai jamais cherché.")], ""),
 ("theo", "Peux-tu jurer en ton âme et conscience que tu n'as jamais voulu ce poste?",
  "Can you swear on your heart and soul that you never wanted this job?",
  [(325, "Peux-tu jurer en ton âme et conscience"), (326, "que tu n'as jamais voulu ce poste")], ""),
 ("lea", "Au début, un peu. Mais je ne me suis jamais portée candidate.",
  "At first, a little. But I never put myself forward as a candidate.",
  [(327, "Au début, un peu."), (328, "Mais je ne me suis jamais portée candidate.")], ""),
 ("theo", "Pas auprès de ton père?",
  "Not to your father?",
  [(329, "Pas auprès de ton père ?")], ""),
 ("lea", "Non. En passant, peut-être, mais c'est tout.",
  "No. In passing, maybe, but that is all.",
  [(330, "Non. En passant, mais...")], "Added peut-être, mais c'est tout"),
 ("theo", "Maintenant tout s'explique! Tout était prémédité.",
  "Now it all makes sense! It was all premeditated.",
  [(331, "Maintenant tout s'explique !"), (332, "Tout était prémédité.")], ""),
 ("lea", "Pas du tout! Ce n'est pas vrai.",
  "Not at all! That is not true.",
  [(333, "Pas du tout !")], "Added Ce n'est pas vrai"),
 ("theo", "Si! Mathias a pistonné sa fille!",
  "Yes! Mathias pulled strings for his daughter!",
  [(334, "Mathias a pistonné sa fille !"), (333, "Si !")], ""),
 ("theo", "Il a influencé Hicham pour te choisir!",
  "He influenced Hicham to pick you!",
  [(335, "Il a influencé Hicham !")], "Added pour te choisir"),
 ("theo", "Et Mademoiselle Judas me disait que c'est mal de trébucher les autres!",
  "And Miss Judas was telling me that it is bad to trip up others!",
  [(336, "Mademoiselle Judas me disait que c'est mal de faire trébucher les autres")], "Adapted infinitive"),
 ("lea", "Arrête, Hervé! Je ne voulais pas te blesser.",
  "Stop, Herve! I did not want to hurt you.",
  [(338, "Arrête !"), (338, "Pas du tout !")], "Added Je ne voulais pas te blesser"),
 ("theo", "Tu as pris ma place, Camille.",
  "You took my place, Camille.",
  [(323, "C'était Hicham.")], "Adapted closing resentment"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Here it is, and he that was called Judas!' Herve summons Camille with ominous biblical solemnity. "
  "The presentative 'voici' introduces a dramatic quotation from the scripture."),
 (1, None,
  "'Judas Barneville, daughter of Mathias!' Herve delivers his biting personal accusation. "
  "He substitutes Mathias's family name to brand Camille as a betrayer."),
 (2, None,
  "'Herve, stop... I am sorry.' Camille tries to apologize for the unexpected promotion. "
  "The adjective 'desolee' expresses genuine regret for the fallout."),
 (3, None,
  "'Let me finish! You betrayed your friends.' Herve cuts off her defense angrily. "
  "The imperative 'laisse-moi finir' demands uninterrupted expression of his anger."),
 (4, None,
  "'It was Hicham. I never asked for it.' Camille explains that the decision came entirely from Hicham. "
  "The verb 'chercher' here means to seek or actively campaign for something."),
 (5, None,
  "'Can you swear on your heart and soul that you never wanted this job?' Herve demands a moral confession. "
  "The idiom 'jurer en ton ame et conscience' appeals to absolute honesty."),
 (6, None,
  "'At first, a little. But I never put myself forward as a candidate.' Camille admits her private longing honestly. "
  "The reflexive locution 'se porter candidate' means to apply formally."),
 (7, None,
  "'Not to your father?' Herve suspects family lobbying behind closed doors. "
  "The preposition 'aupres de' means with or in the presence of someone influential."),
 (8, None,
  "'No. In passing, maybe, but that is all.' Camille downplays any casual conversation. "
  "The locution 'en passant' means casually or incidentally."),
 (9, None,
  "'Now it all makes sense! It was all premeditated.' Herve fits the conspiracy pieces together. "
  "The passive reflexive 'tout s'explique' indicates that everything is now clear."),
 (10, None,
  "'Not at all! That is not true.' Camille denies any underhanded calculation. "
  "The emphatic phrase 'ce n'est pas vrai' rejects the accusation outright."),
 (11, None,
  "'Yes! Mathias pulled strings for his daughter!' Herve accuses Mathias of blatant nepotism. "
  "The colloquial verb 'pistonner' means to pull strings or recommend through favouritism."),
 (12, None,
  "'He influenced Hicham to pick you!' Herve asserts Mathias's hidden leverage over the agency boss. "
  "The preposition 'pour' takes the infinitive 'te choisir'."),
 (13, None,
  "'And Miss Judas was telling me that it is bad to trip up others!' Herve mocks Camille's earlier moral advice. "
  "The verb 'faire trebucher' means to make someone stumble or sabotage them."),
 (14, None,
  "'Stop, Herve! I did not want to hurt you.' Camille pleads for understanding. "
  "The verb 'blesser' means to hurt someone emotionally or physically."),
 (15, None,
  "'You took my place, Camille.' Herve states his deep feeling of professional loss. "
  "The phrase 'prendre ma place' underscores his sense of stolen opportunity."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Herve vents his bitter disappointment at being passed over for the junior agent post, "
         "accusing Camille of benefiting from family nepotism. Camille is left heartbroken by her friend's fierce anger.")
CLOSING = ("theo", "Mathias a pistonné sa fille!")
