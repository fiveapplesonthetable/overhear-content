# Authoring module for dix-pour-cent s01e05 scene 15 (cues 265-282).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-15.py --out out/dix-pour-cent/s01e05/scene-15.json

ID = "dix-pour-cent-s01e05-scene-15"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 15
TITLE = "Tu es un animal, Didier  (You're an Animal, Didier)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "joey": "marcel"}
LABELS = {"lea": "Costumière", "gabriel": "Gabriel", "joey": "JoeyStarr"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 265-282. Spoken contractions ('T'es', 'j'ai rien') are restored to standard A1 ('Tu es', "
               "'je n'ai rien'), and crude slang in cues 268-271 is softened for A1 learners.")

INTRO = ("Down the hall in JoeyStarr's hotel room, a costume assistant finishes fitting Didier's eighteenth-century "
         "shirt just as Gabriel breaks the news that the love scene with Julie is happening tomorrow morning. Behind "
         "his tough-guy image, Didier is suddenly shy about his body and his historical research, so Gabriel tries to "
         "boost his confidence — a little too intensely. Let's listen in French first.")

STORY = [
 ("lea", "Ça t'ira très bien.",
  "That will suit you very well.",
  [(265, "Ça t'ira très bien")], ""),
 ("joey", "J'ai pris du poids.",
  "I have put on weight.",
  [(265, "J'ai pris du poids")], ""),
 ("gabriel", "Pas du tout. Tu es un beau gosse, bébé!",
  "Not at all. You are a handsome guy, baby!",
  [(266, "Pas du tout"), (266, "un beau gosse, bébé")], "'T'es' -> 'Tu es'"),
 ("joey", "Ça va être gênant.",
  "It is going to be embarrassing.",
  [(267, "Ça va être gênant")], ""),
 ("gabriel", "Tu es capable de faire cette scène, champion!",
  "You are capable of doing this scene, champ!",
  [(268, "capable de faire cette scène"), (269, "champion")], "Softened slang; 'T'es' -> 'Tu es'"),
 ("gabriel", "Toute la puissance d'un lion!",
  "All the power of a lion!",
  [(270, "Toute la puissance d'un lion")], "Trimmed 'en rut'"),
 ("joey", "Je me sens plutôt comme un petit chat timide.",
  "I feel more like a shy little cat.",
  [(271, "Je me sens plutôt comme")], "Softened idiom for A1"),
 ("gabriel", "Arrête. Tu as fait beaucoup de scènes comme ça.",
  "Stop. You have done lots of scenes like that.",
  [(272, "Arrête"), (272, "des scènes comme ça")], "'T'en as fait des tas' -> 'Tu as fait beaucoup'"),
 ("joey", "Écoute, je ne sais même pas comment les aristocrates et les domestiques faisaient à l'époque.",
  "Listen, I do not even know how aristocrats and servants did things back then.",
  [(273, "Écoute"), (274, "comment les aristocrates et les domestiques"), (274, "faisaient à l'époque")], "Restored 'ne'"),
 ("joey", "J'ai fait des recherches, je n'ai rien trouvé.",
  "I did some research, I did not find anything.",
  [(275, "J'ai fait des recherches"), (275, "rien trouvé")], "Restored 'ne'"),
 ("gabriel", "Oublie tout ça. Fais juste ce qui vient naturellement.",
  "Forget all that. Just do what comes naturally.",
  [(277, "Oublie tout ça. Fais juste ce qui vient naturellement")], ""),
 ("gabriel", "Tu es un animal, Didier.",
  "You are an animal, Didier.",
  [(278, "un animal, Didier")], "'T'es' -> 'Tu es'"),
 ("gabriel", "C'est attirant. Même pour moi.",
  "It is attractive. Even to me.",
  [(280, "C'est attirant"), (281, "Même pour moi")], ""),
 ("joey", "Hé, arrête de me regarder comme ça!",
  "Hey, stop looking at me like that!",
  [(282, "Hé, arrête de me regarder comme ça")], ""),
]

OPENER = "Now let's break down the scene line by line."

WALK = [
 (0, None,
  "'That will suit you very well.' Handing over the period shirt, the costumier uses the future tense of 'to go' for 'to suit'."),
 (1, None,
  "'I have put on weight.' French uses the verb 'to take' with a partitive article for gaining weight."),
 (2, None,
  "'Not at all. You are a handsome guy, baby!' Gabriel immediately flatters his nervous star."),
 (3, None,
  "'It is going to be embarrassing.' Didier admits his anxiety about tomorrow's intimate scene."),
 (4, None,
  "'You are capable of doing this scene, champ!' Gabriel tries to pump him up like a sports coach."),
 (5, None,
  "'All the power of a lion!' He adds dramatic animal imagery to boost his client's confidence."),
 (6, None,
  "'I feel more like a shy little cat.' Didier deflates the speech with an endearing, quiet confession."),
 (7, None,
  "'Stop. You have done lots of scenes like that.' Gabriel reminds him of his long screen experience."),
 (8, None,
  "'Listen, I do not even know how aristocrats and servants did things back then.' Didier reveals his real historical worry."),
 (9, None,
  "'I did some research, I did not find anything.' Holding up a heavy book, he admits his frustration."),
 (10, None,
  "'Forget all that. Just do what comes naturally.' Gabriel urges him to trust his instincts."),
 (11, None,
  "'You are an animal, Didier.' Getting carried away, Gabriel leans in with intense conviction."),
 (12, None,
  "'It is attractive. Even to me.' Staring deeply into Didier's eyes, Gabriel takes the flattery a bit too far."),
 (13, None,
  "'Hey, stop looking at me like that!' Unsettled by his agent's intense gaze, Didier snaps back to reality."),
]

TRANSITION = "Let's listen to the whole conversation in Didier's room one more time."

OUTRO = ("Even tough-talking JoeyStarr gets stage fright before a period romance scene, especially when he overthinks "
         "eighteenth-century history. Keep the expression for gaining weight in mind: to take some weight.")

CLOSING = ("joey", "Hé, arrête de me regarder comme ça!")
