import asyncio
from pyppeteer import launch

# Provide the YouTube video URL
video_url = "https://www.youtube.com/watch?v=592mNGkpYig"

async def download_video():
    # Launch a headless browser
    browser = await launch()
    page = await browser.newPage()

    # Go to the YouTube video page
    await page.goto(video_url)

    # Wait for the video element to be loaded
    await page.waitForSelector('video')

    # Get the video source URL
    video_src = await page.evaluate('() => document.querySelector("video").src')

    # Download the video using the video source URL
    response = await page.goto(video_src)

    # Save the video to a file
    file_path = 'Software/downloads/video.mp4'
    with open(file_path, 'wb') as file:
        file.write(await response.buffer())

    # Close the browser
    await browser.close()

    print("Video downloaded successfully!")

# Run the download function
asyncio.get_event_loop().run_until_complete(download_video())
