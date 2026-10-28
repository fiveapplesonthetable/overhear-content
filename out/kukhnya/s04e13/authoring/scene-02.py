# Authoring module for kukhnya-s04e13-scene-02.
ID = 'kukhnya-s04e13-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 13
SCENE = 2
TITLE = 'Грустная музыка в зале  (Sad Music in the Dining Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.13'
SOURCE_FILE = 'sources/kukhnya/s04/e13.ru.srt'
INTRO = "Inside the dining room of Claude Monet, the mood is heavy after Vika's painful breakup with Max. Bartender Kostya notices Nastya looking upset, and Nastya tries to comfort Vika with a glass of water while begging the pianist to play something more cheerful."
OPENER = "Let's break down how Kostya, Nastya, and Vika speak to each other in the dining room."
TRANSITION = "Now let's hear the entire dining room conversation again at full speed."
OUTRO = "Vika pulls herself together and throws her energy back into managing the restaurant reports. Next, we return to Chef Barinov's office as Katya asks her father for a job. See you next time!"
CLOSING = ('vika', 'Пока!')
STORY = [
    ('kostya', 'Настя, у тебя что-то случилось?', 'Nastya, did something happen to you?', [(9, 'Настя, что-то случилось?')], 'adapted'),
    ('nastya', 'Нет, Костя, у меня ничего.', 'No, Kostya, nothing is wrong with me.', [(10, 'Ничего.')], 'adapted'),
    ('nastya', 'Виктория Сергеевна, как вы себя чувствуете?', 'Viktoriya Sergeyevna, how do you feel?', [(11, 'Как вы себя чувствуете?')], 'adapted'),
    ('nastya', 'Держитесь, пожалуйста, всё пройдёт.', 'Hang in there, please, everything will pass.', [(12, 'Крепитесь, пожалуйста.')], 'adapted'),
    ('vika', 'Спасибо, Настя, всё вполне нормально.', 'Thank you, Nastya, everything is quite normal.', [(13, 'Все нормально. Водички?')], 'adapted'),
    ('nastya', 'Хотите, я принесу вам водички?', 'Do you want me to bring you some water?', [(13, 'Все нормально. Водички?')], 'adapted'),
    ('vika', 'Да, спасибо тебе большое.', 'Yes, thank you very much.', [(14, 'Спасибо.')], 'adapted'),
    ('nastya', 'Денис, можно играть что-нибудь повеселее?', 'Denis, can you play something more cheerful?', [(15, 'Можно играть в что-нибудь?')], 'adapted'),
    ('nastya', 'От этой музыки хочется плакать.', 'This music makes one want to cry.', [(15, 'Можно играть в что-нибудь?')], 'adapted'),
    ('vika', 'Костя, принеси отчёт в кабинет.', 'Kostya, bring the report to the office.', [(16, 'Костя, принеси отчет в')], 'adapted'),
    ('kostya', 'Хорошо, сейчас всё быстро принесу.', 'All right, I will bring everything right now.', [(17, 'Ну')], 'adapted'),
    ('nastya', 'Бедная Вика, мне её жалко.', 'Poor Vika, I feel sorry for her.', [(17, 'Ну')], 'adapted'),
]
WALK = [
    (0, None, '\'Nastya, did something happen to you?\' Here asking whether something happen to Nastya shows Kostya looking for the real truth. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (1, None, '\'No, Kostya, nothing is wrong with me.\' Nastya mentions that nothing is wrong so Kostya sees what is at stake. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (2, None, "'Viktoriya Sergeyevna, how do you feel?' Asking whether Viktoriya Sergeyevna how do Kostya feels puts Kostya right on the defensive."),
    (3, None, "'Hang in there, please, everything will pass.' Hanging in there please everything will pass moves the conversation forward without extra drama."),
    (4, None, "'Thank you, Nastya, everything is quite normal.' Vika explains that everything is quite normal, keeping her voice calm and direct."),
    (5, None, "'Do you want me to bring you some water?' By asking whether Kostya wants her to bring Kostya some water, Nastya presses Kostya for a straight answer."),
    (6, None, '\'Yes, thank you very much.\' Over the breakup and the truth, Vika answers Kostya without a second thought. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, '\'Denis, can you play something more cheerful?\' Asking whether Kostya plays something more cheerful is how Nastya puts Kostya on the spot. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (8, None, "'This music makes one want to cry.' Admitting that this music makes one want to cry shows Nastya being honest for a change."),
    (9, None, "'Kostya, bring the report to the office.' Because Kostya should bring the report to the office, Vika treats the matter as settled."),
    (10, None, "'All right, I will bring everything right now.' Once all right he will bring everything right now, Kostya can finally tell Nastya what he means."),
    (11, None, "'Poor Vika, I feel sorry for her.' Adding that poor Vika she feels sorry fills in the missing piece for Kostya."),
]
