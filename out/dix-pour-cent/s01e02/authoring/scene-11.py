# Authoring module for dix-pour-cent-s01e02-scene-11.
ID = 'dix-pour-cent-s01e02-scene-11'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = 'Un film ne meurt jamais  (A Film Never Dies)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'emma': 'Emma'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ("Emma, the producer of Gabor's film, confronts Andréa after Françoise has withdrawn. Michel Piccoli refuses "
 'to act without her, and years of work may collapse. Andréa promises to bring Françoise back, then '
 'struggles to record an apology on her voicemail. First, listen to the argument in French.')
OPENER = "Let's go back through it. Emma comes straight in with what Françoise told her."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = 'A rough morning for Andréa, but you came through it fine. See you next time!'
CLOSING = ('andrea', 'Bon courage!')
STORY = [('emma',
  'Françoise a appelé. Elle dit que vous étiez odieuse.',
  'Françoise phoned. She says you were horrible.',
  [(325, 'Françoise a appelé, elle dit que vous étiez odieux')],
  'Feminine odieuse explicitly agrees with Andréa as the formal singular addressee, replacing the ambiguous '
  'masculine source spelling.'),
 ('andrea',
  "C'est tellement malhonnête! Elle avait déjà pris sa décision.",
  "That's so dishonest! She'd already made her decision.",
  [(326, "C'est tellement malhonnête ! Elle avait déjà pris sa décision")],
  ''),
 ('emma',
  'Et Piccoli ne fait pas le film sans Françoise.',
  "And Piccoli won't do the film without Françoise.",
  [(327, 'Piccoli')],
  "Condenses Piccoli's reported condition into a direct statement."),
 ('emma',
  'Sans Samuel, vous vous effondrez!',
  "Without Samuel, you're falling apart!",
  [(328, 'Sans Samuel, vous vous effondrez')],
  ''),
 ('andrea', "C'est vraiment bas, Emma.", "That's really low, Emma.", [(329, "c'est vraiment bas, Emma")], ''),
 ('emma',
  'Je travaille sur ce projet depuis quatre ans!',
  "I've been working on this project for four years!",
  [(330, 'Je travaille sur ce projet depuis quatre ans')],
  ''),
 ('emma',
  'Mais ce film est mort.',
  'But this film is dead.',
  [(333, 'est mort')],
  'Makes the film explicit instead of using the source pronoun.'),
 ('andrea',
  "Non, c'est Samuel qui est mort.",
  "No, it's Samuel who is dead.",
  [(334, "Non, c'est Samuel qui est mort")],
  ''),
 ('andrea', 'Un film ne meurt jamais!', 'A film never dies!', [(335, 'Un film ne meurt jamais')], ''),
 ('andrea',
  'On va trouver une solution.',
  "We'll find a solution.",
  [(336, 'On va trouver une solution')],
  ''),
 ('emma',
  'Une solution? Une grande actrice de quatre-vingts ans, libre dans trois semaines?',
  'A solution? A great eighty-year-old actress, free in three weeks?',
  [(338, 'Une grande actrice de'), (339, 'libre dans trois semaines')],
  "Drops the source asides about Gabor's taste and the actress's health."),
 ('andrea',
  "On n'est pas obligés de remplacer Françoise Fabian.",
  "We don't have to replace Françoise Fabian.",
  [(340, "On n'est pas obligés de remplacer Françoise Fabian")],
  ''),
 ('andrea',
  "Je vais la convaincre de revenir. J'en suis capable.",
  "I'm going to persuade her to come back. I can do it.",
  [(341, 'Je vais la convaincre de revenir'), (342, "J'en suis capable")],
  ''),
 ('andrea',
  "Allô, Françoise, c'est Andréa Martel.",
  "Hello, Françoise, it's Andréa Martel.",
  [(343, "Allô, Françoise, c'est Andréa Martel")],
  ''),
 ('andrea',
  "Je voudrais m'excuser pour hier.",
  "I'd like to apologise for yesterday.",
  [(344, "Je voudrais m'excuser pour hier")],
  ''),
 ('andrea',
  "J'ai une grande admiration pour vous.",
  'I have great admiration for you.',
  [(352, "J'ai une grande admiration pour vous")],
  ''),
 ('andrea',
  'Je me sens vraiment... nulle!',
  'I really feel... useless!',
  [(354, 'Je me sens vraiment... nulle')],
  ''),
 ('andrea',
  "Réservez-moi un massage, s'il vous plaît.",
  'Book me a massage, please.',
  [(359, "Réservez-moi un massage, s'il vous plaît")],
  '')]
WALK = [(0,
  'Françoise a appelé.',
  "'Françoise phoned.' The past with 'has' plus the action word, the everyday way to say something "
  'happened.'),
 (0,
  'Elle dit que vous étiez odieuse.',
  "'She says you were horrible.' Emma uses formal you to Andréa. The description has a feminine ending "
  "because it describes Andréa, a woman. It criticises someone's behaviour as obnoxious, not merely untidy "
  'or unskilled.'),
 (1,
  "C'est tellement malhonnête!",
  "'That's so dishonest!' The long word in the middle means 'so', 'so very'."),
 (1,
  'Elle avait déjà pris sa décision.',
  "'She'd already made her decision.' In French you 'take' a decision, you don't make one. Emma has worse "
  'news.'),
 (2,
  None,
  "'And Piccoli won't do the film without Françoise.' The French present describes a refusal that governs "
  'the future: he does not do it without her. Without introduces the person he insists on having in the '
  'cast.'),
 (3,
  None,
  "'Without Samuel, you're falling apart!' You hear the word for 'you' twice: once as the subject, once as "
  "'yourselves', because this action word always comes with a 'self'."),
 (4,
  None,
  "'That's really low, Emma.' Low is about moral behaviour here, not physical height. Andréa thinks Emma is "
  "being unfair by invoking Samuel's death, and really strengthens the accusation."),
 (5,
  None,
  "'I've been working on this project for four years!' Here is a key pattern: French uses the present, plus "
  "a word meaning 'since', for something that started in the past and is still going on. Literally 'I work "
  "on it since four years'."),
 (6,
  None,
  "'But this film is dead.' Dead is a metaphor for a project that cannot continue. The description has a "
  'masculine shape because film is masculine; Emma is declaring the production finished.'),
 (7,
  None,
  "'No, it's Samuel who is dead.' The pattern it is someone who puts the emphasis on that person. Andréa "
  'insists on the literal meaning of dead: Samuel has died, but the film can still be saved.'),
 (8,
  None,
  "'A film never dies!' Not, then the action word, then 'never' instead of the usual second half. Andréa's "
  'battle cry.'),
 (9,
  None,
  "'We'll find a solution.' The verb 'to go' plus another verb is the near future: we are going to find. "
  'Emma repeats it back to her, mockingly.'),
 (10,
  None,
  "'A solution? A great eighty-year-old actress, free in three weeks?' In French you say 'an actress of "
  "eighty years'. Emma thinks no such person exists."),
 (11,
  None,
  "'We don't have to replace Françoise Fabian.' Literally 'we are not obliged to replace'. The word for "
  "'obliged' takes a plural ending, because 'we' is plural."),
 (12,
  'Je vais la convaincre de revenir.',
  "'I'm going to persuade her to come back.' The near future once more, and the tiny word for 'her' sits "
  'right before the verb it belongs to.'),
 (12,
  "J'en suis capable.",
  "'I can do it.' Literally, I am capable of it. The short word before am stands for of it and refers to "
  'persuading Françoise to return. English can use can here instead of capable. Emma leaves, and Andréa '
  'tries her voicemail.'),
 (13,
  None,
  "'Hello, Françoise, it's Andréa Martel.' On the phone, this is how you say who's calling: it's me, "
  'Andréa.'),
 (14,
  None,
  "'I'd like to apologise for yesterday.' This 'would like' is the polite form of 'want'. But the message "
  'goes wrong, she gets tangled up, and the voicemail robot offers to let her record it again. She tries a '
  'second time.'),
 (15,
  None,
  "'I have great admiration for you.' The word for 'great' comes before the noun, and it's feminine to match "
  "'admiration'."),
 (16,
  None,
  "'I really feel... useless!' Here feel comes with the small self word, unlike feeling an object move. "
  'Useless has a feminine ending because Andréa describes herself. She is calling herself hopeless after '
  'struggling with the voicemail.'),
 (17,
  None,
  "'Book me a massage, please.' Andréa gives a polite command to her assistant and adds 'please', literally "
  "'if it pleases you'. After a morning like this, who can blame her? Okay. Now the whole thing again, from "
  "Emma's first line.")]
