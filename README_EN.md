- EN [English](README_EN.md)
- CN [中文](README.md)

# EzMd
This is a Python script that automatically extracts firmware using the md command.
# Tips
Please first connect the device to the computer using `MobaXterm` or any other serial port connection software and enter `uboot` mode.
Then, `close` the `serial debugging tool !!!` Otherwise, it will display `port occupied !!!`
![alt text](./image/image-5.png)
# Clone GitHub project
```
git clone https://github.com/Nop3z/EzMd.git
```

# Install Python library
```
pip install -r requirements.txt
```
# Usage
```
Usage:python md_EN.py
```
# Demo
```
md 0 32 #View data at addresses 0-32 in memory
```
![alt text](./image/image.png)
```
python md_EN.py #Running python scripts
```
![alt text](./image/image-6.png)
```
Drag into 010Editor to view the extracted data, which is consistent with the data extracted by the `md` command.
```

![alt text](./image/image-7.png)