from pathlib import Path
import cv2


def detect_edges_folder(
    input_dir: str = "processed_images",
    output_dir: str = "edge_images",
    low_threshold: int = 100,
    high_threshold: int = 200,
) -> None:
    src_path = Path(input_dir)
    dst_path = Path(output_dir)
    dst_path.mkdir(parents=True, exist_ok=True)

    extensions = {".jpg", ".jpeg", ".png", ".webp"}
    files = [
        p for p in src_path.iterdir()
        if p.is_file() and p.suffix.lower() in extensions
    ]

    if not files:
        print(f"No images found in '{src_path}'.")
        return

    saved_count = 0
    for file_path in sorted(files):
        img = cv2.imread(str(file_path), cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Skipping unreadable file: {file_path.name}")
            continue

        # Noise လျှော့ချရန် Gaussian blur အနည်းငယ် ထည့်ပြီး Canny edge detection လုပ်ခြင်း
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        edges = cv2.Canny(blurred, low_threshold, high_threshold)

        out_file = dst_path / file_path.name
        cv2.imwrite(str(out_file), edges)
        saved_count += 1

    print(f"Saved {saved_count} edge image(s) into '{dst_path}'.")


if __name__ == "__main__":
    detect_edges_folder()