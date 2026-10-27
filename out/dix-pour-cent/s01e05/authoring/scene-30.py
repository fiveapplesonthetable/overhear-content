# Authoring module for dix-pour-cent s01e05 scene 30 (cues 698-739).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-30.py --out out/dix-pour-cent/s01e05/scene-30.json

ID = "dix-pour-cent-s01e05-scene-30"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 30
TITLE = "J'ai quelque chose à te dire  (I Have Something to Tell You)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "catherine": "emilie"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "catherine": "Catherine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 698-739. To stay within three voices (Camille, Mathias, Catherine), Hippolyte's angry questions "
               "in the hallway in cues 725-734 are narrated while Mathias, Camille, and Catherine speak their lines.")

INTRO = ("Late at night at the agency, Camille is getting ready to go home when Mathias knocks on her office door. "
         "All day long, Camille thought her father had forgotten her twenty-third birthday — and meanwhile, across "
         "town, Catherine and Hippolyte are waiting for Mathias outside the opera house, unable to reach him on his "
         "phone. Listen to the French first, without worrying about catching every word.")

STORY = [
 ("mathias", "Vous avez une minute? J'ai oublié quelque chose.",
  "Do you have a minute? I forgot something.",
  [(698, "Vous avez une minute"), (698, "J'ai oublié quelque chose")], ""),
 ("lea", "Quoi, ici, dans ce bureau?",
  "What, here, in this office?",
  [(699, "Quoi, ici, dans ce bureau")], ""),
 ("mathias", "Votre anniversaire.",
  "Your birthday.",
  [(700, "Votre anniversaire")], ""),
 ("lea", "Ah oui. C'est pas grave. Et j'ai pas six ans!",
  "Oh, yes. It's no big deal. And I'm not six years old!",
  [(701, "Ah oui. C'est pas grave"), (702, "Et j'ai pas six ans")], ""),
 ("mathias", "Bref, qu'est-ce qui vous ferait plaisir? Vous devez bien avoir une idée.",
  "Anyway, what would make you happy? You must have some idea.",
  [(705, "Bref, qu'est-ce qui vous ferait plaisir"), (706, "Vous devez bien avoir une idée")], ""),
 ("lea", "Quand je suis arrivée au centre d'examen, j'ai coincé la portière sur la main de l'examinateur.",
  "When I arrived at the test center, I caught the car door on the examiner's hand.",
  [(713, "Quand je suis arrivée au centre d'examen"), (714, "j'ai coincé la portière sur la main de l'examinateur")], ""),
 ("mathias", "Non!",
  "No!",
  [(715, "Non")], ""),
 ("lea", "Si! Il avait deux doigts cassés.",
  "Yes! He had two broken fingers.",
  [(715, "Si"), (716, "Il avait deux doigts cassés")], ""),
 ("catherine", "Je pensais vous voir à l'opéra. J'ai laissé des messages.",
  "I thought I'd see you at the opera. I left messages.",
  [(718, "Je pensais vous voir à l'opéra"), (719, "J'ai laissé des messages")], ""),
 ("mathias", "Il était en mode silencieux. Tu veux une coupe? On a sorti le champagne.",
  "It was on silent mode. Do you want a glass? We brought out the champagne.",
  [(720, "Il était en mode silencieux"), (721, "Tu veux une coupe"), (721, "On a sorti le champagne")], ""),
 ("mathias", "Camille m'a beaucoup aidé sur une affaire délicate cette semaine. Et on fête ça.",
  "Camille helped me a lot on a delicate matter this week. And we're celebrating that.",
  [(722, "Camille m'a beaucoup aidé sur une affaire délicate cette semaine"), (723, "Et on fête ça")], ""),
 ("catherine", "Camille n'est pas l'assistante d'Andréa?",
  "Isn't Camille Andréa's assistant?",
  [(724, "Camille n'est pas l'assistante d'Andréa")], ""),
 ("mathias", "Elle peut quand même aider les autres.",
  "She can still help the others.",
  [(724, "Elle peut quand même aider les autres")], ""),
 ("mathias", "C'est pas ce que tu crois. Arrête! C'est son assistante, je voulais juste la remercier, c'est tout.",
  "It's not what you think. Stop it! She's her assistant, I just wanted to thank her, that's all.",
  [(726, "C'est pas ce que tu crois"), (728, "Arrête ! C'est son assistante, je voulais juste la remercier, c'est tout")], ""),
 ("lea", "C'est pour ça que tu m'as mise en garde?",
  "Is that why you warned me?",
  [(736, "C'est pour ça que tu m'as mise en garde")], ""),
 ("catherine", "Mathias... explique-moi.",
  "Mathias... explain this to me.",
  [(737, "Mathias"), (738, "explique-moi")], ""),
 ("mathias", "J'ai quelque chose à te dire.",
  "I have something to tell you.",
  [(739, "J'ai quelque chose à te dire")], ""),
]

OPENER = "Let's walk through the final scene of the episode line by line. Mathias steps into Andréa's office, where Camille is still working."

WALK = [
 (0, None,
  "'Do you have a minute? I forgot something.' Even when they are alone at night, Mathias still addresses Camille with the formal 'vous' out of habit."),
 (1, None,
  "'What, here, in this office?' Camille thinks he is looking for a file or a folder."),
 (2, None,
  "'Your birthday.' Quietly, Mathias admits what he forgot all day."),
 (3, None,
  "'Oh, yes. It's no big deal. And I'm not six years old!' Remember that French expresses age with the verb 'to have': 'I don't have six years'."),
 (4, None,
  "'Anyway, what would make you happy? You must have some idea.' He asks what she would like as a birthday present — and what Camille really wants is simply to spend a little time with her father."),
 (5, None,
  "'When I arrived at the test center, I caught the car door on the examiner's hand.' Mathias opens a bottle of champagne in his office, and for the first time they laugh together like father and daughter as Camille tells the story of her fifth driving test."),
 (6, None,
  "'No!' Mathias bursts out laughing in disbelief."),
 (7, None,
  "'Yes! He had two broken fingers.' Notice the word for 'yes' used to contradict a negative exclamation."),
 (8, None,
  "'I thought I'd see you at the opera. I left messages.' Suddenly the office door opens: Catherine and Hippolyte are standing there in their evening clothes, stunned to find Mathias and Camille laughing over champagne in the dark office."),
 (9, None,
  "'It was on silent mode. Do you want a glass? We brought out the champagne.' Mathias scrambles to act casual, pointing to his phone."),
 (10, None,
  "'Camille helped me a lot on a delicate matter this week. And we're celebrating that.' He tries to explain the champagne as a purely professional thank-you for the online petition."),
 (11, None,
  "'Isn't Camille Andréa's assistant?' Catherine has noticed Mathias's strange behavior all week, and this midnight champagne party makes her deeply suspicious."),
 (12, None,
  "'She can still help the others.' The two-word phrase in the middle means 'even so' or 'still'."),
 (13, None,
  "'It's not what you think. Stop it! She's her assistant, I just wanted to thank her, that's all.' Out in the hallway, Hippolyte grabs his father by the collar, convinced that Mathias warned him away from Camille because Mathias is having an affair with her himself!"),
 (14, None,
  "'Is that why you warned me?' Hearing them shout, Camille steps into the hallway and realizes that Mathias told Hippolyte to stay away from her."),
 (15, None,
  "'Mathias... explain this to me.' Catherine sees all three of them together and knows that Mathias is hiding a huge secret."),
 (16, None,
  "'I have something to tell you.' Cornered at last by his wife, his son, and his secret daughter, Mathias has nowhere left to hide."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = ("Mathias's secret is finally out in the open, setting up an explosive season finale. "
         "That concludes Episode 5 of Dix pour cent — see you in Episode 6, where François Berléand takes the stage.")
CLOSING = ("mathias", "J'ai quelque chose à te dire.")
