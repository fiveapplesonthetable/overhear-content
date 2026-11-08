# Authoring module for linden-courtyard-de-s01e05-scene-01.
ID = 'linden-courtyard-de-s01e05-scene-01'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Truth in the Courtyard  (Die Wahrheit im Innenhof)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'caleb': 'Caleb', 'hannah': 'Hannah', 'evelyn': 'Evelyn'}
INTRO = 'Noch immer unter dem alten Hofbaum im Gasthof Lindenhof setzt sich Caleb zu Hannah und Evelyn auf die Bank, um das Rätsel vom Montagabend von Anfang an aufzuklären. Hören Sie zuerst die gesamte Szene im Zusammenhang.'
OPENER = 'Schauen wir uns Calebs ehrliche Beichte im Hof nun Satz für Satz genauer an.'
TRANSITION = 'Hören wir uns das ganze Gespräch unterm Baum jetzt noch einmal flüssig an.'
OUTRO = 'Endlich greifen alle Puzzleteile von Montag und Dienstag ineinander! Gleich in der nächsten Szene erzählt Caleb, warum er seit drei Jahren kein Wort mehr mit seinem Bruder Owen gesprochen hat.'
CLOSING = ('hannah', 'See you soon!')
STORY = [('evelyn',
  'Let me look at you properly, Caleb! You grew taller than the piano!',
  'Lass dich mal richtig anschauen, Caleb! Du bist ja größer als das Klavier geworden!'),
 ('caleb',
  'I cannot believe you are staying in the exact same guesthouse, Miss Evelyn.',
  'Ich kann kaum fassen, dass Sie genau im selben Gästehaus wohnen, Frau Evelyn.'),
 ('hannah',
  'Wait, so we rode the same train on Monday, and you took her suitcase?',
  'Warten Sie, wir sind am Montag also mit demselben Zug gefahren, und Sie haben ihren Koffer mitgenommen?'),
 ('caleb',
  "By complete accident! At my cousin's apartment I opened it and saw sheet music and a red ribbon.",
  'Reiner Zufall! In der Wohnung meines Cousins habe ich ihn geöffnet und Notenblätter samt rotem Band gesehen.'),
 ('evelyn',
  'Why did you leave my bag on the step at night and run away?',
  'Warum hast du meine Tasche abends auf die Stufe gestellt und bist weggelaufen?'),
 ('caleb',
  'Because when I walked here on Monday evening, I saw my older brother walking down this street!',
  'Weil ich am Montagabend auf dem Weg hierher meinen älteren Bruder diese Straße entlanggehen sah!'),
 ('hannah', 'Your older brother lives here in Portland?', 'Ihr älterer Bruder wohnt hier in Portland?'),
 ('caleb',
  'Yes. I panicked, rang your bell, and slipped the Friday note onto the handle.',
  'Ja. Ich bekam Panik, läutete an Ihrer Klingel und schob die Freitagsnotiz unter den Griff.'),
 ('evelyn',
  'Wait, and Wednesday night you checked in here under your real name?',
  'Moment, und am Mittwochabend hast du hier unter deinem echten Namen eingecheckt?'),
 ('caleb',
  'I needed a quiet place nearby before Friday, and honestly forgot you still had my bag!',
  'Ich brauchte vor Freitag eine ruhige Bleibe in der Nähe und hatte ehrlich vergessen, dass meine Tasche noch bei Ihnen stand!'),
 ('hannah',
  'Until you called us on Tuesday asking us not to open the white package!',
  'Bis Sie uns am Dienstag angerufen und gebeten haben, das weiße Päckchen nicht zu öffnen!'),
 ('caleb',
  'Everything in that white paper belongs to my brother Owen, not me.',
  'Alles in diesem weißen Papier gehört meinem Bruder Owen, nicht mir.')]
WALK = [(0,
  None,
  ["'Lass dich mal richtig anschauen, Caleb! Du bist ja größer als das Klavier geworden!' Körpergröße vergleicht das Englische "
   'ausschließlich mit',
   (None, 'taller than the piano'),
   'während das Wort für hoch Gegenständen vorbehalten bleibt.']),
 (1,
  None,
  ["'Ich kann kaum fassen, dass Sie genau im selben Gästehaus wohnen, Frau Evelyn.' Freudige Ungläubigkeit eröffnet man natürlich mit",
   (None, 'I cannot believe'),
   'und lässt das folgende Bindewort einfach weg.']),
 (2,
  None,
  ["'Warten Sie, wir sind am Montag also mit demselben Zug gefahren, und Sie haben ihren Koffer mitgenommen?' Für Fahrten mit Bahn oder "
   'Bus steht',
   (None, 'rode the same train'),
   'ohne Verhältniswort direkt vor dem Verkehrsmittel.']),
 (3,
  None,
  ["'Reiner Zufall! In der Wohnung meines Cousins habe ich ihn geöffnet und Notenblätter samt rotem Band gesehen.' Völlige "
   'Unabsichtlichkeit betont die kräftige Fügung',
   (None, 'By complete accident'),
   'mit vorangestellter Präposition.']),
 (4,
  None,
  ["'Warum hast du meine Tasche abends auf die Stufe gestellt und bist weggelaufen?' Nach dem gemeinsamen Hilfsverb der Frage bleiben "
   'sowohl',
   (None, 'leave'),
   'als auch',
   (None, 'run away'),
   'in der unveränderten Grundform.']),
 (5,
  None,
  ["'Weil ich am Montagabend auf dem Weg hierher meinen älteren Bruder diese Straße entlanggehen sah!' Nach Verben der Wahrnehmung "
   'schildert',
   (None, 'walking down this street'),
   'die beobachtete Bewegung mitten im Verlauf.']),
 (6,
  None,
  ["'Ihr älterer Bruder wohnt hier in Portland?' Einen dauerhaften Wohnsitz drückt die einfache Gegenwart",
   (None, 'lives here in Portland'),
   'im Gegensatz zum vorübergehenden Hotelaufenthalt aus.']),
 (7,
  None,
  ["'Ja. Ich bekam Panik, läutete an Ihrer Klingel und schob die Freitagsnotiz unter den Griff.' Die Zielrichtung auf den Griff hinauf "
   'fasst das zusammengesetzte Verhältniswort in',
   (None, 'onto the handle'),
   'präzise zusammen.']),
 (8,
  None,
  ["'Moment, und am Mittwochabend hast du hier unter deinem echten Namen eingecheckt?' Sich im Hotel anmelden heißt",
   (None, 'checked in'),
   'und',
   (None, 'under your real name'),
   'entspricht genau unserem deutschen unter echtem Namen.']),
 (9,
  None,
  ["'Ich brauchte vor Freitag eine ruhige Bleibe in der Nähe und hatte ehrlich vergessen, dass meine Tasche noch bei Ihnen stand!' Direkt "
   'hinter dem Hauptwort ersetzt das einzelne Wort',
   (None, 'nearby'),
   'eine lange Ortsangabe.']),
 (10,
  None,
  ["'Bis Sie uns am Dienstag angerufen und gebeten haben, das weiße Päckchen nicht zu öffnen!' Verneinte Infinitive stellen im Englischen "
   'wie in',
   (None, 'not to open'),
   'das Verneinungswort immer vor das kleine zu-Wort.']),
 (11,
  None,
  ["'Alles in diesem weißen Papier gehört meinem Bruder Owen, nicht mir.' Besitzverhältnisse regelt",
   (None, 'belongs to my brother'),
   'stets über das kurze Richtungswort vor dem Besitzer.'])]
