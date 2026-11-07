# Authoring module for dvorik-u-mosta-s02e02-scene-04.
ID = 'dvorik-u-mosta-s02e02-scene-04'
SHOW = 'dvorik-u-mosta'
SEASON = 2
EPISODE = 2
SCENE = 4
TITLE = 'Четверг значит сегодня?  (Thursday Means Today?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'yaroslav': 'Ярослав', 'matvey': 'Матвей'}
INTRO = 'Back at the Bridge Courtyard Inn, Matvey is stripping clean copper wire on a stool when Yaroslav strolls up to the front desk, beaming with pride over his telephone bargain. Listen first.'
OPENER = "Let's slow down and replay the front desk conversation line by line."
TRANSITION = 'Now listen to the whole front desk scene again, start to finish.'
OUTRO = 'Without his glasses, Yaroslav ordered twenty-four chairs for Saturday afternoon instead of Thursday, and the delivery van is already at the gate! See you next time.'
CLOSING = ('matvey', 'До встречи!')
STORY = [
    ('yaroslav', 'Поздравь меня, Матвей! Я нашёл складные деревянные стулья за полцены!', 'Congratulate me, Matvey! I found folding wooden chairs at half price!'),
    ('matvey', 'За полцены? Шеф, почему мне уже страшно?', 'At half price? Boss, why am I already scared?'),
    ('yaroslav', 'Потому что такая цена, только если заказать сразу две дюжины!', 'Because that price is only if you order two dozen at once!'),
    ('matvey', 'Две дюжины?! Ярослав Ильич, это двадцать четыре стула!', 'Two dozen?! Yaroslav Ilyich, that is twenty-four chairs!'),
    ('yaroslav', 'Двенадцать в девятый номер, восемь во дворик и четыре... на всякий случай!', 'Twelve for room nine, eight for the courtyard and four... just in case!'),
    ('matvey', 'А где мы будем хранить двадцать четыре стула, пока красим всю неделю?', 'And where will we keep twenty-four chairs while we paint all week?'),
    ('yaroslav', 'Спокойно! Я сказал водителю привезти их в следующий четверг.', 'Relax! I told the driver to bring them next Thursday.'),
    ('matvey', 'Подождите... а кто это подъехал к нашим воротам на фургоне?', 'Wait... who just drove up to our gate in a van?'),
    ('yaroslav', 'Синий фургон? Почему на нём написано «садовые стулья»?!', 'A blue van? Why does it say "garden chairs" on it?!'),
    ('matvey', 'Дайте блокнот... шеф, вы обвели «суббота, два часа»!', 'Give me the notepad... boss, you circled "Saturday, two o\'clock"!'),
    ('yaroslav', 'Без очков я прочитал не ту строчку! Они уже разгружают!', 'Without my glasses I read the wrong line! They are already unloading!'),
    ('matvey', 'Двадцать четыре стула в нашем узком дворике — прекрасно, шеф!', 'Twenty-four chairs in our narrow courtyard — wonderful, boss!'),
]
WALK = [
    (0, None, ["'Congratulate me, Matvey! I found folding wooden chairs at half price!' Yaroslav glows with pride. A bargain sounds like ", (None, 'за полцены!'), ", 'for half a price', with half and price glued into one short word."]),
    (1, None, ["'At half price? Boss, why am I already scared?' Fear in Russian happens to you: ", (None, 'мне уже страшно?'), " is literally 'to me it is already scary'."]),
    (2, None, ["'Because that price is only if you order two dozen at once!' Yaroslav's small word ", (None, 'сразу'), " means 'at once, in one go', and it pops up whenever things happen all together."]),
    (3, None, ["'Two dozen?! Yaroslav Ilyich, that is twenty-four chairs!' Matvey switches from 'boss' to the full name and patronymic, the way you sound when you are truly alarmed. ", (None, 'двадцать четыре стула!'), " keeps 'chair' singular after the four, a Russian counting quirk."]),
    (4, None, ["'Twelve for room nine, eight for the courtyard and four... just in case!' A phrase worth stealing: ", (None, 'на всякий случай!'), " means 'just in case', literally 'for any occasion'."]),
    (5, None, ["'And where will we keep twenty-four chairs while we paint all week?' For storing things Russian uses ", (None, 'хранить'), ", the same verb as keeping a secret or keeping old letters safe."]),
    (6, None, ["'Relax! I told the driver to bring them next Thursday.' Yaroslav waves the worry away with ", (None, 'Спокойно!'), ", literally 'calmly!', the Russian way to say 'relax'."]),
    (7, None, ["'Wait... who just drove up to our gate in a van?' Russian gates are a plural-only word, so 'our gate' comes out as ", (None, 'к нашим воротам'), ", literally 'to our gates'."]),
    (8, None, ["'A blue van? Why does it say \"garden chairs\" on it?!' To report writing on a sign or a van, Russians say ", (None, 'написано'), ", 'it is written', with nobody doing the writing."]),
    (9, None, ["'Give me the notepad... boss, you circled \"Saturday, two o'clock\"!' Matvey is polite but blunt. His ", (None, 'вы обвели'), " means 'you circled', from a verb for drawing a line around something."]),
    (10, None, ["'Without my glasses I read the wrong line! They are already unloading!' For 'the wrong one' Russian simply says 'not that one': ", (None, 'не ту строчку!'), " — 'not that line'."]),
    (11, None, ["'Twenty-four chairs in our narrow courtyard — wonderful, boss!' That ", (None, 'прекрасно, шеф!'), " is pure sarcasm. Matvey praises the disaster in the same warm voice he would use for good news."]),
]
