ID = "dix-pour-cent-s01e03-scene-20"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 20
TITLE = "Je veux être agent  (I Want to Be an Agent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "dominique": "marcel"}
LABELS = {"lea": "Camille", "mathias": "Mathias", "dominique": "Dominique"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"

INTRO = ("In her little loft, Camille's mother helped her dress for the César awards, the French Oscars. She asked for "
         "photos of the stars, and warned her not to expect anything from Mathias. Now Camille is at the ceremony "
         "reception, among the gold lights and the champagne, and Mathias has a surprise for her: he wants her to "
         "meet a famous producer. The next morning, though, Camille will have something to say about it. "
         "First, the whole thing in French; don't worry if it goes by fast.")

STORY = [
 ("mathias", "Va chercher du champagne au bar.", "Go and get some champagne at the bar.",
  [(516, "Va chercher du champagne au bar")], ""),
 ("lea", "D'accord. À tout à l'heure.", "Okay. See you in a bit.",
  [(517, "D'accord"), (519, "À tout à l'heure")], ""),
 ("mathias", "Camille! Par ici. Je te présente Dominique Besnehard.",
  "Camille! Over here. This is Dominique Besnehard.",
  [(530, "Camille ! Par ici"), (531, "Je te présente Dominique Besnehard")], ""),
 ("lea", "Bonjour, ravie.", "Hello, delighted to meet you.", [(532, "Bonjour, ravie")], ""),
 ("mathias", "Un producteur.", "A producer.", [(532, "Un producteur")], ""),
 ("dominique", "Bonjour, Camille. Mathias m'a beaucoup parlé de vous.",
  "Hello, Camille. Mathias has told me a lot about you.",
  [(533, "Bonjour, Camille. Mathias m'a beaucoup parlé de vous")], ""),
 ("lea", "Ah bon? En bien, j'espère!", "Really? Good things, I hope!", [(534, "Ah bon ? En bien, j'espère")], ""),
 ("dominique", "Absolument. Vous aimez le cinéma?", "Absolutely. Do you like films?",
  [(534, "Absolument")], "'Vous avez envie de découvrir le monde des tournages?' (535) simplified to A1"),
 ("lea", "Et comment! C'est mon rêve.", "You bet! It's my dream.", [(536, "Et comment ! C'est mon rêve")], ""),
 ("dominique", "Je peux vous offrir un stage. C'est sur le prochain film de Guillaume Gallienne.",
  "I can offer you an internship. It's on Guillaume Gallienne's next film.",
  [(539, "Je peux vous offrir un stage"), (539, "le prochain film de Guillaume Gallienne")], "split into two sentences"),
 ("lea", "Vraiment?", "Really?", [(540, "Vraiment")], ""),
 ("mathias", "Elle est parfaite pour ça.", "She's perfect for it.", [(540, "Elle est parfaite pour ça")], ""),
 ("dominique", "Ma carte. Appelez-moi au bureau.", "My card. Call me at the office.",
  [(543, "Ma carte"), (544, "Appelez-moi au bureau")], ""),
 ("lea", "Je ne vais pas appeler Besnehard.", "I'm not going to call Besnehard.",
  [(549, "Je ne vais pas appeler Besnehard")], "the next morning (merged scene 21)"),
 ("mathias", "Pourquoi? C'est un super producteur!", "Why? He's a great producer!",
  [(550, "Pourquoi ? C'est un super producteur")], ""),
 ("lea", "Je suis bien ici. Je veux apprendre à être agent.", "I'm happy here. I want to learn to be an agent.",
  [(551, "je suis bien ici"), (552, "Je veux apprendre à être agent")], ""),
 ("lea", "Je n'ai aucune qualification, mais je peux apprendre.", "I have no qualifications, but I can learn.",
  [(553, "je n'ai aucune qualification, mais je peux apprendre")], "'Je sais que' cut"),
 ("lea", "Sinon, je cherche un poste dans une autre agence.", "Otherwise, I'll look for a job at another agency.",
  [(555, "un poste dans une autre agence")], "'Je chercherai' -> 'Sinon, je cherche'; cue 554 folded into 'Sinon'"),
]

OPENER = ("Let's go through it slowly. At the reception, Mathias sends Camille off on a little errand.")

WALK = [
 (0, None,
  "'Go and get some champagne at the bar.' A casual command: Mathias uses the casual 'you' with Camille. The small "
  "word before champagne means 'some'."),
 (1, None,
  "'Okay. See you in a bit.' The second phrase is a handy goodbye for when you'll meet again the same day."),
 (2, "Camille! Par ici.",
  "'Camille! Over here.' Literally 'by here'. Mathias waves to her across the room."),
 (2, "Je te présente Dominique Besnehard.",
  "'This is Dominique Besnehard.' Literally 'I present to you'. It's the standard way to introduce one person to "
  "another. Camille answers very politely."),
 (3, None,
  "'Hello, delighted to meet you.' The word for 'delighted' ends with an extra silent letter, because Camille is "
  "a woman."),
 (4, None,
  "'A producer.' Mathias adds it in a low voice, so that she knows how important this man is."),
 (5, None,
  "'Hello, Camille. Mathias has told me a lot about you.' The everyday past tense, 'has spoken', with the little "
  "word for 'me' tucked in before the helper verb. Notice he uses the polite 'you' with her."),
 (6, None,
  "'Really? Good things, I hope!' Literally 'in good'. A light, charming answer."),
 (7, None,
  "'Absolutely. Do you like films?' A question made just by raising the voice at the end."),
 (8, None,
  "'You bet! It's my dream.' The first two words literally mean 'and how!', a cheerful way to say 'absolutely'."),
 (9, "Je peux vous offrir un stage.",
  "'I can offer you an internship.' Here's our grammar point: 'I can' followed by a verb in its dictionary form, "
  "with the polite word for 'you' placed just before that second verb."),
 (9, "C'est sur le prochain film de Guillaume Gallienne.",
  "'It's on Guillaume Gallienne's next film.' To say 'Gallienne's film', French says 'the film of Gallienne'."),
 (10, None,
  "'Really?' Camille can hardly believe it."),
 (11, None,
  "'She's perfect for it.' The adjective is in its feminine form, because it's about Camille. Mathias looks very "
  "pleased with himself."),
 (12, None,
  "'My card. Call me at the office.' A polite command, 'call me', with 'me' stuck to the verb by a hyphen."),
 (13, None,
  "'I'm not going to call Besnehard.' The next morning, in the agency corridor. This is the near future, 'I am going "
  "to call', made negative: the two little words of the negative wrap around 'going'."),
 (14, None,
  "'Why? He's a great producer!' Mathias doesn't understand. The word for 'great' here is the casual 'super'."),
 (15, "Je suis bien ici.",
  "'I'm happy here.' Literally 'I am well here'. It's what Camille has been saying since she arrived."),
 (15, "Je veux apprendre à être agent.",
  "'I want to learn to be an agent.' Three verbs in a row: 'I want', then 'to learn', then 'to be'. Notice there's "
  "no word for 'an' before a job in French."),
 (16, None,
  "'I have no qualifications, but I can learn.' The negative here uses a word that means 'not a single one'."),
 (17, None,
  "'Otherwise, I'll look for a job at another agency.' The first word means 'if not'. She's polite, but it's a "
  "real ultimatum."),
]

TRANSITION = "Let's listen to the whole scene again from the start."

OUTRO = ("That's all for this scene. When you watch it, listen for the moment Camille says what she really wants to "
         "be; Mathias does not see it coming. See you next time.")
CLOSING = ("lea", "À demain!")
