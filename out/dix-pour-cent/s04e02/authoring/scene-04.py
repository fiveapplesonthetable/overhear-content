# Authoring module for dix-pour-cent s04e02 scene 04 (cues 240-260).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-04.py --out out/dix-pour-cent/s04e02/scene-04.json

ID = "dix-pour-cent-s04e02-scene-04"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 4
TITLE = "L'offre de Mathias  (Mathias's Offer)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 240-260. Andrea meets producer Mathias to negotiate terms for Luchini and Sofia. Mathias uses aggressive blackmail. Adapted for A1 French.")

INTRO = ("At a Parisian café table, Andrea Martel sits down across from her former mentor and rival Mathias Barneville, now acting as an independent producer. "
         "Expecting a fair deal for Fabrice Luchini and rising talent Sofia Leprince, Andrea is outraged by Mathias's drastically low financial offer. "
         "When Mathias coldly threatens to poison ASK's relationship with star client Dany Boon unless she capitulates, a ruthless power struggle erupts. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Cette proposition financière est une mauvaise blague.",
  "This financial proposal is a bad joke.",
  [(240, "C'est une blague")], "Dismissed initial terms indignantly"),
 ("lea", "Tu renverrais un producteur avec cette offre.",
  "You would send a producer packing with this offer.",
  [(243, "une offre aussi nulle")], "Mocked lowball compensation"),
 ("lea", "Nous parlons de Fabrice Luchini ici.",
  "We are talking about Fabrice Luchini here.",
  [(244, "parle de Fabrice Luchini")], "Stressed client's star prestige"),
 ("mathias", "Et nous parlons aussi de Sofia Leprince.",
  "And we are also talking about Sofia Leprince.",
  [(245, "Et de Sofia Leprince")], "Counterbalanced with newcomer talent"),
 ("lea", "Ajoute un zéro à tous ces montants.",
  "Add a zero to all these amounts.",
  [(248, "tu ajoutes un zéro")], "Demanded tenfold remuneration increase"),
 ("mathias", "Tu acceptes cette offre telle quelle.",
  "You accept this offer as is.",
  [(250, "prends comme c'est")], "Refused to negotiate terms"),
 ("mathias", "Sinon, je préviens Dany Boon immédiatement.",
  "Otherwise, I notify Dany Boon immediately.",
  [(251, "dis pas à Dany Boon")], "Threatened damaging client intervention"),
 ("mathias", "Je lui dirai qu'ASK manque d'avenir.",
  "I will tell him ASK lacks a future.",
  [(252, "une agence sans avenir")], "Wielded devastating reputational blackmail"),
 ("lea", "C'est vraiment un sale coup bas!",
  "That is really a dirty low blow!",
  [(253, "C'est un coup bas")], "Condemned hostile blackmail tactic"),
 ("mathias", "Ce n'est absolument rien de personnel.",
  "This is absolutely nothing personal.",
  [(255, "ce n'est pas personnel")], "Depersonalized aggressive corporate tactic"),
 ("mathias", "C'est simplement la réalité du métier.",
  "It is simply the reality of the business.",
  [(255, "ce n'est pas personnel")], "Justified behavior by cutthroat industry norms"),
 ("mathias", "Diriger implique de perdre certaines batailles.",
  "Leading implies losing certain battles.",
  [(256, "perdre des batailles")], "Lectured successor on executive compromises"),
 ("lea", "Je ne me laisserai jamais intimider.",
  "I will never let myself be intimidated.",
  [(253, "C'est un coup bas")], "Refused to yield to intimidation"),
 ("mathias", "Réfléchis bien à l'intérêt de l'agence.",
  "Think carefully about the agency's interest.",
  [(256, "perdre des batailles")], "Advised pragmatic surrender"),
]

OPENER = "Let's observe as Andrea and Mathias clash over contracts and agency loyalty."

WALK = [
 (0, None,
  "'This financial proposal is a bad joke.' An indignant opening dismissing the offer as completely inadequate."),
 (1, None,
  "'You would send a producer packing with this offer.' A sharp comparison turning his own past agent standards against him."),
 (2, None,
  "'We are talking about Fabrice Luchini here.' A powerful reminder emphasizing the immense prestige of the lead actor."),
 (3, None,
  "'And we are also talking about Sofia Leprince.' A shrewd counter-argument pointing to the unproven newcomer co-star."),
 (4, None,
  "'Add a zero to all these amounts.' An aggressive counter-demand insisting on a tenfold increase in fees."),
 (5, None,
  "'You accept this offer as is.' An uncompromising ultimatum rejecting any further discussion on price."),
 (6, None,
  "'Otherwise, I notify Dany Boon immediately.' A ruthless threat turning private client trust into extortion."),
 (7, None,
  "'I will tell him ASK lacks a future.' A damaging weapon aimed directly at undermining client confidence."),
 (8, None,
  "'That is really a dirty low blow!' An outraged condemnation of unethical betrayal by a former partner."),
 (9, None,
  "'This is absolutely nothing personal.' A cynical disavowal detaching private sentiment from commercial aggression."),
 (10, None,
  "'It is simply the reality of the business.' A cold justification rationalizing vicious tactics as standard practice."),
 (11, None,
  "'Leading implies losing certain battles.' A patronizing lesson instructing his successor on executive pragmatism."),
 (12, None,
  "'I will never let myself be intimidated.' A defiant declaration refusing to cave in to corporate blackmail."),
 (13, None,
  "'Think carefully about the agency's interest.' A calculated parting shot advising surrender for corporate survival."),
]

TRANSITION = "Now let's listen to Andrea and Mathias negotiating again at full speed."

OUTRO = ("Refusing to bow to Mathias's blackmail, Andrea leaves the meeting with renewed anger and determination. "
         "The gloves are entirely off, and the battle between the agency and its former founder has turned into open warfare.")

CLOSING = ("lea", "La guerre ne fait que commencer.")
