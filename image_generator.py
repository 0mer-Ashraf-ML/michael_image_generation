import os
import time
from io import BytesIO
from PIL import Image
from google.genai import types
from gemini_client import get_client
from config import MODEL_ID, COST_PER_4K_IMAGE, COST_INPUT_IMAGE

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_image_bytes(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")
    with open(path, "rb") as f:
        return f.read()


def generate_hero_variations(
    hero_name,
    base_prompt,
    outline_path,
    artwork_path,
    iterations=5,
    aspect_ratio="1:1",
    image_size="1K",
):
    client = get_client()

    outline_bytes = load_image_bytes(outline_path)
    artwork_bytes = load_image_bytes(artwork_path)

    total_cost = 0.0

    for i in range(1, iterations + 1):
        start_time = time.time()

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=base_prompt),
                    types.Part.from_bytes(data=outline_bytes, mime_type="image/png"),
                    types.Part.from_bytes(data=artwork_bytes, mime_type="image/png"),
                ],
            )
        ]

        config = types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
                image_size=image_size,
            ),
            temperature=0,
        )

        try:
            image_bytes = None

            for chunk in client.models.generate_content_stream(
                model=MODEL_ID,
                contents=contents,
                config=config,
            ):
                for candidate in chunk.candidates:
                    for part in candidate.content.parts:
                        if part.inline_data and not part.thought:
                            image_bytes = part.inline_data.data

            if image_bytes:
                img = Image.open(BytesIO(image_bytes))

                filename = f"{hero_name.replace(' ','_')}_{i}.png"
                output_path = os.path.join(OUTPUT_DIR, filename)
                img.save(output_path)

                est_cost = COST_PER_4K_IMAGE + (COST_INPUT_IMAGE * 2)
                total_cost += est_cost

                elapsed = time.time() - start_time

                print(
                    f"✅ {hero_name} - Run #{i} | "
                    f"Size: {img.size} | "
                    f"Cost: ${est_cost:.4f} | "
                    f"Time: {elapsed:.1f}s"
                )
            else:
                print(f"⚠ {hero_name} - Run #{i}: No image returned.")

        except Exception as e:
            print(f"❌ {hero_name} - Run #{i} Error: {e}")

        time.sleep(1)

    return total_cost
