# Authoring module for dix-pour-cent-s01e06-scene-17.
ID = 'dix-pour-cent-s01e06-scene-17'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 6
SCENE = 17
TITLE = 'Je ne vous pardonnerai jamais  (I Will Never Forgive You)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'catherine': 'Catherine', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E06'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e06.fr.dual.srt'
INTRO = ('Mathias finds Catherine at a hair salon and asks for a chance to apologize. She refuses forgiveness and rejects his '
 "affectionate words. We then move to Andréa arranging to meet François at Christophe Bel's birthday party and "
 'explaining her changed plans to Colette. Listen first in French.')
OPENER = "Let's go through it slowly. Mathias intercepts Catherine at her workplace."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ('While Mathias is left alone after Catherine rejects his apology, Andréa heads out to meet François at Christophe '
 "Bel's birthday party. See you next time!")
CLOSING = ('andrea', 'Bonne journée!')
STORY = [('catherine',
  "Qu'est-ce que tu veux?",
  'What do you want?',
  [(472, "Qu'est-ce que vous voulez")],
  'Informal family address verified against unprompted original-audio ASR.'),
 ('mathias',
  "Je veux juste te parler. M'excuser.",
  'I just want to talk to you. To apologize.',
  [(473, 'Je veux juste vous parler'), (473, "M'excuser")],
  'Informal family address verified against unprompted original-audio ASR.'),
 ('catherine',
  'Excuse-toi tant que tu veux, je ne te pardonnerai jamais.',
  'Apologize as much as you want, I will never forgive you.',
  [(474, 'Excusez-vous tant que vous voulez, je ne vous pardonnerai jamais')],
  'Informal family address verified against unprompted original-audio ASR.'),
 ('mathias', 'Cinq minutes seulement.', 'Only five minutes.', [(475, 'Cinq minutes seulement')], ''),
 ('mathias',
  "Je m'inquiète pour toi.",
  "I'm worried about you.",
  [(478, "Je m'inquiète pour vous")],
  'Informal family address verified against unprompted original-audio ASR.'),
 ('catherine',
  'Tu as peur pour ton agence?',
  'Are you afraid for your agency?',
  [(479, 'Vous avez peur pour votre agence')],
  'Informal family address verified against unprompted original-audio ASR.'),
 ('mathias', 'Non, chérie.', 'No, darling.', [(481, 'Non, chérie')], ''),
 ('catherine',
  "Ne m'appelle pas chérie! Jamais!",
  "Don't call me darling! Ever!",
  [(482, 'pas'), (482, 'chérie'), (482, 'Jamais')],
  'Informal family address verified against unprompted original-audio ASR.'),
 ('andrea',
  'On se retrouve là-bas. À quelle heure?',
  "We'll meet there. At what time?",
  [(485, 'On se retrouve là-bas. À quelle heure')],
  ''),
 ('andrea',
  "François, il t'a invité personnellement. Et là tu hésites?",
  "François, he invited you personally. And now you're hesitating?",
  [(487, "François, il t'a invité personnellement. Et là tu hésites")],
  ''),
 ('andrea', "Ce n'est pas ce que tu voulais?", "Isn't that what you wanted?", [(488, 'pas ce que tu voulais')], ''),
 ('andrea',
  'Pardon, François, je ne te suis pas.',
  "Sorry, François, I don't follow you.",
  [(493, 'Pardon, François, je ne te suis pas')],
  ''),
 ('andrea',
  'Bon, je serai là à vingt heures trente. On se retrouve dehors.',
  'Well, I will be there at eight thirty in the evening. We will meet outside.',
  [(494, 'Bon, je serai là à'), (494, 'On se retrouve dehors')],
  ''),
 ('andrea',
  "Oui, Colette, c'est moi. Il s'est passé quelque chose au travail.",
  "Yes, Colette, it's me. Something came up at work.",
  [(496, "Colette, c'est moi"), (498, "Il s'est passé quelque chose")],
  '')]
WALK = [(0,
  None,
  "'What do you want?' The opening question frame asks 'what'. It is followed by familiar singular 'you' and 'want'. "
  'Catherine is asking her husband what he has come for.'),
 (1,
  None,
  "'I just want to talk to you. To apologize.' The opening says 'I just want'. The short form before 'apologize' means "
  "'myself', but the complete action simply means apologizing in English."),
 (2,
  None,
  "'Apologize as much as you want, I will never forgive you.' The command says 'apologize'. The following words allow "
  'any amount of that action, before the future negative states that forgiveness will never follow.'),
 (3,
  None,
  "'Just five minutes.' The number gives five minutes. The final word means 'only', minimizing the amount of time "
  'being requested.'),
 (4,
  None,
  "'I'm worried about you.' The shortened word attached to 'worry' goes with worrying oneself. The final word is the "
  "stressed familiar 'you', the person Mathias is worried about."),
 (5,
  None,
  "'Are you afraid for your agency?' French expresses fear with 'have'. The word for 'your' takes its "
  'masculine-looking shape before the vowel in agency, even though agency is feminine.'),
 (6,
  None,
  "'No, darling.' The second word is an affectionate form of address, 'darling'. Its feminine ending matches "
  'Catherine, the woman being addressed.'),
 (7,
  None,
  "'Don't call me darling! Ever!' The opening negative command tells him not to call her that. The last word makes it "
  "absolute: 'never'. She refuses the affectionate label."),
 (8,
  None,
  "'We'll meet there. At what time?' The first action means meeting up. The hyphenated place word means 'over there'. "
  'The following question asks the time of that meeting.'),
 (9,
  None,
  "'François, he invited you personally. And now you're hesitating?' We have moved to Andréa addressing François. The "
  "completed invitation has the object 'you' attached; the final question challenges his present hesitation."),
 (10,
  None,
  "'Isn't that what you wanted?' The negative question asks whether this is what he wanted. The final action looks "
  'back to the wish he had before receiving the invitation.'),
 (11,
  None,
  "'Sorry, François, I don't follow you.' The action literally says 'I do not follow you'. As in English, following "
  'someone can mean understanding their reasoning, rather than walking behind them.'),
 (12,
  'Bon, je serai là à vingt heures trente.',
  "'Right, I'll be there at eight-thirty.' The future action says 'I will be there'. The time is twenty hours thirty: "
  'half past eight in the evening.'),
 (12,
  'On se retrouve dehors.',
  "'We'll meet outside.' The final word means 'outside'. They will meet up there before going into the party "
  'together.'),
 (13,
  None,
  "'Yes, Colette, it's me. Something came up at work.' Now Andréa phones Colette. The final completed action means "
  "'something happened', explaining why she says her work plans have changed.")]
