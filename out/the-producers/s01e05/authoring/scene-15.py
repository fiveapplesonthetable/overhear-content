"""Scene 15: I Did Not Recognize You Without Makeup."""
ID = 'the-producers-s01e05-scene-15'
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 5
SCENE = 15
TITLE = '화장을 안 하셔서 몰라봤어요  (I Did Not Recognize You Without Makeup)'
LEVEL = "A1 — beginner"
LABELS = {"cindy": "신디", "joonmo": "라준모", "yejin": "탁예진"}
SOURCE_NAME = "프로듀사 (The Producers) S1.05"
SOURCE_FILE = 'sources/the-producers/s01/e05.ko.srt'

INTRO = 'At the entrance of the barbecue restaurant, Cindy mistakes bare-faced Tak Ye-jin for restaurant staff and apologizes for not recognizing her without makeup. Inside, Ye-jin runs into Ra Joon-mo and joins the 2 Days & 1 Night dinner.'

STORY = [
    ('cindy', '안녕하세요, 저 신디인데 여기 좀 넣어주세요.', 'Hello, I am Cindy—please put these away here for me.', [(337, '안녕하세요'), (338, '신디'), (339, '여기 좀 넣어주세요')], ''),
    ('yejin', '나? 나 뮤직뱅크 탁예진 피디 기억나지?', 'Me? You remember Music Bank producer Tak Ye-jin, right?', [(340, '나'), (341, '나 뮤직뱅크'), (341, '기억나지')], ''),
    ('cindy', '아, 화장을 안 하셔서 몰라봤어요, 죄송해요.', 'Oh, you were not wearing makeup, so I did not recognize you—I am sorry.', [(343, '아'), (344, '화장을 안 하셔서'), (344, '죄송해요')], ''),
    ('cindy', '저희 오늘 여기서 회식 있어서 먼저 들어가 볼게요.', 'We have a team dinner here today, so I will head in first.', [(345, '저희 오늘 여기서 회식 있어서'), (346, '먼저 들어가 볼게요')], ''),
    ('yejin', '아 재수 없어, 진짜 너무 완전 재수 없어!', 'Ugh, how obnoxious—seriously, totally obnoxious!', [(347, '재수없어 진짜 너무 완전')], ''),
    ('joonmo', '어, 너네 팀 일요일에 여기 웬일이야?', 'Oh, what brings your team here on a Sunday?', [(349, '너네 팀'), (349, '여기 웬일이야')], ''),
    ('yejin', '우리도 회의가 있어서, 지난주에 가수 덕분에 내가 또 방통위 가게 생겼잖아.', 'We had a meeting too—thanks to a singer last week, I ended up having to go before the Broadcast Standards Commission.', [(350, '우리도 회의가 있어서'), (351, '지난주에'), (351, '가수 덕분에 내가 또 방통위'), (351, '생겼잖아')], ''),
    ('joonmo', '어, 이쪽으로 와라.', 'Come join us over here.', [(353, '이쪽으로 와라')], ''),
    ('yejin', '아니 됐어요, 반성문 쓰는 팀이랑 축제 분위기의 1박 팀이랑 같이 어울리는 건 좀 그렇지 않아요?', 'No thanks—would it not be awkward for a team writing apology letters to mingle with the festive 2 Days & 1 Night team?', [(354, '아니 됐어요'), (354, '반성문 쓰는 팀이랑 축제 분위기의'), (354, '같이 어울리는 건 좀 그렇지 않아요')], ''),
    ('yejin', '일로 와, 얘들아!', 'Come right over here, everyone!', [(355, '일로 와 얘들아')], ''),
]

OPENER = "Now let's go through it line by line with the English translation."

WALK = [
    (0, None, "'Hello, I am Cindy—please put these away here for me.'"),
    (1, None, "'Me? You remember Music Bank producer Tak Ye-jin, right?'"),
    (2, None, "'Oh, you were not wearing makeup, so I did not recognize you—I am sorry.'"),
    (3, None, "'We have a team dinner here today, so I will head in first.'"),
    (4, None, "'Ugh, how obnoxious—seriously, totally obnoxious!'"),
    (5, None, "'Oh, what brings your team here on a Sunday?'"),
    (6, None, "'We had a meeting too—thanks to a singer last week, I ended up having to go before the Broadcast Standards Commission.'"),
    (7, None, "'Come join us over here.'"),
    (8, None, "'No thanks—would it not be awkward for a team writing apology letters to mingle with the festive 2 Days & 1 Night team?'"),
    (9, None, "'Come right over here, everyone!'"),
]

TRANSITION = "Now let's listen to the whole conversation one last time."
OUTRO = 'Apologizing for not recognizing someone, declining politely for show, and calling your team to a barbecue table gives you lively Korean social banter. See you next time!'
CLOSING = ('yejin', '다음에 봐요!')
