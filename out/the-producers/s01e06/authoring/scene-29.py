"""Scene 29: The Producer Is More Scared Than the Singer."""
ID = 'the-producers-s01e06-scene-29'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 6
SCENE = 29
TITLE = '피디가 더 무서워하고 있어  (The Producer Is More Scared Than the Singer)'
LEVEL = "A1 — beginner"
LABELS = {"cindy": "신디", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.06"
SOURCE_FILE = 'sources/the-producers/s01/e06.ko.srt'

INTRO = 'Still dazed after catching Cindy smiling brightly backstage, Baek Seung-chan guides her onto the hydraulic lift under the stage. Worried the platform looks wobbly, Seung-chan rides it up himself—and freezes in fear.'

STORY = [
    ('seungchan', '방금 신디가 웃은 거 맞지?', 'Did Cindy really just smile right now?', [(892, '방금 신디가'), (897, '웃은 거 맞지')], ''),
    ('seungchan', '비웃은 것도 아니고 그냥 해맑게 웃은 거 맞지?', 'Not a smirk, just a bright genuine smile, right?', [(895, '비웃은 것도 아니고'), (897, '그냥 해맑게 웃은 거 맞지')], ''),
    ('seungchan', '이따가 공연 시작할 때 큐사인 나면 리프트가 무대 위로 올라가면서 등장하시게 될 겁니다.', 'Later when the concert starts, once the cue sign goes out, the lift will rise onto the stage for your entrance.', [(902, '이따가 공연 시작할 때'), (903, '큐사인 나면 리프트가 무대 위로 올라가면서 등장하시게 될 겁니다')], ''),
    ('cindy', '알아요.', 'I know how stage lifts work.', [(904, '알아요')], ''),
    ('seungchan', '원래 이렇게 흔들리는 거 맞죠? 겉보기에는 되게 허술해 보여서.', 'Is it supposed to wobble like this? On the outside it looks pretty rickety.', [(906, '원래 이렇게 흔들리는 거 맞죠'), (908, '겉보기에는 되게 허술해 보여서')], ''),
    ('cindy', '원래 흔들리는 거예요.', 'Stage lifts always wobble like this.', [(909, '원래 흔들리는 거예요')], ''),
    ('seungchan', '그렇다면 다행입니다, 이렇게 올라오는 거구나!', 'Then that is a relief—so this is how it rises up!', [(911, '그렇다면 다행입니다'), (913, '이렇게 올라오는 거구나')], ''),
    ('cindy', 'PD가 출연자를 보호해줘야지 자기가 더 무서워하고 있어!', 'A producer is supposed to protect the performer, yet you look way more scared than I am!', [(915, 'PD가 출연자를'), (916, '자기가 더 무서워하고 있어')], ''),
    ('seungchan', '그렇게까지 무서운 건 아닙니다.', 'I am not all that scared, really.', [(917, '그렇게까지 무서운 건 아니')], ''),
    ('cindy', '안 무서우면 이것 좀 놓지?', 'If you are not scared, how about letting go of my arm first?', [(918, '안 무서우면 이것 좀')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Did Cindy really just smile right now?'"),
    (1, None, "'Not a smirk, just a bright genuine smile, right?'"),
    (2, None, "'Later when the concert starts, once the cue sign goes out, the lift will rise onto the stage for your entrance.'"),
    (3, None, "'I know how stage lifts work.'"),
    (4, None, "'Is it supposed to wobble like this? On the outside it looks pretty rickety.'"),
    (5, None, "'Stage lifts always wobble like this.'"),
    (6, None, "'Then that is a relief—so this is how it rises up!'"),
    (7, None, "'A producer is supposed to protect the performer, yet you look way more scared than I am!'"),
    (8, None, "'I am not all that scared, really.'"),
    (9, None, "'If you are not scared, how about letting go of my arm first?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Testing a shaky stage lift and getting teased by a performer for clinging to the safety rail gives you charming, memorable Korean dialogue. See you next time!'
CLOSING = ('cindy', '안녕히 계세요!')
