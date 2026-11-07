ID = 'hidamari-ryokan-s02e01-scene-03'
SHOW = 'hidamari-ryokan'
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = 'ガラスとほこり  (Glass and Dust)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'mio': '美央', 'yuka': '由香', 'takashi': '隆'}

INTRO = 'Mio pushes the narrow white door open, and morning light filters through dusty glass panes into a quiet forgotten room. Yuka and Takashi step inside behind her in amazement. Listen to the whole scene first.'

STORY = [
    ('mio', '見てください！中庭の木が見える、高いガラスの窓です！', 'Look! Tall glass windows facing the courtyard tree!'),
    ('yuka', '外の雨戸が閉まっているから、中庭からは誰も気がつかなかったんだね！', 'The shutters outside are closed, so nobody noticed from the courtyard!'),
    ('takashi', '思い出しました！私が十歳のとき、おじはここを「冬のお茶の部屋」と呼んでいました！', "Now I remember! When I was ten, my uncle called this 'the winter tea room'!"),
    ('mio', 'どうしてこんなに明るい部屋を、本棚の後ろに隠したんですか？', 'Why would someone hide such a bright room behind a bookcase?'),
    ('takashi', '昔、雨の春に、ガラスの屋根から水がもれました。直すお金がなかったんです。', 'One rainy spring the glass roof leaked. There was no money to fix it.'),
    ('yuka', 'でも隆さん、床を見て！石の床が乾いている。水は一滴もないよ！', 'But look at the floor, Takashi! The stone floor is dry. Not one drop of water!'),
    ('mio', '昔、中庭の屋根を直した人が、この天井も直したんですね！', 'Whoever fixed the courtyard roof long ago fixed this ceiling too!'),
    ('yuka', '隆さん、ここに小さいカフェのテーブルがいくつ入るか、わかる？', 'Takashi, can you see how many little café tables fit in here?'),
    ('takashi', '待ってください！古い建物を守るために、市に読書カフェを約束しました！', 'Wait! To protect the old building, we promised the city a reading café!'),
    ('mio', '市の手紙に書いてある部屋は、まさにここですね！', "The room in the city's letter is exactly this one!"),
    ('yuka', '温かいパン、熱いお茶、朝の光、冷たい風はゼロ！', 'Warm bread, hot tea, morning light, and zero cold wind!'),
    ('takashi', 'あれ、隅の大きい白い布の下に、何が立っているんですか？', "Wait, what's standing in the corner under that big white cloth?"),
]

OPENER = "Takashi suddenly remembers his childhood, and the room fills with new words. Let's walk through six lines."

WALK = [
    (1, None, ["'The shutters outside are closed, so nobody noticed from the courtyard!' The word for the wooden shutters on old Japanese houses is ", (None, '雨戸'), ", literally a 'rain door'. And ", (None, '気がつかなかった'), " means 'didn't notice'."]),
    (2, None, ["'Now I remember! When I was ten, my uncle called this 'the winter tea room'!' Age has its own counter: ", (None, '十歳'), " means 'ten years old', and ", (None, '思い出しました'), " is 'I remembered', built from 'think' and 'take out'."]),
    (4, None, ["'One rainy spring the glass roof leaked. There was no money to fix it.' Water that drips through a roof ", (None, 'もれました'), ", the everyday word for 'leaked', for roofs, taps and even secrets."]),
    (5, None, ["'But look at the floor, Takashi! The stone floor is dry. Not one drop of water!' Yuka's ", (None, '一滴も'), " means 'not even one drop'. One plus 'also', followed by a 'no' ending, makes a strong 'not a single'."]),
    (8, None, ["'Wait! To protect the old building, we promised the city a reading café!' The café the city wants is a ", (None, '読書カフェ'), ": 'reading' from the words for 'read' and 'book', plus the loanword for café."]),
    (11, None, ["'Wait, what's standing in the corner under that big white cloth?' A tall shape waits in the ", (None, '隅'), ', the word for the corner of a room, hidden under a white ', (None, '布'), ", or 'cloth'."]),
]

TRANSITION = "Now let's hear the whole sunroom discovery again."

OUTRO = "Room 9 is a dry, sunlit glass tea room, and something tall is waiting under a white sheet in the corner. Let's find out what it is next time."

CLOSING = ('takashi', 'さようなら！')
