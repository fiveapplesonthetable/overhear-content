# Authoring module for dix-pour-cent-s02e02-scene-07.
ID = 'dix-pour-cent-s02e02-scene-07'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 2
SCENE = 7
TITLE = "Dans l'ascenseur avec Hippolyte  (In the Elevator with Hippolyte)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'hippolyte': 'Hippolyte', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E02'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e02.fr.dual.srt'
INTRO = "Inside the ASK elevator, Mathias shares an uncomfortable private conversation with his son Hippolyte. They discuss Catherine's depression and Hippolyte's new relationship, before Camille greets Mathias in the lobby. Let's listen to the scene in French first."
OPENER = "Let's examine how Mathias and Hippolyte share a quiet family moment step by step."
TRANSITION = "Now let's listen to the conversation in the elevator once more."
OUTRO = "Hippolyte leaves to meet his girlfriend, wishing his father good luck for the evening. Back in Gabriel's office, Sofia is furious after an explosive argument with casting director Constance. See you next time!"
CLOSING = ('hippolyte', 'Au revoir... Merde pour ce soir!')
STORY = [
    ('mathias', 'Comment va ta mère?', 'How is your mother?', [(197, 'Comment va ta mère ?')], ''),
    ('hippolyte', 'Le bromazépam est devenu son meilleur ami.', 'Bromazepam has become her best friend.', [(198, 'Le bromazépam est devenu son meilleur ami.')], ''),
    ('hippolyte', "C'est toujours très gênant.", 'It is always very awkward.', [(205, "C'est toujours très gênant.")], ''),
    ('mathias', 'En tout cas tu es là.', 'In any case you are here.', [(206, 'En tout cas tu es là.')], ''),
    ('hippolyte', "J'ai besoin de prendre un peu de recul.", 'I need to get some distance.', [(207, "J'ai besoin de prendre un peu de recul.")], ''),
    ('hippolyte', 'Je passe beaucoup de temps chez ma copine.', "I spend a lot of time at my girlfriend\\'s place.", [(208, 'Je passe beaucoup de temps chez ma copine.')], ''),
    ('mathias', 'Tu as une copine?', 'You have a girlfriend?', [(209, '-Tu as une copine.')], ''),
    ('hippolyte', "Oui, c'est tout récent.", 'Yes, it is very recent.', [(210, "c'est tout récent.")], ''),
    ('hippolyte', 'Bon, je vais y aller.', 'Well, I will get going.', [(213, 'Bon, je vais y aller.')], ''),
    ('mathias', "On s'appelle? Bien sûr.", 'We will call each other? Of course.', [(214, "-On s'appelle ? -Bien sûr.")], ''),
    ('hippolyte', 'Au revoir... Bonne chance pour ce soir!', 'Goodbye... Good luck for tonight!', [(216, '-Au revoir.'), (216, 'Merde pour ce soir !')], ''),
    ('camille', 'Pardon, excusez-moi, Mathias.', 'Pardon, excuse me, Mathias.', [(219, 'Pardon, excusez-moi.')], ''),
    ('camille', 'Je vous passe votre prochain appel.', 'I am putting through your next call.', [(221, 'Je vous le passe.')], ''),
]
WALK = [
    (0, None, "'How is your mother?' Mathias gently asks about Catherine's mental state after their separation."),
    (1, None, "'Bromazepam has become her best friend.' Hippolyte describes his mother's heavy reliance on tranquilizers."),
    (2, None, "'It is always very awkward.' In the elevator, Hippolyte admits things are still awkward with his father."),
    (3, None, "'In any case you are here.' Mathias replies quietly that at least Hippolyte came to the building today."),
    (4, None, "'I need to get some distance.' Hippolyte explains that he still needs some distance from his father."),
    (5, None, "'I spend a lot of time at my girlfriend\\'s place.' Hippolyte explains why he has been avoiding the family apartment."),
    (6, None, "'You have a girlfriend?' Mathias is surprised by this unexpected news about his son's personal life."),
    (7, None, "'Yes, it is very recent.' The adjective recent describes something that happened very recently."),
    (8, None, "'Well, I will get going.' Hippolyte prepares to exit as the elevator arrives at the lobby."),
    (9, None, "'We will call each other? Of course.' Father and son promise to stay in touch by telephone."),
    (10, None, "'Goodbye... Good luck for tonight!' As the elevator doors close, Hippolyte wishes his father good luck for tonight."),
    (11, None, "'Pardon, excuse me, Mathias.' Camille politely interrupts her father in the corridor."),
    (12, None, "'I am putting through your next call.' Back at his desk, Camille puts Mathias's next phone call through. Now let's listen to the conversation in the elevator once more."),
]
