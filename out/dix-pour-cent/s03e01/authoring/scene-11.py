# Authoring module for dix-pour-cent s03e01 scene 11 (cues 238-292).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-11.py --out out/dix-pour-cent/s03e01/scene-11.json

ID = "dix-pour-cent-s03e01-scene-11"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 11
TITLE = "Entretien avec la direction  (Meeting with the Boss)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 238-292. In his office, Hicham delicately questions Andréa about her pregnancy and maternity leave, "
               "while Andréa firmly asserts her independence before leaving for client Jean Dujardin. Adapted for A1 French.")

INTRO = ("In the executive office at ASK, agency owner Hicham discusses maternity arrangements with Andrea. "
         "While Hicham frames his questions as benevolent managerial concern, Andrea maintains strict professional boundaries. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Je sais que ce n'est pas facile.",
  "I know that it is not easy.",
  [(238, "Je sais que c'est pas facile.")], "Adapted negative"),
 ("theo", "On a chacun notre tempérament, c'est humain.",
  "We each have our temperament, it is human.",
  [(239, "on a chacun notre petit tempérament,"), (240, "c'est humain.")], ""),
 ("lea", "On avait dit que je gérais ma grossesse seule.",
  "We agreed that I would manage my pregnancy alone.",
  [(241, "qu'on ne parlait pas"), (242, "et que je gérais ma grossesse")], ""),
 ("theo", "Je me soucie de la santé de mes employés.",
  "I care about the health of my employees.",
  [(244, "je ne fais que me soucier de la santé de mes employés.")], ""),
 ("lea", "Oui, je te remercie de ta bienveillance.",
  "Yes, I thank you for your benevolence.",
  [(245, "Oui, je te remercie de ta bienveillance.")], ""),
 ("theo", "Je reste à ta disposition pour ton congé.",
  "I remain at your disposal for your leave.",
  [(246, "je reste évidemment à ta disposition"), (248, "Et ta maternité ?")], "Adapted leave inquiry"),
 ("lea", "Je te demanderai quand je ressentirai le besoin.",
  "I will ask you when I feel the need.",
  [(250, "je le ferai lorsque je ressentirai le besoin.")], "Adapted response"),
 ("theo", "C'est noté. Tout va bien avec ta compagne?",
  "It is noted. Is everything going well with your partner?",
  [(251, "C'est noté."), (252, "Tout va bien avec ta compagne ?")], ""),
 ("lea", "Très bien, merci.",
  "Very well, thank you.",
  [(253, "Très bien, merci.")], ""),
 ("theo", "J'en suis ravi. Transmets-lui mes amitiés.",
  "I am delighted. Pass along my warm regards to her.",
  [(254, "J'en suis ravi."), (255, "Tu lui transmettras mes amitiés.")], ""),
 ("lea", "Je n'y manquerai pas.",
  "I will not fail to do so.",
  [(256, "J'y manquerai pas.")], ""),
 ("theo", "Bonne journée, Andréa.",
  "Have a good day, Andrea.",
  [(257, "Bonne journée.")], "Added Andrea"),
 ("lea", "Cordialement, Hicham.",
  "Cordially, Hicham.",
  [(258, "Cordialement.")], "Added Hicham"),
 ("lea", "Je viens voir Jean Dujardin maintenant.",
  "I am going to see Jean Dujardin now.",
  [(285, "Je viens voir Jean.")], "Adapted client plan"),
 ("theo", "Fais attention à toi sur la route.",
  "Take care of yourself on the road.",
  [(244, "la santé de mes employés.")], "Adapted parting remark"),
 ("lea", "Ne t'inquiète pas, je gère tout.",
  "Do not worry, I manage everything.",
  [(242, "et que je gérais")], "Adapted closing"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'I know that it is not easy.' Hicham acknowledges the workplace pressure. "
  "The introductory clause 'je sais que' validates personal difficulty."),
 (1, None,
  "'We each have our temperament, it is human.' Hicham makes an empathetic concession. "
  "The indefinite pronoun 'chacun' refers to each individual."),
 (2, None,
  "'We agreed that I would manage my pregnancy alone.' Andrea sets firm boundaries. "
  "The imperfect 'gerais' recalls past verbal commitments."),
 (3, None,
  "'I care about the health of my employees.' Hicham defends his managerial intervention. "
  "The pronominal verb 'se soucier de' expresses active concern."),
 (4, None,
  "'Yes, I thank you for your benevolence.' Andrea responds with polite formality. "
  "The abstract noun 'bienveillance' denotes goodwill or kindness."),
 (5, None,
  "'I remain at your disposal for your leave.' Hicham offers administrative support. "
  "The formal idiom 'rester a disposition' expresses ongoing availability."),
 (6, None,
  "'I will ask you when I feel the need.' Andrea defers taking maternity leave. "
  "The future tense 'ressentirai' sets a conditional timeline."),
 (7, None,
  "'It is noted. Is everything going well with your partner?' Hicham inquires courteously about family life. "
  "The noun 'compagne' designates a domestic partner."),
 (8, None,
  "'Very well, thank you.' Andrea keeps her personal life concise. "
  "The polite formula 'tres bien' provides a brief reassuring reply."),
 (9, None,
  "'I am delighted. Pass along my warm regards to her.' Hicham closes the personal inquiry warmly. "
  "The future imperative 'transmettras' functions as a polite request."),
 (10, None,
  "'I will not fail to do so.' Andrea confirms with standard polite phrasing. "
  "The idiomatic verb phrase 'ne pas y manquer' promises compliance."),
 (11, None,
  "'Have a good day, Andrea.' Hicham brings the formal discussion to an end. "
  "The customary greeting 'bonne journee' wraps up the meeting."),
 (12, None,
  "'Cordially, Hicham.' Andrea delivers a delightfully brisk, email-style farewell. "
  "The formal closing adverb 'cordialement' creates dry office humor."),
 (13, None,
  "'I am going to see Jean Dujardin now.' Andrea announces her immediate off-site priority. "
  "The present tense 'viens voir' indicates purposeful motion."),
 (14, None,
  "'Take care of yourself on the road.' Hicham reiterates his paternalistic care. "
  "The imperative 'fais attention' urges caution."),
 (15, None,
  "'Do not worry, I manage everything.' Andrea reasserts total command of her affairs. "
  "The verb 'gerer' underscores professional mastery."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("In his office, Hicham checks in on Andrea's pregnancy and offers maternity assistance. "
         "Guarding her independence with dry wit, Andrea leaves to manage client Jean Dujardin.")
CLOSING = ("lea", "Ne t'inquiète pas, je gère tout.")
