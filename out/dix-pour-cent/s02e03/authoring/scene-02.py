# Authoring module for dix-pour-cent s02e03 scene 02 (cues 32-67).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-02.py --out out/dix-pour-cent/s02e03/scene-02.json

ID = "dix-pour-cent-s02e03-scene-02"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 2
TITLE = "Gabriel négocie à l'accueil  (Begging the Receptionist)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Réceptionniste", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 32-67. Gabriel tries desperately to convince the driving test center receptionist "
               "to schedule an earlier test date for Norman Thavaud. Adapted for A1 French.")

INTRO = ("At the driving exam registration office, Gabriel Sarda desperately attempts to negotiate an early "
         "test date for Norman. With the film shoot fast approaching, every week counts, but the strict receptionist "
         "refuses to grant special treatment. Let's listen to the scene in French first.")

STORY = [
 ("lea", "Il n'y a rien de disponible pour avril.",
  "There is nothing available for April.",
  [(32, "Rien de disponible pour avril.")], "Added full verbal structure"),
 ("lea", "La prochaine date est le seize juin.",
  "The next date is June sixteenth.",
  [(35, "Le 16 juin.")], "Spelled out date"),
 ("gabriel", "C'est beaucoup trop tard, ça ne va pas.",
  "It is much too late, that will not work.",
  [(36, "Trop tard, ça ne va pas.")], "Added adverbial emphasis"),
 ("gabriel", "Mon client joue dans un grand film.",
  "My client acts in a major movie.",
  [(39, "Mon client, Norman Thavaud, joue dans le nouveau film de Jacques Audiard.")], "Simplified film reference"),
 ("lea", "Norman? Mes enfants parlent souvent de lui.",
  "Norman? My children often talk about him.",
  [(41, "Norman ? Mes enfants parlent de lui.")], "Added frequency adverb"),
 ("gabriel", "Exactement, c'est un moment clé pour lui.",
  "Exactly, it is a key moment for him.",
  [(43, "Exactement."), (44, "C'est pourquoi c'est un moment clé dans sa carrière.")], "Combined agreement and career milestone"),
 ("gabriel", "Dans le film, il joue un chauffeur de taxi.",
  "In the movie, he plays a taxi driver.",
  [(45, "Dans le film il joue un jeune chauffeur de taxi")], "Kept central role"),
 ("gabriel", "Le tournage commence dans deux semaines seulement.",
  "The shooting starts in two weeks only.",
  [(48, "Le tournage commence dans deux semaines.")], "Added restrictive adverb"),
 ("lea", "Vous devez simplement reporter ce tournage.",
  "You must simply postpone this shoot.",
  [(49, "Vous devez le reporter.")], "Clarified object"),
 ("gabriel", "Tout le monde est prêt pour tourner.",
  "Everyone is ready to shoot.",
  [(51, "Tout le monde est prêt.")], "Added purposive infinitive"),
 ("gabriel", "Pouvez-vous faire un effort pour nous?",
  "Can you make an effort for us?",
  [(53, "Si vous pouviez faire un effort"), (54, "pour avancer un peu la date...")], "Formulated direct polite request"),
 ("lea", "Non, les règles sont les mêmes pour tous.",
  "No, the rules are the same for all.",
  [(57, "Les règles s'appliquent à tout le monde.")], "Expressed equality of rules"),
 ("lea", "J'ai attendu dix ans pour mes papiers.",
  "I waited ten years for my papers.",
  [(60, "Dix ans j'ai attendu, mais au final,"), (61, "J'ai eu mes papiers.")], "Streamlined personal experience"),
 ("lea", "Alors, vous voulez le seize juin?",
  "So, do you want June sixteenth?",
  [(66, "Alors..."), (67, "tu veux le 16 juin ?")], "Concluded with final scheduling offer"),
]

OPENER = "Let's examine how Gabriel tries to persuade the driving center receptionist."

WALK = [
 (0, None,
  "'There is nothing available for April.' A negative existential phrase introducing the month."),
 (1, None,
  "'The next date is June sixteenth.' A cardinal date construction specifying the calendar appointment."),
 (2, None,
  "'It is much too late, that will not work.' An emphatic negative evaluation expressing urgency."),
 (3, None,
  "'My client acts in a major movie.' A present tense description introducing the actor's professional role."),
 (4, None,
  "'Norman? My children often talk about him.' An interrogative reaction followed by an indirect object pronoun."),
 (5, None,
  "'Exactly, it is a key moment for him.' An adverb of affirmation paired with a defining career moment."),
 (6, None,
  "'In the movie, he plays a taxi driver.' A prepositional locator describing the character's occupation."),
 (7, None,
  "'The shooting starts in two weeks only.' A temporal construction expressing imminent production."),
 (8, None,
  "'You must simply postpone this shoot.' A modal verb expressing an uncompromising practical solution."),
 (9, None,
  "'Everyone is ready to shoot.' An indefinite subject pronoun followed by an adjective of readiness."),
 (10, None,
  "'Can you make an effort for us?' An inverted formal question asking for special assistance."),
 (11, None,
  "'No, the rules are the same for all.' An assertion of bureaucratic fairness rejecting exceptionalism."),
 (12, None,
  "'I waited ten years for my papers.' A compound past verb illustrating personal resilience and delay."),
 (13, None,
  "'So, do you want June sixteenth?' A transitional question offering the only remaining appointment."),
]

TRANSITION = "Now let's listen to Gabriel's tense discussion at the counter again at full speed."

OUTRO = ("The receptionist refuses to bend the rules for a celebrity client, reminding Gabriel that everyone must wait. "
         "Faced with a two-month delay, Gabriel must find another solution for Norman's role.")

CLOSING = ("lea", "Au revoir, monsieur.")
