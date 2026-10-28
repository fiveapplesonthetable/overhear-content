# Authoring module for kukhnya-s01e19-scene-05.
ID = 'kukhnya-s01e19-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 5
TITLE = "Прощание  (Saying Goodbye)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'igor': 'Игорь', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = 'The tour is over, and Igor is saying goodbye to Vika, very politely. Listen to the Russian first; the formal tone matters more than any single word.'
OPENER = 'Now the goodbyes, one at a time.'
TRANSITION = 'Hear the polite farewell once more, from the top.'
OUTRO = "Formal Russian runs long, but you've now heard its key pieces: vy, priyatno and do svidaniya. See you next time!"
CLOSING = ('igor', 'Всего хорошего!')
STORY = [
    ('igor', 'Виктория Сергеевна, спасибо за экскурсию.', 'Viktoria Sergeyevna, thank you for the tour.', [(116, 'Виктория Сергеевна')], ''),
    ('vika', 'Пожалуйста, мы всегда рады гостям.', 'You are welcome, we are always glad to have guests.', [], ''),
    ('igor', 'У вас очень красивый и уютный ресторан.', 'You have a very beautiful and cozy restaurant.', [], ''),
    ('vika', 'Спасибо, мы очень стараемся каждый день.', 'Thank you, we try very hard every day.', [], ''),
    ('vika', 'И кухня здесь действительно прекрасная.', 'And the cuisine here is truly wonderful.', [], ''),
    ('vika', 'Наш шеф-повар знает своё дело.', 'Our head chef knows his craft.', [], ''),
    ('igor', 'Мне было крайне приятно с вами познакомиться.', 'It was a great pleasure meeting you.', [(116, 'мне было крайне приятно с вами познакомиться')], ''),
    ('vika', 'Взаимно, мне тоже было очень приятно.', 'Likewise, it was very pleasant for me too.', [(117, 'Взаимно')], ''),
    ('igor', 'Надеюсь, мы скоро увидимся снова.', 'I hope we will see each other again soon.', [], ''),
    ('vika', 'Будем ждать вас в нашем ресторане.', 'We will be waiting for you in our restaurant.', [], ''),
    ('vika', 'До свидания.', 'Goodbye.', [(117, 'До свидания')], ''),
    ('igor', 'Приятного вечера, Виктория Сергеевна.', 'Have a pleasant evening, Victoria Sergeyevna.', [(116, 'Виктория Сергеевна'), (118, 'Приятного вечера')], ''),
]
WALK = [
    (0, None, "'Viktoria Sergeyevna, thank you for the tour.' \"Spasibo\" za is 'thanks for', and za changes \"ekskursiya\" to \"ekskursiyu\". Swap in \"pomoshch'\" and it's 'thanks for the help'."),
    (1, None, "'You're welcome, we're always glad to have guests.' \"Pozhaluysta\" does double duty, 'please' and 'you're welcome'. \"Rady gostyam\" is 'glad to guests': \"gosti\" becomes \"gostyam\"."),
    (2, None, "'You have a very beautiful and cozy restaurant.' \"U vas\", 'at you', is 'you have' for a guest; to a friend it's \"u tebya\". \"Uyutny\", 'cozy', is a word Russians love for homes and cafes."),
    (3, None, "'Thank you, we try very hard every day.' \"Staraemsya\", 'we try hard', always ends in -sya, like \"ulybaemsya\", 'we smile'. \"Kazhdy den'\", 'every day', is a handy chunk to keep."),
    (4, None, "'And the cuisine here is truly wonderful.' \"Deystvitel'no\" means 'really, truly', a longer and more formal word than \"pravda\". \"Prekrasnaya\", 'wonderful', ends in -aya to match \"kukhnya\"."),
    (5, None, "'Our head chef knows his craft.' \"Shef-povar\" is 'head chef': \"shef\" plus \"povar\", 'cook'. \"Znaet svoyo delo\", 'knows his own business', is high praise for anyone good at their job."),
    (6, None, "'It was a great pleasure meeting you.' \"Mne bylo priyatno\" is literally 'to me it was pleasant'. \"Krayne\", 'extremely', is very formal; in everyday talk you'd say \"ochen'\"."),
    (7, None, "'Likewise, it was very pleasant for me too.' \"Vzaimno\", 'mutually', is a one-word polite reply to 'nice to meet you'. She adds \"mne tozhe\", 'me too', to sound warmer."),
    (8, None, "'I hope we'll see each other again soon.' \"Uvidimsya\" means 'we'll see each other', and the -sya carries the 'each other'. On its own it's a casual 'see you'."),
    (9, None, "'We'll be waiting for you at our restaurant.' \"Budem zhdat'\" is 'we will wait', built from \"budem\", 'we will be', and \"zhdat'\". \"V nashem restorane\", 'in our restaurant', shows the -e that comes after \"v\"."),
    (10, None, "'Goodbye.' Do \"svidaniya\" is literally 'until the meeting'. It's the safe goodbye for anyone you call vy."),
    (11, None, "'Have a pleasant evening, Victoria Sergeyevna.' \"Priyatnogo vechera\" is a wish with 'I wish you' left out, which is why the endings are -ogo and -a. \"Priyatnogo appetita\", 'enjoy your meal', works the same way."),
]
