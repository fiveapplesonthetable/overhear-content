# Authoring module for dix-pour-cent s03e06 scene 27 (cues 1314-1326).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-27.py --out overhear-content/out/dix-pour-cent/s03e06/scene-27.json

ID = "dix-pour-cent-s03e06-scene-27"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 27
TITLE = "La proposition d'Hicham  (Hicham's Offer)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 1314-1326. Late at night at ASK, Andrea and Hicham reflect on Mathias's departure. "
               "Hicham reveals he is moving to London and offers Andrea the director general position.")

INTRO = ("Late in the evening at the ASK offices, Andrea and Hicham reflect upon Mathias's abrupt departure. "
         "Acknowledging his personal priorities, Hicham reveals he is moving to London and makes Andrea a life-changing offer. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Ce sera bizarre sans Mathias.",
  "It will be strange without Mathias.",
  [(1314, "sans Mathias")], "Reflecting on departure"),
 ("lea", "Il m'a fait de la peine.",
  "I felt sorry for him.",
  [(1315, "de la peine")], "Expressing sympathy"),
 ("hicham", "Pour un peu, il nous manquerait.",
  "Almost makes you miss him.",
  [(1317, "il nous manquerait")], "Admitting nostalgia"),
 ("hicham", "Bon, je vais partir maintenant.",
  "Well, I am heading out now.",
  [(1318, "Bon, j'y vais")], "Preparing to leave"),
 ("hicham", "Tu pourras fermer la boutique?",
  "Can you lock up the shop?",
  [(1319, "fermer la boutique")], "Asking to lock up"),
 ("lea", "Pas de problème pour ça.",
  "No problem with that.",
  [(1320, "Pas de problème")], "Accepting closing duty"),
 ("hicham", "Tu pourrais diriger la boutique.",
  "You could run the shop.",
  [(1321, "de la boutique")], "Suggesting bigger role"),
 ("hicham", "Je pars vivre à Londres.",
  "I am moving to London.",
  [(1322, "à Londres")], "Announcing relocation"),
 ("hicham", "Mon fils a besoin de moi.",
  "My son needs me.",
  [(1323, "besoin de moi")], "Prioritizing family"),
 ("hicham", "J'ai besoin de quelqu'un de confiance.",
  "I need someone trustworthy.",
  [(1324, "quelqu'un de confiance")], "Seeking trusted partner"),
 ("hicham", "Je cherche une nouvelle directrice.",
  "I am looking for a new director.",
  [(1325, "Un DG")], "Defining role"),
 ("hicham", "Le poste de directrice t'intéresse?",
  "Does the director post interest you?",
  [(1326, "Ça t'intéresse")], "Making formal offer"),
 ("lea", "C'est une offre incroyable, Hicham.",
  "That is an incredible offer, Hicham.",
  [(1326, "Ça t'intéresse")], "Reacting with awe"),
 ("hicham", "Réfléchis bien à cette opportunité.",
  "Think carefully about this opportunity.",
  [(1326, "Ça t'intéresse")], "Urging serious thought"),
]

WALK = [
 (0, None,
  "'It will be strange without Mathias.' Andrea reflects on the agency atmosphere after Mathias leaves. "
  "The future tense 'ce sera' expresses prospective feeling."),
 (1, None,
  "'I felt sorry for him.' Andrea expresses genuine compassion for their fallen senior partner. "
  "The idiom 'faire de la peine' means to cause sorrow or pity."),
 (2, None,
  "'Almost makes you miss him.' Hicham confesses with a hint of warmth that Mathias will be missed. "
  "The conditional 'manquerait' indicates a hypothetical feeling."),
 (3, None,
  "'Well, I am heading out now.' Hicham prepares to leave the office for the night. "
  "The verb 'partir' means to leave or depart."),
 (4, None,
  "'Can you lock up the shop?' Hicham asks Andrea to lock the premises. "
  "The colloquial expression 'fermer la boutique' means to close down the business for the night."),
 (5, None,
  "'No problem with that.' Andrea accepts the responsibility easily. "
  "The phrase 'pas de probleme' signals casual agreement."),
 (6, None,
  "'You could run the shop.' Hicham expands the metaphor to running the entire agency. "
  "The verb 'diriger' means to manage or lead."),
 (7, None,
  "'I am moving to London.' Hicham announces his impending move across the Channel. "
  "The proper noun 'Londres' designates the British capital."),
 (8, None,
  "'My son needs me.' Hicham explains his personal reason for stepping back from day-to-day operations. "
  "The idiom 'avoir besoin de' expresses necessity."),
 (9, None,
  "'I need someone trustworthy.' Hicham stresses the paramount importance of integrity in management. "
  "The noun phrase 'quelqu'un de confiance' means a trustworthy person."),
 (10, None,
  "'I am looking for a new director.' Hicham describes the executive vacancy. "
  "The feminine noun 'directrice' designates a female managing director."),
 (11, None,
  "'Does the director post interest you?' Hicham presents Andrea with the ultimate promotion. "
  "The verb 'interesser' takes an indirect object pronoun."),
 (12, None,
  "'That is an incredible offer, Hicham.' Andrea is stunned by the magnitude of the proposal. "
  "The adjective 'incroyable' highlights how extraordinary the offer is."),
 (13, None,
  "'Think carefully about this opportunity.' Hicham encourages her to weigh the decision. "
  "The imperative 'reflechis' invites thoughtful deliberation."),
]

OUTRO = ("Andrea stands in the darkened office, overwhelmed by the prospect of taking full command of ASK. "
         "From junior agent to managing director, her journey mirrors the evolving spirit of the agency. "
         "Now, let's review the scene one last time.")

CLOSING = ("hicham", "Réfléchis bien à cette opportunité.")
