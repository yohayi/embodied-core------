# embodied-core：具身智能核心学习模块

## 简介
embodied-core 是一个从零开始的自主发育 AI 学习系统。它不依赖任何预训练模型，通过多模态数据（图像、音频、视频、文本、传感器）的持续交互，自动训练自编码器、聚类概念、构建世界模型，并支持 100 个隔离的“世界”并行发育。教师模型辅助将传感器数据转化为自然语言，内驱力驱动主动探索，情景记忆实现经验回溯。

本项目是具身智能体系的认知核心，为后续执行层、网络层等提供基础。

---
 ``` 

## 项目结构
embodied-core/
│
├── README.md                     # 项目说明
├── requirements.txt              # 依赖列表
├── config.py                     # 配置文件（路径、密钥等）
├── .env.example                  # 环境变量示例
├── start_ai_baby.bat             # Windows 一键启动脚本
│
├── 世界实例管理
│   ├── world_manager.py          # 世界创建、切换、删除
│   ├── world_classifier.py       # 世界分类器
│   ├── batch_create.py           # 批量创建世界
│   ├── delete_worlds.py          # 批量删除世界
│   └── fix_all_worlds.py         # 修复所有世界（补齐预处理与模型）
│
├── 数据摄入与预处理
│   ├── download_images_for_world.py
│   ├── download_audio_for_world.py
│   ├── download_videos_for_world.py
│   ├── auto_downloader.py
│   ├── preprocess_world.py
│   ├── extract_video_pairs.py
│   ├── extract_video_features.py
│   ├── generate_triplets.py
│   └── auto_doc_importer_per_world.py   # 自动导入文档
│
├── OCR 与文档解析
│   ├── ingest_any_doc.py          # 通用文档导入（PDF/Word/图片/音频/视频）
│   ├── ingest_documents.py        # 使用 PaddleOCR 提取文档文本
│   ├── ingest_formulas.py         # 公式识别（PaddleOCR + pix2tex）
│   ├── ingest_scientific_docs.py  # 使用 Nougat 处理科学 PDF
│   ├── batch_ocr.py               # 批量 OCR 图片类书籍
│   └── transcribe_audio.py        # 音频转写（Whisper）
│
├── 模型训练
│   ├── train_from_processed.py    # 图像自编码器
│   ├── train_audio_from_folder.py # 音频自编码器
│   ├── train_text_ae.py           # 文本自编码器
│   ├── train_sensor_ae.py         # 传感器自编码器
│   ├── train_world_model.py       # 世界模型（联合状态预测）
│   ├── train_video_world_model.py # 视频世界模型
│   ├── hand_learner.py            # 手部技能学习
│   ├── auto_learner.py            # 持续学习守护进程（单线程）
│   └── auto_learner_parallel.py   # 并行持续学习守护进程（含教师）
│
├── 概念聚类与认知抽象
│   ├── cluster_image_concepts.py
│   ├── cluster_audio.py
│   ├── cluster_text_concepts.py
│   ├── cluster_sensor_concepts.py
│   ├── cluster_motion_concepts.py
│   └── update_concepts.py
│
├── 多模态对齐
│   ├── align_av.py                # 图像-音频对齐
│   ├── align_multimodal.py        # 三模态对齐（图像、音频、文本）
│   └── align_multimodal_v2.py     # 四模态对齐（加传感器）
│
├── 硬件感知与动作执行
│   ├── sensor_receiver.py         # 传感器数据接收器（TCP）
│   ├── image_receiver.py          # 图像接收器（自动分类世界）
│   ├── audio_receiver.py          # 音频接收器
│   ├── simulate_sensors.py        # 模拟传感器数据生成器
│   ├── dht_receiver_robust.py     # 温湿度接收器（DHT22）
│   ├── hand_controller.py         # 手部控制器（树莓派端）
│   ├── reflex_actions.py          # 快速反射模块
│   ├── actuator_receiver.py       # 执行器响应接收（预留）
│   └── (其他接收器脚本，如 distance_receiver.py 等)
│
├── 情景记忆与状态管理
│   ├── episodic_memory.py         # 情节记忆（FAISS 索引）
│   ├── record_system_state.py     # 系统状态记录（CPU、内存、电池等）
│   └── internal_drive.py          # 内驱力计算（好奇心、疲劳等）
│
└── extra/                         # 可选，存放非核心脚本
    ├── load_resnet50.py           # 下载 pix2tex 模型（公式识别）
    ├── test_pix2text.py           # 测试公式识别
    └── ...                        # 其他测试或临时文件

---

## 快速开始

### 1. 克隆或下载代码
```bash
git clone https://github.com/你的用户名/embodied-core.git
cd embodied-core
2. 安装依赖
建议使用 Python 3.10 及以上版本。

bash
pip install -r requirements.txt
如果缺少某些依赖，按错误提示手动安装（如 pymupdf, easyocr, whisper 等）。

3. 配置
复制 .env.example 为 .env。

修改 .env 中的 AI_BABY_DATA 为你的数据目录（例如 D:/AI_MEMORY）。

若需使用自动下载功能，填写对应的 API 密钥（Pixabay、Freesound 等）。若不需要，可留空。

4. 运行
双击 start_ai_baby.bat 启动所有服务，或单独运行某个脚本：

bash
# 手动训练图像自编码器
python train_from_processed.py

# 启动持续学习守护进程
python auto_learner_parallel.py --interval 120 --threshold 12 --workers 4
5. 数据目录说明
系统运行时会在 AI_BABY_DATA 指定的目录下自动创建以下子目录：

worlds/：100 个世界实例

CONCEPTS/：全局概念中心

MODELS/：预训练模型

tmp/：临时文件

重要：请勿将真实数据提交到 Git，我们已通过 .gitignore 排除了数据目录。

系统特点
多世界并行：100 个隔离世界，独立发育

多模态数据流：自动下载图片/音频/视频，支持文档导入、传感器模拟/真实硬件

自编码器 + 概念聚类：各模态压缩为潜在向量，无监督聚类形成概念

持续学习守护进程：定时扫描新数据，自动触发训练、聚类、分类器更新

多模态对齐：通过对比学习将异构数据映射到公共语义空间

教师模型：本地 LLM（Qwen2.5-3B）为传感器数据生成自然语言指导

内驱力与情节记忆：模拟好奇心、疲劳、饥饿，结合 FAISS 存储重要事件

依赖清单（requirements.txt）
text
numpy
opencv-python
pillow
torch
torchvision
scikit-learn
faiss-cpu
psutil
easyocr
openai-whisper
librosa
soundfile
transformers
pymupdf
pdf2image
python-docx
python-dotenv
（可根据实际需要增删）

许可证
MIT

text

---

## 三、最后的检查

1. **确保 `.gitignore` 存在**，如果还没有，点击 **Add file** → **Create new file**，文件名 `.gitignore`，内容参考之前给出的排除规则（重点排除 `AI_MEMORY/`、`*.pth` 等）。如果不写，用户拉取代码时会自己创建，不影响。
2. **确认 `config.py` 和 `.env.example` 已上传**，如果没有，可以稍后补充。
3. **提交所有文件**，刷新仓库页面，应该能看到 README 渲染的树状图和说明。

这样，用户只需下载代码、安装依赖、配置环境，就能直接运行。你完全不需要本地 Git 操作，所有文件都是通过 GitHub 网页手动上传的。
