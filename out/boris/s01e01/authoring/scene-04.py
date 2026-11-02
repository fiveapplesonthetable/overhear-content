# Authoring module for boris-s01e01-scene-04.
ID = 'boris-s01e01-scene-04'
SHOW = 'boris'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Ti chiamerai Seppia  (You Will Be Called Seppia)'
LEVEL = 'A1 — beginner'
PAIR = 'it-en'
LABELS = {'stanis': 'Stanis', 'arianna': 'Arianna', 'alessandro': 'Alessandro'}
SOURCE_NAME = 'Boris S01E01'
SOURCE_FILE = 'sources/boris/s01/e01.it.srt'
INTRO = (
    'As Rene gets the crew ready for the first scene of the day, star actor Stanis La Rochelle strolls onto the Studio 2 set fresh from a tennis match. '
    'After Arianna reminds Stanis about his contract, he spots Alessandro and decides the intern needs a brand-new name. '
    'Listen to the Italian scene first; you do not need to catch every word.'
)
OPENER = (
    "Let's go through Stanis's grand entrance, his tennis excuse, and Alessandro's new nickname."
)
TRANSITION = 'Now hear the whole scene again, from Stanis arriving on set to the nickname Seppia.'
OUTRO = (
    'You have heard "mi sento a casa" for feeling at home, "sto scherzando" for "just kidding", '
    'and how Stanis christens Alessandro "Seppia". See you next time.'
)
CLOSING = ('stanis', 'Arrivederci!')
STORY = [
    ('stanis', 'Che straordinario odore di set! Mi sento a casa.', 'What an extraordinary studio smell! I feel at home.', [(130, 'che straordinario odore di set mi sento a casa')], ''),
    ('stanis', 'Appena posso, mollo questa serie.', 'As soon as I can, I am quitting this series.', [(136, 'Appena posso'), (136, 'mollo questa serie')], ''),
    ('stanis', 'Sto scherzando! Sto in gran forma.', 'I am kidding! I am in top form.', [(138, 'Sto scherzando, sto in gran forma')], ''),
    ('arianna', 'Ciao Stanis, come stai?', 'Hi Stanis, how are you?', [(144, 'come stai')], ''),
    ('stanis', 'Bene, grazie.', 'Well, thank you.', [(145, 'Bene, grazie')], ''),
    ('arianna', 'Sei andato a giocare a tennis?', 'Did you go and play tennis?', [(146, 'Sei andato a giocare a tennis')], ''),
    ('stanis', 'Certo.', 'Of course.', [(147, 'Certo')], ''),
    ('arianna', 'Da contratto tu non puoi giocare a tennis.', 'Under your contract you cannot play tennis.', [(148, 'da contratto tu non puoi giocare a tennis')], ''),
    ('arianna', 'Ti devo parlare.', 'I need to talk to you.', [(152, 'Ti devo parlare')], ''),
    ('stanis', 'Dopo.', 'Later.', [(153, 'Dopo')], ''),
    ('stanis', "Ma guarda chi c'è!", 'Well, look who is here!', [(155, "ma guarda chi c'è")], ''),
    ('alessandro', 'Io sono Alessandro, il nuovo stagista di regia.', 'I am Alessandro, the new directing intern.', [(160, 'Io sono Alessandro, il nuovo stagista di regia')], ''),
    ('stanis', 'No, da oggi in poi ti chiamerai Seppia.', 'No, from today on you will be called Squid.', [(162, 'da oggi in poi ti chiamerai Seppia')], ''),
    ('stanis', 'Ti piace Seppia?', 'Do you like Squid?', [(163, 'ti piace Seppia')], ''),
]
WALK = [
    (0, None, "'What an extraordinary studio smell! I feel at home.' Opening with \"che\" before a thing means \"what a\", and \"mi sento a casa\" is the warm phrase for feeling right at home."),
    (1, None, "'As soon as I can, I am quitting this series.' \"Appena\" means \"as soon as\", while \"mollare\" is a lively casual word for dropping or quitting something."),
    (2, None, "'I am kidding! I am in top form.' \"Sto scherzando\" is the exact equivalent of \"I'm joking\", built with \"stare\" to show what he is doing right this second."),
    (3, None, "'Hi Stanis, how are you?' \"Come stai?\" is the classic friendly greeting for someone you know well; with a stranger you would say \"come sta?\" instead."),
    (4, None, "'Well, thank you.' Simple, clean, and everywhere: \"bene, grazie\" answers \"come stai?\" in two effortless words."),
    (5, None, "'Did you go and play tennis?' Where English says \"play tennis\" directly, Italian links sport names with \"a\": \"giocare a tennis\"."),
    (6, None, "'Of course.' \"Certo\" literally means \"certain\" or \"sure\", and by itself it makes an upbeat, confident \"of course\"."),
    (7, None, "'Under your contract you cannot play tennis.' \"Da contratto\" packs \"according to your contract\" into two brisk workplace words."),
    (8, None, "'I need to talk to you.' Notice \"ti\" right at the front, meaning \"to you\", before \"devo parlare\", \"I must speak\"."),
    (9, None, "'Later.' Stanis brushes Arianna off with a single word: \"dopo\" covers both \"after\" and \"later\"."),
    (10, None, "'Well, look who is here!' \"Guarda chi c'e\" is a cheerful, theatrical greeting when you spot someone, even when Stanis actually has no idea who Alessandro is."),
    (11, None, "'I am Alessandro, the new directing intern.' Adding \"di regia\" specifies his department: \"stagista di regia\" is an intern on the directing team."),
    (12, None, "'No, from today on you will be called Squid.' \"Da oggi in poi\" means \"from today onwards\", and \"seppia\" is a cuttlefish or squid — Stanis decides Alessandro looks pale."),
    (13, None, "'Do you like Squid?' In Italian, \"ti piace\" literally works backwards from English: \"Seppia\" is the thing that is pleasing \"to you\"."),
]
