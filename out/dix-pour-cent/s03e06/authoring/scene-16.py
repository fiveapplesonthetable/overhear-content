# Authoring module for dix-pour-cent s03e06 scene 16 (cues 639-681).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s03e06/scene-16.json

ID = "dix-pour-cent-s03e06-scene-16"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 16
TITLE = "Les trente ans d'ASK  (Thirty Years of ASK)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Isabelle", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 639-681. Isabelle arrives at ASK's 30th anniversary party, "
               "celebrating with Mathias and toasting to thirty years.")

INTRO = ("In the festive agency lounge, the guests gather to celebrate thirty years of ASK. "
         "Having rushed back from the shoot, Isabelle joins Mathias to toast to the agency and its cinematic history. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Bonsoir Mathias, me voilà enfin arrivée!",
  "Good evening Mathias, here I am at last!",
  [(639, "Bonsoir")], "Arriving at party"),
 ("mathias", "Alors, le tournage est terminé?",
  "So, is the shoot finished?",
  [(642, "C'est bon, c'est dans la boîte")], "Asking about shoot"),
 ("lea", "C'est bon, c'est dans la boîte!",
  "All good, it is in the can!",
  [(642, "C'est bon, c'est dans la boîte")], "Confirming wrap"),
 ("mathias", "Tu as réussi un exploit incroyable.",
  "You achieved an incredible feat.",
  [(647, "Oh, vous êtes fortes")], "Praising achievement"),
 ("lea", "L'équipe envoie tout au montage.",
  "The team sends everything to editing.",
  [(643, "c'est parti au montage")], "Explaining next step"),
 ("mathias", "Quelle fierté de te voir ici.",
  "What pride to see you here.",
  [(667, "ça me fait plaisir de vous voir")], "Welcoming actress"),
 ("lea", "Je voulais être là ce soir.",
  "I wanted to be here tonight.",
  [(656, "ça me fait tout drôle d'être ici pour les 30 ans d'ASK")], "Expressing loyalty"),
 ("mathias", "Nous fêtons les trente ans d'ASK.",
  "We celebrate thirty years of ASK.",
  [(656, "les 30 ans d'ASK")], "Mentioning anniversary"),
 ("lea", "Cette agence compte beaucoup pour moi.",
  "This agency matters a lot to me.",
  [(657, "J'étais une des premières clientes")], "Expressing attachment"),
 ("mathias", "Tu es toujours notre star préférée.",
  "You are always our favorite star.",
  [(658, "J'étais LA première cliente")], "Complimenting star"),
 ("lea", "Regarde tous ces amis réunis.",
  "Look at all these friends gathered.",
  [(670, "Réunis")], "Looking at crowd"),
 ("mathias", "Nous formons une grande famille unie.",
  "We form a large united family.",
  [(671, "Une grande famille")], "Celebrating unity"),
 ("lea", "Buvons un verre tous ensemble.",
  "Let's have a drink all together.",
  [(677, "À nous")], "Proposing drink"),
 ("mathias", "À notre agence et à l'avenir!",
  "To our agency and to the future!",
  [(679, "À ASK")], "Toasting ASK"),
]

WALK = [
 (0, None,
  "'Good evening Mathias, here I am at last!' Isabelle greets her longtime agent. "
  "The presentation word 'voila' marks her joyful arrival."),
 (1, None,
  "'So, is the shoot finished?' Mathias asks about the secret film production. "
  "The adjective 'termine' indicates completion."),
 (2, None,
  "'All good, it is in the can!' Isabelle uses the famous cinema expression. "
  "The idiom 'dans la boite' means the film take is successfully finished."),
 (3, None,
  "'You achieved an incredible feat.' Mathias marvels at her talent. "
  "The noun 'exploit' highlights an extraordinary achievement."),
 (4, None,
  "'The team sends everything to editing.' Isabelle details the postproduction steps. "
  "The noun 'montage' denotes the film editing stage."),
 (5, None,
  "'What pride to see you here.' Mathias welcomes the beloved star warmly. "
  "The noun 'fierte' expresses deep admiration."),
 (6, None,
  "'I wanted to be here tonight.' Isabelle affirms her commitment to the party. "
  "The imperfect 'voulais' conveys her persistent wish."),
 (7, None,
  "'We celebrate thirty years of ASK.' Mathias marks the major milestone. "
  "The verb 'feter' means to celebrate an anniversary."),
 (8, None,
  "'This agency matters a lot to me.' Isabelle expresses her emotional loyalty. "
  "The expression 'compter pour' means to matter dearly to someone."),
 (9, None,
  "'You are always our favorite star.' Mathias showers her with compliments. "
  "The adjective 'preferee' agrees in gender with star."),
 (10, None,
  "'Look at all these friends gathered.' Isabelle observes the crowd of colleagues. "
  "The past participle 'reunis' describes people brought together."),
 (11, None,
  "'We form a large united family.' Mathias reflects on their solidarity. "
  "The adjective 'unie' describes a closely knit bond."),
 (12, None,
  "'Let's have a drink all together.' Isabelle proposes a shared toast. "
  "The imperative 'buvons' invites the group to drink together."),
 (13, None,
  "'To our agency and to the future!' Mathias raises his glass in celebration. "
  "The preposition 'a' is commonly used when toasting."),
]

OUTRO = ("Isabelle and Mathias celebrate thirty years of triumphs and shared memories at ASK. "
         "Surrounded by their cinema family, they look ahead with hope and warmth. "
         "Now, let's review the scene one last time.")

CLOSING = ("mathias", "À notre agence et à l'avenir!")
