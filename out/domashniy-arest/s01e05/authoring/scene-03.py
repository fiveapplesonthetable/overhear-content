# Authoring module for domashniy-arest-s01e05-scene-03.
ID = 'domashniy-arest-s01e05-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 3
TITLE = 'Трезвый водитель  (The Sober Driver)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Just as Nina warns that Samson will die of shame when he remembers crashing the car, a battered, hungover Samson shuffles into the kitchen and admits he can't remember anything from last night. Listen as Arkady seizes the moment to invent a heroic story on the spot, convincing Samson that he fought off restaurant hooligans to protect Nina and called a sober driver to take the car home."
OPENER = "Let's go back through the scene step by step. Samson walks into the kitchen holding his aching head, with a fresh bruise on his cheek."
TRANSITION = "Now let's hear the whole scene in the kitchen again from the start."
OUTRO = 'So Samson believes he is a hero who fought off restaurant hooligans and called a sober driver. See you next time!'
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('samson', 'Здорово!', 'Morning, folks!', [(83, 'Здорово')], ''),
    ('arkady', 'Садись, Ваня.', 'Sit down, Vanya.', [(84, 'Садись, Ваня')], ''),
    ('nina', 'А то ты вчерашний вечер не помнишь?', "As if you don't remember last night?", [(87, 'А то ты не помнишь')], "'вчерашний вечер' added"),
    ('samson', 'Я не помню.', "I don't remember.", [(88, 'Я не помню')], ''),
    ('arkady', 'Нина шутит! Всё было супер! Всё было очень хорошо!', 'Nina is joking! Everything was super! Everything was very good!', [(90, 'Нина шутит'), (91, 'Все было супер'), (92, 'Все было очень хорошо')], ''),
    ('arkady', 'Ты, Ваня, не сделал ничего плохого.', "You, Vanya, didn't do anything bad.", [(94, 'Ты, Ваня, не сделал ничего плохого')], ''),
    ('samson', 'А почему у меня тогда лицо побито?', 'Then why is my face beaten up?', [(95, 'а что мне тогда'), (96, 'побить')], "crude 'рожу побить' -> 'у меня лицо побито'"),
    ('arkady', 'Лицо у тебя побито, Ваня! Ты хулиганов остановил в ресторане!', 'Your face is beaten up, Vanya! You stopped hooligans in the restaurant!', [(97, 'у тебя побита, Ваня'), (99, 'Хулиганов'), (97, 'в ресторане')], "crude 'рожа' -> 'лицо'; 'дебоширов угомонил' -> 'хулиганов остановил'"),
    ('arkady', 'Они приставали к Нине. Нина, ну расскажите вы ему!', 'They were pestering Nina. Nina, come on, tell him!', [(100, 'приставали'), (102, 'Нина, ну расскажите вы ему')], "cue 100 'к ней не приставали' -> 'приставали к Нине'"),
    ('nina', 'Мы танцевали. Сначала они там грубили, оскорбляли.', 'We were dancing. First they were rude and insulting over there.', [(105, 'Мы танцевали'), (109, 'Сначала они там'), (109, 'оскорбляли')], "crude cues 107 ('лапать') and 110 ('шлюхой') omitted; 'дерзили' -> 'грубили'"),
    ('nina', 'А когда ты прибежал, ты всё решил! Потом приехала полиция.', 'And when you came running, you sorted everything out! Then the police arrived.', [(113, 'а когда ты прибежал'), (113, 'ты'), (113, 'все'), (114, 'Потом приехала полиция')], "cue 113 'ну ты и все там это' -> 'ты всё решил'"),
    ('samson', 'Точно, полиция была! А что с машиной?', "That's right, the police were there! And what about the car?", [(115, 'точно'), (115, 'Полиция'), (115, 'была'), (117, 'с машиной')], ''),
    ('arkady', 'С машиной всё хорошо, Ваня! На ней ни одной царапины не было.', "Everything is fine with the car, Vanya! There wasn't a single scratch on it.", [(118, 'С машиной все хорошо, Ваня'), (119, 'на ней ни одной царапины не было')], ''),
    ('arkady', 'Ты же не помнишь ничего. Ты вызвал трезвого водителя!', "You don't remember anything, after all. You called a sober driver!", [(121, 'ты же не помнишь ничего'), (122, 'Ты вызвал трезвого водителя')], ''),
    ('samson', 'Слава богу! Я пьяных за рулём просто терпеть не могу!', 'Thank goodness! I simply cannot stand drunk people behind the wheel!', [(123, 'Слава Богу'), (126, 'за рулем пьяных'), (126, 'просто терпеть не могу')], "cue 127 'уроды конченые' omitted"),
    ('arkady', 'Да что ты, Вань! Ты герой! Да, Нина?', "Come on, Vanya! You're a hero! Right, Nina?", [(131, 'Да что ты, Вань! Ты герой! Да, Нина')], ''),
    ('nina', 'Да.', 'Yes.', [(132, 'Да')], ''),
    ('arkady', 'Кстати, я хочу тебя познакомить. Это новый начальник твоего предвыборного штаба, Илона.', 'By the way, I want to introduce you. This is the new head of your campaign team, Ilona.', [(134, 'Кстати, я хочу тебя познакомить'), (135, 'Это новый начальник'), (135, 'предвыборного штаба, Илона')], "cue 135 'моего' -> 'твоего'; English 'Take your time' in cue 145 omitted"),
]
WALK = [
    (0, None, "'Morning, folks!' Samson greets everyone with a casual, hearty hello."),
    (1, None, "'Sit down, Vanya.' Arkady invites him to sit at the table, using the affectionate short form of Ivan."),
    (2, None, "'As if you don't remember last night?' Nina asks sceptically, assuming he knows what he did."),
    (3, None, "'I don't remember.' As soon as Arkady hears those three words, his eyes light up and he cuts Nina off."),
    (4, None, "'Nina is joking! Everything was super! Everything was very good!' Notice that 'everything was' uses the neuter past tense."),
    (5, None, "'You, Vanya, didn't do anything bad.' Literally 'nothing bad', with 'bad' in the 'of' form singular after 'nothing'."),
    (6, None, "'Then why is my face beaten up?' Literally 'by me then face is beaten', using the short passive form in the neuter form to match 'face'."),
    (7, 'Лицо у тебя побито, Ваня!', "'Your face is beaten up, Vanya!' Arkady repeats Samson's words to buy a second to think."),
    (7, 'Ты хулиганов остановил в ресторане!', "'You stopped hooligans in the restaurant!' Because 'hooligans' is an animate plural noun, its object-form direct object ending matches the plural 'of' form."),
    (8, 'Они приставали к Нине.', "'They were pestering Nina.' Arkady explains the fight by saying those men were pestering Nina."),
    (8, 'Нина, ну расскажите вы ему!', "'Nina, come on, tell him!' Arkady nudges Nina to back up his story."),
    (9, None, "'We were dancing. First they were rude and insulting over there.' Both verbs are ongoing-action form plural, setting the scene."),
    (10, 'А когда ты прибежал, ты всё решил!', "'And when you came running, you sorted everything out!' The prefix on 'ran' adds the meaning of 'arriving by running', and 'decided everything' means 'settled the whole thing'."),
    (10, 'Потом приехала полиция.', "'Then the police arrived.' That sparks a faint memory in Samson's head."),
    (11, None, "'That's right, the police were there! And what about the car?' Literally 'and what with the car?' — asking what happened to the borrowed vehicle."),
    (12, 'С машиной всё хорошо, Ваня!', "'Everything is fine with the car, Vanya!' Arkady doesn't blink."),
    (12, 'На ней ни одной царапины не было.', "'There wasn't a single scratch on it.' With 'was not', the thing that was absent goes into the 'of' form: 'not one scratch'."),
    (13, 'Ты же не помнишь ничего.', "'You don't remember anything, after all.' The particle reminds Samson of what he just admitted."),
    (13, 'Ты вызвал трезвого водителя!', "'You called a sober driver!' In Russian cities, a 'sober driver' is a service where a professional driver comes to drive you home in your own car."),
    (14, 'Слава богу!', "'Thank goodness!' Literally 'glory to God!'"),
    (14, 'Я пьяных за рулём просто терпеть не могу!', "'I simply cannot stand drunk people behind the wheel!' Literally 'I simply cannot endure drunk ones behind the wheel'."),
    (15, None, "'Come on, Vanya! You're a hero! Right, Nina?' Arkady claps Samson on the shoulder and looks at Nina."),
    (16, None, "'Yes.' Nina plays along, and Arkady gestures to Ilona."),
    (17, 'Кстати, я хочу тебя познакомить.', "'By the way, I want to introduce you.' Literally 'to acquaint you'."),
    (17, 'Это новый начальник твоего предвыборного штаба, Илона.', "'This is the new head of your campaign team, Ilona.' Here, Ilona shakes Samson's hand and welcomes him to the team, while Samson goes to wash his face."),
]
