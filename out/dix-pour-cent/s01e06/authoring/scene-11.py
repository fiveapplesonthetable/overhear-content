# Authoring module for dix-pour-cent s01e06 scene 11 (cues 288-322).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-11.py --out out/dix-pour-cent/s01e06/scene-11.json

ID = "dix-pour-cent-s01e06-scene-11"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 11
TITLE = "Notre père  (Our Father)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hippolyte": "theo", "serveur": "marcel"}
LABELS = {"lea": "Camille", "hippolyte": "Hippolyte", "serveur": "Le serveur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 288-322. Camille and Hippolyte meet at a Parisian sidewalk cafe to sign his contracts. "
               "They discuss the cold weather, their father Mathias, and agree to become brother and sister buddies. "
               "Adapted for A1 French.")

INTRO = ("Refusing to visit the agency while his father Mathias is there, Hippolyte asks Camille to meet him at a cafe. "
         "Sitting outside on a cold Paris afternoon, the two half-siblings sign contracts, talk about their shared father, "
         "and invent a warm new friendship. Let's listen to the scene in French first.")

STORY = [
 ("hippolyte", "Mon père est là?",
  "Is my father there?",
  [(288, "Mon père est là")], ""),
 ("lea", "Oui.",
  "Yes.",
  [(289, "Oui")], ""),
 ("hippolyte", "Je ne viens pas, alors. Je ne veux pas le voir.",
  "I'm not coming, then. I don't want to see him.",
  [(290, "Je ne viens pas, alors"), (290, "Je ne veux pas le voir")], ""),
 ("lea", "On peut se retrouver ailleurs?",
  "Can we meet somewhere else?",
  [(292, "On peut se retrouver ailleurs")], ""),
 ("hippolyte", "Salut!",
  "Hi!",
  [(293, "Salut")], ""),
 ("lea", "Un café, s'il vous plaît.",
  "A coffee, please.",
  [(294, "Un café, s'il vous plaît")], ""),
 ("serveur", "D'accord.",
  "All right.",
  [(294, "D'accord")], ""),
 ("hippolyte", "Il a soudainement fait froid. C'est l'enfer en scooter.",
  "It suddenly got cold. It is hell on a scooter.",
  [(295, "Il a soudainement fait froid"), (296, "C'est l'enfer en scooter")], ""),
 ("lea", "Il gèle à vélo. Je pédale comme une folle!",
  "It's freezing on a bike. I pedal like crazy!",
  [(297, "Il gèle à vélo"), (298, "Je pédale comme une folle")], ""),
 ("lea", "Voici vos contrats.",
  "Here are your contracts.",
  [(302, "Vos contrats")], ""),
 ("hippolyte", "Mon stylo ne marche pas. Désolé.",
  "My pen is not working. Sorry.",
  [(304, "Mon stylo ne marche pas"), (304, "Désolé")], ""),
 ("hippolyte", "C'est mon père qui devrait s'excuser, pas toi.",
  "My father is the one who should apologize, not you.",
  [(306, "C'est mon père qui devrait s'excuser, pas toi")], ""),
 ("lea", "Notre père! C'est trop bizarre.",
  "Our father! It is so weird.",
  [(307, "Notre père"), (308, "C'est trop bizarre")], ""),
 ("hippolyte", "On va juste oublier ça et devenir amis.",
  "We are just going to forget about that and become friends.",
  [(315, "On va... juste oublier ça"), (316, "Et devenir amis")], ""),
 ("hippolyte", "Tu es ma sœpote et je suis ton frote!",
  "You are my sister-buddy and I am your brother-buddy!",
  [(319, "mon \"frote\""), (320, "Je suis ta \"sœpote\"")], "Contraction unpacked"),
 ("lea", "Tchin, frote!",
  "Cheers, brother-buddy!",
  [(322, "Tchin, frote")], ""),
]

OPENER = "Camille and Hippolyte break the ice. Let us examine their lines together."

WALK = [
 (0, None, "'Is my father there?' Hippolyte checks whether Mathias is at ASK. Mon pere means my father."),
 (1, None, "'Yes.' Camille confirms with a simple affirmative oui, meaning yes."),
 (2, None, "'I am not coming, then. I do not want to see him.' Venir means to come, and voir means to see."),
 (3, None, "'Can we meet somewhere else?' Se retrouver is a reflexive verb meaning to meet up."),
 (4, None, "'Hi!' Hippolyte greets Camille warmly when she arrives at the terrace."),
 (5, None, "'A coffee, please.' Camille places an order with the waiter. Un cafe means an espresso coffee."),
 (6, None, "'All right.' The waiter acknowledges her order with d'accord, meaning okay or all right."),
 (7, None, "'It suddenly got cold. It is hell on a scooter.' Soudainement means suddenly, and l'enfer means hell."),
 (8, None, "'It is freezing on a bike. I pedal like crazy!' Geler means to freeze, and pedaler means to pedal."),
 (9, None, "'Here are your contracts.' Voici is a handy demonstrative word meaning here is or here are."),
 (10, None, "'My pen is not working. Sorry.' Un stylo is a pen, and marcher means to work."),
 (11, None, "'My father is the one who should apologize, not you.' S'excuser is a reflexive verb meaning to apologize."),
 (12, None, "'Our father! It is so weird.' Notre pere emphasizes their sibling bond, and bizarre means weird."),
 (13, None, "'We are just going to forget about that and become friends.' Oublier means to forget, and devenir means to become."),
 (14, None, "'You are my sister-buddy and I am your brother-buddy!' They coin playful portmanteau words with pote."),
 (15, None, "'Cheers, brother-buddy!' Tchin is a joyful French toast equivalent to cheers."),
]

TRANSITION = "Now listen to their cafe conversation once more from start to finish."
OUTRO = ("Having made peace with their unusual family bond, Camille and Hippolyte raise their cups together. "
         "Meanwhile, Andrea drives out to the countryside to track down Francois Berleand. "
         "Here is our final toast.")
CLOSING = ("lea", "Tchin, frote!")
