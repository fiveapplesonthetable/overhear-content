# Authoring module for dix-pour-cent-s01e01-scene-01.
ID = 'dix-pour-cent-s01e01-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Cécile est en retard  (Cécile Is Late)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
VOICES = {'narrator': 'sky', 'cecile': 'emilie', 'gabriel': 'theo', 'journaliste': 'marcel'}
LABELS = {'cecile': 'Cécile', 'gabriel': 'Gabriel', 'journaliste': 'Le journaliste'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "He is waiting for her at a photo shoot in a smart hotel, the journalist and the photographer are ready, and Cécile is nowhere to be seen. He phones her, and she answers from the back of a horse in the countryside. You'll hear the whole story in French first; don't worry if a lot of it slips past you."
OPENER = "Let's go back through it slowly. Gabriel is at the hotel, phone to his ear, and the first thing he wants to know is where on earth his star is."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's the opening of the episode, and you've already met the polite 'you' between an agent and his star. When you watch it, listen for the phone calls and the apologies; they'll sound familiar now. See you next time!"
CLOSING = ('cecile', 'Bonne soirée!')
STORY = [
    ('gabriel', 'Cécile? Vous êtes où?', 'Cécile? Where are you?', [(12, 'Cécile ?'), (13, 'Vous êtes où ?')], ''),
    ('cecile', "Gabriel! Je suis à mon cours d'équitation.", "Gabriel! I'm at my horse-riding lesson.", [(12, 'Gabriel !'), (17, "Je suis à mon cours d'équitation")], ''),
    ('gabriel', 'On est au Westin. Tout le monde est là.', "We're at the Westin. Everyone is here.", [(14, 'On est au Westin'), (15, 'Tout le monde est là')], ''),
    ('cecile', 'Oh non! Je suis en retard.', 'Oh no! I', [], ''),
    ('gabriel', 'Vous savez monter, non?', 'You can ride, can', [(19, 'vous saviez monter')], ''),
    ('cecile', "Oui, oui. J'ai juste besoin d'un petit cours.", 'Yes, yes. I just need a little lesson.', [(22, "J'ai juste besoin d'un petit cours")], ''),
    ('gabriel', 'Je peux vous faire confiance?', 'Can I trust you?', [(26, 'Je peux vous faire confiance ?')], ''),
    ('cecile', 'Oui. Je suis presque au point. Je vous rappelle.', "Yes. I've almost got it. I'll call you back.", [(27, 'Je suis presque au point'), (29, 'je vous rappelle')], ''),
    ('gabriel', 'Vous serez là quand?', 'When will you be here?', [(30, 'Vous serez là quand ?')], ''),
    ('cecile', 'Dans une heure.', 'In an hour.', [(30, 'Dans une heure')], ''),
    ('cecile', 'Je suis désolée. Vraiment désolée.', 'I', [(41, 'Je suis désolée'), (44, 'Vraiment désolée')], ''),
    ('journaliste', 'Vous tournez un film aux États-Unis?', 'Are you making a film in the United States?', [(51, 'un film aux États-Unis')], ''),
    ('cecile', "Rien n'est signé. On attend l'appel.", 'Nothing is signed. We', [(55, "Rien n'est signé"), (55, "On attend l'appel")], ''),
    ('cecile', "C'est le prochain film de Tarantino.", 'It', [(57, "C'est le prochain film de Tarantino")], ''),
    ('journaliste', 'Fantastique!', 'Fantastic!', [(58, 'Fantastique !')], ''),
    ('gabriel', "Tarantino ne prendra pas Cécile. Problème d'âge.", "Tarantino won't take Cécile. A problem with her age.", [(63, 'Tarantino ne prendra pas Cécile'), (64, "Problème d'âge")], ''),
    ('cecile', "C'est comme un rêve pour moi.", 'It', [(68, "C'est comme un rêve pour moi")], ''),
]
WALK = [
    (0, None, "'Where are you?' The question word comes at the very end, which is how people really talk. And notice the formal 'you': Gabriel and Cécile have worked together for years, but agent and star keep the polite form."),
    (1, None, "'I'm at my horse-riding lesson.' Cécile is cheerful, out in the countryside on a horse called Biscotte, and she has completely forgotten the photo shoot."),
    (2, None, "'We're at the Westin.' That little word at the start means 'we' in everyday speech; it's shorter and more casual than the textbook word for 'we'."),
    (3, None, "'Everyone is here.' Literally 'all the world is here'. Gabriel means the journalist, the photographer, the make-up people, all waiting."),
    (4, None, "'Oh no! I'm late.' In the show she says something much ruder; here she keeps it clean."),
    (5, None, "'You can ride, can't you?' The small word at the end turns a statement into a worried check. The American film people insisted that the actress must be good on a horse."),
    (6, None, "'Yes, yes. I just need a little lesson.' The word for 'just' slips in after the verb. She sounds a lot less sure than she wants to."),
    (7, None, "'Can I trust you?' Again the polite 'you', tucked in before the verb. Gabriel is getting anxious."),
    (8, None, "'I've almost got it.' Literally 'I'm almost at the point'. Then she gets off the phone in a hurry, because the horse is heading into the woods."),
    (9, None, "'I'll call you back.' A sentence you'll hear all the time in an agency where everybody is on the phone. Gabriel has one last question."),
    (10, None, "'When will you be here?' This one is in the future tense, and again the question word sits at the end."),
    (11, None, "'In an hour.' An hour later she rushes into the hotel, still smelling of horse."),
    (12, None, "'I'm sorry. Really sorry.' On paper the word for 'sorry' gets an extra e at the end because Cécile is a woman; a man would write it without, though both sound exactly the same. Then make-up, lights, and the interview."),
    (13, None, "'Are you making a film in the United States?' The journalist has heard a rumour, and she is fishing for news."),
    (14, None, "'Nothing is signed. We're waiting for the call.' The word for 'nothing' works with the little negative word before the verb, just like 'not' does. They are waiting for a call from Los Angeles."),
    (15, None, "'It's Tarantino's next film.' Cécile can't resist telling her, off the record of course."),
    (16, None, "'Fantastic!' The same word as in English, with a French accent. But at that very moment, Gabriel's phone buzzes with a message."),
    (17, None, "'Tarantino won't take Cécile.' The two little negative words wrap around the verb, here a verb in the future."),
    (18, None, "'A problem with her age.' Cécile is in her early forties, and Hollywood has decided that is too old. Gabriel reads it under his breath, goes pale, and says nothing to her."),
    (19, None, "'It's like a dream for me.' Cécile says it to the journalist, happy and unaware, while her agent stands right there holding the bad news. Now let's hear the whole scene again, from the phone call to the photo shoot."),
]
