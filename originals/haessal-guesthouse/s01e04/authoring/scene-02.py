# Authoring module for haessal-guesthouse-s01e04-scene-02.
ID = 'haessal-guesthouse-s01e04-scene-02'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = '파란 나무 문  (The Blue Door)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'junho': '준호'}
INTRO = 'Ten minutes later, Mina has crossed the river bridge in Seoul, yet two narrow streets branch off behind the pharmacy. She phones Junho from beside a stone fountain. Listen first.'
OPENER = "Now let's listen to their dawn phone call line by line."
TRANSITION = "Now let's hear the whole square scene again."
OUTRO = 'Two new brass valves in her pocket and early risers already stirring upstairs! Next time, Sora and Sungmin try to keep everyone busy at breakfast.'
CLOSING = ('junho', '또 만나요!')
STORY = [
    ('mina', '준호 씨, 제 말 잘 들려요? 방금 초록색 약국을 지났어요!', 'Junho, can you hear me well? I just passed the green pharmacy!'),
    ('junho', '아주 잘 들려요. 작은 돌 분수대 옆에 서 있어요?', 'Loud and clear. Are you standing beside the little stone fountain?'),
    ('mina', '네! 왼쪽에 작은 길이 두 개 있는데 어느 길로 가요?', 'Yes! There are two small streets on the left—which street do I take?'),
    ('junho', '좁은 골목 말고 꽃집 옆에 있는 두 번째 길로 가세요.', 'Not the narrow alley—take the second street beside the flower shop.'),
    ('mina', '지금 걷고 있어요... 아, 금색 열쇠 그림하고 파란 문이 보여요!', 'Walking now... oh, I can see the golden key picture and the blue door!'),
    ('junho', '다행이네요! 철문 셔터는 열렸어요?', 'What a relief! Is the metal shutter open?'),
    ('mina', '직원이 지금 자물쇠를 열고 있어요! 전화 끊지 말고 잠시만 기다려 주세요.', 'The clerk is unlocking it right now! Stay on the phone one second.'),
    ('junho', '안쪽 황동 링 너비가 이십 밀리미터인지 꼭 확인하세요.', 'Be sure to check whether the inner brass ring is twenty millimetres wide.'),
    ('mina', '헌 밸브하고 대 보셨는데 딱 맞아요! 선반에 두 개 남았대요!', 'He held it against the old valve and it matches! He says two are left on the shelf!'),
    ('junho', '두 개 다 사세요! 여분 밸브가 있으면 내년 겨울도 안심이에요.', 'Buy both! With a spare valve, next winter is worry-free too.'),
    ('mina', '현금으로 계산했어요! 공구함 열어 두세요, 지금 다리 건너 뛰어갈게요!', 'Paid in cash! Leave your toolbox open, I am running back across the bridge now!'),
    ('junho', '서두르세요, 방금 이층 계단에서 발소리가 들렸어요!', 'Hurry—I just heard footsteps on the second-floor stairs!'),
]
WALK = [
    (0, None, ["'Junho, can you hear me well? I just passed the green pharmacy!' Checking phone reception uses ", (None, '잘 들려요'), ", 'can it be heard well?'."]),
    (2, None, ["'Yes! There are two small streets on the left—which street do I take?' Choosing between routes uses ", (None, '어느 길로'), ", 'by which street?'."]),
    (3, None, ["'Not the narrow alley—take the second street beside the flower shop.' Saying 'not X, take Y instead' is effortless with ", (None, '골목 말고'), ", placing 'malgo' right after the rejected option."]),
    (3, None, ["'Not the narrow alley—take the second street beside the flower shop.' Notice ", (None, '꽃집'), ", literally 'flower house', how Korean names cosy shops like bakeries and florists."]),
    (4, None, ["'Walking now... oh, I can see the golden key picture and the blue door!' Spotting a landmark in the distance uses ", (None, '보여요'), ", 'is visible'."]),
    (9, None, ["'Buy both! With a spare valve, next winter is worry-free too.' Peace of mind has the warm word ", (None, '안심이에요'), ", literally 'resting heart'."]),
    (10, None, ["'Paid in cash! Leave your toolbox open, I am running back across the bridge now!' Settling the bill at a register or market uses ", (None, '계산했어요'), ", 'paid' or 'calculated the bill'."]),
    (11, None, ["'Hurry—I just heard footsteps on the second-floor stairs!' Urging someone to move fast without sounding harsh uses ", (None, '서두르세요'), ", 'please hurry'."]),
]
