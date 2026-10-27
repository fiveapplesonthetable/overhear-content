ID = "dix-pour-cent-s01e01-scene-14"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = "Je suis bien ici  (I'm Fine Here)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "noemie": "emilie"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Back in the corridors of the agency, a storm is coming. "
         "A moment ago Camille, Andréa's brand-new assistant, chatted with the actress Cécile de France and, by mistake, "
         "told her the bad news nobody had dared to give her: Tarantino finds her too old for the part. "
         "This morning Camille also asked Mathias, the cold, ambitious agent, to help her find work, and he said no. "
         "What nobody here knows is that Mathias is her father. Now he walks down the corridor and finds her, "
         "at work, in his own agency. Later, his assistant Noémie, who has seen them argue, has a word with Camille. "
         "First the whole scene in French; just let it wash over you.")

STORY = [
 ("mathias", "Qu'est-ce que tu fais là?", "What are you doing here?",
  [(443, "Qu'est-ce que tu fais là ?")], ""),
 ("lea", "J'ai trouvé un travail. Super, non?", "I found a job. Great, isn't it?",
  [(443, "J'ai trouvé un travail"), (444, "Super, non ?")], ""),
 ("mathias", "Un travail?", "A job?",
  [(445, "Un travail ?")], ""),
 ("lea", "Je suis la nouvelle assistante d'Andréa Martel.", "I'm Andréa Martel's new assistant.",
  [(446, "Je suis la nouvelle assistante d'Andréa Martel")], ""),
 ("mathias", "Écoute, j'ai mal réagi ce matin.", "Listen, I reacted badly this morning.",
  [(449, "Écoute, j'ai"), (450, "J'ai mal réagi ce matin")], ""),
 ("mathias", "Je ne m'attendais pas à te voir.", "I wasn't expecting to see you.",
  [(450, "je ne m'attendais pas à te voir")], ""),
 ("mathias", "Si tu veux, je peux t'aider à trouver un poste dans le cinéma.",
  "If you want, I can help you find a job in film.",
  [(451, "si tu veux"), (452, "trouver un poste dans le cinéma")], "'je peux t'aider' replaces 'que je t'aide'"),
 ("lea", "C'est gentil, mais je suis bien ici.", "That's kind, but I'm fine here.",
  [(453, "C'est gentil, mais je suis bien ici")], ""),
 ("mathias", "Non, Camille! Ce n'est pas possible.", "No, Camille! It's not possible.",
  [(454, "Camille"), (455, "pas possible")], "swear word dropped; 'Non' added; full negation 'ce n'est'"),
 ("lea", "Pourquoi?", "Why?",
  [(455, "Pourquoi ?")], ""),
 ("mathias", "Parce que tu ne peux pas. C'est ma vie!", "Because you can't. It's my life!",
  [(456, "Parce que tu ne peux pas"), (456, "c'est ma vie")], ""),
 ("lea", "Tu ne me donnes rien.", "You give me nothing.",
  [(457, "Tu ne me donnes rien")], ""),
 ("lea", "Alors je me débrouille seule, comme toujours!", "So I'll manage on my own, as always!",
  [(457, "alors je me débrouille seule, comme toujours")], ""),
 ("noemie", "Bonjour. En fait, vous et lui...", "Hello. Actually, you and him...",
  [(458, "Bonjour"), (459, "En fait, vous"), (460, "vous et lui")], "cues 458-460 joined"),
 ("noemie", "Mathias, vous savez, est marié.", "Mathias, you know, is married.",
  [(461, "Mathias, vous savez"), (462, "est marié")], ""),
 ("noemie", "Il est très, très marié.", "He's very, very married.",
  [(463, "Il est très, très marié")], ""),
]

OPENER = ("Let's take it slowly. Mathias stops dead when he sees Camille in the corridor, "
          "and his first words are not exactly a warm hello.")

WALK = [
 (0, None,
  "'What are you doing here?' He uses the casual 'you', the one for family and friends, so we already sense these two "
  "know each other well. Camille answers brightly."),
 (1, "J'ai trouvé un travail.",
  "'I found a job.' This is the past tense French uses most in conversation: a helper verb, 'have', plus the action. "
  "Literally 'I have found a job'."),
 (1, "Super, non?",
  "'Great, isn't it?' Adding the little word for 'no' with a question mark at the end is an easy way to ask for agreement. "
  "Mathias can only repeat her words."),
 (3, None,
  "'I'm Andréa Martel's new assistant.' The word for 'new' takes its feminine form, because Camille is a woman. "
  "And to say whose assistant she is, French puts the owner last, after a small linking word."),
 (4, None,
  "'Listen, I reacted badly this morning.' He starts with a casual command, 'listen', to calm things down. "
  "It's almost an apology."),
 (5, None,
  "'I wasn't expecting to see you.' Notice how the negative wraps around the verb: one small word before it, "
  "and the word for 'not' after it. Then he makes an offer."),
 (6, None,
  "'If you want, I can help you find a job in film.' He means anywhere else, a nice long way from his agency. "
  "Camille is polite, but she doesn't move an inch."),
 (7, None,
  "'That's kind, but I'm fine here.' Literally 'I am well here'. This is the line that makes Mathias lose his temper. "
  "In the show he swears; here we keep it clean."),
 (8, None,
  "'No, Camille! It's not possible.' Here is that negative wrap again, around the verb 'is'. In fast speech the French "
  "often drop the first little word, and you'll hear exactly that in the episode."),
 (9, None,
  "'Why?' One short word, and Camille stands her ground."),
 (10, "Parce que tu ne peux pas.",
  "'Because you can't.' The verb here means 'to be able to', and it often stands alone like this."),
 (10, "C'est ma vie!",
  "'It's my life!' His job, his agency, his secret: he wants her out of all of it."),
 (11, None,
  "'You give me nothing.' Another negative wrap, this time with a different second word, the one that means 'nothing'. "
  "Camille fires back."),
 (12, None,
  "'So I'll manage on my own, as always!' That verb in the middle is a very French one: to get by, to sort yourself out. "
  "The word for 'alone' is feminine here, because she is talking about herself. Then Mathias walks off."),
 (13, None,
  "'Hello. Actually, you and him...' Noémie, Mathias's assistant, has heard everything, and she has completely "
  "misunderstood. She uses the polite 'you' with the newcomer."),
 (14, None,
  "'Mathias, you know, is married.' She thinks Camille is a girlfriend, not a daughter."),
 (15, None,
  "'He's very, very married.' Saying a word twice is a fun way to make it stronger, and Camille can't tell her the truth."),
]

TRANSITION = "Now let's hear the whole scene again, all in French."

OUTRO = ("That's it for this scene, and you followed a real family row in French. "
         "When you watch it, listen for 'I'm fine here', and for Noémie's very married Mathias. See you next time.")
CLOSING = ("lea", "À bientôt!")
