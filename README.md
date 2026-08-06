# Instagram Email Scraper

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/data-scrape/instagram-email-scraper?style=social)](https://github.com/data-scrape/instagram-email-scraper)
[![GitHub forks](https://img.shields.io/github/forks/data-scrape/instagram-email-scraper?style=social)](https://github.com/data-scrape/instagram-email-scraper/fork)
[![GitHub issues](https://img.shields.io/github/issues/data-scrape/instagram-email-scraper)](https://github.com/data-scrape/instagram-email-scraper/issues)
[![GitHub license](https://img.shields.io/github/license/data-scrape/instagram-email-scraper)](https://github.com/data-scrape/instagram-email-scraper/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)

</div>


> Instagram email scraper - extract emails from Instagram bios and profiles


<!-- SEO keywords: instagram email scraper, Instagram Email Scraper, instagram email scraper python, instagram email scraper github, best instagram email scraper -->


<div align="center">

## 💎 Sponsored by CoreClaw

[![CoreClaw](https://img.shields.io/badge/CoreClaw-Data_Scraping_Platform-7B2FF7?style=for-the-badge&labelColor=5B21B6)](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

**The All-in-One Web Scraping & Data Platform** — Scrape Google Maps, Instagram, Amazon, LinkedIn, TikTok, YouTube, and 50+ platforms via ready-to-use REST APIs.

✅ No browser automation · ✅ No proxy management · ✅ Free credits for new users

⬇️ [Get Started with CoreClaw Free](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

</div>

---

## 🔥 Features

- Extract email addresses from Instagram profile bios
- Scan follower/following lists for emails
- Bulk email extraction from multiple profiles
- Email validation and deduplication
- Export to CSV for CRM import
- Proxy rotation for large-scale extraction
- Custom rate limiting to avoid detection
- Bio link scraping for additional contact info

## 🎯 Use Cases

Build email lists from Instagram influencers, extract business contact info from profiles, or enrich existing lead databases with Instagram data.

## 📊 Data Fields Extracted

| Field | Description |
|-------|-------------|
| `username` | Instagram username |
| `media_url` | Direct URL to media |
| `timestamp` | Upload timestamp (ISO 8601) |
| `caption` | Post caption text |
| `likes` | Number of likes |
| `comments_count` | Number of comments |
| `media_type` | IMAGE / VIDEO / CAROUSEL |
| `dimensions` | Width x Height in pixels |

## 💻 Configuration

```python
# config.py
CONFIG = {
    "max_concurrent": 5,
    "rate_limit_ms": 1000,
    "proxy_list": [],  # Add your proxy URLs
    "output_format": "json",  # json, csv, excel
    "download_media": True,
    "media_quality": "high",  # high, medium, low
}
```

## 🔁 Output Example

```python
scrape_instagram_emails("username")
# Extracts emails from bio and posts
# Returns: [{'username': '...', 'email': 'user@example.com', 'source': 'bio'}, ...]
```


## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<sup>Built with ❤️ for the web scraping community</sup>

</div>


<!-- INSTALL_SECTION_START -->
## 📦 Installation

### Using pip

```bash
pip install git+https://github.com/data-scrape/instagram-email-scraper.git
```

### From source

```bash
git clone https://github.com/data-scrape/instagram-email-scraper.git
cd instagram-email-scraper
pip install -e .
```

### Prerequisites

- Python 3.8+
- Required packages listed in `requirements.txt`

<!-- INSTALL_SECTION_END -->


<!-- USAGE_SECTION_START -->
## 🚀 Quick Start

### Basic Usage

```python
# Quick example - see examples/ directory for more
from instagram_email_scraper import Scraper

scraper = Scraper()
results = scraper.scrape("your-query")
print(results)
```

### CLI Usage

```bash
# Run from command line
python -m instagram_email_scraper --query "your-query" --output results.json
```

> 💡 **Tip**: Check the `examples/` directory for detailed usage examples and the `docs/` folder for full documentation.

<!-- USAGE_SECTION_END -->


<!-- FAQ_SECTION_START -->
## 🤔 FAQ

### Is Instagram Email Scraper legal to use?

This tool is designed for scraping publicly available data. Always review and comply with the target website's Terms of Service and robots.txt. Use responsibly and within legal boundaries.

### Do I need to login to use instagram email scraper?

Most public data can be accessed without login. Some features (like private profiles or stories) may require authentication credentials.

### Will I get banned for using instagram email scraper?

The tool includes built-in rate limiting and proxy support to minimize detection. Always use reasonable delays and respect the target platform's rate limits.

### What data formats does Instagram Email Scraper support?

Output is available in JSON, CSV, and Excel formats. You can also access raw Python data structures for custom processing.

### Can I use instagram email scraper for commercial purposes?

Yes, this project is licensed under the MIT License. However, you are responsible for ensuring your use of scraped data complies with applicable laws and the target platform's terms.

<!-- FAQ_SECTION_END -->


<!-- CROSS_LINKS_START -->
## Related Scrapers

Explore our full collection of open-source scrapers:

### Amazon Scrapers

- [amazon-asin-scraper](https://github.com/data-scrape/amazon-asin-scraper)
- [amazon-price-scraper](https://github.com/data-scrape/amazon-price-scraper)
- [amazon-product-scraper](https://github.com/data-scrape/amazon-product-scraper)
- [amazon-review-scraper](https://github.com/data-scrape/amazon-review-scraper)
- [amazon-scraper-api](https://github.com/data-scrape/amazon-scraper-api)
- [best-amazon-scraper](https://github.com/data-scrape/best-amazon-scraper)

### Facebook Scrapers

- [best-facebook-scraper](https://github.com/data-scrape/best-facebook-scraper)
- [facebook-group-scraper](https://github.com/data-scrape/facebook-group-scraper)
- [facebook-marketplace-scraper](https://github.com/data-scrape/facebook-marketplace-scraper)
- [facebook-page-scraper](https://github.com/data-scrape/facebook-page-scraper)
- [facebook-post-scraper](https://github.com/data-scrape/facebook-post-scraper)
- [facebook-profile-scraper](https://github.com/data-scrape/facebook-profile-scraper)
- [facebook-scrape-website](https://github.com/data-scrape/facebook-scrape-website)

### Google Maps Scrapers

- [apify-google-maps-scraper](https://github.com/data-scrape/apify-google-maps-scraper)
- [best-google-maps-scraper](https://github.com/data-scrape/best-google-maps-scraper)
- [google-map-scraper-api-](https://github.com/data-scrape/google-map-scraper-api-)
- [google-maps-data-scraper](https://github.com/data-scrape/google-maps-data-scraper)
- [outscraper-google-maps-scraper](https://github.com/data-scrape/outscraper-google-maps-scraper)
- [scrape-google-maps](https://github.com/data-scrape/scrape-google-maps)

### Google Scrapers

- [best-google-search-scraper](https://github.com/data-scrape/best-google-search-scraper)
- [google-business-scraper](https://github.com/data-scrape/google-business-scraper)
- [google-place-id-api](https://github.com/data-scrape/google-place-id-api)
- [google-reviews-scraper](https://github.com/data-scrape/google-reviews-scraper)
- [google-shopping-scraper](https://github.com/data-scrape/google-shopping-scraper)

### Indeed Job Scrapers

- [apify-indeed-scraper](https://github.com/data-scrape/apify-indeed-scraper)
- [best-indeed-scraper](https://github.com/data-scrape/best-indeed-scraper)
- [indeed-job-scraper](https://github.com/data-scrape/indeed-job-scraper)
- [scrape-indeed-job-postings](https://github.com/data-scrape/scrape-indeed-job-postings)

### Instagram Scrapers

- [apify-instagram-scraper](https://github.com/data-scrape/apify-instagram-scraper)
- [best-instagram-scraper](https://github.com/data-scrape/best-instagram-scraper)
- [instagram-account-scraper](https://github.com/data-scrape/instagram-account-scraper)
- [instagram-comment-scraper](https://github.com/data-scrape/instagram-comment-scraper)
- [instagram-follower-scraper](https://github.com/data-scrape/instagram-follower-scraper)
- [instagram-profile-scraper](https://github.com/data-scrape/instagram-profile-scraper)
- [instagram-scraper](https://github.com/data-scrape/instagram-scraper)
- [scrape-instagram-followers](https://github.com/data-scrape/scrape-instagram-followers)
- [scrape-instagram-photos](https://github.com/data-scrape/scrape-instagram-photos)

### Lead Generation Tools

- [awesome-lead-generation](https://github.com/data-scrape/awesome-lead-generation)

### LinkedIn Scrapers

- [best-linkedin-scraper](https://github.com/data-scrape/best-linkedin-scraper)
- [linkedin-email-scraper](https://github.com/data-scrape/linkedin-email-scraper)
- [linkedin-job-scraper](https://github.com/data-scrape/linkedin-job-scraper)
- [linkedin-post-scraper](https://github.com/data-scrape/linkedin-post-scraper)
- [linkedin-profile-data-scraper](https://github.com/data-scrape/linkedin-profile-data-scraper)
- [linkedin-sales-navigator-scraper](https://github.com/data-scrape/linkedin-sales-navigator-scraper)
- [linkedin-scraper-api](https://github.com/data-scrape/linkedin-scraper-api)

### Other Scrapers

- [blog](https://github.com/data-scrape/blog)

### Proxy & API Alternatives

- [awesome-apify-alternatives](https://github.com/data-scrape/awesome-apify-alternatives)
- [best-apify-alternative](https://github.com/data-scrape/best-apify-alternative)
- [bright-data-alternative](https://github.com/data-scrape/bright-data-alternative)
- [oxylabs-alternative](https://github.com/data-scrape/oxylabs-alternative)
- [scraperapi-alternative](https://github.com/data-scrape/scraperapi-alternative)
- [scrapingbee-alternative](https://github.com/data-scrape/scrapingbee-alternative)
- [serpapi-alternative](https://github.com/data-scrape/serpapi-alternative)
- [zenrows-alternative](https://github.com/data-scrape/zenrows-alternative)

### Reddit Scrapers

- [apify-reddit-scraper](https://github.com/data-scrape/apify-reddit-scraper)
- [best-apollo-scraper-reddit](https://github.com/data-scrape/best-apollo-scraper-reddit)
- [best-reddit-scraper](https://github.com/data-scrape/best-reddit-scraper)

### Reviews & Local Scrapers

- [glassdoor-scraper](https://github.com/data-scrape/glassdoor-scraper)
- [scrape-yelp-reviews](https://github.com/data-scrape/scrape-yelp-reviews)
- [yellow-pages-scraper](https://github.com/data-scrape/yellow-pages-scraper)

### Social Media Scrapers

- [discord-scraper](https://github.com/data-scrape/discord-scraper)
- [pinterest-scraper](https://github.com/data-scrape/pinterest-scraper)
- [telegram-scraper](https://github.com/data-scrape/telegram-scraper)
- [threads-scraper](https://github.com/data-scrape/threads-scraper)
- [twitch-scraper](https://github.com/data-scrape/twitch-scraper)
- [x-scraper](https://github.com/data-scrape/x-scraper)

### TikTok Scrapers

- [apify-tiktok-scraper](https://github.com/data-scrape/apify-tiktok-scraper)
- [best-tiktok-scraper](https://github.com/data-scrape/best-tiktok-scraper)
- [tiktok-comment-scraper](https://github.com/data-scrape/tiktok-comment-scraper)
- [tiktok-comments-scraper](https://github.com/data-scrape/tiktok-comments-scraper)
- [tiktok-data-scraper-api](https://github.com/data-scrape/tiktok-data-scraper-api)
- [tiktok-profile-scraper](https://github.com/data-scrape/tiktok-profile-scraper)
- [tiktok-video-scraper](https://github.com/data-scrape/tiktok-video-scraper)

### YouTube Scrapers

- [best-youtube-scraper](https://github.com/data-scrape/best-youtube-scraper)
- [scrape-youtube-comments](https://github.com/data-scrape/scrape-youtube-comments)
- [scrape-youtube-search-results](https://github.com/data-scrape/scrape-youtube-search-results)
- [youtube-channel-scraper](https://github.com/data-scrape/youtube-channel-scraper)
- [youtube-video-scraper-api](https://github.com/data-scrape/youtube-video-scraper-api)

### Zillow Scrapers

- [apify-zillow-scraper](https://github.com/data-scrape/apify-zillow-scraper)
- [best-zillow-scraper](https://github.com/data-scrape/best-zillow-scraper)
- [easy-scrape-zillow-agents-free](https://github.com/data-scrape/easy-scrape-zillow-agents-free)
- [zillow-data-scraper](https://github.com/data-scrape/zillow-data-scraper)
- [zillow-scraper-api](https://github.com/data-scrape/zillow-scraper-api)

### eBay Scrapers

- [best-ebay-scraper](https://github.com/data-scrape/best-ebay-scraper)
- [ebay-price-scraper](https://github.com/data-scrape/ebay-price-scraper)
- [ebay-web-scraper](https://github.com/data-scrape/ebay-web-scraper)
- [scrap-gold-ebay](https://github.com/data-scrape/scrap-gold-ebay)

### eCommerce Scrapers

- [best-walmart-scraper](https://github.com/data-scrape/best-walmart-scraper)

---

Star this repo if it helps you!

Powered by [CoreClaw](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) - The All-in-One Web Scraping Platform
<!-- CROSS_LINKS_END -->

<!-- STAR_SECTION_START -->
## ⭐ Support This Project

If this tool helped you, please consider:

1. **⭐ Star this repository** — [Click here to star](https://github.com/data-scrape/instagram-email-scraper)
2. **📧 Share with your network** — Help others discover this tool
3. **🐛 Report issues** — [Open an issue](https://github.com/data-scrape/instagram-email-scraper/issues) if you find a bug
4. **📚 Contribute** — PRs are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

<div align="center">

### 👉 Ready to scrape more platforms?

[![Star History](https://img.shields.io/github/stars/data-scrape/instagram-email-scraper?style=social)](https://github.com/data-scrape/instagram-email-scraper)

**Check out all our scrapers:**

[Instagram](https://github.com/data-scrape/instagram-scraper) ·
[Google Maps](https://github.com/data-scrape/best-google-maps-scraper) ·
[Amazon](https://github.com/data-scrape/best-amazon-scraper) ·
[TikTok](https://github.com/data-scrape/best-tiktok-scraper) ·
[YouTube](https://github.com/data-scrape/best-youtube-scraper) ·
[LinkedIn](https://github.com/data-scrape/best-linkedin-scraper) ·
[eBay](https://github.com/data-scrape/best-ebay-scraper) ·
[Reddit](https://github.com/data-scrape/best-reddit-scraper) ·
[Apify Alternative](https://github.com/data-scrape/best-apify-alternative)

</div>

<!-- STAR_SECTION_END -->


<!-- CONTRIB_SECTION_START -->
## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development guidelines.

<!-- CONTRIB_SECTION_END -->

