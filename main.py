from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import sounddevice as sd
from scipy.io.wavfile import write
import time

def set_input_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))
    volume_control.SetMasterVolumeLevelScalar(volume, None)

# Set the desired input gain (volume)
input_volume = 0.5  # Adjust this value (0.0 to 1.0) as needed

# Set the input volume before recording
set_input_volume(input_volume)

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recording
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
print("Recording...")
sd.wait()
print("Recording complete.")

# Save the recording as a WAV file
write("recorded_audio.wav", freq, recording)
print("Recording saved as recorded_audio.wav")
