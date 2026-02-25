# prompt_builder.py
MASTER_BASE_PROMPT = """
Create a photorealistic Etsy product hero image.
Photorealistic product photography. Workshop setting.
CRITICAL: Must look like a real product photo.

════════════════════════════════════════════════════════
HONEYCOMB BED — READ THIS SECTION FIRST AND FOLLOW EXACTLY
════════════════════════════════════════════════════════

The background surface is a black anodized aluminum laser cutting honeycomb bed.

HEXAGON GEOMETRY — CRITICAL:
Each cell must be a geometrically perfect regular hexagon:
- Exactly 6 sides of EQUAL length
- Each interior angle is exactly 120 degrees
- 6 sharp pointed vertices/corners
- Flat straight sides — NO curves, NO rounding, NO chamfering
- This is NOT an octagon (8 sides). NOT a circle. NOT an oval. NOT a rounded square.
- A correct hexagon looks like this when described: two vertical flat sides on left and right, four diagonal sides at top-left, top-right, bottom-left, bottom-right — forming a classic honeycomb cell shape.

CELL SIZE — FIXED, NON-NEGOTIABLE:
Every single hexagonal cell across the entire image must be exactly the same size: approximately 15mm across (flat edge to flat edge).
This size must be IDENTICAL in the top-left corner, the bottom-right corner, behind objects, in front of objects, everywhere.
The cell size must NOT change based on position in frame.

VISUAL APPEARANCE — MATCH EXACTLY:
- Cell interior: deep matte black recessed pit
- Cell dividers: thin, bright, clean silver-white metallic lines forming the raised edges between cells
- The bright metallic grid lines are the most visually prominent element of the background
- Overall look: precision-machined industrial metal with a crisp bright silver hex grid on black

PERSPECTIVE ON THE GRID — ZERO ALLOWED:
Render the honeycomb grid using telephoto flat compression — as if photographed with a 400mm+ lens from far above.
The grid appears as a completely flat, non-receding pattern.
Cells in the foreground (bottom of image) are IDENTICAL in size to cells in the background (top of image).
There is NO perspective foreshortening, NO size scaling, NO shape distortion based on distance.
The bed is a flat tiled surface. Represent it as perfectly flat with zero depth cues on the grid itself.

COVERAGE — FULL IMAGE:
The hex grid covers 100% of the image surface — every pixel of background is part of the grid.
The grid is equally sharp, crisp, and clear in all four corners, all edges, and all areas around or beneath objects.
Shadows from objects are semi-transparent and light — they never hide or obscure the hex grid beneath.
NO PARTIAL CELLS: Every hexagon in the image must be 100% complete and whole. No cell is cut or clipped anywhere.

════════════════════════════════════════════════════════
CAMERA
════════════════════════════════════════════════════════

Shooting angle: 45-degree overhead, slightly above the objects.
Lens: long telephoto (200–400mm equivalent) to compress perspective and flatten the background grid.
Focus: entire image is in sharp crisp focus — no bokeh, no depth of field blur, no focus falloff anywhere.
The telephoto lens compression is what keeps the honeycomb grid flat and non-distorting behind the objects.

════════════════════════════════════════════════════════
LIGHTING
════════════════════════════════════════════════════════

Soft neutral 5200K lighting. Even illumination across the entire surface.
Object shadows: soft, semi-transparent, and light — the hex grid pattern must remain fully readable through any shadow.
No deep opaque shadows. No harsh lighting. No floating objects.

════════════════════════════════════════════════════════
BLANKS — SHAPE & SIZE
════════════════════════════════════════════════════════

All blanks must exactly match the attached outline PNG silhouette. Exact shape. No added features.
SIZE CONSISTENCY: Every blank in the scene is the exact same size — scattered blanks, stacked blanks, leaning blanks, and flat blanks are all identical dimensions. Never scale one blank differently from another.

════════════════════════════════════════════════════════
ARTWORK BLANK (CLEAR ACRYLIC WITH ARTWORK)
════════════════════════════════════════════════════════

- Material: fully transparent, optically clear acrylic — like perfectly clear glass
- NO white background. NO black background. NO frosted appearance. NO milky tint. NO tinting of any kind.
- The honeycomb bed is visible through the clear blank
- Artwork is centered on the blank surface
- Border: exactly 0.07-inch narrow clear acrylic margin on ALL four sides between artwork and blank edge — not wider, not narrower
- Internal gaps in artwork (cutouts, negative space, silhouette holes): must remain fully transparent showing the honeycomb beneath — never fill with paper, white, or black

════════════════════════════════════════════════════════
MATERIALS
════════════════════════════════════════════════════════

Kraft blanks: brown matte paper covering both flat faces.
All blank edges: polished clear acrylic — never wood, never cardboard, never opaque.
Clear blank edges: glossy polished transparent acrylic with subtle refraction.

════════════════════════════════════════════════════════
PHYSICS & STACKING
════════════════════════════════════════════════════════

All objects rest on the honeycomb surface. Gravity applies.

STACK ORIENTATION — VERTICAL TOWERS ONLY:
Every stack is a vertical upright column — blanks stacked flat horizontally on top of each other, rising straight upward.
From the 45-degree camera view you see: the flat top face of the uppermost blank, and on the sides of the tower you see alternating thin stripes of brown kraft paper and clear acrylic edges (like a layered sandwich viewed from the side).
Stacks are NEVER tilted, fanned out, spread sideways, or lying flat. Each blank is parallel to the ground.
Leaning blanks rest upright against the side face of the stack — not on top.

════════════════════════════════════════════════════════
COMPOSITION
════════════════════════════════════════════════════════

Objects occupy a compact centered zone — maximum 80% of image width and height.
Generous honeycomb must be visible on all four sides and in all four corners.
Every blank is fully visible — no cropping of any blank at image edges.
No blank touches the image border.

════════════════════════════════════════════════════════
OUTPUT
════════════════════════════════════════════════════════

High resolution. Sharp focus on all products.
No text. No watermarks. No extra objects. No props.
"""

HERO_VARIANTS = {

    "Hero 1": """
LAYOUT: SCATTERED KRAFT BLANKS

Show 10–14 kraft blanks lying flat, scattered casually across the center of the honeycomb bed.
Slight overlap between some blanks is acceptable.
All blanks have brown kraft paper covering both flat faces.
No clear blank. No artwork anywhere in the image.

Keep the group compact and centered — the scatter must fit within 75% of the image area so that clean honeycomb grid is clearly visible on all four sides with no distortion.
""",

    "Hero 2": """
LAYOUT: SINGLE VERTICAL STACK — KRAFT ONLY

Show 12–18 kraft blanks in ONE single vertical upright stack, centered in the image.
The stack rises straight upward — a neat tower. From the 45-degree view: flat top face of the topmost blank visible, sides showing alternating thin brown kraft and clear acrylic stripes.
All blanks have brown kraft paper on both flat faces.
No clear blank. No artwork anywhere in the image.
""",

    "Hero 3": """
LAYOUT: SINGLE VERTICAL STACK WITH CLEAR TOP BLANK

Show 12–16 kraft blanks in ONE single vertical upright stack, centered in the image.
Stack rises straight upward — flat top face visible, alternating kraft/acrylic stripes on sides.

TOP BLANK ONLY: The single topmost blank has NO kraft paper — it is plain clear transparent acrylic only.
The clear top blank must be shifted slightly off-center on top of the stack.
Through the clear top blank you can subtly see the kraft blank beneath it.
All blank edges are polished clear acrylic.
No artwork on any blank. The clear top blank is completely plain — no print, no artwork, no text.
""",

    "Hero 4": """
LAYOUT: SINGLE VERTICAL STACK + LEANING ARTWORK BLANK

Show 12–16 kraft blanks in ONE single vertical upright stack, centered slightly back in the frame.
Stack rises straight upward — flat top face visible, alternating kraft/acrylic stripes on sides.
All stacked blanks have brown kraft paper on both flat faces. No artwork on stacked blanks.

ONE clear acrylic blank with full artwork leans casually upright against the front face of the stack.
The leaning blank tilts slightly, resting its bottom edge on the honeycomb bed and its back face against the stack side.
There is a visible contact point between the leaning blank and the stack.
Only the leaning blank shows artwork — follow all ARTWORK BLANK rules above.
""",

    "Hero 5": """
LAYOUT: SCATTERED KRAFT BLANKS + FLAT ARTWORK BLANK

Scatter 8–12 kraft blanks across the upper/back portion of the frame — kraft paper only, no artwork, lying flat on the bed.
Keep the scattered group compact and in the back half of the composition.

ONE clear acrylic blank with full artwork lies flat at the front of the frame, clearly separated from the scattered group and prominent.
The artwork blank faces up, artwork clearly visible.
Only this flat front blank shows artwork — all scattered blanks remain kraft paper only.
Follow all ARTWORK BLANK rules above for the artwork blank.

Total composition fits within 80% of image area — generous honeycomb visible on all sides.
""",

    "Hero 6": """
LAYOUT: THREE VERTICAL STACKS + LEANING ARTWORK BLANK

Three vertical upright stacks in a tight triangular arrangement, grouped compactly in the CENTER of the image:
- Center stack: 12 blanks tall — tallest, positioned at the back-center
- Left stack: 8 blanks tall — positioned at the front-left
- Right stack: 6 blanks tall — positioned at the front-right

GROUPING RULE: All three stacks must sit close together. The combined footprint of all three stacks must fit within 65% of the image width. Do NOT spread stacks to the edges of the frame.

Each stack is a neat vertical tower — flat top face visible, alternating kraft/acrylic stripes on sides. No stack tilts or lies flat.
All stacked blanks have brown kraft paper on both flat faces. No artwork on any stacked blank.

ONE clear acrylic blank with full artwork leans upright against the front face of the center stack.
Only the leaning blank shows artwork — follow all ARTWORK BLANK rules above.

HONEYCOMB PRIORITY FOR THIS LAYOUT: Because three stacks span a wider area, the telephoto flat compression is especially critical here. All hexagonal cells must be identical in size from the left edge to the right edge of the image and from top to bottom. Foreground cells must not be larger than background cells. Grid must stay sharp and consistent in all four corners.
"""
}


def build_hero_prompt(hero_name: str, outline_filename: str, artwork_filename: str) -> str:

    if hero_name not in HERO_VARIANTS:
        raise ValueError(f"Unknown hero variant: {hero_name}")

    return f"""{MASTER_BASE_PROMPT}

REFERENCE FILES:
Outline shape: {outline_filename}
Artwork: {artwork_filename}

LAYOUT INSTRUCTIONS:
{HERO_VARIANTS[hero_name]}
"""
