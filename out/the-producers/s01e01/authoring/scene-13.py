"""Scene 13: Veteran actress Youn Yuh-jung refuses Geoje Island and sleeping outdoors on Joon-mo's show."""
ID = "the-producers-s01e01-scene-13"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = "어딜 가, 거제도?  (Go Where? Geoje Island?)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "actress": "윤여정"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "In a flashback to Ra Joon-mo's revamped travel show starring veteran actresses, screen legend Youn Yuh-jung "
    "flatly vetoes a long trip down south and sleeping outdoors. Listen for how she says 'I can't go' "
    "and 'it's cold'."
)

STORY = [
    ("joonmo", "봄맞이 특집으로 거제도를 갑니다.", "For our spring special, we're going to Geoje Island.", [(384, "봄맞이 특집으로 거제도를")], "Completes the interrupted announcement with 갑니다"),
    ("actress", "어딜 가? 거제도? 나 못 가.", "Go where? Geoje Island? I can't go.", [(385, "어딜 가? 거제도?"), (386, "나 못 가")], ""),
    ("actress", "왜 멀리만 가려고 그래?", "Why do you keep trying to go so far away?", [(388, "왜 멀리만 가려고 그래")], ""),
    ("actress", "그리고 야외 취침이야, 이게?", "And is this sleeping outdoors?", [(393, "그리고 야외 취침이야 이게")], ""),
    ("actress", "멀리 간다고 시청률 나오는 거 아니야.", "Going far away doesn't make ratings come out.", [(398, "멀리 간다고 시청자 오는 거 아니야")], "Restores spoken 시청률 나오는 거 from ASR slip 시청자 오는 거"),
    ("actress", "봄이라 그러지 마, 지금 추워 죽겠어.", "Don't call it spring, I'm freezing to death right now.", [(401, "몸이라 그러지 마 지금 추워 죽겠어")], "Restores 봄이라 ('it's spring') from ASR consonant slip 몸이라"),
    ("joonmo", "시청률이 사실 지금 좀 바닥이에요.", "Honestly, our ratings are at rock bottom right now.", [(404, "시청률이 사실 지금 좀 바닥이에요")], ""),
    ("joonmo", "위기는 기회니까 그렇게 불안하지 않아요.", "Crisis is opportunity, so I'm not that anxious.", [(406, "근데 또 위기는 기회니까 그렇게 불안하지 않아요")], "Trims spoken lead-in 근데 또"),
]

OPENER = "Let's walk through the eight lines of Joon-mo's tough outdoor shoot."

WALK = [
    (0, None, "'For our spring special, we're going to Geoje Island.' The opening phrase literally means a special broadcast welcoming spring, built from 'spring' and 'greeting'. Geoje is a scenic southern island hours from Seoul."),
    (1, None, "'Go where? Geoje Island? I can't go.' As a respected elder speaking to a younger director, Yuh-jung uses crisp casual speech to ask 'go where?', then places the negation marker meaning 'cannot' right before 'go' to state flatly 'I cannot go'."),
    (2, None, "'Why do you keep trying to go so far away?' She attaches the marker meaning 'only' onto 'far away' to complain that he only ever picks distant spots, finishing with a casual question meaning 'why do you keep trying to go?'."),
    (3, None, "'And is this sleeping outdoors?' Fans of Korean travel shows know this classic variety-show punishment by heart — pairing the words for 'outdoors' and 'bedtime' to mean sleeping outside for the night, usually inside a chilly tent!"),
    (4, None, "'Going far away doesn't make ratings come out.' She uses a connective ending to challenge a false assumption — 'just because you travel far doesn't mean...' — and pairs 'ratings' with an expression meaning 'that is not how they come out'."),
    (5, None, "'Don't call it spring, I'm freezing to death right now.' After a brisk command meaning 'don't call it spring', Koreans constantly add an expression meaning 'I could die!' right after words like 'cold', 'hungry', or 'tired' for everyday dramatic emphasis."),
    (6, None, "'Honestly, our ratings are at rock bottom right now.' Back in his interview chair, Joon-mo admits the numbers hit the 'floor' — literally 'rock bottom' — while softening the painful truth with everyday words meaning 'honestly' and 'kind of'."),
    (7, None, "'Crisis is opportunity, so I'm not that anxious.' Putting on a brave face, he quotes the classic proverb pairing 'crisis' with 'opportunity', then cleanly negates the word meaning 'anxious'."),
]

TRANSITION = "Now let's listen to the whole Geoje Island flashback again."
OUTRO = "You picked up how to say 'I can't go', an expressive phrase for when it's freezing to death, and the proverb 'crisis is opportunity'. Back to the meeting room next!"
CLOSING = ("actress", "안녕!")
