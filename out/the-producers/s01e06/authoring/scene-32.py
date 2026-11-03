"""Scene 32: Trying to Prevent an Accident."""
ID = 'the-producers-s01e06-scene-32'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 6
SCENE = 32
TITLE = '사고를 막아보겠다고 그런 거  (Trying to Prevent an Accident)'
LEVEL = "A1 — beginner"
LABELS = {"colleague": "PD 동료", "inpyo": "장인표", "taeho": "김태호"}
SOURCE_NAME = "프로듀사 (The Producers) S1.06"
SOURCE_FILE = 'sources/the-producers/s01/e06.ko.srt'

INTRO = 'Back at the concert hall after the rehearsal accident, a panicked colleague messages classmates trying to find someone else to direct the stage. Meanwhile, Kim Tae-ho explains to director Jang In-pyo how Tak Ye-jin got hurt.'

STORY = [
    ('colleague', '동기 여러분, 지금 특집 리허설 중 큰 사고가 났습니다!', 'Classmates, a major accident just broke out during our special concert rehearsal!', [(1002, '동기 여러분'), (1003, '지금 특집 리허설 중 큰 사고가 났습니다')], ''),
    ('colleague', '탁예진이 부상으로 병원으로 실려가서 제가 대신 연출을 해야 할 상황입니다.', 'Tak Ye-jin was rushed to the hospital with injuries, putting me in a spot where I have to direct instead.', [(1004, '탁예진이 부상으로 병원으로 실려가서'), (1005, '대신에 연출을 해야 할 상황입니다')], ''),
    ('colleague', '난 의전해야 하는데, 누구 나 대신 연출해 줄 사람?', 'I am supposed to escort VIPs—anyone willing to direct the stage in my place?', [(1006, '난 의전해야 하는데'), (1007, '누구 나 대신 연출해 줄 사람')], ''),
    ('taeho', '예진이가 미는 바람에 신디가 리프트 구멍에 빠져서 더 다쳤다고 합니다.', 'Because Ye-jin shoved her clear, Cindy tumbled into the lift opening and got hurt worse.', [(1011, '예진이가'), (1011, '미는 바람에'), (1012, '신디가 리프트 구멍에 빠져'), (1012, '더 다쳤다고 합니다')], ''),
    ('inpyo', '예진이는 왜 그랬어?', 'Why did Ye-jin do that?', [(1013, '예진이는 왜 그랬어')], ''),
    ('taeho', '자기 나름대로는 사고를 막아보겠다고 그런 거고요,', 'In her own way, she was trying to prevent a collision.', [(1015, '나름대로는 사고를 막아보겠다고 그런 거고')], ''),
    ('taeho', '예진이 본인도 팔을 다쳐서 뭐라고 나무라기도 그렇습니다.', 'And since Ye-jin hurt her own arm too, it feels harsh to scold her over it.', [(1016, '예진이 본인도 팔을 다쳐'), (1017, '뭐라고 참 나무라기도 그렇고')], ''),
    ('inpyo', '변 대표가 우리 고소한다고 하는 거 아닐까?', 'Do you think CEO Byun might threaten to sue us?', [(1018, '변 대표가 우리'), (1018, '하는 거 아닐까')], ''),
    ('colleague', '제가 대신 연출을 해야 할 상황인데 아무도 답이 없네!', 'I am stuck having to direct the stage myself and nobody in my group chat is replying!', [(1005, '대신에 연출을 해야 할 상황입니다')], ''),
    ('taeho', '일단 병원 상황부터 알아보자.', "First let's check how things are going at the hospital.", [(1015, '사고를 막아보겠다고')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Classmates, a major accident just broke out during our special concert rehearsal!'"),
    (1, None, "'Tak Ye-jin was rushed to the hospital with injuries, putting me in a spot where I have to direct instead.'"),
    (2, None, "'I am supposed to escort VIPs—anyone willing to direct the stage in my place?'"),
    (3, None, "'Because Ye-jin shoved her clear, Cindy tumbled into the lift opening and got hurt worse.'"),
    (4, None, "'Why did Ye-jin do that?'"),
    (5, None, "'In her own way, she was trying to prevent a collision.'"),
    (6, None, "'And since Ye-jin hurt her own arm too, it feels harsh to scold her over it.'"),
    (7, None, "'Do you think CEO Byun might threaten to sue us?'"),
    (8, None, "'I am stuck having to direct the stage myself and nobody in my group chat is replying!'"),
    (9, None, "'First let's check how things are going at the hospital.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Scrambling to cover an emergency on stage and defending a teammate who got hurt trying to prevent a worse accident gives you realistic Korean workplace expressions. Until next time!'
CLOSING = ('taeho', '안녕히 계세요!')
