"""Scene 25: Over Korean beef, Joon-mo's writers immediately suspect bad news until he promises they keep their jobs."""
ID = "the-producers-s01e01-scene-25"
PAIR = "ko-en"
SHOW = "the-producers"
SEASON = 1
EPISODE = 1
SCENE = 25
TITLE = "저희 왜 한우 사주세요?  (Why Are You Buying Us Korean Beef?)"
LEVEL = "A1 — beginner"
LABELS = {"joonmo": "라준모", "writer": "손지연"}
SOURCE_NAME = "프로듀사 (The Producers) S1.01"
SOURCE_FILE = "sources/the-producers/s01/e01.ko.srt"

INTRO = (
    "At a barbecue restaurant that night, Ra Joon-mo treats his writers to pricey Korean beef — which instantly "
    "tips off Son Ji-yeon that something is wrong with the show. Listen for the terms for 'premium Korean beef' "
    "and 'cast replacement'."
)

STORY = [
    ("writer", "전화해봤는데 지금 마포대교를 건너고 계신대요.", "I called her and she says she's crossing Mapo Bridge right now.", [(983, "전화해봤는데 지금 마포대교를 건너고 계신데요")], "Standardizes indirect quote spelling 계신대요"),
    ("joonmo", "맨날 거길 건너고 있어!", "She's crossing that bridge every single day!", [(985, "맨날 거길 건너고 있어")], ""),
    ("writer", "근데 저희 왜 한우 사주세요? 이상한데.", "Wait, why are you buying us Korean beef? That's suspicious.", [(988, "근데 저희 왜 한우 사주세요?"), (989, "이상한데")], ""),
    ("writer", "우리 없어져요?", "Are we getting cancelled?", [(990, "물이 없어져요?")], "Restores 우리 ('our show / we') from ASR homophone 물이"),
    ("joonmo", "폐지는 아니고 멤버 교체하래.", "It's not a cancellation, they told us to replace the cast.", [(999, "폐지는 아니고 멤버 교체하래")], ""),
    ("writer", "일 좀 두 번 시키지 마요, 피곤해 죽겠는데.", "Please don't make us do the work twice, I'm dead tired.", [(995, "일 좀 두 번 시키지 마요"), (996, "피곤해 죽겠는데")], ""),
    ("writer", "우리는 가는 거 맞아요?", "Is it certain that we writers are staying on?", [(1007, "우리는 가는 거 맞아요?")], ""),
    ("joonmo", "누가 너네 잘린대? 내가 그런 사람이야?", "Who says you're getting cut? Am I that kind of person?", [(1010, "누가 니네 짤린데?"), (1017, "내가 그런 사람이야")], "Standardizes spelling 너네 잘린대"),
]

OPENER = "Let's unpack the eight lines of this smoky barbecue-table confrontation."

WALK = [
    (0, None, "'I called her and she says she's crossing Mapo Bridge right now.' Hours after the afternoon meeting, the head writer is still using the exact same bridge excuse! The opening phrase builds on 'phone' with a helper meaning 'I tried calling her, and...'."),
    (1, None, "'She's crossing that bridge every single day!' Fed up, Joon-mo pairs the lively word meaning 'every single day' with the contracted form of 'that place', joking next that she must live on the bridge."),
    (2, None, "'Wait, why are you buying us Korean beef? That's suspicious.' Much pricier than pork belly, prized domestic Korean beef is reserved for big celebrations — or guilty bad news! Her closing remark comes from the everyday word meaning 'strange' or 'fishy'."),
    (3, None, "'Are we getting cancelled?' Sharp as a tack, Ji-yeon jumps straight to asking literally 'are we disappearing?'. In television talk, 'we' stands in for the show itself."),
    (4, None, "'It's not a cancellation, they told us to replace the cast.' Forced to come clean, Joon-mo contrasts 'cancellation' with the noun for 'replacement'. That short reported-speech ending passes along orders from upstairs: 'they told me to swap them'."),
    (5, None, "'Please don't make us do the work twice, I'm dead tired.' Because she already researched Miss A, Ji-yeon groans with a polite 'please don't make us do it twice'. Remember 'freezing to death' earlier? Here she uses that exact pattern for 'tired to death!'."),
    (6, None, "'Is it certain that we writers are staying on?' Unlike salaried staff producers, freelance writers can lose their income overnight. Here the middle phrase literally means 'going forward together', checked with the tag question 'is that right?'."),
    (7, None, "'Who says you're getting cut? Am I that kind of person?' The verb for getting cut literally means 'get snipped off', Korean's everyday slang for getting fired. Loyal to his crew, Joon-mo bristles with 'am I that kind of person?'."),
]

TRANSITION = "Now let's listen to the whole Korean beef dinner scene again."
OUTRO = "You learned the words for prized Korean beef, when something feels fishy, being tired, and getting cut. One cosy family finale to go!"
CLOSING = ("writer", "안녕히 가세요!")
