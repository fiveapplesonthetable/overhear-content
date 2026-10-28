# Authoring module for kukhnya-s05e11-scene-16.
ID = 'kukhnya-s05e11-scene-16'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 16
TITLE = "Третья ложь деда  (Grandpa's Third Lie)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = "In the dining room, Chef Barinov publicly introduces Artyom to Eleonora's business partners as the chef who personally cooked their meal. Upstairs, when the grandmother returns early and catches her husband drinking and eating meat, he invents a third lie: that Max and Vika are divorcing!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings this dual scene to a close. Notice the formal introduction allow me to introduce our new cook and the grandfather's shocking claim that Max and Vika are getting divorced. See you next time!"
CLOSING = ('barinov', 'До завтра!')
STORY = [
    ('barinov', 'Сейчас мы их удивим! Добрый вечер, господа.', 'Right now we will amaze them! Good evening, gentlemen.', [(240, 'Сейчас мы их'), (241, 'Добрый вечер, господа')], 'adapted'),
    ('barinov', 'Добрый вечер, Элеонора Андреевна.', 'Good evening, Eleonora Andreyevna.', [(242, 'Добрый вечер, Элеонора Андреевна')], 'adapted'),
    ('barinov', 'Разрешите вам представить нашего нового повара Артёма.', 'Allow me to introduce to you our new cook Artyom.', [(244, 'Разрешите вам представить нашего нового повара Артёма')], 'adapted'),
    ('barinov', 'Приятного аппетита!', 'Enjoy your meal!', [(247, 'Приятного аппетита')], 'adapted'),
    ('guest', 'Это я! У подруги давление поднялось.', "It is me! My friend's blood pressure went up.", [(248, 'Это я'), (250, 'давление')], 'adapted'),
    ('guest', 'Так, значит, можно пить и есть, чего нельзя?', 'So that means you can drink and eat what is forbidden?', [(254, 'Так, значит'), (255, 'можно пить и есть, чего нельзя')], 'adapted'),
    ('eleonora', 'Успокойся! Да ты сядь, я ведь не просто так пью.', 'Calm down! Sit down, I am not drinking for no reason.', [(256, 'Успокойся'), (257, 'Да ты сядь. Я ведь не просто так пью')], 'adapted'),
    ('eleonora', 'Повод есть.', 'There is a reason.', [(258, 'Повод есть')], 'adapted'),
    ('guest', 'Какой у тебя ещё повод?', 'What reason could you possibly have?', [(258, 'Какой у тебя еще повод-то')], 'adapted'),
    ('eleonora', 'Ты понимаешь, Максим с Викой разводятся.', 'You see, Maxim and Vika are getting divorced.', [(260, 'Ты понимаешь, Максим с Викой'), (261, 'Разводятся')], 'adapted'),
    ('barinov', 'Судя по их лицам, они довольны.', 'Judging by their faces, they are pleased.', [(264, 'Судя по их лицам, они довольны')], 'adapted'),
    ('barinov', 'Тебя ждёт триумф!', 'A triumph awaits you!', [(265, 'Тебя ждет'), (265, 'триумф')], 'adapted'),
]
WALK = [
    (0, None, "'Right now we will amaze them! Good evening, gentlemen.' Because right now they will amaze them, Barinov does not bother softening the blow for Eleonora."),
    (1, None, "'Good evening, Eleonora Andreyevna.' With the room and meat in play, Barinov keeps this short reply brisk and direct."),
    (2, None, '\'Allow me to introduce to you our new cook Artyom.\' Since Eleonora should allow him to introduce to Eleonora their new cook Artyom, Barinov does not waste words on excuses. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (3, None, "'Enjoy your meal!' Declaring that Eleonora should enjoy Eleonora's meal brings Barinov's temper right to the surface."),
    (4, None, '\'It is me! My friend\'s blood pressure went up.\' Once it is him, the guest makes sure Barinov hears every word. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, '\'So that means you can drink and eat what is forbidden?\' The guest asks whether that means Barinov can drink and eat what is forbidden, refusing to let the point slide. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (6, None, "'Calm down! Sit down, I am not drinking for no reason.' Saying that Barinov should sit down she is not drinking for no reason is how Eleonora takes charge of the moment."),
    (7, None, "'There is a reason.' Explaining that there is a reason lays the cards on the table for Barinov."),
    (8, None, '\'What reason could you possibly have?\' Questioning whether what reason could Barinov possibly have is how the guest tests Barinov\'s story. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (9, None, "'You see, Maxim and Vika are getting divorced.' Claiming that Maxim and Vika are getting divorced sounds confident, even if Barinov has doubts."),
    (10, None, "'Judging by their faces, they are pleased.' Noting that judging by their faces they are pleased keeps Barinov's side of the story simple and clear."),
    (11, None, '\'A triumph awaits you!\' With the point and meat at stake, Barinov reacts without holding back. Speaking with the close, informal "you" strips away any polite distance between them.'),
]
