# Authoring module for kukhnya-s05e17-scene-04.
ID = 'kukhnya-s05e17-scene-04'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 17
SCENE = 4
TITLE = 'Ложные схватки и важный гость  (False Contractions and an Important Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.17'
SOURCE_FILE = 'sources/kukhnya/s05/e17.ru.srt'
INTRO = 'In the dining room, Vika meets with influential official Nikolai Maryanovich to arrange a last-minute birthday banquet. Max interrupts them, furious that Vika did not tell him her contractions were false.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right after Max snaps at the VIP guest, Vika's real contractions start on the dining room floor. See you next time!"
CLOSING = ('vika', 'Хорошего дня!')
STORY = [
    ('guest', 'Я хочу закрыть ресторан на спецобслуживание.', 'I want to close the restaurant for a private event.', [(52, 'я хочу в ресторан на спецобслуживание закрыть')], 'adapted'),
    ('guest', 'Свой день рождения буду отмечать.', 'I will be celebrating my birthday.', [(53, 'День рождения буду отмечать')], 'adapted'),
    ('vika', 'Конечно, а когда именно?', 'Of course, and when exactly?', [(54, 'Конечно, когда')], 'adapted'),
    ('guest', 'Ну, сегодня или завтра вечером.', 'Well, tonight or tomorrow evening.', [(54, 'сегодня или завтра')], 'adapted'),
    ('vika', 'Аренда ресторана заранее обговаривается.', 'Renting the restaurant is arranged in advance.', [(57, 'аренда ресторана'), (58, 'Заранее обговаривается')], 'adapted'),
    ('max', 'Вика, можно тебя на минуту?', 'Vika, can I have a word with you?', [(59, 'можно тебя')], 'adapted'),
    ('vika', 'Подожди, я сейчас разговариваю.', 'Wait, I am talking right now.', [(59, 'Я разговариваю')], 'adapted'),
    ('max', 'А почему ты не в роддоме?', 'And why are you not at the maternity hospital?', [(61, 'А почему ты не в роддоме')], 'adapted'),
    ('vika', 'Утренние схватки оказались ложными.', 'The morning contractions turned out to be false.', [(63, 'Схватки оказались ложными')], 'adapted'),
    ('vika', 'Меня врачи домой отпустили.', 'The doctors let me go home.', [(63, 'Меня домой отпустили')], 'adapted'),
    ('max', 'А позвонить мне нельзя было?', 'Could you not have called me?', [(64, 'А позвонить нельзя было')], 'adapted'),
    ('guest', 'Юноша, подождите, пока мы закончим.', 'Young man, wait until we finish.', [(65, 'пока мы закончим')], 'adapted'),
    ('max', 'Я просто поговорю с женой!', 'I will just talk to my wife!', [(66, 'а я поговорю с женой')], 'adapted'),
]
WALK = [
    (0, None, '\'I want to close the restaurant for a private event.\' Mentioning the service in the exchange, the guest chooses "spetsobsluzhivaniye" ("private event service") so Vika gets the point right away.'),
    (1, None, '\'I will be celebrating my birthday.\' Underscoring the birth beside Vika, the guest leans on "rozhdeniya" ("of birth", a form of "rozhdeniye") to give the remark its edge.'),
    (2, None, '\'Of course, and when exactly?\' Vika readily delivers this confirmation to the guest using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (3, None, '\'Well, tonight or tomorrow evening.\' The guest responds firmly around Vika and leans on "segodnya" ("today") to give the whole sentence its punch.'),
    (4, None, '\'Renting the restaurant is arranged in advance.\' Bringing up the rental with the guest, the "-sya" ending on "obgovarivayetsya" ("is arranged") marks an action that unfolds mutually or turns back on the speaker.'),
    (5, None, "'Vika, can I have a word with you?' Max prompts quietly about what Vika just brought up."),
    (6, None, '\'Wait, I am talking right now.\' Vika follows up dryly during the talk and leans on "razgovarivayu" ("to talk, to speak", a form of "razgovarivat") to give the remark its edge.'),
    (7, None, '\'And why are you not at the maternity hospital?\' Returning to the maternity hospital right here, Max links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (8, None, "'The morning contractions turned out to be false.' Vika weighs in sharply around Max, so Max knows she is not just making small talk."),
    (9, None, '\'The doctors let me go home.\' Touching on the doctors in the exchange, Vika puts the weight on "vrachi" ("doctors", from "vrach") as the exchange unfolds.'),
    (10, None, '\'Could you not have called me?\' Pressing on evenly in the exchange, Max leans on "nelzya" ("it is not allowed, one must not"), which carries the whole predicate in Russian without needing "it is".'),
    (11, None, "'Young man, wait until we finish.' The guest speaks up openly on the spot, grounding the moment in plain reality."),
    (12, None, '\'I will just talk to my wife!\' Emphasizing his wife to the guest, Max centers the thought on "pogovoryu" ("I\'ll talk", from "pogovorit") without wasting a word.'),
]
