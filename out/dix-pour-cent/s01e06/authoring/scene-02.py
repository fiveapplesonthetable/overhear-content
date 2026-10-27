# Authoring module for dix-pour-cent s01e06 scene 02 (cues 29-58).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-02.py --out out/dix-pour-cent/s01e06/scene-02.json

ID = "dix-pour-cent-s01e06-scene-02"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = "La visite de Catherine  (Catherine's Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie"}
LABELS = {"lea": "Camille", "catherine": "Catherine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 29-58. The theatrical standoff over the inflatable duck is bridged in the intro; the scene follows "
               "Camille's late-night phone call with her mother and Catherine Barneville's unexpected arrival.")

INTRO = ("At the theatre, François Berléand furiously shouted that it was either him or the duck before storming off. "
         "Meanwhile, late in the evening, Camille is in her small Paris studio talking on the phone with her mother, "
         "who wants her to come back south to the sunshine. But their conversation is cut short when someone unexpectedly "
         "knocks at Camille's apartment door. It is Catherine Barneville, Mathias's wife. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Sa femme l'aide à racheter l'agence.",
  "His wife is helping him buy back the agency.",
  [(33, "Sa femme l'aide à racheter l'agence")], "On the phone with her mother"),
 ("lea", "Tout le monde panique à cause du contrôle fiscal.",
  "Everyone is panicking because of the tax audit.",
  [(35, "tout le monde panique en ce moment à cause du contrôle fiscal")], ""),
 ("lea", "Non, maman, je suis bien ici.",
  "No, Mum, I feel good here.",
  [(39, "Non, maman"), (40, "Je suis bien ici")], ""),
 ("lea", "C'est qui à cette heure-ci? Je vais voir.",
  "Who is that at this hour? I'll go see.",
  [(43, "C'est qui à cette heure-ci"), (44, "Je vais voir")], ""),
 ("lea", "Oui? Catherine?",
  "Yes? Catherine?",
  [(45, "Oui"), (46, "Catherine")], "Surprised through the door"),
 ("catherine", "Catherine.",
  "It's Catherine.",
  [(47, "Catherine")], "Confirming her name"),
 ("lea", "Catherine qui? La femme de mon père?",
  "Catherine who? My father's wife?",
  [(48, "Catherine qui"), (48, "La femme de ton père")], "Pronoun adjusted from conversation context"),
 ("lea", "Au fond de la cour, à gauche.",
  "At the back of the courtyard, on the left.",
  [(49, "Au fond de la cour, à gauche")], "Directions to her studio door"),
 ("lea", "Bisous, maman!",
  "Kisses, Mum!",
  [(50, "Bisous, maman")], "Quickly hanging up"),
 ("catherine", "Ça me calme.",
  "It calms me down.",
  [(53, "Ça me calme")], "Holding her drink"),
 ("catherine", "Tu en veux?",
  "Do you want some?",
  [(54, "T'en veux")], "Standard pronoun form"),
 ("lea", "Non, merci. Qu'est-ce que tu veux?",
  "No, thank you. What do you want?",
  [(54, "Non, merci"), (55, "Qu'est-ce que tu veux")], ""),
 ("catherine", "Comprendre. Ou du moins essayer.",
  "To understand. Or at least try.",
  [(56, "Comprendre. Ou du moins essayer")], ""),
 ("catherine", "Jus d'orange ou bière?",
  "Orange juice or beer?",
  [(58, "Jus d'orange ou bière")], ""),
]

OPENER = "Let's walk through this unexpected midnight encounter step by step."

WALK = [
 (0, None,
  "'His wife is helping him buy back the agency.' Camille explains the financial situation to her mother."),
 (1, None,
  "'Everyone is panicking because of the tax audit.' She describes the growing stress among the agents."),
 (2, None,
  "'No, Mum, I feel good here.' Camille firmly resists her mother's plea to return to the sunny south."),
 (3, None,
  "'Who is that at this hour? I'll go see.' Hearing a knock, Camille checks who is in the courtyard."),
 (4, None,
  "'Yes? Catherine?' Through the intercom, Camille asks for the late-night visitor's identity."),
 (5, None,
  "'It's Catherine.' The visitor repeats her first name calmly without introducing her family title."),
 (6, None,
  "'Catherine who? My father's wife?' Camille pieces together who it is that has tracked down her apartment."),
 (7, None,
  "'At the back of the courtyard, on the left.' She provides directions to reach her studio doorway."),
 (8, None,
  "'Kisses, Mum!' Camille quickly cuts the phone call short before Catherine enters the room."),
 (9, None,
  "'It calms me down.' Stepping inside, Catherine explains that a drink helps steady her nervous feelings."),
 (10, None,
  "'Do you want some?' She politely offers to share a beverage with the nervous young assistant."),
 (11, None,
  "'No, thank you. What do you want?' Camille declines the offer and gets straight to the point."),
 (12, None,
  "'To understand. Or at least try.' Catherine explains her honest desire to uncover the hidden truth."),
 (13, None,
  "'Orange juice or beer?' She offers two everyday refreshments as the confrontation gets underway."),
]

TRANSITION = "Now let's listen to the dialogue once more without interruption."

OUTRO = ("Catherine has tracked down Camille's apartment to discover the truth about Mathias's secret past. "
         "The tension between them is palpable as their confrontation unfolds. See you in the next scene.")

CLOSING = ("catherine", "Comprendre. Ou du moins essayer.")
