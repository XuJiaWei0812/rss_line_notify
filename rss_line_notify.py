import feedparser
import requests
import time


# LINE Notify 
def lineNotify(msg):
    url = 'https://notify-api.line.me/api/notify'
    token = 'YOUR_TOKEN'  # 替換成自己的 LINE Notify 權杖
    headers = {'Authorization': 'Bearer ' + token}
    data = {'message': msg}
    requests.post(url, headers=headers, data=data)


# 檢查 RSS Feed 更新
def check_feed_updates(feed_info, last_titles):
    feed_url, platform_name = feed_info['url'], feed_info['name']
    feed = feedparser.parse(feed_url)
    latest_entry = feed.entries[0]
    if feed_url not in last_titles or latest_entry.title != last_titles[
            feed_url]:
        last_titles[feed_url] = latest_entry.title
        return latest_entry.title, latest_entry.link, platform_name
    return None, None, None


if __name__ == '__main__':
    # 各個部落格 RSS Feed 的信息
    rss_feeds = [
        {
            'url': 'https://example1.com/rss',
            'name': '部落格A'
        },
        {
            'url': 'https://example2.com/rss',
            'name': '部落格B'
        },
        # 更多 RSS Feed 資訊
    ]
    last_checked_titles = {}

    while True:
        for feed_info in rss_feeds:
            title, link, platform_name = check_feed_updates(
                feed_info, last_checked_titles)
            if title:
                message = f"部落格文章更新 \n\n文章作者：{platform_name} \n\n文章標題：{title} \n\n文章連結：\n{link}"
                lineNotify(message)
        time.sleep(3600)  # 每小時檢查一次，您可以根據需要調整這個時間間隔
