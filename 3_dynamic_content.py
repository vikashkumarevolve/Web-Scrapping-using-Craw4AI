
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig, CacheMode

async def crawl_dynamic_content():
    # You can use wait_for to wait for a condition to be met before returning the result
    # wait_for = """() => {
    #     return Array.from(document.querySelectorAll('article.tease-card')).length > 10;
    # }"""

    # wait_for can be also just a css selector
    # wait_for = "article.tease-card:nth-child(10)"

    async with AsyncWebCrawler() as crawler:
        js_code = [
            "const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More')); loadMoreButton && loadMoreButton.click();"
        ]
        config = CrawlerRunConfig(
            cache_mode=CacheMode.ENABLED,
            js_code=js_code,
            # wait_for=wait_for,
        )
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=config,

        )
        print(result.markdown_v2.raw_markdown[:500].replace("\n", " -- "))  # Print first 500 characters

asyncio.run(crawl_dynamic_content())