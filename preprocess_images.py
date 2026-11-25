from pathlib import Path
import cv2


def preprocess_folder(
    input_dir: str = "raw_images",
    output_dir: str = "processed_images",
    size: tuple[int, int] = (224, 224),
    grayscale: bool = False,
) -> None:
    src_path = Path(input_dir)
    dst_path = Path(output_dir)
    dst_path.mkdir(parents=True, exist_ok=True)

    extensions = {".jpg", ".jpeg", ".png", ".webp"}
    files = [p for p in src_path.iterdir() if p.is_file() and p.suffix.lower() in extensions]

    if not files:
        print(f"No images found in '{src_path}'.")
        return

    processed_count = 0
    for file_path in sorted(files):
        img = cv2.imread(str(file_path))
        if img is None:
            print(f"Skipping unreadable file: {file_path.name}")
            continue

        resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        if grayscale:
            resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        out_file = dst_path / file_path.name
        cv2.imwrite(str(out_file), resized)
        processed_count += 1

    print(f"Processed {processed_count} image(s) into '{dst_path}'.")


if __name__ == "__main__":
    preprocess_folder()