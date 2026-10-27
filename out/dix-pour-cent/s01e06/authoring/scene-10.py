# Authoring module for dix-pour-cent s01e06 scene 10 (cues 267-288).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-10.py --out out/dix-pour-cent/s01e06/scene-10.json

ID = "dix-pour-cent-s01e06-scene-10"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 10
TITLE = "La menace de procès  (The Threat of a Lawsuit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "directeur": "theo", "camille": "emilie"}
LABELS = {"lea": "Andréa", "directeur": "Le directeur", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 267-288. The theatre director threatens to sue ASK after François Berléand punches Christophe Bel. "
               "Camille suggests offering a discount like her mother does in her hair salon, then calls Hippolyte Barneville. "
               "Adapted for A1 French.")

INTRO = ("After Francois Berleand punches young theatre director Christophe Bel in a fury over the swimming pool staging, "
         "the theatre director threatens to sue ASK for cancelling the production. Andrea is terrified of a public scandal, "
         "while Camille suggests offering a commercial gesture. Let's listen to the scene in French first.")

STORY = [
 ("directeur", "Faites quelque chose.",
  "Do something.",
  [(267, "Faites quelque chose")], ""),
 ("directeur", "Sinon je vais devoir vous poursuivre, je n'ai pas le choix.",
  "Otherwise I will have to sue you, I have no choice.",
  [(268, "Sinon je vais devoir vous poursuivre"), (268, "je n'ai pas le choix")], ""),
 ("lea", "Oui, bien sûr. Vous pouvez compter sur moi.",
  "Yes, of course. You can count on me.",
  [(269, "Vous pouvez compter sur moi")], ""),
 ("lea", "C'est une catastrophe pour l'agence.",
  "It is a disaster for the agency.",
  [], "New reaction to lawsuit threat"),
 ("camille", "C'est si grave que ça? C'est du théâtre, quand même.",
  "Is it that bad? It's only theatre, after all.",
  [(271, "C'est si grave que ça"), (271, "C'est du théâtre, quand même")], ""),
 ("lea", "Vous savez ce que ça pourrait coûter?",
  "Do you know what this could cost?",
  [(272, "Vous savez ce que ça pourrait coûter")], ""),
 ("lea", "On ne peut pas laisser filtrer cette histoire de coup de poing.",
  "We cannot let this punch story get out.",
  [(274, "on ne peut pas laisser filtrer cette histoire de coup de poing")], ""),
 ("lea", "Il faut étouffer ça maintenant.",
  "We must stifle this right now.",
  [(277, "Il faut étouffer ça maintenant")], ""),
 ("camille", "Quand ma mère a un client mécontent, elle fait un geste pour ses amis.",
  "When my mother has an unhappy customer, she gives her friends a discount.",
  [(278, "Quand ma mère a un client mécontent"), (278, "elle fait un geste pour ses amis")], ""),
 ("camille", "Elle ne perd pas de clientèle.",
  "She doesn't lose any customers.",
  [(279, "Elle ne perd pas de clientèle")], ""),
 ("lea", "Donc on baisse les tarifs pour toutes nos stars?",
  "So we lower the rates for all our stars?",
  [(280, "Donc on baisse les tarifs pour toutes nos stars")], ""),
 ("lea", "Appelez-les vous-même, alors!",
  "Call them yourself, then!",
  [(281, "Appelez-les vous-même, alors")], ""),
 ("camille", "Allô, Hippolyte? Bonjour, c'est Camille, d'ASK.",
  "Hello, Hippolyte? Hello, this is Camille from ASK.",
  [(284, "Allô, Hippolyte ? Bonjour, c'est Camille, d'ASK")], ""),
 ("camille", "Andréa m'a demandé de vous appeler au sujet de vos contrats.",
  "Andréa asked me to call you about your contracts.",
  [(285, "Andréa m'a demandé de vous appeler au sujet de vos contrats")], ""),
 ("camille", "Vous pouvez passer les vérifier et les signer?",
  "Can you come by to check them and sign them?",
  [(287, "Vous pouvez passer les vérifier et les signer")], ""),
]

OPENER = "The theatre director is furious. Let us listen to each sentence again with explanations."

WALK = [
 (0, None, "'Do something.' The director demands immediate action from Andrea. Faites is from the verb faire."),
 (1, None, "'Otherwise I will have to sue you, I have no choice.' Sinon means otherwise, and le choix means choice."),
 (2, None, "'Yes, of course. You can count on me.' Compter sur means to rely or count on someone."),
 (3, None, "'It is a disaster for the agency.' Une catastrophe is a feminine noun meaning a disaster."),
 (4, None, "'Is it that bad? It is only theatre, after all.' Quand meme is a common phrase meaning after all."),
 (5, None, "'Do you know what this could cost?' Pouvoir means can or could, and couter means to cost."),
 (6, None, "'We cannot let this punch story get out.' Un coup de poing is the French term for a punch."),
 (7, None, "'We must stifle this right now.' Il faut is followed by an infinitive meaning one must or we must."),
 (8, None, "'When my mother has an unhappy customer, she gives her friends a discount.' Un geste means a concession."),
 (9, None, "'She does not lose any customers.' Perdre means to lose, and la clientele means the customer base."),
 (10, None, "'So we lower the rates for all our stars?' Baisser les tarifs means to lower the prices or rates."),
 (11, None, "'Call them yourself, then!' Andrea uses an imperative with the emphatic pronoun vous-meme."),
 (12, None, "'Hello, Hippolyte? Hello, this is Camille from ASK.' Camille makes the phone call to Mathias's son."),
 (13, None, "'Andrea asked me to call you about your contracts.' Au sujet de means on the subject of or about."),
 (14, None, "'Can you come by to check them and sign them?' Passer means to stop by, and signer means to sign."),
]

TRANSITION = "Now listen to the full conversation once more at a natural pace."
OUTRO = ("Hippolyte answers Camille's call, but when he asks if his father Mathias is at the office, "
         "he refuses to come in and suggests meeting Camille somewhere else instead. "
         "Here is our final takeaway line.")
CLOSING = ("directeur", "Faites quelque chose.")
