# Authoring module for linden-courtyard-de-s01e01-scene-01.
ID = 'linden-courtyard-de-s01e01-scene-01'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Lift the Handle  (Die Klinke anheben)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'An ihrem allerersten Morgen erreicht Hannah frühzeitig den gemütlichen Gasthof Lindenhof in Portland. Hinter dem Empfangstresen schenkt sich der erfahrene Hausmeister Graham bereits in aller Ruhe einen kräftigen Tee ein. Hören Sie sich zuerst die ganze Szene im Zusammenhang an, ohne sich um jedes einzelne Wort Gedanken zu machen.'
OPENER = 'Gehen wir das Gespräch nun in Ruhe Satz für Satz durch.'
TRANSITION = 'Hören wir uns die gesamte Szene jetzt noch einmal im natürlichen Sprechtempo an.'
OUTRO = 'Hannah hat die Tür gemeistert, die acht Messingschlüssel hängen bereit am Brett, und ihr erster Arbeitstag beginnt. Machen Sie sich keine Sorgen, falls manches noch schnell klang — diese Wörter begegnen Ihnen in den kommenden Folgen immer wieder. Bis gleich in der nächsten Szene!'
CLOSING = ('hannah', 'See you soon!')
STORY = [('hannah', 'Good morning! Excuse me, is the door locked?', 'Guten Morgen! Entschuldigung, ist die Tür abgeschlossen?'),
 ('graham',
  'Good morning. No, lift the handle first, then push.',
  'Guten Morgen. Nein, heben Sie zuerst die Klinke an und drücken Sie dann.'),
 ('hannah',
  'Oh, it opens! Thank you. I am Hannah, the new receptionist.',
  'Ach, sie geht auf! Vielen Dank. Ich bin Hannah, die neue Rezeptionistin.'),
 ('graham', 'I am Graham. You are ten minutes early.', 'Ich bin Graham. Du bist zehn Minuten zu früh.'),
 ('hannah',
  'I always walk fast on my first day. Where is the computer?',
  'An meinem ersten Tag gehe ich immer schnell. Wo ist der Computer?'),
 ('graham',
  'In the drawer. Here we use this big paper book and a pencil.',
  'In der Schublade. Hier benutzen wir dieses große Papierbuch und einen Bleistift.'),
 ('hannah', 'A paper book? Really?', 'Ein Papierbuch? Im Ernst?'),
 ('graham', 'Paper never loses the room list when it rains.', 'Papier verliert nie die Zimmerliste, wenn es regnet.'),
 ('hannah', 'Fair enough! And these are the keys?', 'Das leuchtet ein! Und das hier sind die Schlüssel?'),
 ('graham',
  'Yes, eight rooms, eight brass keys. Room four is arriving today.',
  'Ja, acht Zimmer, acht Messingschlüssel. Zimmer vier reist heute an.'),
 ('hannah', 'Great. Tell me everything I need to know.', 'Klasse. Sag mir alles, was ich wissen muss.'),
 ('graham',
  'Rule one: drink hot tea first, then answer the bell.',
  'Regel Nummer eins: Trink zuerst heißen Tee und geh dann an die Klingel.')]
WALK = [(0,
  None,
  ["'Guten Morgen! Entschuldigung, ist die Tür abgeschlossen?' Der englische Morgengruß",
   (None, 'Good morning'),
   'kommt ganz ohne Artikel aus, und für die Entscheidungsfrage rückt',
   (None, 'is'),
   'direkt vor das Subjekt.']),
 (1,
  None,
  ["'Guten Morgen. Nein, heben Sie zuerst die Klinke an und drücken Sie dann.' Für freundliche Anleitungen genügt im Englischen die bloße "
   'Grundform des Verbs, hier',
   (None, 'lift'),
   'zum Anheben und',
   (None, 'push'),
   'zum Aufdrücken, ganz ohne Fürwort.']),
 (2,
  None,
  ["'Ach, sie geht auf! Vielen Dank. Ich bin Hannah, die neue Rezeptionistin.' Beachten Sie die Verbindung",
   (None, 'it opens'),
   'denn Gegenstände wie eine Tür sind im Englischen sprachlich immer sächlich, niemals weiblich wie im Deutschen.']),
 (3,
  None,
  ["'Ich bin Graham. Du bist zehn Minuten zu früh.' Während das Deutsche hier ein zusätzliches Wort für zu ergänzt, drückt",
   (None, 'You are ten minutes early'),
   'ganz schlicht aus, dass jemand vor der vereinbarten Zeit da ist.']),
 (4,
  None,
  ["'An meinem ersten Tag gehe ich immer schnell. Wo ist der Computer?' Häufigkeitswörter stehen vor dem Vollverb, und für bestimmte "
   'Kalendertage nutzt das Englische die Wendung',
   (None, 'on my first day'),
   'am Satzende.']),
 (5,
  None,
  ["'In der Schublade. Hier benutzen wir dieses große Papierbuch und einen Bleistift.' In der Wortgruppe",
   (None, 'big paper book'),
   'stehen Größe und Material direkt vor dem Hauptwort, wo wir im Deutschen ein zusammengesetztes Wort bilden.']),
 (6,
  None,
  ["'Ein Papierbuch? Im Ernst?' Mit fragend ansteigender Stimme dient das einzelne Wort",
   (None, 'Really'),
   'im Gespräch als natürliche Überraschungsfrage.']),
 (7,
  None,
  ["'Papier verliert nie die Zimmerliste, wenn es regnet.' Im zeitlichen Nebensatz",
   (None, 'when it rains'),
   'bleibt die Wortstellung anders als im Deutschen unverändert: erst das Subjekt, gleich dahinter das Verb.']),
 (8,
  None,
  ["'Das leuchtet ein! Und das hier sind die Schlüssel?' Wenn das Gegenüber ein gutes Argument vorbringt, signalisiert der idiomatische "
   'Ausruf',
   (None, 'Fair enough'),
   'sofort freundliche Zustimmung.']),
 (9,
  None,
  ["'Ja, acht Zimmer, acht Messingschlüssel. Zimmer vier reist heute an.' Die Verlaufsform der Gegenwart in",
   (None, 'is arriving today'),
   'kennzeichnet im Englischen ein Ereignis, das für heute bereits fest eingeplant ist.']),
 (10,
  None,
  ["'Klasse. Sag mir alles, was ich wissen muss.' Direkt hinter",
   (None, 'everything'),
   'fällt das Bindewort im Englischen gern weg, sodass sich',
   (None, 'I need to know'),
   'flüssig und ohne Pause anschließt.']),
 (11,
  None,
  ["'Regel Nummer eins: Trink zuerst heißen Tee und geh dann an die Klingel.' Im Englischen nimmt man nicht nur Telefonate oder Fragen "
   'entgegen, sondern sagt auch',
   (None, 'answer the bell'),
   'für den Gang zur Empfangsklingel.'])]
