import asyncio

from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig, CacheMode,BrowserConfig



async def custom_hook_workflow(verbose=True):
    async with AsyncWebCrawler(config=BrowserConfig( verbose=verbose)) as crawler:
        # Set a 'before_goto' hook to run custom code just before navigation
        crawler.crawler_strategy.set_hook("before_goto", lambda page, context: print("[Hook] Preparing to navigate..."))

        # Perform the crawl operation
        result = await crawler.arun(
            url="https://crawl4ai.com",
            config=CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        )
        print(result.markdown_v2.raw_markdown[:500].replace("\n", " -- "))

asyncio.run(custom_hook_workflow())