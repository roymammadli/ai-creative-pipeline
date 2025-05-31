import json
from uuid import uuid4

# --- Simulate Local LLM ---
def enhance_prompt(prompt):
    return f"A highly detailed digital artwork of {prompt}, in cinematic lighting, ultra HD."

# --- Simulated Openfabric API Call ---
def call_openfabric_app(app_id, input_text_or_image):
    # In a real system, you'd call the Openfabric API using the app_id
    return f"output_from_{app_id[:8]}_{uuid4().hex[:6]}"

# --- Core Pipeline Function ---
def creative_pipeline(prompt):
    memory_file = "memory.json"

    # Step 1: Interpret and enhance prompt
    enhanced_prompt = enhance_prompt(prompt)

    # Step 2: Generate image from text
    image_result = call_openfabric_app("f0997a01-d6d3-a5fe-53d8-561300318557", enhanced_prompt)

    # Step 3: Generate 3D from image
    model_result = call_openfabric_app("69543f29-4d41-4afc-7f29-3d51591f11eb", image_result)

    # Step 4: Remember the result
    entry = {
        "prompt": prompt,
        "enhanced_prompt": enhanced_prompt,
        "image_output": image_result,
        "model_output": model_result
    }

    try:
        with open(memory_file, "r") as f:
            memory = json.load(f)
    except FileNotFoundError:
        memory = []

    memory.append(entry)

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

    return entry


# --- Test Run ---
if __name__ == "__main__":
    test_prompt = "a glowing dragon standing on a cliff at sunset"
    result = creative_pipeline(test_prompt)
    print(json.dumps(result, indent=2))