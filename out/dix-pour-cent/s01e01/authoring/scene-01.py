# Authoring module for dix-pour-cent-s01e01-scene-01.
ID = 'dix-pour-cent-s01e01-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Cécile est en retard  (Cécile Is Late)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'cecile': 'Cécile', 'gabriel': 'Gabriel', 'journaliste': 'Le journaliste'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "He is waiting for her at a photo shoot in a smart hotel, the journalist and the photographer are ready, and Cécile is nowhere to be seen. He phones her, and she answers from the back of a horse in the countryside. You'll hear the whole story in French first; don't worry if a lot of it slips past you."
OPENER = "Let's go back through it slowly. Gabriel is at the hotel, phone to his ear, and the first thing he wants to know is where on earth his star is."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's the opening of the episode, and you've already met the polite 'you' between an agent and his star. When you watch it, listen for the phone calls and the apologies; they'll sound familiar now. See you next time!"
CLOSING = ('cecile', 'Bonne soirée!')
STORY = [
    ('gabriel', 'Cécile? Vous êtes où?', 'Where are you?', [(12, 'Cécile ?'), (13, 'Vous êtes où ?')], ''),
    ('cecile', "Gabriel! Je suis à mon cours d'équitation.", "I'm at my horse-riding lesson.", [(12, 'Gabriel !'), (17, "Je suis à mon cours d'équitation")], ''),
    ('gabriel', 'On est au Westin. Tout le monde est là.', 'Everyone is here.', [(14, 'On est au Westin'), (15, 'Tout le monde est là')], ''),
    ('cecile', 'Oh non! Je suis en retard.', "Oh no! I'm late.", [], ''),
    ('gabriel', 'Vous savez monter, non?', "You can ride, can't you?", [(19, 'vous saviez monter')], ''),
    ('cecile', "Oui, oui. J'ai juste besoin d'un petit cours.", 'Yes, yes. I just need a little lesson.', [(22, "J'ai juste besoin d'un petit cours")], ''),
    ('gabriel', 'Je peux vous faire confiance?', 'Can I trust you?', [(26, 'Je peux vous faire confiance ?')], ''),
    ('cecile', 'Oui. Je suis presque au point. Je vous rappelle.', "I'll call you back.", [(27, 'Je suis presque au point'), (29, 'je vous rappelle')], ''),
    ('gabriel', 'Vous serez là quand?', 'When will you be here?', [(30, 'Vous serez là quand ?')], ''),
    ('cecile', 'Dans une heure.', 'In an hour.', [(30, 'Dans une heure')], ''),
    ('cecile', 'Je suis désolée. Vraiment désolée.', "I'm sorry. Really sorry.", [(41, 'Je suis désolée'), (44, 'Vraiment désolée')], ''),
    ('journaliste', 'Vous tournez un film aux États-Unis?', 'Are you making a film in the United States?', [(51, 'un film aux États-Unis')], ''),
    ('cecile', "Rien n'est signé. On attend l'appel.", "Nothing is signed. We're waiting for the call.", [(55, "Rien n'est signé"), (55, "On attend l'appel")], ''),
    ('cecile', "C'est le prochain film de Tarantino.", "It's Tarantino's next film.", [(57, "C'est le prochain film de Tarantino")], ''),
    ('journaliste', 'Fantastique!', 'Fantastic!', [(58, 'Fantastique !')], ''),
    ('gabriel', "Tarantino ne prendra pas Cécile. Problème d'âge.", 'A problem with her age.', [(63, 'Tarantino ne prendra pas Cécile'), (64, "Problème d'âge")], ''),
    ('cecile', "C'est comme un rêve pour moi.", "It's like a dream for me.", [(68, "C'est comme un rêve pour moi")], ''),
]
WALK = [
    (0, 'Vous êtes où?', "'Where are you?' This question word comes at the very end, which is how people really talk. And notice the formal 'you': Gabriel and Cécile have worked together for years, but agent and star keep the polite form."),
    (1, "Je suis à mon cours d'équitation.", "'I'm at my horse-riding lesson.' Cécile is cheerful, out in the countryside on a horse called Biscotte, and she has completely forgotten the photo shoot."),
    (2, 'On est au Westin.', "'We're at the Westin.' That little word at the start means 'we' in everyday speech; it's shorter and more casual than the textbook word for 'we'."),
    (2, 'Tout le monde est là.', "'Everyone is here.' Literally 'all the world is here'. Gabriel means the journalist, the photographer, the make-up people, all waiting."),
    (3, None, "'Oh no! I'm late.' In the show she says something much ruder; here she keeps it clean."),
    (4, None, "'You can ride, can't you?' This small word at the end turns a statement into a worried check. The American film people insisted that the actress must be good on a horse."),
    (5, None, "'Yes, yes. I just need a little lesson.' The word for 'just' slips in after the action word. She sounds a lot less sure than she wants to."),
    (6, None, "'Can I trust you?' Again the polite 'you', tucked in before the verb. Gabriel is getting anxious."),
    (7, 'Je suis presque au point.', "'I've almost got it.' Literally 'I'm almost at the point'. Then she gets off the phone in a hurry, because the horse is heading into the woods."),
    (7, 'Je vous rappelle.', "'I'll call you back.' You will hear this sentence all the time in an agency where everybody is on the phone. Gabriel has one last question."),
    (8, None, "'When will you be here?' This one is in the future tense, and again the question word sits at the end."),
    (9, None, "'In an hour.' An hour later she rushes into the hotel, still smelling of horse."),
    (10, None, "'I'm sorry. Really sorry.' On paper the word for 'sorry' gets an extra e at the end because Cécile is a woman; a man would write it without, though both sound exactly the same. Then make-up, lights, and the interview."),
    (11, None, "'Are you making a film in the United States?' The journalist has heard a rumour, and she is fishing for news."),
    (12, None, "'Nothing is signed. We're waiting for the call.' The word for 'nothing' works with the little negative word before the verb, just like 'not' does. They are waiting for a call from Los Angeles."),
    (13, None, "'It's Tarantino's next film.' Cécile can't resist telling her, off the record of course."),
    (14, None, "'Fantastic!' The same word as in English, with a French accent. But at that very moment, Gabriel's phone buzzes with a message."),
    (15, 'Tarantino ne prendra pas Cécile.', "'Tarantino won't take Cécile.' The two little negative words wrap around the verb, here a verb in the future."),
    (15, "Problème d'âge.", "'A problem with her age.' Here, Cécile is in her early forties, and Hollywood has decided that is too old. Gabriel reads it under his breath, goes pale, and says nothing to her."),
    (16, None, "'It's like a dream for me.' Cécile says it to the journalist, happy and unaware, while her agent stands right there holding the bad news."),
]
