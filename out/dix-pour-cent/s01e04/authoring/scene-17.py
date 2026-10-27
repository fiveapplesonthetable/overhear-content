# Authoring module for dix-pour-cent s01e04 scene 17 (cues 422-441).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-17.py --out out/dix-pour-cent/s01e04/scene-17.json

ID = "dix-pour-cent-s01e04-scene-17"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 17
TITLE = "Photos d'enfance  (Childhood Photos)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie", "hippolyte": "theo"}
LABELS = {"lea": "Camille", "andrea": "Andréa", "hippolyte": "Hippolyte"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 422-441. Cue 431 ('C'est cool') uses 'C'est super'; cue 435 ('un type') uses A1 'un garçon'.")

INTRO = ("While Audrey wins her part in Mathias's office, Andréa calls Camille in for a job. Young actor Hippolyte "
         "Rivière has just landed a role in a detective series, and the production team needs childhood photos of "
         "him. Remember that Camille now knows Hippolyte is Mathias's son — her own half-brother — though Hippolyte "
         "still has no idea. Let's listen in French first, and just follow the flow.")

STORY = [
 ("lea", "Vous vouliez me voir?",
  "Did you want to see me?",
  [(422, "Vous vouliez me voir")], ""),
 ("andrea", "Oui. Vous connaissez Hippolyte Rivière?",
  "Yes. Do you know Hippolyte Rivière?",
  [(422, "Oui. Vous connaissez Hippolyte Rivière")], ""),
 ("lea", "Oui, je le connais.",
  "Yes, I know him.",
  [(423, "Oui")], "expanded from 'Oui'"),
 ("andrea", "Entrez. Il a été choisi pour une série policière.",
  "Come in. He has been chosen for a detective series.",
  [(423, "Entrez"), (424, "Il a été choisi pour une série policière")], ""),
 ("andrea", "On a besoin de photos de lui enfant.",
  "We need photos of him as a child.",
  [(425, "On a besoin de photos de lui enfant")], ""),
 ("andrea", "Accompagnez-le et aidez-le à choisir.",
  "Go with him and help him choose.",
  [(426, "Accompagnez-le et aidez-le à choisir")], ""),
 ("lea", "Quand? Lundi prochain?",
  "When? Next Monday?",
  [(427, "Quand"), (428, "Lundi prochain")], ""),
 ("andrea", "Non, Camille, maintenant!",
  "No, Camille, now!",
  [(429, "Non, Camille, maintenant")], ""),
 ("lea", "D'accord.",
  "Okay.",
  [(430, "D'accord")], ""),
 ("lea", "C'est super, d'être choisi pour ça.",
  "It's great, to be chosen for that.",
  [(431, "d'être choisi pour ça")], "'C'est cool' -> 'C'est super'"),
 ("hippolyte", "Oui, je suis content.",
  "Yes, I'm pleased.",
  [(432, "Je suis content")], "'Ouais' -> 'Oui'"),
 ("lea", "C'est un bon rôle?",
  "Is it a good part?",
  [(433, "C'est un bon rôle")], ""),
 ("hippolyte", "Pas mal. Je joue un garçon qui a le cœur brisé.",
  "Not bad. I play a boy who has a broken heart.",
  [(434, "Pas mal"), (434, "Je joue"), (435, "qui a le cœur brisé")], "'un type' -> 'un garçon'"),
 ("hippolyte", "Désolé pour tes messages. J'ai été très occupé.",
  "Sorry about your messages. I've been very busy.",
  [(436, "Désolé"), (436, "tes messages. J'ai été très occupé")], "'de ne pas avoir répondu à' simplified"),
 ("hippolyte", "Mais c'est bon de te voir.",
  "But it's good to see you.",
  [(436, "Mais c'est bon de te voir")], ""),
 ("hippolyte", "On y va sur mon scooter. Tu n'as pas peur?",
  "We're going on my scooter. You're not afraid?",
  [(440, "On y va sur mon scooter"), (441, "Tu n'as pas peur")], ""),
]

OPENER = ("Let's go through it line by line. Camille knocks at Andréa's door.")

WALK = [
 (0, None,
  "'Did you want to see me?' She uses the past tense for 'wanted', which sounds polite and tentative."),
 (1, None,
  "'Yes. Do you know Hippolyte Rivière?' Andréa is already standing there with him."),
 (2, None,
  "'Yes, I know him.' The little word before the verb means 'him'."),
 (3, None,
  "'Come in. He has been chosen for a detective series.' Literally 'a police series'."),
 (4, None,
  "'We need photos of him as a child.' The everyday expression for 'to need' literally means 'to have need of'."),
 (5, None,
  "'Go with him and help him choose.' Two polite commands, each with the word for 'him' joined to the verb by a hyphen."),
 (6, None,
  "'When? Next Monday?' In French, 'next' comes after the day of the week."),
 (7, None,
  "'No, Camille, now!' With Andréa, everything is urgent."),
 (8, None,
  "'Okay.' Camille has no choice but to go with Hippolyte."),
 (9, None,
  "'It's great, to be chosen for that.' As they walk to the lift, Camille congratulates him."),
 (10, None,
  "'Yes, I'm pleased.' Notice the masculine form of 'pleased' for Hippolyte."),
 (11, None,
  "'Is it a good part?' A simple question about his new role."),
 (12, None,
  "'Not bad. I play a boy who has a broken heart.' Literally 'the broken heart'."),
 (13, None,
  "'Sorry about your messages. I've been very busy.' He switches to the casual 'your' with her, as he has since "
  "they met."),
 (14, None,
  "'But it's good to see you.' Hippolyte is still clearly charmed by her."),
 (15, "On y va sur mon scooter.",
  "'We're going on my scooter.' Outside the building, his scooter is waiting."),
 (15, "Tu n'as pas peur?",
  "'You're not afraid?' In French you 'have fear' rather than 'are afraid'."),
]

TRANSITION = "Now let's listen to the whole scene again."

OUTRO = ("Camille says she's never afraid, and off they ride to the Barneville family house. Next, they look through "
         "the photos, and someone unexpected walks in. See you there.")
CLOSING = ("lea", "Jamais!")
