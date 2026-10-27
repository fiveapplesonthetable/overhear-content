# Authoring module for dix-pour-cent s01e05 scene 07 (cues 116-138).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-07.py --out out/dix-pour-cent/s01e05/scene-07.json

ID = "dix-pour-cent-s01e05-scene-07"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 7
TITLE = "Comme un aimant  (Like a Magnet)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "joey": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "joey": "JoeyStarr", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 116-138. Inside JoeyStarr's trailer on the film set, JoeyStarr complains to Gabriel about "
               "Julie Gayet, while Gabriel is distracted by texts from Sofia. Coarse slang in cues 122, 130, 132, "
               "and 135-136 is softened or trimmed for A1.")

INTRO = ("While Andrea calms Julie Gayet down in her trailer by promising the costume film could win her an award, "
         "Gabriel follows JoeyStarr into his trailer. JoeyStarr is furious about how Julie treats him on set, "
         "but Gabriel cannot stop looking at his phone. "
         "Listen to the French first, without worrying about catching every word.")

STORY = [
 ("joey", "Dis-le si je t'ennuie.",
  "Say it if I'm boring you.",
  [(116, "Dis-le si je t'ennuie")], ""),
 ("gabriel", "Non, excuse-moi! Regarde, j'écoute. Vas-y, je suis tout à toi.",
  "No, excuse me! Look, I'm listening. Go ahead, I'm all yours.",
  [(117, "Non, excuse-moi"), (118, "regarde"), (119, "J'écoute. Vas-y, je suis tout à toi")],
  "combined and trimmed for A1"),
 ("joey", "Je n'en ai plus envie maintenant.",
  "I don't feel like it anymore now.",
  [(120, "ai plus envie maintenant")],
  "spoken 'J'en ai' restored to 'Je n'en ai' for A1"),
 ("gabriel", "Allez, j'écoute! Et alors?",
  "Come on, I'm listening! And then?",
  [(120, "Allez, j'écoute"), (121, "Et alors")], ""),
 ("joey", "Je finis par passer pour un idiot! Tu sais ce qu'elle a fait?",
  "I end up looking like an idiot! Do you know what she did?",
  [(122, "Je finis par passer pour un"), (123, "Tu sais ce qu'elle a fait")],
  "'grand con' softened to 'idiot' for A1"),
 ("gabriel", "Non.",
  "No.",
  [(123, "Non")], ""),
 ("joey", "Elle n'avait pas son script avec elle.",
  "She didn't have her script with her.",
  [(124, "Elle n'avait pas son script avec elle")], ""),
 ("joey", "Alors moi, sympa, je lui donne le mien.",
  "So me, being nice, I give her mine.",
  [(125, "Alors moi, sympa, je lui donne le mien")], ""),
 ("joey", "Elle le prend comme un torchon sale! C'est agaçant.",
  "She takes it like a dirty rag! It's annoying.",
  [(126, "Elle le prend"), (126, "comme un torchon sale"), (127, "C'est agaçant")],
  "'du bout des doigts' omitted for A1"),
 ("gabriel", "Non, ça va.",
  "No, it's fine.",
  [(127, "Non, ça va")], ""),
 ("joey", "Réponds!",
  "Answer it!",
  [(128, "Réponds")], ""),
 ("gabriel", "D'accord. J'ai rencontré cette fille.",
  "Okay. I met this girl.",
  [(129, "D'accord"), (130, "j'ai rencontré cette")],
  "'nana' adapted to 'fille' for A1"),
 ("gabriel", "Ce n'est pas mon genre. Elle est blonde, elle est normale!",
  "She's not my type. She's blonde, she's normal!",
  [(131, "pas mon genre"), (132, "elle est blonde"), (132, "elle est normale")],
  "spoken 'C'est pas' restored to 'Ce n'est pas' and 'elle se drogue pas' omitted for A1"),
 ("gabriel", "Mais je suis attiré par elle comme un aimant.",
  "But I'm drawn to her like a magnet.",
  [(133, "Mais je suis attiré par elle comme un aimant")], ""),
 ("gabriel", "Tu vois? C'est très puissant.",
  "You see? It's very powerful.",
  [(134, "Tu vois"), (134, "puissant")],
  "'super' adapted to 'très' and cues 135-136 omitted for A1"),
 ("joey", "Mon inconscient et celui de Julie Gayet se heurtent de partout.",
  "My subconscious and Julie Gayet's clash everywhere.",
  [(138, "Mon inconscient et celui de Julie Gayet se heurtent de partout")], ""),
]

OPENER = "Let's walk through the scene line by line. JoeyStarr notices that Gabriel is staring at his phone instead of listening."

WALK = [
 (0, None,
  "'Say it if I'm boring you.' In an affirmative command, the object pronoun 'it' attaches after the verb with a hyphen."),
 (1, None,
  "'No, excuse me! Look, I'm listening. Go ahead, I'm all yours.' Gabriel puts his phone down on the table to prove he is paying attention."),
 (2, None,
  "'I don't feel like it anymore now.' The expression 'to have desire of it' means 'to feel like it', and 'no more' wraps around the verb."),
 (3, None,
  "'Come on, I'm listening! And then?' Gabriel urges his client to continue his story."),
 (4, None,
  "'I end up looking like an idiot! Do you know what she did?' The phrase 'to finish by passing for' means 'to end up looking like'."),
 (5, None,
  "'No.' Gabriel waits to hear Julie's latest offense on set."),
 (6, None,
  "'She didn't have her script with her.' The imperfect tense of 'to have' describes the background situation during rehearsal."),
 (7, None,
  "'So me, being nice, I give her mine.' The possessive pronoun 'the mine' stands in for 'my script' without repeating the noun."),
 (8, None,
  "'She takes it like a dirty rag! It's annoying.' In French, the adjective 'dirty' comes after the noun 'rag'."),
 (9, None,
  "'No, it's fine.' Gabriel's phone buzzes again on the table, and he tries to ignore it."),
 (10, None,
  "'Answer it!' JoeyStarr tells Gabriel to just read his message."),
 (11, None,
  "'Okay. I met this girl.' Instead of answering the message, Gabriel confesses why he has been so distracted: he cannot stop thinking about Anna, the blonde woman he met at the cinema."),
 (12, None,
  "'She's not my type. She's blonde, she's normal!' Literally 'It is not my type' — the word for 'genre' or 'sort' also means someone's romantic type."),
 (13, None,
  "'But I'm drawn to her like a magnet.' The passive participle 'attracted' is followed by the preposition 'by'."),
 (14, None,
  "'You see? It's very powerful.' Gabriel describes the sudden attraction he feels for a woman who is the complete opposite of his usual girlfriends."),
 (15, None,
  "'My subconscious and Julie Gayet's clash everywhere.' Hearing Gabriel talk about attraction between opposites makes JoeyStarr think about his own explosive tension with Julie Gayet."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = ("Gabriel's confession about being drawn to his opposite gives JoeyStarr food for thought about Julie Gayet. "
         "Next, out at the catering tent in the courtyard, Sofia spots Gabriel and proudly introduces him as her agent. See you there.")
CLOSING = ("gabriel", "Je suis attiré par elle comme un aimant.")
