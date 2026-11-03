"""Scene 15: Ye-jin lectures rookies on guarding their own turf and rejects Joon-mo's request on speakerphone."""
ID = "the-producers-s01e01-scene-15"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 15
TITLE = "자기 밥그릇은 자기가 챙겨야 돼  (Guard Your Own Rice Bowl)"
LEVEL = "A1 — beginner"
LABELS = {"yejin": "탁예진", "joonmo": "라준모", "writer": "손지연"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Right after telling the rookies never to cave to backstage favours, Tak Ye-jin gets Ra Joon-mo's call "
    "on speakerphone in front of both teams. Listen for the word for 'a favour' and the expression for "
    "'rice bowl' — meaning your own livelihood and turf."
)

STORY = [
    ("yejin", "우리 라준모 피디가 나한테 무슨 부탁이 있는데?", "What favour does our PD Ra Joon-mo have to ask me?", [(446, "우리 라즈모 피디가 나한테 무슨 부탁이 있는데?")], "Restores 라준모 from ASR spelling 라즈모"),
    ("joonmo", "그쪽에서 사전 녹화 좀 떠주면 안 되냐?", "Couldn't your side pre-record them for us?", [(449, "그쪽에서 사전 녹화 좀 떠주면 안 되냐?")], ""),
    ("yejin", "안 돼, 그날은 무대가 많아요.", "No way, we have lots of stages that day.", [(450, "안 돼"), (451, "그날은 무대가 많아요")], ""),
    ("joonmo", "아 좀, 뮤뱅 피디님, 부탁 좀 합시다!", "Come on, Music Bank PD, let me ask this one favour!", [(452, "아 좀 뮤백 피디님"), (453, "부탁 좀 합시다")], "Restores 뮤뱅 from ASR 뮤백"),
    ("yejin", "우리 각자도생합시다.", "Let's each fend for ourselves.", [(457, "우리 각자 도생합시다")], "Writes four-character idiom 각자도생 solid"),
    ("yejin", "이 바닥은 자기 밥그릇은 자기가 챙겨야 돼.", "In this industry, you have to look after your own rice bowl.", [(459, "이 바닥은 자기 밥그릇은 자기가 챙겨야 돼")], ""),
    ("writer", "돼요, 안 돼요?", "Is it on, or is it off?", [(471, "돼요, 안 돼요")], ""),
    ("joonmo", "얘가 분위기 파악 못 하네.", "She really can't read the room.", [(470, "얘 분위기 파악 못하네")], ""),
]

OPENER = "Let's savour the eight lines of Joon-mo's speakerphone humiliation."

WALK = [
    (0, None, "'What favour does our PD Ra Joon-mo have to ask me?' Showing off in front of the rookies, Ye-jin puts 'our' teasingly before Joon-mo's name, then pairs the noun meaning a favour or personal request with 'to me'."),
    (1, None, "'Couldn't your side pre-record them for us?' He points politely to 'your team over there' and uses the broadcast term for taping a performance ahead of the live show, ending with a casual phrasing meaning 'couldn't you do this for us?'."),
    (2, None, "'No way, we have lots of stages that day.' First comes a blunt casual 'no can do', then she switches to a polite 'there are many' because she knows his writers are listening, pointing to the day's stage performances."),
    (3, None, "'Come on, Music Bank PD, let me ask this one favour!' Swallowing his pride, Joon-mo tacks an honorific suffix onto 'PD' and pleads with a formal suggestion ending: 'let us please make this request!'."),
    (4, None, "'Let's each fend for ourselves.' Ye-jin drops a punchy four-syllable idiom literally meaning 'each person seeks their own survival', turning it into a brisk 'let's each handle our own show!'."),
    (5, None, "'In this industry, you have to look after your own rice bowl.' Hanging up, she lectures the rookies using slang that literally means 'this floor' for 'this industry', then compares your livelihood and turf to a 'rice bowl' you must guard yourself."),
    (6, None, "'Is it on, or is it off?' Back in Joon-mo's room, Ji-yeon cuts straight to the chase with a four-syllable phrase literally meaning 'does it work, doesn't it work?' — the quickest way to settle any yes-or-no question in Korean."),
    (7, None, "'She really can't read the room.' Embarrassed in front of his staff, Joon-mo mutters Korean's exact match for 'reading the room', combining the words for 'atmosphere' and 'grasping' into one sharp expression."),
]

TRANSITION = "Now let's listen to the whole speakerphone showdown again."
OUTRO = "You now have the expressions for asking a favour, demanding a quick yes-or-no, and reading the room. Next, Director Jang calls Joon-mo in!"
CLOSING = ("yejin", "안녕히 가세요!")
