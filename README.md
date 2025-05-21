# Real-Time Image Colorization Web App

This project is a web-based image colorization tool powered by the [ncnn](https://github.com/Tencent/ncnn) deep learning framework and OpenCV. It lets users upload black & white images and colorizes them using a pre-trained neural network in real-time, with a smooth user experience.



## Inspired By

🚀 Adapted from [Qengineering's Raspberry Pi 4 Colorization Project](https://github.com/Qengineering/ncnn-Colorization_Raspberry-Pi-4) for Raspberry pi and desktop systems.

⚠️ **Note:** This version is modified to run on Ubuntu 18.04/20.04+ and **does not require a Raspberry Pi.**



## Features

- Upload black & white images via web interface
- Real-time preview of colorized image
- Download the colorized result
- Uses a custom C++ colorization backend compiled with OpenCV and ncnn
- Lightweight and efficient for quick processing


## Setup
1. Clone or download this repo
2. Install Flask
Run this in your terminal:
```
pip install flask
```
3. Run the Server. From inside the directory:
```
python3 server.py
```
Visit `http://127.0.0.1:5000` in your browser. You will now be able to upload an image.

---
If you want the woriking of the model, do the below steps:

## 🛠 Requirements

- Ubuntu 18.04/20.04+ (or similar Linux)
- OpenCV ≥ 4.5 (built with necessary modules)
- Tencent ncnn framework installed  
- g++ compiler with OpenMP support  
- Code::Blocks IDE (optional, or compile manually)


## 🧪 How to Use
1. Clone or download this repo
2. Before you can run the app, you have to download the model weights. The file is too large (125 MB) to be stored on GitHub (limited to 100 MB).
   Download location of [siggraph17_color_sim.bin](https://drive.google.com/file/d/1wdlu9IpbIPeeWdkOouGcwUttKtjK9fW8/view) at GDrive.
3. Compile the C++ app manually or load `Colorization.cbp` in Code::Blocks
4. Change input image in project -> Set program's arguement and change your image path(eg: `images_input/img.jpg`)
5. Run and check output like `colorized_out.png`


## Build tips:
- Update your build options in `Project -> Build options`
- Add your NCNN include path under **Search directories** (e.g. `../ncnn/build/install/include`)
- Add your NCNN lib path under **Linker settings** (e.g. `../ncnn/build/install/lib`)
- Add `ncnn` to the list of linked libraries
- Enable `-fopenmp` under **Compiler Flags**
- Make sure model files `siggraph17_color_sim.param` and `siggraph17_color_sim.bin` are in your project folder
- If using terminal compile, for example:

  ```bash
  g++ main.cpp -o colorize_app -fopenmp \
  -I/home/yourname/ncnn/build/install/include \
  -L/home/yourname/ncnn/build/install/lib -lncnn \
  `pkg-config --cflags --libs opencv4`
  ```


  # Final output would be:
![Example Result](static/example/exampleimage.jpg)

  ---

#### 📝 P.S.  Yep, this is *my* little corner of the internet — and I dropped my dev details inside the project just in case you want to say hi or give credit where it’s due. Because, you know, humble bragging is an art. 😎
