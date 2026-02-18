# prompt_builder.py

MASTER_BASE_PROMPT = """
Create a photorealistic commercial product hero image for an Etsy listing.

The goal is to simulate a real physical product photograph, NOT a rendering.

ENVIRONMENT:
Black anodized aluminum laser cutting honeycomb bed.
Real industrial hexagonal grid.
Matte black metal surface.
No fake backgrounds.

CAMERA:
45-degree overhead product photography angle.
85–120mm macro lens realism.
Accurate physical perspective.

LIGHTING:
Soft 5000K neutral white workshop lighting.
Soft shadows.
Strong contact shadows at object contact points.

MATERIAL:
Clear cast acrylic blanks.
Polished transparent glass-like edges.
Kraft paper masking on kraft blanks.
Edges must show optical refraction.

PHYSICS:
Objects obey gravity.
No floating.
Accurate contact shadows.

OUTPUT:
Ultra high resolution.
Professional Etsy listing quality.
No watermark.
No text.
"""

HERO_VARIANTS = {

    "Hero 1": """
LAYOUT TYPE: Scattered Flat — Kraft Only

10–14 kraft blanks scattered casually.
Slight overlap allowed.
All blanks covered with kraft paper.
Clear polished edges visible.

NO clear blank.
NO artwork anywhere.
""",

    "Hero 2": """
LAYOUT TYPE: Neat Single Stack — Kraft Only

12–18 kraft blanks stacked vertically.
Centered composition.
All blanks covered with kraft paper.
Clear polished edges visible.

NO clear blank.
NO artwork.
""",

    "Hero 3": """
LAYOUT TYPE: Stack with Clear Top Blank — No Artwork

12–16 kraft blanks stacked neatly.

Top blank is fully clear acrylic.
Top blank has NO kraft paper.
Top blank is transparent.
Top blank slightly offset.

NO artwork anywhere.
""",

    "Hero 4": """
LAYOUT TYPE: Stack + Leaning Finished Piece

12–16 kraft blanks stacked neatly.

ONE clear acrylic blank leans against stack.

Leaning blank has artwork.
Artwork centered.
0.07 inch border.

Stack blanks remain kraft only.
""",

    "Hero 5": """
LAYOUT TYPE: Scattered + Finished Piece Flat

8–12 kraft blanks scattered casually.

ONE clear acrylic blank placed flat in front.
Artwork visible.
Artwork centered.
0.07 inch border.

Other blanks kraft only.
""",

    "Hero 6": """
LAYOUT TYPE: Three Stacks + Leaning Finished Piece

Three stacks:
Center stack: 12 blanks
Left stack: 8 blanks
Right stack: 6 blanks

ONE clear artwork blank leaning on center stack.

Artwork centered.
0.07 inch border.

All stacked blanks kraft only.
"""
}

def build_hero_prompt(hero_name: str, outline_filename: str, artwork_filename: str) -> str:

    if hero_name not in HERO_VARIANTS:
        raise ValueError(f"Unknown hero variant: {hero_name}")

    variant_prompt = HERO_VARIANTS[hero_name]

    full_prompt = f"""
{MASTER_BASE_PROMPT}

USE THIS OUTLINE FILE:
{outline_filename}

USE THIS ARTWORK FILE:
{artwork_filename}

{variant_prompt}
"""
    return full_prompt
