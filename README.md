### 2. `README.md` for `feat/preprocess`

```markdown
# Batch Image Preprocessing (`feat/preprocess`)

A Python and OpenCV (`cv2`) batch preprocessing script using `pathlib` to standardize images from an input folder into an output directory.

## Feature Overview
- **Script:** `preprocess_images.py`
- **Input Directory:** `raw_images/` (supports `.jpg`, `.jpeg`, `.png`, `.webp`)
- **Output Directory:** `processed_images/` (excluded via `.gitignore`)
- **Key Capabilities:**
  - Scans `raw_images/` cleanly using `pathlib.Path`.
  - Resizes images to a uniform resolution (`224x224` by default) with `cv2.INTER_AREA` interpolation.
  - Supports optional BGR-to-grayscale conversion (`cv2.cvtColor`).
  - Safely skips unreadable or corrupted image files without crashing the batch run.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
