"""Scene 05: Why Cannot This Be Processed?."""
ID = 'the-producers-s01e03-scene-05'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = "왜 처리가 안 돼요?  (Why Cannot This Be Processed?)"
LEVEL = "A1 — beginner"
LABELS = {"colleague": "PD 동료", "ilyong": "유일용", "taeho": "김태호"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'Back in the KBS variety office, chief producer Kim Tae-ho tries to turn in his meal receipts to a department colleague. He discovers that expenses near his own home are blocked, while Ryu Il-yong questions what he ordered.'

STORY = [
    ('taeho', '왜 처리가 안 돼요? 다 업무상 사용한 건데.', 'Why cannot this be processed? I used all of it for work.', [(174, '왜 처리가 안 돼요'), (175, '다 업무상 사용한 건데')], ''),
    ('colleague', '주소지나 휴일에 사용한 건 카드 처리 불가입니다.', 'Charges made near your home address or on holidays cannot be put on the company card.', [(176, '주소지에서 사용한 거나'), (177, '휴일에 사용한 건'), (178, '카드 처리 불가입니다')], ''),
    ('colleague', '김 피디님 목동 살죠? 이 영수증이 다 목동에서 쓴 것들이에요.', 'You live in that neighborhood, right? All of these receipts were used right there.', [(180, '김 피디님 목동 살죠?'), (182, '이 영수증이 다 목동에서 쓴 것들이에요')], ''),
    ('taeho', '그럼 난 목동에서 업무 보면 안 돼요?', 'Then am I not allowed to do work near my own neighborhood?', [(183, '그럼 난 목동에서 업무 보면 안 돼요?')], ''),
    ('colleague', '국장님 지적사항입니다.', 'This was flagged directly by the department director.', [(186, '국장님 지적사항입니다')], ''),
    ('taeho', '한 장만 해 주면 안 돼요, 그럼?', 'Could you not process just one receipt for me, then?', [(187, '한 장만 해 주면 안 돼요, 그럼?')], ''),
    ('colleague', '알았어요.', 'All right.', [(193, '알았어요')], ''),
    ('taeho', '그럼 이걸로 해 줘요. 두고 가요.', 'Then please process this one. I will leave it with you.', [(194, '그럼 이걸로 해줘요'), (195, '두고 가요')], ''),
    ('ilyong', '이 집은 순대랑 떡볶이 전골이라고요.', 'That shop is famous for blood sausage and spicy rice-cake hotpot.', [(196, '이 집은 순대예요'), (198, '순대랑 떡볶이'), (199, '전골이라고요')], ''),
    ('ilyong', '그 집에서 김밥을 왜 먹어요?', 'Why would you eat seaweed rice rolls at that place?', [(201, '그 집에서 김밥을 왜 먹어요?')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Why cannot this be processed? I used all of it for work.'"),
    (1, None, "'Charges made near your home address or on holidays cannot be put on the company card.'"),
    (2, None, "'You live in that neighborhood, right? All of these receipts were used right there.'"),
    (3, None, "'Then am I not allowed to do work near my own neighborhood?'"),
    (4, None, "'This was flagged directly by the department director.'"),
    (5, None, "'Could you not process just one receipt for me, then?'"),
    (6, None, "'All right.'"),
    (7, None, "'Then please process this one. I will leave it with you.'"),
    (8, None, "'That shop is famous for blood sausage and spicy rice-cake hotpot.'"),
    (9, None, "'Why would you eat seaweed rice rolls at that place?'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'From office receipts and company cards to favorite street-food dishes, you now have practical Korean phrases for both work expenses and lunch spots. Until next time!'
CLOSING = ('ilyong', '안녕히 계세요!')
