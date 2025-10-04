# chatbot-gemini
# AI Assistant

 powered by Google Gemini API.

## ✨ Features

- 💬 Real-time chat interface
- 🎨 Beautiful aqua-green gradient design
- 📱 Fully responsive
- ⚡ Fast and efficient


## 📁Project Structure

```
ai-assistant/
├── api/
│   └── chat.py           # Backend API endpoint
├── public/
│   └── index.html        # Frontend interface (password: Arif)
├── requirements.txt     dependencies
├── vercel.json          # Vercel configuration (IMPORTANT!)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Important Files

### vercel.json (Must be in root folder!)
```json
{
  "version": 2,
  "builds": [
    { "src": "api/chat.py", "use": "@vercel/python" },
    { "src": "public/**/*", "use": "@vercel/static" }
  ],
  "routes": [
    { "src": "/api/chat", "dest": "api/chat.py" },
    { "src": "/(.*)", "dest": "/public/$1" }
  ]
}
```

This configuration:
- Tells Vercel to serve files from `public/` folder
- Runs Python files in `api/` folder as serverless functions
- Routes `/api/chat` to your Python backend
- Routes everything else to your frontend

##  Deployment on Vercel

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2.  Commit and push

### Step 2: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "Import Project"
4. Select your repository
5. **IMPORTANT**: Add Environment Variable:
   - Key: `GEMINI_API_KEY`
   - Value: `api key here`
6. Click "Deploy"

### Step 3: Done! 

live : `https://chatbot-gemini-ryag.vercel.app/`

## Environment Variables

You need to set this in Vercel Dashboard (NOT in code):

```
GEMINI_API_KEY=your_api_key_here
```

**Never commit `.env` file to GitHub!**

## Local Development

### Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install google-genai
```

### Test Locally

```bash
# Set environment variable
# Windows:
set GEMINI_API_KEY=your_api_key_here
# Mac/Linux:
export GEMINI_API_KEY=your_api_key_here

```

## Files to Upload to GitHub

✅ Upload these:
- `api/chat.py`
- `public/index.html`
- `requirements.txt`
- `vercel.json`
- `.gitignore`
- `README.md`

## Color Theme

Current theme: **Aqua Green**
- Primary: `#06b6d4` (Cyan)
- Secondary: `#10b981` (Emerald)

## Troubleshooting

### Issue: "Module not found"
**Solution**: Make sure `requirements.txt` exists with `google-genai`

### Issue: "API key not configured"
**Solution**: Add `GEMINI_API_KEY` in Vercel environment variables

### Issue: "404 on /api/chat"
**Solution**: Ensure `vercel.json` is in root folder

## 👨‍💻 Made by Arif

Personal AI Assistant - Version 1.0

---

**Note**: Keep your API key secure! Never share it publicly or commit it to GitHub.