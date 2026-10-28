# Authoring module for kukhnya-s02e03-scene-04.
ID = 'kukhnya-s02e03-scene-04'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 4
TITLE = 'Надрыв связок  (A Torn Ligament)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'doctor': 'Врач'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = 'Chef Viktor is at the hospital after being hit by a car. The doctor examines his leg, but Viktor makes up a story to protect the person who hit him.'
OPENER = "Let's listen to their conversation."
TRANSITION = "Now let's hear the whole thing once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around a torn ligament, and for the words meaning 'strain' and 'ligament'. You'll catch them now. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('doctor', 'У вас надрыв связок.', 'You have a partial ligament tear.', [(42, 'Надрыв связок.')], ''),
    ('doctor', 'Это не очень страшно.', "It's not too serious.", [(43, 'Это не очень страшно.')], ''),
    ('doctor', 'Не нагружайте ногу.', 'Keep your weight off that leg.', [(44, 'Не нагружайте ногу.')], ''),
    ('barinov', 'Спасибо.', 'Thank you.', [(46, 'Спасибо.')], ''),
    ('doctor', 'Какая причина вашей травмы?', 'What is the cause of your injury?', [(46, 'Мы должны записать причину вашей травмы.')], ''),
    ('barinov', 'Я попал под машину.', 'I got hit by a car.', [(48, 'попал под машину.')], ''),
    ('doctor', 'Будете заявлять в полицию?', 'Will you report to the police?', [(50, 'Будете заявлять в полицию?')], ''),
    ('barinov', 'Нет.', 'No.', [(50, 'Нет.')], ''),
    ('barinov', 'Я забыл поставить машину на ручник.', 'I forgot to put the car on handbrake.', [(51, 'Я забыл поставить на ручник свою машину.')], ''),
    ('barinov', 'И она на меня наехала.', 'And it ran over me.', [(52, 'И она на меня наехала.')], ''),
    ('doctor', 'Понятно.', 'I see.', [], ''),
    ('barinov', 'Заявлять не буду.', 'I will not report it.', [(53, 'Заявлять не будет.')], ''),
]
WALK = [
    (0, None, "'You have a partial ligament tear.' After examining Viktor's leg at the hospital, the doctor diagnoses a partial ligament tear."),
    (1, None, "'It's not too serious.' He reassures the chef that the injury is not too serious."),
    (2, None, "'Keep your weight off that leg.' Still, the doctor warns Viktor to keep his weight off that leg while it heals."),
    (3, None, "'Thank you.' Barinov thanks the doctor for the exam."),
    (4, None, "'What is the cause of your injury?' Filling out his report, the doctor asks how the injury happened. Chef Viktor answers straight away."),
    (5, None, "'I got hit by a car.' Viktor admits that he got hit by a car."),
    (6, None, "'Will you report to the police?' Filling out the hospital report, the doctor asks whether Viktor plans to file a complaint with the police."),
    (7, None, "'No.' When asked if he will file a police report against the driver, Viktor says no."),
    (8, None, "'I forgot to put the car on handbrake.' To protect Elena from losing her license, Viktor makes up a story about forgetting his own handbrake."),
    (9, None, "'And it ran over me.' He claims his own parked car rolled forward and bumped into him."),
    (10, None, "'I see.' The doctor nods and takes down the excuse without pressing further. And Chef Viktor jumps in."),
    (11, None, "'I will not report it.' Viktor repeats firmly that he will not be reporting the accident."),
]
