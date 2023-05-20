# 🤖 Chat-History
基于Streamlit搭建的历史答疑助手，简单易用，支持以下功能：
- 多聊天窗口
- 历史对话留存
- 预设聊天上下文 
- 对话导出为Markdown文件
- 语音交流（推荐电脑端Edge浏览器）

## 使用技巧：
- 双击页面可直接定位输入栏
- Ctrl + Enter 可快捷提交问题

## 本地部署
1. 建立虚拟环境（建议
2. 克隆项目（也可以手动下载到本地）
3. 安装依赖
```bash
pip install -r requirements.txt
```
5. 启动应用
```bash
streamlit run app.py
```

## 说明
- 在[custom.py]文件中可自定义用户名和SVG格式头像。
- 在部署的项目源码中编辑[set_context.py]，即可增加预设定的上下文选项，会自动同步到应用中。

