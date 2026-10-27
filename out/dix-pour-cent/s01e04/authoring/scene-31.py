# Authoring module for dix-pour-cent s01e04 scene 31 (cues 804-837).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-31.py --out out/dix-pour-cent/s01e04/scene-31.json

ID = "dix-pour-cent-s01e04-scene-31"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 31
TITLE = "L'Allemand se retire  (The German Pulls Out)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "arlette": "Arlette", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 804-837. Swearing in cue 806 ('Le salaud !') is omitted. Gabriel's lines in the three-way partner "
               "conversation are given to Andréa/Arlette to stay within three voices, and Hélène's angry shout on the "
               "phone (824) is narrated. Feminine 'sûre' is used in cue 812 when addressing Arlette, and 'M.' in "
               "cue 827 is written out as 'monsieur'.")

INTRO = ("After Audrey Fleurot's triumph at the UNICEF gala, the next morning back at ASK begins in panic. "
         "Andréa and Gabriel are scrambling to keep Mathias's famous clients from following him to the rival agency "
         "StarMédia. Then Arlette walks in with news about Jonas Hirsch, the German businessman who wanted to buy "
         "the agency from Samuel's widow Hélène. Listen to the French first; don't worry about catching every word.")

STORY = [
 ("lea", "Fais une liste des acteurs de Mathias. Il faut faire vite.",
  "Make a list of Mathias's actors. We have to be quick.",
  [(804, "Fais une liste des acteurs de Mathias"), (805, "mais il faut faire vite")], "swearing in 806 omitted"),
 ("arlette", "L'Allemand se retire.", "The German is pulling out.",
  [(808, "L'Allemand se retire")], ""),
 ("lea", "Quoi?", "What?",
  [(809, "Quoi")], ""),
 ("arlette", "Il a appris que Mathias rejoint StarMédia.",
  "He heard that Mathias is joining StarMédia.",
  [(810, "Il a appris que Mathias rejoint StarMédia")], ""),
 ("arlette", "Il dit que sans lui, l'agence va perdre trop de valeur.",
  "He says that without him, the agency is going to lose too much value.",
  [(811, "Il dit que sans lui, l'agence va perdre trop de valeur")], ""),
 ("lea", "Tu en es sûre? Qu'est-ce qu'Hélène dit?",
  "Are you sure about it? What does Hélène say?",
  [(812, "Tu en es"), (814, "Qu'est-ce qu'Hélène dit")], "feminine 'sûre' addressing Arlette"),
 ("arlette", "Elle est furieuse contre Mathias.",
  "She's furious with Mathias.",
  [(815, "Elle est furieuse contre Mathias")], ""),
 ("lea", "Et s'il l'avait fait exprès? Pour sauver l'agence!",
  "And what if he did it on purpose? To save the agency!",
  [(819, "Et s'il l'avait fait exprès"), (816, "Il l'a fait exprès")],
  "'Pour qu'on ne soit pas rachetés' simplified to 'Pour sauver l'agence!'"),
 ("lea", "Un acte généreux de Mathias? Quelle blague!",
  "A generous act from Mathias? What a joke!",
  [(821, "Un acte généreux de Mathias ? Quelle blague")], ""),
 ("arlette", "Peut-être pas généreux, mais c'est un stratège.",
  "Maybe not generous, but he's a strategist.",
  [(822, "Peut-être pas généreux, mais c'est un stratège")], ""),
 ("mathias", "Il se retire?", "He's pulling out?",
  [(826, "Il se retire")], "Mathias on the phone with Hélène"),
 ("mathias", "Non, je n'ai pas dit à monsieur Hirsch que je rejoignais StarMédia.",
  "No, I didn't tell Mr Hirsch that I was joining StarMédia.",
  [(827, "Non, je n'ai pas dit à"), (827, "Hirsch que je rejoignais StarMédia")], "'M.' written out as 'monsieur'"),
 ("mathias", "Je ne sais pas comment il l'a appris. Hélène, calme-toi.",
  "I don't know how he found out. Hélène, calm down.",
  [(828, "Je ne sais pas comment il l'a appris"), (829, "Hélène, calme-toi")], ""),
 ("arlette", "Bravo, Mathias! Laisse-moi t'embrasser.",
  "Well done, Mathias! Let me kiss you.",
  [(831, "Bravo, Mathias"), (834, "Laisse-moi t'embrasser")], ""),
 ("mathias", "Merci, Hélène. Je te rappelle.",
  "Thank you, Hélène. I'll call you back.",
  [(833, "Merci"), (833, "Je te rappelle")], "cue 833 says 'Merci, Mathias' by slip; Mathias is ending call with Hélène"),
 ("lea", "Super, Mathias! Tu as fait quelque chose de formidable. Bravo!",
  "Great, Mathias! You did something wonderful. Well done!",
  [(835, "Super, Mathias"), (836, "Tu as fait quelque chose de formidable"), (837, "Bravo")], ""),
]

OPENER = ("Let's walk through it together. Andréa is still preparing for war with Mathias when Arlette walks in.")

WALK = [
 (0, None,
  "'Make a list of Mathias's actors. We have to be quick.' A casual command at the start, and at the end the "
  "impersonal phrase for 'it is necessary to act fast'."),
 (1, None,
  "'The German is pulling out.' A reflexive verb that literally means 'withdraws himself'."),
 (2, None,
  "'What?' Andréa can hardly believe her ears."),
 (3, None,
  "'He heard that Mathias is joining StarMédia.' Literally 'he learned that Mathias joins StarMédia'."),
 (4, None,
  "'He says that without him, the agency is going to lose too much value.' Because Mathias represents the biggest "
  "stars at ASK, the German buyer no longer wants the company without him."),
 (5, None,
  "'Are you sure about it? What does Hélène say?' The little word before 'are' means 'of it'."),
 (6, None,
  "'She's furious with Mathias.' Hélène was hoping to sell the agency for millions, and now the deal is dead."),
 (7, None,
  "'And what if he did it on purpose? To save the agency!' The phrase at the end of the question means 'on purpose'. "
  "Suddenly the agents imagine that Mathias only pretended to leave in order to scare off the German buyer."),
 (8, None,
  "'A generous act from Mathias? What a joke!' Andréa isn't convinced so easily."),
 (9, None,
  "'Maybe not generous, but he's a strategist.' Arlette thinks Mathias planned the whole thing like a chess game."),
 (10, None,
  "'He's pulling out?' At that very moment, the lift doors open and Mathias steps out on the phone with Hélène, "
  "who is shouting at him."),
 (11, None,
  "'No, I didn't tell Mr Hirsch that I was joining StarMédia.' Poor Mathias is telling the complete truth: he really "
  "was planning to leave, and never meant for the German buyer to find out!"),
 (12, None,
  "'I don't know how he found out. Hélène, calm down.' A reflexive command at the end: 'calm yourself'."),
 (13, None,
  "'Bravo, Mathias! Let me kiss you.' Before Mathias can even understand what is happening, Arlette throws her arms "
  "around his neck."),
 (14, None,
  "'Thank you, Hélène. I'll call you back.' Baffled, Mathias hangs up the phone."),
 (15, None,
  "'Great, Mathias! You did something wonderful. Bravo!' Notice how 'something' is linked to the adjective 'wonderful' "
  "with the little word for 'of'. Without meaning to, Mathias has become the saviour of the agency."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = ("Mathias wanted to leave ASK in secret, and instead his leak scared away the German buyer and made him "
         "look like a hero. In the final scene of the episode, the whole agency gathers with champagne to toast him.")
CLOSING = ("arlette", "Bravo, Mathias!")
