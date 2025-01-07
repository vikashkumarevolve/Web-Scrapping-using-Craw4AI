import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig, CacheMode


async def media_handling():
    async with AsyncWebCrawler() as crawler:
        config = CrawlerRunConfig(
            cache_mode=CacheMode.ENABLED,
            exclude_external_images=False,
            # screenshot=True # Set this to True if you want to take a screenshot
        )
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=config,
        )
        for img in result.media['images'][:5]:
            print(f"Image URL: {img['src']}, Alt: {img['alt']}, Score: {img['score']}")

asyncio.run(media_handling())