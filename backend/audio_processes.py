from threading import Thread
from typing import Optional
from pathlib import Path
import sounddevice as sd
import soundfile as sf
import numpy as np
import time

class Recorder:
    def __init__(self):
        self.deviceindex = None
        self.sample_rate = 16000
        self.channels = 1
        self.audio_data: list = []
        self.is_recording = False
        self.recordingThread: Thread = None
        self.stream = None

    def _record(self):
        def callback(indata, frames, time_info, status):
            if self.is_recording:
                self.audio_data.append(indata.copy())
        
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype='int16',
            device=self.deviceindex,
            callback=callback,
            blocksize=1024
        )
        
        self.stream.start()
        
        while self.is_recording:
            time.sleep(0.1)
        
        self.stream.stop()
        self.stream.close()

    def start_recording(self) -> bool:
        if self.is_recording:
            return False
        
        try:
            self.audio_data = []
            self.is_recording = True
            self.recordingThread = Thread(target=self._record)
            self.recordingThread.start()
            
            time.sleep(0.1)
            return True
        except Exception as e:
            self.is_recording = False
            return False
        
    def stop_recording(self, output_path: Path) -> Path:
        if not self.is_recording:
            return False
            
        try:
            self.is_recording = False

            if self.recordingThread:
                self.recordingThread.join(timeout=2.0)  # Add timeout
            
            if not self.audio_data:
                return False
                
            audio_array = np.concatenate(self.audio_data, axis=0)
            sf.write(str(output_path), audio_array, self.sample_rate)
            
            duration = len(audio_array) / self.sample_rate
            return True
        except Exception as e:
            return False