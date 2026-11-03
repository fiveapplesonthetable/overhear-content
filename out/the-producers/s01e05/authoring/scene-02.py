"""Scene 02: Pink Captions and Lies."""
ID = 'the-producers-s01e05-scene-02'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = '핑크 자막과 거짓말  (Pink Captions and Lies)'
LEVEL = "A1 — beginner"
LABELS = {"manager": "매니저", "seungchan": "백승찬"}
SOURCE_NAME = "프로듀사 (The Producers) S1.05"
SOURCE_FILE = 'sources/the-producers/s01/e05.ko.srt'

INTRO = "At the start of Episode 5, rookie producer Baek Seung-chan struggles to pitch Cindy's tent in the pouring rain. Cindy's road manager steps in and suggests editing the scene with bright pink captions so viewers think Cindy built the tent herself."

STORY = [
    ('manager', '텐트 치는 그림 필요하지 않으세요?', 'Do you not need a shot of her pitching the tent?', [(35, '그림 필요하지 않으세요')], ''),
    ('seungchan', '아, 예, 있으면 좋겠지만.', 'Ah, yes, it would be nice if we had one, though.', [(36, '아, 예'), (36, '있으면 좋겠지만')], ''),
    ('manager', '앞에 피디님 혼자 치던 거 편집하고 방금 거부터 쓰면 된다고요.', 'Just edit out the part where you pitched it alone earlier and use it from right now.', [(38, '앞에 피디님 혼자 치던 거 편집하고 방금 거부터 쓰면 된다고요')], ''),
    ('manager', '자막은 신디가 손수 친 첫 야외 취침 텐트, 핑크로 해주시면 되고요.', 'For the caption, you can make it "Cindy\'s first hand-pitched outdoor tent" in pink.', [(39, '자막은'), (40, '신디가'), (40, '첫 야외'), (40, '텐트'), (41, '해주시면 되고요'), (42, '핑크로')], ''),
    ('seungchan', '그건 어렵습니다.', 'That will be difficult.', [(43, '그건 어렵습니다')], ''),
    ('manager', '핑크 어려워요? 요새 자막들 컬러풀하던데.', 'Is pink hard? Captions these days are pretty colorful.', [(44, '핑크 어려워요'), (45, '요새 자막들 컬러풀하던데')], ''),
    ('seungchan', '아니, 핑크가 어려운 게 아니라 그런 거짓말이 어렵다고요.', 'No, it is not that pink is difficult—telling that kind of lie is difficult.', [(46, '핑크가 어려운 게 아니라'), (47, '그런 거짓말이 어렵다고')], ''),
    ('manager', '다큐 찍으러 오셨어요?', 'Did you come here to film a documentary?', [(48, '다큐 찍으러 오셨어요')], ''),
    ('manager', '이거 예능이잖아요, 재밌어야죠.', 'This is a variety show, you know—it has to be fun.', [(51, '이거 예능이잖아요 재밌어야죠')], ''),
    ('seungchan', '저희는 리얼 예능입니다, 더 정확하게는 리얼 야생 로드 버라이어티!', 'We are a reality variety show—more precisely, a real wild road variety show!', [(53, '저희는 리얼 예능입니다'), (54, '더 정확하게는 리얼 야생 로드')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Do you not need a shot of her pitching the tent?'"),
    (1, None, "'Ah, yes, it would be nice if we had one, though.'"),
    (2, None, "'Just edit out the part where you pitched it alone earlier and use it from right now.'"),
    (3, None, '\'For the caption, you can make it "Cindy\'s first hand-pitched outdoor tent" in pink.\''),
    (4, None, "'That will be difficult.'"),
    (5, None, "'Is pink hard? Captions these days are pretty colorful.'"),
    (6, None, "'No, it is not that pink is difficult—telling that kind of lie is difficult.'"),
    (7, None, "'Did you come here to film a documentary?'"),
    (8, None, "'This is a variety show, you know—it has to be fun.'"),
    (9, None, "'We are a reality variety show—more precisely, a real wild road variety show!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Asking to cut footage, add pink captions, and tell apart variety comedy from a documentary gives you vivid Korean vocabulary from television sets. Until next time!'
CLOSING = ('seungchan', '안녕히 계세요!')
