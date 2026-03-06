import os
from dotenv import load_dotenv
import streamlit as st
from apify_client import ApifyClient
import google.generativeai as genai


load_dotenv()
APIFY_API_KEY = os.getenv("APIFY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

apify_client = ApifyClient(APIFY_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


platform_actors = {
    "facebook": "apify/facebook-posts-scraper",
    "instagram": "apify/instagram-post-scraper",
    "x": "pratikdani/twitter-posts-scraper",
    "threads": "logical_scrapers/threads-post-scraper"
}

def get_actor_id(url):
    url = url.lower()
    if "facebook.com" in url:
        return platform_actors["facebook"]
    elif "instagram.com" in url:
        return platform_actors["instagram"]
    elif "twitter.com" in url or "x.com" in url:
        return platform_actors["x"]
    elif "threads.net" in url:
        return platform_actors["threads"]
    else:
        return None


def scrape_caption(url):
    actor_id = get_actor_id(url)
    if not actor_id:
        return None

    run_input = {"startUrls": [{"url": url}], "resultsLimit": 1}
    run = apify_client.actor(actor_id).call(run_input=run_input)
    dataset_items = apify_client.dataset(run["defaultDatasetId"]).list_items().items

    if not dataset_items:
        return None

    caption = dataset_items[0].get("text")
    return caption

def generate_versions(caption, versions):
    prompt = f"""
Rewrite the following social media caption:

Rules:
- Keep same meaning
- Change wording
- Generate {versions} versions
- Short, natural, catchy
- Return as numbered list

Caption:
{caption}
"""
    response = model.generate_content(prompt)
    return response.text


st.title("🌟 Universal Social Media Caption Remixer")
st.markdown("""
Paste your post URL from **Facebook, Instagram, X/Twitter, Threads**.
Choose how many versions you want.
""")

url = st.text_input("Post URL")
versions = st.selectbox("Number of versions", [3, 5, 6, 10], index=0)


if "instagram.com" in url.lower():
    st.warning("Instagram scraping not supported. Please paste the caption manually.")
    caption = st.text_area("Paste Instagram caption here")
else:
    caption = scrape_caption(url)

if st.button("Generate Remixed Captions"):
    if not url:
        st.warning("Please enter a valid post URL")
    else:
        with st.spinner("Scraping caption..."):
            caption = scrape_caption(url)

        if not caption:
            st.error("Could not extract caption from this URL or unsupported platform")
        else:
            st.success("Original Caption Extracted:")
            st.write(caption)

            st.info("Generating remixed versions...")
            remixed = generate_versions(caption, versions)
            st.success(f"{versions} Remixed Versions:")
            st.text(remixed)
