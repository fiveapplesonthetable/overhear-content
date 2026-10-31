SOURCE_NOTE = 'French dialogue is an A1 abridgment. Original video confirms speakers and setting; unprompted original-audio transcription confirms the address forms. Dual subtitles provide scene locators.'
# Authoring module for dix-pour-cent-s01e01-scene-08.
ID = 'dix-pour-cent-s01e01-scene-08'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Andréa engage Camille  (Andréa Hires Camille)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'camille': 'Camille'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ('After Magali leaves, Andrea needs a new assistant, and Sofia has turned the job down. She brings Camille '
 'into her office for an impromptu interview. Listen to the French first; you can follow the questions '
 'without catching every word.')
OPENER = "Let's follow the interview. Andrea begins with a question that sounds almost like an order."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("Camille has found a job, and you have heard several ways to ask about someone's background and "
 "availability. Listen again for the different uses of 'come'; see you next time.")
CLOSING = ('camille', 'À bientôt!')
STORY = [('andrea',
  'Vous venez?',
  'Are you coming?',
  [(251, 'Tu viens, oui ou non ?')],
  'A1 question preserves the initial polite address confirmed by original audio.'),
 ('andrea',
  "Vous venez d'où?",
  'Where are you from?',
  [(252, "Tu viens d'où ?")],
  'A1 question preserves the initial polite address confirmed by original audio.'),
 ('camille',
  "Je viens de la Côte d'Azur. Près de Cannes.",
  "I'm from the Côte d'Azur. Near Cannes.",
  [(253, "Je viens... de la Côte d'Azur"), (254, 'Près de Cannes')],
  ''),
 ('andrea',
  'Cannes? Vous avez travaillé au festival?',
  'Cannes? Did you work at the festival?',
  [(255, 'Cannes ? Tu as travaillé au festival ?')],
  'A1 question preserves the initial polite address confirmed by original audio.'),
 ('camille',
  'Oui, exactement. Le Festival de Cannes.',
  'Yes, exactly. The Cannes Film Festival.',
  [(256, 'Oui, exactement. Le Festival de Cannes')],
  ''),
 ('andrea', 'Pour faire quoi?', 'Doing what?', [(257, 'Pour faire quoi ?')], ''),
 ('camille',
  "Ça dépend. Au début, j'étais dans les sous-vêtements des stars.",
  'It depends. At first, I worked with celebrity underwear.',
  [(258, 'Ça dépend. Au début'), (259, "J'étais dans les sous-vêtements"), (260, 'des stars')],
  ''),
 ('camille',
  'Ne pleurez pas, on va arranger ça!',
  "Don't cry, we're going to fix this!",
  [(264, 'Pleurez pas. On va arranger ça')],
  ''),
 ('andrea',
  'Vous avez un petit ami?',
  'Have you got a boyfriend?',
  [(270, 'Tu as un petit ami ?')],
  'A1 question preserves the initial polite address confirmed by original audio.'),
 ('camille', 'Non.', 'No.', [(270, 'Non')], ''),
 ('andrea', 'Des amis à Paris?', 'Friends in Paris?', [(272, 'Des amis à Paris ?')], ''),
 ('camille',
  "Non, je viens d'arriver. Mon père, mais c'est compliqué.",
  "No, I've just arrived. My dad, but it's complicated.",
  [(273, "Non, je viens d'arriver"), (274, "Mon père, mais c'est compliqué")],
  ''),
 ('andrea',
  'Vous vous occupez de lui?',
  'Do you look after him?',
  [(275, "Tu t'occupes de lui ?")],
  'A1 question preserves the initial polite address confirmed by original audio.'),
 ('camille', 'Hors de question!', 'No way!', [(276, 'Hors de question')], ''),
 ('andrea',
  "Je peux t'appeler à quatre heures du matin? Tu travailles le dimanche?",
  'Can I call you at four in the morning? Do you work on Sundays?',
  [(278, "Je peux t'appeler"), (278, 'à quatre heures du matin'), (279, 'le dimanche')],
  ''),
 ('camille',
  'Oui, oui.',
  'Yes, yes.',
  [(281, 'Oui, oui')],
  'Only the answers to the two retained questions are kept.'),
 ('andrea',
  'Très bien. Tu peux commencer maintenant?',
  'Very good. Can you start now?',
  [(283, 'Très bien'), (284, 'Tu peux commencer maintenant ?')],
  ''),
 ('camille', 'Oui, maintenant!', 'Yes, right now!', [], '')]
WALK = [(0,
  None,
  "'Are you coming?' Andrea initially uses the polite address with Camille. The form of 'come' follows that "
  'address, even though she is speaking to one person.'),
 (1,
  None,
  "'Where are you from?' The same action now combines with a question meaning 'from where'. The question "
  'word comes after the action in this everyday spoken order.'),
 (2,
  None,
  "'I'm from the French Riviera. Near Cannes.' To say where she comes from, Camille puts a place after the "
  "small word meaning 'from'. The second sentence adds a more precise location with 'near'."),
 (3,
  None,
  "'Cannes? Did you work at the festival?' This is the everyday past: a form of 'to have' plus 'worked'. "
  "Camille isn't going to let a good chance go."),
 (4,
  None,
  "'Yes, exactly. The Cannes Film Festival.' The adverb meaning 'exactly' confirms Andrea's guess. Its "
  'familiar sound gives you a useful clue to the meaning.'),
 (5,
  None,
  "'Doing what?' The plain action 'do' is followed by 'what'. This short follow-up asks which job Camille "
  'did, rather than whether she worked there.'),
 (6,
  'Ça dépend.',
  "'It depends.' The verb is in the singular because the subject is 'it'. As in English, this short reply "
  'can stand on its own while someone thinks of an answer.'),
 (6,
  "Au début, j'étais dans les sous-vêtements des stars.",
  "'At first, I worked with celebrity underwear.' Literally, she says she 'was in' that kind of clothing. "
  "The past form of 'be' describes her supposed area of work, and 'at first' places it earlier in her "
  'story.'),
 (7,
  None,
  "'Don't cry, we're going to fix this!' Camille imitates what she would tell a star. The polite command is "
  "negative; after it, 'go' plus the plain action 'fix' promises an immediate solution."),
 (8,
  None,
  "'Have you got a boyfriend?' The expression literally combines 'little' and 'friend'. Together, the two "
  'words can mean boyfriend rather than a friend who is small.'),
 (9, None, "'No.' That's the first of many short answers. Andréa moves on."),
 (10,
  None,
  "'Friends in Paris?' Both the word for 'friends' and the small word before it are plural. Andrea leaves "
  'out a verb because the question is clear from the conversation.'),
 (11,
  "Non, je viens d'arriver.",
  "'No, I've just arrived.' 'Come' followed by 'from' and an action describes something that has just "
  'happened. Here Camille is explaining why she has no friends in Paris yet.'),
 (11,
  "Mon père, mais c'est compliqué.",
  "'My dad, but it's complicated.' The possessive matches a masculine noun because she is naming her father. "
  "The connecting word 'but' warns that having him in Paris does not make things simple."),
 (12,
  None,
  "'Do you look after him?' The expression for 'look after' needs a small word meaning 'of' before the "
  "person. The last word is the form of 'him' used after a preposition."),
 (13, None, "'No way!' Literally 'out of the question'. Andréa likes that. Then she gets to the real test."),
 (14,
  None,
  "'Can I call you at four in the morning? Do you work on Sundays?' Andrea now switches to the familiar "
  "address as she sets out the job's demands. A day with the article can describe a regular weekly habit."),
 (15,
  None,
  "'Yes, yes.' The repeated answer confirms both requests Andrea has just made. Camille accepts both without "
  'hesitation.'),
 (16,
  None,
  "'Very good. Can you start now?' 'Can' is followed straight away by the plain action 'start'. The final "
  'word makes the offer immediate.'),
 (17,
  None,
  "'Yes, right now!' The time word is the same one Andrea has just used. Camille repeats it to show that she "
  'is ready without any delay.')]
