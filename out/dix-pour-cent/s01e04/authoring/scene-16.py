# Authoring module for dix-pour-cent s01e04 scene 16 (cues 388-421).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-16.py --out out/dix-pour-cent/s01e04/scene-16.json

ID = "dix-pour-cent-s01e04-scene-16"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 16
TITLE = "Démonstration de pole dance  (Pole-Dancing Demo)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "augustin": "marcel"}
LABELS = {"lea": "Audrey", "mathias": "Mathias", "augustin": "Augustin"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 388-421. Outside the office, Noémie giving the children a toy and Arlette worrying about her dog "
               "catching germs (388-392) is told in the intro. Augustin's long description of the recycling-centre "
               "scene (403-406) is condensed to cue 406.")

INTRO = ("Audrey has just discovered that Augustin's film shoots for a whole month in Canada, something Mathias "
         "conveniently forgot to mention. Outside in the corridor, Noémie keeps Audrey's children busy with a little "
         "present while Arlette hurries past, worried that her dog Jean Gabin might catch their germs. Back in "
         "Mathias's office, Augustin asks Audrey a decisive question about the role: can she really pole dance? "
         "Let's listen in French first; don't worry about catching every word.")

STORY = [
 ("augustin", "Pour la danse à la barre, je sais que vous faites du tango.",
  "For the pole dancing, I know that you do the tango.",
  [(393, "Pour la danse à la barre"), (393, "je sais que vous faites du tango")], ""),
 ("lea", "Non, je sais aussi faire un peu de barre.",
  "No, I also know how to do a bit of pole dancing.",
  [(394, "Non, je sais aussi faire un peu de barre")], ""),
 ("augustin", "Ah bon? Vous savez vraiment faire de la barre?",
  "Really? Do you really know how to pole dance?",
  [(395, "Ah bon"), (397, "Vous savez vraiment faire de la barre")], ""),
 ("lea", "Oui. Je connais les bases.",
  "Yes. I know the basics.",
  [(398, "Oui"), (399, "Je connais les bases")], "'disons' omitted"),
 ("augustin", "C'est largement suffisant. Fantastique!",
  "That's more than enough. Fantastic!",
  [(400, "C'est largement suffisant. Fantastique")], ""),
 ("augustin", "J'aime travailler avec le vrai.",
  "I like to work with what's real.",
  [(401, "J'aime travailler avec le vrai")], ""),
 ("augustin", "Dans le film, c'est un geste de rébellion.",
  "In the film, it's a gesture of rebellion.",
  [(406, "un geste de rébellion")], "cues 403-406 simplified"),
 ("augustin", "Elle ressemble à Isabelle Adjani.",
  "She looks like Isabelle Adjani.",
  [(407, "Elle ressemble à Isabelle Adjani")], ""),
 ("lea", "Fermez à clé!",
  "Lock the door!",
  [(408, "Fermez à clé")], "second sentence omitted"),
 ("mathias", "Il n'y a pas de clé.",
  "There is no key.",
  [(409, "Il n'y a pas de clé")], ""),
 ("lea", "Maintenez la porte fermée et tirez les rideaux.",
  "Hold the door closed and draw the curtains.",
  [(410, "Maintenez la porte fermée et tirez les rideaux")], ""),
 ("mathias", "Audrey, ça va?",
  "Audrey, are you okay?",
  [(411, "Audrey, ça va")], ""),
 ("augustin", "Vous n'êtes pas fâchée? C'est juste une idée.",
  "You're not angry? It's just an idea.",
  [(412, "Vous n'êtes pas fâchée"), (414, "C'est juste une idée")], ""),
 ("mathias", "Vous pouvez nous laisser cinq minutes?",
  "Can you give us five minutes?",
  [(416, "Vous pouvez nous laisser cinq minutes")], "calling through the door to Arlette"),
 ("mathias", "Dix minutes? Pas de problème.",
  "Ten minutes? No problem.",
  [(418, "Dix minutes"), (419, "Pas de problème")], ""),
 ("augustin", "Magnifique!",
  "Magnificent!",
  [(421, "Magnifique")], ""),
]

OPENER = ("Let's go through the scene together. Augustin brings up the physical side of the part.")

WALK = [
 (0, None,
  "'For the pole dancing, I know that you do the tango.' Literally 'the dance at the bar'. He uses the polite 'you' "
  "with Audrey."),
 (1, None,
  "'No, I also know how to do a bit of pole dancing.' To say you know how to do something in French, you put 'know' "
  "straight before the verb 'to do'."),
 (2, None,
  "'Really? Do you really know how to pole dance?' Augustin can hardly believe his luck."),
 (3, None,
  "'Yes. I know the basics.' Notice that French uses a different verb for 'know' when it's followed by a noun "
  "instead of a verb."),
 (4, None,
  "'That's more than enough. Fantastic!' Literally 'widely sufficient'."),
 (5, None,
  "'I like to work with what's real.' Literally 'with the true'."),
 (6, None,
  "'In the film, it's a gesture of rebellion.' Augustin launches into his big artistic vision for the character."),
 (7, None,
  "'She looks like Isabelle Adjani.' The verb for 'resembles' takes the preposition 'to' before the person's name."),
 (8, None,
  "'Lock the door!' Literally 'close with a key'. Audrey has decided to prove right here and now that she can dance."),
 (9, None,
  "'There is no key.' The negative 'there is not' is followed by 'of', meaning 'no key at all'."),
 (10, None,
  "'Hold the door closed and draw the curtains.' Two polite commands, because she doesn't want the whole agency "
  "watching through the glass."),
 (11, None,
  "'Audrey, are you okay?' Mathias has no idea what his client is about to do."),
 (12, None,
  "'You're not angry? It's just an idea.' Augustin is worried he offended her with his script."),
 (13, None,
  "'Can you give us five minutes?' Outside, Arlette tries to open the door, and Mathias leans against it to keep "
  "her out."),
 (14, None,
  "'Ten minutes? No problem.' Meanwhile, Audrey uses the office coat stand as a dance pole."),
 (15, None,
  "'Magnificent!' Augustin is completely won over: the part is hers."),
]

TRANSITION = "Now let's hear the whole scene in Mathias's office again."

OUTRO = ("Audrey has won the role on the spot, even if she now has to learn pole dancing for real. Next, Andréa "
         "sends Camille on an errand with Hippolyte. See you there.")
CLOSING = ("mathias", "C'est bon!")
