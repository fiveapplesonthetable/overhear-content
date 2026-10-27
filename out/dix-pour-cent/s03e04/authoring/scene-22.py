# Authoring module for dix-pour-cent s03e04 scene 22 (cues 1187-1213).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-22.py --out out/dix-pour-cent/s03e04/scene-22.json

ID = "dix-pour-cent-s03e04-scene-22"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 22
TITLE = "Le talent de Samy  (Samy's Talent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 1187-1213. Camille and Herve watch Samy's homemade audition tape at ASK. "
               "Herve thinks he is terrible, but Camille sees raw potential and insists on representing him.")

INTRO = ("At the ASK agency, Camille and Herve review a homemade video sent by the aspiring actor Samy. "
         "Herve is completely unimpressed by his eccentric performance, but Camille passionately defends the young actor. "
         "Let's listen to their discussion in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("herve", "Ton instinct est à quel niveau?",
  "What level is your instinct at?",
  [(1187, "ton instinct")], "Inquiring about instinct"),
 ("lea", "Il a fait ça tout seul.",
  "He did that all by himself.",
  [(1190, "il a fait ça tout seul")], "Defending self-made tape"),
 ("herve", "Arrête, c'est vraiment une quiche.",
  "Stop, he is a total amateur.",
  [(1193, "c'est une quiche")], "Brutal assessment"),
 ("lea", "C'est novateur et très spécial.",
  "It is innovative and very special.",
  [(1195, "C'est très spécial")], "Praising originality"),
 ("lea", "De grands acteurs ont réussi.",
  "Great actors have succeeded.",
  [(1198, "réussir")], "Citing great examples"),
 ("lea", "Personne ne croyait en Belmondo.",
  "Nobody believed in Belmondo.",
  [(1200, "Belmondo")], "Mentioning Belmondo"),
 ("herve", "On ne représente pas ce mec.",
  "We are not representing this guy.",
  [(1203, "ce mec")], "Refusing to represent"),
 ("lea", "Moi, j'y crois vraiment.",
  "I truly believe in him.",
  [(1204, "Moi, j'y crois.")], "Declaring strong belief"),
 ("lea", "Il a un potentiel énorme.",
  "He has enormous potential.",
  [(1207, "Il a un potentiel énorme.")], "Emphasizing potential"),
 ("herve", "Tu parles pour nous deux?",
  "Are you speaking for both of us?",
  [(1209, "Tu parles pour nous")], "Questioning partnership"),
 ("lea", "Je serai son propre pygmalion.",
  "I will be his own Pygmalion.",
  [(1210, "je serai")], "Vowing to mentor"),
 ("lea", "Je peux en faire une star.",
  "I can make him a star.",
  [(1211, "je peux en faire une star.")], "Promising stardom"),
 ("lea", "Un jour, tu me remercieras.",
  "One day, you will thank me.",
  [(1212, "tu me remercieras.")], "Predicting gratitude"),
 ("lea", "La France entière me remerciera.",
  "All of France will thank me.",
  [(1213, "me remerciera")], "Grand conclusion"),
]

WALK = [
 (0, None,
  "'What level is your instinct at?' Herve asks Camille skeptically about her intuition. "
  "The noun 'instinct' refers to gut feeling."),
 (1, None,
  "'He did that all by himself.' Camille defends Samy's self-tape initiative. "
  "The phrase 'tout seul' means alone or on his own."),
 (2, None,
  "'Stop, he is a total amateur.' Herve dismisses the actor's audition video. "
  "The colloquial French slang 'une quiche' means someone terrible or incompetent at something."),
 (3, None,
  "'It is innovative and very special.' Camille praises the unusual performance style. "
  "The adjective 'novateur' describes pioneering artistic work."),
 (4, None,
  "'Great actors have succeeded.' Camille reminds him that unconventional actors often succeed. "
  "The past participle 'reussi' comes from reussir."),
 (5, None,
  "'Nobody believed in Belmondo.' Camille cites legendary French actor Jean-Paul Belmondo. "
  "The negative pronoun 'personne' means nobody."),
 (6, None,
  "'We are not representing this guy.' Herve refuses to sign the eccentric actor. "
  "The informal noun 'ce mec' means this guy."),
 (7, None,
  "'I truly believe in him.' Camille asserts her strong conviction. "
  "The pronoun 'y' refers back to believing in him."),
 (8, None,
  "'He has enormous potential.' Camille highlights his untapped acting talent. "
  "The adjective 'enorme' emphasizes great capability."),
 (9, None,
  "'Are you speaking for both of us?' Herve questions whether this serves their agency partnership. "
  "The preposition 'pour' expresses on behalf of."),
 (10, None,
  "'I will be his own Pygmalion.' Camille vows to mentor and train him into shape. "
  "The simple future 'serai' comes from etre."),
 (11, None,
  "'I can make him a star.' Camille declares her ambition with absolute confidence. "
  "The modal verb 'peux' expresses ability."),
 (12, None,
  "'One day, you will thank me.' Camille promises Herve he will appreciate her decision. "
  "The simple future 'remercieras' means will thank."),
 (13, None,
  "'All of France will thank me.' Camille concludes with dramatic enthusiasm. "
  "The feminine adjective 'entiere' means whole or entire."),
]

OUTRO = ("Camille's determination wins out over Herve's skepticism, securing Samy a spot with Camille Valentini. "
         "Her belief in unconventional talent shows her growing confidence as an agent. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Je peux en faire une star.")
