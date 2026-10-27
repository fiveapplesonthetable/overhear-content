# Authoring module for dix-pour-cent s02e04 scene 07 (cues 174-191).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-07.py --out out/dix-pour-cent/s02e04/scene-07.json

ID = "dix-pour-cent-s02e04-scene-07"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 7
TITLE = "Les essais de voix  (Voice Tests)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 174-191. At home, Sofia tells Gabriel she had drinks with Julien Doré, "
               "who invited her to do studio voice tests for his musical project. "
               "Adapted for A1 French.")

INTRO = ("At Gabriel's apartment, Sofia reveals that she had a drink with pop star Julien Dore. "
         "Although Gabriel initially questions why Julien bypassed normal agent protocol, he is thrilled to learn that Sofia has a major recording audition. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "J'ai pris un verre avec Julien Doré.",
  "I had a drink with Julien Doré.",
  [(174, "Non, j'ai pris un verre avec Julien Doré.")], "Sofia shares her news"),
 ("gabriel", "Vraiment? Pourquoi tu ne m'as rien dit?",
  "Really? Why didn't you tell me anything?",
  [(175, "Vraiment ? C'est super."), (176, "Pourquoi tu me l'as pas dit ?")], "Gabriel is surprised"),
 ("lea", "Je te le dis maintenant, Gabriel.",
  "I am telling you now, Gabriel.",
  [(177, "Je te le dis là.")], "Sofia replies calmly"),
 ("gabriel", "Comment a-t-il eu ton numéro?",
  "How did he get your number?",
  [(178, "Il a ton numéro ?")], "Gabriel asks"),
 ("lea", "Je le lui ai donné hier soir.",
  "I gave it to him yesterday evening.",
  [(179, "Je le lui ai donné à la soirée d'Elvis.")], "Sofia explains"),
 ("gabriel", "Il aurait dû m'appeler d'abord.",
  "He should have called me first.",
  [(180, "Sauf qu'il aurait dû m'appeler.")], "Gabriel mentions protocol"),
 ("gabriel", "Ou appeler ton agent officiel, Mathias.",
  "Or call your official agent, Mathias.",
  [(181, "Ou parlé directement à Mathias, ton agent.")], "Gabriel adds"),
 ("lea", "C'est toi qui as tout fait.",
  "You are the one who did everything.",
  [(182, "C'est toi qui as fait le travail, qui nous as présentés...")], "Sofia credits Gabriel"),
 ("lea", "C'est grâce à toi, mon amour.",
  "It is thanks to you, my love.",
  [(183, "C'est grâce à toi.")], "Sofia reassures Gabriel"),
 ("gabriel", "Tu as raison. Et alors?",
  "You are right. And so?",
  [(184, "Tu as raison... Et donc ?")], "Gabriel listens eagerly"),
 ("lea", "Je fais des essais de voix demain!",
  "I am doing voice tests tomorrow!",
  [(185, "Je fais des essais voix dans son studio demain.")], "Sofia announces the audition"),
 ("gabriel", "C'est une nouvelle fantastique, chérie.",
  "That is fantastic news, darling.",
  [(186, "Fantastique."), (187, "C'est fantastique, chérie.")], "Gabriel celebrates"),
 ("gabriel", "Et en plus, tu as apporté des chocolats!",
  "And what is more, you brought chocolates!",
  [(188, "Et en plus tu as fait à dîner."), (190, "Des chocolats !")], "Gabriel smiles happily"),
]

OPENER = "Let's examine how Sofia and Gabriel discuss the exciting studio audition step by step to learn natural conversational phrasing."

WALK = [
 (0, None,
  "'I had a drink with Julien Dore.' Sofia shares that she met up casually with the famous musician."),
 (1, None,
  "'Really? Why didn't you tell me anything?' Gabriel is taken aback that she kept the meeting secret until now."),
 (2, None,
  "'I am telling you now, Gabriel.' Sofia gently reassures him that she is being fully transparent."),
 (3, None,
  "'How did he get your number?' Gabriel wonders how Julien obtained her personal phone contact."),
 (4, None,
  "'I gave it to him yesterday evening.' Sofia clarifies that she exchanged numbers at the agency party."),
 (5, None,
  "'He should have called me first.' Gabriel points out standard professional courtesy between agent and client."),
 (6, None,
  "'Or call your official agent, Mathias.' Gabriel worries that Mathias will be furious to find out about the direct artist contact."),
 (7, None,
  "'You are the one who did everything.' Sofia lovingly reminds Gabriel that he created this opportunity for her."),
 (8, None,
  "'It is thanks to you, my love.' Sofia reaffirms her gratitude and deep affection for Gabriel."),
 (9, None,
  "'You are right. And so?' Gabriel smiles, setting aside his agent worries to hear the big outcome."),
 (10, None,
  "'I am doing voice tests tomorrow!' Sofia delivers the thrilling news that Julien invited her into his recording studio."),
 (11, None,
  "'That is fantastic news, darling.' Gabriel warmly congratulates her on this major breakthrough."),
 (12, None,
  "'And what is more, you brought chocolates!' Gabriel happily spots the sweet treat she bought for dinner."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Sofia's talent earns her a coveted voice trial with Julien Dore, celebrating a sweet domestic victory with Gabriel. "
         "Let's review the vocabulary and everyday conversational idioms from this scene.")

CLOSING = ("gabriel", "Et en plus, tu as apporté des chocolats!")
