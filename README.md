
# 🔫 Weapon Detection System with UI

A **Machine Learning-based Weapon Detection System** with an interactive user interface. This project uses computer vision and deep learning to detect weapons in real-time from camera feeds or uploaded videos/images.

---

## 🎯 Objective

To build an automated system that identifies weapons (like guns or knives) using a trained ML model, triggering alerts and enhancing security surveillance.

---

## 🚀 Features

- 🧠 Pre-trained deep learning model for weapon detection
- 🖥️ Interactive UI for video/image input
- 🎥 Real-time camera feed processing
- 🔊 Alarm sound on weapon detection
- 🧪 Easy-to-customize model inference code

---


## ⬇️ Model Weights

👉 > [click here to download weight file](https://drive.google.com/file/d/10uJEsUpQI3EmD98iwrwzbD4e19Ps-LHZ/view?usp=sharing)


## 🛠️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Typical packages used:
- OpenCV
- PyTorch or TensorFlow (depending on your model)
- Pygame (for sound)
- Tkinter or PyQt5 (for UI)

---

## 🧪 How to Run

```bash
python ui/interface.py
```

This will launch the GUI, allowing you to:
- Upload images/videos
- Activate your webcam
- Get real-time detection alerts

---

## 🔊 Sound Issue Fix

If `playsound` gives errors, replace it with `pygame`. Use the following fix:

```python
import pygame

def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

play_sound('alarm.wav')
```

This ensures reliable alarm triggering during detections.

---

## 📸 Sample UI Preview

> *(Insert UI screenshots here if available)*

---

## 🔒 Use Case

✅ Ideal for:
- CCTV Surveillance Systems  
- School/College/Building Security  
- Public event monitoring

---

## 📄 License

This project is open-sourced under the [MIT License](./LICENSE).

---
