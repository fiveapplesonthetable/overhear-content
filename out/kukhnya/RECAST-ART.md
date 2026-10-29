# Kukhnya S01: speaker changes

Every S01 scene whose set of speaking characters changed after the role-key migration (commit 2d619127d), compared with the current authoring modules. Names follow `cast.json`. "Merged away" means the scene was folded into the next one. Commits are the ones that changed the scene's speaker set.

## Speaker-set changes

| Episode | Scene | Old speakers | New speakers | Commit(s) |
|---|---|---|---|---|
| s01e05 | 8 | Barinov, Max, Senya | Barinov, Max | 38288d036 |
| s01e06 | 4 | Barinov, Max, Timur | Barinov, Timur | 9fa32b9f5 |
| s01e06 | 16 | Kostya, Max | Max, Rodion | 79f02181e |
| s01e07 | 4 | Fedya, Max, Senya | Fedya, Senya | 9fa32b9f5 |
| s01e07 | 5 | Barinov, Elena, Max | Barinov, Elena | 9fa32b9f5 |
| s01e07 | 6 | Barinov, Max, seller | Barinov, seller | 9fa32b9f5 |
| s01e08 | 5 | Barinov, Max, Nagiyev | Barinov, Nagiyev | 9fa32b9f5 |
| s01e08 | 6 | Barinov, Elena, Max | Barinov, Elena | 9fa32b9f5 |
| s01e08 | 7 | Barinov, Elena, Max | Barinov, Elena | 9fa32b9f5 |
| s01e08 | 13 | Max, Sasha, Vika | Lyova, Max, Vika | content-review-s01 |
| s01e08 | 15 | Max, Sasha | Max, Vika | content-review-s01 |
| s01e10 | 20 | Max, Sasha | Max, Vika | e79c07e82 |
| s01e10 | 26 | Barinov, Max | (merged away) | 3d7975f7d |
| s01e10 | 28 | Barinov, Senya | (merged away) | 3d7975f7d |
| s01e11 | 6 | Barinov, Kostya | Barinov, Kostya, Vika | 9fa32b9f5 |
| s01e14 | 22 | Nagiyev | Barinov, Nagiyev | 9fa32b9f5 629845f94 |
| s01e14 | 25 | Barinov, Nagiyev | Barinov, Lyova, Nagiyev | 363434501 |
| s01e15 | 5 | Max, Nastya | Max, Vika | ece881815 |
| s01e15 | 6 | Kostya, Max | Max, Vika | ece881815 |
| s01e16 | 15 | Barinov, Fedya, inspector | Fedya, Senya, inspector | b67a0698c |
| s01e16 | 18 | Louis, inspector | Fedya, inspector | b67a0698c |
| s01e16 | 19 | Louis, inspector | Fedya, inspector | b67a0698c |
| s01e16 | 21 | Ainura, Barinov | Barinov, Fedya | b67a0698c |
| s01e16 | 22 | Barinov, Max, Nastya | Barinov, Fedya, inspector | b67a0698c |
| s01e16 | 25 | Barinov, Max | Barinov, Fedya, Max | b67a0698c |
| s01e17 | 1 | Barinov, Max | Barinov, Senya, seller | 2049f92ef |
| s01e17 | 2 | Barinov, Max | Barinov, Elena, Senya | 2049f92ef |
| s01e17 | 7 | Max, Nastya, Vika | Kostya, Max, Nastya | 8ffcd5b50 |
| s01e17 | 10 | Fedya, Senya | (merged away) | 2049f92ef |
| s01e17 | 13 | Barinov, Hostess | Barinov, Hostess, Nagiyev | 2049f92ef |
| s01e17 | 21 | Barinov, Max, Vika | Max, Nastya, Vika | 2049f92ef |
| s01e17 | 22 | Barinov, Max, Nastya | (merged away) | 2049f92ef |
| s01e17 | 24 | Kostya, Max | Max | 2049f92ef |
| s01e18 | 9 | Ilya, Kostya, Max | Kostya, Max | da11ce536 |
| s01e18 | 11 | Kostya, Max, Nagiyev | Barinov, Max, Nagiyev | aceaca344 |
| s01e18 | 12 | Barinov, Ilya, Max | Barinov, Max, Nagiyev | da11ce536 |
| s01e19 | 2 | Artyom, Barinov, Fedya | Artyom, Barinov, cook | ff981effe |
| s01e19 | 5 | Guest, Igor, Vika | Igor, Vika | df04a71d3 |
| s01e19 | 6 | Guest, Igor, Vika | Igor, Max, Vika | df04a71d3 |
| s01e19 | 8 | Kostya, Max, Vika | Kostya, Max | df04a71d3 |
| s01e20 | 12 | Barinov, Guest, Vika | Barinov, Kostya, Max | 140a817e0 |
| s01e20 | 15 | Guest, Max, Vika | Max, Vika | 140a817e0 |
| s01e20 | 16 | Max, old man | Max, passerby | 140a817e0 |

## Earlier changes (before the role-key migration)

The pre-migration files used placeholder voice keys (`anya`, `dima`, `chef`), so they are listed by display label.

| Episode | Scene | Old speakers | New speakers | Note |
|---|---|---|---|---|
| s01e15 | 5 | Nastya, Max (keys `anya`/`vika` swapped in 712144c16) | Max, Vika | First fixed to Max/Nastya in 93e3a33a9; recast to Vika in ece881815 (see table above). |
| s01e20 | 19 | Chef, Dima, Eleonora (bc4d9802b) | Barinov, Eleonora, Nagiyev | Dima became Nagiyev in 93e3a33a9; keys settled in 2d619127d; cues 302-304 dropped from the lines in 140a817e0. |

## Lines moved to another speaker within the same set

Only lines whose Russian text is unchanged are listed. Scenes rebuilt from their cues with new lines (s01e17 scenes 9, 12 and 21; s01e18 scenes 14 and 18; s01e20 scene 19) are not repeated here: check their review sheets.

| Episode | Scene | Line | Old | New |
|---|---|---|---|---|
| s01e08 | 29 | Шеф, вы мне должны отличный ужин! | Barinov | Elena |
| s01e13 | 20 | Сказал, что выставка отменяется. | Vika | Nagiyev |
| s01e13 | 22 | В чём дело, Макс? | Max | Vika |
| s01e14 | 13 | Максимилиан, вот вы где. | Nagiyev | Diana |
| s01e14 | 13 | Вы прячетесь от нас. | Nagiyev | Diana |
| s01e14 | 13 | Приготовьте нам маленький шедевр. | Nagiyev | Diana |
| s01e14 | 13 | Мы хотим старинную французскую кухню. | Nagiyev | Diana |
| s01e14 | 13 | Максимилиан, я вас жду. | Nagiyev | Diana |
| s01e14 | 20 | Представляешь, мы жили в Париже. | Nagiyev | Barinov |
| s01e15 | 17 | Привет, Макс. | Max | Vika |
| s01e15 | 17 | Привет. | Vika | Max |
| s01e15 | 19 | Доброе утро. | Mama | Lyova |
| s01e15 | 19 | Это очень вкусно. | Barinov | Lyova |
| s01e16 | 9 | Отлично, люблю французскую кухню. | Elena | inspector |
| s01e16 | 14 | Ничем не смогу вам помочь. | inspector | Barinov |
| s01e16 | 14 | Мои сотрудники потеряли ключ. | inspector | Barinov |
| s01e16 | 14 | Экая досада. | Barinov | inspector |
| s01e16 | 14 | У меня есть запасной ключ. | Barinov | inspector |
| s01e16 | 14 | Я всегда дубликаты храню. | Barinov | inspector |
| s01e11 | 20 | Ты в своём уме? (now «Витя, ты в своём уме?») | Barinov | Vika |
| s01e17 | 12 | Очень неплохо. Спасибо. | Nagiyev | Senya |
| s01e17 | 20 | Это твоя вечеринка? | Vika | Nastya |
| s01e18 | 10 | Но мне это совсем не помогло. | Fedya | Senya |
| s01e18 | 10 | Если выживу, воровать продукты перестану! | Fedya | Senya |
| s01e19 | 1 | Разбудил? | Vika | Max |
| s01e19 | 3 | Что ты здесь делаешь? | Max | Kostya |
| s01e19 | 3 | Что не на работе? | Max | Kostya |
| s01e19 | 3 | Опять допрос. | Kostya | Max |
| s01e19 | 3 | Вы сговорились что ли? | Kostya | Max |
| s01e19 | 3 | Она все усложнять начала. | Kostya | Max |
| s01e19 | 7 | В общем, это тебе. | Vika | Max |
| s01e19 | 7 | Тогда это вам, распишитесь вот здесь. | Vika | Guest |
| s01e19 | 21 | Почему? | Vika | Max |
| s01e19 | 22 | Здесь и сейчас. | Vika | Max |
| s01e20 | 2 | Мы же не торопимся подниматься? | Kostya | Nastya |
| s01e20 | 19 | О, смотри, кто пришёл. Здравствуйте. | Nagiyev | Barinov |
