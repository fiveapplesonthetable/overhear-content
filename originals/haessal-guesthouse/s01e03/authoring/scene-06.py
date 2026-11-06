# Authoring module for haessal-guesthouse-s01e03-scene-06.
ID = 'haessal-guesthouse-s01e03-scene-06'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = '별 다섯 개짜리 안도  (A Five-Star Sigh of Relief)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'sungmin': '성민', 'mina': '미나', 'sora': '소라'}
INTRO = 'Back at the ground-floor desk, Sungmin paces anxiously until Mina comes down smiling to join him and Sora. Then Mina spots something lying beside the brass bell. Listen first.'
OPENER = "Let's see why that forgotten notebook sets off a new theory."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "Neat pencil sketches and a 'nine out of ten' rating have convinced them Jihoon is a secret travel-guide inspector—just as a strange metallic clanking echoes through the house! See you next time."
CLOSING = ('sora', '또 봐요!')
STORY = [
    ('sungmin', '어떻게 됐어요? 손님이 화내셨어요? 환불해 달라고 하셨어요?', 'How did it go? Did the guest get angry? Did he ask for a refund?'),
    ('mina', '둘 다 아니에요! 조용한 지붕 들보를 아주 좋아하시면서 고맙다고 하셨어요.', 'Neither! He loved the quiet roof beams and thanked us.'),
    ('sungmin', '미나 씨는 호텔 일에 재능이 있어요! 제 혈압이 살았네요!', 'Mina, you have a talent for hospitality! My blood pressure is saved!'),
    ('sora', '올라가시기 전에 채소 수프도 한 방울 안 남기고 다 드셨어요.', 'Before going up, he even ate every last drop of the vegetable soup.'),
    ('mina', '잠깐만요, 카운터 위에 있는 이 작은 갈색 가죽 수첩은 누구 거예요?', 'Wait—whose small brown leather notebook is this on the counter?'),
    ('sora', '지훈 님이 나한테서 마른 수건을 받을 때 내려놓으셨어!', 'Mr Jihoon set it down when he took the dry towel from me!'),
    ('sungmin', '물론 남의 수첩을 몰래 보면 안 되지만... 어, 가운데 페이지가 펼쳐져 있네요!', "Of course we must not peek at someone else's notebook... oh, the middle page fell right open!"),
    ('mina', '왜 우리 골목 게스트하우스 세 곳이 연필로 깔끔하게 그려져 있죠?', 'Why are three guesthouses on our lane neatly drawn in pencil?'),
    ('sora', "우리 집 옆에 적힌 글씨 좀 봐. '안마당 너비, 거리 소음, 정숙도 십 점 만점에 구 점!'", "Look at the writing beside our house: 'Courtyard width, street noise, quietness score: nine out of ten!'"),
    ('sungmin', '십 점 만점에 구 점이라고요?! 보통 손님은 로비를 재지 않는데 설마...', 'Nine out of ten?! Ordinary guests do not measure lobbies unless...'),
    ('sora', '설마 매년 나오는 서울 여행 가이드북 작가님 아니에요?!', 'Could he write for the annual Seoul travel guidebook?!'),
    ('mina', '얼른 덮어요! 위층에 가져다드릴게요... 어, 방금 저 큰 쇠 소리는 뭐예요?', 'Close it quickly! Let me take it upstairs... wait, what was that loud metal sound just now?'),
]
WALK = [
    (0, None, ["'How did it go? Did the guest get angry? Did he ask for a refund?' Asking for money back on a ticket or room uses ", (None, '환불해'), ", 'refund'."]),
    (1, None, ["'Neither! He loved the quiet roof beams and thanked us.' Dismissing two worries at once is easy with ", (None, '둘 다 아니에요'), ", 'it is neither of the two'."]),
    (2, None, ["'Mina, you have a talent for hospitality! My blood pressure is saved!' Praising someone's natural knack uses ", (None, '재능이 있어요'), ", 'you have talent'."]),
    (4, None, ["'Wait—whose small brown leather notebook is this on the counter?' Pocket notebooks are called ", (None, '수첩은'), ', and ', (None, '누구 거예요'), " asks 'whose is it?'."]),
    (6, None, ["'Of course we must not peek at someone else's notebook... oh, the middle page fell right open!' Doing something secretly on the sly uses ", (None, '몰래'), '.']),
    (8, None, ["'Look at the writing beside our house: Courtyard width, street noise, quietness score: nine out of ten!' Korean states 'out of ten points' first—", (None, '십 점 만점에'), '—and puts the earned score second.']),
    (9, None, ["'Nine out of ten?! Ordinary guests do not measure lobbies unless...' When a wild suspicion suddenly dawns on you, ", (None, '설마'), " expresses 'surely not... could it be?'."]),
    (11, None, ["'Close it quickly! Let me take it upstairs... wait, what was that loud metal sound just now?' Closing a book or lid uses ", (None, '덮어요'), ', distinct from shutting a door.']),
]
