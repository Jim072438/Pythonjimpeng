import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        result = await crawler.arun(url='https://www.sap.com/taiwan/products/technology-platform/what-is-blockchain.html')
        print(type(result))
        print("=" * 20)        

        #列印取出的結果
        
        print(result.markdown.raw_markdown)  

if __name__ == "__main__":
    asyncio.run(main())

