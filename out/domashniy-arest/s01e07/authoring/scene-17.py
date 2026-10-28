# Authoring module for domashniy-arest-s01e07-scene-17.
ID = 'domashniy-arest-s01e07-scene-17'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 7
SCENE = 17
TITLE = 'Мы телохранители, а не телоломатели  (Bodyguards, Not Body-Breakers)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'pasha': 'Паша', 'vitalik': 'Виталик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.07'
SOURCE_FILE = 'sources/domashniy-arest/s01/e07.ru.dual.srt'
INTRO = "Last night, Arkady banged on Marina's wall to ruin Eduard's date while Samsonov phoned lawyer Danya to invite him over for fondue. The next morning at City Hall, acting mayor Pasha Osipenko calls in his two bodyguards and orders them to stage an attack on his rival Samsonov. Listen to the Russian conversation first, and don't worry about catching every word."
OPENER = "Did you hear why the bodyguards hesitated at first? Let's walk through Pasha's order line by line."
TRANSITION = "Now let's listen to the whole conversation in the mayor's office again."
OUTRO = "So much for the bodyguards' Buddhist principles: as soon as Pasha threatens their generous salary and free food, the two Vitaliks agree to ambush Samsonov. See you next time!"
CLOSING = ('vitalik', 'Пока!')
STORY = [
    ('pasha', 'У меня для вас есть серьёзное задание. Я же могу вам доверять?', 'I have a serious assignment for you. I can trust you, right?', [(652, 'У меня для вас есть серьезное задание'), (653, 'Я же могу вам доверять')], ''),
    ('pasha', 'Как вы знаете, Виталий, я участвую в выборах.', 'As you know, Vitaly, I am taking part in the election.', [(654, 'Как вы знаете, Виталий, я участвую в выборах')], ''),
    ('pasha', 'И у меня есть один конкурент. Я говорю о Самсонове, конечно.', 'And I have one competitor. I am talking about Samsonov, of course.', [(655, 'И у меня есть один конкурент'), (656, 'Я говорю о Самсонове, конечно')], ''),
    ('pasha', 'А жизнь — сложная штука. Вы понимаете, о чём я?', 'And life is a complicated thing. Do you understand what I am talking about?', [(657, 'А жизнь'), (657, 'штука'), (659, 'Вы понимаете, о чем я')], ''),
    ('pasha', 'Вот человек выбирается в мэры. Тот же Самсонов, например.', 'Say a man is running for mayor. That same Samsonov, for example.', [(660, 'человек выбирается в мэры'), (661, 'тот же Самсонов, например')], ''),
    ('pasha', 'И какие-то хулиганы вдруг напали на него. Не сильно, но человеку плохо.', 'And some hooligans suddenly attacked him. Not badly, of course, but the man feels unwell.', [(662, 'И какие-то хулиганы вдруг'), (663, 'Не сильно'), (663, 'но человеку плохо')], "'проломили голову' (662, 666) softened to 'напали на него'"),
    ('pasha', 'И выбираться он уже не может. Так, понятно?', 'And he cannot run for office anymore. So, is that clear?', [(664, 'И выбираться он уже'), (664, 'не может'), (665, 'Так, понятно')], ''),
    ('vitalik', 'Павел Юрьевич, мы против!', 'Pavel Yuryevich, we are against this!', [(667, 'Павел Юрьевич, мы против')], ''),
    ('vitalik', 'Мы же телохранители, а не телоломатели.', 'We are bodyguards, not body-breakers.', [(668, 'Мы же телохранители, а не телоломатели')], ''),
    ('pasha', 'А у Аникеева чем вы занимались, интересно?', 'And what were you doing for Anikeyev, I wonder?', [(669, 'чем вы занимались, интересно')], "ASR 'Никеева' -> 'Аникеева'"),
    ('vitalik', 'Одно дело в караоке руку сломать. Другое — обидеть человека.', 'Breaking an arm at karaoke is one thing. And hurting a person for life is another.', [(670, 'Одно дело в караоке руку'), (670, 'сломать'), (671, 'на всю жизнь')], "'покалечить' (671) softened to 'обидеть'"),
    ('vitalik', 'Поверьте, вам это не надо. Вы так карму портите.', 'Believe us, you do not need this. You ruin your karma that way.', [(672, 'вам это не надо'), (673, 'карму портите')], ''),
    ('pasha', 'Послушайте меня внимательно, философы! Я вам отдал приказ!', 'Listen to me carefully, you philosophers! I gave you an order!', [(674, 'послушайте меня внимательно'), (676, 'Я вам отдал приказ')], "crude 'буддистовы хреновы' (674) -> 'философы'"),
    ('pasha', 'Если не можете работать, уходите! Ищите себе другое место с хорошей зарплатой!', 'If you cannot do the job, leave! And find yourselves another job with a good salary!', [(677, 'не можете работать'), (678, 'ищите себе другое место')], "crude 'пошли к чертовой матери' / 'вас хрен догонишь' / 'Зажрались' (677-680) cleaned"),
    ('vitalik', 'Хорошо, мы всё сделаем.', 'Fine, we will do everything.', [(681, 'Хорошо, мы все сделаем')], ''),
    ('pasha', 'Я надеюсь. Идите, действуйте быстрее!', 'I hope so. Go on, act quickly!', [(682, 'Я надеюсь'), (682, 'действуйте')], "slang 'шевелите булками' (682) -> 'действуйте быстрее'"),
]
WALK = [
    (0, 'У меня для вас есть серьёзное задание.', "In the mayor's office, Pasha addresses his two bodyguards: 'I have a serious assignment for you.'"),
    (0, 'Я же могу вам доверять?', "'I can trust you, right?' Notice the 'to me/you' pronoun after the verb for trusting."),
    (1, None, "'As you know, Vitaly, I am taking part in the election,' Pasha continues."),
    (2, 'И у меня есть один конкурент.', "'And I have one competitor.' Pasha centres the line on the verb for 'there is' alongside the noun for 'competitor'."),
    (2, 'Я говорю о Самсонове, конечно.', "'I am talking about Samsonov, of course.' Pasha quickly clarifies that he is talking about their rival Samsonov, of course."),
    (3, 'А жизнь — сложная штука.', "'And life is a complicated thing,' Pasha hints darkly."),
    (3, 'Вы понимаете, о чём я?', "'Do you understand what I am talking about?' There is no question word here — in Russian, rising intonation on 'I' is enough to make it a question."),
    (4, 'Вот человек выбирается в мэры.', "'Say a man is running for mayor,' Pasha explains."),
    (4, 'Тот же Самсонов, например.', "'That same Samsonov, for example.' Looking for a scapegoat, he points to that very same Samsonov as an example."),
    (5, 'И какие-то хулиганы вдруг напали на него.', "'And some hooligans suddenly attacked him.' The verb meaning 'attacked' works together with 'hooligans' to carry the point."),
    (5, 'Не сильно, но человеку плохо.', "'Not badly, of course, but the man feels unwell.' He tries to soften the blow: not badly, of course, just enough that the man feels unwell."),
    (6, 'И выбираться он уже не может.', "'And he cannot run for office anymore.' The self-action verb form on the verb for 'to run for office' turns the action back onto the subject."),
    (6, 'Так, понятно?', "'So, is that clear?' Pasha asks pointedly."),
    (7, None, "To Pasha's surprise, the bodyguard objects: 'Pavel Yuryevich, we are against this!'"),
    (8, None, "'We are bodyguards, not body-breakers!' Vitalik says, coining a funny opposite word from the roots for body, guard, and break."),
    (9, None, "'And what were you doing for Anikeyev, I wonder?' Pasha asks sarcastically."),
    (10, 'Одно дело в караоке руку сломать.', "'Breaking an arm at karaoke is one thing,' Vitalik explains."),
    (10, 'Другое — обидеть человека.', "'Hurting a person for life is another.' Vitalik puts 'another' up front and finishes with 'life' to make the point unmistakable."),
    (11, 'Поверьте, вам это не надо.', "'Believe us, you do not need this.' The bodyguard adds a quiet warning."),
    (11, 'Вы так карму портите.', "'You ruin your karma that way.' Vitalik uses the adverb for 'that way' right alongside the verb meaning 'ruin'."),
    (12, 'Послушайте меня внимательно, философы!', "Pasha loses his temper: 'Listen to me carefully, you philosophers!'"),
    (12, 'Я вам отдал приказ!', "'I gave you an order!' Losing his patience, Pasha barks that he gave them a direct order!"),
    (13, 'Если не можете работать, уходите!', "'If you cannot do the job, leave!' He snaps at his guards in frustration."),
    (13, 'Ищите себе другое место с хорошей зарплатой!', "'Find yourselves another place with a good salary!' He threatens to fire them on the spot: they can go find another job with a good salary!"),
    (14, None, "Faced with losing their perks, the bodyguards fold immediately: 'Fine, we will do everything.'"),
    (15, 'Я надеюсь.', "'I hope so,' Pasha replies."),
    (15, 'Идите, действуйте быстрее!', "'Go on, act quickly!' He orders them out of his office."),
]
