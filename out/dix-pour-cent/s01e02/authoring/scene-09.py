# Authoring module for dix-pour-cent-s01e02-scene-09.
ID = 'dix-pour-cent-s01e02-scene-09'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = 'Quelque chose de fort  (Something Powerful)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'line': 'Line'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = ('Lunch continues with Line Renaud and Gabriel. She wants a film role with energy and substance, despite the '
 "shortage of big parts for women her age. Gabriel knows that Françoise Fabian has withdrawn from Gabor's "
 'film and begins to suggest it to Line. First, listen to their exchange in French.')
OPENER = "Let's take it line by line. Line starts with a warm word about her old friend Samuel."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("That's the end of lunch, and the start of a lot of trouble for Gabriel. Listen for the casual and the "
 "polite 'you' going in opposite directions when you watch. See you next time!")
CLOSING = ('line', 'Au revoir, Gabriel!')
STORY = [('line',
  'Samuel était un excellent agent.',
  'Samuel was an excellent agent.',
  [(263, 'Samuel était un excellent agent')],
  ''),
 ('line',
  'Mais les grands rôles sont rares pour une femme de mon âge.',
  'But big parts are rare for a woman my age.',
  [(264, 'pour une femme de mon âge')],
  'Replaces the idiom ne courent pas les rues with the straightforward sont rares.'),
 ('line',
  "Je veux du mouvement, de l'action, de l'énergie!",
  'I want movement, action, energy!',
  [(268, "Je veux du mouvement, de l'action, de l'énergie")],
  ''),
 ('line',
  'Trouve-moi quelque chose de fort! Tu me suis?',
  'Find me something powerful! Do you follow me?',
  [(269, 'quelque chose de fort'), (271, 'Tu me suis')],
  'Changes the request I want you to find me into a direct command.'),
 ('gabriel',
  'Oui. Line, on a un super projet en ce moment.',
  'Yes. Line, we have a great project right now.',
  [(272, 'Oui'), (274, 'Line, on a un super projet en ce moment')],
  ''),
 ('gabriel', "J'ai pensé à vous.", 'I thought of you.', [(275, "J'ai pensé à vous")], ''),
 ('line', 'Vraiment?', 'Really?', [(276, 'Vraiment')], ''),
 ('gabriel',
  "C'est un film de Gabor Rajevski, avec Michel Piccoli.",
  "It's a film by Gabor Rajevski, with Michel Piccoli.",
  [(279, "C'est un film de Gabor Rajevski"), (277, 'Avec Michel Piccoli')],
  ''),
 ('line', "J'adore Michel!", 'I adore Michel!', [(278, "J'adore Michel")], ''),
 ('gabriel',
  "C'est l'histoire d'un vieux couple qui fait des braquages.",
  "It's the story of an old couple who do hold-ups.",
  [(289, "C'est l'histoire d'un vieux couple"), (290, 'braquages')],
  'Condenses the longer plot summary without changing the bank robberies.'),
 ('line',
  'Magnifique! Pourquoi tu as pensé à moi?',
  'Wonderful! Why did you think of me?',
  [(295, 'Magnifique'), (299, 'pensé à moi')],
  'Simplifies the spoken question while retaining original familiar tu; the dual subtitles had incorrectly '
  'changed the source to vous.'),
 ('gabriel',
  'Parce que le rôle est puissant, plein de vie!',
  'Because the part is powerful, full of life!',
  [(301, 'puissant')],
  'Makes the referent rôle explicit and simplifies vibrant de vie to plein de vie.'),
 ('gabriel',
  'Et le tournage commence dans trois semaines.',
  'And shooting starts in three weeks.',
  [(302, 'Et le tournage commence dans trois semaines')],
  ''),
 ('line',
  'Trois semaines? Pourquoi si tôt?',
  'Three weeks? Why so soon?',
  [(303, 'Trois semaines'), (304, 'Pourquoi si tôt')],
  ''),
 ('gabriel',
  'Au départ, Françoise Fabian devait prendre le rôle.',
  'At first, Françoise Fabian was supposed to take the part.',
  [(305, 'Françoise Fabian devait prendre le rôle')],
  ''),
 ('gabriel',
  'Elle était juste un peu fatiguée.',
  'She was just a bit tired.',
  [(309, 'elle était juste un peu')],
  ''),
 ('line',
  'Line Renaud dans un film de Gabor Rajevski?',
  'Line Renaud in a Gabor Rajevski film?',
  [(310, 'Line Renaud dans un film de Gabor Rajevski')],
  ''),
 ('line',
  'Je trouve que ça sonne vraiment bien. Pourquoi pas?',
  'I think that sounds really good. Why not?',
  [(311, 'Je trouve que ça sonne vraiment bien'), (312, 'Pourquoi pas')],
  '')]
WALK = [(0,
  None,
  "'Samuel was an excellent agent.' The action word is 'to be' in the past form used for describing how "
  'things were. Then she gets to the point.'),
 (1,
  None,
  "'But big parts are rare for a woman my age.' Literally, of my age. Big describes important roles rather "
  'than their physical size. My follows the gender of age, which is masculine, even though Line herself is a '
  'woman.'),
 (2,
  None,
  "'I want movement, action, energy!' Notice the little words in front of each noun. They mean 'some': "
  'French puts them in where English puts nothing. The form changes with the noun: masculine, or shortened '
  'before a vowel.'),
 (3,
  'Trouve-moi quelque chose de fort!',
  "'Find me something powerful!' Line gives a casual command, with 'me' stuck on after a hyphen."),
 (3,
  'Tu me suis?',
  "'Do you follow me?' Follow means understand the thought here, just as in English. The action word has the "
  'same spelling as am after I, but here the subject you and the sense make it follow, not be.'),
 (4,
  None,
  "'Yes. Line, we have a great project right now.' The little word for 'we' in everyday French is the same "
  "one that can mean 'people' in general."),
 (5,
  None,
  "'I thought of you.' And here's something to notice: Gabriel says the polite 'you' to her. She calls him "
  'the casual way, he stays respectful. A younger agent with a legend, that feels right.'),
 (6,
  None,
  "'Really?' The same word can strengthen a description, as in really good, or stand alone to ask if "
  "something is true. Line's rising voice makes it a surprised question."),
 (7,
  None,
  "'It's a film by Gabor Rajevski, with Michel Piccoli.' By introduces the film's director, while with "
  'introduces a member of the cast. French uses different short linking words for those two relationships.'),
 (8,
  None,
  "'I adore Michel!' The word for 'I' loses its vowel and sticks to the verb, because the verb starts with a "
  'vowel: a very common French sound.'),
 (9,
  None,
  "'It's the story of an old couple who do hold-ups.' Couple is singular in French, so the following action "
  'uses the singular form too, even though two people are involved. A hold-up here is an armed robbery, not '
  'a delay.'),
 (10,
  'Magnifique!',
  "'Wonderful!' Line exclaims with an easy word that sounds just like the English 'magnificent'."),
 (10,
  'Pourquoi tu as pensé à moi?',
  "'Why did you think of me?' The past of 'think' is made with 'have' plus a form of the verb, just like 'I "
  "have thought'. Gabriel has to think fast."),
 (11,
  None,
  "'Because the part is powerful, full of life!' Full is followed by of and what fills the part: life. The "
  'image describes a vivid, energetic role, rather than simply saying it is a long or important one.'),
 (12,
  None,
  "'And shooting starts in three weeks.' The little word before 'three weeks' means 'in', counting forward "
  'from now.'),
 (13,
  None,
  "'Three weeks? Why so soon?' So strengthens soon here. The same little word can also mean if in a "
  'condition or yes when contradicting a negative, but neither of those meanings fits this question.'),
 (14,
  None,
  "'At first, Françoise Fabian was supposed to take the part.' The verb 'must' in this past form means 'was "
  "supposed to'. Now the truth is out, or half of it."),
 (15,
  None,
  "'She was just a bit tired.' The word for 'tired' has a feminine ending for Françoise. It's a polite "
  'little lie.'),
 (16,
  None,
  "'Line Renaud in a Gabor Rajevski film?' She gives the director's name after the short word of, where "
  'English can place the name before film. She is imagining how that credit would sound on a poster.'),
 (17,
  'Je trouve que ça sonne vraiment bien.',
  "'I think that sounds really good.' Literally 'I find that it sounds'. Using 'find' for 'think' is very "
  'common in opinions.'),
 (17,
  'Pourquoi pas?',
  "'Why not?' Two little words that leave the idea open. Now he only has to tell Andréa. Lovely. Let's hear "
  'the whole lunch again.')]
