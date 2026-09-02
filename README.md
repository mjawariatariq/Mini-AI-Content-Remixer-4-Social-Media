# Universal Social Media Caption Remixer

An AI-powered **social media caption remixing tool** that extracts captions from social media posts and generates multiple rewritten versions while preserving the original meaning.

The application supports platforms such as **Facebook, Instagram, X/Twitter, and Threads**, with a simple **Streamlit interface** powered by **Apify** for content extraction and **Google Gemini 2.5 Flash** for AI-powered caption generation.

## Features

- **Multi-Platform Support**
  - Facebook — automatic caption scraping
  - Instagram — manual caption input
  - X / Twitter — automatic caption scraping
  - Threads — automatic caption scraping

- **AI Caption Remixing**
  - Generate 3, 5, 6, or 10 caption variations
  - Preserve the original meaning
  - Change wording and sentence structure
  - Create more unique and engaging captions

- **AI-Powered**
  - Google Gemini 2.5 Flash for caption generation
  - Apify actors for social media content extraction

- **Streamlit Interface**
  - Simple and user-friendly UI
  - Easy URL-based workflow
  - Displays original and remixed captions together

- **Multilingual Potential**
  - English
  - Urdu
  - Roman Urdu
  - Hindi
  - Additional languages can be added

## How It Works

```text
Social Media Post
       │
       ▼
   Post URL
       │
       ▼
Platform Detection
       │
 ┌─────┼──────────────┐
 ▼     ▼              ▼
Facebook  X/Twitter  Threads
 │        │              │
 └────────┼──────────────┘
          ▼
    Apify Scraping
          │
          ▼
   Original Caption
          │
          ▼
    Google Gemini
          │
          ▼
  Multiple Remixed
     Captions
          │
          ▼
     Streamlit UI
```

For Instagram, the caption is currently entered manually because automatic caption extraction is not implemented.

## Supported Platforms

| Platform | Caption Extraction |
|---|---|
| Facebook | Automatic |
| Instagram | Manual |
| X / Twitter | Automatic |
| Threads | Automatic |

## Example

### Original Caption

```text
Building the future with AI, one idea at a time.
```

### Remixed Captions

```text
1. Creating tomorrow with AI, one idea after another.

2. Shaping the future through AI and innovative ideas.

3. One idea, one innovation, one step closer to an AI-powered future.

4. Turning bold ideas into the future with AI.
```

The generated versions aim to maintain the **core meaning** while providing different wording and sentence structures.

## Technology Stack

| Category | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| Web Scraping | Apify |
| Programming Language | Python |
| Configuration | Python dotenv |
| Social Platforms | Facebook, Instagram, X/Twitter, Threads |

## Project Structure

```text
social-caption-remixer/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The exact structure may vary depending on the implementation and additional modules added to the project.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mjawariatariq/Mini-AI-Content-Remixer-4-Social-Media.git
cd Mini-AI-Content-Remixer-4-Social-Media
```

### 2. Create a Virtual Environment

Creating a virtual environment is recommended.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
APIFY_API_KEY=your_apify_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

Keep API keys private and never commit the `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

### 5. Run the Application

```bash
streamlit run main.py
```

## How to Use

1. Open the Streamlit application.
2. Select the social media platform.
3. Paste the post URL for supported platforms.
4. For Instagram, manually paste the caption.
5. Select the number of remixed captions.
6. Click **Generate Remixed Captions**.
7. View the original caption and generated variations.

## Caption Generation

The application uses **Google Gemini 2.5 Flash** to rewrite captions while maintaining their original intent.

The AI generation process focuses on:

- Meaning preservation
- Different wording
- Sentence restructuring
- Readability
- Engagement
- Natural language

## Apify Integration

Apify is used to retrieve publicly available social media content for supported platforms.

The workflow is:

```text
Post URL
   ↓
Apify Actor
   ↓
Scraped Post Data
   ↓
Caption Extraction
   ↓
Gemini Caption Remixing
```

The specific Apify actor can vary depending on the platform and implementation.

## Instagram Limitation

Instagram caption extraction is currently handled through **manual input**.

Users need to:

1. Open the Instagram post.
2. Copy the caption.
3. Paste it into the application.
4. Generate remixed versions.

This avoids relying on unsupported or restricted Instagram scraping methods.

## Future Improvements

- **Multilingual Caption Generation**
- **Tone Selection**
  - Professional
  - Casual
  - Funny
  - Motivational
  - Inspirational
  - Viral
- **Automatic Hashtag Generation**
- **Emoji Suggestions**
- **Platform-Specific Caption Optimization**
- **Instagram Caption Extraction**
- **Image + Caption Analysis**
- **AI-Powered Image Understanding**
- **Caption Length Control**
- **Download Results as CSV**
- **Download Results as TXT**
- **Copy-to-Clipboard Support**
- **Batch Caption Remixing**

## Planned Advanced Workflow

```text
Social Media Post
       │
       ├── Text
       │
       └── Image
             │
             ▼
        AI Analysis
             │
       ┌─────┴─────┐
       ▼           ▼
 Caption Text   Image Context
       │           │
       └─────┬─────┘
             ▼
       Gemini AI
             │
             ▼
   Platform-Optimized
      Captions
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
    Casual Professional Viral
```

## Security

Never hardcode API keys in Python source files.

Use environment variables:

```env
APIFY_API_KEY=your_key
GEMINI_API_KEY=your_key
```

and keep `.env` excluded from version control.

## License

This project is open-source and available under the **MIT License**.

## Author

**Jawaria Tariq**

AI Engineer focused on **LLM Applications, AI Agents, RAG Systems, and AI Automation**.

GitHub: `mjawariatariq`

LinkedIn: `m-jawaria-tariq`
