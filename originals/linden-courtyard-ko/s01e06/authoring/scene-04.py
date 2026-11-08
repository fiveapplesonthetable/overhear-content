# Authoring module for linden-courtyard-ko-s01e06-scene-04.
ID = 'linden-courtyard-ko-s01e06-scene-04'
SHOW = 'linden-courtyard-ko'
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = 'Lemon Cake and Sharp Eyes  (레몬 케이크와 예리한 눈썰미)'
LEVEL = 'A1 — 입문'
PAIR = 'en-ko'
LABELS = {'tessa': 'Tessa', 'owen': 'Owen', 'caleb': 'Caleb'}
INTRO = '갓 구운 따뜻한 레몬 케이크 한 입에 오언은 어린 시절 린든 거리의 맛을 단번에 떠올려요. 하지만 예리한 눈썰미를 가진 오언이 로비 창문 너머로 울상인 아서의 얼굴을 발견하면서 뜻밖의 구원투수가 나섭니다. 활기찬 안뜰 대화를 들어 보세요.'
OPENER = '달콤한 케이크와 든든한 제안이 오가는 문장들을 살펴볼까요.'
TRANSITION = '반전의 실마리가 풀리는 네 사람의 호흡을 떠올리며 다시 들어 보세요.'
OUTRO = '시청 계약 부서에서 일하는 오언과 문화유산 건축법을 꿰고 있는 케일럽이라니, 이보다 더 든든한 지원군이 또 있을까요! 찻잔을 두고 모두 서둘러 로비 안으로 들어섭니다. 다음 장면에서 만나요.'
CLOSING = ('tessa', 'See you soon!')
STORY = [
    ('tessa', 'Fresh from the oven: Friday lemon cake with extra corner pieces!', '오븐에서 막 꺼내 온 따끈한 금요일 레몬 케이크예요, 모서리 조각도 넉넉히 담았답니다!'),
    ('owen', 'One bite... Caleb, close your eyes! That tastes exactly like Grandfather\'s cake!', '한 입 먹어 보렴... 제임스, 눈을 감아 봐! 할아버지 케이크 맛이랑 똑같아!'),
    ('caleb', 'Tessa baked it this morning when Miss Evelyn told her our Friday story.', '오늘 아침 에블린 선생님께서 우리 금요일 이야기를 들려주시자 테사가 직접 구워 주셨어요.'),
    ('owen', 'What kind of magical guesthouse did you walk into, little brother?', '대체 어떤 마법 같은 여관에 걸어 들어온 거니, 아우야?'),
    ('caleb', "The kind that fixes attic lamps in the rain and guards a stranger's bag.", '빗속에서 다락방 스탠드를 고쳐 주고 낯선 사람의 가방까지 지켜 주는 그런 곳이죠.'),
    ('owen', 'Then tell me why the poor gentleman behind the front desk looks ready to cry.', '그렇다면 프런트 데스크 뒤에 계신 저 가엾은 신사분은 왜 당장이라도 울 것 같은 표정이신지 말해 보렴.'),
    ('tessa', 'Oh! Did you see Arthur through the window? I tried to smile twice as wide!', '어머! 창문 너머로 아서를 보셨어요? 일부러 두 배나 활짝 웃어 보이려고 애썼는데!'),
    ('caleb', 'Tessa, is something wrong inside? Did the boiler break again?', '테사, 안에서 무슨 안 좋은 일이라도 생겼나요? 보일러가 또 고장 났나요?'),
    ('tessa', 'Worse than a pipe... a registered letter came from the building owner at noon.', '배관 문제보다 훨씬 심각해요... 정오에 건물주한테서 등기 우편이 날아왔거든요.'),
    ('owen', 'A property letter? Let Caleb and me see it. I work in city contracts, and he knows heritage law!', '부동산 편지라고요? 케일럽과 제가 한번 보게 해 주세요. 저는 시 계약 부서에서 일하고, 얘는 문화유산 법규를 잘 알거든요!'),
    ('caleb', "Wait, Owen, you still work at City Hall's contract desk?!", '잠깐만요, 오언 형, 아직도 시청 계약 담당 부서에서 일해요?!'),
    ('tessa', 'Both of you?! Leave your teacups, come inside this very second!', '두 분 다요?! 찻잔은 그대로 두고 지금 당장 이 순간 안으로 들어오세요!'),
]
WALK = [
    (0, None, ["'오븐에서 막 꺼내 온 따끈한 금요일 레몬 케이크예요, 모서리 조각도 넉넉히 담았답니다!' 오븐에서 방금 구워져 나와 김이 모락모락 나는 상태는 형용사구", (None, 'Fresh from the oven'), '표현으로 제과점처럼 향긋하게 소개해요.']),
    (1, None, ["'한 입 먹어 보렴... 제임스, 눈을 감아 봐! 할아버지 케이크 맛이랑 똑같아!' 음식 맛이 기억 속 무언가와 똑같다고 감탄할 때는 감각 동사에 전치사를 붙인", (None, 'tastes exactly like'), '구절로 추억의 맛을 생생히 소환해요.']),
    (2, None, ["'오늘 아침 에블린 선생님께서 우리 금요일 이야기를 들려주시자 테사가 직접 구워 주셨어요.' 누구에게 어떤 사연을 들려주었다고 말할 때는 간접목적어와 직접목적어를 나란히 둔", (None, 'told her our Friday story'), '어순으로 자연스럽게 풀어내요.']),
    (3, None, ["'대체 어떤 마법 같은 여관에 걸어 들어온 거니, 아우야?' 대상의 종류나 성격을 감탄 섞어 물어볼 때는 의문사 덩어리", (None, 'What kind of'), '표현으로 문장 맨 앞을 힘 있게 열어요.']),
    (4, None, ["'빗속에서 다락방 스탠드를 고쳐 주고 낯선 사람의 가방까지 지켜 주는 그런 곳이죠.' 비가 내리는 날씨 한가운데서 일어난 일을 묘사할 때는 전치사구", (None, 'in the rain'), '세 단어로 정겨운 에피소드를 덧붙여요.']),
    (5, None, ["'그렇다면 프런트 데스크 뒤에 계신 저 가엾은 신사분은 왜 당장이라도 울 것 같은 표정이신지 말해 보렴.' 금방이라도 눈물을 터뜨릴 듯한 표정을 포착할 때는 형용사와 부정사를 이은", (None, 'looks ready to cry'), '구절로 상대의 안색을 예리하게 짚어 내요.']),
    (6, None, ["'어머! 창문 너머로 아서를 보셨어요? 일부러 두 배나 활짝 웃어 보이려고 애썼는데!' 평소보다 갑절로 크게 미소 지었다는 배수 비교 표현은 원급을 활용한", (None, 'twice as wide'), '어순으로 태연한 척 애썼던 순간을 말해요.']),
    (7, None, ["'테사, 안에서 무슨 안 좋은 일이라도 생겼나요? 보일러가 또 고장 났나요?' 이상한 낌새를 채고 무슨 문제가 있는지 조심스레 물을 때는 뒤에서 형용사가 꾸미는", (None, 'is something wrong'), '단골 회화 구문을 그대로 활용해요.']),
    (8, None, ["'배관 문제보다 훨씬 심각해요... 정오에 건물주한테서 등기 우편이 날아왔거든요.' 앞선 걱정거리보다 상황이 한층 더 나쁘다고 맞받을 때는 비교급 구절", (None, 'Worse than a pipe'), '표현으로 심각한 분위기를 단번에 알려요.']),
    (9, None, ["'부동산 편지라고요? 케일럽과 제가 한번 보게 해 주세요. 저는 시 계약 부서에서 일하고, 얘는 문화유산 법규를 잘 알거든요!' 사역동사 뒤에 두 사람을 목적격으로 반듯하게 세운", (None, 'Let Caleb and me see it'), '문장으로 믿음직한 도움을 자청해요.']),
    (10, None, ["'잠깐만요, 오언 형, 아직도 시청 계약 담당 부서에서 일해요?!' 도시 행정을 맡아보는 시청 청사의 소속 부서를 말할 때는 소유격을 붙인", (None, "City Hall's"), '형태로 뜻밖의 반가운 인연을 확인해요.']),
    (11, None, ["'두 분 다요?! 찻잔은 그대로 두고 지금 당장 이 순간 안으로 들어오세요!' 일 초도 지체하지 말고 바로 지금 당장 움직여 달라고 재촉할 때는 강조어를 더한", (None, 'this very second'), '부사구로 다급하고 반가운 마음을 터뜨려요.']),
]
