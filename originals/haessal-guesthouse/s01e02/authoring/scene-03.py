# Authoring module for haessal-guesthouse-s01e02-scene-03.
ID = 'haessal-guesthouse-s01e02-scene-03'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = '거스름돈 세기  (Counting the Change)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'sungmin': '성민', 'sora': '소라'}
INTRO = 'Nine minutes later, Mina bursts back through the courtyard gate carrying two heavy cloth bags of groceries for Sora and Sungmin. Listen to the scene in Korean first.'
OPENER = "Let's unpack those grocery bags line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'An accidental packet of salted butter nearly caused a jam crisis, until Sora turned it into the secret ingredient for the eggs. See you next time.'
CLOSING = ('sora', '안녕!')
STORY = [
    ('mina', '구 분 걸렸어요! 여기 우유하고 계란하고 사과예요!', 'It took nine minutes! Here are the milk, the eggs, and the apples!'),
    ('sora', '미나야, 진짜 영웅이야! 커피 머신에 쓸 우유부터 먼저 줘.', 'Mina, you are a real hero! Hand me the milk for the coffee machine first.'),
    ('sungmin', '정말 빠르네요! 가게 사장님이 영수증을 주셨어요?', 'So fast! Did the shopkeeper give you a receipt?'),
    ('mina', '여기 있어요! 전부 삼만 팔천 원이라서 거스름돈이 만 이천 원이에요.', 'Right here! Everything cost thirty-eight thousand won, so the change is twelve thousand won.'),
    ('sungmin', '만 원, 만 천 원, 만 이천 원. 백 원까지 딱 맞네요, 고마워요!', 'Ten thousand, eleven thousand, twelve thousand won. Exact to the last coin—thank you!'),
    ('sora', '잠깐만, 미나야... 방금 어떤 버터를 집어 왔어?', 'Wait a second, Mina... which butter did you grab just now?'),
    ('mina', '맨 위 선반에 있던 금색 포장지! 왜?', 'The gold wrapper on the top shelf! Why?'),
    ('sora', '이건 짭짤한 바다 소금 버터야! 달콤한 잼 빵에는 무염 버터가 필요해!', 'This is salty sea-salt butter! Sweet jam rolls need unsalted butter!'),
    ('mina', '어쩌지! 급하게 뛰느라 포장지가 다 똑같아 보였어!', 'Oh no! Because I was running in a rush, all the wrappers looked identical!'),
    ('sungmin', '달콤한 딸기잼에 짭짤한 버터를 같이 내놓아도 될까요?', 'Could we serve salty butter alongside sweet strawberry jam?'),
    ('sora', '잠깐만요, 소금 버터는 잼에는 별로지만 스크램블드에그에는 최고예요!', 'Hold on—salted butter is no good with jam, yet it is the best for scrambled eggs!'),
    ('mina', '휴, 다행이다! 언니의 빠른 생각 덕분에 또 살았네.', 'Phew, what a relief! Quick thinking from you saved breakfast again.'),
]
WALK = [
    (0, None, ["'It took nine minutes! Here are the milk, the eggs, and the apples!' Expressing how much time a trip took uses ", (None, '걸렸어요'), ' right after the minutes.']),
    (1, None, ["'Mina, you are a real hero! Hand me the milk for the coffee machine first.' Notice Sora drops into friendly casual speech with ", (None, '영웅이야'), ', calling Mina a hero.']),
    (3, None, ["'Right here! Everything cost thirty-eight thousand won, so the change is twelve thousand won.' Money handed back across a counter is ", (None, '거스름돈이'), ", 'change'."]),
    (5, None, ["'Wait a second, Mina... which butter did you grab just now?' Asking 'which kind' before a noun uses ", (None, '어떤'), '.']),
    (6, None, ["'The gold wrapper on the top shelf! Why?' Alone with Sora's question, Mina answers casually too, ending with ", (None, '왜'), ", simply 'why?'."]),
    (7, None, ["'This is salty sea-salt butter! Sweet jam rolls need unsalted butter!' Tasty, pleasant saltiness has its own lively word, ", (None, '짭짤한'), ', softer than calling food overly salty.']),
    (8, None, ["'Oh no! Because I was running in a rush, all the wrappers looked identical!' When you wonder 'what do I do now?', casual Korean sighs ", (None, '어쩌지'), '.']),
    (10, None, ["'Hold on—salted butter is no good with jam, yet it is the best for scrambled eggs!' Calling something 'number one' or 'the absolute best' uses ", (None, '최고예요'), '.']),
]
