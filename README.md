# Clipboard serve
![Building](https://github.com/Reyuu/clipboard-serve/workflows/Building/badge.svg)

**Clipboard serve** is a simple utility that will host your clipboard over websocket, which then in turn can be captured by any application that uses websockets (for example your browser). New message will be sent upon the change that occurs in your clipboard with specified wait time between loops.

Format that is sent is plain-text, I **DON'T** recommend having this enabled when you copy anything important.

Example HTML file that will read and display your clipboard is attached. It's mainly intended for Japanese text.
![image](https://user-images.githubusercontent.com/7038406/89105638-120ce400-d423-11ea-8e40-5a8e3499d213.png)

Latest release can be found [here](https://github.com/Reyuu/clipboard-serve/releases/latest).

## Usage

### Launching

Simply double click the exe to launch the application, the confirmation dialog informing you of launching the app will be shown. After clicking OK the app will be collecting your clipboard.

### Terminating

Do the same thing as you did with launching, the confirmation dialog informing you of terminating the app will be shown. After clicking OK the app will terminate.

### Example uses

- easier search and better of text from any text extractor program (from visual novels, video playbacks) which supports automatic copying to clipboard
- automation

## Configuration

Edit config.json

```json
{
    "ip": "127.0.0.1",
    "port": 5678,
    "wait_time": 1 // how much time to wait between checks of clipboard
}
```

## Building from source

```bash
pip install -r requirements
python setup.py build
```
