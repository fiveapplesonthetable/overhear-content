#!/usr/bin/env python3
"""Pre-stage Season 4 scenes.json, Season-04-Master-Script.md, and 480 bespoke 1024x1024 flat-vector WebP illustrations in scratch/s04_staged."""
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

STAGE_DIR = SCRATCH / "s04_staged"
ENG_DIR = STAGE_DIR / "_english"

S4_META = {
    "dvorik-u-mosta": {
        "season_title": {"ru": "Сезон 4: Фестиваль двориков", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "Пропавшая табличка у ворот",
            "Каждый гость под подозрением",
            "Трёхъярусная этажерка",
            "Четырёхметровый баннер",
            "Ровно в десять в субботу",
            "Золотая табличка",
        ],
    },
    "hotel-du-tilleul": {
        "season_title": {"fr": "Saison 4 : Le festival des cours", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "La plaque manquante du portail",
            "Chaque client est suspect",
            "Le présentoir à trois étages",
            "La banderole de quatre mètres",
            "Samedi à dix heures pile",
            "La plaque d'or",
        ],
    },
    "posada-del-limonero": {
        "season_title": {"es": "Temporada 4: El festival de los patios", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "La placa perdida del portal",
            "Cada huésped es sospechoso",
            "La torre de dulces de tres pisos",
            "La pancarta de cuatro metros",
            "El sábado a las diez en punto",
            "La placa de oro",
        ],
    },
    "locanda-del-tiglio": {
        "season_title": {"it": "Stagione 4: Il festival dei cortili", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "La targa scomparsa del portone",
            "Ogni ospite è un sospetto",
            "L'alzata per dolci a tre piani",
            "Lo striscione di quattro metri",
            "Sabato alle dieci in punto",
            "La targa d'oro",
        ],
    },
    "pousada-do-cajueiro": {
        "season_title": {"pt": "Temporada 4: O festival dos pátios", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "A placa desaparecida do portão",
            "Todo hóspede é suspeito",
            "A torre de doces de três andares",
            "A faixa de quatro metros",
            "Sábado às dez em ponto",
            "A placa de ouro",
        ],
    },
    "pension-sonnenhof": {
        "season_title": {"de": "Staffel 4: Das Innenhoffest", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "Das fehlende Torschild",
            "Jeder Gast ist verdächtig",
            "Die dreistöckige Gebäcketagere",
            "Das Vier-Meter-Banner",
            "Samstag Punkt zehn",
            "Die goldene Plakette",
        ],
    },
    "bayt-al-yasmin": {
        "season_title": {"ar": "الموسم الرابع: مهرجان الساحات", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "اللوحة النحاسية المفقودة",
            "كل ضيف موضع اشتباه",
            "حامل المعجنات ذو الطبقات الثلاث",
            "لافتة الأربعة أمتار",
            "السبت العاشرة تماماً",
            "اللوحة الذهبية",
        ],
    },
    "hidamari-ryokan": {
        "season_title": {"ja": "シーズン4：中庭フェスティバル", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "消えた門のプレート",
            "お客さまはみんな審査員？",
            "三段のお菓子スタンド",
            "四メートルの横断幕",
            "土曜日の十時ちょうど",
            "黄金のプレート",
        ],
    },
    "haessal-guesthouse": {
        "season_title": {"ko": "시즌 4: 안마당 축제", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "사라진 대문 명판",
            "모든 손님이 심사위원?",
            "삼단 빵 트레이",
            "사 미터짜리 현수막",
            "토요일 열 시 정각",
            "황금 명판",
        ],
    },
    "xiaoyuan-kezhan": {
        "season_title": {"zh": "第四季：小院文化节", "en": "Season 4: The Courtyard Festival"},
        "ep_titles": [
            "不见了的大门铜牌",
            "每位客人都是评委？",
            "三层点心架",
            "四米长的大横幅",
            "星期六上午十点整",
            "金色奖牌",
        ],
    },
}

S4_THEMES = [
    # E1: The Missing Gate Plaque
    [("#56749A", "festival_booklet"), ("#6E7F94", "empty_plaque_arch"), ("#84624E", "hallway_cupboard"), ("#4E8E84", "receipt_ledger"),
     ("#7864A2", "festival_booklet"), ("#628268", "receipt_ledger"), ("#5486A0", "cedar_screens"), ("#4A6688", "festival_booklet")],
    # E2: Every Guest Is a Suspect
    [("#665E96", "white_gloves"), ("#D4864E", "white_gloves"), ("#587CA2", "metronome"), ("#629A7A", "cedar_screens"),
     ("#7A689C", "receipt_ledger"), ("#549288", "fig_twists"), ("#C86E5A", "canvas_roll"), ("#4C7698", "oval_plaque")],
    # E3: The Three-Tier Pastry Tower
    [("#5A789C", "oval_plaque"), ("#D8844A", "fig_twists"), ("#E0A844", "pastry_tower"), ("#D26A58", "pastry_tower"),
     ("#5E9678", "cedar_screens"), ("#886652", "pastry_tower"), ("#4A6C8E", "empty_plaque_arch"), ("#74629E", "canvas_roll")],
    # E4: The Four-Metre Banner
    [("#C67258", "giant_banner"), ("#688CA8", "pennant_arch"), ("#56987A", "cedar_screens"), ("#4E849C", "flute_duet"),
     ("#D68E4E", "teapot_booth"), ("#5E789A", "pennant_arch"), ("#78609A", "festival_booklet"), ("#4B7E90", "teapot_booth")],
    # E5: Ten Sharp on Saturday
    [("#6A649E", "festival_booklet"), ("#4E8E86", "oval_plaque"), ("#587A9E", "pennant_arch"), ("#7A68A4", "flute_duet"),
     ("#DA824E", "fig_twists"), ("#5C9A78", "pastry_tower"), ("#4C829C", "white_gloves"), ("#C67E4C", "pennant_arch")],
    # E6: The Golden Plaque
    [("#5888A6", "pennant_arch"), ("#D87664", "pastry_tower"), ("#6E66A4", "flute_duet"), ("#54967E", "cedar_screens"),
     ("#C89644", "velvet_box"), ("#4C7296", "twin_plaques_arch"), ("#D27884", "flute_duet"), ("#486684", "ivy_bakehouse_arch")],
]

BG_PROPS = {
    "empty_plaque_arch", "hallway_cupboard", "cedar_screens",
    "giant_banner", "pennant_arch", "teapot_booth",
    "twin_plaques_arch", "ivy_bakehouse_arch",
}


def _star_pts(cx, cy, r_out, r_in, n=5):
    pts = []
    for i in range(n * 2):
        ang = math.radians(-90 + i * (180.0 / n))
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))
    return pts


def draw_s4_prop(c: s1.Canvas, prop: str):
    """Bespoke Season 4 festival flat-vector props with zero text/digits."""
    if prop == "festival_booklet":
        c.rect(108, 672, 808, 188, "#7A543E", rx=24)
        c.rect(424, 550, 176, 122, s1.CREAM, rx=10, stroke="#E5B342", sw=6)
        c.poly_fill(_star_pts(512, 598, 22, 9, 5), "#E5B342")
        c.rect(456, 634, 112, 14, "#4A7C9D", rx=5)
    elif prop == "empty_plaque_arch":
        c.rect(366, 78, 292, 236, "#CFC7BA", rx=48)
        c.rect(412, 128, 200, 186, "#3F4E5E", rx=32)
        c.ellipse(390, 198, 22, 14, "#E5DFD4")
        for dx, dy in [(-15, -7), (15, -7), (-15, 7), (15, 7)]:
            c.circle(390 + dx, 198 + dy, 3, s1.INK)
    elif prop == "hallway_cupboard":
        c.rect(374, 84, 276, 236, "#6E4832", rx=16)
        c.rect(394, 104, 236, 92, "#4B3022", rx=6)
        c.rect(394, 210, 236, 92, "#4B3022", rx=6)
        c.ellipse(468, 168, 34, 14, "#D9A438")
        c.circle(468, 152, 8, "#D9A438")
        c.rect(542, 132, 20, 52, "#E5B342", rx=4)
    elif prop == "receipt_ledger":
        c.rect(112, 674, 800, 186, "#6E4C3A", rx=24)
        c.rect(406, 562, 212, 110, "#3B7A5A", rx=10)
        c.rect(418, 572, 90, 90, s1.CREAM, rx=4)
        c.rect(516, 572, 90, 90, s1.CREAM, rx=4)
        c.rect(534, 584, 58, 36, "#FCE277", rx=4)
        c.circle(563, 588, 5, "#D6493E")
    elif prop == "white_gloves":
        c.rect(108, 672, 808, 188, "#7A543E", rx=24)
        # Pair of crisp white gloves + small turquoise flower vase
        c.ellipse(452, 626, 34, 24, "#FFFFFF")
        c.ellipse(504, 632, 34, 24, "#F4F6F8")
        c.rect(566, 602, 44, 64, "#3B9B96", rx=12)
        c.circle(576, 586, 15, "#F28482")
        c.circle(600, 590, 14, "#F6BD60")
    elif prop == "metronome":
        c.rect(112, 674, 800, 186, "#6E4C3A", rx=24)
        c.poly_fill([(462, 672), (562, 672), (534, 542), (490, 542)], "#7A4832")
        c.poly_fill([(484, 656), (540, 656), (524, 558), (500, 558)], s1.CREAM)
        c.stroke_pts([(512, 652), (548, 560)], "#E5B342", 7)
        c.rect(526, 588, 18, 14, "#D9A438", rx=3)
    elif prop == "cedar_screens":
        for sx in (268, 448, 628):
            c.rect(sx, 96, 128, 212, "#B87A4B", rx=10)
            c.rect(sx + 12, 108, 104, 188, "#EFE6D5", rx=6)
            c.rect(sx + 38, 276, 52, 36, "#C86D52", rx=6)
            c.circle(sx + 64, 268, 18, "#4A8C64")
    elif prop == "oval_plaque":
        c.rect(108, 672, 808, 188, "#7A543E", rx=24)
        c.rect(396, 580, 232, 92, "#2F6E56", rx=12)
        c.ellipse(512, 622, 94, 46, "#E5B342")
        c.ellipse(512, 622, 76, 34, "#F4CA64")
        for dx in (-76, 76):
            c.circle(512 + dx, 622, 5, "#6E4C3A")
    elif prop == "fig_twists":
        c.rect(112, 674, 800, 186, "#6E4C3A", rx=24)
        c.ellipse(512, 642, 136, 34, s1.CREAM)
        for tx, ty in [(448, 626), (512, 616), (576, 626), (480, 644), (544, 644)]:
            c.circle(tx, ty, 26, "#D98A46")
            c.circle(tx, ty, 12, "#8C3B4A")
    elif prop == "pastry_tower":
        c.rect(112, 674, 800, 186, "#694B3C", rx=24)
        c.rect(505, 518, 14, 154, "#E5B342", rx=4)
        c.circle(512, 514, 12, "#F2C14E")
        for ty, rx in [(656, 108), (598, 84), (544, 60)]:
            c.ellipse(512, ty, rx, 15, "#E5B342")
            for dx in (-rx + 28, 0, rx - 28):
                c.circle(512 + dx, ty - 12, 14, "#D98A46")
    elif prop == "canvas_roll":
        c.rect(112, 674, 800, 186, "#6E4C3A", rx=24)
        c.rect(322, 598, 380, 56, s1.CREAM, rx=22, stroke="#E5B342", sw=6)
        c.circle(336, 626, 24, "#E5B342")
        c.circle(688, 626, 24, "#E5B342")
    elif prop == "giant_banner":
        c.rect(164, 84, 696, 232, s1.CREAM, rx=14, stroke="#E5B342", sw=8)
        for fx in range(184, 848, 36):
            c.rect(fx, 314, 18, 24, "#E5B342", rx=4)
        c.ellipse(512, 204, 68, 52, "#E5B342")
        c.circle(512, 144, 14, "#E5B342")
        c.stroke_pts([(444, 194), (412, 168)], "#E5B342", 14)
    elif prop == "pennant_arch":
        c.rect(352, 74, 320, 240, "#D4CCC0", rx=52)
        c.rect(396, 126, 232, 188, "#3B4D5E", rx=36)
        c.stroke_pts([(140, 102), (512, 148), (884, 102)], "#FFFFFF", 6)
        cols = [s1.CREAM, "#F2C14E"]
        for i, px in enumerate(range(180, 845, 56)):
            py = 108 + round(36 * (1 - abs(px - 512) / 372))
            c.poly_fill([(px - 22, py), (px + 22, py), (px, py + 42)], cols[i % 2])
    elif prop == "teapot_booth":
        c.rect(424, 90, 176, 156, s1.CREAM, rx=14, stroke="#E5B342", sw=7)
        c.ellipse(512, 178, 46, 36, "#E5B342")
        c.circle(512, 136, 10, "#E5B342")
        c.stroke_pts([(466, 170), (444, 152)], "#E5B342", 10)
    elif prop == "flute_duet":
        c.rect(344, 544, 336, 250, "#5C3A28", rx=16)
        c.rect(366, 626, 292, 38, s1.CREAM, rx=6)
        for kx in range(382, 646, 26):
            c.rect(kx, 626, 11, 22, s1.INK, rx=2)
        c.stroke_pts([(404, 578), (620, 564)], "#DCE4EC", 10)
        c.stroke_pts([(412, 598), (628, 584)], "#DCE4EC", 10)
    elif prop == "velvet_box":
        c.rect(112, 674, 800, 186, "#6E4C3A", rx=24)
        c.rect(416, 552, 192, 122, "#243B6B", rx=14)
        c.rect(438, 572, 148, 82, "#F2C14E", rx=10)
        c.poly_fill(_star_pts(512, 613, 24, 10, 5), s1.CREAM)
    elif prop == "twin_plaques_arch":
        c.rect(344, 76, 336, 240, "#D4CCC0", rx=52)
        c.rect(396, 128, 232, 188, "#35495E", rx=36)
        c.ellipse(370, 198, 22, 14, "#E5B342")
        c.rect(636, 182, 36, 30, "#F2C14E", rx=5)
    elif prop == "ivy_bakehouse_arch":
        c.rect(376, 104, 272, 212, "#8C5843", rx=18)
        c.rect(424, 168, 176, 148, "#5C4438", rx=88)
        c.circle(512, 246, 18, fill=None, stroke="#2E2A3A", sw=7)
        for ix, iy, ir in [(394, 124, 34), (438, 112, 30), (586, 116, 32), (628, 142, 28), (388, 176, 26)]:
            c.circle(ix, iy, ir, "#46895E")
    else:
        s1.draw_prop(c, prop)


def render_s4_scene(args):
    show, ep_idx, sc_obj = args
    sc_idx = sc_obj["scene"] - 1
    base_dom, prop = S4_THEMES[ep_idx][sc_idx]
    tint_col, tint_amt = show["tint"]
    dom = s1.mix(base_dom, tint_col, tint_amt + 0.022 * ((ep_idx * 3 + sc_idx + 2) % 4))
    c = s1.Canvas(dom)
    spot_x = 472 + ((ep_idx * 17 + sc_idx * 23) % 76)
    spot_y = 428 + ((ep_idx * 2 + sc_idx) % 3) * 5
    s1.draw_stage(c, dom, spot=(spot_x, spot_y, 406))
    if prop in BG_PROPS:
        draw_s4_prop(c, prop)

    roles = sc_obj["characters"]
    xs = [300, 724] if len(roles) == 2 else [204, 512, 820]
    rs = [94, 94] if len(roles) == 2 else [85, 91, 85]
    faces = ["happy", "smile", "o", "worried"]
    for idx, role in enumerate(roles):
        spec = show["cast"][role]
        face = faces[(ep_idx * 2 + sc_idx * 3 + idx + 1) % len(faces)]
        if prop in ("velvet_box", "twin_plaques_arch", "fig_twists", "flute_duet") and face == "worried":
            face = "happy"
        forehead = (role == "M2" and ep_idx < 4 and (ep_idx + sc_idx) % 2 == 0)
        arm_l = "up" if (idx == 0 and ((ep_idx + sc_idx) % 2 == 1)) else "down"
        arm_r = "mid" if (idx == len(roles) - 1 and ((ep_idx + sc_idx) % 2 == 0)) else "in"
        look = (1 if idx == 0 else (-1 if idx == len(roles) - 1 else 0), 0)
        s1.draw_person(
            c, xs[idx], 400 + ((idx + ep_idx + 1) % 2) * 15, rs[idx], spec,
            face=face, look=look, arm_l=arm_l, arm_r=arm_r, forehead_glasses=forehead,
        )

    if prop not in BG_PROPS:
        draw_s4_prop(c, prop)

    out_path = STAGE_DIR / show["slug"] / f"s04e{ep_idx + 1:02d}" / f"scene-{sc_obj['scene']:02d}.webp"
    c.save_webp(out_path)


def write_s4_master_markdown(episodes: list):
    lines = ["# Courtyard Inn — Season 4 Master English Script", ""]
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
    (ENG_DIR / "Season-04-Master-Script.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    episodes = [json.loads((ENG_DIR / f"s04e{i:02d}.json").read_text("utf-8")) for i in range(1, 7)]
    write_s4_master_markdown(episodes)

    jobs = []
    for show in s1.SHOWS:
        slug = show["slug"]
        meta = S4_META[slug]

        def sub_vars(text: str) -> str:
            res = text.replace("{SHOW}", show["title"]["en"]).replace("{CITY}", show["city"]).replace("{STREET}", show["street"])
            for slot in ("F1", "M1", "F2", "M2", "F3", "M3", "M4"):
                name = show["cast"][slot][2][0]
                res = res.replace("{" + slot + "}", name)
                res = _re.sub(r"\b" + slot + r"\b", name, res)
            return res

        for ep_idx, ep in enumerate(episodes):
            ep_dir = STAGE_DIR / slug / f"s04e{ep_idx + 1:02d}"
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
                "season": 4,
                "episode": ep_idx + 1,
                "title": meta["ep_titles"][ep_idx],
                "scenes": scenes_list,
            }
            out_txt = json.dumps(scenes_json, ensure_ascii=False, indent=2) + "\n"
            assert "\u0301" not in out_txt, f"Stress mark found in {slug}"
            (ep_dir / "scenes.json").write_text(out_txt, encoding="utf-8")

        meta_txt = json.dumps(meta, ensure_ascii=False, indent=2) + "\n"
        assert "\u0301" not in meta_txt, f"Stress mark found in {slug} meta"
        (STAGE_DIR / slug / "season4_meta.json").write_text(meta_txt, encoding="utf-8")

    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as ex:
        list(ex.map(render_s4_scene, jobs))

    # Verify MD5 uniqueness across S1 + S2 + S3 + S4 (all 1,920 WebPs)!
    s1_webps = sorted((SCRATCH / "author_repo" / "originals").glob("*/s01e*/scene-*.webp"))
    s2_webps = sorted((SCRATCH / "s02_staged").glob("*/s02e*/scene-*.webp"))
    s3_webps = sorted((SCRATCH / "s03_staged").glob("*/s03e*/scene-*.webp"))
    s4_webps = sorted(STAGE_DIR.glob("*/s04e*/scene-*.webp"))
    all_files = s1_webps + s2_webps + s3_webps + s4_webps
    seen = {}
    collisions = []
    for p in all_files:
        h = hashlib.md5(p.read_bytes()).hexdigest()
        if h in seen:
            collisions.append((str(seen[h]), str(p)))
        else:
            seen[h] = p
    print(f"Pre-staged 60 Season 4 scenes.json files, 10 season4_meta.json files, and {len(s4_webps)} 1024x1024 WebPs in {STAGE_DIR}")
    print(f"MD5 check across S1({len(s1_webps)}) + S2({len(s2_webps)}) + S3({len(s3_webps)}) + S4({len(s4_webps)}) = {len(all_files)} WebPs: {len(seen)} unique, {len(collisions)} collisions")
    if collisions:
        raise RuntimeError(f"Collisions detected: {collisions[:5]}")


if __name__ == "__main__":
    main()
