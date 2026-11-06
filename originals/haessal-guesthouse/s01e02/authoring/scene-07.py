# Authoring module for haessal-guesthouse-s01e02-scene-07.
ID = 'haessal-guesthouse-s01e02-scene-07'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 2
SCENE = 7
TITLE = '오후의 휴식  (How Regulars Order)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'sora': '소라', 'mina': '미나', 'junho': '준호'}
INTRO = 'In the calm afternoon sunshine, Mina takes a ten-minute break in the café corner while Sora wipes the counter and Junho tightens a loose wooden chair leg. Listen first.'
OPENER = "Let's join their afternoon coffee break one line at a time."
TRANSITION = "Now let's listen to the whole afternoon scene again."
OUTRO = 'A quiet cup of coffee, a tightened chair, and three colleagues who already feel like a team. One scene left in Episode 2—and Sungmin is about to make a dreadful discovery. See you next time.'
CLOSING = ('sora', '다음에 봐요!')
STORY = [
    ('sora', '미나야, 여기 앉아! 오늘 아침에 동네를 다 뛰었잖아, 커피 마셔.', 'Mina, sit here! You ran all over the neighbourhood this morning—drink some coffee.'),
    ('mina', '좋아! 우유 넣고 설탕은 조금만 넣어 줘.', 'Gladly! Put in milk and just a little sugar for me.'),
    ('junho', '그 구석 의자 조심해요. 이 나사만 조일 테니까 십 초만 기다리세요.', 'Watch that corner chair. Wait ten seconds while I tighten this screw.'),
    ('mina', '벌써 끝났어요? 준호 씨는 어디에나 드라이버를 가지고 다니시네요!', 'Finished already? Junho, you carry a screwdriver everywhere!'),
    ('junho', '오래된 집은 화요일마다 나사가 하나씩 풀려요. 이제 앉으세요.', 'In old houses one screw loosens every Tuesday. Now sit down.'),
    ('sora', '봐, 바쁜 아침 식사도 넘기고 수상한 전화도 잘 받았잖아!', 'Look, you made it through the busy breakfast and handled the mysterious call too!'),
    ('mina', '솔직히 회색빛 옛날 사무실보다 여기가 훨씬 좋아요.', 'Honestly, I like it here much better than my grey old office.'),
    ('sora', '금요일 정오가 빨리 오면 좋겠다! 가방 주인이 들어올 때 맨 앞자리에 앉을 거야!', "I hope Friday noon comes fast! When the bag's owner walks in, I am sitting in the front row!"),
    ('junho', '손님을 그렇게 쳐다보면 안 돼요. 가방만 돌려드리고 우리 일만 합시다.', "You must not stare at a guest like that. Let's return the bag and mind our own work."),
    ('sora', '저 말 좀 들어 봐! 사실은 준호 씨가 우리보다 두 배나 더 궁금해해요!', 'Listen to him talk! In truth, Junho is twice as curious as we are!'),
    ('junho', '저는 그냥 안전을 확인하는 거예요. 그게 제 일이니까요.', 'I am simply checking safety. Because that is my job.'),
    ('mina', '그럼요, 준호 씨! 비밀은 꼭 지켜 드릴게요!', 'Of course, Junho! We will guard your secret well!'),
]
WALK = [
    (1, None, ["'Gladly! Put in milk and just a little sugar for me.' Asking for a tiny bit of sugar or salt uses ", (None, '조금만'), ", 'just a little'."]),
    (3, None, ["'Finished already? Junho, you carry a screwdriver everywhere!' Surprise that something happened sooner than expected starts with ", (None, '벌써'), ", 'already'."]),
    (4, None, ["'In old houses one screw loosens every Tuesday. Now sit down.' Putting ", (None, '화요일마다'), " together turns 'Tuesday' into 'every Tuesday', a pattern that works with any time word."]),
    (6, None, ["'Honestly, I like it here much better than my grey old office.' Comparing two places uses ", (None, '훨씬 좋아요'), " for 'much better', with 'than' hooked onto the old office."]),
    (7, None, ["'I hope Friday noon comes fast! When the bag's owner walks in, I am sitting in the front row!' Wishing aloud in Korean often ends with ", (None, '좋겠다'), ", literally 'it would be good if'."]),
    (9, None, ["'Listen to him talk! In truth, Junho is twice as curious as we are!' Double and triple amounts pair a number with ", (None, '두 배나'), ", 'a full two times as much'."]),
    (10, None, ["'I am simply checking safety. Because that is my job.' Downplaying something with a shrug uses ", (None, '그냥'), ", 'just' or 'simply'."]),
    (11, None, ["'Of course, Junho! We will guard your secret well!' Keeping a promise or a secret uses ", (None, '비밀은'), " paired with 'protect'."]),
]
