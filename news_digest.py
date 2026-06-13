import feedparser
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NEWS_SOURCES = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "The Hindu": "https://www.thehindu.com/news/feeder/default.rss",
    "Reuters": "https://feeds.reuters.com/reuters/topNews"
}
def fetch_news():

    all_news = []

    for source, url in NEWS_SOURCES.items():

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            all_news.append({
                "source": source,
                "title": entry.title,
                "link": entry.link,
                "published": getattr(entry, "published", "Unknown")
            })

    return all_news

def generate_html(news):

    html = """
    <html>
    <body>
    <h1>📰 Daily News Digest</h1>
    """

    for item in news:

        html += f"""
        <hr>
        <h3>{item['title']}</h3>

        <p>
        <b>Source:</b> {item['source']}<br>
        <b>Published:</b> {item['published']}
        </p>

        <a href="{item['link']}">
        Read Full Article
        </a>
        """

    html += """
    </body>
    </html>
    """

    return html
    

def send_email(html):

    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = MIMEMultipart()

    msg["Subject"] = "Daily News Digest"
    msg["From"] = sender
    msg["To"] = sender

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender, password)

        smtp.send_message(msg)

    print("Email Sent!")
def run():

    news = fetch_news()

    html = generate_html(news)

    send_email(html)

if __name__ == "__main__":
    run()