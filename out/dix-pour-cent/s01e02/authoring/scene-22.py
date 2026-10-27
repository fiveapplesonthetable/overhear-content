ID = "dix-pour-cent-s01e02-scene-22"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = "Je déteste les actrices  (I Hate Actresses)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Hélène", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E02"
SOURCE_FILE = "sources/dix-pour-cent/s01/e02.fr.dual.srt"

INTRO = ("At the agency, Line Renaud has just rung in delight: after two hours with the director Gabor, the part is "
         "hers. The trouble is, Andréa has won Françoise Fabian back for the very same role, so she and Gabriel now "
         "have two stars for one part, and they ended up in a furious row. Meanwhile, Mathias takes Samuel's widow, "
         "Hélène Kerr, to a restaurant. She has inherited Samuel's shares in the agency, and Mathias has an offer "
         "for her. We'll take this one from Hélène's side of the table. First the French; don't try to catch "
         "everything.")

STORY = [
 ("lea", "Donc je garde dix-sept pour cent des parts?", "So I keep seventeen percent of the shares?",
  [(631, "des parts")], "'Donc je garderai bien 17 %' -> present tense, number spelled out"),
 ("mathias", "Oui. Vous n'avez rien à faire.", "Yes. You have nothing to do.",
  [(632, "Oui"), (634, "Vous n'avez rien à faire")], ""),
 ("mathias", "Vous touchez simplement les bénéfices.", "You simply collect the profits.",
  [(634, "simplement les bénéfices")], "'toucherez' -> 'touchez'"),
 ("lea", "Comme c'est gentil de penser à ma retraite.", "How kind of you to think of my retirement.",
  [(635, "Comme c'est gentil de penser à ma retraite")], ""),
 ("mathias", "Nous avons fait un énorme effort, Hélène.", "We've made a huge effort, Hélène.",
  [(638, "Nous avons fait un énorme effort"), (638, "Hélène")], "'pour vous soumettre cette offre' cut"),
 ("mathias", "Andréa a pris un crédit sur vingt ans.", "Andréa has taken out a twenty-year loan.",
  [(639, "Andréa a pris un crédit sur 20 ans")], "number spelled out"),
 ("lea", "Et vous devenez le patron d'ASK.", "And you become the boss of ASK.",
  [(641, "patron d'ASK")], "'actionnaire majoritaire et' cut"),
 ("mathias", "Et dans un an, nous rachetons tout.", "And in a year, we buy everything back.",
  [(643, "un an")], "simplified from 'nous pourrons vous racheter entièrement d'ici un an environ'"),
 ("lea", "Avez-vous déjà trompé votre femme, Mathias?", "Have you ever cheated on your wife, Mathias?",
  [(644, "Avez-vous déjà trompé votre femme, Mathias")], ""),
 ("mathias", "Pardonnez-moi, mais je ne parle pas de ça.", "Forgive me, but I don't talk about that.",
  [(645, "Pardonnez-moi, mais je ne")], "'je ne suis pas du genre à me confier' -> 'je ne parle pas de ça'"),
 ("lea", "Samuel m'a beaucoup trompée, surtout avec des actrices.",
  "Samuel cheated on me a lot, mostly with actresses.",
  [(646, "Samuel m'a beaucoup trompée, surtout avec des actrices")], ""),
 ("lea", "Mais vous le saviez, non?", "But you knew that, didn't you?",
  [(647, "vous le saviez")], "'j'imagine que' -> tag 'non?'"),
 ("mathias", "Pas vraiment, non.", "Not really, no.", [(647, "Pas vraiment, non")], ""),
 ("lea", "Je vais vous dire quelque chose. Je déteste les actrices.",
  "I'll tell you something. I hate actresses.",
  [(651, "Je vais vous dire quelque chose"), (652, "Je déteste les actrices")], ""),
 ("lea", "Désolée, Mathias, mais je dois regarder les autres offres.",
  "Sorry, Mathias, but I have to look at the other offers.",
  [(655, "Désolée, Mathias, mais je dois"), (655, "les autres offres")], "'examiner' -> 'regarder'"),
 ("lea", "L'addition, s'il vous plaît.", "The bill, please.", [(656, "L'addition, s'il vous plaît")], ""),
 ("mathias", "D'autres offres?", "Other offers?", [(656, "D'autres offres")], ""),
 ("lea", "Oh, oui. Tout le monde veut la place de Samuel.", "Oh, yes. Everyone wants Samuel's place.",
  [(657, "Oh, oui")], "second sentence retells cue 658 (people are quick to jump on dead bodies) cleanly"),
]

OPENER = ("Let's go back through the meal. Hélène starts by checking the numbers, very calmly.")

WALK = [
 (0, None,
  "'So I keep seventeen percent of the shares?' The first word means 'so', to sum up what she's heard. Big numbers "
  "in French are built like in English: seventeen, then the word for percent."),
 (1, "Oui. Vous n'avez rien à faire.",
  "'Yes. You have nothing to do.' The negative here wraps around the verb with a word meaning 'nothing' instead of "
  "the usual 'not'. And notice the polite 'you': these two stay formal all evening."),
 (2, None,
  "'You simply collect the profits.' The verb is the one for 'to touch', and here it means to receive money. "
  "It sounds like a gift, but Hélène is not fooled."),
 (3, None,
  "'How kind of you to think of my retirement.' The first word, which usually means 'like', here turns the sentence "
  "into an exclamation. She is being sarcastic."),
 (4, None,
  "'We've made a huge effort, Hélène.' Here is the everyday past tense: 'we have' plus the past form of 'to make'. "
  "That's our first grammar point, and you'll hear it all through this scene."),
 (5, None,
  "'Andréa has taken out a twenty-year loan.' The past tense again: 'has' plus 'taken'. The agents are putting their "
  "own money on the table."),
 (6, None,
  "'And you become the boss of ASK.' She sees straight through him. The word for 'boss' is the ordinary one you'd "
  "use for the head of any company."),
 (7, None,
  "'And in a year, we buy everything back.' French often uses the present tense for a plan in the near future, "
  "just like 'we fly out tomorrow' in English."),
 (8, None,
  "'Have you ever cheated on your wife, Mathias?' Our second grammar point: in a polite, careful question, the verb "
  "and 'you' can swap places, joined by a hyphen. The question takes Mathias completely by surprise."),
 (9, None,
  "'Forgive me, but I don't talk about that.' A polite command, 'forgive me', then a firm negative around the verb "
  "'talk'."),
 (10, None,
  "'Samuel cheated on me a lot, mostly with actresses.' The past tense once more. There's an extra letter on the "
  "end of the past form, silent, because the person cheated on is a woman: Hélène herself."),
 (11, None,
  "'But you knew that, didn't you?' A different past tense, for something that went on over time. The little "
  "'no?' at the end works like 'didn't you?' in English."),
 (12, None,
  "'Not really, no.' Mathias tries to look innocent."),
 (13, "Je vais vous dire quelque chose.",
  "'I'll tell you something.' The near future: 'I am going' plus 'to tell'. The little word in the middle means "
  "'to you', and it sits before the verb."),
 (13, "Je déteste les actrices.",
  "'I hate actresses.' Short and brutal, for a woman whose husband ran a talent agency full of them."),
 (14, None,
  "'Sorry, Mathias, but I have to look at the other offers.' The word for 'sorry' takes its feminine spelling "
  "because Hélène is a woman, though it sounds the same. Then 'I must' plus an infinitive."),
 (15, None,
  "'The bill, please.' A sentence worth knowing for any restaurant. The last part is the polite 'please'."),
 (16, None,
  "'Other offers?' Mathias didn't see that coming at all."),
 (17, None,
  "'Oh, yes. Everyone wants Samuel's place.' The phrase for 'everyone' is literally 'all the world', and it takes "
  "a singular verb. In the show she puts it much more darkly, about people jumping on dead bodies."),
]

TRANSITION = "Let's hear the whole dinner once more, without stopping."

OUTRO = ("That's the end of this scene. When you watch it, listen for the polite question with the verb first, the "
         "one that leaves Mathias speechless. See you next time.")
CLOSING = ("lea", "Bonsoir, Mathias.")
