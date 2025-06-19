# LiveSegConcat  
Lossless concat tool for segmented live-stream recordings  
分段录播无损合并工具

---

## ✨  What is LiveSegConcat?
LiveSegConcat is a lightweight Python CLI that

1. batch-renames recording chunks by stripping non-ASCII (e.g. Chinese) characters,
2. filters segments by date and extension, and
3. generates an FFmpeg *concat* list to merge them into a single file **without re-encoding**.

Typical use-case: merge `.flv` / `.mp4` segments produced by Bilibili 录播姬, Twitch recorders, Streamlink etc.

---

## ⚙️  Features
| English | 中文 |
| ------- | ---- |
| Lossless join via FFmpeg `-c copy` | FFmpeg 无损拼接 |
| Auto strip Chinese / non-ASCII chars from filenames | 自动去除文件名中的中文或非 ASCII 字符 |
| Date keyword filter (e.g. `20240423`) | 按日期关键字筛选 |
| Works on Windows / macOS / Linux | 跨平台（Python 3 + FFmpeg） |
| Zero third-party Python deps | 无其他 Python 依赖 |

---

## 📦  Requirements
* Python 3.8+
* FFmpeg added to **PATH**

---

## 🚀  Quick Start

```shell
git clone https://github.com/Henry-GongZY/LiveSegConcat.git
cd LiveSegConcat
python live_seg_concat.py # CLI will ask for a date
```


---

## 🖥️  CLI Usage
| Option | 说明 |
| ------ | ---- |
| (interactive) **date** | 执行脚本时输入，如 `20240423` |
| Hard-coded `format = ['flv','mp4']` | 需要其他扩展名请自行修改 |

> Tip：可将交互式输入改为命令行参数（`argparse`）；参见 [TODO](#todo)。

---

---

## 📑  TODO
- [ ] Support `python live_seg_concat.py -d 20240423 -e flv,mp4`
- [ ] Auto sort segments by timestamp / index
- [ ] Provide a simple GUI

Contributions are welcome—issues and PRs appreciated!

---

## 🔒  License
MIT License. See [`LICENSE`](LICENSE) for full text.

---

## 🙏  Acknowledgements
Powered by the amazing [FFmpeg](https://ffmpeg.org/).  
Special thanks to the Bilibili 录播姬 community for inspiration.

---

## 中文简介

### ① 项目简介  
LiveSegConcat 是一个极简命令行工具，可将 **录播姬等软件产生的多段 `.flv/.mp4` 文件无损合并为单文件**，并自动去除文件名中的中文字符、按日期筛选目标文件。

### ② 快速使用  
1. 安装并配置好 FFmpeg。  
2. 运行 `python live_seg_concat.py`，在提示中输入日期（如 `20240423`）。  
3. 程序将生成 `20240423.flv`。  

### ③ 主要功能  
- 中文 / 非 ASCII 文件名清理  
- 日期关键字筛选  
- FFmpeg 无损拼接  
- 跨平台 & 零依赖  

### ④ 开发计划  
详见 [TODO](#todo)。

---

Happy stitching! 🎬


