# Authoring module for dix-pour-cent s03e05 scene 29 (cues 1095-1144).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-29.py --out overhear-content/out/dix-pour-cent/s03e05/scene-29.json

ID = "dix-pour-cent-s03e05-scene-29"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 29
TITLE = "L'erreur fatale de Gabriel  (Gabriel's Fatal Mistake)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 1095-1144. Gabriel realizes with horror that he left the voicemail on Hicham's phone. "
               "An explosive confrontation breaks out before Hicham storms out, ceding the agency to Mathias.")

INTRO = ("In the open office area of ASK, Gabriel checks his mobile phone and turns pale with terror. "
         "He realizes he left his secret voice message on Hicham's voicemail instead of their lawyer's, sparking an explosive agency confrontation. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("gabriel", "Je n'aime pas ce ton.",
  "I do not like that tone.",
  [(1095, "pas du tout ce ton")], "Reacting to voice tone"),
 ("gabriel", "C'est une catastrophe totale!",
  "It is a complete catastrophe!",
  [(1100, "merde absolue")], "Panicking at blunder"),
 ("lea", "Gabriel, qu'est-ce qu'il y a?",
  "Gabriel, what is the matter?",
  [(1101, "Qu'est-ce qu'il y a")], "Asking with concern"),
 ("gabriel", "J'ai laissé le message à Hicham!",
  "I left the message for Hicham!",
  [(1102, "laissé le message")], "Confessing fatal error"),
 ("gabriel", "Son numéro était juste en dessous.",
  "His number was right underneath.",
  [(1104, "juste en dessous")], "Explaining contact mishap"),
 ("lea", "Non, c'est absolument impossible!",
  "No, that is absolutely impossible!",
  [(1105, "Oh putain")], "Reacting in disbelief"),
 ("hicham", "Vous êtes des traîtres lâches!",
  "You are cowardly traitors!",
  [(1112, "lâches et de traîtres")], "Confronting defectors"),
 ("gabriel", "Nous avons voulu tout arrêter.",
  "We wanted to stop everything.",
  [(1108, "tout arrêter")], "Attempting to explain"),
 ("lea", "C'est très compliqué avec toi!",
  "It is very complicated with you!",
  [(1119, "compliqué de bosser avec toi")], "Defending frustrations"),
 ("lea", "Tu nous étouffes souvent, Hicham.",
  "You often suffocate us, Hicham.",
  [(1126, "un peu étouffant")], "Calling out oppression"),
 ("hicham", "Je donne tout à Mathias.",
  "I am handing everything over to Mathias.",
  [(1129, "Mathias")], "Announcing transfer"),
 ("hicham", "Je n'ai plus rien ici.",
  "I have nothing left here anymore.",
  [(1133, "plus rien à faire ici")], "Declaring departure"),
 ("lea", "Pourquoi réagis-tu comme ça?",
  "Why are you reacting like that?",
  [(1135, "Pourquoi tu le prends comme ça")], "Questioning reaction"),
 ("lea", "La fuite vient de nous.",
  "The leak comes from us.",
  [(1144, "La fuite")], "Realizing internal betrayal"),
]

WALK = [
 (0, None,
  "'I do not like that tone.' Gabriel hears Hicham's menacing voice on the line and senses disaster. "
  "The noun 'ton' refers to tone of voice."),
 (1, None,
  "'It is a complete catastrophe!' Gabriel panics as the reality of his blunder sinks in. "
  "The feminine adjective 'totale' intensifies the noun catastrophe."),
 (2, None,
  "'Gabriel, what is the matter?' Andrea asks him with rising concern. "
  "The interrogative phrase 'qu'est-ce qu'il y a' asks what is wrong."),
 (3, None,
  "'I left the message for Hicham!' Gabriel confesses his catastrophic dialing error. "
  "The past participle 'laisse' comes from laisser."),
 (4, None,
  "'His number was right underneath.' Gabriel explains the phone contact list accident. "
  "The prepositional locution 'en dessous' means underneath or below."),
 (5, None,
  "'No, that is absolutely impossible!' Andrea reacts with horror at the disclosure. "
  "The negative adverb 'absolument' intensifies impossible."),
 (6, None,
  "'You are cowardly traitors!' Hicham confronts them with searing anger. "
  "The plural noun 'traitres' designates people who betray trust."),
 (7, None,
  "'We wanted to stop everything.' Gabriel attempts to explain that they reconsidered leaving. "
  "The infinitive 'arreter' means to cease or halt."),
 (8, None,
  "'It is very complicated with you!' Andrea fires back about Hicham's difficult management style. "
  "The adjective 'complique' denotes difficulty."),
 (9, None,
  "'You often suffocate us, Hicham.' Andrea explains how his oppressive control alienated the team. "
  "The verb 'etouffer' means to suffocate or stifle."),
 (10, None,
  "'I am handing everything over to Mathias.' Hicham announces he is selling out to Mathias to punish them. "
  "The proper noun 'Mathias' names the senior partner."),
 (11, None,
  "'I have nothing left here anymore.' Hicham declares his departure from ASK. "
  "The negative expression 'ne plus rien' means nothing anymore."),
 (12, None,
  "'Why are you reacting like that?' Andrea pleads as Hicham walks away. "
  "The adverb 'pourquoi' opens the question."),
 (13, None,
  "'The leak comes from us.' Andrea realizes that the internal leak came from within their own walls. "
  "The noun 'fuite' denotes an information leak."),
]

OUTRO = ("Hicham storms out of ASK in fury, leaving Andrea and Gabriel facing the wreckage of their botched scheme. "
         "By handing control over to Mathias, Hicham seals the dramatic transformation of the agency. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "La fuite vient de nous.")
