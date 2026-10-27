ID = "dix-pour-cent-s01e01-scene-02"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = "Je vais déjeuner deux fois  (I'll Have Lunch Twice)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "magali": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "magali": "Magali", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Last time, Cécile de France turned up late to a photo shoot, still smelling of her horse-riding lesson, and "
         "her agent Gabriel learned by message that Tarantino doesn't want her because of her age. He kept it to "
         "himself. "
         "Now it's morning at the agency in Paris. The doors open, the phones start ringing, and we follow "
         "Andréa, the toughest and fastest-talking agent at ASK, as she rushes in with her assistant Magali reading "
         "out her diary. Mathias, a smooth, ambitious agent, is already on the phone talking money. "
         "Here it is in French first; just let it wash over you.")

STORY = [
 ("lea", "Bonjour! Salut, Mathias.", "Morning! Hi, Mathias.",
  [(74, "Bonjour"), (75, "Salut, Mathias")], "put together from two greetings in the busy entrance"),
 ("mathias", "Oui, trois cent mille. Je parle de ses vingt ans de carrière.",
  "Yes, three hundred thousand. I'm talking about his twenty years of career.",
  [(75, "Oui, 300 000"), (78, "Je parle de ses 20 ans de carrière")], "on the phone; numbers written out in words"),
 ("lea", "Magali, je dois voir la pièce de Koltès cette semaine.", "Magali, I have to see the Koltès play this week.",
  [(79, "Je dois voir la pièce de Koltès cette semaine")], "'Magali,' added"),
 ("magali", "Deux places pour mardi? Mardi, tu as le film de Kechiche.",
  "Two tickets for Tuesday? On Tuesday you've got the Kechiche film.",
  [(80, "Deux places pour mardi"), (81, "Mardi tu as le film de Kechiche")], ""),
 ("lea", "Jeudi, alors.", "Thursday, then.",
  [(82, "Jeudi, alors")], ""),
 ("magali", "Et demain, tu déjeunes avec Audiard.", "And tomorrow you're having lunch with Audiard.",
  [(83, "déjeuner avec Audiard"), (83, "demain")], "'et Arestrup' dropped; turned into a sentence"),
 ("lea", "Je prends ça. Merci.", "I'll take that. Thanks.",
  [(84, "Je prends ça. Merci")], ""),
 ("magali", "Tu déjeunes aussi avec Dany Boon demain.", "You're also having lunch with Dany Boon tomorrow.",
  [(85, "Tu déjeunes avec Dany Boon demain")], "'aussi' added"),
 ("lea", "Tu es pénible, Magali.", "You're a pain, Magali.",
  [(86, "Tu es pénible, Magali")], ""),
 ("lea", "L'un à midi, l'autre à quatorze heures. Je vais déjeuner deux fois.",
  "One at noon, the other at two. I'm going to have lunch twice.",
  [(89, "l'un à midi, l'autre à quatorze heures"), (89, "deux fois")], "'Je déjeunerai' -> 'Je vais déjeuner'"),
 ("lea", "Appelle Clémentine. Dis-lui que je ne peux pas venir ce soir.",
  "Call Clémentine. Tell her I can't come tonight.",
  [(90, "Appelle Clémentine"), (90, "dis-lui que je ne peux pas venir ce soir")], "'excuse-toi' dropped"),
 ("magali", "Clémentine? Celle de la semaine dernière?", "Clémentine? The one from last week?",
  [(91, "Clémentine ? Celle de la semaine dernière ?")], ""),
 ("lea", "Il y a une autre Clémentine?", "Is there another Clémentine?",
  [(91, "une autre Clémentine")], "her cruder joke retold cleanly"),
 ("magali", "Qu'est-ce que je lui dis?", "What do I tell her?",
  [(94, "Qu'est-ce que je lui dis ?")], ""),
 ("lea", "Je ne sais pas. Trouve quelque chose.", "I don't know. Think of something.",
  [(93, "Je ne sais pas"), (97, "Trouve quelque chose")], ""),
 ("lea", "Dis que j'ai une réunion. Improvise!", "Say I've got a meeting. Improvise!",
  [(98, "une réunion"), (98, "Improvise !")], "'Dis que t'as une réunion ou un truc' simplified"),
 ("mathias", "Gabriel. Tu ne rappelles pas Cécile de France?", "Gabriel. Aren't you calling Cécile de France back?",
  [(99, "Gabriel."), (100, "Tu ne rappelles pas Cécile de France ?")], "said to Gabriel across the office"),
]

OPENER = ("Let's take it apart. Andréa sweeps in through the door, greeting everyone in one breath, while Mathias "
          "barely looks up from his call.")

WALK = [
 (0, None,
  "'Morning! Hi, Mathias.' The first word is the all-purpose greeting; the second is the casual hello you use with "
  "people you know well. Colleagues here are all on first-name terms."),
 (1, "Oui, trois cent mille.",
  "'Yes, three hundred thousand.' Mathias is negotiating a fee for an actor, and he doesn't waste words."),
 (1, "Je parle de ses vingt ans de carrière.",
  "'I'm talking about his twenty years of career.' In other words: you're not paying for twenty days of filming, "
  "you're paying for twenty years of being a star."),
 (2, None,
  "'Magali, I have to see the Koltès play this week.' The verb for 'have to' comes first, then the plain verb 'to "
  "see'. Koltès is a famous French playwright."),
 (3, "Deux places pour mardi?",
  "'Two tickets for Tuesday?' The word for ticket here really means 'seat', as in a seat at the theatre."),
 (3, "Mardi, tu as le film de Kechiche.",
  "'On Tuesday you've got the Kechiche film.' Magali uses the casual 'you' with her boss, and that's normal at ASK. "
  "Days of the week need no little word in front of them."),
 (4, None,
  "'Thursday, then.' Andréa decides in a second."),
 (5, None,
  "'And tomorrow you're having lunch with Audiard.' French has a single verb that means 'to have lunch'. Audiard is "
  "a big film director, so Andréa grabs the chance."),
 (6, None,
  "'I'll take that. Thanks.' The present tense is enough to say what you're about to do."),
 (7, None,
  "'You're also having lunch with Dany Boon tomorrow.' The trouble is she already has a lunch with a famous comedian "
  "tomorrow."),
 (8, None,
  "'You're a pain, Magali.' Said with a sigh, to the one person keeping her life in order."),
 (9, "L'un à midi, l'autre à quatorze heures.",
  "'One at noon, the other at two.' French offices often use the twenty-four-hour clock, so two in the afternoon "
  "is fourteen hours."),
 (9, "Je vais déjeuner deux fois.",
  "'I'm going to have lunch twice.' Here's a handy pattern: the verb 'to go' plus a plain verb gives you the near "
  "future, exactly like 'I'm going to' in English."),
 (10, "Appelle Clémentine.",
  "'Call Clémentine.' Now a string of orders in the casual form. Clémentine is a woman Andréa is seeing, and she wants "
  "to cancel tonight's date."),
 (10, "Dis-lui que je ne peux pas venir ce soir.",
  "'Tell her I can't come tonight.' The command comes first, joined to the little word for 'to her'. And notice the "
  "negative again, wrapped around the verb 'can'."),
 (11, None,
  "'Clémentine? The one from last week?' Magali can't keep up with Andréa's love life."),
 (12, None,
  "'Is there another Clémentine?' Andréa teases her right back."),
 (13, None,
  "'What do I tell her?' A useful question starter that simply means 'what'."),
 (14, None,
  "'I don't know. Think of something.' Another casual command: think up, come up with something."),
 (15, None,
  "'Say I've got a meeting. Improvise!' That last word is the same as in English, and it's Andréa's motto. Meanwhile, "
  "across the room, Mathias stops at Gabriel's desk."),
 (16, None,
  "'Gabriel. Aren't you calling Cécile de France back?' Cécile has been calling, and Gabriel hasn't picked up. He "
  "mumbles that he'll call her. Only we know why he's hiding."),
]

TRANSITION = "Let's hear the morning rush once more, all the way through."

OUTRO = ("That's a typical morning at ASK: two lunches, one cancelled date and a lot of casual commands. Don't worry if "
         "it felt fast; it is fast, even for the French. See you in the next scene.")
CLOSING = ("lea", "Allez, au travail!")
