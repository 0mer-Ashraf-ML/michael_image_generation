# main.py
from image_generator import generate_hero_variations
from prompt_builder import build_hero_prompt

OUTLINE_PATH = "inputs/outline.png"
ARTWORK_PATH = "inputs/artwork.png"

HEROES = [
    "Hero 1",
    "Hero 2",
    "Hero 3",
    "Hero 4",
    "Hero 5",
    "Hero 6"
]

ITERATIONS_PER_HERO = 3


def run_generation():

    total_cost = 0

    for hero in HEROES:

        print(f"\n🚀 Generating {hero}")
        print("-" * 50)

        prompt = build_hero_prompt(
            hero_name=hero,
            outline_filename="outline.png",
            artwork_filename="artwork.png"
        )

        cost = generate_hero_variations(
            hero_name=hero,
            base_prompt=prompt,
            outline_path=OUTLINE_PATH,
            artwork_path=ARTWORK_PATH,
            iterations=ITERATIONS_PER_HERO,
            aspect_ratio="1:1",
            image_size="1K",
        )

        total_cost += cost

    print("\n===============================")
    print(f"Session Complete. Cost: ${total_cost:.2f}")


if __name__ == "__main__":
    run_generation()
