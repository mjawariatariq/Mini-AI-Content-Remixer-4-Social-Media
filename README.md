# 🌟 Universal Social Media Caption Remixer

This project allows you to **remix captions from social media posts** (Facebook, Instagram, X/Twitter, Threads) using AI.  
It generates multiple versions of a caption while keeping the same meaning but changing the wording.  

---

## 🚀 Features

- Support for multiple platforms:
  - Facebook (automatic scraping)
  - Instagram (manual caption input)
  - X / Twitter (automatic scraping)
  - Threads (automatic scraping)
- Generate **3, 5, 6, or 10 versions** of a caption
- Multilingual support (English, Urdu, Roman Urdu, Hindi, etc. can be added)
- Tone and style can be customized (future upgrade)
- Streamlit interface for easy use
- Powered by **Apify actors** and **Google Gemini 2.5 Flash** for AI remixing

---

## ⚙️ Setup Instructions

1. **Clone this repository**

```bash
git clone https://github.com/your-username/social-caption-remixer.git
cd social-caption-remixer

Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

Install dependencies
pip install -r requirements.txt

Create a .env file in the root directory with your API keys:
APIFY_API_KEY=your_apify_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

⚠️ Note: For social media platforms other than Facebook, you must provide official API keys in the .env file. Otherwise, caption scraping might fail.

Run the Streamlit app
streamlit run main.py

📝 How to Use
Paste the post URL from Facebook, X/Twitter, or Threads.
For Instagram, copy and paste the caption manually (automatic scraping is not supported due to API restrictions).
Choose the number of remixed versions you want.
Click Generate Remixed Captions.
The app will display the original caption and the remixed versions.

📌 Notes
Facebook, X/Twitter, and Threads posts are automatically scraped using Apify actors.
Instagram scraping is not supported; captions must be manually pasted.
The app uses Google Gemini 2.5 Flash to generate remixed captions.
The generated captions maintain the same meaning but use different wording to make them unique and catchy.

🛠️ Future Improvements
Add multilingual UI for all supported languages
Tone/style selection for captions (Casual, Professional, Funny, Motivational, Viral)
Automatic hashtag generation
Image + text detection for posts with images
Download remixed captions as CSV / TXT

📄 License
This project is open-source under the MIT License.
