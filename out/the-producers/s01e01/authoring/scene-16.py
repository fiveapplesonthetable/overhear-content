"""Scene 16: Director Jang In-pyo and CP Kim Tae-ho tell Joon-mo his season is ending."""
ID = "the-producers-s01e01-scene-16"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 16
TITLE = "왜 너만 몰랐어?  (Why Were You the Only One Who Didn't Know?)"
LEVEL = "A1 — beginner"
LABELS = {"inpyo": "장인표", "joonmo": "라준모", "taeho": "김태호"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "Summoned into Variety Director Jang In-pyo's office alongside CP Kim Tae-ho, Ra Joon-mo tries to defend "
    "his 5.7 percent ratings — only to learn that Reporter Kang's rumour was true. Listen for the phrases for "
    "'a sharp spike' and 'why did only you not know?'."
)

STORY = [
    ("inpyo", "어떻게 이렇게 모든 연령층이 골고루 안 보니?", "How does every single age group equally not watch it like this?", [(499, "어떻게 이렇게 모든 연령층이"), (500, "골고루 안 보니")], "Trims duplicate 똑같이"),
    ("joonmo", "국장님, 여기 보시면 급상승한 구간도 있어요.", "Director, if you look here, there's a section that spiked sharply too.", [(501, "국장님 여기 보시면 이렇게"), (502, "급상승한 구간도 있어요")], ""),
    ("inpyo", "게임은 끝났다, 준모야.", "The game is over, Joon-mo.", [(505, "게임은 끝났다줌 뭐야")], "Restores 준모야 word from ASR homophone 줌 뭐야"),
    ("joonmo", "요즘은 매체가 많아서 오 점 칠이 옛날 십오는 된다니까요.", "There are so many outlets now that five point seven equals fifteen in the old days.", [(513, "요즘은 매체가 많아서"), (514, "지금 5.7이 옛날 한 15는 된다니까요")], "Spells 5.7 and 15 in Hangul 오 점 칠 and 십오"),
    ("inpyo", "이거 답이 없다, 접자.", "There's no answer for this, let's fold it.", [(516, "이거 답이 없다"), (517, "없자")], "Restores spoken 접자 ('let's wrap it up') / 엎자"),
    ("inpyo", "이미 결정 다 난 사항이야.", "It's a matter that has already been decided.", [(519, "이미 결정 다 난 사항이야")], ""),
    ("joonmo", "형은 알았어?", "Did you know about this, Tae-ho?", [(520, "형은 알았어?")], ""),
    ("taeho", "예능국 전체가 다 아는데 왜 너만 몰랐어?", "The entire variety department knows, so why were you the only one who didn't?", [(522, "예능국 전체가 다 알고"), (523, "왜 너만 몰랐어?")], "Joins Tae-ho's main clause cleanly"),
]

OPENER = "Let's walk through the eight lines of Joon-mo's reality check in the director's office."

WALK = [
    (0, None, "'How does every single age group equally not watch it like this?' Staring at the chart, Director Jang pairs the phrase for 'every age bracket' with the word for 'evenly' — usually a positive term for balanced meals, turned wickedly ironic when nobody watches! This literally means that."),
    (1, None, "'Director, if you look here, there's a section that spiked sharply too.' Pointing at one tiny bump on the page, Joon-mo addresses his boss as 'department director' and highlights a sudden upward jump in one 'segment' This literally means that."),
    (2, None, "'The game is over, Joon-mo.' The word for 'to end' or 'be finished' is used here to declare 'game over'. Adding a friendly word suffix onto a given name ending in a vowel is how an older boss addresses a junior warmly yet firmly Notice the word for."),
    (3, None, "'There are so many outlets now that five point seven equals fifteen in the old days.' Korean has a dedicated word for a decimal point when reading numbers aloud, and here the expression for 'the old days' is contrasted with 'nowadays' Swap in this word."),
    (4, None, "'There's no answer for this, let's fold it.' Saying literally 'there is no answer' means a situation is hopeless. Then the word meaning 'to fold up' is used in blunt TV talk for shutting a project down The word doubles the."),
    (5, None, "'It's a matter that has already been decided.' Alongside the word for 'already' and the word for 'decision', notice how in Korean a decision doesn't get made — it literally 'comes out' This short for that."),
    (6, None, "'Did you know about this, Tae-ho?' Stunned, Joon-mo turns to Tae-ho and uses a younger man's word for a close older brother or senior mentor, asking 'did you know?' It comes from this."),
    (7, None, "'The entire variety department knows, so why were you the only one who didn't?' The word for 'the whole thing' is set cruelly against 'only you'. Reporter Kang was right: the main producer truly found out last! This means that."),
]

TRANSITION = "Now let's hear the whole scene in the director's office again."
OUTRO = "You heard an ironic 'evenly', the decimal-point marker in 'five point seven', 'there is no answer' when nothing helps, and the phrase for 'only you'. Let's see what happens to Joon-mo's job next!"
CLOSING = ("inpyo", "다음에 봐요!")
