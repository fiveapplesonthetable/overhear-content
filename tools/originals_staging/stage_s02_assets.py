#!/usr/bin/env python3
"""Pre-stage Season 2 scenes.json and 480 bespoke 1024x1024 flat-vector WebP illustrations in scratch/s02_staged."""
import concurrent.futures
import json
import pathlib
import re as _re
import sys

SCRATCH = pathlib.Path("/usr/local/google/home/zezeozue/.gemini/jetski/brain/7c92d1f4-f827-44cd-97ef-f1f29eab2bd7/scratch")
sys.path.insert(0, str(SCRATCH))
import scaffold_originals as s1  # noqa: E402

STAGE_DIR = SCRATCH / "s02_staged"

S2_META = {
    "dvorik-u-mosta": {
        "season_title": {"ru": "Сезон 2: Комната девять", "en": "Season 2: Room Nine"},
        "ep_titles": ["За книжным шкафом", "Субботний рынок", "Молчащая клавиша", "Зелёные ставни и лимоны", "В среду в три часа", "Комната девять открыта"],
    },
    "hotel-du-tilleul": {
        "season_title": {"fr": "Saison 2 : La chambre neuf", "en": "Season 2: Room Nine"},
        "ep_titles": ["Derrière la bibliothèque", "Le marché du samedi", "La touche muette", "Volets verts et citrons", "Mercredi à trois heures", "La chambre neuf est ouverte"],
    },
    "posada-del-limonero": {
        "season_title": {"es": "Temporada 2: La habitación nueve", "en": "Season 2: Room Nine"},
        "ep_titles": ["Detrás de la librería", "El mercado del sábado", "La tecla silenciosa", "Contraventanas verdes y limones", "El miércoles a las tres", "La habitación nueve está abierta"],
    },
    "locanda-del-tiglio": {
        "season_title": {"it": "Stagione 2: La camera nove", "en": "Season 2: Room Nine"},
        "ep_titles": ["Dietro la libreria", "Il mercato del sabato", "Il tasto muto", "Persiane verdi e limoni", "Mercoledì alle tre", "La camera nove è aperta"],
    },
    "pousada-do-cajueiro": {
        "season_title": {"pt": "Temporada 2: O quarto nove", "en": "Season 2: Room Nine"},
        "ep_titles": ["Atrás da estante", "A feira de sábado", "A tecla silenciosa", "Janelas verdes e limões", "Quarta-feira às três", "O quarto nove está aberto"],
    },
    "pension-sonnenhof": {
        "season_title": {"de": "Staffel 2: Zimmer neun", "en": "Season 2: Room Nine"},
        "ep_titles": ["Hinter dem Bücherregal", "Der Samstagsmarkt", "Die stumme Taste", "Grüne Läden und Zitronen", "Mittwoch um drei", "Zimmer neun ist offen"],
    },
    "bayt-al-yasmin": {
        "season_title": {"ar": "الموسم الثاني: الغرفة التاسعة", "en": "Season 2: Room Nine"},
        "ep_titles": ["خلف خزانة الكتب", "سوق يوم السبت", "المفتاح الصامت", "نوافذ خضراء وليمون", "الأربعاء الساعة الثالثة", "الغرفة التاسعة مفتوحة"],
    },
    "hidamari-ryokan": {
        "season_title": {"ja": "シーズン2：九号室のひみつ", "en": "Season 2: Room Nine"},
        "ep_titles": ["本棚のうしろ", "土曜日の市場", "鳴らない鍵盤", "緑の雨戸とレモン", "水曜日の三時", "九号室オープン"],
    },
    "haessal-guesthouse": {
        "season_title": {"ko": "시즌 2: 구호실의 비밀", "en": "Season 2: Room Nine"},
        "ep_titles": ["책장 뒤의 문", "토요일 시장", "소리 없는 건반", "초록 덧문과 레몬", "수요일 세 시", "구호실이 열렸어요"],
    },
    "xiaoyuan-kezhan": {
        "season_title": {"zh": "第二季：九号房", "en": "Season 2: Room Nine"},
        "ep_titles": ["书架后面", "星期六集市", "不响的琴键", "绿窗板与柠檬", "星期三下午三点", "九号房开业了"],
    },
}

S2_THEMES = [
    # E1: Behind the Bookcase
    [("#6C5B7B", "cedar_box"), ("#8D6E63", "bookcase"), ("#4DA89B", "sunroom_arch"), ("#5C85A6", "piano"),
     ("#649E78", "notebook"), ("#C98B5E", "tea_cardigan"), ("#7A6FB8", "desk_bell"), ("#3D5A80", "attic_lamp")],
    # E2: The Saturday Market
    [("#5BA882", "groceries"), ("#F2C14E", "honey_lemons"), ("#78B9E8", "white_cups"), ("#E08A4B", "desk_bell"),
     ("#D96B52", "green_shutters"), ("#C9964C", "attic_lamp"), ("#8E6CC4", "music_sheet"), ("#577590", "music_sheet")],
    # E3: The Silent Key
    [("#C98B5E", "tea_cardigan"), ("#649E78", "notebook"), ("#5C85A6", "piano"), ("#78B9E8", "sunroom_arch"),
     ("#4DA89B", "green_shutters"), ("#D97C8E", "music_sheet"), ("#E08A4B", "lemon_cake"), ("#4B6584", "rain_umbrella")],
    # E4: Green Shutters and Lemons
    [("#5A9C72", "green_shutters"), ("#6BB26D", "green_shutters"), ("#5C85A6", "piano"), ("#4DA89B", "sunroom_arch"),
     ("#7A6FB8", "letter"), ("#E2604F", "tea_cardigan"), ("#C9964C", "warm_rolls"), ("#6E86A0", "white_cups")],
    # E5: Wednesday at Three
    [("#577590", "letter"), ("#F2C14E", "honey_lemons"), ("#E08A4B", "warm_rolls"), ("#86CDB2", "white_cups"),
     ("#7A6FB8", "desk_bell"), ("#5BA882", "piano"), ("#C98B5E", "tea_cardigan"), ("#D97C8E", "violin")],
    # E6: Room Nine Is Open
    [("#F2C14E", "honey_lemons"), ("#5C85A6", "bridge_key"), ("#649E78", "lanterns"), ("#E08A4B", "lemon_cake"),
     ("#8E6CC4", "violin"), ("#5BA882", "warm_rolls"), ("#4DA89B", "piano"), ("#6C5B7B", "letter")],
]

BG_PROPS = {"lanterns", "rain_umbrella", "boiler_valve", "bridge_key", "attic_lamp", "sunroom_arch"}


def draw_s2_prop(c: s1.Canvas, prop: str):
    if prop == "piano":
        c.rect(352, 545, 320, 250, "#5C3A28", rx=16)
        c.rect(372, 625, 280, 38, s1.CREAM, rx=6)
        for kx in range(388, 640, 28):
            c.rect(kx, 625, 11, 22, s1.INK, rx=2)
        c.rect(456, 560, 112, 54, s1.CREAM, rx=6)
    elif prop == "bookcase":
        c.rect(372, 540, 280, 260, "#7A4E34", rx=14)
        c.rect(392, 562, 240, 66, "#543422", rx=6)
        c.rect(392, 646, 240, 66, "#543422", rx=6)
        for bx, col in [(404, "#3B9B96"), (436, "#E2604F"), (468, "#F2C14E"), (512, "#5C85A6"), (554, "#649E78")]:
            c.rect(bx, 570, 26, 56, col, rx=4)
    elif prop == "sunroom_arch":
        c.rect(372, 95, 280, 245, "#BEE3F8", rx=36)
        c.stroke_pts([(512, 95), (512, 340)], "#FFFFFF", 10)
        c.stroke_pts([(372, 215), (652, 215)], "#FFFFFF", 10)
    elif prop == "green_shutters":
        c.rect(120, 675, 784, 185, "#6E4C3A", rx=24)
        c.rect(400, 545, 102, 145, "#4E8C64", rx=10)
        c.rect(522, 545, 102, 145, "#4E8C64", rx=10)
        for sy in (572, 602, 632, 662):
            c.stroke_pts([(416, sy), (486, sy)], "#356346", 7)
            c.stroke_pts([(538, sy), (608, sy)], "#356346", 7)
    elif prop == "honey_lemons":
        c.rect(120, 675, 784, 185, "#6E4C3A", rx=24)
        c.rect(430, 568, 78, 105, "#F2B705", rx=16)
        c.rect(440, 552, 58, 20, s1.CREAM, rx=6)
        for lx, ly in [(545, 642), (590, 646), (566, 610)]:
            c.ellipse(lx, ly, 28, 20, "#F7D436")
    elif prop == "white_cups":
        c.rect(120, 675, 784, 185, "#6E4C3A", rx=24)
        for cx in (430, 512, 594):
            c.ellipse(cx, 665, 36, 10, s1.CREAM)
            c.rect(cx - 24, 618, 48, 44, s1.CREAM, rx=10)
    elif prop == "music_sheet":
        c.rect(120, 675, 784, 185, "#6E4C3A", rx=24)
        c.rect(424, 558, 176, 118, s1.CREAM, rx=10)
        for ly in (584, 604, 624, 644):
            c.stroke_pts([(446, ly), (578, ly)], "#8C8580", 4)
        c.circle(482, 604, 9, s1.INK)
        c.circle(538, 624, 9, s1.INK)
    elif prop == "violin":
        c.rect(120, 675, 784, 185, "#6E4C3A", rx=24)
        c.ellipse(485, 628, 46, 34, "#B85D3B")
        c.ellipse(535, 628, 38, 28, "#B85D3B")
        c.rect(565, 620, 82, 16, "#3D2B24", rx=5)
        c.stroke_pts([(442, 628), (642, 628)], s1.CREAM, 4)
    else:
        s1.draw_prop(c, prop)


def render_s2_scene(args):
    show, ep_idx, sc_obj = args
    sc_idx = sc_obj["scene"] - 1
    base_dom, prop = S2_THEMES[ep_idx][sc_idx]
    tint_col, tint_amt = show["tint"]
    dom = s1.mix(base_dom, tint_col, tint_amt + 0.03 * ((ep_idx + sc_idx + 1) % 3))
    c = s1.Canvas(dom)
    spot_x = 485 + ((ep_idx * 11 + sc_idx * 17) % 55)
    s1.draw_stage(c, dom, spot=(spot_x, 438, 398))
    if prop in BG_PROPS:
        draw_s2_prop(c, prop)

    roles = sc_obj["characters"]
    xs = [308, 716] if len(roles) == 2 else [212, 512, 812]
    rs = [96, 96] if len(roles) == 2 else [86, 92, 86]
    faces = ["happy", "smile", "o", "worried"]
    for idx, role in enumerate(roles):
        spec = show["cast"][role]
        face = faces[(ep_idx * 2 + sc_idx + idx) % len(faces)]
        if prop in ("piano", "violin", "lanterns", "lemon_cake", "honey_lemons") and face == "worried":
            face = "smile"
        forehead = (role == "M2" and (ep_idx + sc_idx) % 2 == 1)
        arm_l = "up" if (idx == 0 and (sc_idx % 2 == 1)) else "down"
        arm_r = "mid" if (idx == len(roles) - 1 and (sc_idx % 2 == 0)) else "in"
        look = (1 if idx == 0 else (-1 if idx == len(roles) - 1 else 0), 0)
        s1.draw_person(c, xs[idx], 404 + (idx % 2) * 14, rs[idx], spec, face=face, look=look,
                       arm_l=arm_l, arm_r=arm_r, forehead_glasses=forehead)

    if prop not in BG_PROPS:
        draw_s2_prop(c, prop)

    out_path = STAGE_DIR / show["slug"] / f"s02e{ep_idx + 1:02d}" / f"scene-{sc_obj['scene']:02d}.webp"
    c.save_webp(out_path)


def main():
    episodes = [json.loads((s1.ENG / f"s02e{i:02d}.json").read_text("utf-8")) for i in range(1, 7)]
    jobs = []
    for show in s1.SHOWS:
        slug = show["slug"]
        meta = S2_META[slug]

        def sub_vars(text: str) -> str:
            res = text.replace("{SHOW}", show["title"]["en"]).replace("{CITY}", show["city"]).replace("{STREET}", show["street"])
            for slot in ("F1", "M1", "F2", "M2", "F3", "M3", "M4"):
                name = show["cast"][slot][2][0]
                res = res.replace("{" + slot + "}", name)
                res = _re.sub(r"\b" + slot + r"\b", name, res)
            return res

        for ep_idx, ep in enumerate(episodes):
            ep_dir = STAGE_DIR / slug / f"s02e{ep_idx + 1:02d}"
            ep_dir.mkdir(parents=True, exist_ok=True)
            scenes_list = []
            for sc in ep["scenes"]:
                scenes_list.append({
                    "scene": sc["scene"],
                    "title": sc["title"],
                    "summary": sub_vars(sc["summary"]),
                    "characters": [show["cast"][r][0] for r in sc["characters"]],
                    "location": sc["location"],
                })
                jobs.append((show, ep_idx, sc))
            scenes_json = {
                "schemaVersion": 1,
                "show": slug,
                "season": 2,
                "episode": ep_idx + 1,
                "title": meta["ep_titles"][ep_idx],
                "scenes": scenes_list,
            }
            (ep_dir / "scenes.json").write_text(json.dumps(scenes_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        # Also save season_2_entry.json for show.json update when S2 activates
        (STAGE_DIR / slug / "season2_meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as ex:
        list(ex.map(render_s2_scene, jobs))
    print(f"Pre-staged 60 Season 2 scenes.json files and {len(jobs)} 1024x1024 WebPs in {STAGE_DIR}")


if __name__ == "__main__":
    main()
