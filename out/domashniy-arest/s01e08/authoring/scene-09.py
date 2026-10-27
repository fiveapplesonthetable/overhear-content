ID = "domashniy-arest-s01e08-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 9
TITLE = "Сон Самсонова  (Samsonov's Dream)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "soldier": "anja"}
LABELS = {"anya": "Иван", "soldier": "Солдат"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 135-142. Ivan's feverish dream sequence on a WWII battlefield. "
    "He crawls through the mud as the famous wartime song 'Последний бой' echoes in his mind."
)

INTRO = (
    "Welcome back to Domashniy Arest! Deeply wounded by the slanderous smear campaign accusing "
    "his grandfather of being a Nazi collaborator, Ivan Samsonov has disappeared on a drinking binge. "
    "In his troubled sleep, he experiences a feverish wartime dream where he crawls across a foggy "
    "battlefield, accompanied by the famous Soviet song 'The Final Battle'. Let's listen to the scene in Russian first."
)

STORY = [
    ("anya", "Где мы? Кругом дым и воронки.",
     "Where are we? Smoke and bomb craters are all around.",
     [], ""),
    ("soldier", "Ползи вперёд! Мы почти дошли.",
     "Crawl forward! We have almost arrived.",
     [(136, "по-пластунски отпахали")], ""),
    ("anya", "Мы ползём по грязи так долго!",
     "We have been crawling through mud for so long!",
     [(136, "по-пластунски")], ""),
    ("soldier", "Завтра нас ждёт последний бой.",
     "Tomorrow the final battle awaits us.",
     [(137, "завтра, наконец, последний бой")], ""),
    ("anya", "Ещё немного, ещё чуть-чуть!",
     "Just a little more, just a little bit!",
     [(138, "Еще немного, а еще чуть-чуть")], ""),
    ("soldier", "Этот бой будет самый трудный.",
     "This battle will be the hardest one.",
     [(139, "Последний бой, он трудный самый")], ""),
    ("anya", "Мой дедушка не был предателем!",
     "My grandfather was not a traitor!",
     [], ""),
    ("soldier", "Все знают правду. Держись, боец!",
     "Everyone knows the truth. Hold on, soldier!",
     [], ""),
    ("anya", "А я домой в Россию хочу.",
     "And I want to go home to Russia.",
     [(140, "А я в Россию домой хочу")], ""),
    ("soldier", "Скоро мы вернёмся домой.",
     "Soon we will return home.",
     [], ""),
    ("anya", "Я так давно не видел маму.",
     "I haven't seen my mother in so long.",
     [(141, "Так давно не видел маму")], ""),
    ("soldier", "Мама ждёт тебя живым.",
     "Mother is waiting for you alive.",
     [], ""),
    ("anya", "Я не предам родную землю!",
     "I will not betray my native land!",
     [], ""),
    ("soldier", "Тогда просыпайся, Иван! Тебе пора.",
     "Then wake up, Ivan! It is time for you.",
     [], ""),
]

OPENER = (
    "Now let's examine Ivan's dramatic wartime dream sequence line by line. "
    "The lines weave together iconic lyrics from the famous song with Ivan's inner torment over his grandfather's reputation."
)

WALK = [
    (0, None,
     "'Where are we? Smoke and bomb craters are all around.' Ivan looks around in confusion at the foggy war landscape."),
    (1, None,
     "'Crawl forward! We have almost arrived.' The fellow soldier urges him to keep moving through the mud."),
    (2, None,
     "'We have been crawling through mud for so long!' Ivan struggles forward on his elbows across the battlefield."),
    (3, None,
     "'Tomorrow the final battle awaits us.' The phrase echoes the iconic Soviet wartime song of the same name."),
    (4, None,
     "'Just a little more, just a little bit!' This famous lyric conveys exhaustion and desperate hope."),
    (5, None,
     "'This battle will be the hardest one.' The superlative adjective highlights the ultimate sacrifice required."),
    (6, None,
     "'My grandfather was not a traitor!' Even in his feverish nightmare, Ivan defends his family honor."),
    (7, None,
     "'Everyone knows the truth. Hold on, soldier!' The comrade soldier offers reassurance and encouragement."),
    (8, None,
     "'And I want to go home to Russia.' The accusative directional noun expresses deep homesickness."),
    (9, None,
     "'Soon we will return home.' The perfective verb indicates an eventual successful homecoming."),
    (10, None,
     "'I haven't seen my mother in so long.' The accusative noun refers affectionately to his mother."),
    (11, None,
     "'Mother is waiting for you alive.' The short adjective agrees in gender and case with the pronoun."),
    (12, None,
     "'I will not betray my native land!' Ivan affirms his steadfast loyalty to his motherland."),
    (13, None,
     "'Then wake up, Ivan! It is time for you.' The dream begins to dissolve as reality calls him back."),
]

TRANSITION = "Now let's listen to Ivan's dream sequence once more in Russian."

OUTRO = (
    "Ivan's dream reflects the heavy burden of wartime memory and patriotism in modern Russian life. "
    "Next, morning arrives and Ivan wakes up with a terrible hangover on a dive bar table; see you there!"
)

CLOSING = ("soldier", "Тогда просыпайся, Иван! Тебе пора.")
