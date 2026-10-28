# Authoring module for kukhnya-s04e12-scene-10.
ID = 'kukhnya-s04e12-scene-10'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 12
SCENE = 10
TITLE = 'Легенда про вывих  (The Sprained-Ankle Cover Story)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.12'
SOURCE_FILE = 'sources/kukhnya/s04/e12.ru.srt'
INTRO = "To get out of the apartment without waking Vika's jealousy, Max has Denis call Vika's phone with a story about Kostya spraining his ankle, then calls sleeping Kostya to brief him."
OPENER = "Let's examine each line of the late-night cover story."
TRANSITION = "Now let's hear the whole cover-story scene again from start to finish."
OUTRO = "That wraps up this scene as at Max's request, Denis calls Vika's phone pretending Kostya sprained his ankle at a bar so Max can borrow Vika's car, and Max wakes Kostya to make him memorize the cover story. See you next time!"
CLOSING = ('kostya', 'До свидания!')
STORY = [
    ('denis', 'Вика, привет, это звонит Денис.', 'Vika, hi, this is Denis calling.', [(140, 'Вик, привет. Это Денис')], 'adapted for A1 clarity'),
    ('denis', 'Извините, пожалуйста, что звоню так поздно.', 'Excuse me, please, for calling so late.', [(141, 'Извините, что так поздно')], 'adapted for A1 clarity'),
    ('denis', 'Я не могу дозвониться до Макса.', 'I cannot get through to Max on the phone.', [(141, 'Не могу до Макса дозвониться')], 'adapted for A1 clarity'),
    ('denis', 'Костя тут упал и ногу подвернул.', 'Kostya fell here and twisted his ankle.', [(142, 'Костя упал, и ногу подвернул')], 'adapted for A1 clarity'),
    ('denis', 'Макс, я так долго никогда не врал!', 'Max, I have never lied at such length before!', [(146, 'Макс, я так долго еще никогда не врал')], 'adapted for A1 clarity'),
    ('denis', 'Я сказал, что Костя подвернул ногу.', 'I told her that Kostya twisted his ankle.', [(147, 'я ей сказал, что Костя подвернул ногу')], 'adapted for A1 clarity'),
    ('max', 'Понял, Костя, да, я сейчас приеду.', 'Got it, Kostya, yes, I will come right now.', [(148, 'Костя, да, сейчас приеду')], 'adapted for A1 clarity'),
    ('max', 'Викуля, можно я твою машину возьму?', 'Vikulya, may I take your car?', [(149, 'а можно я твою машину возьму')], 'adapted for A1 clarity'),
    ('max', 'Костян, здорово, ты уже спишь?', 'Kostyan, hey, are you asleep already?', [(153, 'Костян, здорово. Спишь')], 'adapted for A1 clarity'),
    ('max', 'Я тебя попрошу, только вопросов не задавай.', 'I will ask you a favor, just do not ask questions.', [(154, 'только ты вопросов не задавай, ладно')], 'adapted for A1 clarity'),
    ('max', 'Если Вика спросит, ты вывихнул ногу.', 'If Vika asks, you dislocated your foot.', [(155, 'если Вика тебя спросит, то сегодня ты гулял с Денисом и вывихнул ногу')], 'adapted for A1 clarity'),
    ('kostya', 'Подожди, а зачем я вывихнул ногу?', 'Wait, and why did I dislocate my foot?', [(157, 'Зачем вывихнул ногу')], 'adapted for A1 clarity'),
    ('kostya', 'А какую ногу, правую или левую?', 'And which leg, the right one or the left one?', [(159, 'А правую или левую')], 'adapted for A1 clarity'),
    ('max', 'Да вообще любую, потом всё объясню!', 'Any leg at all, I will explain everything later!', [(160, 'Любую')], 'adapted for A1 clarity'),
]
WALK = [
    (0, None, "'Vika, hi, this is Denis calling.' Saying that this is Denis calling is how Denis sets the tone with Kostya."),
    (1, None, "'Excuse me, please, for calling so late.' Between the car and the kitchen, Denis gives Kostya a quick, grounded response."),
    (2, None, "'I cannot get through to Max on the phone.' Denis mentions that he cannot get through to Max on the phone so Kostya sees what is at stake."),
    (3, None, "'Kostya fell here and twisted his ankle.' Even though Kostya fell here and twisted his ankle, Denis keeps a steady face in front of Kostya."),
    (4, None, '\'Max, I have never lied at such length before!\' Insisting that he has never lied at such length shows Denis is not backing down. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (5, None, "'I told her that Kostya twisted his ankle.' Saying that he told her that Kostya twisted his ankle is how Denis sets the tone with Kostya."),
    (6, None, "'Got it, Kostya, yes, I will come right now.' Once got it Kostya yes he will come right now, Max can finally tell Denis what he means."),
    (7, None, '\'Vikulya, may I take your car?\' Asking whether someone may he takes Denis\'s car puts Denis right on the defensive. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (8, None, '\'Kostyan, hey, are you asleep already?\' Wondering if someone hey are Denis asleep already shows Max caught off guard. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (9, None, "'I will ask you a favor, just do not ask questions.' Since he will ask Denis a favor just do not ask questions, Max does not waste words on excuses."),
    (10, None, '\'If Vika asks, you dislocated your foot.\' Mentioning that if Vika asks Denis dislocated Denis\'s foot moves the talk in a new direction. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (11, None, '\'Wait, and why did I dislocate my foot?\' Here asking why he dislocate his foot shows Kostya looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (12, None, "'And which leg, the right one or the left one?' Asking whether which leg the right one or the left one puts Denis right on the defensive."),
    (13, None, "'Any leg at all, I will explain everything later!' Max declares that any leg at all he will explain everything later as the tension in the room peaks. Russian puts the key word right up front so his emotion lands on the first beat."),
]
