# Authoring module for dix-pour-cent s03e04 scene 25 (cues 1302-1304).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-25.py --out out/dix-pour-cent/s03e04/scene-25.json

ID = "dix-pour-cent-s03e04-scene-25"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 25
TITLE = "L'envoi du coursier  (Dispatching the Courier)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 1302-1304. Late at night at ASK, Mathias and Noemie prepare the confidential envelope. "
               "Mathias calls a dispatch service to send the documents across Paris, setting their plan into motion.")

INTRO = ("Late at night inside the quiet offices of ASK, Mathias and Noemie prepare to launch their offensive. "
         "With all the confidential takeover documents sealed inside an envelope, Mathias dials a courier service. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Le dossier secret est enfin prêt.",
  "The secret file is finally ready.",
  [(1302, "coursier")], "Announcing dossier readiness"),
 ("mathias", "Tu as vérifié chaque document important?",
  "Did you verify each important document?",
  [(1302, "coursier")], "Checking documents"),
 ("lea", "Oui, toutes les copies sont là.",
  "Yes, all the copies are there.",
  [(1302, "coursier")], "Confirming copies"),
 ("mathias", "Nous devons agir sans attendre demain.",
  "We must act without waiting for tomorrow.",
  [(1302, "coursier")], "Stressing urgency"),
 ("lea", "Tu appelles le service de livraison?",
  "Are you calling the delivery service?",
  [(1302, "coursier")], "Inquiring about courier"),
 ("mathias", "Oui, je téléphone au coursier maintenant.",
  "Yes, I am phoning the courier now.",
  [(1302, "coursier")], "Calling dispatch"),
 ("mathias", "Bonsoir, je voudrais un coursier.",
  "Good evening, I would like a courier.",
  [(1302, "je voudrais un coursier")], "Requesting courier"),
 ("mathias", "C'est pour le premier arrondissement.",
  "It is for the first arrondissement.",
  [(1303, "1er arrondissement.")], "Specifying destination"),
 ("mathias", "C'est une livraison très urgente.",
  "It is a very urgent delivery.",
  [(1302, "coursier")], "Stressing speed"),
 ("mathias", "Merci beaucoup, à tout de suite.",
  "Thank you very much, see you shortly.",
  [(1302, "coursier")], "Concluding call"),
 ("lea", "Le coursier arrive dans dix minutes.",
  "The courier arrives in ten minutes.",
  [(1302, "coursier")], "Noting arrival time"),
 ("mathias", "Ce soir, notre plan commence enfin.",
  "Tonight, our plan finally begins.",
  [(1302, "coursier")], "Marking turning point"),
 ("lea", "Nous allons reprendre notre agence, Mathias.",
  "We are going to take back our agency, Mathias.",
  [(1302, "coursier")], "Expressing determination"),
 ("mathias", "Merci pour ta confiance, chère Noémie.",
  "Thank you for your trust, dear Noemie.",
  [(1302, "coursier")], "Expressing gratitude"),
]

WALK = [
 (0, None,
  "'The secret file is finally ready.' Noemie announces that the dossier is assembled. "
  "The adverb 'enfin' denotes the long-awaited completion of a task."),
 (1, None,
  "'Did you verify each important document?' Mathias checks every detail before sending the paperwork. "
  "The indefinite adjective 'chaque' modifies singular nouns."),
 (2, None,
  "'Yes, all the copies are there.' Noemie confirms the documents have been duplicated properly. "
  "The feminine plural 'toutes les' modifies plural feminine nouns."),
 (3, None,
  "'We must act without waiting for tomorrow.' Mathias stresses the urgent necessity of moving immediately. "
  "The preposition 'sans' means without."),
 (4, None,
  "'Are you calling the delivery service?' Noemie asks as Mathias reaches for the telephone. "
  "The noun 'livraison' refers to courier dispatch."),
 (5, None,
  "'Yes, I am phoning the courier now.' Mathias prepares to dispatch the envelope across Paris. "
  "The noun 'coursier' designates a bicycle or motorcycle courier."),
 (6, None,
  "'Good evening, I would like a courier.' Mathias places the telephone request for rapid pickup. "
  "The conditional 'je voudrais' expresses a polite order."),
 (7, None,
  "'It is for the first arrondissement.' Mathias gives the central destination address in Paris. "
  "The ordinal 'premier' indicates the 1st district of Paris."),
 (8, None,
  "'It is a very urgent delivery.' Mathias informs dispatch that speed is essential. "
  "The adjective 'urgente' agrees with the feminine noun livraison."),
 (9, None,
  "'Thank you very much, see you shortly.' Mathias closes the phone call politely. "
  "The locution 'a tout de suite' means see you in a moment."),
 (10, None,
  "'The courier arrives in ten minutes.' Noemie prepares the sealed package for dispatch. "
  "The preposition 'dans' indicates time until an event."),
 (11, None,
  "'Tonight, our plan finally begins.' Mathias reflects on the launch of their campaign. "
  "The noun 'plan' refers to a strategic scheme."),
 (12, None,
  "'We are going to take back our agency, Mathias.' Noemie reaffirms their joint partnership and ambition. "
  "The infinitive 'reprendre' means to recover or reclaim."),
 (13, None,
  "'Thank you for your trust, dear Noemie.' Mathias acknowledges her steadfast loyalty. "
  "The noun 'confiance' means faith or trust in someone."),
]

OUTRO = ("The courier is dispatched into the Parisian night with the crucial documents that will seal ASK's destiny. "
         "Mathias and Noemie stand united, poised for the dramatic confrontation ahead. "
         "Now, let's review the scene one last time.")

CLOSING = ("mathias", "Ce soir, notre plan commence enfin.")
