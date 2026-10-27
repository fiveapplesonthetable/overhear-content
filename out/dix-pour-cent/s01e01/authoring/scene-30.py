ID = "dix-pour-cent-s01e01-scene-30"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 30
TITLE = "Cécile dit oui  (Cécile Says Yes)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Cécile", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("While Camille was meeting Arlette and her little dog, Cécile was still at the agency, thinking hard. "
         "A few minutes ago, Mathias and the American producer Miranda told her the director wants her for the role, "
         "but only if she has a small treatment to make her cheeks look younger. Cécile said no, and then said she didn't know anymore. "
         "Now Mathias catches her on her way out and takes her into his office, because he has one more argument up his sleeve. "
         "Here's the story in French first. Just let it wash over you, you don't need every word.")

STORY = [
 ("mathias", "Cécile! Ça va? On peut parler?", "Cécile! Are you okay? Can we talk?",
  [(774, "Cécile"), (775, "Ça va ? On peut parler")], ""),
 ("mathias", "Viens dans mon bureau.", "Come into my office.",
  [(776, "dans mon bureau")], "'On ne sera pas dérangés dans mon bureau' simplified to an invitation"),
 ("mathias", "Ce n'est pas un drame, Cécile. C'est simple.", "It's not a big drama, Cécile. It's simple.",
  [(777, "drame, Cécile"), (778, "simple")], "'N'en fais pas tout un drame' simplified; hair-dye comparison dropped"),
 ("lea", "Je sais, Mathias. Je suis comédienne.", "I know, Mathias. I'm an actress.",
  [(779, "Je sais, Mathias. Je suis comédienne")], ""),
 ("lea", "Mes amies en parlent tout le temps.", "My friends talk about it all the time.",
  [(780, "en parle")], "'On en parle plus souvent que tu ne prononces le mot euro' simplified"),
 ("lea", "C'est facile, je sais. Mais je ne pensais pas faire ça un jour.", "It's easy, I know. But I never thought I'd do it one day.",
  [(781, "C'est facile"), (783, "je pensais")], "'je pensais ne jamais avoir à y passer' simplified"),
 ("mathias", "Regarde. C'est ma femme.", "Look. That's my wife.",
  [(786, "Ma femme")], "he shows her a photo; 'Regarde. C'est' added"),
 ("mathias", "Quel âge tu lui donnes?", "How old would you say she is?",
  [(787, "Quel âge")], "source 'Quel âge lui donnez-vous ?' put in tu, as everywhere else between them"),
 ("lea", "Quarante ans? Quarante-deux?", "Forty? Forty-two?",
  [(788, "Quarante ? Quarante-deux")], "'ans' added to the first number"),
 ("mathias", "Elle a cinquante et un ans.", "She's fifty-one.",
  [(788, "Elle a")], "'51' written out"),
 ("mathias", "Du Botox chaque année, et les yeux il y a deux ans.", "Botox every year, and her eyes two years ago.",
  [(789, "Du Botox chaque année"), (792, "il y a deux ans")], "'les paupières' -> 'les yeux'; the fillers and cheekbones dropped"),
 ("lea", "Impressionnant. C'est bien fait.", "Impressive. It's well done.",
  [(793, "Impressionnant"), (794, "C'est bien fait")], ""),
 ("lea", "Ça ne te dérange pas?", "Doesn't it bother you?",
  [(795, "dérange pas")], "source 'Ça ne vous dérange pas ?' put in tu"),
 ("mathias", "Non, au contraire.", "No, quite the opposite.",
  [(796, "Non, au contraire")], ""),
 ("lea", "Elle a un bon chirurgien?", "Does she have a good surgeon?",
  [(796, "Elle a un bon chirurgien")], ""),
 ("mathias", "Le meilleur.", "The best.",
  [(797, "Le meilleur")], ""),
 ("mathias", "Miranda? Cécile a accepté.", "Miranda? Cécile has said yes.",
  [(798, "Miranda"), (799, "Cécile a accepté")], "on the phone, after Cécile has gone"),
 ("mathias", "Elle peut se remettre en selle. À bientôt!", "She can get back in the saddle. Talk soon!",
  [(802, "Elle peut se remettre en selle"), (803, "À bientôt")], ""),
]

OPENER = ("Let's go back through it. Mathias spots Cécile in the corridor and greets her in a friendly, easy way, "
          "the way old friends do.")

WALK = [
 (0, None,
  "'Cécile! Are you okay? Can we talk?' The first question is just two short words, and it's the most common check-in there is. "
  "The second one uses the little word for 'we' that the French say all the time in conversation."),
 (1, None,
  "'Come into my office.' It's a casual command, the kind you give someone you know well. Mathias wants a quiet room for this."),
 (2, None,
  "'It's not a big drama, Cécile. It's simple.' Notice the two little words wrapped around the verb: that's how French says 'not'. "
  "One goes before the verb and one comes right after it."),
 (3, "Je sais, Mathias.",
  "'I know, Mathias.' Cécile doesn't need a lecture."),
 (3, "Je suis comédienne.",
  "'I'm an actress.' There's no word for 'an' here: in French, you just say 'I am actress' when you talk about your job."),
 (4, None,
  "'My friends talk about it all the time.' The tiny word in the middle stands for 'about it', so she doesn't have to name the treatment."),
 (5, None,
  "'It's easy, I know. But I never thought I'd do it one day.' This is the heart of it: she knows it's common, she just never imagined it would be her turn. "
  "Mathias stops arguing and takes out a photo instead."),
 (6, None,
  "'Look. That's my wife.' Another casual command, and a surprise: he's going to use his own wife as the example."),
 (7, None,
  "'How old would you say she is?' Literally 'what age do you give her?'. The small word before the verb means 'to her'. "
  "And Mathias uses the casual 'you' with Cécile, because they've known each other for years."),
 (8, None,
  "'Forty? Forty-two?' Cécile makes a polite guess. In French, you say how old someone is with the verb 'to have': you 'have' forty years."),
 (9, None,
  "'She's fifty-one.' Here's that 'to have' again: literally 'she has fifty-one years'. Much older than Cécile guessed."),
 (10, None,
  "'Botox every year, and her eyes two years ago.' The phrase at the end, 'there are two years', is how French says 'two years ago'. "
  "Mathias lists everything, perfectly calm."),
 (11, None,
  "'Impressive. It's well done.' Cécile is honestly struck. Then she asks the question that matters to her."),
 (12, None,
  "'Doesn't it bother you?' Look at the 'not' again: the two little words now wrap around both the 'you' and the verb. "
  "This 'you' is the casual one, like the rest of their chat."),
 (13, None,
  "'No, quite the opposite.' He likes it. That answer settles something in Cécile's mind."),
 (14, None,
  "'Does she have a good surgeon?' A question made just by raising your voice at the end. And with it, Cécile is really saying yes."),
 (15, None,
  "'The best.' Two words, and the deal is done. Once Cécile has left, Mathias picks up the phone."),
 (16, None,
  "'Miranda? Cécile has said yes.' The verb means 'to accept', in the past tense, built with 'to have' plus the past form."),
 (17, None,
  "'She can get back in the saddle. Talk soon!' It's a little joke, because Cécile loves riding horses, and it means she's back in the race for the role."),
]

TRANSITION = "Good. Now let's listen to the whole conversation one more time."

OUTRO = ("That's the end of this scene, and you followed a real grown-up negotiation in French. "
         "Next time you watch it, listen for the little 'not' that wraps around the verb, and you'll hear it everywhere. Until next time.")
CLOSING = ("lea", "Au revoir, Mathias!")
