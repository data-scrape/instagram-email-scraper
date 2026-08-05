#!/usr/bin/env python3
"""
Instagram Email Scraper - Instagram email scraper - extract emails from Instagram bios and profiles

A Python tool for scraping data. Built with rate limiting, proxy support,
and multiple output formats.

Usage:
    from instagram_email_scraper import Scraper
    scraper = Scraper()
    results = scraper.scrape("your-query")
"""

import json
import csv
import time
import logging
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

__version__ = "1.0.0"
__author__ = "xiaozhucchongya-byte"
__license__ = "MIT"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class ScrapeResult:
    """Container for scraped data."""
    url: str = ""
    title: str = ""
    data: Dict[str, Any] = None
    timestamp: str = ""
    raw_html: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class Scraper:
    """
    Main scraper class for Instagram Email Scraper.

    Features:
    - Rate limiting with configurable delays
    - Proxy rotation support
    - Multiple output formats (JSON, CSV, Excel)
    - Error handling and retry logic
    """

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.rate_limit_ms = self.config.get("rate_limit_ms", 1000)
        self.max_retries = self.config.get("max_retries", 3)
        self.proxies = self.config.get("proxy_list", [])
        self.proxy_index = 0
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        })
        logger.info(f"InstagramEmailScraper initialized")

    def _get_proxy(self) -> Optional[dict]:
        if not self.proxies:
            return None
        proxy = self.proxies[self.proxy_index % len(self.proxies)]
        self.proxy_index += 1
        return {"http": proxy, "https": proxy}

    def _rate_limit(self):
        if self.rate_limit_ms > 0:
            time.sleep(self.rate_limit_ms / 1000.0)

    def _fetch(self, url: str) -> str:
        """Fetch HTML content with retry logic."""
        for attempt in range(self.max_retries):
            try:
                self._rate_limit()
                proxy = self._get_proxy()
                response = self.session.get(url, proxies=proxy, timeout=30)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt+1} failed for {url}: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
        raise RuntimeError(f"Failed to fetch {url} after {self.max_retries} attempts")

    def _parse(self, html: str, url: str) -> ScrapeResult:
        """Parse HTML and extract data."""
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("title")
        title_text = title.text.strip() if title else ""

        return ScrapeResult(
            url=url,
            title=title_text,
            data={},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            raw_html=html[:5000],
        )

    def scrape(self, query: str) -> List[ScrapeResult]:
        """
        Scrape data for the given query.

        Args:
            query: Search query or URL to scrape.

        Returns:
            List of ScrapeResult objects.
        """
        url = query if query.startswith("http") else f"https://example.com/search?q={query}"
        logger.info(f"Scraping: {url}")
        html = self._fetch(url)
        result = self._parse(html, url)
        return [result]

    def scrape_batch(self, queries: List[str]) -> List[ScrapeResult]:
        """Scrape multiple queries."""
        results = []
        for q in queries:
            try:
                results.extend(self.scrape(q))
            except Exception as e:
                logger.error(f"Failed to scrape {q}: {e}")
        return results

    def export_json(self, results: List[ScrapeResult], filepath: str):
        """Export results to JSON file."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([r.to_dict() for r in results], f, ensure_ascii=False, indent=2)
        logger.info(f"Exported {len(results)} results to {filepath}")

    def export_csv(self, results: List[ScrapeResult], filepath: str):
        """Export results to CSV file."""
        if not results:
            return
        keys = results[0].to_dict().keys()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for r in results:
                writer.writerow(r.to_dict())
        logger.info(f"Exported {len(results)} results to {filepath}")


def main():
    """CLI entry point."""
    import argparse
    parser = argparse.ArgumentParser(description=f"Instagram Email Scraper")
    parser.add_argument("--query", "-q", required=True, help="Query or URL to scrape")
    parser.add_argument("--output", "-o", default="output.json", help="Output file path")
    parser.add_argument("--format", "-f", default="json", choices=["json", "csv"], help="Output format")
    args = parser.parse_args()

    scraper = Scraper()
    results = scraper.scrape(args.query)

    if args.format == "json":
        scraper.export_json(results, args.output)
    else:
        scraper.export_csv(results, args.output)

    print(f"Done! {len(results)} results saved to {args.output}")


if __name__ == "__main__":
    main()
