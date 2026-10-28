# Authoring module for dix-pour-cent-s01e01-scene-05.
ID = 'dix-pour-cent-s01e01-scene-05'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 5
TITLE = "La dernière réunion de Samuel  (Samuel's Last Meeting)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
VOICES = {'narrator': 'sky', 'samuel': 'marcel', 'lea': 'lucie', 'gabriel': 'theo'}
LABELS = {'samuel': 'Samuel', 'lea': 'Andréa', 'gabriel': 'Gabriel'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "We sit next to Andréa. Gabriel still hasn't told anyone that Tarantino doesn't want Cécile. Today it comes out, and Mathias, who doesn't speak in our version, is quick to blame him. We'll hear the scene in French first. Don't worry about catching every word. Let's listen to the scene in French first."
OPENER = "Let's go back through it slowly. Samuel's agents have just been teasing him about his trip to Brazil, and he wants to make one thing clear."
TRANSITION = "Now let's listen to the whole meeting again."
OUTRO = "That's the end of the meeting, and of Gabriel's secret. If you caught the little sandwich around the verb, you'll start hearing it everywhere in the show. See you next time!"
CLOSING = ('samuel', 'Au revoir, tout le monde!')
STORY = [
    ('samuel', 'Je pars en vacances, pas à la retraite.', 'I', [(176, 'Je pars en vacances, pas à la retraite')], ''),
    ('lea', 'Tes premières vacances en huit ans!', 'Your first holiday in eight years!', [(177, 'Premières vacances en huit ans')], ''),
    ('samuel', 'Merci à tous. Bon, dernière réunion avant mon départ.', 'Thank you, everyone. Right, last meeting before I go.', [(183, 'Merci à tous'), (184, 'Bon, dernière réunion avant mon départ')], ''),
    ('samuel', 'Des nouvelles importantes?', 'Any important news?', [(185, 'Des nouvelles importantes ?')], ''),
    ('lea', 'Oui! Mon préféré, Pierre Niney, a un nouveau rôle.', 'Yes! My favourite, Pierre Niney, has a new part.', [(186, 'Mon préféré, Pierre Niney')], ''),
    ('lea', 'Il joue le frère de Guillaume Canet.', 'He plays Guillaume Canet', [(187, 'frère de Guillaume Canet')], ''),
    ('samuel', 'Excellent! Deux de nos acteurs.', 'Excellent! Two of our actors.', [(188, 'Excellent !'), (190, 'Deux de nos acteurs')], ''),
    ('samuel', 'Autre chose? Gabriel?', 'Anything else? Gabriel?', [(193, 'Autre chose ? Gabriel ?')], ''),
    ('lea', 'Cécile de France et Tarantino?', 'Cécile de France and Tarantino?', [(194, 'Cécile de France et Tarantino ?')], ''),
    ('samuel', 'Ça ne se passe pas bien?', 'It', [(195, 'Ça ne se passe pas bien ?')], ''),
    ('gabriel', 'Je ne dirais pas ça.', 'I wouldn', [(196, 'Je ne dirais pas ça')], ''),
    ('gabriel', 'Ça ne se passe pas du tout.', 'It', [(197, 'Ça ne se passe pas du tout')], ''),
    ('lea', "Ce n'est pas possible!", 'That', [(198, 'pas possible')], ''),
    ('gabriel', 'Ils ne veulent pas Cécile.', 'They don', [(202, 'veulent pas')], ''),
    ('gabriel', 'Elle est trop vieille pour le rôle.', 'She', [(203, 'elle est trop vieille pour le rôle')], ''),
    ('lea', "Trop vieille? C'est quoi le rôle, une gamine?", 'Too old? What', [(205, "Trop vieille ? C'est quoi le rôle, une gamine ?")], ''),
    ('samuel', 'Mathias, ça suffit!', 'Mathias, that', [(211, 'Mathias, ça suffit !')], ''),
]
WALK = [
    (0, None, "'I'm going on holiday, not retiring.' Notice that the word for holiday is always plural in French, as if you always take several of them at once. Andréa teases him."),
    (1, None, "'Your first holiday in eight years!' Because the holiday word is plural, the words in front of it are plural too: your, first, all with a plural ending. Samuel thanks everyone and gets down to business."),
    (2, None, "'Right, last meeting before I go.' Literally 'before my departure'. The little opening word is how French speakers say 'right' or 'okay then' when they move on. He asks for news."),
    (3, None, "'Any important news?' News is plural here as well, like in English 'the news'. Andréa has something good."),
    (4, None, "'My favourite, Pierre Niney, has a new part.' In the show the line is that he has been cast in a big new film. And there's more."),
    (5, None, "'He plays Guillaume Canet's brother.' French has no apostrophe s: you say 'the brother of Guillaume Canet'. Canet is an agency client too, so Samuel is pleased."),
    (6, None, "'Excellent! Two of our actors.' Two clients in one film is a good day for an agency. Then Samuel turns to Gabriel."),
    (7, None, "'Anything else? Gabriel?' Literally 'other thing?'. Andréa says out loud what everyone wants to know."),
    (8, None, "'Cécile de France and Tarantino?' Just two names and a rising voice make a question. Gabriel stays quiet, so Samuel guesses."),
    (9, None, "'It's not going well?' Here is our first grammar point. To say 'not', French wraps the verb in two little words, one just before it and one just after it. Listen for that sandwich all through the scene. Gabriel hesitates."),
    (10, None, "'I wouldn't say that.' The same sandwich around the verb, and the verb has the soft 'would' ending. For a second it sounds like good news. Then he finishes."),
    (11, None, "'It's not going at all.' The second half of the sandwich is now 'at all'. It isn't going badly, it simply isn't happening. Andréa can't believe it."),
    (12, None, "'That's not possible!' In the show you hear it without the first little word, as people often say it when they talk fast. Written down, the full sandwich looks like this. Gabriel explains."),
    (13, None, "'They don't want Cécile.' After a year of flights to Los Angeles, riding lessons and English lessons, the answer is no. And the reason hurts."),
    (14, None, "'She's too old for the part.' Second grammar point: the word for old has a special feminine form, because it's about Cécile. For a man you'd hear a different word. Andréa is outraged."),
    (15, None, "'Too old? What's the part, a little girl?' The last word is a casual word for a kid. Then Mathias jumps in: he says it was a three-film deal worth millions, and that Gabriel let it slip away. Samuel stops him."),
    (16, None, "'Mathias, that's enough!' A very handy phrase, literally 'that suffices'. Parents use it, bosses use it, and here it ends the argument."),
]
