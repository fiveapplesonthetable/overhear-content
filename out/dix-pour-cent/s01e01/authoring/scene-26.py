ID = "dix-pour-cent-s01e01-scene-26"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 26
TITLE = "Ta nouvelle assistante  (Your New Assistant)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("In her garden, Cécile told Mathias that everyone in this business lies, but he brought news: Miranda is "
         "ready to talk again. It worked. Back at the agency, Gabriel tells Andréa the news: Cécile has said yes to "
         "Mathias, who has stolen his star, and Gabriel is furious. Now Mathias walks in, and Andréa watches the two "
         "men face off. Then Mathias turns to her with a surprise of his own. First the French version; it's fine "
         "if a lot of it goes over your head.")

STORY = [
 ("gabriel", "Merci, Mathias! Tu as volé Cécile!", "Thanks, Mathias! You stole Cécile!",
  [(684, "Merci, Mathias"), (681, "Il a volé Cécile")], "'Il a volé' -> 'Tu as volé' (said to his face)"),
 ("gabriel", "Et ne dis pas que c'était pour le bien de l'agence.",
  "And don't say it was for the good of the agency.",
  [(685, "pour le bien de l'agence")], "'Ne me dis pas' -> 'Et ne dis pas que', no quotation"),
 ("mathias", "Bien sûr que oui, Gabriel.", "Of course it was, Gabriel.",
  [(686, "Bien sûr que oui, Gabriel")], ""),
 ("mathias", "Deux autres agences voulaient Cécile.", "Two other agencies wanted Cécile.",
  [(689, "Deux autres agences")], "'étaient déjà sur elle' -> 'voulaient Cécile'"),
 ("gabriel", "Encore vingt-quatre heures, et elle revient!", "Twenty-four more hours, and she comes back!",
  [(690, "24 heures de plus")], "simplified from 'Si tu m'avais laissé 24 heures de plus, elle serait revenue'"),
 ("mathias", "On n'avait pas vingt-quatre heures.", "We didn't have twenty-four hours.",
  [(691, "on n'avait pas 24 heures")], "'Pour ce dossier' cut"),
 ("gabriel", "Ce n'est pas un dossier. C'est Cécile.", "She's not a file. She's Cécile.",
  [(691, "C'est pas un"), (692, "C'est Cécile")], "'C'est pas' -> 'Ce n'est pas'"),
 ("mathias", "Oui, c'est Cécile.", "Yes, it's Cécile.", [(692, "Oui, c'est Cécile")], ""),
 ("lea", "Félicitations, Mathias.", "Congratulations, Mathias.", [(693, "Félicitations")], "'Mathias' added"),
 ("lea", "Tu as volé la star de Gabriel avec beaucoup de classe.",
  "You stole Gabriel's star with a lot of class.",
  [(694, "Tu as volé la star de Gabriel avec beaucoup de classe")], ""),
 ("lea", "Tu es fier de toi?", "Are you proud of yourself?", [(695, "Tu en es fier")],
  "'Tu en es fier' -> 'Tu es fier de toi'"),
 ("mathias", "J'ai sauvé une cliente de l'agence, c'est tout.", "I saved one of the agency's clients, that's all.",
  [(698, "sauver une cliente de l'agence")], "'Tout ce que j'ai fait, c'est sauver' -> 'J'ai sauvé ..., c'est tout'"),
 ("mathias", "Maintenant, laisse-moi te dire un truc.", "Now, let me tell you something.",
  [(699, "Maintenant, laisse-moi te dire un truc")], ""),
 ("mathias", "C'est ta nouvelle assistante. Elle a dit à Cécile qu'elle était trop vieille.",
  "It was your new assistant. She told Cécile she was too old.",
  [(700, "C'est ta nouvelle assistante"), (700, "qu'elle était trop vieille")],
  "split into two sentences; 'lui' -> 'à Cécile'"),
 ("lea", "Camille? Mais pourquoi?", "Camille? But why?", [],
  "Andréa's reaction (in the source Mathias does the talking)"),
 ("mathias", "Tu l'as trouvée où? Elle est dangereuse.", "Where did you find her? She's dangerous.",
  [(701, "Tu l'as trouvée où ? Elle est dangereuse")], ""),
 ("mathias", "Je n'en ai pas parlé à Gabriel. Mais règle ça, tu veux bien?",
  "I haven't told Gabriel. But sort it out, will you?",
  [(705, "Je n'en ai pas parlé à Gabriel"), (706, "mais règle ça, tu veux bien")], ""),
 ("mathias", "Bonne journée.", "Have a nice day.", [(707, "Bonne journée")], ""),
]

OPENER = ("Let's go back over it. Gabriel starts with a thank-you, but he doesn't mean it at all.")

WALK = [
 (0, "Merci, Mathias!",
  "'Thanks, Mathias!' Pure sarcasm. Then he says what he really thinks."),
 (0, "Tu as volé Cécile!",
  "'You stole Cécile!' This is the everyday past tense: the verb 'to have' plus the past form of 'steal'. It's the "
  "grammar point of this scene, and you'll hear it again and again."),
 (1, None,
  "'And don't say it was for the good of the agency.' A negative command: the negative wraps around the casual "
  "'say'. Gabriel knows exactly what Mathias will answer."),
 (2, None,
  "'Of course it was, Gabriel.' Literally 'of course yes'. Mathias doesn't apologise for anything."),
 (3, None,
  "'Two other agencies wanted Cécile.' The verb is 'to want' in the past, describing how things stood: a "
  "different past tense, used for background."),
 (4, None,
  "'Twenty-four more hours, and she comes back!' Gabriel speaks in the present to make it vivid: one more day, "
  "and she would have come home."),
 (5, None,
  "'We didn't have twenty-four hours.' The word at the start means 'we' in everyday speech. And the negative wraps "
  "around the verb again."),
 (6, None,
  "'She's not a file. She's Cécile.' The word for 'file' is what agents call a case or a deal. For Gabriel she's a "
  "person, not a deal."),
 (7, None,
  "'Yes, it's Cécile.' Mathias repeats it calmly, and Gabriel storms off. Now Andréa speaks up."),
 (8, None,
  "'Congratulations, Mathias.' The word looks long but it's simply 'congratulations'. She says it drily."),
 (9, None,
  "'You stole Gabriel's star with a lot of class.' The past tense again, with 'have'. To say 'Gabriel's star', French "
  "says 'the star of Gabriel'."),
 (10, None,
  "'Are you proud of yourself?' A question made just by raising your voice at the end. Mathias isn't ashamed one bit."),
 (11, None,
  "'I saved one of the agency's clients, that's all.' Past tense with 'have' once more: 'I have saved'. The word "
  "for 'client' has an extra letter at the end because Cécile is a woman."),
 (12, None,
  "'Now, let me tell you something.' The last word is a very casual word for 'thing'. Andréa doesn't see it coming."),
 (13, "C'est ta nouvelle assistante.",
  "'It was your new assistant.' The word for 'new' takes its feminine form, because the assistant is a woman: "
  "Camille."),
 (13, "Elle a dit à Cécile qu'elle était trop vieille.",
  "'She told Cécile she was too old.' The past tense with 'have' again, plus the feminine of 'old'. So now Andréa "
  "knows who talked."),
 (14, None,
  "'Camille? But why?' Andréa hired her only this morning."),
 (15, None,
  "'Where did you find her? She's dangerous.' The question word for 'where' comes at the very end, which is common "
  "in spoken French."),
 (16, "Je n'en ai pas parlé à Gabriel.",
  "'I haven't told Gabriel.' Literally 'I haven't spoken of it to Gabriel'. So the secret stays between them."),
 (16, "Mais règle ça, tu veux bien?",
  "'But sort it out, will you?' A casual command with a soft tag at the end, 'you want, okay?'. It sounds polite, "
  "but it's an order."),
 (17, None,
  "'Have a nice day.' Literally 'good day'. A sweet goodbye that leaves Andréa with a big problem."),
]

TRANSITION = "Here is the whole scene one more time."

OUTRO = ("That's it for this scene. When you watch it, listen for the past tense with 'have' each time someone is "
         "accused of something; you'll hear plenty of it. Until next time.")
CLOSING = ("lea", "Bonne journée, Mathias!")
