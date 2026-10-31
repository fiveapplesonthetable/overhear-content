"""One genuine continuous E01 taster. Original show media is private; public speech is validated TTS."""
ID = 'the-producers-s01e01-scene-01'
FORMAT = 'taster'
PAIR = 'ko-en'
SHOW = 'the-producers'
SEASON = EPISODE = SCENE = 1
TITLE = '왜 뛰세요?  (Why Are You Running?)'
LEVEL = 'A1 — Duolingo Section 2'
LABELS = {'seungchan': '백승찬', 'camera_pd': '촬영자'}
SOURCE_NAME = '프로듀사 (The Producers), KBS2015 E01, official Part1'
SOURCE_FILE = 'sources/the-producers/s01/e01.ko.srt'
SOURCE_NOTE = ('Original Korean audio independently decoded without prompts by cached small and large models. '
               'The complete official Part1 automatic-caption track is retained with explicit bounded opening corrections; '
               'outside the opening it remains unreviewed automatic ASR. No English backtranslation or human-listening certificate.')
INTRO = ('Outside KBS, a camera operator stops a new employee on his first day. He is in a hurry. '
         'Listen for a polite question about why he is running, then the reason he gives.')
STORY = [
 ('camera_pd', 'KBS 신입사원이시죠?', "You're a new KBS employee, right?", [(7, 'KBS 신입사원이시죠?')], 'Camera operator confirms the newcomer\'s status; original audio resolves the automatic caption\'s missing ending.'),
 ('seungchan', '아, 네.', 'Ah, yes.', [(8, '아, 네.')], ''),
 ('camera_pd', '왜 뛰세요?', 'Why are you running?', [(9, '왜 뛰세요?')], 'Native caption and large source decoder agree 뛰세요; small\'s 띄세요 is rejected against the other readings and visible running.'),
 ('seungchan', '아, 저 입사식 하는데요.', 'Ah, I have an induction ceremony.', [(10, '아, 저 입사식 하는데요.')], 'Standard spacing; the English uses have for the scheduled event, not a claim that he organizes the ceremony.'),
 ('seungchan', '늦은 거 같아가지고.', "Because I think I'm late.", [(11, '늦은 거 같아가지고.')], 'Preserve actual colloquial 거 and the spoken reason link, corroborated by native caption and large; small normalizes 거 to 것.'),
]
OPENER = 'Now take those five short turns one at a time.'
WALK = [
 (0, None, "'You're a new KBS employee, right?' The camera operator checks Seung-chan's new-employee status. The word for new employee combines newly joining with company staff. Its final sounds politely invite confirmation."),
 (1, None, "'Ah, yes.' His short yes confirms the question. The little word at the start is a natural reaction while he catches his breath. The same acknowledgement works when someone checks an appointment."),
 (2, None, "'Why are you running?' The first word means why and asks for the reason. The other word addresses the running person with respect. Keep those final sounds when you ask a stranger a question."),
 (3, None, "'Ah, I have an induction ceremony.' The short word for I is used when speaking respectfully. The ceremony word joins the ideas of entering a company and a formal event. He gives this as background to his hurry."),
 (4, None, "'Because I think I'm late.' The word for being late carries the main news. The phrase around it presents his own impression, then links that impression back to the question about running. The small spoken word in the middle means a thing or fact."),
]
TRANSITION = 'Listen to the whole exchange again, from the question to his explanation.'
OUTRO = 'A quick yes, a respectful question, and a reason for being in a hurry. That is your first Korean listen from The Producers.'
CLOSING = None
