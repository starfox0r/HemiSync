import numpy as np
from scipy.io.wavfile import write

# Define the frequencies and duration of the sinus waves
left_freq = 100
right_freq = 106
duration = 120  # seconds

# Generate the left and right sinus waves
t = np.linspace(0, duration, int(duration * 44100), False)
left_signal = np.sin(left_freq * 2 * np.pi * t)
right_signal = np.sin(right_freq * 2 * np.pi * t)

# Save the left and right signals as separate WAV files
write('left.wav', 44100, left_signal)
write('right.wav', 44100, right_signal)