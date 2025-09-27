import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="个人主页",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main > div {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    .stApp > header {
        background-color: transparent;
    }

    .stApp {
        margin: 0;
        padding: 0;
    }

    iframe {
        border: none;
        height: 100vh;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# HTML内容
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>个人主页</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #ffffff;
            overflow-x: hidden;
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
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .navbar.scrolled {
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(20px);
        }

        .nav-brand {
            font-size: 1.5rem;
            font-weight: bold;
            color: #ffffff;
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-menu a {
            color: #ffffff;
            text-decoration: none;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-menu a:hover {
            color: #ffd700;
        }

        .nav-menu a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: #ffd700;
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
        }

        .highlight {
            background: linear-gradient(45deg, #ffd700, #ff6b6b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            opacity: 0.9;
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
            background: linear-gradient(45deg, #ffd700, #ff6b6b);
            color: #000;
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.2);
            color: #ffffff;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);
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
            font-size: 2.5rem;
            margin-bottom: 2rem;
            position: relative;
            display: inline-block;
        }

        .section h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 3px;
            background: linear-gradient(45deg, #ffd700, #ff6b6b);
        }

        .section p {
            font-size: 1.2rem;
            line-height: 1.6;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .project-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            background: rgba(255, 255, 255, 0.2);
        }

        .project-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #ffd700;
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
                <li><a href="#home">首页</a></li>
                <li><a href="#about">关于</a></li>
                <li><a href="#projects">项目</a></li>
                <li><a href="#contact">联系</a></li>
            </ul>
        </nav>

        <main class="hero-section" id="home">
            <div class="hero-content">
                <h1 class="hero-title">你好，我是 <span class="highlight">开发者</span></h1>
                <p class="hero-subtitle">全栈开发工程师 | 用代码创造美好</p>
                <div class="hero-buttons">
                    <a href="#projects" class="btn btn-primary">查看项目</a>
                    <a href="#contact" class="btn btn-secondary">联系我</a>
                </div>
            </div>
        </main>

        <section id="about" class="section">
            <div class="section-content">
                <h2>关于我</h2>
                <p>passionate开发者，专注于前端技术和用户体验。擅长JavaScript、React、Node.js等技术栈，致力于用代码创造更美好的数字体验。</p>
                <div class="skills">
                    <div class="skill-item">Frontend</div>
                    <div class="skill-item">Backend</div>
                    <div class="skill-item">UI/UX</div>
                    <div class="skill-item">DevOps</div>
                </div>
            </div>
        </section>

        <section id="projects" class="section">
            <div class="section-content">
                <h2>我的项目</h2>
                <div class="projects-grid">
                    <div class="project-card">
                        <h3>AI智能助手</h3>
                        <p>基于Streamlit开发的智能对话系统，集成先进的NLP技术</p>
                    </div>
                    <div class="project-card">
                        <h3>数据可视化平台</h3>
                        <p>使用Python和Plotly构建的交互式数据分析工具</p>
                    </div>
                    <div class="project-card">
                        <h3>Web应用开发</h3>
                        <p>响应式设计的现代化Web应用，具备粒子动画效果</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="contact" class="section">
            <div class="section-content">
                <h2>联系我</h2>
                <p>邮箱: your-email@example.com</p>
                <p>GitHub: github.com/yourusername</p>
                <p>Streamlit Cloud: 部署在云端的应用</p>
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
                    "value": "#ffffff"
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
                    "color": "#ffffff",
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

# 渲染HTML组件
components.html(html_content, height=600, scrolling=True)

# 侧边栏功能（可选）
with st.sidebar:
    st.title("✨ 个人主页设置")

    st.subheader("🎨 定制选项")

    # 主题选择
    theme_color = st.selectbox(
        "选择主题色调",
        ["蓝紫渐变", "日落橙红", "森林绿色", "夜空深蓝"]
    )

    # 粒子数量
    particle_count = st.slider("粒子数量", 50, 200, 100)

    # 动画速度
    animation_speed = st.slider("动画速度", 1, 10, 3)

    st.info("💡 修改设置后需要刷新页面生效")

    # 导出功能
    st.subheader("📁 导出选项")
    if st.button("下载HTML文件"):
        st.download_button(
            label="💾 下载完整HTML",
            data=html_content,
            file_name="portfolio.html",
            mime="text/html"
        )

# 页脚信息
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🚀 基于 Streamlit 构建的粒子效果个人主页</p>
    <p>✨ 支持鼠标交互的动态粒子背景</p>
</div>
""", unsafe_allow_html=True)