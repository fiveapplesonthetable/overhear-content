#!/usr/bin/env python3
"""Pre-stage Season 5 scenes.json, Season-05-Master-Script.md, and 480 bespoke 1024x1024 flat-vector WebP illustrations in scratch/s05_staged."""
import concurrent.futures
import hashlib
import json
import math
import pathlib
import re as _re
import shutil
import sys

SCRATCH = pathlib.Path("/usr/local/google/home/zezeozue/.gemini/jetski/brain/7c92d1f4-f827-44cd-97ef-f1f29eab2bd7/scratch")
sys.path.insert(0, str(SCRATCH))
import scaffold_originals as s1  # noqa: E402

STAGE_DIR = SCRATCH / "s05_staged"
ENG_DIR = STAGE_DIR / "_english"

S5_META = {
    "dvorik-u-mosta": {
        "season_title": {"ru": "Сезон 5: Тайная арка 1890 года", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "За стеной плюща",
            "Договор двух ключей",
            "Два ключа в пять часов",
            "Общий зимний сад",
            "В четверг ровно в четыре",
            "Обложка путеводителя",
        ],
    },
    "hotel-du-tilleul": {
        "season_title": {"fr": "Saison 5 : L'arche secrète de 1890", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "Derrière le mur de lierre",
            "Le pacte des deux clés",
            "Deux clés tournent à cinq heures",
            "Le jardin d'hiver partagé",
            "Jeudi à quatre heures pile",
            "La couverture du guide",
        ],
    },
    "posada-del-limonero": {
        "season_title": {"es": "Temporada 5: El arco secreto de 1890", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "Detrás del muro de hiedra",
            "El pacto de las dos llaves",
            "Dos llaves giran a las cinco",
            "El jardín de invierno compartido",
            "El jueves a las cuatro en punto",
            "La portada de la guía",
        ],
    },
    "locanda-del-tiglio": {
        "season_title": {"it": "Stagione 5: L'arco segreto del 1890", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "Dietro il muro d'edera",
            "Il patto delle due chiavi",
            "Due chiavi girano alle cinque",
            "Il giardino d'inverno condiviso",
            "Giovedì alle quattro in punto",
            "La copertina della guida",
        ],
    },
    "pousada-do-cajueiro": {
        "season_title": {"pt": "Temporada 5: O arco secreto de 1890", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "Atrás do muro de hera",
            "O pacto das duas chaves",
            "Duas chaves giram às cinco",
            "A galeria de vidro partilhada",
            "Quinta-feira às quatro em ponto",
            "A capa do guia",
        ],
    },
    "pension-sonnenhof": {
        "season_title": {"de": "Staffel 5: Der geheime Bogen von 1890", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "Hinter der Efeumauer",
            "Der Pakt der zwei Schlüssel",
            "Zwei Schlüssel um Punkt fünf",
            "Der gemeinsame Wintergarten",
            "Donnerstag Punkt vier",
            "Auf dem Titelbild des Reiseführers",
        ],
    },
    "bayt-al-yasmin": {
        "season_title": {"ar": "الموسم الخامس: القوس السري لعام ١٨٩٠", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "خلف جدار اللبلاب",
            "عهد المفتاحين",
            "مفتاحان يدوران عند الخامسة",
            "الرواق الزجاجي المشترك",
            "الخميس الرابعة تماماً",
            "غلاف الدليل الوطني",
        ],
    },
    "hidamari-ryokan": {
        "season_title": {"ja": "シーズン5：1890年の秘密のアーチ", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "ツタの壁のむこう",
            "ふたつの鍵の約束",
            "五時にまわるふたつの鍵",
            "ふたつの宿のガラス回廊",
            "木曜日の四時ちょうど",
            "ガイドブックの表紙",
        ],
    },
    "haessal-guesthouse": {
        "season_title": {"ko": "시즌 5: 1890년의 비밀 아치", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "담쟁이 벽 너머",
            "두 열쇠의 약속",
            "다섯 시에 돌아가는 두 열쇠",
            "함께 쓰는 유리 온실",
            "목요일 네 시 정각",
            "가이드북의 표지",
        ],
    },
    "xiaoyuan-kezhan": {
        "season_title": {"zh": "第五季：1890年的秘密拱门", "en": "Season 5: The Secret Arch of 1890"},
        "ep_titles": [
            "常春藤墙后面",
            "双钥之约",
            "五点钟转动两把铁钥",
            "共享玻璃花房",
            "星期四下午四点整",
            "国家指南的封面",
        ],
    },
}

S5_THEMES = [
    # E1: Behind the Ivy Wall
    [("#3E6278", "ivy_keyhole_arch"), ("#547E8C", "keyring_lock"), ("#648C78", "ivy_keyhole_arch"), ("#746498", "postal_atlas"),
     ("#C87A56", "plum_tart_tile"), ("#4A728A", "ivy_keyhole_arch"), ("#5E869E", "postal_atlas"), ("#4E6884", "copper_spout")],
    # E2: The Double-Key Pact
    [("#D68850", "stamped_loaves"), ("#6A6298", "six_blue_tiles"), ("#54867C", "copper_spout"), ("#846452", "six_blue_tiles"),
     ("#4A7E96", "six_blue_tiles"), ("#6C8E74", "lime_mortar_bowl"), ("#5A769A", "six_blue_tiles"), ("#D27262", "cobalt_cups")],
    # E3: Two Keys Turn at Five
    [("#566E94", "twin_iron_keys"), ("#589282", "six_blue_tiles"), ("#4C768C", "keyring_lock"), ("#C47E4E", "ivy_keyhole_arch"),
     ("#3E7898", "cobalt_vault"), ("#D48654", "bread_stamps"), ("#54849A", "skylight_putty"), ("#78649A", "postal_atlas")],
    # E4: The Shared Winter Garden
    [("#4E7A94", "cobalt_vault"), ("#629482", "skylight_putty"), ("#6C68A0", "leaded_doors"), ("#4C8896", "leaded_doors"),
     ("#DA844C", "stamped_loaves"), ("#528CA8", "cobalt_vault"), ("#3E6E92", "cobalt_cups"), ("#6A5C92", "twin_iron_keys")],
    # E5: Four Sharp on Thursday
    [("#58789A", "postal_atlas"), ("#C87852", "bread_stamps"), ("#46888E", "fern_mister"), ("#569678", "fern_mister"),
     ("#447498", "cobalt_cups"), ("#DC8A4E", "stamped_loaves"), ("#5E6EA2", "leaded_doors"), ("#4E6C88", "camera_tripod")],
    # E6: The Cover of the Guidebook
    [("#D29248", "camera_tripod"), ("#467A9E", "cobalt_cups"), ("#685E9A", "brass_nameplate"), ("#528496", "brass_nameplate"),
     ("#5A947C", "cobalt_vault"), ("#76669E", "postal_atlas"), ("#486A86", "attic_cupola_hatch"), ("#3E5C7A", "attic_cupola_hatch")],
]

BG_PROPS = {
    "ivy_keyhole_arch", "copper_spout", "cobalt_vault",
    "skylight_putty", "leaded_doors", "fern_mister", "attic_cupola_hatch",
}


def _star_pts(cx, cy, r_out, r_in, n=4):
    pts = []
    for i in range(n * 2):
        ang = math.radians(-90 + i * (180.0 / n))
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))
    return pts


def draw_s5_prop(c: s1.Canvas, prop: str):
    """Bespoke Season 5 flat-vector props with zero text/digits."""
    if prop == "ivy_keyhole_arch":
        c.rect(368, 86, 288, 228, "#C9C0B2", rx=48)
        c.rect(404, 122, 216, 192, "#285888", rx=38)
        c.rect(424, 144, 176, 170, "#6E4832", rx=30)
        # Star-shaped three-pronged iron keyhole + trimmed ivy leaves
        c.circle(556, 226, 16, s1.INK)
        c.rect(551, 226, 10, 24, s1.INK, rx=3)
        for ix, iy, ir in [(382, 114, 28), (416, 98, 24), (608, 104, 26), (638, 134, 24)]:
            c.circle(ix, iy, ir, "#3E845B")
    elif prop == "keyring_lock":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        c.circle(448, 616, 42, fill=None, stroke="#E5B342", sw=10)
        for ang, col in [(35, "#E5B342"), (75, "#D9A438"), (115, "#E5B342")]:
            rad = math.radians(ang)
            c.stroke_pts([(448 + math.cos(rad) * 38, 616 + math.sin(rad) * 38),
                          (448 + math.cos(rad) * 86, 616 + math.sin(rad) * 86)], col, 9)
        # Large wrought-iron clover key beside brass ring
        for dx, dy in [(-14, 0), (14, 0), (0, -14)]:
            c.circle(576 + dx, 588 + dy, 12, "#3A4452")
        c.rect(570, 596, 12, 68, "#3A4452", rx=4)
        c.rect(582, 642, 22, 16, "#3A4452", rx=3)
    elif prop == "postal_atlas":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        c.rect(396, 556, 232, 118, "#6D3F2E", rx=10)
        c.rect(410, 568, 98, 94, s1.CREAM, rx=4)
        c.rect(516, 568, 98, 94, s1.CREAM, rx=4)
        c.rect(434, 590, 52, 48, "#78B9E8", rx=4)
        c.rect(538, 590, 52, 48, "#285888", rx=4)
        c.stroke_pts([(512, 574), (512, 656)], "#E25B4B", 5)
    elif prop == "plum_tart_tile":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        c.rect(422, 574, 180, 96, "#24588A", rx=10, stroke=s1.CREAM, sw=5)
        c.ellipse(512, 618, 68, 28, "#E6A852")
        for px in (482, 512, 542):
            c.circle(px, 614, 14, "#7B2D52")
    elif prop == "copper_spout":
        c.rect(384, 82, 256, 232, "#B86E58", rx=16)
        c.rect(496, 82, 28, 232, "#469682", rx=8)
        for by in (124, 198, 272):
            c.rect(486, by, 48, 12, "#C9824C", rx=4)
        c.circle(576, 136, 16, s1.CREAM, stroke="#3A4452", sw=5)
    elif prop == "six_blue_tiles":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        c.rect(394, 554, 236, 120, "#9E5B3B", rx=12)
        for row in range(2):
            for col in range(3):
                tx = 412 + col * 68
                ty = 570 + row * 46
                c.rect(tx, ty, 60, 38, s1.CREAM, rx=4)
                c.circle(tx + 30, ty + 19, 11, "#24588A")
    elif prop == "lime_mortar_bowl":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        c.ellipse(492, 636, 82, 36, "#8C583A")
        c.ellipse(492, 622, 68, 22, "#F2EFE9")
        c.poly_fill([(556, 604), (618, 626), (576, 646)], "#C8D0D8")
        c.rect(612, 620, 42, 12, "#7A4832", rx=5)
    elif prop == "twin_iron_keys":
        c.rect(108, 672, 808, 188, "#7A543E", rx=24)
        c.rect(398, 566, 228, 104, "#EED49A", rx=10)
        for kx, tag_col in [(472, "#3B9B96"), (552, "#24588A")]:
            for dx, dy in [(-11, 0), (11, 0), (0, -11)]:
                c.circle(kx + dx, 594 + dy, 9, "#343D48")
            c.rect(kx - 5, 600, 10, 54, "#343D48", rx=3)
            c.rect(kx + 5, 638, 16, 12, "#343D48", rx=2)
            c.circle(kx - 18, 618, 9, tag_col)
    elif prop == "cobalt_vault":
        c.rect(336, 78, 352, 238, "#BEE3F8", rx=64)
        for rx in (424, 512, 600):
            c.stroke_pts([(rx, 80), (rx, 314)], "#3A4B5C", 7)
        c.stroke_pts([(338, 188), (686, 188)], "#3A4B5C", 7)
        c.rect(336, 228, 44, 88, "#24588A", rx=8)
        c.rect(644, 228, 44, 88, "#24588A", rx=8)
        c.poly_fill(_star_pts(358, 268, 10, 4, 4), "#F2C14E")
        c.poly_fill(_star_pts(666, 268, 10, 4, 4), "#F2C14E")
    elif prop == "bread_stamps":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        for sx in (418, 480, 544, 606):
            c.circle(sx, 622, 26, "#C86A4B")
            c.poly_fill(_star_pts(sx, 622, 14, 6, 4), "#F4D398")
    elif prop == "skylight_putty":
        c.rect(356, 84, 312, 224, "#9AD0F5", rx=28, stroke="#3A4B5C", sw=8)
        c.rect(462, 104, 100, 184, "#E6F6FF", rx=8, stroke="#F2C14E", sw=6)
        c.stroke_pts([(356, 196), (668, 196)], "#3A4B5C", 7)
    elif prop == "leaded_doors":
        for dx in (386, 518):
            c.rect(dx, 86, 120, 228, "#6E4730", rx=10)
            c.rect(dx + 14, 102, 92, 196, "#D8EFFC", rx=6)
            c.stroke_pts([(dx + 14, 200), (dx + 60, 102), (dx + 106, 200), (dx + 60, 298), (dx + 14, 200)], "#7A8A9A", 4)
    elif prop == "stamped_loaves":
        c.rect(110, 672, 804, 188, "#694B3C", rx=24)
        for lx in (448, 576):
            c.ellipse(lx, 628, 56, 38, "#DF9442")
            c.circle(lx, 620, 22, "#F4C45A")
            c.poly_fill(_star_pts(lx, 620, 13, 5, 4), "#9E5228")
    elif prop == "cobalt_cups":
        c.rect(110, 672, 804, 188, "#6E4C3A", rx=24)
        for i, cx in enumerate((398, 474, 550, 626)):
            col = "#24588A" if i % 2 == 0 else s1.CREAM
            c.ellipse(cx, 660, 30, 9, col)
            c.rect(cx - 20, 618, 40, 38, col, rx=8)
            if i % 2 == 0:
                c.circle(cx, 636, 5, "#F2C14E")
    elif prop == "fern_mister":
        c.stroke_pts([(140, 106), (884, 106)], "#B88446", 9)
        for fx in (280, 512, 744):
            c.circle(fx, 118, 10, "#E5B342")
            c.ellipse(fx, 188, 54, 34, "#3E8E62")
            c.ellipse(fx - 34, 198, 32, 18, "#4DA874")
            c.ellipse(fx + 34, 198, 32, 18, "#4DA874")
            for dy in (140, 156):
                c.circle(fx - 12, dy, 4, "#A6DEFF")
                c.circle(fx + 12, dy, 4, "#A6DEFF")
    elif prop == "camera_tripod":
        c.stroke_pts([(512, 622), (446, 812)], "#6E4730", 11)
        c.stroke_pts([(512, 622), (578, 812)], "#6E4730", 11)
        c.stroke_pts([(512, 622), (512, 820)], "#543422", 10)
        c.rect(458, 548, 108, 76, "#7A4832", rx=12)
        c.circle(512, 586, 26, "#E5B342")
        c.circle(512, 586, 16, "#2E3B4E")
    elif prop == "brass_nameplate":
        c.rect(104, 670, 816, 190, "#7A543E", rx=24)
        c.poly_fill([(416, 668), (608, 668), (590, 608), (434, 608)], "#E5B342")
        c.rect(454, 626, 116, 18, "#FFF4C8", rx=5)
    elif prop == "attic_cupola_hatch":
        c.stroke_pts([(48, 214), (512, 46), (976, 214)], "#5A3E2E", 30)
        c.rect(432, 108, 160, 118, s1.CREAM, rx=10, stroke="#5A3E2E", sw=8)
        c.circle(576, 166, 12, "#E5B342")
        c.stroke_pts([(576, 178), (576, 276)], "#C9963B", 6)
    else:
        s1.draw_prop(c, prop)


def render_s5_scene(args):
    show, ep_idx, sc_obj = args
    sc_idx = sc_obj["scene"] - 1
    base_dom, prop = S5_THEMES[ep_idx][sc_idx]
    tint_col, tint_amt = show["tint"]
    dom = s1.mix(base_dom, tint_col, tint_amt + 0.024 * ((ep_idx + sc_idx * 2 + 1) % 4))
    c = s1.Canvas(dom)
    spot_x = 468 + ((ep_idx * 19 + sc_idx * 29) % 88)
    spot_y = 426 + ((ep_idx + sc_idx * 2) % 3) * 6
    s1.draw_stage(c, dom, spot=(spot_x, spot_y, 408))
    if prop in BG_PROPS:
        draw_s5_prop(c, prop)

    roles = sc_obj["characters"]
    xs = [296, 728] if len(roles) == 2 else [200, 512, 824]
    rs = [95, 95] if len(roles) == 2 else [85, 92, 85]
    faces = ["smile", "happy", "o", "worried"]
    for idx, role in enumerate(roles):
        spec = show["cast"][role]
        face = faces[(ep_idx * 3 + sc_idx + idx + 2) % len(faces)]
        if prop in ("stamped_loaves", "cobalt_cups", "brass_nameplate", "camera_tripod") and face == "worried":
            face = "happy"
        forehead = (role == "M2" and ep_idx < 5 and (ep_idx + sc_idx) % 2 == 1)
        arm_l = "up" if (idx == 0 and ((ep_idx * 2 + sc_idx) % 2 == 0)) else "down"
        arm_r = "mid" if (idx == len(roles) - 1 and ((ep_idx + sc_idx) % 2 == 1)) else "in"
        look = (1 if idx == 0 else (-1 if idx == len(roles) - 1 else 0), 0)
        s1.draw_person(
            c, xs[idx], 398 + ((idx + ep_idx) % 2) * 16, rs[idx], spec,
            face=face, look=look, arm_l=arm_l, arm_r=arm_r, forehead_glasses=forehead,
        )

    if prop not in BG_PROPS:
        draw_s5_prop(c, prop)

    out_path = STAGE_DIR / show["slug"] / f"s05e{ep_idx + 1:02d}" / f"scene-{sc_obj['scene']:02d}.webp"
    c.save_webp(out_path)


def write_s5_master_markdown(episodes: list):
    lines = ["# Courtyard Inn — Season 5 Master English Script", ""]
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
    (ENG_DIR / "Season-05-Master-Script.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    episodes = [json.loads((ENG_DIR / f"s05e{i:02d}.json").read_text("utf-8")) for i in range(1, 7)]
    write_s5_master_markdown(episodes)
    if (STAGE_DIR / "bible_s05_section.md").exists():
        shutil.copyfile(STAGE_DIR / "bible_s05_section.md", ENG_DIR / "bible_s05_section.md")

    jobs = []
    for show in s1.SHOWS:
        slug = show["slug"]
        meta = S5_META[slug]

        def sub_vars(text: str) -> str:
            res = text.replace("{SHOW}", show["title"]["en"]).replace("{CITY}", show["city"]).replace("{STREET}", show["street"])
            for slot in ("F1", "M1", "F2", "M2", "F3", "M3", "M4"):
                name = show["cast"][slot][2][0]
                res = res.replace("{" + slot + "}", name)
                res = _re.sub(r"\b" + slot + r"\b", name, res)
            return res

        for ep_idx, ep in enumerate(episodes):
            ep_dir = STAGE_DIR / slug / f"s05e{ep_idx + 1:02d}"
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
                "season": 5,
                "episode": ep_idx + 1,
                "title": meta["ep_titles"][ep_idx],
                "scenes": scenes_list,
            }
            out_txt = json.dumps(scenes_json, ensure_ascii=False, indent=2) + "\n"
            assert "\u0301" not in out_txt, f"Stress mark found in {slug}"
            (ep_dir / "scenes.json").write_text(out_txt, encoding="utf-8")

        meta_txt = json.dumps(meta, ensure_ascii=False, indent=2) + "\n"
        assert "\u0301" not in meta_txt, f"Stress mark found in {slug} meta"
        (STAGE_DIR / slug / "season5_meta.json").write_text(meta_txt, encoding="utf-8")

    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as ex:
        list(ex.map(render_s5_scene, jobs))

    # Verify MD5 uniqueness across S1 + S2 + S3 + S4 + S5 (all 2,400 WebPs)!
    s1_webps = sorted((SCRATCH / "author_repo" / "originals").glob("*/s01e*/scene-*.webp"))
    s2_webps = sorted((SCRATCH / "s02_staged").glob("*/s02e*/scene-*.webp"))
    s3_webps = sorted((SCRATCH / "s03_staged").glob("*/s03e*/scene-*.webp"))
    s4_webps = sorted((SCRATCH / "s04_staged").glob("*/s04e*/scene-*.webp"))
    s5_webps = sorted(STAGE_DIR.glob("*/s05e*/scene-*.webp"))
    all_files = s1_webps + s2_webps + s3_webps + s4_webps + s5_webps
    seen = {}
    collisions = []
    for p in all_files:
        h = hashlib.md5(p.read_bytes()).hexdigest()
        if h in seen:
            collisions.append((str(seen[h]), str(p)))
        else:
            seen[h] = p
    print(f"Pre-staged 60 Season 5 scenes.json files, 10 season5_meta.json files, and {len(s5_webps)} 1024x1024 WebPs in {STAGE_DIR}")
    print(f"MD5 check across S1({len(s1_webps)}) + S2({len(s2_webps)}) + S3({len(s3_webps)}) + S4({len(s4_webps)}) + S5({len(s5_webps)}) = {len(all_files)} WebPs: {len(seen)} unique, {len(collisions)} collisions")
    if collisions:
        raise RuntimeError(f"Collisions detected: {collisions[:5]}")


if __name__ == "__main__":
    main()
