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
    (0, None, "It literally means this. 'For our spring special, we're going to Geoje Island.' The opening phrase literally means a special broadcast episode welcoming spring. Geoje is a scenic southern island hours from Seoul This literally means that."),
    (1, None, "It literally means this. 'Go where? Geoje Island? I can't go.' As a respected elder speaking to a younger director, Yuh-jung uses crisp casual speech to ask 'go where?', then places the negation word for 'cannot' right before the word 'go' to state flatly 'I cannot go' The word doubles the."),
    (2, None, "It literally means this. 'Why do you keep trying to go so far away?' She attaches the word for 'only' onto 'far away' to complain that he only ever picks distant spots, then ends by asking 'why are you trying to go?' This literally means that."),
    (3, None, "It literally means this. 'And is this sleeping outdoors?' Fans of Korean travel shows know this classic variety-show punishment by heart—sleeping outdoors for the night, usually inside a chilly tent! It is a handy word."),
    (4, None, "It literally means this. 'Going far away doesn't make ratings come out.' She uses a connective ending to challenge a false assumption—'just because you travel far doesn't mean...'—and pairs 'ratings' with an expression meaning 'that's not how they come out' Notice the word for."),
    (5, None, "It literally means this. 'Don't call it spring, I'm freezing to death right now.' Koreans constantly add 'I could die!' right after word like 'cold', 'hungry', or 'tired' for everyday dramatic emphasis It comes from this."),
    (6, None, "It literally means this. 'Honestly, our ratings are at rock bottom right now.' Back in his interview chair, Joon-mo admits the numbers hit the 'floor'—literally 'rock bottom'—while softening the painful truth with words meaning 'in fact' and 'kind of' We built from this."),
    (7, None, "It literally means this. 'Crisis is opportunity, so I'm not that anxious.' Putting on a brave face, he quotes the classic proverb pairing 'crisis' with 'opportunity', then cleanly negates the word for 'anxious' This short for that."),
]

TRANSITION = "Now let's listen to the whole Geoje Island flashback again."
OUTRO = "You picked up how to say 'I can't go', an expressive phrase for when it's freezing to death, and the proverb 'crisis is opportunity'. Back to the meeting room next!"
CLOSING = ("actress", "안녕!")
