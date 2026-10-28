# Authoring module for kukhnya-s04e17-scene-02.
ID = 'kukhnya-s04e17-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 17
SCENE = 2
TITLE = 'Благодарность Герману  (Thanking German)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'german': 'Герман', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.17'
SOURCE_FILE = 'sources/kukhnya/s04/e17.ru.srt'
INTRO = "Art director Vika Goncharova steps into the chef's office to thank the new head chef, German Land. He recently took the blame for a prank and saved Vika from being fired by Dmitry Nagiyev. Let's listen to their polite exchange in Russian."
OPENER = "Let's go through Vika and German's conversation in the office line by line."
TRANSITION = "Now let's hear their office exchange again from beginning to end."
OUTRO = 'German charms Vika with a delicate dessert and hints that he hopes they will become more than colleagues. Notice the formal plural pronouns they use to maintain professional distance. See you next time!'
CLOSING = ('german', 'Пока!')
STORY = [
    ('german', 'Виктория Сергеевна, проходите, пожалуйста.', 'Viktoriya Sergeyevna, come in, please.', [(11, 'Виктория Сергеевна, проходите, пожалуйста')], 'adapted'),
    ('vika', 'Я хотела ещё раз поблагодарить.', 'I wanted to thank you once again.', [(12, 'Я хотела еще раз')], 'adapted'),
    ('vika', 'Хочу сказать вам большое спасибо.', 'I want to say a big thank you to you.', [(13, 'Сказать вам спасибо')], 'adapted'),
    ('vika', 'Вы спасли меня от увольнения.', 'You saved me from being fired.', [(13, 'вы спасли меня от увольнения')], 'adapted'),
    ('vika', 'Не знаю, как благодарить вас.', 'I do not know how to thank you.', [(14, 'Даже не знаю, как благодарить вас')], 'adapted'),
    ('german', 'Может быть, попробуете этот десерт?', 'Perhaps you will try this dessert?', [(15, 'Может быть так')], 'adapted'),
    ('vika', 'Вы сами его сейчас приготовили?', 'Did you prepare it yourself just now?', [], 'new'),
    ('german', 'Не нужно никакой особой благодарности.', 'There is no need for any special gratitude.', [(16, 'Благодарности')], 'adapted'),
    ('german', 'Мы ведь с вами друзья.', 'After all, you and I are friends.', [(16, 'Мы ведь с вами друзья')], ''),
    ('german', 'Ну, хотя бы в перспективе.', 'Well, at least in the future.', [(17, 'Ну, хотя бы в перспективе')], ''),
    ('german', 'Желаю вам приятного аппетита.', 'I wish you bon appetit.', [(18, 'Приятного аппетита')], 'adapted'),
    ('vika', 'Это выглядит просто очень вкусно.', 'This looks simply delicious.', [], 'new'),
]
WALK = [
    (0, None, "'Viktoriya Sergeyevna, come in, please.' Around the moment and exchange, German sets a calm, everyday tone with Vika."),
    (1, None, "'I wanted to thank you once again.' Claiming that she wanted to thank German once again sounds confident, even if German has doubts."),
    (2, None, "'I want to say a big thank you to you.' Here wanting to say a big thank German to German sets up the next turn in their exchange."),
    (3, None, '\'You saved me from being fired.\' Around the conversation and office, Vika sets a calm, everyday tone with German. Notice how she sticks to the formal "you", keeping a professional line between them.'),
    (4, None, '\'I do not know how to thank you.\' Realizing that she does not know how to thank German changes how Vika handles the situation. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (5, None, "'Perhaps you will try this dessert?' Questioning whether perhaps Vika will try this dessert is how German tests Vika's story."),
    (6, None, '\'Did you prepare it yourself just now?\' Asking whether German prepares it themselves just now cuts straight through the tension between Vika and German. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (7, None, '\'There is no need for any special gratitude.\' Admitting that there is no need for any special gratitude shows German being honest for a change. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (8, None, "'After all, you and I are friends.' Saying that after all Vika and he are friends is how German sets the tone with Vika."),
    (9, None, "'Well, at least in the future.' Over the work and the exchange, German answers Vika without a second thought."),
    (10, None, '\'I wish you bon appetit.\' Explaining that he wishes Vika bon appetit lays the cards on the table for Vika. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (11, None, "'This looks simply delicious.' Vika tells German that this looks simply delicious without dressing it up."),
]
