# Authoring module for dix-pour-cent s03e03 scene 21 (cues 1231-1241).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-21.py --out out/dix-pour-cent/s03e03/scene-21.json

ID = "dix-pour-cent-s03e03-scene-21"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 21
TITLE = "Soixante-dix films  (Seventy Films)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "theo"}
LABELS = {"lea": "Samy", "gerard": "Gérard"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 1231-1241. Reconciling on the street, Gérard Lanvin and Samy joke about their age gap "
               "and aches before Gérard commits to calling the director back to support Samy. Adapted for A1 French.")

INTRO = ("Relieved and smiling on the pavement, Gerard Lanvin and Samy bond over shared humor and the physical toll of cinema. "
         "While Samy prepares to return to his busy cafe shift, Gerard promises to immediately contact the director to champion his casting. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Je ne savais pas pour votre dos.",
  "I did not know about your back.",
  [(1231, "je savais pas que vous étiez fragiles du dos.")], "Apologized for physical strain"),
 ("gerard", "Après cinquante films, on a mal partout!",
  "After fifty films, we hurt everywhere!",
  [(1233, "Après 50 films, on est fragiles de partout, mon gars.")], "Joked about physical aches"),
 ("lea", "Vous avez vraiment fait cinquante films?",
  "You really made fifty films?",
  [(1234, "Vous avez fait 50 films.")], "Inquired about filmography"),
 ("gerard", "Non, en réalité, c'est soixante-dix films!",
  "No, in reality, it is seventy films!",
  [(1236, "70.")], "Corrected total movie count"),
 ("lea", "C'est une très belle carrière, Gérard.",
  "That is a very fine career, Gerard.",
  [(1237, "Elle est pas belle, l'histoire.")], "Praised long-standing career"),
 ("gerard", "C'est vrai, une histoire avec beaucoup de classe.",
  "It is true, a story with lots of class.",
  [(1238, "La classe.")], "Affirmed proud legacy"),
 ("lea", "Et moi, j'ai soixante-dix cafés à servir.",
  "And me, I have seventy coffees to serve.",
  [(1239, "Bon, moi, je vais aller servir à mes 70 cafés.")], "Compared films to coffees"),
 ("gerard", "Soixante et onze cafés, mon ami!",
  "Seventy-one coffees, my friend!",
  [(1240, "71.")], "Teased about coffee count"),
 ("lea", "Je dois retourner travailler au bar.",
  "I have to go back to work at the bar.",
  [(1239, "je vais aller servir")], "Announced return to shift"),
 ("gerard", "Attends, je vais tout arranger pour toi.",
  "Wait, I am going to sort everything out for you.",
  [(1241, "Et moi, je vais rappeler Emma.")], "Offered to fix casting"),
 ("lea", "Vous voulez parler à la réalisatrice?",
  "You want to speak to the director?",
  [(1241, "rappeler Emma.")], "Asked about director call"),
 ("gerard", "Je vais rappeler Emma immédiatement.",
  "I am going to call Emma back immediately.",
  [(1241, "je vais rappeler Emma.")], "Promised urgent phone call"),
 ("lea", "Merci Gérard, vous êtes un vrai grand!",
  "Thank you Gerard, you are a truly great person!",
  [(1238, "La classe.")], "Praised mentor generosity"),
 ("gerard", "Nous allons faire ce film ensemble.",
  "We are going to make this film together.",
  [(1241, "rappeler Emma")], "Promised future collaboration"),
]

OPENER = "Let's see how Gerard and Samy find humor and solidarity on the pavement."

WALK = [
 (0, None,
  "'I did not know about your back.' A polite acknowledgment of physical vulnerability. The formal 'you' pronoun sets a courteous, professional distance around 'knew'."),
 (1, None,
  "'After fifty films, we hurt everywhere!' The verb meaning 'has' pairs naturally with the noun for 'films' in everyday conversation."),
 (2, None,
  "'You really made fifty films?' Notice how 'have' leads directly into the noun meaning 'films'. Notice how 'have' leads directly into the noun meaning 'films'."),
 (3, None,
  "'No, in reality, it is seventy films!' A proud correction updating the film count. Notice how 'it is' leads directly into the noun meaning 'reality'."),
 (4, None,
  "'That is a very fine career, Gerard.' In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe. In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe."),
 (5, None,
  "'It is true, a story with lots of class.' A satisfied agreement reflecting on an honorable journey. The verb meaning 'it is' pairs naturally with the noun for 'story' in everyday conversation."),
 (6, None,
  "'And me, I have seventy coffees to serve.' A witty parallel linking cinema to catering duties. Notice how 'I have' leads directly into the noun meaning 'coffees'."),
 (7, None,
  "'Seventy-one coffees, my friend!' A playful tease adding another coffee to the tally. The key noun here means 'coffees', anchored by its matching French article."),
 (8, None,
  "'I have to go back to work at the bar.' Notice how 'must' leads directly into the noun meaning 'bar'. Notice how 'must' leads directly into the noun meaning 'bar'."),
 (9, None,
  "'Wait, I am going to sort everything out for you.' Gerard uses the casual singular 'you' with 'wait', showing close familiarity. Gerard uses the casual singular 'you' with 'wait', showing close familiarity."),
 (10, None,
  "'You want to speak to the director?' The verb meaning 'want' pairs naturally with the noun for 'director' in everyday conversation."),
 (11, None,
  "'I am going to call Emma back immediately.' A decisive commitment to contact the filmmaker. French forms the near future by pairing the present tense of 'to go' directly with 'to call back'."),
 (12, None,
  "'Thank you Gerard, you are a truly great person!' The formal 'you' pronoun sets a courteous, professional distance around 'great person'."),
 (13, None,
  "'We are going to make this film together.' An inspiring pledge promising cinematic collaboration. The verb meaning 'are going to' pairs naturally with the noun for 'film' in everyday conversation."),
]

TRANSITION = "Now let's listen to Samy and Gerard again at full speed."

OUTRO = ("Sharing laughter and mutual respect on the Parisian street, Gerard Lanvin turns Samy's dream into reality by advocating for his talent. "
         "Behind the glamour of cinema, authentic mentorship and generosity prove to be the true mark of great artistry.")

CLOSING = ("gerard", "À très vite sur le tournage, Samy.")
