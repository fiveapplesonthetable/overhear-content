# Authoring module for haessal-guesthouse-s01e01-scene-06.
ID = 'haessal-guesthouse-s01e01-scene-06'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = '가방 이름표  (The Luggage Tag)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'youngmi': '영미', 'sungmin': '성민'}
INTRO = 'Back at the front desk, Mina, Youngmi, and owner Sungmin lean over the blue suitcase under the desk lamp. Sungmin finally puts his glasses to good use. Listen to the scene first.'
OPENER = "Let's go through the clues on that tag one line at a time."
TRANSITION = "Now let's listen to the whole conversation again from beginning to end."
OUTRO = "No luck at the train station yet, and the mysterious suitcase owner wrote down an address just five minutes away. Next time, Sora steps in to rescue Youngmi's evening."
CLOSING = ('sungmin', '안녕히 가세요!')
STORY = [
    ('sungmin', '아이구, 이런 일이 있나요! 안경을 쓰고 이름표를 볼게요.', 'Dear me, what a mix-up! Let me put on my glasses and read the tag.'),
    ('youngmi', '거기에 이름이나 전화번호가 있어요?', 'Is there a name or a phone number on it?'),
    ('sungmin', '아쉽게도 전화번호는 없네요. 글자 두 개하고 옛날 길 이름만 있어요.', 'Unfortunately there is no phone number. Only two initials and an old street name.'),
    ('mina', '잠깐만요, 그 길은 바로 우리 동네예요! 걸어서 오 분 거리예요!', 'Wait—that street is right here in our neighbourhood! Five minutes on foot!'),
    ('youngmi', '참 신기하네요! 같은 아침 기차를 타고 같은 동네로 왔군요.', 'How strange! We rode the very same morning train to the same neighbourhood.'),
    ('sungmin', '미나 씨, 지금 바로 기차역 분실물 센터에 전화하세요.', 'Mina, call the train station lost-and-found office right away.'),
    ('mina', '지금 걸고 있어요... 여보세요? 혹시 바뀐 파란 가방 신고가 들어왔나요?', 'I am dialling now... Hello? Has anyone reported a swapped blue bag, by chance?'),
    ('youngmi', '제 가방 위쪽 주머니 안에는 빨간 리본이 있다고 말해 주세요!', 'Please tell them my bag has a red ribbon inside the top pocket!'),
    ('mina', '아직 없다고요? 저희 게스트하우스 전화번호하고 주소를 적어 주세요. 감사합니다!', 'Nothing yet? Please write down our guesthouse phone number and address. Thank you!'),
    ('sungmin', '아직 연락이 없군요, 선생님. 정말 죄송합니다.', "No word yet, ma'am. I am truly sorry."),
    ('youngmi', '사장님 잘못이 아니에요. 그래도 저는 지금 입은 코트밖에 없네요!', 'It is not your fault, sir. Still, I have nothing except the coat I am wearing!'),
    ('mina', '잠시만요, 카페에서 소라 언니가 좋은 생각이 있다고 손을 흔들어요!', 'One moment—Sora in the café is waving with a good idea!'),
]
WALK = [
    (0, None, ["'Dear me, what a mix-up! Let me put on my glasses and read the tag.' Whereas shoes took their own verb earlier, Korean puts on glasses, hats, and umbrellas with ", (None, '안경을 쓰고'), '.']),
    (1, None, ["'Is there a name or a phone number on it?' Linking two nouns with 'or' snaps right onto the first word in ", (None, '이름이나'), ", meaning 'a name or'."]),
    (3, None, ["'Wait—that street is right here in our neighbourhood! Five minutes on foot!' Korean speakers warm up 'my neighbourhood' by saying ", (None, '우리 동네예요'), ", literally 'our neighbourhood'."]),
    (6, None, ["'I am dialling now... Hello? Has anyone reported a swapped blue bag, by chance?' Answering or starting a phone call uses ", (None, '여보세요'), ', reserved exclusively for the telephone or calling into an empty doorway.']),
    (6, None, ["'I am dialling now... Hello? Has anyone reported a swapped blue bag, by chance?' Slipping ", (None, '혹시'), " into a question adds a courteous 'by any chance?'."]),
    (9, None, ["'No word yet, ma'am. I am truly sorry.' Sungmin reaches for the formal apology ", (None, '죄송합니다'), ' to show sincere hospitality.']),
    (10, None, ["'It is not your fault, sir. Still, I have nothing except the coat I am wearing!' Combining ", (None, '코트밖에'), " with 'not exist' literally says 'outside of this coat, nothing exists'."]),
    (11, None, ["'One moment—Sora in the café is waving with a good idea!' Notice Mina calls Sora ", (None, '언니가'), ', the warm Korean word a younger woman uses for an older sister or close female colleague.']),
]
