### 3. `README.md` for `feat/edge-detect`

```markdown
# Canny Edge Detection (`feat/edge-detect`)

A Python and OpenCV (`cv2`) batch edge-detection script that extracts structural outlines from preprocessed images using Gaussian blur and Canny thresholding.

## Feature Overview
- **Script:** `edge_detect.py`
- **Input Directory:** `processed_images/`
- **Output Directory:** `edge_images/` (excluded via `.gitignore`)
- **Key Capabilities:**
  - Loads images in grayscale and applies `cv2.GaussianBlur` to reduce fine noise before edge detection.
  - Runs `cv2.Canny` edge detection with configurable low and high thresholds (`100` and `200` by default).
  - Saves resulting edge images to `edge_images/` and skips unreadable files safely.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
