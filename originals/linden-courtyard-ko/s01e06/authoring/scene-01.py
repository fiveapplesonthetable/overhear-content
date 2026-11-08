# Authoring module for linden-courtyard-ko-s01e06-scene-01.
ID = 'linden-courtyard-ko-s01e06-scene-01'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = 'At the Iron Gate  (철문 앞에서 나눈 인사)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'caleb': 'Caleb', 'owen': 'Owen', 'hannah': 'Hannah'}
INTRO = '메인주 포틀랜드의 린든 코트야드 여관 안뜰에서 세 해 만에 만난 오언과 케일럽이 마주 앉아요. 케일럽은 해나에게 배운 소박하고 진심 어린 세 문장으로 어색한 침묵을 녹이고, 해나는 뜨거운 차를 조용히 내어 옵니다. 먼저 세 사람의 대화를 들어 보세요.'
OPENER = '오랜 침묵을 깨는 형제의 대화를 한 줄씩 함께 읽어 볼까요.'
TRANSITION = '마음이 사르르 풀리는 안뜰의 장면을 처음부터 다시 들어 보세요.'
OUTRO = '또박또박 적은 엽서 글씨체를 단 이 초 만에 알아보고도 기꺼이 찾아온 형의 마음이 참 따뜻하네요. 이제 할아버지의 작업실에서 온 낡은 파란 가방이 열릴 차례입니다. 곧 다음 장면에서 만나요.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('owen', "So 'someone with something from Grandfather' was you all along, Caleb.", '그러니까 할아버지 물건을 맡아 둔 누군가가 처음부터 줄곧 너였구나, 케일럽.'),
    ('caleb', 'Hello, Owen. Thank you for coming today.', '안녕하세요, 오언 형. 오늘 와 줘서 고마워요.'),
    ('owen', 'I recognized your neat block handwriting on that postcard in two seconds.', '그 엽서에 적힌 네 반듯한 정자체 손글씨를 이 초 만에 알아봤단다.'),
    ('caleb', 'Wait, you knew it was from me and came anyway?', '잠깐만요, 제가 보낸 줄 알면서도 어쨌든 와 준 거예요?'),
    ('owen', 'Of course I came. Why did you hide behind a mystery note?', '당연히 왔지. 어째서 수수께끼 같은 쪽지 뒤에 숨었니?'),
    ('caleb', 'Because I was afraid you were still angry. I missed you these three years.', '형이 아직도 화가 나 있을까 봐 두려웠거든요. 지난 삼 년 동안 형이 참 보고 싶었어요.'),
    ('owen', 'Three stubborn years... honestly, little brother, I missed you too.', '고집만 부린 세 해였구나... 솔직히 말하면 아우야, 나도 네가 보고 싶었단다.'),
    ('hannah', 'Excuse me, gentlemen. Here is hot tea, and warm lemon cake is on the way.', '실례합니다, 두 분. 여기 뜨거운 차가 나왔고요, 따뜻한 레몬 케이크도 곧 나옵니다.'),
    ('owen', 'Lemon cake? Wait, how did she know about Friday lemon cake?', '레몬 케이크라고? 잠깐, 저분이 금요일 레몬 케이크 이야기를 어떻게 아시지?'),
    ('caleb', 'Sit down, Owen, take off your heavy coat, and look at this blue suitcase.', '자리에 앉아요, 오언 형, 무거운 코트도 벗고 이 파란 여행 가방 좀 보세요.'),
    ('owen', "Is that the old dark blue bag from Grandfather's workshop?", '저건 할아버지 작업실에 있던 그 낡은 남색 가방 아니니?'),
    ('hannah', 'Take all the time you need. The courtyard is yours.', '필요한 만큼 얼마든지 천천히 시간 보내세요. 안뜰은 온전히 두 분 차지예요.'),
]
WALK = [
    (0, None, ["'그러니까 할아버지 물건을 맡아 둔 누군가가 처음부터 줄곧 너였구나, 케일럽.' 익명 뒤에 숨어 있던 주인공이 애초부터 동생이었음을 짚어 줄 때는", (None, 'was you all along'), '비 동사 과거형에 시간 부사구를 덧붙여 정겹게 말해요.']),
    (1, None, ["'안녕하세요, 오언 형. 오늘 와 줘서 고마워요.' 약속 자리에 걸음해 준 상대에게 오늘이라는 시간 부사까지 더해 인사할 때는", (None, 'Thank you for coming today'), '짧고 반듯한 한 문장으로 진심을 건네요.']),
    (2, None, ["'그 엽서에 적힌 네 반듯한 정자체 손글씨를 이 초 만에 알아봤단다.' 글자를 흘리지 않고 네모반듯하게 또박또박 쓴 손글씨는 영어로", (None, 'block handwriting'), '명사 조합을 써서 단정한 필체를 묘사해요.']),
    (3, None, ["'잠깐만요, 제가 보낸 줄 알면서도 어쨌든 와 준 거예요?' 앞선 사정에도 아랑곳하지 않고 결국 발걸음을 해 주었다는 뜻은 부사를 붙인", (None, 'came anyway'), '두 단어로 벅찬 놀라움을 담아 되물어요.']),
    (4, None, ["'당연히 왔지. 어째서 수수께끼 같은 쪽지 뒤에 숨었니?' 망설일 이유조차 없이 당연한 일이었다고 힘주어 답할 때는", (None, 'Of course I came'), '어순으로 동생을 단번에 안심시켜 주어요.']),
    (5, None, ["'형이 아직도 화가 나 있을까 봐 두려웠거든요. 지난 삼 년 동안 형이 참 보고 싶었어요.' 혹시라도 나쁜 상황일까 봐 겁이 났다는 솔직한 속마음은", (None, 'I was afraid'), '뒤쪽에 접속사 생략 절을 이어 부드럽게 털어놓아요.']),
    (6, None, ["'고집만 부린 세 해였구나... 솔직히 말하면 아우야, 나도 네가 보고 싶었단다.' 상대의 그리움에 나 역시 똑같은 마음이었다고 화답할 때는 끝에 부사를 둔", (None, 'I missed you too'), '네 단어로 묵은 감정을 따뜻하게 녹여 내요.']),
    (7, None, ["'실례합니다, 두 분. 여기 뜨거운 차가 나왔고요, 따뜻한 레몬 케이크도 곧 나옵니다.' 주문한 음식이나 사람이 지금 막 이리로 오는 중이라고 알릴 때는", (None, 'is on the way'), '관용 전치사구로 기분 좋은 기대감을 더해 줘요.']),
    (8, None, ["'레몬 케이크라고? 잠깐, 저분이 금요일 레몬 케이크 이야기를 어떻게 아시지?' 어떤 사실이나 사연에 대해 알고 있는지 물을 때는 전치사를 짝지은", (None, 'know about'), '동사구로 뜻밖의 음식에 담긴 비밀을 궁금해해요.']),
    (9, None, ["'자리에 앉아요, 오언 형, 무거운 코트도 벗고 이 파란 여행 가방 좀 보세요.' 입고 있던 외투나 신발, 안경 따위를 몸에서 벗을 때는 구동사", (None, 'take off'), '표현을 써서 한결 편안히 쉬라고 권해요.']),
    (10, None, ["'저건 할아버지 작업실에 있던 그 낡은 남색 가방 아니니?' 손수 나무를 깎고 물건을 만들던 공방 공간을 가리킬 때는 소유격을 붙인", (None, "Grandfather's workshop"), '명사구로 어린 날의 정겨운 장소를 불러내요.']),
    (11, None, ["'필요한 만큼 얼마든지 천천히 시간 보내세요. 안뜰은 온전히 두 분 차지예요.' 서두르지 말고 넉넉히 대화를 나누라는 배려의 인사", (None, 'Take all the time you need'), '뒤이어 공간이 두 사람 몫이라는 소유대명사 구문', (None, 'is yours'), '표현까지 더해져 여관의 깊은 정이 느껴져요.']),
]
