# Authoring module for dix-pour-cent s03e06 scene 10 (cues 490-518).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s03e06/scene-10.json

ID = "dix-pour-cent-s03e06-scene-10"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 10
TITLE = "Les cartons de Sophia  (Sophia's Boxes)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sophia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 490-518. Gabriel visits Sophia's apartment and finds her packing cardboard boxes "
               "to move back to Vitry, leading to a bitter clash over their derailed careers and personal regrets.")

INTRO = ("Gabriel arrives at Sophia Leprince's apartment intending to discuss agency business. "
         "Instead, he discovers her packing moving boxes to return to her parents' home after months without work, "
         "sparking an emotional confrontation between former partners. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("gabriel", "Salut Sophia, tu prépares tes cartons?",
  "Hi Sophia, are you packing your boxes?",
  [(494, "Tu déménages ?")], "Noticing moving boxes"),
 ("lea", "Je retourne vivre chez mes parents, Gabriel.",
  "I am returning to live with my parents, Gabriel.",
  [(497, "Je retourne à Vitry-sur-Seine, habiter chez mes parents.")], "Announcing departure"),
 ("gabriel", "Pourquoi tu ne m'as rien dit?",
  "Why didn't you tell me anything?",
  [(498, "T'aurais dû m'en parler")], "Expressing hurt surprise"),
 ("lea", "Parce que ton aide ne m'aide jamais.",
  "Because your help never helps me.",
  [(499, "Ben non, parce que quand tu m'aides, ça m'aide pas")], "Stating harsh truth"),
 ("gabriel", "Le flop du film n'est pas ma faute.",
  "The film's flop is not my fault.",
  [(500, "j'y suis pour rien si le film de Julien a pas marché")], "Defending himself"),
 ("lea", "Tu pensais à toi, pas à moi.",
  "You were thinking about yourself, not me.",
  [(504, "Oui, mais tu pensais à toi, pas à moi.")], "Accusing selfish motives"),
 ("gabriel", "Je voulais seulement protéger ta carrière d'actrice.",
  "I only wanted to protect your acting career.",
  [(503, "Mais j'ai pas arrêté de te le dire.")], "Explaining protective intentions"),
 ("lea", "Je n'ai pas travaillé depuis six mois.",
  "I haven't worked in six months.",
  [(505, "Moi, depuis, ça fait six mois que j'ai pas bossé")], "Lamenting long unemployment"),
 ("gabriel", "Tu crois que ma vie est facile?",
  "Do you think my life is easy?",
  [(509, "Ah ouais, moi, ça va, la vie, ouais.")], "Challenging her assumptions"),
 ("lea", "Toi, tu as toujours ton grand travail.",
  "You, you still have your great job.",
  [(508, "Alors que toi, ça va, la vie ?")], "Pointing to agency status"),
 ("gabriel", "J'ai perdu la femme de ma vie.",
  "I lost the woman of my life.",
  [(511, "J'ai perdu la meuf que j'aimais le plus au monde.")], "Confessing personal heartbreak"),
 ("gabriel", "Et je vais perdre mon agence ce soir.",
  "And I will lose my agency tonight.",
  [(513, "Je vais peut-être perdre mon agence aussi, tiens, ce soir.")], "Admitting impending ruin"),
 ("gabriel", "Bonne soirée, excuse-moi de t'avoir dérangée.",
  "Good evening, sorry to have bothered you.",
  [(515, "OK, excuse-moi de t'avoir dérangé, hein.")], "Turning to leave"),
 ("lea", "Attends, Gabriel, qu'est-ce qui se passe chez ASK?",
  "Wait, Gabriel, what is happening at ASK?",
  [(518, "Qu'est-ce qui se passe chez SK ?")], "Calling him back in concern"),
]

WALK = [
 (0, None,
  "'Hi Sophia, are you packing your boxes?' Gabriel asks about the packed apartment. "
  "The noun 'carton' commonly refers to a cardboard moving box."),
 (1, None,
  "'I am returning to live with my parents, Gabriel.' Sophia reveals her forced relocation. "
  "The preposition 'chez' precedes the noun designating someone's home."),
 (2, None,
  "'Why didn't you tell me anything?' Gabriel feels hurt that she kept it secret. "
  "The negative adverb 'rien' expresses complete negation of speech."),
 (3, None,
  "'Because your help never helps me.' Sophia criticizes his well-meaning intervention. "
  "The adverb 'jamais' indicates habitual lack of success."),
 (4, None,
  "'The film's flop is not my fault.' Gabriel disclaims responsibility for the failure. "
  "The noun 'faute' denotes personal blame or fault."),
 (5, None,
  "'You were thinking about yourself, not me.' Sophia reproaches his agency priorities. "
  "The imperfect 'pensais' describes an ongoing selfish mindset."),
 (6, None,
  "'I only wanted to protect your acting career.' Gabriel asserts his honest goal. "
  "The adverb 'seulement' restricts his intent to protecting her."),
 (7, None,
  "'I haven't worked in six months.' Sophia explains her financial desperation. "
  "The preposition 'depuis' indicates a duration extending to the present."),
 (8, None,
  "'Do you think my life is easy?' Gabriel bristles at her sarcastic tone. "
  "The adjective 'facile' describes a life without hardship."),
 (9, None,
  "'You, you still have your great job.' Sophia assumes Gabriel remains secure. "
  "The adverb 'toujours' expresses continuity of employment."),
 (10, None,
  "'I lost the woman of my life.' Gabriel expresses his deep romantic regret. "
  "The passe compose 'ai perdu' denotes irreparable loss."),
 (11, None,
  "'And I will lose my agency tonight.' Gabriel reveals that ASK is on the brink of collapse. "
  "The near future 'vais perdre' warns of imminent disaster."),
 (12, None,
  "'Good evening, sorry to have bothered you.' Gabriel steps away feeling defeated. "
  "The polite expression 'excuse-moi' softens his sudden departure."),
 (13, None,
  "'Wait, Gabriel, what is happening at ASK?' Sophia drops her bitterness out of genuine concern. "
  "The imperative 'attends' urges him to stop and explain."),
]

OUTRO = ("Sophia and Gabriel lay bare their mutual wounds, discovering that both are on the brink of losing everything. "
         "As Gabriel reveals the catastrophe at ASK, Sophia realizes how desperately he needs an ally. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Attends, Gabriel, qu'est-ce qui se passe chez ASK?")
