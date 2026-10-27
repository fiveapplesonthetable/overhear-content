# Authoring module for dix-pour-cent s03e06 scene 12 (cues 585-620).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s03e06/scene-12.json

ID = "dix-pour-cent-s03e06-scene-12"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 12
TITLE = "Le silence du fantôme  (The Ghost's Silence)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "isabelle": "emilie", "director": "theo"}
LABELS = {"lea": "Camille", "isabelle": "Isabelle", "director": "Le réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 585-620. Freezing during an outdoor shoot, lookalike nurse Isabelle threatens to quit, "
               "leading Camille to negotiate removing spoken lines so the ghost acts purely through silent presence.")

INTRO = ("Shivering in the cold during their outdoor take, lookalike nurse Isabelle struggles to articulate her lines. "
         "Exasperated by the director's complaints, she threatens to walk away back to her hospital job until Camille "
         "finds an artistic compromise that saves the shoot. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("director", "Cette pâleur spectrale est vraiment magnifique.",
  "This spectral pallor is really magnificent.",
  [(585, "Cette pâleur spectrale")], "Admiring haunting look"),
 ("isabelle", "J'ai trop froid, mes lèvres se bloquent.",
  "I am too cold, my lips are locking up.",
  [(590, "Oh, non, j'ai froid."), (594, "J'ai les lèvres qui se bloquent.")], "Complaining about shivering cold"),
 ("director", "Isabelle, dites votre texte maintenant, s'il vous plaît!",
  "Isabelle, say your line now, please!",
  [(593, "Et ça tourne, là !"), (596, "Non, écoutez, Isabelle, c'est pas possible.")], "Demanding dialogue delivery"),
 ("isabelle", "Je ne peux plus parler du tout.",
  "I cannot speak at all anymore.",
  [(595, "J'arrive même plus à dire mon texte.")], "Unable to speak in freezing air"),
 ("director", "Vous sauvez des gens et vous bloquez?",
  "You save people and you freeze up?",
  [(598, "Vous arrivez à recoudre des gens, et puis vous pouvez pas parler en marchant ?")], "Mocking nurse hesitation"),
 ("isabelle", "Chacun son métier, je retourne à l'hôpital.",
  "To each their own trade, I am going back to the hospital.",
  [(599, "Ben non, chacun son métier, voilà."), (601, "Je vais retourner à l'hôpital.")], "Threatening to quit"),
 ("lea", "Attendez Isabelle, ne partez pas comme ça!",
  "Wait Isabelle, do not leave like that!",
  [(603, "Non, mais attends.")], "Pleading to prevent departure"),
 ("lea", "En réalité, ce texte est trop compliqué.",
  "In reality, this text is too complicated.",
  [(604, "En même temps, il est nul, ce texte, aussi.")], "Questioning script dialogue"),
 ("director", "Ce texte est parfait, je l'ai écrit!",
  "This text is perfect, I wrote it!",
  [(607, "Il est très bien, ce texte."), (608, "C'est moi qui l'ai écrit.")], "Defending auteur pride"),
 ("isabelle", "Elle a raison, les mots ne coulent pas.",
  "She is right, the words do not flow.",
  [(609, "Non, mais elle a raison."), (610, "Ça coule pas.")], "Agreeing with critique"),
 ("lea", "Un fantôme ne parle jamais dans l'histoire.",
  "A ghost never speaks in the story.",
  [(611, "Oui, un fantôme, ça dit rien, normalement.")], "Proposing silent concept"),
 ("director", "Vous voulez supprimer toutes les répliques?",
  "You want to delete all the lines?",
  [(617, "Ah non, non, mais moi, je change pas le texte.")], "Balking at removing words"),
 ("lea", "Oui, un regard silencieux sera beaucoup plus fort.",
  "Yes, a silent gaze will be much stronger.",
  [(613, "Un fantôme, ça apparaît, c'est tout.")], "Arguing artistic impact"),
 ("isabelle", "Parfait, je peux enfin jouer ce rôle.",
  "Perfect, I can finally play this role.",
  [(615, "Et peut-être que comme ça, Isabelle, elle pourra un petit peu s'épanouir")], "Embracing silent acting"),
]

WALK = [
 (0, None,
  "'This spectral pallor is really magnificent.' The director praises the ghost aesthetic. "
  "The feminine adjective 'spectrale' evokes ghostly apparitions."),
 (1, None,
  "'I am too cold, my lips are locking up.' Isabelle shivers under the cold wind. "
  "The reflexive verb 'se bloquer' means to lock up or freeze."),
 (2, None,
  "'Isabelle, say your line now, please!' The director demands her cue while rolling. "
  "The imperative 'dites' instructs the speaker directly."),
 (3, None,
  "'I cannot speak at all anymore.' Isabelle feels paralyzed by the low temperature. "
  "The negative phrase 'ne plus... du tout' indicates complete inability."),
 (4, None,
  "'You save people and you freeze up?' The director contrasts her surgery skills with acting. "
  "The verb 'bloquer' here means to freeze emotionally or mentally."),
 (5, None,
  "'To each their own trade, I am going back to the hospital.' Isabelle asserts her real calling. "
  "The proverb 'chacun son metier' means to each their own trade."),
 (6, None,
  "'Wait Isabelle, do not leave like that!' Camille intervenes to salvage the video. "
  "The negative imperative 'ne partez pas' urges her not to walk away."),
 (7, None,
  "'In reality, this text is too complicated.' Camille honestly analyzes the dialogue flaw. "
  "The locution 'en realite' means in fact or in reality."),
 (8, None,
  "'This text is perfect, I wrote it!' The director indignantly defends his authorship. "
  "The passe compose 'ai ecrit' marks his personal creation."),
 (9, None,
  "'She is right, the words do not flow.' Isabelle agrees that the phrasing feels awkward. "
  "The verb 'couler' figuratively describes natural dialogue flow."),
 (10, None,
  "'A ghost never speaks in the story.' Camille suggests an elegant atmospheric solution. "
  "The noun 'fantome' designates a phantom or ghost."),
 (11, None,
  "'You want to delete all the lines?' The director is taken aback by cutting dialogue. "
  "The verb 'supprimer' means to delete or remove."),
 (12, None,
  "'Yes, a silent gaze will be much stronger.' Camille makes a persuasive artistic case. "
  "The comparative structure 'beaucoup plus fort' argues for greater intensity."),
 (13, None,
  "'Perfect, I can finally play this role.' Isabelle gladly welcomes a silent performance. "
  "The adverb 'enfin' expresses relief at reaching a workable solution."),
]

OUTRO = ("Camille's quick artistic instincts resolve an impasse between director and actress. "
         "By turning Isabelle into a silent phantom, the shoot is saved without another freezing line. "
         "Now, let's review the scene one last time.")

CLOSING = ("isabelle", "Parfait, je peux enfin jouer ce rôle.")
