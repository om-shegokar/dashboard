# 🤖 Coding Model Evaluation Dashboard

A comprehensive Streamlit dashboard for evaluating coding models across multiple benchmarks including ARCHIT EVAL, HumanEval, SWE Benchmark, RustEvo, Aider-Polyglot, and Haskell LLM.

## 🚀 Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - FREE)

**Streamlit Community Cloud** is the easiest and FREE way to deploy your Streamlit app.

#### Prerequisites
- GitHub account
- Your code pushed to a GitHub repository

#### Step-by-Step Deployment:

1. **Push your code to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Go to Streamlit Community Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy your app**:
   - Click "New app"
   - Select your repository: `om-shegokar/dashboard`
   - Branch: `main` (or your default branch)
   - Main file path: `dashboard.py`
   - Click "Deploy!"

4. **Your app will be live** at:
   - `https://[your-app-name].streamlit.app`
   - Deployment takes 2-3 minutes

#### Features:
- ✅ Completely FREE
- ✅ Automatic updates when you push to GitHub
- ✅ Custom subdomain
- ✅ HTTPS enabled
- ✅ No configuration needed

---

### Option 2: Render

**Render** offers free hosting with good performance.

#### Deployment Steps:

1. **Create a Render account** at [render.com](https://render.com)

2. **Connect your GitHub repository**

3. **Create a new Web Service**:
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run dashboard.py --server.port=$PORT --server.address=0.0.0.0`

4. **Deploy** - Your app will be available at `https://[your-app-name].onrender.com`

---

### Option 3: Railway

**Railway** provides simple deployment with a generous free tier.

#### Deployment Steps:

1. **Create account** at [railway.app](https://railway.app)

2. **New Project** → **Deploy from GitHub repo**

3. **Select your repository**

4. **Add start command** in Railway settings:
   ```
   streamlit run dashboard.py --server.port=$PORT --server.address=0.0.0.0
   ```

5. **Deploy** - Railway will provide a public URL

---

### Option 4: Heroku

**Heroku** requires additional configuration files but is reliable.

#### Additional Files Needed:

**Create `setup.sh`:**
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@example.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

**Create `Procfile`:**
```
web: sh setup.sh && streamlit run dashboard.py
```

#### Deployment Steps:
1. Install Heroku CLI: `brew install heroku/brew/heroku`
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

---

## 🏃 Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard.py
```

The dashboard will open at `http://localhost:8501`

---

## 📊 Features

- **Multiple Benchmarks**: ARCHIT EVAL, HumanEval (Rust), SWE Benchmark, RustEvo, Aider-Polyglot, Haskell LLM
- **Interactive Visualizations**: Plotly charts, graphs, heatmaps, and radar charts
- **Model Comparison**: Compare performance across different models and metrics
- **Comprehensive Metrics**: Pass@k rates, API accuracy, error rates, success counts

---

## 🛠️ Tech Stack

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **Python 3.8+**: Programming language

---

## 📝 License

This project is for evaluation and analysis purposes.

---

## 🤝 Contributing

Feel free to submit issues or pull requests for improvements!
