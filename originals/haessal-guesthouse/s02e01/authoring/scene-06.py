# Authoring module for haessal-guesthouse-s02e01-scene-06.
ID = 'haessal-guesthouse-s02e01-scene-06'
SHOW = 'haessal-guesthouse'
SEASON = 2
EPISODE = 1
SCENE = 6
TITLE = '오월의 엽서  (Postcards from May)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'sora': '소라', 'youngmi': '영미', 'junho': '준호'}
INTRO = 'Back at the four-table café corner while Mina answers the front-desk phone, Sora pours fresh tea for Youngmi and Junho as they spread the old postcards from the cedar box across the table. Let\'s listen in first.'
OPENER = "Let's read the old postcards over Sora's shoulder."
TRANSITION = "Now let's listen to the whole postcard scene again."
OUTRO = 'Thirty years ago Room 9 welcomed the street every Friday at six, and now Sora, Youngmi and Junho are ready to bring the tradition back. See you next time.'
CLOSING = ('sora', '또 봐요!')
STORY = [
    ('sora', '이 흑백 사진 좀 보세요! 안마당 나무가 일층까지밖에 안 와요!', 'Look at this black-and-white photo! The courtyard tree only reaches the ground floor!'),
    ('junho', '선생님, 그 파란 엽서 뒷면을 읽어 주세요.', 'Madam, please read the back of that blue postcard.'),
    ('youngmi', "'삼십 년 전 오월 십 일. 매주 금요일 여섯 시, 구호실에서 차와 피아노.'", "'May tenth, thirty years ago. Every Friday at six, tea and piano in Room Nine.'"),
    ('sora', '매주 금요일 여섯 시요! 동네 사람들이 다 여기 와서 차 마시고 음악을 들었네요!', 'Every Friday at six! The whole neighbourhood came here for tea and music!'),
    ('junho', "다음 카드도 보세요. '제빵사와 선생님 자리로 구석 의자 두 개를 남겨 주세요.'", "Look at the next card too: 'Please save two corner chairs for the baker and the teacher.'"),
    ('youngmi', '정말 좋네요. 삼십 년 전에도 이 집이 이웃들을 모았어요.', 'How lovely. Thirty years ago this house was already bringing neighbours together.'),
    ('sora', '그리고 다음 주 금요일이 이번 달 첫 번째 금요일이에요!', 'And next Friday is the first Friday of the month!'),
    ('junho', '잠깐만요. 다음 주 금요일 여섯 시에 구호실을 다시 열고 싶어요?', 'Wait. You want to open Room Nine again next Friday at six?'),
    ('sora', '육 일 동안 유리 닦고, 덧문 칠하고, 레몬 타르트 구워요!', 'Six days to wash the glass, paint the shutters and bake lemon tarts!'),
    ('youngmi', '준호 씨가 조용한 가운데 건반을 깨우면, 제가 기꺼이 여섯 시에 칠게요.', 'If you wake up that silent middle key, Junho, I will gladly play at six.'),
    ('junho', '좋아요, 약속이에요! 미나 씨하고 사장님한테 금요일 계획을 말하러 가요!', "Deal, it's a promise! Let's go tell Mina and the boss our Friday plan!"),
    ('sora', '엽서 가져가요! 사장님이 이 사진을 보면 바로 좋다고 할 거예요!', 'Bring the postcard! Once the boss sees this photo, he will say yes right away!'),
]
WALK = [
    (0, None, ["'Look at this black-and-white photo! The courtyard tree only reaches the ground floor!' Korean says 'only' with a pair, 'outside of' plus 'not': ", (None, '일층까지밖에 안 와요'), '.']),
    (0, None, ["'Look at this black-and-white photo! The courtyard tree only reaches the ground floor!' A black-and-white photo is ", (None, '흑백'), ", built from the old words for 'black' and 'white'."]),
    (1, None, ["'Madam, please read the back of that blue postcard.' The back side of a card or page is ", (None, '뒷면을'), ", from 'back' and 'face'."]),
    (2, None, ["'May tenth, thirty years ago. Every Friday at six, tea and piano in Room Nine.' Korean months are just numbers plus 'month', so May is ", (None, '오월'), ", 'month five'."]),
    (4, None, ["'Look at the next card too: Please save two corner chairs for the baker and the teacher.' A baker is ", (None, '제빵사와'), ", from 'make', 'bread' and 'expert', with 'and' tagged on."]),
    (5, None, ["'How lovely. Thirty years ago this house was already bringing neighbours together.' Your neighbours are ", (None, '이웃들을'), ', a warm everyday word with a plural ending.']),
    (8, None, ["'Six days to wash the glass, paint the shutters and bake lemon tarts!' Sora strings jobs together with a little ending meaning 'and': ", (None, '닦고, 덧문 칠하고'), '.']),
    (9, None, ["'If you wake up that silent middle key, Junho, I will gladly play at six.' The word ", (None, '기꺼이'), " means 'gladly, with pleasure', a lovely word for saying yes."]),
    (10, None, ["'Deal, it's a promise! Let's go tell Mina and the boss our Friday plan!' Going somewhere to do something is the reusable chunk ", (None, '말하러 가요'), ", 'go to tell'."]),
]
