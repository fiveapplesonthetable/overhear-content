ID = "dix-pour-cent-s01e03-scene-25"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 25
TITLE = "La femme du site  (The Woman from the Website)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"

INTRO = ("While Gabriel was busy on the phone, talking the director Solveig Akerfelt into seeing Laura again, "
         "Andréa has a problem of her own. "
         "The tax inspector auditing the agency, Colette Brancillon, is working in a borrowed office, "
         "and Andréa can't shake the feeling that she has seen her somewhere before. "
         "She has: a few nights ago, on a dating website, Andréa chatted with a woman and ended the chat with a very rude message. "
         "That woman was Colette. "
         "We'll hear the scene in French first. Don't worry about every word; the looks between them say a lot.")

STORY = [
 ("lea", "C'est dingue! Je vous ai vue quelque part.", "It's crazy! I've seen you somewhere.",
  [(640, "C'est dingue"), (641, "vue quelque part")], "'je suis sûr de vous avoir vue' simplified to the passé composé"),
 ("colette", "Je vais vous donner un indice.", "I'll give you a clue.", [(642, "Je vais vous donner un indice")], ""),
 ("colette", "Je cite: pas de petites filles comme vous.", "I quote: no little girls like you.",
  [(644, "Je cite"), (645, "petites filles")], "Andréa's crude chat message retold cleanly; 'dans votre genre' -> 'comme vous'"),
 ("lea", "Oh non. C'était vous!", "Oh no. It was you!", [], "new: Andréa realises"),
 ("colette", "Laissez-moi tranquille!", "Leave me alone!", [(647, "Laissez-moi tranquille")], ""),
 ("lea", "C'était juste un malentendu.", "It was just a misunderstanding.", [(648, "c'était juste un malentendu")], ""),
 ("lea", "Colette, on a raté notre premier rendez-vous.", "Colette, we missed our first date.",
  [(650, "Colette, on a raté notre premier rendez-vous")], ""),
 ("colette", "Laissez la porte ouverte, s'il vous plaît.", "Leave the door open, please.",
  [(651, "Laissez la porte ouverte, s'il vous plaît")], ""),
 ("lea", "Vous êtes bien plus jolie en vrai.", "You're much prettier in real life.",
  [(652, "Vous êtes bien plus jolie en vrai")], ""),
 ("colette", "Maintenant vous êtes gentille, à cause de votre agence.", "Now you're being nice, because of your agency.",
  [(654, "votre agence")], "'Vous faites marche arrière... je pourrais nuire à votre agence' simplified"),
 ("colette", "C'est pathétique.", "It's pathetic.", [(655, "C'est pathétique")], ""),
 ("lea", "Pas du tout. Je suis sincère.", "Not at all. I mean it.", [(655, "Pas du tout"), (656, "Je suis sincère")], ""),
 ("colette", "Je ne mélange pas le travail et la vie privée.", "I don't mix work and private life.",
  [(657, "Je ne mélange pas")], "'ma vie professionnelle et ma vie privée' simplified"),
 ("lea", "Je veux juste parler.", "I just want to talk.", [(660, "Je veux juste parler")], ""),
 ("lea", "On peut en rire?", "Can we laugh about it?", [(662, "On peut en rire")], ""),
 ("colette", "Moi, je n'ai pas envie de rire.", "I don't feel like laughing.", [(662, "envie de rire")],
  "'aucune envie' -> 'pas envie'"),
 ("colette", "Partez maintenant. Au revoir, madame Martel.", "Leave now. Goodbye, Ms Martel.",
  [(664, "Partez maintenant"), (666, "Au revoir")], "'Mme' written out as 'madame'"),
 ("lea", "Au revoir, Colette.", "Goodbye, Colette.", [(666, "Au revoir, Colette")], ""),
]

OPENER = ("Let's go back through it. Andréa starts with a smile, trying to place the face.")

WALK = [
 (0, "C'est dingue!",
  "'It's crazy!' The last word is casual, the kind of thing you say to a friend."),
 (0, "Je vous ai vue quelque part.",
  "'I've seen you somewhere.' Here's this scene's first grammar point. Andréa uses the polite 'you' with Colette, and she keeps it all the way through, even while flirting. Colette is a stranger, and she's here on official business."),
 (1, None,
  "'I'll give you a clue.' The verb 'to go' plus another verb: the near future. Colette has been waiting for this moment."),
 (2, None,
  "'I quote: no little girls like you.' She quotes Andréa's own rude message from the dating site, toned down here. The two short words at the start mean 'no' before a noun."),
 (3, None,
  "'Oh no. It was you!' The verb is in the past: 'it was'. Now Andréa understands."),
 (4, None,
  "'Leave me alone!' A polite command, ending in the sound of the polite 'you'. The little word for 'me' is attached after it with a hyphen. Andréa tries to explain."),
 (5, None,
  "'It was just a misunderstanding.' A long word, but you can almost see the English in it: 'mis-heard'. Then she tries charm."),
 (6, None,
  "'Colette, we missed our first date.' The small word for 'we' at the start is the everyday one. The verb 'to miss' is in the past with 'have'. Colette stays very formal."),
 (7, None,
  "'Leave the door open, please.' She doesn't want to be alone in a closed room with Andréa. The last part is the polite 'please', literally 'if it pleases you'."),
 (8, None,
  "'You're much prettier in real life.' The word for 'pretty' takes a feminine ending here. Colette isn't fooled."),
 (9, None,
  "'Now you're being nice, because of your agency.' The word for 'nice' is feminine too, because Andréa is a woman. Colette thinks she's only nice because of the tax audit."),
 (10, None,
  "'It's pathetic.' Easy to guess from the English."),
 (11, None,
  "'Not at all. I mean it.' The second sentence literally says 'I am sincere'. Colette lays down her rule."),
 (12, None,
  "'I don't mix work and private life.' Another grammar point: to make a verb negative, French wraps two little words around it, one before, one after. Andréa insists."),
 (13, None,
  "'I just want to talk.' The verb 'to want' plus another verb in its basic form."),
 (14, None,
  "'Can we laugh about it?' The little word in the middle means 'about it'. Colette is not amused."),
 (15, None,
  "'I don't feel like laughing.' Literally 'I don't have the desire to laugh'. The negative wraps around 'have'."),
 (16, None,
  "'Leave now. Goodbye, Ms Martel.' Another polite command, and her surname: very cold, very official. Andréa answers with her first name."),
 (17, None,
  "'Goodbye, Colette.' Using the first name is Andréa's last little attempt at warmth."),
]

TRANSITION = "Let's listen to the whole scene again."

OUTRO = ("A very awkward meeting, and not the last one between these two. Notice how the polite 'you' "
         "keeps a cool distance between them the whole time. See you next time.")
CLOSING = ("lea", "À bientôt!")
