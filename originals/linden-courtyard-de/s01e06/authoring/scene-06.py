# Authoring module for linden-courtyard-de-s01e06-scene-06.
ID = 'linden-courtyard-de-s01e06-scene-06'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = 'Permanent Keys  (Schlüssel auf Dauer)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'arthur': 'Arthur', 'tessa': 'Tessa', 'hannah': 'Hannah'}
INTRO = 'In der sonnigen Café-Ecke stellt sich Arthur mit breitem Lächeln und der zweiten Briefseite in der Hand vor Tessa und Hannah auf. Hören wir uns zuerst die gesamte Szene im Zusammenhang an.'
OPENER = 'Schauen wir uns Arthurs doppelte Freudenbotschaft nun Zeile für Zeile an.'
TRANSITION = 'Lassen Sie uns diese Feierstunde im Café jetzt noch einmal am Stück genießen.'
OUTRO = 'Ein offenes Nachbarschaftscafé für Tessa und eine Festanstellung als Empfangsleiterin für Hannah! In der nächsten Szene senkt sich der Abend über den Hof und die Laternen leuchten auf.'
CLOSING = ('arthur', 'See you later!')
STORY = [('arthur',
  'Tessa, how many cinnamon rolls and lemon cakes can your oven bake each morning?',
  'Tessa, wie viele Zimtschnecken und Zitronenkuchen schafft dein Ofen jeden Morgen?'),
 ('tessa',
  'Double what I make now! Are we really opening the courtyard cafe to our street?',
  'Doppelt so viel wie jetzt! Öffnen wir das Hofcafé wirklich für unsere Straße?'),
 ('arthur',
  'Starting tomorrow at eight! Four tables inside, three tables under the tree!',
  'Ab morgen früh um acht! Vier Tische drinnen, drei Tische unterm Baum!'),
 ('tessa',
  "My dream cafe, right here in our own courtyard! Wait until I tell the baker's market!",
  'Mein Traumcafé, direkt hier in unserem eigenen Innenhof! Wartet nur, bis ich das auf dem Bäckermarkt erzähle!'),
 ('arthur',
  'And now, Hannah, today is Friday, the last day of your five day trial week.',
  'Und nun zu dir, Hannah: Heute ist Freitag, der letzte Tag deiner fünftägigen Probewoche.'),
 ('hannah',
  'Oh! With the suitcases, the boiler, and the letter, I completely forgot!',
  'Ach! Bei den Koffern, dem Heizkessel und dem Brief habe ich das völlig vergessen!'),
 ('arthur',
  'On Monday you opened our tricky door; since then you saved rooms, pipes, breakfast, and our lease.',
  'Am Montag hast du unsere tückische Tür geöffnet; seitdem hast du Zimmer, Rohre, das Frühstück und unseren Pachtvertrag gerettet.'),
 ('tessa',
  'If you do not hire her full time, Arthur, I am hiring her in my kitchen!',
  'Wenn du sie nicht Vollzeit einstellst, Arthur, stelle ich sie in meiner Küche ein!'),
 ('arthur',
  'Hands off, Tessa! Hannah, would you stay as our permanent front desk manager?',
  'Finger weg, Tessa! Hannah, möchtest du fest als unsere Empfangsleiterin bei uns bleiben?'),
 ('hannah', 'Stay here with all of you? Yes, a hundred times yes!', 'Hier bei euch allen bleiben? Ja, hundertmal ja!'),
 ('arthur',
  "Wonderful! Your name goes in Graham's big paper book in permanent ink!",
  'Wunderbar! Dein Name kommt mit dokumentenechter Tinte in Grahams großes Papierbuch!'),
 ('hannah', 'Best first week of my life!', 'Die schönste erste Arbeitswoche meines Lebens!')]
WALK = [(0,
  None,
  ["'Tessa, wie viele Zimtschnecken und Zitronenkuchen schafft dein Ofen jeden Morgen?' Da Gebäckstücke einzeln zählbar sind, fragt Arthur "
   'mit',
   (None, 'how many'),
   'nach der genauen Stückzahl.']),
 (1,
  None,
  ["'Doppelt so viel wie jetzt! Öffnen wir das Hofcafé wirklich für unsere Straße?' Eine Verdopplung der bisherigen Menge packt Tessa "
   'schwungvoll in',
   (None, 'Double what I make now'),
   'am Satzbeginn.']),
 (2,
  None,
  ["'Ab morgen früh um acht! Vier Tische drinnen, drei Tische unterm Baum!' Den Beginn einer neuen Regelung kündigt",
   (None, 'Starting tomorrow'),
   'knapp und schwungvoll an.']),
 (3,
  None,
  ["'Mein Traumcafé, direkt hier in unserem eigenen Innenhof! Wartet nur, bis ich das auf dem Bäckermarkt erzähle!' Einen lang gehegten "
   'Wunsch benennt die Verbindung',
   (None, 'My dream cafe'),
   'mit vorangestelltem Hauptwort.']),
 (4,
  None,
  ["'Und nun zu dir, Hannah: Heute ist Freitag, der letzte Tag deiner fünftägigen Probewoche.' Als vorangestellte Bestimmung bleibt der "
   'Zeitraum in',
   (None, 'five day trial week'),
   'wieder ohne Mehrzahlzeichen.']),
 (5,
  None,
  ["'Ach! Bei den Koffern, dem Heizkessel und dem Brief habe ich das völlig vergessen!' Vor dem unregelmäßigen Vergangenheitsverb "
   'verstärkt das Umstandswort in',
   (None, 'I completely forgot'),
   'das Vergessen.']),
 (6,
  None,
  ["'Am Montag hast du unsere tückische Tür geöffnet; seitdem hast du Zimmer, Rohre, das Frühstück und unseren Pachtvertrag gerettet.' Von "
   'jenem Zeitpunkt bis heute schlägt',
   (None, 'since then'),
   'die zeitliche Brücke.']),
 (7,
  None,
  ["'Wenn du sie nicht Vollzeit einstellst, Arthur, stelle ich sie in meiner Küche ein!' Jemanden auf einer vollen Stelle beschäftigen "
   'heißt im Berufsleben',
   (None, 'hire her full time'),
   'ganz ohne Verhältniswort am Ende.']),
 (8,
  None,
  ["'Finger weg, Tessa! Hannah, möchtest du fest als unsere Empfangsleiterin bei uns bleiben?' Scherzhaft wehrt",
   (None, 'Hands off'),
   'Tessas Abwerbeversuch ab, bevor',
   (None, 'would you stay'),
   'höflich das Stellenangebot stellt.']),
 (9,
  None,
  ["'Hier bei euch allen bleiben? Ja, hundertmal ja!' Überschäumende Zustimmung ruft das begeisterte",
   (None, 'a hundred times yes'),
   'mit unbestimmtem Artikel vor hundert aus.']),
 (10,
  None,
  ["'Wunderbar! Dein Name kommt mit dokumentenechter Tinte in Grahams großes Papierbuch!' Geschriebenes in Tinte oder Bleistift steht auf "
   'Englisch immer mit dem Verhältniswort in',
   (None, 'in permanent ink'),
   'für unauslöschliche Schrift.']),
 (11,
  None,
  ["'Die schönste erste Arbeitswoche meines Lebens!' Jubelnde Höchststufen im Alltag lassen am Anfang von",
   (None, 'Best first week of my life'),
   'gern den bestimmten Artikel weg.'])]
