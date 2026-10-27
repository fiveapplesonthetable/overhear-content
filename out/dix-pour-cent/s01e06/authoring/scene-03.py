# Authoring module for dix-pour-cent s01e06 scene 03 (cues 59-91).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-03.py --out out/dix-pour-cent/s01e06/scene-03.json

ID = "dix-pour-cent-s01e06-scene-03"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = "La vérité sur Mathias  (The Truth About Mathias)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie", "mathias": "theo"}
LABELS = {"lea": "Camille", "catherine": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 59-91. Catherine questions Camille about Mathias's visits during her childhood, discovers Camille's age, "
               "and realizes Mathias's affair occurred while Catherine was pregnant. Obscenities in cue 81 are cleaned up.")

INTRO = ("In Camille's apartment, Catherine Barneville has sat down to understand how Mathias's secret daughter "
         "arrived in Paris. Camille insists that coming to ASK was entirely her own decision. But as Catherine digs into "
         "the dates and discovers Camille's exact age, a devastating realization hits her: Mathias had an affair while "
         "Catherine was pregnant with their son Hippolyte. Downstairs in the courtyard, Mathias waits in dread. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "C'est moi qui ai tout fait.",
  "It was all my doing.",
  [(59, "C'est moi qui ai tout fait")], ""),
 ("lea", "Je suis montée à Paris, je suis allée à l'agence.",
  "I came to Paris, I went to the agency.",
  [(60, "Je suis montée à Paris, je suis allée à l'agence")], ""),
 ("lea", "C'était une envie soudaine.",
  "It was a sudden urge.",
  [(61, "C'était une envie soudaine")], ""),
 ("catherine", "Avant ça, tu le voyais de temps en temps?",
  "Before that, did you see him from time to time?",
  [(65, "Avant ça, tu le voyais de temps en temps ?")], ""),
 ("lea", "Quand j'étais petite, une ou deux fois par an.",
  "When I was little, once or twice a year.",
  [(66, "Quand j'étais petite, une ou deux fois par an")], ""),
 ("catherine", "Qu'est-ce que vous faisiez?",
  "What did you do?",
  [(68, "Qu'est-ce que vous faisiez ?")], ""),
 ("lea", "Il m'apportait un cadeau et passait du temps avec moi.",
  "He would bring me a gift and spend time with me.",
  [(69, "Il m'apportait un cadeau"), (69, "passait du temps avec moi")], ""),
 ("catherine", "Vous avez quel âge?",
  "How old are you?",
  [(72, "Vous avez quel âge ?")], ""),
 ("lea", "J'ai eu vingt-trois ans la semaine dernière.",
  "I turned twenty-three last week.",
  [(72, "J'ai eu 23 ans la semaine dernière")], "Number written out in full words"),
 ("catherine", "Prends tes affaires et va-t'en!",
  "Pack your things and get out!",
  [(74, "Prends tes affaires et va-t'en !")], ""),
 ("lea", "On peut se parler avant de crier?",
  "Can we talk before shouting?",
  [(76, "On peut se parler avant de commencer à crier ?")], ""),
 ("catherine", "J'étais enceinte! Pars!",
  "I was pregnant! Leave!",
  [(77, "J'étais enceinte !"), (78, "Pars !")], "The devastating realization"),
 ("mathias", "Je m'inquiète pour toi.",
  "I am worried about you.",
  [(84, "Je m'inquiète pour")], "Down in the courtyard"),
 ("mathias", "Appelle-moi, s'il te plaît.",
  "Call me, please.",
  [(88, "Appelle-moi, hein ?")], "Desperate plea"),
]

OPENER = "Let's examine how this painful family truth comes to light sentence by sentence."

WALK = [
 (0, None,
  "'It was all my doing.' Camille defends Mathias by insisting she came to Paris on her own initiative."),
 (1, None,
  "'I came to Paris, I went to the agency.' She explains that arriving at ASK was her personal journey."),
 (2, None,
  "'It was a sudden urge.' She admits that years of silence ended with an impulsive family visit."),
 (3, None,
  "'Before that, did you see him from time to time?' Catherine asks about secret childhood meetings."),
 (4, None,
  "'When I was little, once or twice a year.' Camille recalls occasional visits during film festivals."),
 (5, None,
  "'What did you do?' Catherine presses for details about how father and daughter spent their time."),
 (6, None,
  "'He would bring me a gift and spend time with me.' Camille describes small presents and brief moments."),
 (7, None,
  "'How old are you?' Catherine asks for Camille's age as she begins calculating the past timeline."),
 (8, None,
  "'I turned twenty-three last week.' Camille states her age, confirming the dates of Mathias's betrayal."),
 (9, None,
  "'Pack your things and get out!' Horrified by the truth, Catherine orders her to leave Paris."),
 (10, None,
  "'Can we talk before shouting?' Camille desperately pleads for calm as emotions boil over."),
 (11, None,
  "'I was pregnant! Leave!' Catherine reveals that she was carrying Hippolyte during the affair."),
 (12, None,
  "'I am worried about you.' Down in the street, Mathias tries to reach Catherine on the phone."),
 (13, None,
  "'Call me, please.' Mathias pleads into the receiver as his family life falls into crisis."),
]

TRANSITION = "Now let's listen to the entire dramatic scene once more in French."

OUTRO = ("The truth is out: Catherine now knows that Mathias betrayed her while she was pregnant with Hippolyte. "
         "This revelation will ignite an explosive crisis for the entire Barneville family. See you in the next scene.")

CLOSING = ("catherine", "Prends tes affaires et va-t'en!")
