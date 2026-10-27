# Authoring module for dix-pour-cent s01e06 scene 01 (cues 1-28).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-01.py --out out/dix-pour-cent/s01e06/scene-01.json

ID = "dix-pour-cent-s01e06-scene-01"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = "La répétition de François  (François's Rehearsal)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "christophe": "theo", "francois": "marcel"}
LABELS = {"lea": "Andréa", "christophe": "Christophe", "francois": "François"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-28. Andréa introduces the artistic pairing of François Berléand and director Christophe Bel. "
               "François's swearing in cue 26 is cleaned up for an A1 audience.")

INTRO = ("Welcome to the season finale of Call My Agent. At ASK, the agency is in turmoil: Samuel is gone, and the "
         "tax audit is pressing down on everyone. But the show must go on. Andréa has arranged a bold theatrical "
         "collaboration: veteran actor François Berléand is starring in Molière's Dom Juan, directed by the young "
         "and provocative Christophe Bel. The rehearsal takes place around an indoor swimming pool. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Tu sais ce qu'est un agent?",
  "Do you know what an agent is?",
  [(1, "Tu sais ce qu'est un agent ?")], ""),
 ("christophe", "Dix pour cent du cachet d'une star?",
  "Ten percent of a star's pay?",
  [(2, "Dix pour cent du cachet d'une star ?")], ""),
 ("lea", "Ce projet avec François Berléand, c'était mon idée.",
  "This project with François Berléand was my idea.",
  [(8, "C'était mon idée"), (10, "Bel avec Berléand")], "Combined for clarity"),
 ("christophe", "Le jeune metteur en scène avec l'acteur âgé.",
  "The young director with the older actor.",
  [(12, "avec le jeune metteur en scène"), (12, "L'acteur âgé")], ""),
 ("lea", "Une perspective excitante, non?",
  "An exciting prospect, right?",
  [(13, "Une perspective excitante, non ?")], ""),
 ("christophe", "J'adore!",
  "I love it!",
  [(14, "J'adore !")], ""),
 ("francois", "Je suis tout à vous.",
  "I am all yours.",
  [(19, "Je suis tout à vous")], "Rehearsal line from Dom Juan"),
 ("francois", "Mais je ne saute pas sur le canard!",
  "But I'm not jumping on the duck!",
  [(20, "Je ne saute pas sur le canard")], ""),
 ("christophe", "Juste une fois, pour voir!",
  "Just once, to see!",
  [(21, "Juste une fois, pour voir !")], ""),
 ("francois", "Je ne saute pas sur le canard, c'est clair?",
  "I'm not jumping on the duck, is that clear?",
  [(22, "Je ne saute pas sur le canard ! C'est clair ?")], ""),
 ("christophe", "L'eau est délicieuse, tu peux essayer.",
  "The water is lovely, you can try.",
  [(23, "L'eau est délicieuse"), (24, "Tu peux au moins essayer")], ""),
 ("francois", "C'est ridicule, la piscine et le canard!",
  "It's ridiculous, the pool and the duck!",
  [(25, "C'est ridicule ! La piscine, le canard")], ""),
 ("francois", "Ce n'est pas Dom Juan, ça!",
  "That is not Dom Juan!",
  [(25, "C'est pas Dom Juan, ça !")], "Formal negative particle restored"),
 ("francois", "J'en ai marre!",
  "I have had enough!",
  [(27, "J'en ai marre !")], ""),
]

OPENER = "Let's break down the scene line by line to understand how the clash begins."

WALK = [
 (0, None,
  "'Do you know what an agent is?' Andréa begins with a fundamental question about their profession."),
 (1, None,
  "'Ten percent of a star's pay?' Christophe gives the standard cynical formula about agency fees."),
 (2, None,
  "'This project with François Berléand was my idea.' Andréa proudly claims credit for the bold pairing."),
 (3, None,
  "'The young director with the older actor.' Christophe summarizes the artistic contrast between them."),
 (4, None,
  "'An exciting prospect, right?' Andréa asks whether this creative tension makes good theatre."),
 (5, None,
  "'I love it!' Christophe enthusiastically agrees that the dynamic is full of potential."),
 (6, None,
  "'I am all yours.' François delivers his classical stage line from Molière in character."),
 (7, None,
  "'But I'm not jumping on the duck!' Suddenly breaking character, François rejects the absurd prop."),
 (8, None,
  "'Just once, to see!' Christophe pleads from the water for François to try the inflatable duck."),
 (9, None,
  "'I'm not jumping on the duck, is that clear?' François repeats his refusal with absolute finality."),
 (10, None,
  "'The water is lovely, you can try.' Christophe tries to tempt him into the heated swimming pool."),
 (11, None,
  "'It's ridiculous, the pool and the duck!' François insists that the avant-garde staging looks absurd."),
 (12, None,
  "'That is not Dom Juan!' He argues that modern stage gimmicks ruin the spirit of classical drama."),
 (13, None,
  "'I have had enough!' Losing his patience entirely, François storms off the rehearsal set."),
]

TRANSITION = "Now let's hear the whole rehearsal once more from beginning to end."

OUTRO = ("François has made his position clear: he refuses to jump on a plastic duck in a pool. Andréa will have her "
         "hands full trying to keep this production from collapsing. See you in the next scene.")

CLOSING = ("francois", "Je ne saute pas sur le canard!")
