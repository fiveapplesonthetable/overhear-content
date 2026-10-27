# Authoring module for dix-pour-cent s03e03 scene 19 (cues 1190-1218).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-19.py --out out/dix-pour-cent/s03e03/scene-19.json

ID = "dix-pour-cent-s03e03-scene-19"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 19
TITLE = "J'ai la haine  (I'm So Angry)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "theo"}
LABELS = {"lea": "Samy", "gerard": "Gérard"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 1190-1218. Outside on the street, young waiter Samy catches up with Gérard Lanvin, "
               "confessing his bitter regret and apologizing for blowing the audition after Gérard gave him his break. Adapted for A1 French.")

INTRO = ("Outside on the Parisian pavement, young waiter Samy catches up with veteran actor Gerard Lanvin in deep despair. "
         "Convinced that he completely botched his screen audition, Samy tearfully apologizes for wasting the incredible opportunity Gerard gave him. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Gérard, attendez-moi dans la rue!",
  "Gerard, wait for me in the street!",
  [(1190, "Gérard !")], "Called out on street"),
 ("gerard", "Pourquoi tu cours comme ça, Samy?",
  "Why are you running like that, Samy?",
  [(1193, "La haine de quoi ?")], "Asked about hurried pace"),
 ("lea", "J'ai tellement la haine contre moi.",
  "I am so angry with myself.",
  [(1192, "Putain, j'ai la haine.")], "Expressed inner anger"),
 ("gerard", "Mais la haine de quoi exactement?",
  "But angry about what exactly?",
  [(1193, "La haine de quoi ?")], "Questioned emotional distress"),
 ("lea", "J'ai totalement foiré mon audition aujourd'hui.",
  "I totally blew my audition today.",
  [(1197, "J'ai tout foiré")], "Admitted ruined screen test"),
 ("gerard", "Ce n'est pas de ta faute.",
  "It is not your fault.",
  [(1199, "C'est pas de ta faute.")], "Refused to assign blame"),
 ("lea", "Vous m'avez fait tellement confiance!",
  "You trusted me so much!",
  [(1203, "vous m'avez fait confiance")], "Recalled mentor trust"),
 ("gerard", "Tu as beaucoup de talent naturel.",
  "You have lots of natural talent.",
  [(1203, "Vous m'avez ouvert les portes")], "Praised innate acting skill"),
 ("lea", "Et regardez ce que j'en fais.",
  "And look what I do with it.",
  [(1204, "regardez ce que j'en ai fait")], "Lamented wasted opportunity"),
 ("gerard", "L'échec fait partie de ce métier.",
  "Failure is part of this profession.",
  [(1201, "c'est de ma faute.")], "Shared professional reality"),
 ("lea", "Je ne suis qu'un simple serveur.",
  "I am only a simple waiter.",
  [(1210, "Je suis qu'un simple serveur.")], "Downplayed personal worth"),
 ("gerard", "Ne dis pas de telles bêtises.",
  "Do not say such silly things.",
  [(1211, "Non, t'assois pas là")], "Dismissed self-deprecating remark"),
 ("lea", "Je n'ai pas le bon niveau.",
  "I do not have the right level.",
  [(1207, "Je suis pas au niveau")], "Doubted acting qualification"),
 ("gerard", "Assieds-toi deux minutes avec moi.",
  "Sit down two minutes with me.",
  [(1218, "Tu sais, Samy")], "Invited to sit together"),
]

OPENER = "Let's see how Gerard listens to Samy's anguish on the street."

WALK = [
 (0, None,
  "'Gerard, wait for me in the street!' An urgent imperative calling after the star."),
 (1, None,
  "'Why are you running like that, Samy?' A curious inquiry asking about his hurried pace."),
 (2, None,
  "'I am so angry with myself.' A raw emotional outburst confessing inner frustration."),
 (3, None,
  "'But angry about what exactly?' A gentle question probing the cause of his distress."),
 (4, None,
  "'I totally blew my audition today.' A regretful confession lamenting a failed performance."),
 (5, None,
  "'It is not your fault.' A direct reassurance relieving the young actor of blame."),
 (6, None,
  "'You trusted me so much!' An appreciative exclamation remembering his mentor's faith."),
 (7, None,
  "'You have lots of natural talent.' An encouraging compliment praising his raw ability."),
 (8, None,
  "'And look what I do with it.' A bitter self-criticism acknowledging missed opportunity."),
 (9, None,
  "'Failure is part of this profession.' A realistic reminder framing setbacks as normal experience."),
 (10, None,
  "'I am only a simple waiter.' A self-deprecating statement questioning his place in cinema."),
 (11, None,
  "'Do not say such silly things.' A firm imperative rejecting unfair self-pity."),
 (12, None,
  "'I do not have the right level.' A disheartened admission doubting his acting standard."),
 (13, None,
  "'Sit down two minutes with me.' A friendly invitation offering compassionate counsel."),
]

TRANSITION = "Now let's listen to Samy and Gerard again at natural speed."

OUTRO = ("Touched by Samy's genuine passion and humility, Gerard pauses to offer wise counsel rather than walking away. "
         "Their candid exchange sets the stage for an unexpected revelation between two very different generations of artists.")

CLOSING = ("gerard", "Écoute ce que j'ai à te dire.")
