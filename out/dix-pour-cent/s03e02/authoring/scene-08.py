# Authoring module for dix-pour-cent s03e02 scene 08 (cues 541-547).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-08.py --out out/dix-pour-cent/s03e02/scene-08.json

ID = "dix-pour-cent-s03e02-scene-08"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 8
TITLE = "Fin de soirée  (End of the Evening)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Chantal", "theo": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 541-547. Outside her apartment late at night, Gabriel says goodnight to Chantal "
               "after their evening together. Adapted for A1 French.")

INTRO = ("Late at night outside her apartment building, Gabriel walks Chantal to her entrance. "
         "After spending the evening together, the two share a hesitant and polite goodnight farewell. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Voilà, nous sommes arrivés devant chez toi.",
  "Here we are, we have arrived in front of your place.",
  [(541, "Voilà.")], "Adapted arrival"),
 ("lea", "Merci pour cette très belle soirée.",
  "Thank you for this very lovely evening.",
  [(541, "Voilà.")], "Adapted gratitude"),
 ("theo", "Bon, il est tard maintenant.",
  "Well, it is late now.",
  [(542, "Bon, il est tard,")], ""),
 ("theo", "Le temps passe très vite avec toi.",
  "Time passes very quickly with you.",
  [(542, "il est tard, bref.")], "Adapted compliment"),
 ("lea", "Oui, j'ai passé un excellent moment.",
  "Yes, I had an excellent time.",
  [(541, "Voilà.")], "Adapted agreement"),
 ("theo", "Je dois y aller maintenant.",
  "I must get going now.",
  [(543, "je vais y aller.")], ""),
 ("lea", "Tu as une longue journée demain?",
  "Do you have a long day tomorrow?",
  [(542, "il est tard,")], "Adapted inquiry"),
 ("theo", "Oui, j'ai beaucoup de travail à l'agence.",
  "Yes, I have a lot of work at the agency.",
  [(543, "je vais y aller.")], "Adapted reply"),
 ("lea", "Alors tu dois bien te reposer.",
  "Then you must rest well.",
  [(545, "Bonne nuit,")], "Adapted advice"),
 ("theo", "Toi aussi, repose-toi bien.",
  "You too, rest well.",
  [(545, "Bonne nuit, Chantal.")], "Adapted wish"),
 ("theo", "Bonne nuit, Chantal.",
  "Good night, Chantal.",
  [(545, "Bonne nuit, Chantal.")], ""),
 ("lea", "Bonne nuit, Gabriel.",
  "Good night, Gabriel.",
  [(546, "Bonne nuit, Gabrielle.")], ""),
 ("theo", "On s'appelle bientôt?",
  "Shall we call each other soon?",
  [(547, "On s'appelle ?")], "Adapted question"),
 ("lea", "Oui, avec grand plaisir.",
  "Yes, with great pleasure.",
  [(547, "On s'appelle ?")], "Adapted confirmation"),
 ("theo", "Je t'appelle demain après-midi.",
  "I will call you tomorrow afternoon.",
  [(547, "On s'appelle ?")], "Adapted promise"),
 ("lea", "D'accord, à demain, Gabriel.",
  "Okay, see you tomorrow, Gabriel.",
  [(546, "Bonne nuit, Gabrielle.")], "Adapted closing"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Here we are, we have arrived in front of your place.' Gabriel signals the end of the walk home. "
  "The particle 'voila' marks arrival at a destination."),
 (1, None,
  "'Thank you for this very lovely evening.' Chantal expresses polite appreciation. "
  "The feminine noun phrase 'cette tres belle soiree' praises the shared time."),
 (2, None,
  "'Well, it is late now.' Gabriel notices the late hour. "
  "The impersonal expression 'il est tard' states the late time of night."),
 (3, None,
  "'Time passes very quickly with you.' Gabriel pays a gentle compliment. "
  "The adverbial phrase 'tres vite' emphasizes how fast time flew by."),
 (4, None,
  "'Yes, I had an excellent time.' Chantal confirms her enjoyment. "
  "The compound past 'ai passe' describes a completed positive experience."),
 (5, None,
  "'I must get going now.' Gabriel prepares to leave. "
  "The modal verb 'dois' followed by the adverbial pronoun 'y' expresses impending departure."),
 (6, None,
  "'Do you have a long day tomorrow?' Chantal inquires about his schedule. "
  "The adjective 'longue' qualifies the upcoming workday."),
 (7, None,
  "'Yes, I have a lot of work at the agency.' Gabriel explains his professional obligations. "
  "The noun 'agence' refers to ASK."),
 (8, None,
  "'Then you must rest well.' Chantal offers considerate advice. "
  "The reflexive structure 'te reposer' expresses getting rest."),
 (9, None,
  "'You too, rest well.' Gabriel returns the affectionate wish. "
  "The imperative 'repose-toi' directly bids someone to rest."),
 (10, None,
  "'Good night, Chantal.' Gabriel offers a formal bedtime farewell. "
  "The standard polite formula 'bonne nuit' bids someone good night."),
 (11, None,
  "'Good night, Gabriel.' Chantal replies in kind. "
  "The reciprocal greeting concludes their conversation outside her door."),
 (12, None,
  "'Shall we call each other soon?' Gabriel suggests a future contact. "
  "The pronominal verb 's'appeler' expresses mutual phoning."),
 (13, None,
  "'Yes, with great pleasure.' Chantal accepts with enthusiasm. "
  "The polite idiom 'avec grand plaisir' confirms keen agreement."),
 (14, None,
  "'I will call you tomorrow afternoon.' Gabriel sets a specific time frame. "
  "The time expression 'demain apres-midi' denotes the next day."),
 (15, None,
  "'Okay, see you tomorrow, Gabriel.' Chantal brings the parting to a close. "
  "The parting phrase 'a demain' anticipates their next conversation."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Outside her building, Gabriel and Chantal exchange polite farewells after an evening out. "
         "Agreeing to talk again soon, Gabriel heads home.")
CLOSING = ("theo", "On s'appelle bientôt?")
