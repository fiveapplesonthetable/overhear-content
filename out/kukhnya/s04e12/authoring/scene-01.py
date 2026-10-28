# Authoring module for kukhnya-s04e12-scene-01.
ID = 'kukhnya-s04e12-scene-01'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 12
SCENE = 1
TITLE = 'Свадебный банкет  (The Wedding Banquet)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.12'
SOURCE_FILE = 'sources/kukhnya/s04/e12.ru.srt'
INTRO = "At the host podium in Claude Monet, Max's ex-girlfriend Sasha cheerfully greets Vika and asks to book a Thursday wedding banquet for thirty guests, triggering an immediate lie from Vika."
OPENER = "Let's go through each line of Sasha's request and Vika's polite refusal."
TRANSITION = 'Now listen to the whole opening conversation again at natural speed.'
OUTRO = "Notice how Russian says 'in a close circle' with the special locative ending '-u' on 'v uzkom krugu'. Until next time!"
CLOSING = ('sasha', 'Всего хорошего!')
STORY = [
    ('sasha', 'Вика, привет, как твои дела?', 'Vika, hi, how are you doing?', [(1, 'Вика, привет')], 'adapted for A1 clarity'),
    ('sasha', 'А я решила отпраздновать здесь свадьбу.', 'And I decided to celebrate my wedding here.', [(2, 'А я решила отпраздновать здесь свадьбу')], ''),
    ('sasha', 'Это ведь здорово, правда?', "That is great, isn't it?", [(3, 'Здорово, правда')], 'adapted for A1 clarity'),
    ('vika', 'Ты хочешь праздновать свадьбу здесь?', 'You want to celebrate your wedding here?', [(4, 'Свадьбу? Здесь')], 'adapted for A1 clarity'),
    ('sasha', 'Ну да, мы с Мишей женимся.', 'Well yes, Misha and I are getting married.', [(5, 'Ну да. Мы с Мишей')], 'adapted for A1 clarity'),
    ('sasha', 'Хотим отпраздновать в узком кругу.', 'We want to celebrate in a close circle.', [(6, 'Хотим отпраздновать в узком кругу')], ''),
    ('sasha', 'Банкет примерно человек на тридцать.', 'A banquet for approximately thirty people.', [(7, 'Банкет приблизительно человек на')], 'adapted for A1 clarity'),
    ('sasha', 'Посмотри, пожалуйста, у вас четверг свободен?', 'Check, please, is Thursday free at your place?', [(8, 'Посмотри, пожалуйста, у вас четверг свободен')], ''),
    ('vika', 'Сейчас посмотрю в нашем журнале.', 'I will look in our logbook right now.', [(8, 'у вас четверг свободен')], 'adapted for A1 clarity'),
    ('vika', 'К сожалению, на этой неделе всё занято.', 'Unfortunately, everything is booked this week.', [(9, 'К сожалению, на этой неделе у нас все занято')], 'adapted for A1 clarity'),
    ('vika', 'Так что извините меня, пожалуйста.', 'So excuse me, please.', [(10, 'Так что извините')], 'adapted for A1 clarity'),
    ('vika', 'Ничем не можем вам помочь.', 'We cannot help you with anything.', [(10, 'ничем я помочь не можем')], 'adapted for A1 clarity'),
]
WALK = [
    (0, None, "'Vika, hi, how are you doing?' By asking how Vika doing is, Sasha presses Vika for a straight answer."),
    (1, None, "'And I decided to celebrate my wedding here.' Realizing that she decided to celebrate her wedding here changes how Sasha handles the situation."),
    (2, None, '\'That is great, isn\'t it?\' Sasha asks whether that is great is not it, refusing to let the point slide. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (3, None, "'You want to celebrate your wedding here?' Vika asks whether Sasha wants to celebrate Sasha's wedding here, refusing to let the point slide."),
    (4, None, "'Well yes, Misha and I are getting married.' Admitting that Misha and she are getting married shows Sasha being honest for a change."),
    (5, None, "'We want to celebrate in a close circle.' Wanting to celebrate in a close circle is how Sasha lays out the situation for Vika."),
    (6, None, "'A banquet for approximately thirty people.' Over the wedding and the point, Sasha answers Vika without a second thought."),
    (7, None, '\'Check, please, is Thursday free at your place?\' Questioning whether check please is Thursday free at Vika\'s place is how Sasha tests Vika\'s story. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (8, None, "'I will look in our logbook right now.' Saying that she will look in their logbook right now is how Vika sets the tone with Sasha."),
    (9, None, "'Unfortunately, everything is booked this week.' Since everything is booked this week, Vika does not waste words on excuses."),
    (10, None, "'So excuse me, please.' Over the banquet and the moment, Vika answers Sasha without a second thought."),
    (11, None, '\'We cannot help you with anything.\' Pointing out that they cannot help Sasha with anything gives Sasha a sobering reality check. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
]
