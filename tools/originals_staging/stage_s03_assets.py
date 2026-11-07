#!/usr/bin/env python3
"""Pre-stage Season 3 scenes.json, Season-03-Master-Script.md, and 480 bespoke 1024x1024 flat-vector WebP illustrations in scratch/s03_staged."""
import concurrent.futures
import hashlib
import json
import math
import pathlib
import re as _re
import sys

SCRATCH = pathlib.Path("/usr/local/google/home/zezeozue/.gemini/jetski/brain/7c92d1f4-f827-44cd-97ef-f1f29eab2bd7/scratch")
sys.path.insert(0, str(SCRATCH))
import scaffold_originals as s1  # noqa: E402

ENG_DIR = SCRATCH / "author_repo" / "originals" / "_english"
STAGE_DIR = SCRATCH / "s03_staged"

S3_META = {
    "dvorik-u-mosta": {
        "season_title": {"ru": "Сезон 3: Капсула времени", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "Жестяная коробка под деревом",
            "Четыре подсказки в Липовом переулке",
            "Вторая половина рецепта",
            "Фонарики на балконе",
            "Ранний поезд",
            "Тридцать лет спустя",
        ],
    },
    "hotel-du-tilleul": {
        "season_title": {"fr": "Saison 3 : La capsule temporelle", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "La boîte en fer sous l'arbre",
            "Quatre indices rue des Tilleuls",
            "La moitié manquante de la recette",
            "Les lanternes du balcon",
            "Le train en avance",
            "Trente étés plus tard",
        ],
    },
    "posada-del-limonero": {
        "season_title": {"es": "Temporada 3: La cápsula del tiempo", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "La caja de lata bajo el árbol",
            "Cuatro pistas en la calle de los Tilos",
            "La mitad que falta de la receta",
            "Los farolillos del balcón",
            "El tren adelantado",
            "Treinta veranos después",
        ],
    },
    "locanda-del-tiglio": {
        "season_title": {"it": "Stagione 3: La capsula del tempo", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "La scatola di latta sotto l'albero",
            "Quattro indizi in via dei Tigli",
            "La metà mancante della ricetta",
            "Le lanterne del balcone",
            "Il treno in anticipo",
            "Trenta estati dopo",
        ],
    },
    "pousada-do-cajueiro": {
        "season_title": {"pt": "Temporada 3: A cápsula do tempo", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "A lata sob a árvore",
            "Quatro pistas na Rua das Acácias",
            "A metade que faltava da receita",
            "As lanternas da varanda",
            "A chegada adiantada",
            "Trinta verões depois",
        ],
    },
    "pension-sonnenhof": {
        "season_title": {"de": "Staffel 3: Die Zeitkapsel", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "Die Blechdose unter dem Baum",
            "Vier Hinweise in der Lindengasse",
            "Die fehlende Hälfte des Rezepts",
            "Die Laternen am Balkon",
            "Der frühe Zug",
            "Dreißig Sommer später",
        ],
    },
    "bayt-al-yasmin": {
        "season_title": {"ar": "الموسم الثالث: كبسولة الزمن", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "العلبة المعدنية تحت الشجرة",
            "أربعة أدلة في شارع الياسمين",
            "النصف المفقود من الوصفة",
            "فوانيس الشرفة العلوية",
            "الموعد المبكر",
            "بعد ثلاثين صيفاً",
        ],
    },
    "hidamari-ryokan": {
        "season_title": {"ja": "シーズン3：タイムカプセル", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "木の下のブリキ缶",
            "けやき通りの四つの手がかり",
            "レシピの残り半分",
            "バルコニーのちょうちん",
            "三時間早い電車",
            "三十回目の夏に",
        ],
    },
    "haessal-guesthouse": {
        "season_title": {"ko": "시즌 3: 타임캡슐", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "나무 아래 양철 상자",
            "은행길의 네 가지 단서",
            "사라진 레시피 반쪽",
            "발코니의 등불",
            "세 시간 일찍 온 기차",
            "서른 번의 여름이 지나고",
        ],
    },
    "xiaoyuan-kezhan": {
        "season_title": {"zh": "第三季：时间胶囊", "en": "Season 3: The Time Capsule"},
        "ep_titles": [
            "树下的铁盒",
            "梧桐巷的四张线索卡",
            "菜谱的另一半",
            "二楼走廊的灯笼",
            "提前三小时的火车",
            "三十个夏天之后",
        ],
    },
}

S3_THEMES = [
    # E1: The Tin Box Under the Tree
    [("#4E6E8E", "flagstone_tree"), ("#5F8D78", "waxed_parcel"), ("#C86D58", "tin_capsule"), ("#468284", "compass"),
     ("#7B68A6", "walking_map"), ("#D48C4E", "herb_book"), ("#8C6D58", "sketch_sheet"), ("#527196", "wax_envelope")],
    # E2: Four Clues on {STREET}
    [("#5AA388", "compass"), ("#4C8DAE", "fountain"), ("#D8824C", "warm_rolls"), ("#6874A8", "clock_tower"),
     ("#866552", "bookshop_arch"), ("#529471", "walking_map"), ("#6A8CAF", "wax_envelope"), ("#7A5E96", "pocket_watch")],
    # E3: The Missing Half of the Recipe
    [("#587B9C", "herb_book"), ("#4A9B8E", "herb_book"), ("#D98A4E", "baking_tins"), ("#E4B644", "baking_tins"),
     ("#C46D52", "baking_tins"), ("#679E7A", "herb_book"), ("#D66874", "berry_cake"), ("#486B8A", "balcony_lanterns")],
    # E4: The Rooftop Lanterns
    [("#5E88A8", "balcony_lanterns"), ("#D48B54", "balcony_lanterns"), ("#7264A4", "seating_scroll"), ("#4A7E96", "fountain"),
     ("#568EA6", "fountain"), ("#64987C", "balcony_lanterns"), ("#8A6B56", "clothespins"), ("#C87A62", "clothespins")],
    # E5: The Early Train
    [("#4E6C92", "pocket_watch"), ("#D87E52", "baking_tins"), ("#6C5E98", "pocket_watch"), ("#589688", "hatbox_pack"),
     ("#5A7EA4", "piano_duet"), ("#68A276", "berry_cake"), ("#4B829E", "compass"), ("#C9864C", "balcony_lanterns")],
    # E6: Thirty Summers Later
    [("#58789E", "compass"), ("#D96E78", "berry_cake"), ("#7E68AC", "piano_duet"), ("#5A9A82", "framed_map"),
     ("#467A9C", "blue_capsule"), ("#C88852", "clothespins"), ("#4E6A8A", "flagstone_tree"), ("#6E5C94", "framed_map")],
]

BG_PROPS = {"flagstone_tree", "fountain", "clock_tower", "bookshop_arch", "balcony_lanterns", "framed_map"}


def _star_pts(cx, cy, r_out, r_in, n=4):
    pts = []
    for i in range(n * 2):
        ang = math.radians(-90 + i * (180.0 / n))
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))
    return pts


def draw_s3_prop(c: s1.Canvas, prop: str):
    """Bespoke Season 3 flat-vector props with zero text/digits."""
    if prop == "flagstone_tree":
        # Leafy shade tree canopy top-left + stone courtyard pavers below
        c.rect(458, 90, 56, 215, "#6D4C3D", rx=14)
        for lx, ly, lr, col in [(420, 118, 72, "#4F8A64"), (512, 98, 84, "#5EA074"), (596, 126, 68, "#467D59")]:
            c.circle(lx, ly, lr, col)
        for sx in (360, 462, 564):
            c.rect(sx, 772, 90, 34, "#B8B2A8", rx=8)
        c.rect(462, 748, 90, 32, "#D5CFC4", rx=8, stroke=s1.INK, sw=3)
    elif prop == "waxed_parcel":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.rect(420, 562, 184, 116, "#E6C770", rx=14)
        c.stroke_pts([(420, 620), (604, 620)], "#8C583A", 8)
        c.stroke_pts([(512, 562), (512, 678)], "#8C583A", 8)
        c.circle(512, 620, 14, "#B86B43")
    elif prop == "tin_capsule":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        # Folded cream waxed cloth underneath + crimson & gold biscuit tin
        c.poly_fill([(382, 676), (642, 676), (616, 642), (408, 642)], "#F3E3B2")
        c.rect(424, 560, 176, 112, "#C84B44", rx=12)
        c.rect(418, 548, 188, 26, "#F2C14E", rx=8)
        c.rect(454, 594, 116, 48, s1.CREAM, rx=6)
        c.circle(512, 618, 12, "#F2C14E")
    elif prop == "blue_capsule":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.poly_fill([(382, 676), (642, 676), (616, 642), (408, 642)], "#F5DF9E")
        c.rect(424, 560, 176, 112, "#2F6690", rx=12)
        c.rect(418, 548, 188, 26, "#F2C14E", rx=8)
        c.rect(460, 596, 104, 44, s1.CREAM, rx=6)
        c.poly_fill(_star_pts(512, 618, 14, 6, 4), "#E2604F")
    elif prop == "compass":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.circle(512, 536, 18, fill=None, stroke="#D9A438", sw=8)
        c.circle(512, 616, 68, "#E5B342")
        c.circle(512, 616, 52, s1.CREAM)
        c.poly_fill([(512, 570), (525, 616), (499, 616)], "#E25B4B")
        c.poly_fill([(512, 662), (525, 616), (499, 616)], "#3D5A80")
        c.circle(512, 616, 8, "#D9A438")
    elif prop == "walking_map":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        # Four square puzzle cards laid 2x2
        coords = [(426, 550), (516, 550), (426, 616), (516, 616)]
        for cx, cy in coords:
            c.rect(cx, cy, 82, 58, s1.CREAM, rx=6)
        c.stroke_pts([(446, 646), (488, 582), (556, 578), (576, 640)], "#3B9B96", 6)
        c.poly_fill(_star_pts(556, 578, 13, 5, 5), "#E25B4B")
    elif prop == "herb_book":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.rect(410, 566, 204, 108, "#3E7A56", rx=10)
        c.rect(422, 576, 86, 88, s1.CREAM, rx=4)
        c.rect(516, 576, 86, 88, s1.CREAM, rx=4)
        # Pressed mint sprig on left + torn recipe card on right
        c.stroke_pts([(464, 650), (464, 594)], "#4E9A68", 5)
        c.ellipse(450, 618, 12, 7, "#5CB278")
        c.ellipse(478, 608, 12, 7, "#5CB278")
        c.rect(532, 592, 56, 52, "#F9E5B4", rx=4)
    elif prop == "sketch_sheet":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.rect(418, 556, 188, 118, s1.CREAM, rx=8)
        for sx in (450, 480, 512, 544, 574):
            c.circle(sx, 602, 11, "#6E6764")
            c.rect(sx - 10, 616, 20, 32, "#8C8580", rx=6)
    elif prop == "wax_envelope":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.rect(430, 562, 164, 108, s1.CREAM, rx=10)
        c.poly_fill([(430, 562), (512, 622), (594, 562)], s1.darken(s1.CREAM, 0.09))
        c.circle(512, 620, 22, "#D6493E")
        c.poly_fill(_star_pts(512, 620, 12, 5, 4), "#F6D58E")
    elif prop == "fountain":
        c.ellipse(512, 255, 148, 42, "#D8D2C8")
        c.ellipse(512, 252, 124, 30, "#7CC6EE")
        c.rect(488, 152, 48, 98, "#C9C2B6", rx=12)
        c.qbez((512, 154), (458, 112), (434, 242), "#A6DEFF", sw=8)
        c.qbez((512, 154), (566, 112), (590, 242), "#A6DEFF", sw=8)
    elif prop == "clock_tower":
        c.rect(432, 74, 160, 236, "#D6C7B2", rx=18)
        c.poly_fill([(418, 82), (512, 28), (606, 82)], "#8C5843")
        c.circle(512, 168, 54, s1.CREAM, stroke="#6E4C3A", sw=8)
        c.stroke_pts([(512, 168), (512, 128)], s1.INK, 7)
        c.stroke_pts([(512, 168), (512, 140)], "#C9963B", 5)
    elif prop == "bookshop_arch":
        c.rect(376, 84, 272, 236, "#C9B8A4", rx=44)
        c.rect(408, 122, 208, 198, "#4A3C36", rx=32)
        c.rect(424, 188, 76, 98, "#4E8C64", rx=6)
        for bx, col in [(434, "#F2C14E"), (454, "#E2604F"), (474, "#78B9E8")]:
            c.rect(bx, 198, 14, 38, col, rx=2)
    elif prop == "pocket_watch":
        c.rect(105, 670, 814, 190, "#7A543E", rx=24)
        c.qbez((472, 622), (420, 658), (382, 636), "#E5B342", sw=6)
        c.circle(492, 616, 48, "#E5B342")
        c.circle(492, 616, 36, s1.CREAM)
        c.stroke_pts([(492, 616), (492, 590)], s1.INK, 6)
        c.stroke_pts([(492, 616), (514, 616)], s1.INK, 6)
        # Two room keys beside watch
        for ky, tag_col in [(602, "#3B9B96"), (642, "#E2604F")]:
            c.rect(564, ky - 10, 42, 22, tag_col, rx=6)
            c.rect(604, ky - 4, 48, 8, "#E5B342", rx=3)
    elif prop == "baking_tins":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        for tx, top_col in [(396, "#F4D35E"), (512, "#C97A40"), (628, "#E8A85A")]:
            c.rect(tx - 46, 618, 92, 52, "#9AA5B1", rx=10)
            c.ellipse(tx, 616, 44, 16, top_col)
    elif prop == "berry_cake":
        c.rect(115, 675, 794, 185, "#694B3C", rx=24)
        c.rect(488, 652, 48, 28, s1.CREAM, rx=6)
        c.ellipse(512, 652, 118, 22, s1.CREAM)
        c.rect(428, 582, 168, 66, "#E6A856", rx=16)
        c.rect(428, 578, 168, 22, "#F6C85F", rx=10)
        for bx in (456, 492, 528, 564):
            c.circle(bx, 572, 13, "#C83E5B")
            c.ellipse(bx + 12, 584, 9, 5, s1.CREAM)
    elif prop == "balcony_lanterns":
        c.rect(76, 86, 872, 18, "#6E4834", rx=6)
        for px in range(120, 920, 96):
            c.rect(px, 86, 14, 78, "#6E4834", rx=4)
        c.rect(76, 156, 872, 14, "#5A3A29", rx=5)
        c.stroke_pts([(150, 162), (512, 224), (874, 162)], s1.INK, 6)
        for lx, ly, col in [(250, 186, "#F6BD60"), (380, 206, "#F2846E"), (512, 218, "#F6BD60"),
                            (644, 206, "#F2846E"), (774, 186, "#F6BD60")]:
            c.circle(lx, ly + 26, 40, "#FFE89E", opacity=0.34)
            c.ellipse(lx, ly + 26, 24, 30, col)
    elif prop == "seating_scroll":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        c.rect(388, 554, 248, 122, "#FFFFFF", rx=10)
        for ry in (580, 608, 636):
            for rx in (416, 488, 560):
                c.rect(rx, ry, 44, 12, "#4A86C8", rx=4)
    elif prop == "clothespins":
        c.rect(105, 670, 814, 190, "#7A543E", rx=24)
        for px in (404, 476, 548, 620):
            c.rect(px - 26, 616, 52, 48, s1.CREAM, rx=6)
            c.rect(px - 8, 568, 16, 62, "#DEB887", rx=5)
            c.circle(px, 598, 5, "#8C6D58")
    elif prop == "hatbox_pack":
        c.rect(115, 675, 794, 185, "#6E4C3A", rx=24)
        # Green hiking backpack + round coral-striped hatbox
        c.rect(402, 562, 96, 114, "#3E8468", rx=20)
        c.rect(420, 594, 60, 48, "#2F6650", rx=10)
        c.ellipse(572, 624, 56, 48, "#F2D5C4")
        c.rect(516, 588, 112, 20, "#E06D53", rx=8)
        c.qbez((542, 588), (572, 548), (602, 588), "#8C583A", sw=8)
    elif prop == "piano_duet":
        c.rect(344, 542, 336, 252, "#5C3A28", rx=16)
        c.rect(366, 624, 292, 40, s1.CREAM, rx=6)
        for kx in range(382, 646, 26):
            c.rect(kx, 624, 11, 22, s1.INK, rx=2)
        c.rect(430, 558, 76, 54, s1.CREAM, rx=5)
        c.rect(518, 558, 76, 54, "#FCE8B2", rx=5)
    elif prop == "framed_map":
        c.rect(368, 86, 288, 214, "#6E4730", rx=16)
        c.rect(388, 106, 248, 174, s1.CREAM, rx=8)
        c.stroke_pts([(406, 236), (472, 178), (554, 184), (618, 138)], "#4EA898", 9)
        c.rect(484, 154, 56, 48, "#F2C14E", rx=8)
        c.poly_fill(_star_pts(512, 178, 14, 6, 4), "#E25B4B")
    else:
        s1.draw_prop(c, prop)


def render_s3_scene(args):
    show, ep_idx, sc_obj = args
    sc_idx = sc_obj["scene"] - 1
    base_dom, prop = S3_THEMES[ep_idx][sc_idx]
    tint_col, tint_amt = show["tint"]
    dom = s1.mix(base_dom, tint_col, tint_amt + 0.025 * ((ep_idx * 2 + sc_idx) % 4))
    c = s1.Canvas(dom)
    spot_x = 476 + ((ep_idx * 13 + sc_idx * 19) % 68)
    spot_y = 432 + ((ep_idx + sc_idx) % 3) * 4
    s1.draw_stage(c, dom, spot=(spot_x, spot_y, 402))
    if prop in BG_PROPS:
        draw_s3_prop(c, prop)

    roles = sc_obj["characters"]
    xs = [304, 720] if len(roles) == 2 else [208, 512, 816]
    rs = [95, 95] if len(roles) == 2 else [86, 92, 86]
    faces = ["smile", "happy", "o", "worried"]
    for idx, role in enumerate(roles):
        spec = show["cast"][role]
        face = faces[(ep_idx * 3 + sc_idx * 2 + idx) % len(faces)]
        if prop in ("berry_cake", "piano_duet", "framed_map", "balcony_lanterns", "warm_rolls") and face == "worried":
            face = "happy"
        forehead = (role == "M2" and (ep_idx + sc_idx) % 2 == 0 and not (ep_idx >= 4 and sc_idx == 7))
        arm_l = "up" if (idx == 0 and ((ep_idx + sc_idx) % 2 == 0)) else "down"
        arm_r = "mid" if (idx == len(roles) - 1 and ((ep_idx + sc_idx) % 2 == 1)) else "in"
        look = (1 if idx == 0 else (-1 if idx == len(roles) - 1 else 0), 0)
        s1.draw_person(
            c, xs[idx], 402 + ((idx + ep_idx) % 2) * 14, rs[idx], spec,
            face=face, look=look, arm_l=arm_l, arm_r=arm_r, forehead_glasses=forehead,
        )

    if prop not in BG_PROPS:
        draw_s3_prop(c, prop)

    out_path = STAGE_DIR / show["slug"] / f"s03e{ep_idx + 1:02d}" / f"scene-{sc_obj['scene']:02d}.webp"
    c.save_webp(out_path)


def write_s3_master_markdown(episodes: list):
    lines = ["# Courtyard Inn — Season 3 Master English Script", ""]
    for ep in episodes:
        lines.append(f"## Episode {ep['episode']}: {ep['title']}")
        lines.append("")
        for sc in ep["scenes"]:
            chars = ", ".join(sc["characters"])
            lines.append(f"### Scene {sc['scene']}: {sc['title']} ({sc['location']}) — {chars}")
            lines.append(f"- **Summary:** {sc['summary']}")
            lines.append(f"- **Intro:** {sc['intro']}")
            for spk, txt in sc["story"]:
                lines.append(f"  - **{spk}:** {txt}")
            lines.append(f"- **Outro:** {sc['outro']}")
            lines.append("")
    (ENG_DIR / "Season-03-Master-Script.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    episodes = [json.loads((ENG_DIR / f"s03e{i:02d}.json").read_text("utf-8")) for i in range(1, 7)]
    write_s3_master_markdown(episodes)

    jobs = []
    for show in s1.SHOWS:
        slug = show["slug"]
        meta = S3_META[slug]

        def sub_vars(text: str) -> str:
            res = text.replace("{SHOW}", show["title"]["en"]).replace("{CITY}", show["city"]).replace("{STREET}", show["street"])
            for slot in ("F1", "M1", "F2", "M2", "F3", "M3", "M4"):
                name = show["cast"][slot][2][0]
                res = res.replace("{" + slot + "}", name)
                res = _re.sub(r"\b" + slot + r"\b", name, res)
            return res

        for ep_idx, ep in enumerate(episodes):
            ep_dir = STAGE_DIR / slug / f"s03e{ep_idx + 1:02d}"
            ep_dir.mkdir(parents=True, exist_ok=True)
            scenes_list = []
            for sc in ep["scenes"]:
                scenes_list.append({
                    "scene": sc["scene"],
                    "title": sub_vars(sc["title"]),
                    "summary": sub_vars(sc["summary"]),
                    "characters": [show["cast"][r][0] for r in sc["characters"]],
                    "location": sc["location"],
                })
                jobs.append((show, ep_idx, sc))
            scenes_json = {
                "schemaVersion": 1,
                "show": slug,
                "season": 3,
                "episode": ep_idx + 1,
                "title": meta["ep_titles"][ep_idx],
                "scenes": scenes_list,
            }
            (ep_dir / "scenes.json").write_text(json.dumps(scenes_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        (STAGE_DIR / slug / "season3_meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as ex:
        list(ex.map(render_s3_scene, jobs))

    # Verify MD5 uniqueness across S1 + S2 + S3!
    s1_webps = sorted((SCRATCH / "author_repo" / "originals").glob("*/s01e*/scene-*.webp"))
    s2_webps = sorted((SCRATCH / "s02_staged").glob("*/s02e*/scene-*.webp"))
    s3_webps = sorted(STAGE_DIR.glob("*/s03e*/scene-*.webp"))
    all_files = s1_webps + s2_webps + s3_webps
    seen = {}
    collisions = []
    for p in all_files:
        h = hashlib.md5(p.read_bytes()).hexdigest()
        if h in seen:
            collisions.append((str(seen[h]), str(p)))
        else:
            seen[h] = p
    print(f"Pre-staged 60 Season 3 scenes.json files, 10 season3_meta.json files, and {len(s3_webps)} 1024x1024 WebPs in {STAGE_DIR}")
    print(f"MD5 uniqueness check across S1({len(s1_webps)}) + S2({len(s2_webps)}) + S3({len(s3_webps)}) = {len(all_files)} WebPs: {len(seen)} unique, {len(collisions)} collisions")
    if collisions:
        raise RuntimeError(f"Collisions detected: {collisions[:5]}")


if __name__ == "__main__":
    main()
