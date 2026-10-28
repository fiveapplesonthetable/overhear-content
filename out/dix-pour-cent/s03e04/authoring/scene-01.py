# Authoring module for dix-pour-cent-s03e04-scene-01.
ID = 'dix-pour-cent-s03e04-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 3
EPISODE = 4
SCENE = 1
TITLE = 'Le double tournage  (The Double Shoot)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'gabriel': 'Gabriel', 'hicham': 'Hicham'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S03E04'
SOURCE_FILE = 'sources/dix-pour-cent/s03/e04.fr.dual.srt'
INTRO = "At the ASK agency, director Hicham Janowski scrutinizes client paperwork and discovers a serious breach. Agent Gabriel Sarda has secretly double-booked screen legend Isabelle Huppert on two conflicting film productions. Let's listen to the scene in French first."
OPENER = "Let's observe as Hicham confronts Gabriel about Isabelle's secret schedule."
TRANSITION = "Now let's listen to Hicham and Gabriel again at full speed."
OUTRO = "Hicham remains tense about the risky double booking, fearing disastrous legal blowback from the American producers. When you watch the episode, listen out for the expressions meaning 'problem' and 'business agreements'. You'll catch them now. See you next time!"
CLOSING = ('hicham', 'Bonne soirée!')
STORY = [
    ('hicham', 'Il y a un problème dans tes contrats.', 'There is a problem in your contracts.', [(28, 'tes contrats')], ''),
    ('gabriel', "De quel contrat parles-tu aujourd'hui?", 'Which contract are you talking about today?', [(29, 'Isabelle Huppert')], ''),
    ('hicham', 'Isabelle Huppert tourne deux films différents.', 'Isabelle Huppert is shooting two different films.', [(30, "She's a femme fatale"), (32, 'Marie-Médicis')], ''),
    ('gabriel', "C'est juste un léger chevauchement d'horaires.", 'It is just a slight schedule overlap.', [(41, "c'est juste un léger chevauchement.")], ''),
    ('hicham', "Le contrat américain exige l'exclusivité totale.", 'The American contract demands total exclusivity.', [(35, 'il y a écrit exclusive.'), (36, "Ça veut dire contrat d'exclusivité.")], ''),
    ('gabriel', 'Elle tourne de nuit pour les Français.', 'She shoots at night for the French.', [(61, 'et la nuit, pour les Français.')], ''),
    ('hicham', 'Nous sommes complètement hors-la-loi, Gabriel!', 'We are completely outside the law, Gabriel!', [(46, 'on est complètement hors-la-loi.')], ''),
    ('gabriel', 'Isabelle est une véritable légende vivante.', 'Isabelle is a veritable living legend.', [(49, "C'est une espèce de légende vivante")], ''),
    ('hicham', 'Elle ne peut pas tenir ce rythme.', 'She cannot keep up this pace.', [(64, 'Elle doit être complètement épuisée.')], ''),
    ('gabriel', 'Elle a une énergie absolument formidable.', 'She has an absolutely tremendous energy.', [(65, "c'est une force de la nature.")], ''),
    ('hicham', 'Ce double tournage est trop dangereux.', 'This double shoot is too dangerous.', [(38, 'elle a pas le droit de tourner dans un autre film en même temps.')], ''),
    ('gabriel', 'Il ne reste que deux jours difficiles.', 'Only two difficult days remain.', [(62, 'il en reste plus que deux.')], ''),
    ('hicham', 'Si les Américains apprennent cela, attention!', 'If the Americans learn about this, look out!', [(38, 'elle a pas le droit de tourner dans un autre film en même temps.')], ''),
    ('gabriel', 'Fais-moi confiance, tout se passera bien.', 'Trust me, everything will go well.', [(67, "T'inquiète pas.")], ''),
]
WALK = [
    (0, None, "'There is a problem in your contracts.' An administrative warning alerting an agent to legal irregularities."),
    (1, None, "'Which contract are you talking about today?' A defensive inquiry seeking specific clarification."),
    (2, None, "'Isabelle Huppert is shooting two different films.' A direct accusation pointing out an impossible work schedule."),
    (3, None, "'It is just a slight schedule overlap.' A minimizing explanation attempting to soften the conflict."),
    (4, None, "'The American contract demands total exclusivity.' A stern contractual reminder enforcing legal boundaries."),
    (5, None, "'She shoots at night for the French.' A practical explanation revealing the day-and-night filming arrangement."),
    (6, None, "'We are completely outside the law, Gabriel!' An alarmed rebuke protesting unacceptable professional risk."),
    (7, None, "'Isabelle is a veritable living legend.' A reverent defense justifying extraordinary accommodations for a star."),
    (8, None, "'She cannot keep up this pace.' A worried assessment warning against physical and mental exhaustion."),
    (9, None, "'She has an absolutely tremendous energy.' An admiring praise highlighting the actress's rare stamina."),
    (10, None, "'This double shoot is too dangerous.' A grave executive verdict condemning the clandestine schedule."),
    (11, None, "'Only two difficult days remain.' A calming temporal reassurance emphasizing that the ordeal is nearly over."),
    (12, None, "'If the Americans learn about this, look out!' A cautionary warning anticipating severe contractual penalties."),
    (13, None, "'Trust me, everything will go well.' A confident final promise reassuring an anxious supervisor."),
]
