"""Scene 20: Did You Graduate From Seoul National?."""
ID = 'the-producers-s01e03-scene-20'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 3
SCENE = 20
TITLE = "너 서울대 나왔냐?  (Did You Graduate From Seoul National?)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "seungchan": "백승찬", "writer": "손지연"}
SOURCE_NAME = "프로듀사 (The Producers) S1.03"
SOURCE_FILE = "sources/the-producers/s01/e03.ko.srt"

INTRO = 'Returning from his meeting with Director Jang, Ra Joon-mo announces a brand-new three-on-three idol couple trip to his team. When Son Ji-yeon points out that it is the exact idea Baek Seung-chan suggested earlier, Joon-mo scrambles to save face.'

STORY = [
    ('joonmo', '짝짓기라기보다는 멤버 구성을 새롭게 하자.', "Rather than calling it matchmaking, let's refresh the cast lineup.", [(682, '짝짓기라기보다는 멤버 구성을 새롭게 하자')], ''),
    ('seungchan', '커플 매칭 여행을 하자는 이 말씀이시죠?', "So you mean let's do an overnight couple-matching trip, right?", [(683, '커플 매칭 여행을 하자'), (684, '이 말씀이시죠?')], ''),
    ('joonmo', '딱은 아닌데 얼추 비슷해.', 'Not word for word, though roughly along those lines.', [(685, '딱은 아닌데 얼추')], ''),
    ('writer', '그게 짝짓기죠. 그거 아까 신입이 얘기한 거잖아요.', 'That is matchmaking! That is what the rookie pitched earlier.', [(686, '그게 짝짓기죠'), (687, '그거 아까 신입이 얘기한 거잖아')], ''),
    ('joonmo', '다르지, 그거랑은!', 'It is completely different from that!', [(688, '다르지 그거랑은')], ''),
    ('writer', '아까 싫다더니.', 'Earlier you acted like you hated it.', [(690, '아까 싫다더니')], ''),
    ('joonmo', '싫다고 그랬다고, 내가?', 'I said I hated it? Me?', [(691, '싫다고 그랬다고? 내가?')], ''),
    ('writer', '너 서울대 나왔냐 그러셨잖아요.', 'You asked him, did you graduate from Seoul National University?', [(693, '너 서울대 나왔냐?')], ''),
    ('seungchan', '그러셨습니다.', 'Yes, you did say that.', [(695, '그러셨습니다')], ''),
    ('joonmo', '그래, 물어봤잖아! 그게 왜 싫다는 소리야?', 'Yes, I asked! How does asking that mean I disliked the idea?', [(696, '그래 물어봤잖아'), (697, '그게 왜 싫단 소리야?')], ''),
    ('joonmo', '간만에 쓸 만한 얘기를 하니까 놀라서 확인한 거였다고!', 'He finally said something useful for once, so I was just checking out of amazement!', [(700, '간만에 쓸만한 얘기를 하니까 놀라서 확인한 거였다고')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Rather than calling it matchmaking, let's refresh the cast lineup.'"),
    (1, None, "'So you mean let's do an overnight couple-matching trip, right?'"),
    (2, None, "'Not word for word, though roughly along those lines.'"),
    (3, None, "'That is matchmaking! That is what the rookie pitched earlier.'"),
    (4, None, "'It is completely different from that!'"),
    (5, None, "'Earlier you acted like you hated it.'"),
    (6, None, "'I said I hated it? Me?'"),
    (7, None, "'You asked him, did you graduate from Seoul National University?'"),
    (8, None, "'Yes, you did say that.'"),
    (9, None, "'Yes, I asked! How does asking that mean I disliked the idea?'"),
    (10, None, "'He finally said something useful for once, so I was just checking out of amazement!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Intonation changes everything in Korean, turning the exact same question into either a sarcastic jab or surprised praise. Until next time!'
CLOSING = ('writer', '다음에 또 봐요!')
