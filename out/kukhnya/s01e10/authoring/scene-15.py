# Authoring module for kukhnya-s01e10-scene-15.
ID = 'kukhnya-s01e10-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 15
TITLE = 'Ставка против своих  (A Bet Against His Own)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'tamara': 'Тамара'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "In his private office at Claude Monet, Chef Viktor Barinov desperately needs a quick financial windfall to pay off debts. Calling bookmaker Tamara, he shocks her by placing a massive hundred-thousand-ruble wager on CSKA to beat his lifelong beloved club Spartak. Let's listen to their phone call in Russian first."
OPENER = "Let's examine how Chef Barinov places a risky sports bet over the telephone line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Now you know how to talk about sports wagers, financial risks, and moral compromises in Russian. See you next time!'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Тамара, здравствуй, это Витя Баринов беспокоит.', 'Tamara, hello, this is Vitya Barinov calling.', [(131, 'Тамарочка, здравствуй'), (132, 'Это Витя Баринов тебя беспокоит')], ''),
    ('tamara', 'Привет, Витя, ты хочешь сделать ставку?', 'Hi, Vitya, do you want to place a bet?', [], ''),
    ('barinov', 'Да, поставь деньги на матч Спартака.', 'Yes, put money on the Spartak match.', [(133, 'А я хотел сделать ставочку на Спартак ЦСКА')], ''),
    ('tamara', 'Ты ставишь на победу родного Спартака?', "Are you betting on your native Spartak's victory?", [], ''),
    ('barinov', 'Нет, я ставлю на победу ЦСКА!', 'No, I am betting on a CSKA victory!', [(134, 'Не-не, на победу ЦСКА'), (135, 'ЦСКА')], ''),
    ('tamara', 'Ты не шутишь? Это же твои враги!', 'Are you not joking? They are your enemies!', [], ''),
    ('barinov', 'Я ставлю ровно сто тысяч рублей!', 'I bet exactly one hundred thousand rubles!', [(136, 'Сто тысяч')], ''),
    ('tamara', 'У тебя есть с собой такие деньги?', 'Do you have that kind of money with you?', [], ''),
    ('barinov', 'Зарезервируй ставку, я скоро привезу наличные.', 'Reserve the bet, I will bring cash soon.', [(137, 'Ты зарезервируй за мной ставочку, а я по почте денежку завезу')], ''),
    ('tamara', 'Хорошо, твоя ставка принята в конторе.', 'All right, your bet is accepted at the office.', [], ''),
    ('barinov', 'Спасибо, деньги сейчас для меня важнее всего.', 'Thank you, money right now matters more than anything to me.', [(138, 'спасибо')], ''),
    ('tamara', 'Надеюсь, ты понимаешь свой огромный риск.', 'I hope you understand your huge risk.', [], ''),
]
WALK = [
    (0, None, "'Tamara, hello, this is Vitya Barinov calling.' The chef opens the phone call using a polite greeting and a third person identifier."),
    (1, None, "'Hi, Vitya, do you want to place a bet?' Tamara greets 'Vitya' at the betting office."),
    (2, None, "'Yes, put money on the Spartak match.' Barinov wants to gamble on 'Spartak'."),
    (3, None, "'Are you betting on your native Spartak's victory?' Tamara asks if he backs his favorite."),
    (4, None, "'No, I am betting on a CSKA victory!' The chef drops a bombshell by wagering on his bitter rival team."),
    (5, None, "'Are you not joking? They are your enemies!' Tamara is shocked he bets against them."),
    (6, None, "'I bet exactly one hundred thousand rubles!' Barinov confirms his massive wager."),
    (7, None, "'Do you have that kind of money with you?' Tamara asks if he has cash ready."),
    (8, None, "'Reserve the bet, I will bring cash soon.' Barinov promises to bring the cash soon."),
    (9, None, "'All right, your bet is accepted at the office.' Tamara accepts the reservation for him."),
    (10, None, "'Thank you, money right now matters more than anything to me.' Barinov admits cash is his priority now."),
    (11, None, "'I hope you understand your huge risk.' The bookmaker concludes the conversation with a cautionary statement."),
]
