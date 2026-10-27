# Authoring module for dix-pour-cent s01e04 scene 15 (cues 361-387, plus merged scene 14 cues 339-360).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-15.py --out out/dix-pour-cent/s01e04/scene-15.json

ID = "dix-pour-cent-s01e04-scene-15"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 15
TITLE = "Un mois au Canada  (A Month in Canada)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "augustin": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Audrey", "augustin": "Augustin", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 361-387. Merged scene 14 (cues 339-360: Audrey praising Augustin's script while her little "
               "girl wanders out, and Mathias phoning François in the corridor to accept StarMédia's offer, "
               "overheard by Noémie) is retold in the intro bridge. In the second part (378-387), the costume-drama "
               "director's brief replies are folded into Gabriel's lines.")

INTRO = ("Audrey Fleurot has arrived at ASK in a painfully tight girdle with her two small children, and while she "
         "tells the young director Augustin how funny and powerful she finds his script, her little girl wanders "
         "through the corridors looking for her mother. At that very moment Mathias steps outside, phones François "
         "at the rival agency StarMédia to accept his offer, and is overheard by a heartbroken Noémie. Back inside "
         "Mathias's office, Augustin reveals a detail of the shoot that Mathias carefully hid from Audrey. Listen "
         "to the French first; you don't need to catch every word.")

STORY = [
 ("augustin", "Moi aussi, je suis très content.", "I'm very pleased too.",
  [(361, "moi aussi, je suis content")], ""),
 ("augustin", "On va tourner d'abord la partie canadienne.", "We're going to shoot the Canadian part first.",
  [(362, "d'abord la partie canadienne")], "future 'On tournera' -> near future 'On va tourner'"),
 ("lea", "Quelle partie canadienne?", "What Canadian part?",
  [(363, "Quelle partie canadienne")], ""),
 ("augustin", "Un mois de tournage au Canada. Mathias ne vous l'a pas dit?", "A month of filming in Canada. Didn't Mathias tell you?",
  [(364, "Un mois de tournage au Canada. Mathias ne vous l'a pas dit")], ""),
 ("lea", "Non, il a oublié.", "No, he forgot.",
  [(365, "Non"), (365, "il a")], "'il a dû oublier' simplified to passé composé"),
 ("augustin", "Je vous explique maintenant. C'est dans le nord, près des lacs.", "I'll explain to you now. It's in the north, near the lakes.",
  [(366, "je vous explique maintenant"), (367, "C'est dans le nord, près des lacs")], ""),
 ("augustin", "Le paysage est magnifique!", "The landscape is magnificent!",
  [(368, "paysage"), (370, "magnifique")], ""),
 ("lea", "Pardon, mais il y a des endroits incroyables autour de Paris.", "Sorry, but there are incredible places around Paris.",
  [(370, "Pardon, mais"), (371, "Il y a des endroits incroyables"), (371, "autour de Paris")], ""),
 ("lea", "Vous connaissez Rambouillet? Il y a aussi de grandes forêts!", "Do you know Rambouillet? There are big forests there too!",
  [(372, "Vous connaissez Rambouillet"), (373, "forêts")], "'similaire aux forêts canadiennes' simplified"),
 ("augustin", "Le film raconte la vie de ma mère, et elle est canadienne.", "The film tells the story of my mother's life, and she's Canadian.",
  [(375, "le film"), (375, "de la vie de ma mère, et elle est canadienne")], "'s'inspire de' simplified to 'raconte'"),
 ("lea", "Ah, je vois.", "Oh, I see.",
  [(376, "Ah, je vois")], ""),
 ("augustin", "Donc je veux vraiment tourner là-bas.", "So I really want to shoot over there.",
  [(377, "Donc je"), (377, "tourner là-bas")], "'tiens à' -> 'veux vraiment'"),
 ("lea", "Oui, bien sûr.", "Yes, of course.",
  [(377, "Oui")], ""),
 ("gabriel", "Je ne dis pas de remplacer Julie Gayet par une actrice noire.", "I'm not saying to replace Julie Gayet with a Black actress.",
  [(380, "Je ne dis pas de remplacer Julie Gayet par une actrice noire")], ""),
 ("gabriel", "Mais je peux vous envoyer Sofia Leprince pour jouer le rôle de la comtesse.", "But I can send you Sofia Leprince to play the role of the countess.",
  [(382, "je peux"), (382, "vous envoyer Sofia Leprince"), (383, "pour jouer le rôle de la comtesse")], ""),
 ("gabriel", "C'est parfait! À bientôt.", "That's perfect! See you soon.",
  [(384, "C'est parfait"), (385, "À bientôt")], ""),
]

OPENER = ("Let's go through it step by step. Augustin is delighted that Audrey likes his script, and starts talking "
          "about the shooting schedule.")

WALK = [
 (0, None,
  "'I'm very pleased too.' Literally 'me too, I am very pleased', using the masculine form of the adjective."),
 (1, None,
  "'We're going to shoot the Canadian part first.' The verb for filming a movie is the same as the verb 'to turn'."),
 (2, None,
  "'What Canadian part?' The question word at the start is in its feminine form to match 'part'."),
 (3, None,
  "'A month of filming in Canada. Didn't Mathias tell you?' Before a masculine country name like Canada, French "
  "uses the combined word for 'to the'."),
 (4, None,
  "'No, he forgot.' Audrey covers for Mathias, though she is privately furious that he hid a whole month abroad."),
 (5, None,
  "'I'll explain to you now. It's in the north, near the lakes.' French uses the present tense here where English "
  "says 'I will explain'."),
 (6, None,
  "'The landscape is magnificent!' Augustin is carried away by his artistic vision."),
 (7, None,
  "'Sorry, but there are incredible places around Paris.' Audrey cannot bear the thought of leaving her babies for "
  "a month."),
 (8, None,
  "'Do you know Rambouillet? There are big forests there too!' Rambouillet is a wooded town just outside Paris. Notice "
  "how 'some' shrinks to the short word for 'of' before a plural adjective."),
 (9, None,
  "'The film tells the story of my mother's life, and she's Canadian.' That settles the question of filming near "
  "Paris."),
 (10, None,
  "'Oh, I see.' Three simple words when you finally understand."),
 (11, None,
  "'So I really want to shoot over there.' The hyphenated word at the end means 'over there'."),
 (12, None,
  "'Yes, of course.' Meanwhile, in the next office, Gabriel is pitching Sofia to a director making an eighteenth-"
  "century costume film."),
 (13, None,
  "'I'm not saying to replace Julie Gayet with a Black actress.' Julie Gayet is a well-known French star."),
 (14, None,
  "'But I can send you Sofia Leprince to play the role of the countess.' Gabriel tries to get Sofia a noble part."),
 (15, None,
  "'That's perfect! See you soon.' The director agrees to see her, and Gabriel is thrilled."),
]

TRANSITION = "Now let's listen to the whole scene again."

OUTRO = ("So Gabriel has won Sofia an audition, while Audrey has just learned that the role means a month in "
         "Canada. And Augustin still has one more question for her: can she really pole dance? See you in the next "
         "scene.")
CLOSING = ("gabriel", "Très bien! Voilà!")
