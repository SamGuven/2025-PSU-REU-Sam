import cv2

p = "/u/samguv_guest/2025-PSU-REU-Sam/2025-PSU-REU-Sam/datasets/ECP/img/train/REPLACE_WITH_A_REAL_FILENAME.png"
img = cv2.imread(p)
print("Loaded?", img is not None)
if img is not None:
    print("Shape:", img.shape)