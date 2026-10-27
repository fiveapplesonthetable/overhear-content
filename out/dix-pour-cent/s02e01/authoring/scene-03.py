# Authoring module for dix-pour-cent s02e01 scene 03 (cues 64-91).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-03.py --out out/dix-pour-cent/s02e01/scene-03.json

ID = "dix-pour-cent-s02e01-scene-03"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = "Matin agité à l'agence ASK  (Hectic Morning at the ASK Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "herve": "marcel"}
LABELS = {"lea": "Noémie", "gabriel": "Gabriel", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 64-91. The agents and assistants arrive at work and discover the tabloid magazine "
               "revealing Virginie's infidelity, creating immediate panic. "
               "Adapted for A1 French.")

INTRO = ("The next morning at the ASK agency reception desk, Noémie is busy fielding phone calls from fans. "
         "Gabriel arrives looking for Camille while Hervé brings the morning mail. "
         "Suddenly a shocking magazine cover catches their attention. Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Camille est là? Où est-elle?",
  "Is Camille here? Where is she?",
  [(72, "Camille est là ?"), (73, "Mais elle est où")], ""),
 ("lea", "Camille n'est pas encore arrivée.",
  "Camille has not arrived yet.",
  [(72, "Pas encore.")], "Expanded short answer for clarity"),
 ("gabriel", "On se retrouve au café comme la première fois.",
  "Let's meet at the café like the first time.",
  [(74, "On se retrouve au Café"), (75, "comme la première fois.")], ""),
 ("gabriel", "Attends, tu ne t'appelles pas Laurence?",
  "Wait, isn't your name Laurence?",
  [(77, "Tu ne t'appelles pas Laurence ?")], "Added greeting verb 'attends'"),
 ("lea", "Non, Laura Smet n'habite pas ici.",
  "No, Laura Smet does not live here.",
  [(78, "Non, Laura Smet n'habite pas ici.")], ""),
 ("lea", "Vous pouvez envoyer du courrier pour elle.",
  "You can send mail for her.",
  [(79, "Vous pouvez envoyer du courrier ici")], "Adapted 'ici' to 'pour elle'"),
 ("herve", "Bonjour Noémie, le meilleur pour la fin!",
  "Hello Noémie, the best for last!",
  [(84, "Le meilleur pour la fin !")], "Added greeting"),
 ("herve", "Tu sens très bon aujourd'hui.",
  "You smell very good today.",
  [(85, "Tu sens bon !")], "Added intensifier 'très' and adverb 'aujourd'hui'"),
 ("lea", "C'est le parfum de Léa Seydoux.",
  "It is Léa Seydoux's perfume.",
  [(86, "C'est le parfum de Léa Seydoux.")], ""),
 ("herve", "Tu sens comme une vraie star!",
  "You smell like a real star!",
  [(87, "Tu sens la star !")], "Expanded idiom for A1 learners"),
 ("gabriel", "Noémie, j'ai des choses pour toi.",
  "Noémie, I have things for you.",
  [(88, "J'ai des choses pour toi.")], ""),
 ("lea", "Regardez la couverture de ce magazine!",
  "Look at the cover of this magazine!",
  [(90, "LA NOUVELLE PASSION DE VIRGINIE EFIRA")], "Introduced tabloid visual"),
 ("herve", "La nouvelle passion de Virginie Efira?",
  "Virginie Efira's new passion?",
  [(90, "LA NOUVELLE PASSION DE VIRGINIE EFIRA")], ""),
 ("gabriel", "Merde! C'est une catastrophe pour l'agence.",
  "Damn! It is a disaster for the agency.",
  [(91, "Merde !")], "Added contextual reaction"),
]

OPENER = "Let's examine how normal agency banter suddenly turns into an emergency."

WALK = [
 (0, None,
  "'Is Camille here? Where is she?' Gabriel asks two quick questions about his missing assistant."),
 (1, None,
  "'Camille has not arrived yet.' A negative compound past construction with a temporal adverb."),
 (2, None,
  "'Let's meet at the cafe like the first time.' A pronominal reciprocal verb in the present tense with a comparative phrase."),
 (3, None,
  "'Wait, isn't your name Laurence?' An imperative followed by a pronominal verb in a negative question."),
 (4, None,
  "'No, Laura Smet does not live here.' A negative present tense statement clarifying agency reality to a fan."),
 (5, None,
  "'You can send mail for her.' A modal verb expressing permission or possibility followed by an infinitive."),
 (6, None,
  "'Hello Noemie, the best for last!' A cheerful workplace greeting followed by a classic proverb."),
 (7, None,
  "'You smell very good today.' The sensory verb meaning to smell followed by a quality adverb."),
 (8, None,
  "'It is Lea Seydoux's perfume.' A demonstrative presentative introducing a celebrity possession."),
 (9, None,
  "'You smell like a real star!' A comparative preposition followed by a feminine adjective and noun."),
 (10, None,
  "'Noemie, I have things for you.' A straightforward sentence with the verb to have and an indirect preposition."),
 (11, None,
  "'Look at the cover of this magazine!' An imperative plural addressing colleagues with a demonstrative adjective."),
 (12, None,
  "'Virginie Efira's new passion?' A sensational headline repeated as an incredulous question."),
 (13, None,
  "'Damn! It is a disaster for the agency.' An exclamation of frustration followed by an evaluation noun."),
]

TRANSITION = "Now let's listen to the whole morning scene at ASK again without pausing."

OUTRO = ("The tabloid magazine is on newsstands everywhere, threatening Virginie and Ramzy's film release. "
         "The agents must quickly find a way to manage the fallout.")

CLOSING = ("gabriel", "C'est une catastrophe.")
