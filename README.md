
# YouTube Transcript Translator

This Streamlit app aims to provide educational assistance by allowing users to generate transcripts from YouTube videos and translate them into different languages. The tool is designed to help language learners, students, and educators access and understand spoken content more effectively.

## Purpose

The primary goal of this project is to facilitate language learning and educational activities by providing a convenient tool for extracting and translating transcripts from YouTube videos. By converting spoken content into written form and offering translation capabilities, the app aims to:

- Assist language learners in improving their listening and comprehension skills.
- Support students in accessing educational content in their native language or a language they are studying.
- Aid educators in creating subtitles or transcripts for instructional videos.
- Promote accessibility by making video content more comprehensible for individuals with hearing impairments or language barriers.

## Issues Addressed

### GitHub Push Protection

When attempting to push changes to GitHub, you may encounter an error related to push protection. This error occurs when secrets are detected in the repository, which violates GitHub's security rules.

### OpenAI API Key

Another potential issue is the inclusion of sensitive information, such as the OpenAI API key, in the code. Including API keys in a public repository can pose security risks and violate best practices.

## Resolving Issues

To resolve these issues, follow these steps:

### Push Protection Error

1. **Review Repository Rules**: Visit the [repository settings page](https://github.com/OSAMAGHAFFARTKOJL/VideoTranscribHackathon/settings/security_analysis) to review all repository rules.
2. **Resolve Detected Secrets**: Resolve any detected secrets by removing them from the commits or allowing them via the provided URL.
3. **Enable Secret Scanning**: If Secret Scanning is not enabled for the repository, consider enabling it to manage detected secrets more effectively.

### OpenAI API Key

1. **Remove API Key from Code**: Ensure that sensitive information like the OpenAI API key is not included in the code before pushing to GitHub.
2. **Environment Variables**: Use environment variables or secure storage solutions to manage API keys and other secrets securely.

## Usage

1. Enter a valid YouTube video link in the input field.
2. Enter the target language for translation.
3. Click the "Generate Transcript" button to generate the transcript and translate it.
4. The original and translated summaries will be displayed, and you can download the translated text using the "Download Text" button.

## Requirements

- Python 3.x
- Streamlit
- pytube
- OpenAI API (for translation)
- ffmpeg (for audio conversion)

## Setup

1. Clone the repository:

```
git clone https://github.com/OSAMAGHAFFARTKOJL/VideoTranscribHackathon.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the Streamlit app:

```
streamlit run app.py
```

# Founding Team:


Our team comprises passionate developers and AI enthusiasts dedicated to reimagining the future of education. With diverse backgrounds in academia and technology, we bring a unique blend of expertise to Ai.

**Collaborators**:
https://github.com/shaistaDev7
https://github.com/shahzcoder
https://github.com/Fayaz-khani
https://github.com/hamna321
