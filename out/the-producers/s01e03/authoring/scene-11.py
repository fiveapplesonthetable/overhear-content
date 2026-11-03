"""Scene 11: Let's Pay It in Installments."""
ID = 'the-producers-s01e03-scene-11'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 11
TITLE = "할부로 주는 걸로 해  (Let's Pay It in Installments)"
LEVEL = "A1 — beginner"
LABELS = {"seungchan": "백승찬", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'In the tape storage room, Tak Ye-jin catches Baek Seung-chan painting white correction fluid over a tape label instead of using the magnetic eraser. She keeps his mistake quiet in exchange for paying her car repair bill in tiny installments.'

STORY = [
    ('yejin', '뭐 하냐, 여기서?', 'What are you doing in here?', [(388, '뭐하냐 여기서')], ''),
    ('seungchan', '네, 저희가 여기 테이프를 재활용해야 된다고 해서요.', 'Yes, they said our team needs to recycle the tapes in here.', [(389, '네 저희가 여기 테이프를 재활용해야 된다고 해서요')], ''),
    ('yejin', '이걸로 테이프의 내용을 지우라고, 겉에 글씨를 지우는 게 아니고!', 'You are supposed to erase the footage with this machine, not paint over the label outside!', [(399, '이걸로 테이프의 내용을 지우라고'), (400, '겉에 글씨를 지우는 게 아니고')], ''),
    ('yejin', '모르겠으면 물어봐. 알겠어도 물어봐.', 'If you do not know, ask. Even if you think you know, ask.', [(401, '모르겠으면 물어봐'), (403, '알겠어도 물어봐')], ''),
    ('seungchan', '선배님, 죄송하지만 라준모 선배님께는 비밀로 좀 부탁드리겠습니다.', 'Senior, I am sorry, but please keep this a secret from Senior Ra Joon-mo.', [(406, '선배님, 죄송하지만'), (407, '라준모 선배님께는'), (409, '부탁드리겠습니다')], ''),
    ('yejin', '그럼 이렇게 하자. 그 팔십삼만 원을 할부로 주는 걸로 해.', "Then let's do this. Let's make that eight hundred thirty thousand won payable in installments.", [(410, '그럼 이렇게 하자'), (413, '할부로 주는 걸로 해')], ''),
    ('seungchan', '할부요?', 'In installments?', [(414, '할부요?')], ''),
    ('yejin', '내가 돈이 없어서가 아니야. 투자하는 데가 많아서 그래.', 'It is not because I have no money. It is because I have many places where my money is invested.', [(415, '내가 돈이 없어서가 아니야'), (416, '투자하는 데가 많아서 그래')], ''),
    ('yejin', '자, 오늘 삼만 원. 받아, 미안해하지 말고.', 'Here, thirty thousand won for today. Take it, and do not feel sorry.', [(418, '자, 오늘'), (419, '받아, 미안해하지 말고')], ''),
    ('seungchan', '네, 감사합니다.', 'Yes, thank you.', [(420, '네, 감사합니다')], ''),
    ('yejin', '감사해? 그럼 과자 좀 사 오든가.', 'You are thankful? Then go buy some snacks for the room.', [(421, '감사해?'), (422, '그럼 과자 좀 사 오든가')], ''),
    ('yejin', '트레이닝 시키는 거야, 이게 다.', 'I am putting you through producer training, all of this.', [(428, '트레이닝 시키는 거야, 이게 다')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'What are you doing in here?'"),
    (1, None, "'Yes, they said our team needs to recycle the tapes in here.'"),
    (2, None, "'You are supposed to erase the footage with this machine, not paint over the label outside!'"),
    (3, None, "'If you do not know, ask. Even if you think you know, ask.'"),
    (4, None, "'Senior, I am sorry, but please keep this a secret from Senior Ra Joon-mo.'"),
    (5, None, "'Then let's do this. Let's make that eight hundred thirty thousand won payable in installments.'"),
    (6, None, "'In installments?'"),
    (7, None, "'It is not because I have no money. It is because I have many places where my money is invested.'"),
    (8, None, "'Here, thirty thousand won for today. Take it, and do not feel sorry.'"),
    (9, None, "'Yes, thank you.'"),
    (10, None, "'You are thankful? Then go buy some snacks for the room.'"),
    (11, None, "'I am putting you through producer training, all of this.'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'From asking questions whenever you are unsure to negotiating an installment plan, you now have memorable workplace Korean from the tape library. Until next time!'
CLOSING = ('seungchan', '안녕히 계세요!')
