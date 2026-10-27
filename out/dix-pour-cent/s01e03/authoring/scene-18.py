# Authoring module for dix-pour-cent s01e03 scene 18 (cues 446-489).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e03/authoring/scene-18.py --out out/dix-pour-cent/s01e03/scene-18.json

ID = "dix-pour-cent-s01e03-scene-18"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 18
TITLE = "Le caprice de Laura  (Laura's Diva Act)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "solveig": "emilie", "herve": "theo"}
LABELS = {"lea": "Laura", "solveig": "Solveig", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 446-489. The brief crossover at the lift after Nathalie's audition (446-455) is told in the intro. "
               "Gabriel's request to Hervé (467-468) is given to Laura in the first person to stay within three voices. "
               "Gabriel's voicemail at the end (483-489, with swearing in 488) is told cleanly by the narrator in the outro.")

INTRO = ("Nathalie tried her best to spoil her audition, and failed completely: she was wonderful, and as she leaves "
         "with Mathias she cheerfully tells Laura and Gabriel outside the lift that it went magnificently. "
         "Now it is Laura's turn with the director Solveig Akerfelt. Remember Gabriel's plan: since Solveig hates "
         "difficult stars, Laura is going to play an impossible diva so that Solveig turns her down. "
         "Listen to the scene in French first, and just enjoy the performance.")

STORY = [
 ("solveig", "C'est l'isolement de la mère et de la fille qui m'intéresse.",
  "It's the isolation of the mother and the daughter that interests me.",
  [(457, "C'est l'isolement de la mère et de la fille qui m'intéresse")], ""),
 ("solveig", "Et leur relation intense sur l'île.",
  "And their intense relationship on the island.",
  [(458, "leur relation intense sur l'île")], "'de Bergman' omitted"),
 ("solveig", "C'est une bombe à retardement.",
  "It's a time bomb.",
  [(459, "C'est une bombe à retardement")], ""),
 ("lea", "Oui. C'est ce que je pensais.",
  "Yes. That's what I thought.",
  [(460, "Oui"), (461, "C'est ce que je pensais")], ""),
 ("solveig", "C'est de l'intimité pure.",
  "It's pure intimacy.",
  [(462, "C'est de l'intimité pure")], ""),
 ("lea", "J'avais demandé du thé. Du thé à la fleur d'Himalaya.",
  "I had asked for tea. Himalayan flower tea.",
  [(464, "J'avais demandé du thé"), (465, "Du thé à la fleur d'Himalaya")], ""),
 ("lea", "Hervé, s'il te plaît! Je veux mon thé.",
  "Hervé, please! I want my tea.",
  [(467, "Hervé, s'il te plaît"), (468, "veut du thé")], "Gabriel's line 467-468 adapted in 1st person for Laura"),
 ("herve", "Votre thé, Madame Laura.",
  "Your tea, Miss Laura.",
  [(470, "Votre thé"), (470, "Laura")], "'Mme' written out as 'Madame'"),
 ("herve", "Avec une goutte de lait d'amande, comme vous l'aimez.",
  "With a drop of almond milk, as you like it.",
  [(471, "Avec une goutte de lait d'amande, comme vous l'aimez")], ""),
 ("lea", "Pas infusé trop longtemps?",
  "Not brewed for too long?",
  [(472, "Pas infusé trop longtemps")], ""),
 ("herve", "C'était la dernière fois, je suis désolé.",
  "That was last time, I'm sorry.",
  [(473, "C'était la dernière fois, je suis désolé")], ""),
 ("solveig", "Vous avez terminé?",
  "Have you finished?",
  [(474, "Vous avez terminé")], ""),
 ("lea", "Bien sûr.",
  "Of course.",
  [(475, "Bien sûr")], ""),
 ("lea", "Pharrell? Pharrell Williams!",
  "Pharrell? Oh, Pharrell Williams!",
  [(476, "Pharrell"), (477, "Pharrell Williams")], ""),
 ("lea", "Vous pouvez? C'est à neuf heures.",
  "Can you make it? It's at nine o'clock.",
  [(478, "Vous pouvez"), (479, "C'est à neuf heures")], ""),
 ("lea", "J'avais une répétition avec John Malkovich ce soir?",
  "Did I have a rehearsal with John Malkovich tonight?",
  [(480, "J'avais une répétition avec John Malkovich ce soir")], ""),
 ("lea", "Dis que je suis malade, que je ne peux pas venir.",
  "Say that I'm ill, that I can't come.",
  [(482, "Dis que je suis malade, que je ne peux pas venir")], ""),
]

OPENER = ("Let's walk through it step by step. Solveig starts in her serious, intense way.")

WALK = [
 (0, None,
  "'It's the isolation of the mother and the daughter that interests me.' Notice the frame 'it is ... that' "
  "to put the focus on isolation. At the end, the verb means 'interests me'."),
 (1, None,
  "'And their intense relationship on the island.' In French the adjective 'intense' comes right after the noun."),
 (2, None,
  "'It's a time bomb.' Literally 'a bomb with a delay mechanism'. Solveig is very proud of her metaphor."),
 (3, None,
  "'Yes. That's what I thought.' Literally 'it is that which I was thinking', using the past tense for an ongoing thought."),
 (4, None,
  "'It's pure intimacy.' Again the adjective 'pure' follows the noun. And right in the middle of this deep speech, "
  "Laura launches her act."),
 (5, "J'avais demandé du thé.",
  "'I had asked for tea.' She uses the 'had done' tense, as if she has been waiting for hours."),
 (5, "Du thé à la fleur d'Himalaya.",
  "'Himalayan flower tea.' When you name a flavour or an ingredient in French, you link it with 'to the'."),
 (6, None,
  "'Hervé, please! I want my tea.' She calls the assistant straight into the room, using the casual 'please'."),
 (7, None,
  "'Your tea, Miss Laura.' Poor Hervé hurries in with the cup and plays along very politely."),
 (8, None,
  "'With a drop of almond milk, as you like it.' Literally 'a drop of milk of almond'. The little word before 'like' "
  "is 'it'."),
 (9, None,
  "'Not brewed for too long?' She doesn't even say thank you; she just checks that the tea isn't ruined."),
 (10, None,
  "'That was last time, I'm sorry.' Hervé apologises for an imaginary mistake from the past."),
 (11, None,
  "'Have you finished?' Solveig has been sitting there in disbelief. She uses the polite 'you'."),
 (12, None,
  "'Of course.' And just as Laura says that, her phone rings, and she answers it right in front of the director."),
 (13, None,
  "'Pharrell? Oh, Pharrell Williams!' She pretends a world-famous singer is calling her on her mobile."),
 (14, None,
  "'Can you make it? It's at nine o'clock.' Literally 'You can? It is at nine hours.'"),
 (15, None,
  "'Did I have a rehearsal with John Malkovich tonight?' She turns to Gabriel to drop another famous name."),
 (16, None,
  "'Say that I'm ill, that I can't come.' A casual command at the start: 'say'. Cancelling a rehearsal for a party "
  "is the final straw for Solveig."),
]

TRANSITION = "Now let's hear Laura's whole audition again."

OUTRO = ("Laura's diva act works like a charm: soon after, Gabriel leaves a delighted voicemail on her phone to say "
         "that Solveig Akerfelt found her 'too beautiful for the part', a polite excuse because they don't want a "
         "prima donna. Next we visit Camille at home as she gets ready for the César awards.")
CLOSING = ("lea", "Merci, Hervé.")
