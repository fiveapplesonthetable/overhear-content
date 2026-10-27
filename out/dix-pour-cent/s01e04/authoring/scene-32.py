# Authoring module for dix-pour-cent s01e04 scene 32 (cues 838-861).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-32.py --out out/dix-pour-cent/s01e04/scene-32.json

ID = "dix-pour-cent-s01e04-scene-32"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 32
TITLE = "Le héros du jour  (The Hero of the Day)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "arlette": "Arlette", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 838-861. Gabriel's lines in the group celebration are shared between Arlette and Andréa to stay "
               "within three voices; 'M.' in cue 841 is written out as 'monsieur'; feminine 'Désolée' is used in "
               "cue 845 for Andréa; conditional perfect 'J'aurais tellement voulu que Samuel voie ça' (851) is "
               "simplified to A1 'Samuel serait si fier de nous!'.")

INTRO = ("In the final scene of the fourth episode, the whole agency gathers with glasses of sparkling wine to "
         "celebrate Mathias Barneville. Everyone believes he pretended to join their rival StarMédia just to scare "
         "off the German buyer and save ASK—and now that he is a hero here, Mathias can hardly leave! Only Andréa "
         "still has a quiet doubt. Listen to the French first, without worrying about catching every word.")

STORY = [
 ("arlette", "Champagne! Faire croire à tout le monde que tu allais chez nos rivaux pour sauver l'agence!",
  "Champagne! Making everyone believe you were going to our rivals to save the agency!",
  [(838, "Champagne"), (839, "Faire croire à tout le monde que tu allais chez nos rivaux"), (840, "pour sauver l'agence")], ""),
 ("lea", "Vivre dangereusement! Respect, monsieur Barneville!",
  "Living dangerously! Respect, Mr Barneville!",
  [(840, "Vivre dangereusement"), (841, "Respect"), (841, "Barneville")], "'M.' written out as 'monsieur'"),
 ("arlette", "Le héros du jour! Mathias, vous entrerez dans l'histoire.",
  "The hero of the day! Mathias, you'll go down in history.",
  [(842, "Le héros du jour"), (844, "Mathias, vous entrerez dans l'histoire")], ""),
 ("lea", "Désolée de vous avoir insulté. Dîner demain?",
  "Sorry for insulting you. Dinner tomorrow?",
  [(845, "de vous avoir insulté"), (846, "Dîner demain")], "feminine 'Désolée'"),
 ("arlette", "Jean Gabin aussi. Dis pardon, Jean Gabin.",
  "Jean Gabin too. Say sorry, Jean Gabin.",
  [(847, "Jean Gabin aussi. Dis pardon, Jean Gabin")], ""),
 ("mathias", "Laisse tomber.", "Forget it.",
  [(848, "Laisse tomber")], ""),
 ("lea", "Pourquoi vous ne nous avez rien dit?",
  "Why didn't you tell us anything?",
  [(849, "Pourquoi vous ne nous avez rien dit")], "'Mais quel idiot !' omitted"),
 ("mathias", "Je ne voulais prendre aucun risque.",
  "I didn't want to take any risk.",
  [(850, "Je ne voulais prendre aucun risque")], ""),
 ("arlette", "Samuel serait si fier de nous! Encore une goutte.",
  "Samuel would be so proud of us! Another drop.",
  [(851, "Samuel"), (852, "Encore une goutte")],
  "subjunctive/conditional perfect in 851 simplified to A1"),
 ("lea", "Vous n'alliez jamais partir?", "You were never going to leave?",
  [(853, "Vous n'alliez jamais partir")], ""),
 ("mathias", "Non! Vous en doutez?", "No! Do you doubt it?",
  [(854, "Non"), (854, "Vous en doutez")], ""),
 ("lea", "Un peu. Mais c'est moi.", "A bit. But that's me.",
  [(855, "Un peu. Mais c'est moi")], ""),
 ("mathias", "Quel rabat-joie! On trinque?",
  "What a killjoy! Shall we clink glasses?",
  [(856, "Quel rabat-joie"), (857, "On trinque")], ""),
 ("lea", "Oui! À ASK!", "Yes! To ASK!",
  [(857, "Oui"), (858, "À ASK")], ""),
 ("arlette", "À ASK! Longue vie!", "To ASK! Long life!",
  [(858, "À ASK"), (859, "Longue vie")], ""),
 ("mathias", "Il est bon, ce pétillant. Un peu jeune.",
  "It's good, this bubbly. A bit young.",
  [(860, "Il est bon, ce pétillant"), (861, "Un peu jeune")], ""),
]

OPENER = ("Let's go through it line by line. The corks pop and everyone raises a glass to Mathias.")

WALK = [
 (0, None,
  "'Champagne! Making everyone believe you were going to our rivals to save the agency!' The two-verb phrase at "
  "the start literally means 'to make believe to everyone'."),
 (1, None,
  "'Living dangerously! Respect, Mr Barneville!' Andréa teases him with his formal title."),
 (2, None,
  "'The hero of the day! Mathias, you'll go down in history.' Literally 'you will enter into history', using the "
  "future tense."),
 (3, None,
  "'Sorry for insulting you. Dinner tomorrow?' Earlier, when they thought Mathias was betraying them, Andréa "
  "threatened to sue him."),
 (4, None,
  "'Jean Gabin too. Say sorry, Jean Gabin.' Arlette tells her little dog—who bit Mathias's ankle earlier—to "
  "apologise too."),
 (5, None,
  "'Forget it.' Literally 'let fall', the everyday French idiom for 'never mind' or 'drop it'. Mathias still "
  "doesn't want the dog near his leg!"),
 (6, None,
  "'Why didn't you tell us anything?' Notice the word for 'nothing' placed between the helper verb 'have' and "
  "'told'."),
 (7, None,
  "'I didn't want to take any risk.' With a straight face, Mathias plays the part of the secret mastermind."),
 (8, None,
  "'Samuel would be so proud of us! Another drop.' Arlette holds out her glass for a little more wine."),
 (9, None,
  "'You were never going to leave?' Quietly, Andréa looks Mathias in the eye. The negative wraps 'never' around "
  "'were going'."),
 (10, None,
  "'No! Do you doubt it?' Again the little word before 'doubt' means 'of it'."),
 (11, None,
  "'A bit. But that's me.' Andréa knows Mathias too well to believe he is a saint, even if she can't prove it."),
 (12, "Quel rabat-joie!",
  "'What a killjoy!' Literally 'what a joy-folder', a colourful compound noun for someone who spoils the mood."),
 (12, "On trinque?",
  "'Shall we clink glasses?' French has a single verb for clinking glasses together in a toast."),
 (13, None,
  "'Yes! To ASK!' In a toast, you simply put the preposition 'to' before the name."),
 (14, None,
  "'To ASK! Long life!' Notice how the adjective 'long' comes before the noun in this fixed wish."),
 (15, None,
  "'It's good, this bubbly. A bit young.' Even at his own triumph, snobbish Mathias cannot resist judging the "
  "cheap sparkling wine."),
]

TRANSITION = "Now let's hear the whole celebration again from start to finish."

OUTRO = ("That wraps up the fourth episode of Call My Agent: Audrey Fleurot has a new comedy film to pay off her "
         "taxes, Sofia has her very first screen role, Colette knows the truth about the Hotel Saint-Georges, and "
         "Mathias is staying at ASK as an accidental hero. See you soon for episode five!")
CLOSING = ("arlette", "À ASK! Longue vie!")
