import os
import cv2

input_path = "sample.jpg"
output_path = "sample_resized.jpg"

img = cv2.imread(input_path)

if img is None:
  print(f"Error: '{input_path}' ကို ရှာမတွေ့ပါ။ Open-CV folder ထဲမှာ ပုံထည့်ထားပါ။")
else:
  height, width = img.shape[:2]
  print(f"Original size: {width}x{height}")

  new_width = 640
  new_height = 480
  resized_img = cv2.resize(
      img, (new_width, new_height), interpolation=cv2.INTER_AREA
  )

  saved = cv2.imwrite(output_path, resized_img)
  if saved:
    print(f"Saved resized image to '{output_path}' ({new_width}x{new_height})")
  else:
    print("Error: ပုံကို သိမ်းဆည်း၍ မရပါ။")