# Authoring module for dix-pour-cent-s01e02-scene-26.
ID = 'dix-pour-cent-s01e02-scene-26'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 26
TITLE = 'Adieu, Samuel  (Goodbye, Samuel)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'francoise': 'Françoise', 'line': 'Line', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = "At the Père-Lachaise cemetery the agents bicker in whispers, because Françoise Fabian and Line Renaud both want the same part. Then, at the evening tribute, both great ladies speak about Samuel, and we follow Françoise. As always, the French comes first; let it carry you, word for word doesn't matter."
OPENER = "Let's go back through it. At the cemetery Mathias sums up the agency's problem in one sentence."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's the end of this scene. When you watch it, listen for the back-to-front way of saying 'we miss you'; both Françoise and Line use it. See you next time!"
CLOSING = ('francoise', 'Bonne journée!')
STORY = [
    ('mathias', 'Françoise Fabian et Line Renaud veulent le même rôle.', 'Françoise Fabian and Line Renaud want the same part.', [(703, 'Françoise Fabian et Line Renaud veulent le même rôle')], ''),
    ('mathias', "Et celle qui ne l'obtient pas va nous détester.", "And the one who doesn't get it will hate us.", [(704, "celle qui ne l'obtient pas")], ''),
    ('mathias', "Stop! On enterre Samuel aujourd'hui.", "Stop! We're burying Samuel today.", [(711, 'On enterre Samuel')], ''),
    ('mathias', "Bonsoir. Au nom d'ASK, je vous remercie d'être venus.", 'Good evening.', [(713, 'Bonsoir'), (714, "Au nom d'ASK, je vous remercie d'être venus")], ''),
    ('mathias', 'Je laisse la parole à une grande amie de Samuel, Françoise Fabian.', "I give the floor to a great friend of Samuel's, Françoise Fabian.", [(715, 'Je laisse la parole à une grande amie de Samuel'), (716, 'Françoise Fabian')], ''),
    ('francoise', 'Bonsoir. Il y a quelques semaines, je dînais avec Samuel.', 'A few weeks ago, I was having dinner with Samuel.', [(717, 'Bonsoir'), (718, 'Il y a quelques semaines, je dînais avec Samuel')], ''),
    ('francoise', 'Il a dit quelque chose de merveilleux.', 'He said something wonderful.', [(719, 'Il a dit quelque chose de merveilleux')], ''),
    ('francoise', 'Vous, les acteurs, vous jouez pour ne pas grandir.', "You actors, you play so you don't grow up.", [(720, 'vous les acteurs'), (723, 'Vous jouez pour ne pas grandir')], ''),
    ('francoise', 'Vous jouez pour ne pas mourir.', "You play so you don't die.", [(723, 'vous jouez pour ne pas mourir')], ''),
    ('francoise', 'Samuel, tu nous manques terriblement.', 'Samuel, we miss you terribly.', [(726, 'Tu nous manques terriblement')], ''),
    ('line', 'Samou était plein de joie, libre!', 'Samou was full of joy, free!', [(730, 'Samou était plein de joie, libre')], ''),
    ('line', 'Comme on faisait la fête, dans le temps!', 'How we used to party, back in the day!', [(732, 'Comme on faisait la fête, dans le temps')], ''),
    ('line', 'Tu nous manques, Samou.', 'We miss you, Samou.', [(735, 'Tu nous manques, Samou')], ''),
    ('line', 'Mais je te promets une chose. Nous continuerons à rire.', "We'll keep on laughing.", [(736, 'Mais je te promets une chose'), (737, 'Nous continuerons à rire')], ''),
    ('francoise', 'Oui, il faut se battre contre le chagrin.', 'Yes, we must fight against sorrow.', [(740, 'Oui, il faut se battre contre le chagrin')], ''),
    ('francoise', 'Samuel aimait vraiment rire.', 'Samuel really loved to laugh.', [(741, 'Samuel aimait vraiment rire')], ''),
    ('line', 'Tu aimais une belle chanson. Celle-là surtout.', 'You loved a beautiful song. This one most of all.', [(746, 'Tu aimais une belle chanson'), (747, 'celle-là surtout')], ''),
    ('line', "Tu disais que c'était notre chanson.", 'You used to say it was our song.', [(748, "Tu disais que c'était")], ''),
]
WALK = [
    (0, None, "'Françoise Fabian and Line Renaud want the same part.' The action word is 'to want', in its plural form for two people. The word for 'same' comes before the word."),
    (1, None, "'And the one who doesn't get it will hate us.' The near future again, 'is going to hate'."),
    (2, None, "'Stop! We're burying Samuel today.' The word for 'we' here is the everyday one. The agents fall quiet. That evening, at the tribute, Mathias welcomes everyone."),
    (3, 'Bonsoir.', "'Good evening.' Remember, this is the greeting for the evening."),
    (3, "Au nom d'ASK, je vous remercie d'être venus.", "'On behalf of ASK, thank you for coming.' Literally 'in the name of ASK, I thank you for having come'. A formal phrase for speeches."),
    (4, None, "'I give the floor to a great friend of Samuel's, Françoise Fabian.' Literally 'I leave the word to'. The word for 'friend' has its feminine ending here, and so does 'great'."),
    (3, 'Bonsoir.', "'Good evening.' Françoise greets the room in the same way, simply and with dignity."),
    (5, 'Il y a quelques semaines, je dînais avec Samuel.', "'A few weeks ago, I was having dinner with Samuel.' Françoise recalls a dinner with Samuel a few weeks earlier."),
    (6, None, "'He said something wonderful.' This time it's the other past form, with 'has', for one single event."),
    (7, None, "'You actors, you play so you don't grow up.' She's quoting Samuel."),
    (8, None, "'You play so you don't die.' The same pattern again, with 'to die'."),
    (9, None, "'Samuel, we miss you terribly.' Watch out, this one works back to front. In French you say 'you are missing to us'. The person who is missed is the subject."),
    (10, None, "'Samou was full of joy, free!' Now Line speaks, using her pet name for Samuel."),
    (11, None, "'How we used to party, back in the day!' The background past again, for something that happened again and again. Literally 'how we used to make the party'."),
    (12, None, "'We miss you, Samou.' The same back-to-front verb as in Françoise's speech: the two rivals are saying the same thing."),
    (13, 'Mais je te promets une chose.', "'But I promise you one thing.' She speaks to Samuel with the casual 'you', as to an old friend."),
    (13, 'Nous continuerons à rire.', "'We'll keep on laughing.' This is the simple future: the verb 'continue' with a future ending. Line wants laughter, not tears."),
    (14, None, "'Yes, we must fight against sorrow.' Françoise takes the floor back, with the expression for 'we must'. The word at the end is a strong one for grief."),
    (15, None, "'Samuel really loved to laugh.' The background past of 'to love', and then an infinitive. She means: but he was more than that, and the rivalry between the two women is right there, under the politeness."),
    (16, None, "'You loved a beautiful song. This one most of all.' Line has the last word. The word for 'beautiful' is feminine, like the song."),
    (17, None, "'You used to say it was our song.' Line uses two action words in the background past. Then the music starts, and the whole room sings Samuel's song together. Let's hear the whole farewell once more."),
]
