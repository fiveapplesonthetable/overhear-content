# Authoring module for haessal-guesthouse-s01e01-scene-08.
ID = 'haessal-guesthouse-s01e01-scene-08'
SHOW = 'haessal-guesthouse'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = '계단 위의 가방  (Left on the Step)'
LEVEL = 'A1 — beginner'
PAIR = 'ko-en'
LABELS = {'mina': '미나', 'junho': '준호'}
INTRO = 'It is almost nine in the evening, and the courtyard lanterns glow softly as Mina finishes her first day with Junho. Suddenly, the front gate bell rings once in the quiet night. Listen first.'
OPENER = "Let's step outside and unpack each line slowly."
TRANSITION = "Now let's listen to the final scene of Episode 1 again from start to finish."
OUTRO = "Miss Youngmi's suitcase is back, yet the mystery stranger vanished into the night asking them to keep his bag until Friday. Episode 1 is complete—see you next time for Episode 2!"
CLOSING = ('junho', '안녕히 가세요!')
STORY = [
    ('mina', '준호 씨, 방금 들었어요? 누가 대문 종을 눌렀어요!', 'Junho, did you just hear that? Someone rang the front gate bell!'),
    ('junho', '밤 아홉 시요? 잠깐만요, 대문을 같이 열어요.', "At nine at night? Wait, let us open the gate together."),
    ('mina', '계세요? 안녕하세요! 대문에 아무도 없어요!', 'Hello? Good evening! Nobody is standing at the gate!'),
    ('junho', '잠깐만요. 아래 돌계단을 보세요.', 'Wait a second. Look down at the stone step.'),
    ('mina', '또 남색 가방이에요! 이게 영미 선생님 가방이에요?', "Another dark-blue bag! Is this Miss Youngmi's bag?"),
    ('junho', '지퍼를 확인해 보세요... 네, 선생님 이름 글자가 여기 있어요!', 'Check the zipper... yes, her initials are right here!'),
    ('mina', '왜 자기 가방은 안 가져가고 그냥 도망갔을까요?', 'Why did the person run away without taking their own bag?'),
    ('junho', '보세요, 손잡이에 접힌 하얀 봉투가 붙어 있어요.', 'Look, there is a folded white envelope taped to the handle.'),
    ('mina', "제가 읽어 볼게요. '실수해서 죄송합니다. 금요일까지 제 파란 가방을 맡아 주세요.'", "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'"),
    ('junho', '금요일까지요? 이름도 없고 서명도 없네요!', 'Until Friday? No name and no signature!'),
    ('mina', '왜 모르는 사람들한테 금요일까지 구두하고 나무 기차를 맡길까요?', 'Why leave shoes and a wooden train with strangers until Friday?'),
    ('junho', '햇살 하우스에 온 걸 환영해요, 미나 씨. 내일 둘째 날도 심심하지 않겠네요.', "Welcome to Sunshine House, Mina. Your second day tomorrow won't be boring either."),
]
WALK = [
    (0, None, ["'Junho, did you just hear that? Someone rang the front gate bell!' Placing ", (None, '방금'), ' before an action points to what happened just seconds ago.']),
    (1, None, ["'At nine at night? Wait, let us open the gate together.' Notice how ", (None, '같이'), " is spelled with a 't' sound at the bottom yet pronounced 'gachi' in natural speech, meaning 'together'."]),
    (3, None, ["'Wait a second. Look down at the stone step.' Joining 'stone' and 'stairs' builds ", (None, '돌계단을'), ' in one crisp compound.']),
    (6, None, ["'Why did the person run away without taking their own bag?' Wondering aloud softly uses the ending on ", (None, '도망갔을까요'), ', inviting the listener to guess along with you.']),
    (7, None, ["'Look, there is a folded white envelope taped to the handle.' Envelopes and paper bags share the word ", (None, '봉투가'), ' in everyday Korean.']),
    (8, None, ["'Let me read it: Sorry for the mistake. Please keep my blue bag until Friday.' Asking a desk clerk to hold or guard luggage uses ", (None, '맡아 주세요'), ", 'please keep it in your care'."]),
    (9, None, ["'Until Friday? No name and no signature!' Days of the week end in 'day', and ", (None, '금요일까지요'), " pairs 'gold day'—Friday—with 'until'."]),
    (11, None, ["'Welcome to Sunshine House, Mina. Your second day tomorrow won't be boring either.' Notice the show's Korean name, ", (None, '햇살'), ', which means warm rays of sunshine.']),
]
