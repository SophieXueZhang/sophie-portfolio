import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏Streamlit默认元素和侧边栏
st.markdown("""
<style>
    /* 隐藏主菜单 */
    #MainMenu {visibility: hidden;}

    /* 隐藏页脚 */
    footer {visibility: hidden;}

    /* 隐藏顶部header */
    header {visibility: hidden;}

    /* 隐藏侧边栏 */
    .css-1d391kg {display: none;}
    section[data-testid="stSidebar"] {display: none;}

    /* 移除内边距 */
    .main > div {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }

    /* 移除容器边距 */
    .stApp {
        margin: 0;
        padding: 0;
    }

    /* 让iframe占满整个屏幕 */
    iframe {
        border: none;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
    }

    /* 隐藏Streamlit的所有默认组件 */
    .block-container {
        padding: 0;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# HTML内容
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 50%, #dee2e6 100%);
            color: #2c3e50;
            overflow-x: hidden;
            font-weight: 300;
            letter-spacing: 0.02em;
        }

        #particles-js {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }

        .container {
            position: relative;
            z-index: 1;
        }

        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(248, 249, 250, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(206, 212, 218, 0.3);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .navbar.scrolled {
            background: rgba(248, 249, 250, 0.95);
            backdrop-filter: blur(25px);
            box-shadow: 0 1px 20px rgba(0, 0, 0, 0.05);
        }

        .nav-brand {
            font-size: 1.5rem;
            font-weight: 500;
            color: #2c3e50;
            letter-spacing: 0.05em;
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-menu a {
            color: #495057;
            text-decoration: none;
            transition: color 0.3s ease;
            position: relative;
            font-weight: 400;
            font-size: 0.95rem;
        }

        .nav-menu a:hover {
            color: #2c3e50;
        }

        .nav-menu a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 1px;
            background: #2c3e50;
            transition: width 0.3s ease;
        }

        .nav-menu a:hover::after {
            width: 100%;
        }

        .hero-section {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 0 2rem;
        }

        .hero-content {
            max-width: 800px;
            animation: fadeInUp 1s ease-out;
        }

        .hero-title {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            line-height: 1.2;
            font-weight: 300;
            color: #2c3e50;
        }

        .highlight {
            color: #495057;
            font-weight: 400;
            border-bottom: 2px solid #dee2e6;
            padding-bottom: 2px;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.8;
            color: #6c757d;
            font-weight: 300;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            cursor: pointer;
            display: inline-block;
        }

        .btn-primary {
            background: #2c3e50;
            color: #ffffff;
            border: 1px solid #2c3e50;
        }

        .btn-primary:hover {
            background: #34495e;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(44, 62, 80, 0.2);
        }

        .btn-secondary {
            background: transparent;
            color: #2c3e50;
            border: 1px solid #2c3e50;
        }

        .btn-secondary:hover {
            background: #2c3e50;
            color: #ffffff;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(44, 62, 80, 0.2);
        }

        .section {
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-content {
            text-align: center;
        }

        .section h2 {
            font-size: 2.2rem;
            margin-bottom: 2rem;
            position: relative;
            display: inline-block;
            font-weight: 300;
            color: #2c3e50;
        }

        .section h2::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 40px;
            height: 1px;
            background: #dee2e6;
        }

        .section p {
            font-size: 1.1rem;
            line-height: 1.7;
            opacity: 0.85;
            max-width: 600px;
            margin: 0 auto;
            color: #495057;
            font-weight: 300;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .project-card {
            background: rgba(248, 249, 250, 0.8);
            backdrop-filter: blur(20px);
            border-radius: 12px;
            padding: 2rem;
            border: 1px solid rgba(206, 212, 218, 0.3);
            transition: all 0.3s ease;
        }

        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
            background: rgba(255, 255, 255, 0.9);
        }

        .project-card h3 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            color: #2c3e50;
            font-weight: 400;
        }

        .project-card h3 a {
            color: inherit;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .project-card h3 a:hover {
            color: #495057;
            text-decoration: underline;
        }

        .skills {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }

        .skill-item {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 25px;
            padding: 0.7rem 1.5rem;
            font-weight: bold;
            transition: all 0.3s ease;
            color: #ffd700;
        }

        .skill-item:hover {
            background: rgba(255, 215, 0, 0.2);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(255, 215, 0, 0.2);
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 1rem;
        }

        .skill-category {
            background: rgba(248, 249, 250, 0.7);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(206, 212, 218, 0.3);
            border-radius: 10px;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }

        .skill-category:hover {
            background: rgba(255, 255, 255, 0.85);
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.06);
        }

        .skill-category h4 {
            color: #2c3e50;
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
            font-weight: 400;
        }

        .skill-category p {
            color: #495057;
            opacity: 0.85;
            font-size: 0.9rem;
            font-weight: 300;
        }

        .about-box {
            background: transparent;
            backdrop-filter: none;
            border: none;
            border-radius: 0;
            padding: 2rem;
            margin: 2rem auto;
            max-width: 700px;
            text-align: left;
            box-shadow: none;
            transition: none;
        }

        .about-box:hover {
            box-shadow: none;
            transform: none;
        }

        .about-box p {
            margin-bottom: 1.2rem;
        }

        .about-box p:last-child {
            margin-bottom: 0;
        }

        .contact-box {
            background: transparent;
            backdrop-filter: none;
            border: none;
            border-radius: 0;
            padding: 2rem;
            margin: 2rem auto;
            max-width: 700px;
            text-align: left;
            box-shadow: none;
            transition: none;
        }

        .contact-box:hover {
            box-shadow: none;
            transform: none;
        }

        .contact-box p {
            margin-bottom: 1.2rem;
        }

        .contact-box p:last-child {
            margin-bottom: 0;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 768px) {
            .nav-menu {
                display: none;
            }

            .hero-title {
                font-size: 2.5rem;
            }

            .hero-subtitle {
                font-size: 1.2rem;
            }

            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }

            .btn {
                width: 200px;
            }

            .section {
                padding: 3rem 1rem;
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div id="particles-js"></div>

    <div class="container">
        <nav class="navbar">
            <div class="nav-brand">Portfolio</div>
            <ul class="nav-menu">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>

        <main class="hero-section" id="home">
            <div class="hero-content">
                <h1 class="hero-title">Hello, I'm <span class="highlight">Sophie</span></h1>
                <p class="hero-subtitle">Business Solutions Developer & AI Enthusiast | Turning Data into Insights & Experiences</p>
                <div class="hero-buttons">
                    <a href="#projects" class="btn btn-primary">View Projects</a>
                    <a href="#contact" class="btn btn-secondary">Contact Me</a>
                </div>
            </div>
        </main>

        <section id="about" class="section">
            <div class="section-content">
                <h2>About Me</h2>
                <div class="about-box">
                    <p>I am a Business Solutions Developer with several years of experience in the healthcare industry, specializing in data visualization, workflow automation, and AI-driven applications.</p>
                    <p>My expertise lies in transforming complex datasets into clear, actionable insights that support strategic decision-making.</p>
                    <p>I focus on combining data, artificial intelligence, and user-centered design to deliver solutions that improve efficiency, enhance decision quality, and generate measurable business value.</p>
                </div>

                <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: #495057;">Key Skills</h3>
                <div class="skills-grid">
                    <div class="skill-category">
                        <h4>Data Science</h4>
                        <p>SQL, Python, Power BI, Machine Learning</p>
                    </div>
                    <div class="skill-category">
                        <h4>AI & Automation</h4>
                        <p>LangChain, n8n, Databricks, vibe coding</p>
                    </div>
                    <div class="skill-category">
                        <h4>LLM & AI Applications</h4>
                        <p>RAG pipelines, fine-tuning (SFT), chatbots, TTS & speech recognition</p>
                    </div>
                    <div class="skill-category">
                        <h4>Collaboration & Delivery</h4>
                        <p>Agile, cross-team projects</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="projects" class="section">
            <div class="section-content">
                <h2>My Projects</h2>
                <div class="projects-grid">
                    <div class="project-card">
                        <h3><a href="https://hospital-lengthofstay-dashboard.streamlit.app/" target="_blank" rel="noopener noreferrer">AI Health Assistant</a></h3>
                        <p>A Streamlit-based dialogue system that explains health reports, highlights risks, and provides easy-to-understand insights.</p>
                    </div>
                    <div class="project-card">
                        <h3>Data Visualization Platform</h3>
                        <p>An interactive analysis tool using Python + Plotly, helping non-technical users explore and interpret data intuitively.</p>
                    </div>
                    <div class="project-card">
                        <h3>Contract Insights Dashboard</h3>
                        <p>A visualization tool analyzing healthcare contracts by stage, client type, and risk class—helping leadership make faster decisions.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="contact" class="section">
            <div class="section-content">
                <h2>Contact Me</h2>
                <div class="contact-box">
                    <p>Email: haggler-shelf-putt@duck.com</p>
                    <p>GitHub: https://github.com/SophieXueZhang</p>
                    <p>LinkedIn: https://www.linkedin.com/in/sophie-xuezhang/</p>
                </div>

                <div class="quote" style="margin-top: 3rem; padding: 2rem; background: rgba(255, 255, 255, 0.1); border-radius: 15px; text-align: center; font-style: italic; font-size: 1.2rem; color: #6c757d;">
                    "Great data + good design = better decisions."
                </div>
            </div>
        </section>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
        // 粒子效果配置
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 100,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#6c757d"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    }
                },
                "opacity": {
                    "value": 0.6,
                    "random": true,
                    "anim": {
                        "enable": true,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": true,
                        "speed": 3,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#6c757d",
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 3,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false,
                    "attract": {
                        "enable": true,
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": ["grab", "bubble"]
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 200,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "bubble": {
                        "distance": 150,
                        "size": 8,
                        "duration": 2,
                        "opacity": 1,
                        "speed": 3
                    },
                    "repulse": {
                        "distance": 100,
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 4
                    },
                    "remove": {
                        "particles_nb": 2
                    }
                }
            },
            "retina_detect": true
        });

        // 平滑滚动
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();

                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // 滚动时导航栏样式变化
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // 打字机效果
        function typeWriter(element, text, speed = 100) {
            let i = 0;
            element.innerHTML = '';

            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            }

            type();
        }

        // 页面加载完成后启动打字机效果
        document.addEventListener('DOMContentLoaded', function() {
            const heroTitle = document.querySelector('.hero-title');
            if (heroTitle) {
                const originalText = heroTitle.textContent;
                typeWriter(heroTitle, originalText, 80);
            }
        });
    </script>
</body>
</html>
"""

# 渲染HTML组件（全屏显示）
components.html(html_content, height=800, scrolling=True)

