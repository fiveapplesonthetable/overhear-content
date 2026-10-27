# Authoring module for dix-pour-cent s01e01 scene 13 (cues 422-441).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e01/authoring/scene-13.py --out out/dix-pour-cent/s01e01/scene-13.json

ID = "dix-pour-cent-s01e01-scene-13"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = "Trop vieille pour le rôle  (Too Old for the Part)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "cecile": "emilie"}
LABELS = {"lea": "Camille", "cecile": "Cécile"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("A few minutes later, still at the agency. Cécile came looking for Gabriel, and he ran off behind a pretend "
         "urgent phone call, so she still knows nothing. "
         "But Camille, on her tour, heard the gossip: the star was turned down for the Tarantino film because of her age. "
         "Nobody told Camille it was a secret. Now the new assistant finds herself next to Cécile at the washroom mirror, "
         "and she's sure Cécile already knows. She means to be kind. "
         "You'll hear it in French first; just follow the feeling of it, the words will come later.")

STORY = [
 ("lea", "Journée difficile?", "Tough day?",
  [(423, "Journée difficile")], ""),
 ("cecile", "Pas difficile. Juste très particulière.", "Not tough. Just very strange.",
  [(424, "Pas difficile"), (424, "très particulière")], ""),
 ("lea", "Moi aussi.", "Me too.",
  [(425, "Moi aussi")], ""),
 ("cecile", "Ce film de Tarantino...", "This Tarantino film...",
  [(425, "Ce film de Tarantino")], "she doesn't finish the sentence"),
 ("lea", "Je comprends. C'est un coup dur.", "I understand. It's a real blow.",
  [(426, "Je comprends")], "'coup de massue' (cue 427) simplified to 'coup dur'"),
 ("cecile", "C'est-à-dire?", "Meaning?",
  [(428, "C'est-à-dire")], ""),
 ("lea", "Vous ne perdez pas grand-chose.", "You're not missing much.",
  [(429, "vous ne perdez pas grand-chose")], ""),
 ("cecile", "De quoi vous parlez?", "What are you talking about?",
  [], "retells 'À faire de quoi?' (cue 430)"),
 ("lea", "De votre âge! Vous êtes belle naturellement.", "Your age! You're naturally beautiful.",
  [(430, "De votre âge"), (431, "Vous êtes belle naturellement")], ""),
 ("cecile", "Merci. Continuez!", "Thank you. Go on!",
  [(432, "Merci"), (433, "Continuez")], "'je suis tout ouïe' left out"),
 ("lea", "Les actrices américaines ont toutes le même lifting.", "American actresses all have the same facelift.",
  [(434, "Les actrices américaines ont toutes le même lifting")], ""),
 ("lea", "Ils disent que vous êtes trop vieille pour le rôle.", "They say you're too old for the part.",
  [(437, "trop vieille pour le rôle")], "'ils vous ont dit que vous étiez' simplified to the present"),
 ("lea", "Mais c'est tellement stupide!", "But it's so stupid!",
  [(438, "Mais c'est tellement stupide")], ""),
 ("cecile", "Ah. Trop vieille.", "Ah. Too old.", [], "new: Cécile takes in the news, hiding it"),
 ("lea", "J'espère être comme vous à votre âge.", "I hope I'm like you at your age.",
  [(439, "à votre âge")], "'vous ressembler' simplified to 'être comme vous'"),
 ("cecile", "Merci. Au revoir.", "Thank you. Goodbye.",
  [(440, "Merci"), (441, "Au revoir")], ""),
 ("lea", "Au revoir!", "Goodbye!",
  [(441, "Au revoir")], ""),
]

OPENER = ("Let's go back through it. Camille opens with a friendly little question, "
          "the kind you ask a stranger at a sink.")

WALK = [
 (0, None,
  "'Tough day?' Just two words, no verb: the noun for 'day' and the adjective for 'difficult'. Cécile answers politely."),
 (1, None,
  "'Not tough. Just very strange.' Her word means 'peculiar' or 'unusual', and it has a feminine ending because it describes the day, "
  "which is a feminine word in French. Camille sympathises."),
 (2, None,
  "'Me too.' A very handy pair of words. Then Cécile names what's on her mind."),
 (3, None,
  "'This Tarantino film...' She stops there. She is thinking of the part she hopes to get. Camille thinks she's talking about losing it."),
 (4, "Je comprends.",
  "'I understand.' A useful verb, and a dangerous one here, because Camille doesn't understand at all."),
 (4, "C'est un coup dur.",
  "'It's a real blow.' Literally 'a hard hit': bad news that knocks you over. Cécile senses something."),
 (5, None,
  "'Meaning?' Literally 'that is to say?'. It's how you ask someone to explain what they just said."),
 (6, None,
  "'You're not missing much.' Camille uses the polite 'you' with the star, and the full negative, one little word before the verb "
  "and one after, here a word meaning 'big thing'. So: you are not losing a big thing."),
 (7, None,
  "'What are you talking about?' Word for word: of what you speak? Cécile keeps her voice calm."),
 (8, "De votre âge!",
  "'Your age!' The word for 'your' here is the polite one, matching the polite 'you'."),
 (8, "Vous êtes belle naturellement.",
  "'You're naturally beautiful.' The word for 'beautiful' is in its feminine form; for a man it would be completely different. "
  "Cécile says thank you, and wants to hear more."),
 (9, None,
  "'Thank you. Go on!' A polite command. And Camille happily goes on."),
 (10, None,
  "'American actresses all have the same facelift.' Notice the endings: the actresses are feminine and plural, "
  "so 'American' and 'all' take feminine plural endings too."),
 (11, None,
  "'They say you're too old for the part.' Here it is, out loud. The word for 'old' is feminine, because Cécile is a woman; "
  "the small word in front means 'too'. This is the secret Gabriel has been hiding all day."),
 (12, None,
  "'But it's so stupid!' Camille is truly on Cécile's side; she just has no idea what she has done."),
 (13, None,
  "'Ah. Too old.' Two quiet words. Cécile repeats the news to herself, and keeps smiling."),
 (14, None,
  "'I hope I'm like you at your age.' A compliment, and also a small knife. It's the verb 'to hope' followed by 'to be'."),
 (15, None,
  "'Thank you. Goodbye.' Cécile is perfectly polite, and she leaves."),
 (16, None,
  "'Goodbye!' Camille waves her off, cheerful, with no idea of the storm she has just started."),
]

TRANSITION = "Okay, let's hear the conversation one more time."

OUTRO = ("That was a painful one, but you followed it. Listen out for the polite 'you' and those feminine endings when you watch, "
         "and I'll see you next time.")
CLOSING = ("lea", "Bonne journée!")
