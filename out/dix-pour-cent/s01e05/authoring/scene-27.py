# Authoring module for dix-pour-cent s01e05 scene 27 (cues 592-625; merges scene 26 cues 572-591).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-27.py --out out/dix-pour-cent/s01e05/scene-27.json

ID = "dix-pour-cent-s01e05-scene-27"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 27
TITLE = "ASK ne sera pas vendue  (ASK Will Not Be Sold)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 592-625 (with cues 572-591 from merged Scene 26 summarized in the intro). "
               "Cue 601 is given to Andréa to stay within three voices. Long compound clauses and slang in cues 595-596 and 615-619 are simplified for A1.")

INTRO = ("At home with Catherine, Mathias finalized his financial plan with his father-in-law and promised Catherine "
         "he would meet her at the opera tonight. The next morning at ASK, the assistants wonder why Mathias has "
         "called an urgent meeting. Now Andréa, Gabriel, and Arlette gather in Mathias's office to hear his announcement. "
         "Listen to the French first, without worrying about catching every word.")

STORY = [
 ("mathias", "Bonjour à tous. Merci à tous d'être venus.",
  "Good morning, everyone. Thank you all for coming.",
  [(592, "Bonjour à tous"), (593, "Merci à tous d'être venus")], "'malgré vos emplois du temps chargés' omitted for A1"),
 ("mathias", "Je vous ai demandé de venir ce matin pour vous annoncer une bonne nouvelle.",
  "I asked you to come this morning to announce some good news to you.",
  [(599, "Je vous ai demandé de venir ce matin pour vous annoncer une bonne nouvelle")], ""),
 ("mathias", "ASK ne sera pas vendue.",
  "ASK will not be sold.",
  [(600, "ASK ne sera pas vendue")], ""),
 ("lea", "Hélène Kerr garde les parts de Samuel?",
  "Is Hélène Kerr keeping Samuel's shares?",
  [(601, "Hélène Kerr garde les parts de Samuel")], "spoken by Arlette in the episode"),
 ("mathias", "Non. Je les rachète.",
  "No. I'm buying them.",
  [(601, "Non. Je les rachète")], ""),
 ("mathias", "L'avenir d'ASK est assuré. Vous pouvez être soulagés.",
  "ASK's future is secure. You can be relieved.",
  [(602, "L'avenir d'ASK est assuré. Vous pouvez être soulagés")], ""),
 ("gabriel", "Depuis quand tu le sais?",
  "How long have you known?",
  [(603, "Depuis quand tu le sais")], ""),
 ("mathias", "J'ai trouvé un partenaire financier hier.",
  "I found a financial partner yesterday.",
  [(604, "J'ai trouvé un partenaire financier hier")], ""),
 ("lea", "Mais tu ne voulais pas nous le présenter?",
  "But you didn't want to introduce us to him?",
  [(605, "Mais tu ne voulais pas nous le présenter")], ""),
 ("mathias", "Je n'en avais pas l'intention parce que c'est ma femme.",
  "I didn't intend to, because it's my wife.",
  [(606, "Je n'en avais pas l'intention parce que c'est ma femme")], ""),
 ("gabriel", "Quoi? Et on est censés être soulagés?",
  "What? And we're supposed to be relieved?",
  [(607, "Quoi"), (608, "Et on est censés être soulagés")], ""),
 ("lea", "Bravo!",
  "Well done!",
  [(610, "Bravo")], ""),
 ("mathias", "Vous auriez préféré les Allemands?",
  "Would you have preferred the Germans?",
  [(611, "Vous auriez préféré les Allemands")], ""),
 ("gabriel", "Il récupère tout, lui! Même les bonnes nouvelles ont l'air de mauvaises nouvelles!",
  "He takes over everything! Even good news looks like bad news!",
  [(612, "Il récupère tout, lui"), (613, "même les bonnes nouvelles ont l'air de mauvaises nouvelles")], ""),
 ("gabriel", "Oui? Julie Gayet et JoeyStarr ont disparu.",
  "Yes? Julie Gayet and JoeyStarr have disappeared.",
  [(620, "Oui"), (621, "Julie Gayet et JoeyStarr ont disparu")], ""),
 ("lea", "Julie, c'est encore moi. Rappelle-moi, s'il te plaît.",
  "Julie, it's me again. Call me back, please.",
  [(623, "Julie, c'est encore moi"), (624, "Rappelle-moi, s'il te plaît")], ""),
 ("gabriel", "Didier, rappelle-moi. La prod est furieuse!",
  "Didier, call me back. Production is furious!",
  [(624, "Didier, rappelle-moi"), (625, "La prod est furieuse")], ""),
]

OPENER = "Let's walk through the scene line by line. Mathias greets the other partners in his office."

WALK = [
 (0, None,
  "'Good morning, everyone. Thank you all for coming.' After 'for', French uses the infinitive of the helper verb 'to be' plus the past participle 'come'."),
 (1, None,
  "'I asked you to come this morning to announce some good news to you.' Before an infinitive verb, the word for 'for' means 'in order to'."),
 (2, None,
  "'ASK will not be sold.' The future form of 'to be' combines with the past participle 'sold', spelled with a feminine ending because 'an agency' is feminine."),
 (3, None,
  "'Is Hélène Kerr keeping Samuel's shares?' In French, 'the parts' is the everyday word for company shares."),
 (4, None,
  "'No. I'm buying them.' Adding the prefix 're-' to the verb for 'to buy' creates 'to buy back' or 'to buy out'."),
 (5, None,
  "'ASK's future is secure. You can be relieved.' Mathias expects his colleagues to thank him for saving the agency."),
 (6, None,
  "'How long have you known?' Literally 'Since when do you know it?' — French uses the present tense for an action that started in the past and continues right now."),
 (7, None,
  "'I found a financial partner yesterday.' In French, the adjective 'financial' comes after the noun 'partner'."),
 (8, None,
  "'But you didn't want to introduce us to him?' Two object pronouns sit together before the infinitive verb: 'to us' and 'him'."),
 (9, None,
  "'I didn't intend to, because it's my wife.' Literally 'I did not have the intention of it, because it is my wife.'"),
 (10, None,
  "'What? And we're supposed to be relieved?' Gabriel is stunned that Mathias and his wife will now control the whole agency."),
 (11, None,
  "'Well done!' Andréa claps with heavy irony as she realizes they will now have to answer to Mathias."),
 (12, None,
  "'Would you have preferred the Germans?' Mathias reminds them how close they came to being bought by the German media group StarMédia."),
 (13, None,
  "'He takes over everything! Even good news looks like bad news!' Out in the corridor, Gabriel vents to Andréa. The expression 'to have the air of' means 'to look like'."),
 (14, None,
  "'Yes? Julie Gayet and JoeyStarr have disappeared.' Gabriel's phone rings with a new emergency from the film set: after yesterday's passionate love scene in the barn, the two stars have vanished together."),
 (15, None,
  "'Julie, it's me again. Call me back, please.' Andréa leaves an urgent voicemail for her actress."),
 (16, None,
  "'Didier, call me back. Production is furious!' In film slang, 'the prod' is short for the production team."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = ("While Mathias celebrates taking control of ASK, Andréa and Gabriel have to track down two runaway movie stars. "
         "Next, Hervé comes up with a clever phone trick to make Julie Gayet pick up. See you there.")
CLOSING = ("mathias", "ASK ne sera pas vendue.")
