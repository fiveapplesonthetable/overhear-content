SOURCE_NOTE = 'French dialogue is an A1 abridgment. Original video confirms speakers and setting; unprompted original-audio transcription confirms the address forms. Dual subtitles provide scene locators.'
# Authoring module for dix-pour-cent-s01e01-scene-20.
ID = 'dix-pour-cent-s01e01-scene-20'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 20
TITLE = 'Miranda dit non  (Miranda Says No)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'mathias': 'Mathias', 'miranda': 'Miranda'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ("Mathias meets the producer Miranda Jones at a Paris tea room. He hopes to win back Cecile's part, but "
 'Miranda has already made a decision. Listen to the compliments, the argument about age and the sudden '
 'change of subject.')
OPENER = "Let's take it slowly. Mathias starts the way he always does with an important person: with a big compliment."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That's the scene: words like radiant and student change their sound for a woman, and now you can hear the difference. See you next time!"
CLOSING = ('miranda', 'Au revoir, Mathias!')
STORY = [('mathias',
  'Miranda, vous êtes resplendissante.',
  'Miranda, you look radiant.',
  [(584, 'Miranda, vous êtes resplendissante')],
  ''),
 ('mathias',
  'Paris vous va à merveille.',
  'Paris suits you wonderfully.',
  [(585, 'Paris vous va à merveille')],
  ''),
 ('miranda',
  "Merci, Mathias. J'adore Paris!",
  'Thank you, Mathias. I love Paris!',
  [(586, "Merci, Mathias. J'adore Paris")],
  ''),
 ('miranda',
  "J'ai vécu ici quand j'étais étudiante.",
  'I lived here when I was a student.',
  [(587, "quand j'étais étudiante")],
  'Place pronoun expanded to ici.'),
 ('mathias',
  "Nous comprenons l'hésitation de Tarantino.",
  "We understand Tarantino's hesitation.",
  [(590, "Nous comprenons l'hésitation de Tarantino")],
  ''),
 ('miranda',
  'Oui, Quentin a beaucoup de talent.',
  'Yes, Quentin has a lot of talent.',
  [(592, 'Oui, Quentin déborde de talent')],
  'Expression simplified to has a lot of talent.'),
 ('miranda',
  "C'est vraiment dommage pour Cécile.",
  "It's a real shame about Cécile.",
  [(593, "C'est vraiment dommage pour Cécile")],
  ''),
 ('miranda',
  "Mais il veut quelqu'un de moins de trente ans.",
  'But he wants someone under thirty.',
  [(595, "il veut quelqu'un de moins de")],
  'Number written out for speech.'),
 ('mathias',
  'Oui, Cécile est un peu plus âgée.',
  'Yes, Cécile is a little older.',
  [(595, 'Cécile est'), (596, 'un peu plus âgée')],
  ''),
 ('miranda',
  'Un peu? Elle a quarante et un ans.',
  "A little? She's forty-one.",
  [(597, 'Un peu ? Elle a')],
  'Number written out for speech.'),
 ('mathias',
  "Quarante. Elle vient d'avoir quarante ans.",
  "Forty. She's just turned forty.",
  [(598, "Quarante. Elle vient d'avoir")],
  'Number written out for speech.'),
 ('miranda',
  'Elle aura quarante et un ans pour le film.',
  "She'll be forty-one for the film.",
  [(599, 'Elle en aura'), (599, 'quand on tournera le film')],
  'Future age statement condensed; number written out.'),
 ('mathias',
  'Oui, mais elle fait trente ans.',
  'Yes, but she looks thirty.',
  [(600, 'Oui, mais'), (600, 'elle fait')],
  ''),
 ('miranda',
  "Je suis désolée, Mathias, c'est décidé.",
  "I'm sorry, Mathias, it's decided.",
  [(601, "Mathias, c'est décidé")],
  'Feminine apology agrees with Miranda; source transcript uses masculine spelling.'),
 ('mathias',
  "Goûtez un macaron! C'est leur spécialité.",
  "Try a macaron! It's their speciality.",
  [(602, 'un macaron'), (603, "C'est leur spécialité")],
  'Polite suggestion shortened to a polite instruction.'),
 ('miranda', 'Merci.', 'Thank you.', [(603, 'Merci')], '')]
WALK = [(0,
  None,
  "'Miranda, you look radiant.' French literally says 'you are radiant'. Listen for the final consonant in "
  'the feminine description; the masculine version ends sooner.'),
 (1,
  None,
  "'Paris suits you wonderfully.' Mathias uses a set phrase: the city 'goes to you' marvellously. Flattery, "
  'in the smoothest possible French.'),
 (2,
  None,
  "'Thank you, Mathias. I love Paris!' The action word here is 'to adore', and the French use it for things "
  'they like a lot, cities included.'),
 (3,
  None,
  "'I lived here when I was a student.' The word for 'student' takes the feminine ending too, because "
  "Miranda is talking about herself. She jokes that she won't say how long ago that was."),
 (4,
  None,
  "'We understand Tarantino's hesitation.' Mathias uses the word for 'we' to speak for the agency. The "
  "ending of 'understand' matches that subject."),
 (5,
  None,
  "'Yes, Quentin has a lot of talent.' A short word meaning 'of' links 'a lot' to 'talent'. The French noun "
  "can stay singular when talking about someone's ability."),
 (6,
  None,
  "'It's a real shame about Cecile.' The short expression beginning 'it's' introduces disappointment. Here "
  "the word for 'for' naturally becomes English 'about'."),
 (7,
  None,
  "'But he wants someone under thirty.' Literally 'someone of less than thirty years'. So now we know: it "
  'really is about age.'),
 (8,
  None,
  "'Yes, Cecile is a little older.' French builds 'older' by putting 'more' before the description of age. "
  "The extra written letter for Cecile's gender is silent here."),
 (9,
  None,
  "'A little? She's forty-one.' Listen to how age works: in French you don't 'are' an age, you 'have' it. "
  'She has forty-one years.'),
 (10,
  None,
  "'Forty. She's just turned forty.' A present form of 'come', a short word meaning 'from', and another "
  "action together mean 'has just'. The action 'have' belongs to the French way of saying someone's age."),
 (11,
  None,
  "'She'll be forty-one for the film.' French again uses 'have' for age, this time with an ending pointing "
  "to the future. Miranda is thinking about Cecile's age during filming."),
 (12,
  None,
  "'Yes, but she looks thirty.' French uses the action 'do' before an age to say how old someone looks. It "
  'describes her appearance, rather than her actual age.'),
 (13,
  None,
  "'I'm sorry, Mathias, it's decided.' The word for 'sorry' is spelled with the feminine ending, because a "
  "woman says it, but it sounds exactly the same as a man's. The door is closed."),
 (14,
  None,
  "'Try a macaron! It's their speciality.' Mathias changes the subject with a polite invitation. The "
  "possessive before 'speciality' refers to the tea room and has a singular spelling for one speciality."),
 (15,
  None,
  "'Thank you.' Miranda gives a short polite response to his offer. Her decision about the film part still "
  'stands.')]
