# Instagram Email Scraper

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/xiaozhucchongya-byte/instagram-email-scraper?style=social)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper)
[![GitHub forks](https://img.shields.io/github/forks/xiaozhucchongya-byte/instagram-email-scraper?style=social)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/fork)
[![GitHub issues](https://img.shields.io/github/issues/xiaozhucchongya-byte/instagram-email-scraper)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/issues)
[![GitHub license](https://img.shields.io/github/license/xiaozhucchongya-byte/instagram-email-scraper)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/blob/main/LICENSE)
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


## 📘 Table of Contents

- [🔥 Features](#-features)
- [🎯 Use Cases](#-use-cases)
- [📊 Data Fields Extracted](#-data-fields-extracted)
- [💻 Configuration](#-configuration)
- [🔁 Output Example](#-output-example)
- [📝 License](#-license)
- [Related Repositories](#related-repositories)
- [Support This Project](#-support-this-project)

---


<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/xiaozhucchongya-byte/instagram-email-scraper?style=social)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper)
[![GitHub forks](https://img.shields.io/github/forks/xiaozhucchongya-byte/instagram-email-scraper?style=social)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/fork)
[![GitHub issues](https://img.shields.io/github/issues/xiaozhucchongya-byte/instagram-email-scraper)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/issues)
[![GitHub license](https://img.shields.io/github/license/xiaozhucchongya-byte/instagram-email-scraper)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)

</div>


> Instagram email scraper - extract emails from Instagram bios and profiles


<!-- SEO keywords: instagram email scraper, Instagram Email Scraper, instagram email scraper python, instagram email scraper github, best instagram email scraper -->


<div align="center">

[![CoreClaw](https://img.shields.io/badge/CoreClaw-Data_Scraping_Platform-7B2FF7?style=for-the-badge&labelColor=5B21B6)](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

**The All-in-One Web Scraping & Data Platform** — Scrape Google Maps, Instagram, Amazon, LinkedIn, TikTok, YouTube, and 50+ platforms via ready-to-use REST APIs.

✅ No browser automation · ✅ No proxy management · ✅ Free credits for new users

⬇️ [Get Started with CoreClaw Free](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7)

</div>

---


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
pip install git+https://github.com/xiaozhucchongya-byte/instagram-email-scraper.git
```

### From source

```bash
git clone https://github.com/xiaozhucchongya-byte/instagram-email-scraper.git
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
## 🔗 Related Repositories

Explore our complete web scraping toolkit:

### Instagram Scrapers

- [Instagram Scraper](https://github.com/xiaozhucchongya-byte/instagram-scraper) - Python Instagram scraper - extract posts, profiles, followers, hashtags
- [Instagram Account Scraper](https://github.com/xiaozhucchongya-byte/instagram-account-scraper) - Instagram account scraper - profiles, posts, reels, stories, emails
- [Instagram Follower Scraper](https://github.com/xiaozhucchongya-byte/instagram-follower-scraper) - Instagram follower scraper - extract follower and following lists
- [Instagram Profile Scraper](https://github.com/xiaozhucchongya-byte/instagram-profile-scraper) - Instagram profile scraper - extract profile data and analytics
- [Scrape Instagram Followers](https://github.com/xiaozhucchongya-byte/scrape-instagram-followers) - Scrape Instagram followers and following lists in bulk
- [Best Instagram Scraper](https://github.com/xiaozhucchongya-byte/best-instagram-scraper) - Best Instagram scraper 2025 - extract posts, reels, stories, profiles
- [Apify Instagram Scraper](https://github.com/xiaozhucchongya-byte/apify-instagram-scraper) - Apify Instagram scraper alternative - free Python Instagram scraper
- [Scrape Instagram Photos](https://github.com/xiaozhucchongya-byte/scrape-instagram-photos) - Scrape Instagram photos - download photos from any profile in bulk
- [Instagram Comment Scraper](https://github.com/xiaozhucchongya-byte/instagram-comment-scraper) - Instagram comment scraper - extract comments from posts and reels

### Google Maps Scrapers

- [Google Maps Data Scraper](https://github.com/xiaozhucchongya-byte/google-maps-data-scraper) - Google Maps data scraper - extract business data, reviews, ratings
- [Best Google Maps Scraper](https://github.com/xiaozhucchongya-byte/best-google-maps-scraper) - Best Google Maps scraper 2025 - business data extraction tool
- [Scrape Google Maps](https://github.com/xiaozhucchongya-byte/scrape-google-maps) - Scrape Google Maps - extract places, reviews, and business data
- [Google Map Scraper Api ](https://github.com/xiaozhucchongya-byte/google-map-scraper-api-) - Google Maps scraper API - REST API for business data extraction
- [Outscraper Google Maps Scraper](https://github.com/xiaozhucchongya-byte/outscraper-google-maps-scraper) - Outscraper Google Maps scraper alternative - free Python tool
- [Apify Google Maps Scraper](https://github.com/xiaozhucchongya-byte/apify-google-maps-scraper) - Apify Google Maps scraper alternative - free Python scraper

### Amazon Scrapers

- [Best Amazon Scraper](https://github.com/xiaozhucchongya-byte/best-amazon-scraper) - Best Amazon scraper 2025 - extract product data, reviews, prices
- [Amazon Review Scraper](https://github.com/xiaozhucchongya-byte/amazon-review-scraper) - Amazon review scraper - extract product reviews and ratings in bulk
- [Amazon Product Scraper](https://github.com/xiaozhucchongya-byte/amazon-product-scraper) - Amazon product scraper - extract product details, images, and specs
- [Amazon Asin Scraper](https://github.com/xiaozhucchongya-byte/amazon-asin-scraper) - Amazon ASIN scraper - lookup ASIN data and product information
- [Amazon Price Scraper](https://github.com/xiaozhucchongya-byte/amazon-price-scraper) - Amazon price scraper - track prices and extract pricing history
- [Amazon Scraper Api](https://github.com/xiaozhucchongya-byte/amazon-scraper-api) - Amazon scraper API - REST API for Amazon data extraction

### E-commerce Scrapers

- [Best Ebay Scraper](https://github.com/xiaozhucchongya-byte/best-ebay-scraper) - Best eBay scraper 2025 - extract product listings and seller data
- [Best Walmart Scraper](https://github.com/xiaozhucchongya-byte/best-walmart-scraper) - Best Walmart scraper 2025 - extract product data and reviews
- [Best Zillow Scraper](https://github.com/xiaozhucchongya-byte/best-zillow-scraper) - Best Zillow scraper 2025 - extract property listings and agent data

### Social Media Scrapers

- [Best Tiktok Scraper](https://github.com/xiaozhucchongya-byte/best-tiktok-scraper) - Best TikTok scraper 2025 - extract videos, profiles, and hashtags
- [Best Youtube Scraper](https://github.com/xiaozhucchongya-byte/best-youtube-scraper) - Best YouTube scraper 2025 - extract videos, comments, and channel data
- [Best Facebook Scraper](https://github.com/xiaozhucchongya-byte/best-facebook-scraper) - Best Facebook scraper 2025 - extract pages, posts, and reviews
- [Best Linkedin Scraper](https://github.com/xiaozhucchongya-byte/best-linkedin-scraper) - Best LinkedIn scraper 2025 - extract profiles, company data, jobs
- [Best Reddit Scraper](https://github.com/xiaozhucchongya-byte/best-reddit-scraper) - Best Reddit scraper 2025 - extract posts, comments, and user data

### Search & Job Scrapers

- [Best Google Search Scraper](https://github.com/xiaozhucchongya-byte/best-google-search-scraper) - Best Google Search scraper 2025 - extract search results in bulk
- [Best Indeed Scraper](https://github.com/xiaozhucchongya-byte/best-indeed-scraper) - Best Indeed scraper 2025 - extract job listings and company data

### Scraping Platforms & Lists

- [Best Apify Alternative](https://github.com/xiaozhucchongya-byte/best-apify-alternative) - Best Apify alternative 2025 - free web scraping platform
- [Awesome Apify Alternatives](https://github.com/xiaozhucchongya-byte/awesome-apify-alternatives) - Awesome Apify alternatives - curated list of web scraping tools
- [Awesome Lead Generation](https://github.com/xiaozhucchongya-byte/awesome-lead-generation) - Awesome lead generation tools - curated list of scrapers and extractors

---

<!-- CROSS_LINKS_END -->


<!-- STAR_SECTION_START -->
## ⭐ Support This Project

If this tool helped you, please consider:

1. **⭐ Star this repository** — [Click here to star](https://github.com/xiaozhucchongya-byte/instagram-email-scraper)
2. **📧 Share with your network** — Help others discover this tool
3. **🐛 Report issues** — [Open an issue](https://github.com/xiaozhucchongya-byte/instagram-email-scraper/issues) if you find a bug
4. **📚 Contribute** — PRs are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

<div align="center">

### 👉 Ready to scrape more platforms?

[![Star History](https://img.shields.io/github/stars/xiaozhucchongya-byte/instagram-email-scraper?style=social)](https://github.com/xiaozhucchongya-byte/instagram-email-scraper)

**Check out all our scrapers:**

[Instagram](https://github.com/xiaozhucchongya-byte/instagram-scraper) ·
[Google Maps](https://github.com/xiaozhucchongya-byte/best-google-maps-scraper) ·
[Amazon](https://github.com/xiaozhucchongya-byte/best-amazon-scraper) ·
[TikTok](https://github.com/xiaozhucchongya-byte/best-tiktok-scraper) ·
[YouTube](https://github.com/xiaozhucchongya-byte/best-youtube-scraper) ·
[LinkedIn](https://github.com/xiaozhucchongya-byte/best-linkedin-scraper) ·
[eBay](https://github.com/xiaozhucchongya-byte/best-ebay-scraper) ·
[Reddit](https://github.com/xiaozhucchongya-byte/best-reddit-scraper) ·
[Apify Alternative](https://github.com/xiaozhucchongya-byte/best-apify-alternative)

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

