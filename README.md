# RSS Feed LINE Notify

## 簡介
這是一個使用 Python 開發的 RSS Feed 更新通知工具。它可以定期檢查多個 RSS Feed，當發現新的文章發布時，會透過 LINE Notify 發送通知。

## 功能
- **支持多個 RSS Feed**：可以同時追蹤多個部落格或網站的 RSS Feed。
- **LINE Notify 通知**：透過 LINE Notify 服務發送新文章的更新通知。
- **自定義更新檢查**：可設定檢查新文章的時間間隔。

## 開始之前
在開始之前，請確保您已經安裝了 Python 並且設定了 LINE Notify 的權杖。

## 環境設定安裝
1. **安裝套件**：
首先安裝需要的 Python 庫:
   ```bash
   pip install feedparser requests

2. **設定 LINE Notify 權杖**：
在程式碼中找到 YOUR_TOKEN，並將其替換成您的 LINE Notify 權杖。

## 使用方法
1. **添加 RSS Feed URL**：
在 rss_feeds 列表中添加您要追蹤的 RSS Feed URL。
2. **運行腳本**：
使用以下命令來運行腳本：
   ```bash
   python rss_line_notify.py
3. **接收通知**：
每當有新文章發布時，您將通過 LINE 收到通知。
