# Authoring module for dix-pour-cent-s01e01-scene-13.
ID = 'dix-pour-cent-s01e01-scene-13'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = 'Trop vieille pour le rôle  (Too Old for the Part)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'cecile': 'Cécile'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "Nobody told Camille it was a secret. Now the new assistant finds herself next to Cécile at the washroom mirror, and she's sure Cécile already knows. She means to be kind. You'll hear it in French first; just follow the feeling of it, the words will come later."
OPENER = "Let's go back through it. Camille opens with a friendly little question, the kind you ask a stranger at a sink."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That was a painful one, but you followed it. Listen out for the polite 'you' and those feminine endings when you watch. See you next time!"
CLOSING = ('camille', 'Bonne journée!')
STORY = [
    ('camille', 'Journée difficile?', 'Tough day?', [(423, 'Journée difficile')], ''),
    ('cecile', 'Pas difficile. Juste très particulière.', 'Not tough. Just very strange.', [(424, 'Pas difficile'), (424, 'très particulière')], ''),
    ('camille', 'Moi aussi.', 'Me too.', [(425, 'Moi aussi')], ''),
    ('cecile', 'Ce film de Tarantino...', 'This Tarantino film...', [(425, 'Ce film de Tarantino')], ''),
    ('camille', "Je comprends. C'est un coup dur.", "I understand. It's a real blow.", [(426, 'Je comprends')], ''),
    ('cecile', "C'est-à-dire?", 'Meaning?', [(428, "C'est-à-dire")], ''),
    ('camille', 'Vous ne perdez pas grand-chose.', 'You', [(429, 'vous ne perdez pas grand-chose')], ''),
    ('cecile', 'De quoi vous parlez?', 'What are you talking about?', [], ''),
    ('camille', 'De votre âge! Vous êtes belle naturellement.', "Your age! You're naturally beautiful.", [(430, 'De votre âge'), (431, 'Vous êtes belle naturellement')], ''),
    ('cecile', 'Merci. Continuez!', 'Thank you. Go on!', [(432, 'Merci'), (433, 'Continuez')], ''),
    ('camille', 'Les actrices américaines ont toutes le même lifting.', 'American actresses all have the same facelift.', [(434, 'Les actrices américaines ont toutes le même lifting')], ''),
    ('camille', 'Ils disent que vous êtes trop vieille pour le rôle.', 'They say you', [(437, 'trop vieille pour le rôle')], ''),
    ('camille', "Mais c'est tellement stupide!", 'But it', [(438, "Mais c'est tellement stupide")], ''),
    ('cecile', 'Ah. Trop vieille.', 'Ah. Too old.', [], ''),
    ('camille', "J'espère être comme vous à votre âge.", 'I hope I', [(439, 'à votre âge')], ''),
    ('cecile', 'Merci. Au revoir.', 'Thank you. Goodbye.', [(440, 'Merci'), (441, 'Au revoir')], ''),
    ('camille', 'Au revoir!', 'Goodbye!', [(441, 'Au revoir')], ''),
]
WALK = [
    (0, None, "'Tough day?' Just two words, no verb: the noun for 'day' and the adjective for 'difficult'. Cécile answers politely."),
    (1, None, "'Not tough. Just very strange.' Her word means 'peculiar' or 'unusual', and it has a feminine ending because it describes the day, which is a feminine word in French. Camille sympathises."),
    (2, None, "'Me too.' A very handy pair of words. Then Cécile names what's on her mind."),
    (3, None, "'This Tarantino film...' She stops there. She is thinking of the part she hopes to get. Camille thinks she's talking about losing it."),
    (4, 'Je comprends.', "'I understand.' A useful verb, and a dangerous one here, because Camille doesn't understand at all."),
    (4, "C'est un coup dur.", "'It's a real blow.' Literally 'a hard hit': bad news that knocks you over. Cécile senses something."),
    (5, None, "'Meaning?' Literally 'that is to say?'. It's how you ask someone to explain what they just said."),
    (6, None, "'You're not missing much.' Camille uses the polite 'you' with the star, and the full negative, one little word before the verb and one after, here a word meaning 'big thing'. So: you are not losing a big thing."),
    (7, None, "'What are you talking about?' Word for word: of what you speak? Cécile keeps her voice calm."),
    (8, 'De votre âge!', "'Your age!' The word for 'your' here is the polite one, matching the polite 'you'."),
    (8, 'Vous êtes belle naturellement.', "'You're naturally beautiful.' The word for 'beautiful' is in its feminine form; for a man it would be completely different. Cécile says thank you, and wants to hear more."),
    (9, None, "'Thank you. Go on!' A polite command. And Camille happily goes on."),
    (10, None, "'American actresses all have the same facelift.' Notice the endings: the actresses are feminine and plural, so 'American' and 'all' take feminine plural endings too."),
    (11, None, "'They say you're too old for the part.' Here it is, out loud. The word for 'old' is feminine, because Cécile is a woman; the small word in front means 'too'. This is the secret Gabriel has been hiding all day."),
    (12, None, "'But it's so stupid!' Camille is truly on Cécile's side; she just has no idea what she has done."),
    (13, None, "'Ah. Too old.' Two quiet words. Cécile repeats the news to herself, and keeps smiling."),
    (14, None, "'I hope I'm like you at your age.' A compliment, and also a small knife."),
    (15, None, "'Thank you. Goodbye.' Cécile is perfectly polite, and she leaves."),
    (16, None, "'Goodbye!' Camille waves her off, cheerful, with no idea of the storm she has just started. Okay, let's hear the conversation one more time."),
]
