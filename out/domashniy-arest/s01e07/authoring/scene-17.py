"""
Scene 17 of s01e07: "Мы телохранители, а не телоломатели  (Bodyguards, Not Body-Breakers)" (00:31:44,050 -> 00:34:28,540, cues 652-682).

Pasha Osipenko orders his two bodyguards to stage a mugging and injure Samsonov
so he cannot run for mayor, overcoming their Buddhist moral objections about
ruining their karma by threatening to fire them.
"""

ID = "domashniy-arest-s01e07-scene-17"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 17
TITLE = "Мы телохранители, а не телоломатели  (Bodyguards, Not Body-Breakers)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "vitalik": "anja",
}

LABELS = {
    "anya": "Паша",
    "vitalik": "Виталик",
}

INTRO = (
    "Last night, Arkady banged on Marina's wall to ruin Eduard's date while Samsonov phoned lawyer Danya to invite him over for fondue. "
    "The next morning at City Hall, acting mayor Pasha Osipenko calls in his two bodyguards and orders them to stage an attack on his rival Samsonov. "
    "Listen to the Russian conversation first, and don't worry about catching every word."
)

STORY = [
    ("anya", "У меня для вас есть серьёзное задание. Я же могу вам доверять?",
     "I have a serious assignment for you. I can trust you, right?",
     [(652, "У меня для вас есть серьезное задание"), (653, "Я же могу вам доверять")], ""),
    ("anya", "Как вы знаете, Виталий, я участвую в выборах.",
     "As you know, Vitaly, I am taking part in the election.",
     [(654, "Как вы знаете, Виталий, я участвую в выборах")], ""),
    ("anya", "И у меня есть один конкурент. Я говорю о Самсонове, конечно.",
     "And I have one competitor. I am talking about Samsonov, of course.",
     [(655, "И у меня есть один конкурент"), (656, "Я говорю о Самсонове, конечно")], ""),
    ("anya", "А жизнь — сложная штука. Вы понимаете, о чём я?",
     "And life is a complicated thing. Do you understand what I am talking about?",
     [(657, "А жизнь"), (657, "штука"), (659, "Вы понимаете, о чем я")], ""),
    ("anya", "Вот человек выбирается в мэры. Тот же Самсонов, например.",
     "Say a man is running for mayor. That same Samsonov, for example.",
     [(660, "человек выбирается в мэры"), (661, "тот же Самсонов, например")], ""),
    ("anya", "И какие-то хулиганы вдруг напали на него. Не сильно, но человеку плохо.",
     "And some hooligans suddenly attacked him. Not badly, of course, but the man feels unwell.",
     [(662, "И какие-то хулиганы вдруг"), (663, "Не сильно"), (663, "но человеку плохо")], "'проломили голову' (662, 666) softened to 'напали на него'"),
    ("anya", "И выбираться он уже не может. Так, понятно?",
     "And he cannot run for office anymore. So, is that clear?",
     [(664, "И выбираться он уже"), (664, "не может"), (665, "Так, понятно")], ""),
    ("vitalik", "Павел Юрьевич, мы против!",
     "Pavel Yuryevich, we are against this!",
     [(667, "Павел Юрьевич, мы против")], ""),
    ("vitalik", "Мы же телохранители, а не телоломатели.",
     "We are bodyguards, not body-breakers.",
     [(668, "Мы же телохранители, а не телоломатели")], ""),
    ("anya", "А у Аникеева чем вы занимались, интересно?",
     "And what were you doing for Anikeyev, I wonder?",
     [(669, "чем вы занимались, интересно")], "ASR 'Никеева' -> 'Аникеева'"),
    ("vitalik", "Одно дело в караоке руку сломать. А другое — обидеть человека на всю жизнь.",
     "Breaking an arm at karaoke is one thing. And hurting a person for life is another.",
     [(670, "Одно дело в караоке руку"), (670, "сломать"), (671, "на всю жизнь")], "'покалечить' (671) softened to 'обидеть'"),
    ("vitalik", "Поверьте, вам это не надо. Вы так карму портите.",
     "Believe us, you do not need this. You ruin your karma that way.",
     [(672, "вам это не надо"), (673, "карму портите")], ""),
    ("anya", "Послушайте меня внимательно, философы! Я вам отдал приказ!",
     "Listen to me carefully, you philosophers! I gave you an order!",
     [(674, "послушайте меня внимательно"), (676, "Я вам отдал приказ")], "crude 'буддистовы хреновы' (674) -> 'философы'"),
    ("anya", "Если вы не можете работать, уходите! И ищите себе другое место с хорошей зарплатой!",
     "If you cannot do the job, leave! And find yourselves another job with a good salary!",
     [(677, "Если вы не можете работать"), (678, "И ищите себе другое место")], "crude 'пошли к чертовой матери' / 'вас хрен догонишь' / 'Зажрались' (677-680) cleaned"),
    ("vitalik", "Хорошо, мы всё сделаем.",
     "Fine, we will do everything.",
     [(681, "Хорошо, мы все сделаем")], ""),
    ("anya", "Я надеюсь. Идите, действуйте быстрее!",
     "I hope so. Go on, act quickly!",
     [(682, "Я надеюсь"), (682, "действуйте")], "slang 'шевелите булками' (682) -> 'действуйте быстрее'"),
]

OPENER = "Did you hear why the bodyguards hesitated at first? Let's walk through Pasha's order line by line."

WALK = [
    (0, "У меня для вас есть серьёзное задание.", "In the mayor's office, Pasha addresses his two bodyguards: 'I have a serious assignment for you.'"),
    (0, "Я же могу вам доверять?", "'I can trust you, right?' Notice the dative pronoun after the verb for trusting."),
    (1, None, "'As you know, Vitaly, I am taking part in the election,' Pasha continues."),
    (2, "И у меня есть один конкурент.", "'And I have one competitor.' You'll hear 'me' all the time in the show, here connected with 'competitor'."),
    (2, "Я говорю о Самсонове, конечно.", "'I am talking about Samsonov, of course.' The key word here means 'I', which the speaker combines with 'am talking'."),
    (3, "А жизнь — сложная штука.", "'And life is a complicated thing,' Pasha hints darkly."),
    (3, "Вы понимаете, о чём я?", "'Do you understand what I am talking about?' There is no question word here — in Russian, rising intonation on 'I' is enough to make it a question."),
    (4, "Вот человек выбирается в мэры.", "'Say a man is running for mayor,' Pasha explains."),
    (4, "Тот же Самсонов, например.", "'That same Samsonov, for example.' The first content word means 'that', and 'for example' rounds out the thought."),
    (5, "И какие-то хулиганы вдруг напали на него.", "'And some hooligans suddenly attacked him.' A compact expression built around 'some' and 'him'."),
    (5, "Не сильно, но человеку плохо.", "'Not badly, of course, but the man feels unwell.' Listen for the word meaning 'badly' right alongside 'to the man' in this line."),
    (6, "И выбираться он уже не может.", "'And he cannot run for office anymore.' The reflexive ending on the verb for 'to run for office' turns the action back onto the subject."),
    (6, "Так, понятно?", "'So, is that clear?' Pasha asks pointedly."),
    (7, None, "To Pasha's surprise, the bodyguard objects: 'Pavel Yuryevich, we are against this!'"),
    (8, None, "'We are bodyguards, not body-breakers!' Vitalik says, coining a funny opposite word from the roots for body, guard, and break."),
    (9, None, "'And what were you doing for Anikeyev, I wonder?' Pasha asks sarcastically."),
    (10, "Одно дело в караоке руку сломать.", "'Breaking an arm at karaoke is one thing,' Vitalik explains."),
    (10, "А другое — обидеть человека на всю жизнь.", "'And hurting a person for life is another.' Notice the word order: 'another' comes first, and 'life' finishes the sentence."),
    (11, "Поверьте, вам это не надо.", "'Believe us, you do not need this,' the bodyguard adds."),
    (11, "Вы так карму портите.", "'You ruin your karma that way.' The first content word means 'you', and 'ruin' rounds out the thought."),
    (12, "Послушайте меня внимательно, философы!", "Pasha loses his temper: 'Listen to me carefully, you philosophers!'"),
    (12, "Я вам отдал приказ!", "'I gave you an order!' Notice the word order: 'I' comes first, and 'order' finishes the sentence."),
    (13, "Если вы не можете работать, уходите!", "'If you cannot do the job, leave!' he snaps."),
    (13, "И ищите себе другое место с хорошей зарплатой!", "'And find yourselves another job with a good salary!' Notice the word order: 'look for' comes first, and 'salary' finishes the sentence."),
    (14, None, "Faced with losing their perks, the bodyguards fold immediately: 'Fine, we will do everything.'"),
    (15, "Я надеюсь.", "'I hope so,' Pasha replies."),
    (15, "Идите, действуйте быстрее!", "'Go on, act quickly!' he orders them out of his office."),
]

TRANSITION = "Now let's listen to the whole conversation in the mayor's office again."

OUTRO = "So much for the bodyguards' Buddhist principles: as soon as Pasha threatens their generous salary and free food, the two Vitaliks agree to ambush Samsonov."

CLOSING = ("vitalik", "Мы же телохранители, а не телоломатели.")
