ID = "dix-pour-cent-s01e01-scene-21"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 21
TITLE = "Laisse-lui un peu d'espace  (Give Her Some Space)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 604-617. Merged scene 22 (cues 618-628, Gabriel and Hervé in a bar) is retold in the bridge of "
               "scene 23 and hinted at in the outro here. Cue 605 'Pas du tout' is left out: what it answers isn't "
               "subtitled.")

INTRO = ("While Mathias was having tea with Miranda Jones, who told him firmly that Cécile, at forty-one, is too old "
         "for Tarantino, Gabriel was back at the agency, lost. Cécile has walked out on him, and he goes to the one "
         "colleague who never runs out of ideas: Andréa. Today we hear things from her side. As usual, the French "
         "comes first, and it's fine to understand only part of it.")

STORY = [
 ("gabriel", "Andréa, je ne sais pas quoi faire.", "Andréa, I don't know what to do.",
  [(604, "Je ne sais pas quoi faire")], "'Andréa' added"),
 ("gabriel", "Cécile est partie. Elle veut changer d'agent.", "Cécile has left. She wants to change agents.", [],
  "new; recaps scene 17 (cue 521 'Je change d'agent')"),
 ("gabriel", "Tu ne peux pas lui parler?", "Can't you talk to her?", [(606, "Tu ne peux pas lui parler")], ""),
 ("lea", "Moi? Qu'est-ce que je peux lui dire?", "Me? What can I say to her?",
  [(607, "Moi ?")], "'pourrais' -> 'peux'"),
 ("gabriel", "Je ne sais pas. Tu es une femme, vous avez le même âge.",
  "I don't know. You're a woman, you're the same age.",
  [(608, "Je ne sais pas"), (609, "Tu es une femme, vous avez le même âge")], ""),
 ("lea", "Le même âge?", "The same age?", [], "new: Andréa's reaction"),
 ("lea", "Toutes les vieilles dames s'entendent bien, c'est ça?", "All old ladies get along, is that it?",
  [(610, "Toutes les vieilles dames s'entendent bien, c'est ça")], ""),
 ("lea", "J'ai seulement trente-quatre ans. Merci beaucoup!", "I'm only thirty-four. Thanks a lot!",
  [(611, "j'ai seulement"), (611, "Merci beaucoup")], "'En tout cas' dropped; '34' written out"),
 ("gabriel", "Désolé, ce n'est pas ce que je voulais dire.", "Sorry, that's not what I meant.",
  [(612, "Désolé"), (612, "ce que je voulais dire")], "'c'est pas' -> 'ce n'est pas'"),
 ("gabriel", "Mais tu es tellement douée!", "But you're so good at this!",
  [(613, "Mais tu es tellement douée")], "unfinished 'douée pour...' closed"),
 ("lea", "Écoute, laisse-lui un peu d'espace.", "Listen, give her a bit of space.",
  [(614, "Laisse-lui un peu d'espace")], "'Écoute' added"),
 ("lea", "Tu vas seulement l'agacer.", "You'll only annoy her.", [(615, "Tu vas seulement l'agacer")], ""),
 ("gabriel", "Alors, je ne fais rien?", "So I don't do anything?", [(616, "Alors")],
  "Gabriel's unfinished 'Alors...' completed"),
 ("lea", "Attends. Au moins jusqu'à demain.", "Wait. Until tomorrow at least.",
  [(617, "Attends. Au moins jusqu'à demain")], ""),
]

OPENER = ("Let's walk through it. Gabriel comes into Andréa's office and admits, quite simply, that he is stuck.")

WALK = [
 (0, None,
  "'Andréa, I don't know what to do.' The verb for 'to know' is wrapped in the two-part negative, and then comes "
  "'what to do'. A line you can use any time you're stuck."),
 (1, None,
  "'Cécile has left. She wants to change agents.' After 'she wants', the next verb stays in its basic dictionary "
  "form. That's how French chains two verbs."),
 (2, None,
  "'Can't you talk to her?' Notice the casual 'you': Andréa and Gabriel are colleagues and friends. The little word "
  "before the verb means 'to her'."),
 (3, None,
  "'Me? What can I say to her?' Andréa is surprised. Why her?"),
 (4, None,
  "'I don't know. You're a woman, you're the same age.' Careful: to say 'the same age' French uses the verb 'to "
  "have', as if age were something you own. In the second half Gabriel switches to the plural 'you', meaning "
  "Andréa and Cécile together. It's the wrong thing to say."),
 (5, None,
  "'The same age?' Andréa repeats it, slowly, the way people do when they can't believe what they've heard."),
 (6, None,
  "'All old ladies get along, is that it?' Both the word for 'all' and the word for 'old' take the feminine plural "
  "form, to match 'ladies'. She is joking, but she is annoyed."),
 (7, None,
  "'I'm only thirty-four. Thanks a lot!' Again, age goes with 'to have': I have thirty-four years. And the thanks "
  "at the end is pure sarcasm. Cécile is over forty, so Gabriel has put his foot in it."),
 (8, None,
  "'Sorry, that's not what I meant.' Literally 'that's not what I wanted to say'. A useful sentence when you need "
  "to take something back."),
 (9, None,
  "'But you're so good at this!' The word for 'gifted' has the feminine ending, because Andréa is a woman. He tries "
  "flattery. Andréa ignores it and gives him real advice."),
 (10, None,
  "'Listen, give her a bit of space.' Two commands in the casual 'you' form. For an order, French simply drops the "
  "word for 'you' and starts with the verb. That's our second grammar point."),
 (11, None,
  "'You'll only annoy her.' The verb 'to go' plus another verb gives the near future, just like 'you're going to' "
  "in English. Gabriel doesn't like waiting."),
 (12, None,
  "'So I don't do anything?' Here the negative pairs with the word for 'nothing'. He sounds like a child being "
  "told no."),
 (13, None,
  "'Wait. Until tomorrow at least.' One more casual command, short and firm. That's the end of the advice."),
]

TRANSITION = "Let's hear it all once more."

OUTRO = ("That's all for this scene; Gabriel will try to follow the advice, and his assistant Hervé will soon drag "
         "him out for a drink to take his mind off things. You followed a real office argument in French, so be "
         "pleased with yourself, and see you next time.")
CLOSING = ("lea", "À demain, Gabriel!")
