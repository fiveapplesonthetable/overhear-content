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
  "Handing over the costume shirt, the dresser reassures Didier: that will suit you very well. Here the future tense of "
  "the verb to go with an indirect object pronoun means to fit or suit someone."),
 (1, None,
  "Looking in the mirror, Didier sighs: I have put on weight. French uses the verb to take with a partitive article for "
  "gaining weight."),
 (2, None,
  "Gabriel immediately flatters his client: not at all, you are a handsome guy, baby!"),
 (3, None,
  "Didier admits how nervous he feels about tomorrow's shoot: it is going to be embarrassing, or awkward."),
 (4, None,
  "Gabriel tries to pump him up like a boxing coach: you are capable of doing this scene, champ!"),
 (5, None,
  "He adds dramatically: all the power of a lion!"),
 (6, None,
  "Didier deflates the pep talk with a quiet confession: I feel more like a shy little cat. Notice the reflexive verb "
  "to feel followed by the adverb for rather or more like."),
 (7, None,
  "Gabriel tells him to stop and reminds him: you have done lots of scenes like that."),
 (8, None,
  "Then Didier reveals his real worry: listen, I do not even know how aristocrats and servants did things back then."),
 (9, None,
  "Holding up a serious history book, he adds: I did some research, I did not find anything."),
 (10, None,
  "Gabriel waves the book away: forget all that, just do what comes naturally."),
 (11, None,
  "Getting carried away with his own speech, Gabriel leans in and declares: you are an animal, Didier."),
 (12, None,
  "Staring deeply into Didier's eyes, Gabriel adds: it is attractive, even to me."),
 (13, None,
  "Creeped out by his agent's intense stare, Didier snaps: hey, stop looking at me like that!"),
]

TRANSITION = "Let's listen to the whole conversation in Didier's room one more time."

OUTRO = ("Even tough-talking JoeyStarr gets stage fright before a period romance scene, especially when he overthinks "
         "eighteenth-century history. Keep the expression for gaining weight in mind: to take some weight.")

CLOSING = ("joey", "Hé, arrête de me regarder comme ça!")
