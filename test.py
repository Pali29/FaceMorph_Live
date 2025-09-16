import numpy as np
import pyvirtualcam as pvc

frame = np.zeros((300, 200, 3), dtype=np.uint8)
frame[:10, :] = [255, 0, 0]       # Top border
frame[-10:, :] = [255, 0, 0]      # Bottom border
frame[:, :10] = [255, 0, 0]       # Left border
frame[:, -10:] = [255, 0, 0]    # Right border

