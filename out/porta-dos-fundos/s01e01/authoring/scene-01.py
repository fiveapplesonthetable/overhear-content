ID = 'porta-dos-fundos-s01e01-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'porta-dos-fundos', 1, 1, 1
TITLE = 'Bora pra reunião  (The Meeting — Brazilian Portuguese Taster)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'colega': 'Colega', 'financeiro': 'Funcionário'}
SOURCE_NAME = 'Porta dos Fundos — VEM PRA REUNIÃO, official sketch, 2026-01-05'
SOURCE_FILE = 'sources/porta-dos-fundos/s01/e01.pt.srt'
SOURCE_NOTE = 'One short Brazilian Portuguese adaptation of a single official workplace sketch. Complete native automatic captions retained; independent source audio verification recorded in SOURCE-REVIEW before approval. S01E01 is this learning collection slot, not an original channel episode number.'
INTRO = ('This is a Brazilian Portuguese taster from an office comedy sketch. A colleague invites a finance employee to a marketing meeting. The employee does not think he needs to go. We have shortened their exchange for beginners. Listen first, then we will go through it together.')
OPENER = 'The invitation sounds casual. The refusal is polite, but the colleague keeps asking.'
TRANSITION = 'Now hear the short exchange once more.'
OUTRO = ('The employee says he is not going to be at the meeting, but still thanks his colleague. He explains that the meeting concerns marketing and he works in finance. Practice the invitation and the question about going, then the short refusal. See you next time!')
CLOSING = ('financeiro', 'Até logo!')
STORY = [
 ('colega','Bora pra reunião.',"Let's go to the meeting.",[(7,'bora pra reunião')],''),
 ('financeiro','Não vou estar nessa reunião, não. Mas valeu.',"I'm not going to be at that meeting. But thanks.",[(15,'não vou estar nessa reunião'),(15,'não. Mas valeu')],'Omit Ah and the first repeated não, plus the following extra thanks/address. Keep the original future expression and reinforcing final negative.'),
 ('colega','Você não vai pra reunião?',"Aren't you going to the meeting?",[(19,'Você não vai pra reunião')],'Shortened confirmation question; no meaning added.'),
 ('financeiro','É reunião de marketing. Eu sou do financeiro.',"It's a marketing meeting. I'm in finance.",[(19,'é reunião'),(21,'de marketing'),(21,'Eu sou do financeiro')],'Simplify the marketing-planning meeting to a marketing meeting; omit the connecting porque and following explanation about having no reason to attend.')
]
WALK = [
 (0,None,"'Let's go to the meeting.' The opening word is an informal invitation to do something together. The next word is a shortened everyday form meaning to or for. Here it gives the destination. The last word means meeting; its final nasal sound is part of the word, not a separate ending to skip."),
 (1,None,"'I'm not going to be at that meeting. But thanks.' The speaker places a negative at the start and repeats it at the end for emphasis. This is common in conversational Brazilian Portuguese. The last word is a casual way to say thanks here; it does not mean that he accepts the invitation."),
 (2,None,"'Aren't you going to the meeting?' There is no extra question word. The questioning voice asks the employee to confirm his refusal. The opening word refers to the person being addressed, but it takes a third-person verb form. That is why the form for going differs from the earlier one used by the speaker about himself."),
 (3,None,"'It's a marketing meeting. I'm in finance.' The first sentence names the kind of meeting. In the second, the employee identifies his department. Literally, he says that he is from the finance department. The joined word before the department combines a linking word with the masculine article. His department is the reason he gives for declining.")
]
