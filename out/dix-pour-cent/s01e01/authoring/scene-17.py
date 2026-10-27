ID = "dix-pour-cent-s01e01-scene-17"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 17
TITLE = "Je change d'agent  (I'm Changing Agents)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Cécile", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Same restaurant, a few seconds later. Gabriel was having lunch with Sofia, who was pitching her play, "
         "when Cécile de France appeared at his table. All day he has been dodging her, because Tarantino turned her down "
         "for being too old and he hasn't found the courage to tell her. "
         "But Cécile already knows: Camille, the new assistant, let it slip in the washroom earlier. "
         "Now she wants to see if her agent will tell her the truth. "
         "Listen to the French first, and don't worry if some of it goes by too fast.")

STORY = [
 ("gabriel", "Cécile, super! Ça va?", "Cécile, great! How are you?",
  [(486, "Cécile, super !"), (487, "Ça va ?")], ""),
 ("lea", "Oui, et toi?", "Fine, and you?",
  [(487, "Oui, et toi ?")], ""),
 ("gabriel", "J'ai essayé de t'appeler. C'est non-stop au boulot aujourd'hui.",
  "I tried to call you. It's non-stop at work today.",
  [(488, "J'ai essayé de t'appeler"), (489, "C'est non-stop au boulot aujourd'hui")], ""),
 ("lea", "Toujours aucune nouvelle?", "Still no news?",
  [(490, "Toujours aucune nouvelle ?")], ""),
 ("gabriel", "Ah, si! J'ai eu Miranda Jones au téléphone.", "Oh, yes! I had Miranda Jones on the phone.",
  [(491, "Ah, si !"), (492, "Miranda Jones au téléphone")], "'Je venais d'avoir' -> 'J'ai eu'"),
 ("lea", "Dis-moi tout.", "Tell me everything.",
  [(493, "Dis-moi tout")], ""),
 ("gabriel", "Je ne te mens jamais, Cécile.", "I never lie to you, Cécile.",
  [(494, "Je ne te mens jamais, Cécile")], ""),
 ("gabriel", "Ils ont pensé que ce serait mieux avec un homme.", "They thought it would be better with a man.",
  [(507, "ils ont pensé que ce serait mieux"), (507, "un homme")], "'de... d'en faire un homme' -> 'avec un homme'"),
 ("lea", "Un homme?", "A man?",
  [(508, "Un homme ?")], ""),
 ("gabriel", "Je sais, c'est fou!", "I know, it's crazy!",
  [(509, "Je sais, c'est fou !")], ""),
 ("lea", "Ça n'a rien à voir avec moi?", "It has nothing to do with me?",
  [(510, "Ça n'a rien à voir avec moi ?")], ""),
 ("gabriel", "Pas du tout! Elle a dit que tu étais fantastique.", "Not at all! She said you were fantastic.",
  [(511, "Pas du tout !"), (512, "Elle a dit que tu étais fantastique")], ""),
 ("gabriel", "Je sais que tu es déçue, mais on va rebondir.", "I know you're disappointed, but we'll bounce back.",
  [(515, "je sais que tu es"), (515, "déçue"), (516, "mais on va rebondir")], "'vraiment' dropped"),
 ("lea", "Tu sais combien je voulais ce rôle?", "Do you know how much I wanted this part?",
  [(517, "Tu sais combien je voulais ce rôle ?")], ""),
 ("gabriel", "Qu'est-ce que tu fais?", "What are you doing?",
  [(521, "Qu'est-ce que tu fais ?")], "Cécile stands up"),
 ("lea", "Je change d'agent.", "I'm changing agents.",
  [(521, "Je change d'agent")], ""),
 ("lea", "Tu es un menteur et un lâche. Je sais que c'est à cause de mon âge.",
  "You're a liar and a coward. I know it's because of my age.",
  [(523, "Tu es un menteur et un lâche"), (523, "Je sais que c'est à cause de mon âge")], ""),
 ("lea", "Pourquoi te donner dix pour cent si tu ne me défends pas?",
  "Why give you ten percent if you don't stand up for me?",
  [(524, "Pourquoi te donner dix pour cent si tu ne me défends pas ?")], "the show's title"),
]

OPENER = ("Let's go back over it. Gabriel jumps up, all smiles, as if he were delighted to see her.")

WALK = [
 (0, None,
  "'Cécile, great! How are you?' Those two little words at the end are the everyday way to ask how someone is. "
  "Cécile plays along."),
 (1, None,
  "'Fine, and you?' She uses the casual 'you' with Gabriel; they've worked together for years."),
 (2, "J'ai essayé de t'appeler.",
  "'I tried to call you.' The everyday past tense again: the verb 'have', then the action. It's a fib: this morning he "
  "rejected her call."),
 (2, "C'est non-stop au boulot aujourd'hui.",
  "'It's non-stop at work today.' The French borrow the English 'non-stop', and use their casual word for 'work'."),
 (3, None,
  "'Still no news?' The middle word means 'no' or 'not a single', before a noun."),
 (4, None,
  "'Oh, yes! I had Miranda Jones on the phone.' That first little word is a special 'yes', used to contradict a negative "
  "question. Miranda Jones is the American producer."),
 (5, None,
  "'Tell me everything.' A casual command, with the word for 'me' stuck on after a hyphen."),
 (6, None,
  "'I never lie to you, Cécile.' The negative wraps around the verb again, but this time the second word means 'never'. "
  "The audience knows it's a lie. Then he invents a long story about the Wild West, where women died young."),
 (7, None,
  "'They thought it would be better with a man.' His tale is that the film people now want a man for the part. "
  "The words for 'it would be' are a polite, hypothetical form."),
 (8, None,
  "'A man?' She repeats it, staring at him."),
 (9, None,
  "'I know, it's crazy!' He pretends to be as shocked as she is."),
 (10, None,
  "'It has nothing to do with me?' Literally 'that has nothing to see with me'. She's giving him one last chance."),
 (11, "Pas du tout!",
  "'Not at all!' A strong, useful way to say no."),
 (11, "Elle a dit que tu étais fantastique.",
  "'She said you were fantastic.' The second verb is in the past form French uses for descriptions, 'you were'."),
 (12, None,
  "'I know you're disappointed, but we'll bounce back.' The word for 'disappointed' ends with an extra letter because "
  "Cécile is a woman. And 'we're going to', plus a verb, is the easy way to talk about the future."),
 (13, None,
  "'Do you know how much I wanted this part?' Another descriptive past form, for a wish that lasted a long time. "
  "Then she gets up."),
 (14, None,
  "'What are you doing?' Almost the same question Mathias asked Camille earlier, in a very different mood."),
 (15, None,
  "'I'm changing agents.' Short and final."),
 (16, "Tu es un menteur et un lâche.",
  "'You're a liar and a coward.' Two hard words, but no swearing: Cécile doesn't need it."),
 (16, "Je sais que c'est à cause de mon âge.",
  "'I know it's because of my age.' So she knew all along."),
 (17, None,
  "'Why give you ten percent if you don't stand up for me?' Ten percent is what an agent earns, and it's the name of "
  "the show. And with that, Cécile walks out of the restaurant."),
]

TRANSITION = "Now the whole scene once more, straight through."

OUTRO = ("That was a hard scene for Gabriel, but a good one for your French. "
         "When you watch, wait for the line about ten percent: you'll recognise it. Take care, and see you soon.")
CLOSING = ("lea", "Salut!")
