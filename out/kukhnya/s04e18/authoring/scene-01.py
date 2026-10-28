# Authoring module for kukhnya-s04e18-scene-01.
ID = 'kukhnya-s04e18-scene-01'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 18
SCENE = 1
TITLE = 'Счастливый билет  (A Lucky Ticket)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.18'
SOURCE_FILE = 'sources/kukhnya/s04/e18.ru.srt'
INTRO = "Young cook Denis believes he has finally won a lucky lottery ticket after spending a romantic evening with Katya. When morning comes, however, Katya tries to slip out early because their relationship is moving so fast. Let's listen to their tender morning conversation in Russian."
OPENER = "Now let's examine how Denis convinces Katya to stay in the apartment line by line."
TRANSITION = "Let's hear the entire morning exchange in Russian from start to finish."
OUTRO = 'Denis persuades Katya not to rush out of the apartment so they can enjoy the morning together. Notice how the adverb meaning fast and the imperative verb meaning stay anchor their dialogue. Until next time!'
CLOSING = ('denis', 'Всего хорошего!')
STORY = [
    ('denis', 'Я выиграл счастливый билет.', 'I won a lucky ticket.', [(1, 'я выиграл счастливый билет')], 'adapted'),
    ('denis', 'Когда зарождаются новые отношения?', 'When do new relationships begin?', [(3, 'Когда зарождаются отношения')], 'adapted'),
    ('denis', 'Тогда вспыхивает яркое пламя.', 'Then a bright flame flares up.', [(4, 'вспыхивает яркое пламя')], 'adapted'),
    ('denis', 'Со временем пламя может потухнуть.', 'Over time a flame can go out.', [(5, 'со временем любое пламя может потухнуть')], 'adapted'),
    ('denis', 'Но достаточно только одной искры.', 'But just one spark is enough.', [(6, 'достаточно одной искры')], 'adapted'),
    ('denis', 'Ты сегодня опять убегаешь?', 'Are you running away again today?', [(7, 'Опять убегаешь')], 'adapted'),
    ('katya', 'Нет, я не убегаю.', 'No, I am not running away.', [(8, 'Нет')], 'adapted'),
    ('katya', 'Просто всё так быстро происходит.', 'Everything is just happening so fast.', [(9, 'просто все как-то так быстро происходит')], 'adapted'),
    ('denis', 'Тебе со мной сейчас плохо?', 'Do you feel bad with me right now?', [], 'new'),
    ('katya', 'Мне с тобой очень хорошо.', 'I feel very good with you.', [], 'new'),
    ('denis', 'Катя, я тебя прошу, останься.', 'Katya, I beg you, stay.', [(10, 'Катя, я тебя прошу, останься')], ''),
    ('katya', 'Ладно, я ещё немного побуду.', 'All right, I will stay a little longer.', [], 'new'),
]
WALK = [
    (0, None, "'I won a lucky ticket.' Mentioning that he won a lucky ticket moves the talk in a new direction."),
    (1, None, '\'When do new relationships begin?\' By asking when new relationships begin, Denis presses Katya for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, "'Then a bright flame flares up.' With the moment and ticket in play, Denis keeps this short reply brisk and direct."),
    (3, None, "'Over time a flame can go out.' Explaining that over time a flame can go out lays the cards on the table for Katya."),
    (4, None, "'But just one spark is enough.' Denis mentions that just one spark is enough so Katya sees what is at stake."),
    (5, None, '\'Are you running away again today?\' By checking whether Katya running away again today, Denis presses Katya for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (6, None, "'No, I am not running away.' Mentioning that she is not running away moves the talk in a new direction."),
    (7, None, "'Everything is just happening so fast.' Katya explains that everything is just happening so fast, keeping her voice calm and direct."),
    (8, None, '\'Do you feel bad with me right now?\' Here checking whether Katya feels bad with him right now shows Denis looking for the real truth. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, "'I feel very good with you.' Feeling very good with Denis is how Katya lays out the situation for Denis."),
    (10, None, '\'Katya, I beg you, stay.\' Admitting that he begs Katya stays shows Denis being honest for a change. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, "'All right, I will stay a little longer.' Realizing that all right she will stay a little longer changes how Katya handles the situation."),
]
