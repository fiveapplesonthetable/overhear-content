# Authoring module for dix-pour-cent s01e05 scene 09 (cues 158-176).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-09.py --out out/dix-pour-cent/s01e05/scene-09.json

ID = "dix-pour-cent-s01e05-scene-09"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 9
TITLE = "La mort de Jonathan  (The Death of Jonathan)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "mathias": "marcel"}
LABELS = {"lea": "Marie-Sophie", "arlette": "Arlette", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 158-176. In Mathias's office at ASK, Arlette and head writer Marie-Sophie Garnier announce "
               "that they are killing off Jonathan Joubert's soap-opera character Ryan. Vulgarities and idioms in "
               "cues 161, 165, 167, 172, and 175-176 are softened to clean A1 French.")

INTRO = ("Back in Paris at the ASK agency, Mathias is working in his office when Arlette walks in with one of her "
         "oldest clients: Marie-Sophie Garnier, the head screenwriter of the hit daytime soap opera Happy Ever After. "
         "Mathias represents the show's arrogant leading man, Jonathan Joubert, who plays Doctor Ryan. "
         "Listen to the French first, without worrying about catching every word.")

STORY = [
 ("mathias", "Bonjour. Ah, vous voilà.",
  "Hello. Ah, there you are.",
  [(158, "Bonjour"), (158, "Ah, vous voilà")], ""),
 ("arlette", "Voici Marie-Sophie Garnier, chef scénariste sur Heureux pour toujours.",
  "This is Marie-Sophie Garnier, head screenwriter on Happy Ever After.",
  [(159, "Voici Marie-Sophie Garnier"), (160, "chef scénariste sur Heureux pour toujours")],
  "'le feuilleton' omitted for A1"),
 ("mathias", "Je sais. Qu'est-ce qui se passe? Jonathan Joubert pose encore un problème?",
  "I know. What's going on? Is Jonathan Joubert causing a problem again?",
  [(161, "Je sais. Qu'est-ce qui se passe ? Jonathan Joubert"), (161, "encore")],
  "idiom 'fait encore des siennes' simplified to 'pose encore un problème' for A1"),
 ("arlette", "Nous sommes là pour annoncer la mort de Jonathan.",
  "We're here to announce Jonathan's death.",
  [(162, "Nous sommes là pour annoncer la mort de Jonathan")], ""),
 ("arlette", "Dans la série, j'entends.",
  "In the series, I mean.",
  [(163, "Dans la série, j'entends")], ""),
 ("mathias", "Ryan est un chouchou du public. Vous ne pouvez pas le tuer!",
  "Ryan is a darling of the public. You can't kill him!",
  [(164, "Ryan est un chouchou du public. Vous ne pouvez pas le tuer")], ""),
 ("lea", "C'est un plus grand égoïste que mon premier mari!",
  "He's a bigger egoist than my first husband!",
  [(165, "C'est un plus grand"), (165, "que mon premier mari")],
  "'connard' softened to 'égoïste' for A1"),
 ("lea", "Je suis dans la série depuis huit ans.",
  "I've been on the series for eight years.",
  [(166, "Je suis dans la série depuis huit ans")], ""),
 ("lea", "On travaille ces scripts pendant des heures, et lui change toutes les répliques.",
  "We work on these scripts for hours, and he changes all the lines.",
  [(167, "ces scripts pendant des heures, et lui"), (168, "change toutes les répliques")],
  "slang 'bosse' adapted to 'travaille' for A1"),
 ("lea", "Il veut écrire, diriger, choisir ses partenaires. C'est l'enfer!",
  "He wants to write, direct, choose his partners. It's hell!",
  [(169, "Il veut écrire, diriger"), (170, "choisir ses partenaires"), (170, "C'est l'enfer")], ""),
 ("mathias", "Je vais l'appeler et arranger ça.",
  "I'm going to call him and fix that.",
  [(171, "Je vais l'appeler et arranger ça")], ""),
 ("arlette", "Non, on lui a déjà parlé. Il n'écoute pas du tout!",
  "No, we've already spoken to him. He doesn't listen at all!",
  [(172, "Non, on lui a déjà")],
  "'passé un savon. Il s'en fout complètement' softened to 'parlé. Il n'écoute pas du tout' for A1"),
 ("mathias", "Laissez-moi lui parler.",
  "Let me talk to him.",
  [(173, "Laissez-moi lui parler")], ""),
 ("lea", "Jonathan va mourir! Ryan, d'un cancer terrible.",
  "Jonathan is going to die! Ryan, of a terrible cancer.",
  [(173, "Jonathan va mourir"), (174, "Ryan"), (175, "D'un cancer")],
  "'des testicules' softened to 'terrible' for A1"),
 ("lea", "Il le mérite après huit ans à me fatiguer!",
  "He deserves it after eight years of tiring me out!",
  [(176, "Il le mérite après huit ans à me")],
  "'casser les couilles' softened to 'fatiguer' for A1"),
]

OPENER = "Let's walk through the scene line by line. Mathias greets Arlette and her client in his office."

WALK = [
 (0, None,
  "'Hello. Ah, there you are.' Literally 'you there-is' — French uses this pointer word with an object pronoun before it to say 'there you are'."),
 (1, None,
  "'This is Marie-Sophie Garnier, head screenwriter on Happy Ever After.' The related pointer word introduces someone who is standing right beside you."),
 (2, None,
  "'I know. What's going on? Is Jonathan Joubert causing a problem again?' Mathias already knows that his soap-opera star is difficult on set."),
 (3, None,
  "'We're here to announce Jonathan's death.' Arlette delivers the news with a completely straight face."),
 (4, None,
  "'In the series, I mean.' Literally 'In the series, I hear' — the verb for 'to hear' also means 'to mean' or 'to intend'."),
 (5, None,
  "'Ryan is a darling of the public. You can't kill him!' Mathias panics at the thought of his lucrative client losing his starring role."),
 (6, None,
  "'He's a bigger egoist than my first husband!' To form a comparative, French places 'more' before the adjective and 'than' after it."),
 (7, None,
  "'I've been on the series for eight years.' French uses the present tense with 'since' for a job that started in the past and continues today."),
 (8, None,
  "'We work on these scripts for hours, and he changes all the lines.' The emphatic pronoun 'he' stresses the contrast between the writers' hard work and the actor's arrogance."),
 (9, None,
  "'He wants to write, direct, choose his partners. It's hell!' Three infinitive verbs list everything Jonathan tries to control on the show."),
 (10, None,
  "'I'm going to call him and fix that.' Mathias uses the near future ('I go to call') to promise a quick solution."),
 (11, None,
  "'No, we've already spoken to him. He doesn't listen at all!' The indirect object pronoun 'to him' sits before the helper verb 'has'."),
 (12, None,
  "'Let me talk to him.' Mathias makes one last plea to save his client's job."),
 (13, None,
  "'Jonathan is going to die! Ryan, of a terrible cancer.' In her anger, Marie-Sophie mixes up the actor's real name with his character's name."),
 (14, None,
  "'He deserves it after eight years of tiring me out!' Marie-Sophie storms out of the office, determined to write Ryan's final episode."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = ("Marie-Sophie is determined to kill off Mathias's soap-opera star, and Arlette is backing her screenwriter "
         "all the way. Next, Mathias tries to charm Marie-Sophie with flowers while Camille and Herve react to the news. See you there.")
CLOSING = ("arlette", "Nous sommes là pour annoncer la mort de Jonathan.")
