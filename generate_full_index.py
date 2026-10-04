import json
import os
import re

html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PHOTO-REAL VIRTUALITY · 纯光学相机实拍与活人感摄影典藏</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Playfair+Display:ital,wght@0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    /* ─── Global Reset & Design Tokens ─── */
    :root {
      --bg-black: #070709;
      --bg-surface: #0e0e12;
      --bg-elevated: #15151b;
      --text-main: #ece7de;
      --text-muted: #a39c90;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-card: #1f1f26;
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      
      --font-serif: 'Playfair Display', Georgia, Cambria, serif;
      --font-display: 'Cinzel', serif;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif;
      --font-mono: 'JetBrains Mono', 'SF Mono', Menlo, Monaco, Consolas, monospace;
      
      /* Active Game Theming (Clean Architectural Colors) */
      --accent-primary: #c9aa71;
      --accent-bright: #e7ca94;
      --accent-dark: #8c734b;
    }

    body[data-game="eldenring"] {
      --accent-primary: #c9aa71;
      --accent-bright: #e7ca94;
      --accent-dark: #8c734b;
      --font-display: 'Cinzel', serif;
    }

    body[data-game="cyberpunk"] {
      --accent-primary: #00e5ff;
      --accent-bright: #70f3ff;
      --accent-dark: #0099ab;
      --font-display: var(--font-sans);
    }

    body[data-game="zelda"] {
      --accent-primary: #00bfa5;
      --accent-bright: #64ffda;
      --accent-dark: #00796b;
      --font-display: 'Cinzel', serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    ::selection {
      background: var(--accent-primary);
      color: #000;
    }

    body {
      background-color: var(--bg-black);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      letter-spacing: normal;
    }

    /* ─── Top Global Navigation & Game Universe Selector ─── */
    .top-nav {
      position: sticky;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 1000;
      background: rgba(7, 7, 9, 0.92);
      -webkit-backdrop-filter: blur(16px);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-logo {
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 500;
      letter-spacing: 0.04em;
      color: #fff;
    }

    .brand-tag {
      font-size: 11.5px;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.06);
      color: var(--accent-bright);
      font-family: var(--font-mono);
      letter-spacing: 0.02em;
    }

    /* Game Selector Pills */
    .game-selector {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(18, 18, 24, 0.8);
      padding: 4px;
      border-radius: 999px;
      border: 1px solid var(--border-subtle);
    }

    .game-tab {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 999px;
      border: 1px solid transparent;
      background: transparent;
      color: var(--text-muted);
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: color 150ms ease, background 150ms ease, border-color 150ms ease;
      white-space: nowrap;
    }

    .game-tab:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.04);
    }

    .game-tab.active {
      color: #fff;
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--accent-primary);
    }

    .game-tab .tab-count {
      font-family: var(--font-mono);
      font-size: 11.5px;
      padding: 1px 6px;
      border-radius: 999px;
      background: rgba(0, 0, 0, 0.35);
      color: var(--accent-bright);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .btn-methodology {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--accent-bright);
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 160ms ease;
    }

    .btn-methodology:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
      border-color: var(--accent-bright);
    }

    .nav-github {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 12px;
      font-family: var(--font-mono);
      transition: color 150ms ease;
    }

    .nav-github:hover {
      color: #fff;
    }

    @media (max-width: 900px) {
      .top-nav {
        flex-direction: column;
        align-items: stretch;
        gap: 12px;
        padding: 12px 16px;
      }
      .brand-section {
        justify-content: space-between;
      }
      .game-selector {
        overflow-x: auto;
      }
      .nav-actions {
        justify-content: flex-end;
      }
    }

    /* ─── Stage Harness ─── */
    #stage {
      min-height: calc(100vh - 65px);
      padding-bottom: 48px;
    }

    /* ─── EDITORIAL EXHIBITION ─── */
    .v-editorial {
      max-width: 1360px;
      margin: 0 auto;
      padding: 48px 24px 64px;
      animation: fadeIn 220ms var(--ease-out);
    }

    .v-editorial .hero {
      text-align: center;
      margin-bottom: 56px;
      position: relative;
    }

    .v-editorial .hero-title {
      font-family: var(--font-display);
      font-size: clamp(2rem, 4.5vw, 3.4rem);
      font-weight: 700;
      color: var(--accent-bright);
      line-height: 1.2;
      margin-bottom: 14px;
    }

    .v-editorial .hero-sub {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: clamp(1rem, 1.8vw, 1.25rem);
      color: var(--text-muted);
      max-width: 740px;
      margin: 0 auto;
      line-height: 1.6;
    }

    .v-editorial .hero-divider {
      width: 60px;
      height: 1px;
      background: var(--accent-primary);
      margin: 24px auto 0;
      opacity: 0.4;
    }

    .v-editorial .exhibit-grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 48px 32px;
      align-items: start;
    }

    .v-editorial .exhibit-item {
      grid-column: span 6;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .v-editorial .exhibit-item:nth-child(3n+1) {
      grid-column: span 12;
      display: grid;
      grid-template-columns: 7fr 5fr;
      gap: 36px;
      align-items: start;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border-subtle);
    }

    @media (max-width: 980px) {
      .v-editorial .exhibit-item { grid-column: span 12 !important; display: flex !important; }
    }

    .v-editorial .exhibit-media {
      position: relative;
      overflow: hidden;
      border-radius: 6px;
      background: #060608;
      border: 1px solid var(--border-subtle);
      cursor: zoom-in;
      transition: border-color 200ms ease;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .v-editorial .exhibit-media:hover {
      border-color: rgba(255, 255, 255, 0.22);
    }

    .v-editorial .exhibit-media img {
      width: 100%;
      height: auto;
      max-height: 85vh;
      object-fit: contain;
      display: block;
    }

    .v-editorial .exhibit-plate {
      position: absolute;
      bottom: 12px;
      left: 12px;
      background: rgba(0, 0, 0, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 4px 10px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: var(--accent-bright);
      border-radius: 4px;
    }

    .v-editorial .exhibit-info {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .v-editorial .exhibit-num {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-primary);
      letter-spacing: 0.02em;
    }

    .v-editorial .exhibit-title {
      font-family: var(--font-serif);
      font-size: 1.55rem;
      font-weight: 600;
      color: #fff;
      line-height: 1.25;
    }

    .v-editorial .exhibit-meta-line {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-muted);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
      padding: 6px 0;
    }

    .v-editorial .exhibit-desc {
      font-size: 0.92rem;
      color: #b0a99c;
      line-height: 1.7;
    }

    .v-editorial .exhibit-quote {
      font-family: var(--font-serif);
      font-style: italic;
      color: var(--accent-bright);
      font-size: 0.95rem;
      padding-left: 12px;
      border-left: 1px solid var(--accent-primary);
      margin-top: 4px;
    }

    /* ─── LIGHTBOX MODAL ─── */
    .lightbox-modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.94);
      z-index: 2147483646;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(12px);
    }
    .lightbox-modal.active {
      display: flex;
    }
    #lightboxMedia {
      display: flex;
      align-items: center;
      justify-content: center;
      max-width: 90vw;
      max-height: 84vh;
    }
    .lightbox-modal img {
      max-width: 90vw;
      max-height: 84vh;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.85);
      object-fit: contain;
      user-select: none;
      transition: opacity 150ms ease;
    }
    .lightbox-close {
      position: absolute;
      top: 20px;
      right: 28px;
      background: rgba(20, 20, 26, 0.75);
      border: 1px solid var(--border-subtle);
      color: #fff;
      font-size: 26px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 180ms ease;
      z-index: 20;
    }
    .lightbox-close:hover {
      background: rgba(40, 40, 50, 0.9);
      border-color: rgba(255, 255, 255, 0.28);
      color: var(--accent-bright);
    }
    .lightbox-nav {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: rgba(18, 18, 24, 0.82);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #fff;
      font-size: 28px;
      line-height: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 180ms ease;
      user-select: none;
      z-index: 20;
    }
    .lightbox-nav:hover {
      background: rgba(36, 36, 48, 0.95);
      border-color: rgba(255, 255, 255, 0.32);
      color: var(--accent-bright);
      transform: translateY(-50%) scale(1.05);
    }
    .lightbox-prev {
      left: 28px;
      padding-right: 2px;
    }
    .lightbox-next {
      right: 28px;
      padding-left: 2px;
    }
    .lightbox-hud {
      position: absolute;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(12, 12, 16, 0.85);
      backdrop-filter: blur(14px);
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      padding: 7px 22px;
      display: flex;
      align-items: center;
      gap: 16px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-muted);
      user-select: none;
      z-index: 20;
      white-space: nowrap;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
    }
    .lightbox-counter {
      color: var(--accent-bright);
      font-weight: 500;
    }
    .lightbox-name {
      color: #fff;
      font-family: var(--font-sans);
      font-weight: 500;
    }
    .lightbox-meta {
      color: var(--accent-primary);
    }
    @media (max-width: 768px) {
      .lightbox-nav {
        width: 42px;
        height: 42px;
        font-size: 22px;
      }
      .lightbox-prev { left: 12px; }
      .lightbox-next { right: 12px; }
      .lightbox-meta { display: none; }
      .lightbox-hud {
        bottom: 16px;
        padding: 5px 16px;
        gap: 10px;
        font-size: 11.5px;
      }
    }

    /* ─── METHODOLOGY MODAL ─── */
    .methodology-modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.88);
      z-index: 2147483645;
      backdrop-filter: blur(12px);
      overflow-y: auto;
      padding: 40px 20px 90px;
    }

    .methodology-content {
      max-width: 840px;
      margin: 0 auto;
      background: #0f0f14;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 36px 32px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7);
      position: relative;
      animation: fadeIn 180ms var(--ease-out);
    }

    .methodology-close {
      position: absolute;
      top: 20px;
      right: 24px;
      font-size: 26px;
      color: var(--text-muted);
      background: transparent;
      border: 0;
      cursor: pointer;
    }
    .methodology-close:hover { color: #fff; }

    .methodology-tag {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-bright);
      letter-spacing: 0.02em;
      margin-bottom: 8px;
    }

    .methodology-title {
      font-family: var(--font-serif);
      font-size: 1.8rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 12px;
    }

    .methodology-intro {
      color: #b5ada2;
      font-size: 0.95rem;
      line-height: 1.7;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 18px;
    }

    .methodology-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 18px;
    }

    .rule-card {
      background: #14141a;
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
      padding: 20px;
    }

    .rule-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }

    .rule-idx {
      font-family: var(--font-mono);
      font-size: 11.5px;
      padding: 2px 7px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.06);
      color: var(--accent-bright);
      border: 1px solid var(--accent-dark);
    }

    .rule-title {
      font-size: 1.05rem;
      font-weight: 600;
      color: #fff;
    }

    .rule-body {
      font-size: 0.9rem;
      color: #a8a195;
      line-height: 1.65;
    }

    .rule-body code {
      font-family: var(--font-mono);
      background: rgba(0, 0, 0, 0.35);
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--accent-bright);
      font-size: 0.88em;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(3px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body data-game="eldenring">

  <!-- TOP NAV WITH GAME UNIVERSE SELECTOR -->
  <header class="top-nav">
    <div class="brand-section">
      <div class="brand-logo">
        <span>PHOTO-REAL VIRTUALITY</span>
      </div>
      <span class="brand-tag" id="currentTag">Elden Ring · 25 Plates</span>
    </div>

    <!-- GAME UNIVERSE SWITCHER -->
    <nav class="game-selector" aria-label="Game Universe Selector">
      <button class="game-tab active" data-game="eldenring" onclick="switchGame('eldenring')">
        <span>艾尔登法环</span>
        <span class="tab-count">25</span>
      </button>
      <button class="game-tab" data-game="cyberpunk" onclick="switchGame('cyberpunk')">
        <span>赛博朋克 2077</span>
        <span class="tab-count">21</span>
      </button>
      <button class="game-tab" data-game="zelda" onclick="switchGame('zelda')">
        <span>塞尔达传说：旷野之息</span>
        <span class="tab-count">21</span>
      </button>
    </nav>

    <div class="nav-actions">
      <button class="btn-methodology" onclick="openMethodology()">
        <span>摄影法典 (Methodology)</span>
      </button>
      <a class="nav-github" href="https://github.com/holynova/elden-ring-liveaction" target="_blank" rel="noopener">
        <span>GitHub ↗</span>
      </a>
    </div>
  </header>

  <!-- PROTOTYPE STAGE -->
  <main id="stage"></main>

  <!-- LIGHTBOX MODAL (Interactive Plate Viewer with Left/Right Navigation) -->
  <div class="lightbox-modal" id="lightbox" onclick="handleLightboxBackdrop(event)">
    <button class="lightbox-close" onclick="closeLightbox(event)" aria-label="Close details">&times;</button>
    <button class="lightbox-nav lightbox-prev" onclick="prevLightboxImage(event)" aria-label="Previous plate">‹</button>
    <div id="lightboxMedia"></div>
    <button class="lightbox-nav lightbox-next" onclick="nextLightboxImage(event)" aria-label="Next plate">›</button>
    <div class="lightbox-hud" id="lightboxHud"></div>
  </div>

  <!-- METHODOLOGY MODAL -->
  <div class="methodology-modal" id="methodologyModal" onclick="handleMethodologyClick(event)">
    <div class="methodology-content">
      <button class="methodology-close" onclick="closeMethodology()">&times;</button>
      <div class="methodology-tag">Visual Methodology & Prompt Engineering</div>
      <h2 class="methodology-title">AI 单反纯光学实拍与“活人呼吸感”作图方法论</h2>
      <p class="methodology-intro">
        从传统 AI 生图常见的“虚浮 3D 渲染、游戏 CG 引擎假面、磨皮塑料娃娃感”，蜕变到具有“真实物理快门抓拍与鲜活生命力”的真实世界肖像纪实。以下为经过三大经典游戏 67 幅作品全面验证的五大黄金法则。
      </p>

      <div class="methodology-grid">
        <div class="rule-card">
          <div class="rule-header">
            <span class="rule-idx">RULE 01</span>
            <h3 class="rule-title">光学硬件与物理焦段深度锚定 (Hardware Anchoring)</h3>
          </div>
          <p class="rule-body">
            坚决抛弃 <code>8K</code>、<code>masterpiece</code>、<code>epic cinematic</code> 等虚浮词。明确声明具体相机与镜头型号：<code>佳能 EOS R5 搭配 85mm f/1.4 定焦镜头</code> 或 <code>哈苏中画幅 80mm f/2.2</code>，直接激活真实光学镜头的大光圈景深、焦外柔和散景与物理边缘色散。
          </p>
        </div>

        <div class="rule-card">
          <div class="rule-header">
            <span class="rule-idx">RULE 02</span>
            <h3 class="rule-title">生物学生理微观细节与“活人呼吸感” (Biological Reality)</h3>
          </div>
          <p class="rule-body">
            显式注入人类皮肤的天然生理特征：<code>完全未精修的自然皮肤质感</code>、<code>肉眼可见的细密毛孔与微小皮脂光泽</code>、<code>天然唇纹与微小脱皮</code>、<code>眼角战痕与疲惫眼神光</code>。必须加入 <code>被狂风吹乱贴在面颊的凌乱无序碎发</code>，彻底打破完美发胶假发带来的假人感。
          </p>
        </div>

        <div class="rule-card">
          <div class="rule-header">
            <span class="rule-idx">RULE 03</span>
            <h3 class="rule-title">实物道具的冷锻工艺与物理岁月磨损 (Weathering & Props)</h3>
          </div>
          <p class="rule-body">
            彻底否定 3D 模型表面平整无暇的平滑材质。写明道具的制作工艺与物理损耗：金属铠甲声明 <code>手工冷锻敲打留下的微小凹坑</code>、<code>做旧氧化暗痕与工业划痕</code>；义肢声明 <code>机械铰链与润滑油渍</code>；服饰强调 <code>粗纺亚麻</code>、<code>未处理毛边的粗剪羊毛</code> 与 <code>真皮自然折痕与重力垂坠褶皱</code>。
          </p>
        </div>

        <div class="rule-card">
          <div class="rule-header">
            <span class="rule-idx">RULE 04</span>
            <h3 class="rule-title">环境微气候与动态物理粒子系统 (Atmospheric Physics)</h3>
          </div>
          <p class="rule-body">
            让人体与所处微环境产生物理层面的呼吸与对流：深秋清晨 <code>口鼻与战马鼻孔喷出的真实白色热雾</code>；泥泞古道 <code>飞溅的真实雨水泥浆</code>；夜之城小巷 <code>拉面摊翻滚的热腾腾白色水汽与镜头表面微弱水雾光斑</code>；恶土沙漠 <code>夕阳低角度硬光下的飞扬沙尘颗粒</code>。
          </p>
        </div>

        <div class="rule-card">
          <div class="rule-header">
            <span class="rule-idx">RULE 05</span>
            <h3 class="rule-title">绝对否定关键词的坚决免疫阻断 (Negative Immunization)</h3>
          </div>
          <p class="rule-body">
            在提示词末尾部署绝对负面防火墙：<code>“绝对没有任何CG、3D建模渲染、二次元动画、网游磨皮假面或数字绘画感，完全是一张真实生活中的人物快门实拍照片。”</code> 强行迫使模型扩散路径远离游戏引擎与插画渲染树分支。
          </p>
        </div>
      </div>
    </div>
  </div>

  <script>
    /* ─── MULTI-GAME DATASET ─── */
    const GAMES = DATASETS_PLACEHOLDER;

    /* ─── ACTIVE STATE ─── */
    let currentGameKey = 'eldenring';

    function getActiveGame() {
      return GAMES[currentGameKey] || GAMES.eldenring;
    }

    /* ─── VARIANT 1: EDITORIAL ─── */
    function renderEditorial() {
      const g = getActiveGame();
      return `
        <div class="v-editorial">
          <header class="hero">
            <h1 class="hero-title">${g.heroTitle}</h1>
            <p class="hero-sub">${g.heroSub}</p>
            <div class="hero-divider"></div>
          </header>

          <div class="exhibit-grid">
            ${g.items.map((item, idx) => `
              <article class="exhibit-item">
                <div class="exhibit-media" onclick="openLightbox(${idx})">
                  <img src="${item.thumb}" data-full="${item.src}" alt="${item.name}" loading="${idx < 2 ? 'eager' : 'lazy'}" decoding="async" ${idx < 2 ? 'fetchpriority="high"' : ''}>
                  <span class="exhibit-plate">${item.lens}</span>
                </div>
                <div class="exhibit-info">
                  <span class="exhibit-num">Plate ${String(idx + 1).padStart(2, '0')}</span>
                  <h2 class="exhibit-title">${item.name}</h2>
                  <div class="exhibit-meta-line">
                    <span>${item.en}</span>
                    <span>${item.shutter}</span>
                  </div>
                  <p class="exhibit-desc">${item.desc}</p>
                  <blockquote class="exhibit-quote">${item.quote}</blockquote>
                </div>
              </article>
            `).join('')}
          </div>
        </div>
      `;
    }

    let currentLightboxIndex = -1;

    function openLightbox(idx) {
      const g = getActiveGame();
      if (!g || !g.items || idx < 0 || idx >= g.items.length) return;
      currentLightboxIndex = idx;
      const item = g.items[idx];
      const lb = document.getElementById('lightbox');
      const media = document.getElementById('lightboxMedia');
      const hud = document.getElementById('lightboxHud');
      if (!lb || !media) return;

      // 1. Immediately render thumbnail for zero-latency feedback
      media.innerHTML = `<img id="lightboxImg" alt="${item.name}" src="${item.thumb}">`;

      // 2. Render HUD info
      if (hud) {
        hud.innerHTML = `
          <span class="lightbox-counter">Plate ${String(idx + 1).padStart(2, '0')} / ${g.items.length}</span>
          <span class="lightbox-name">${item.name}</span>
          <span class="lightbox-meta">${item.lens} · ${item.shutter}</span>
        `;
      }

      lb.classList.add('active');

      // 3. Asynchronously load high-res image and smoothly swap
      const fullImg = new Image();
      fullImg.src = item.src;
      if (fullImg.decode) {
        fullImg.decode().then(() => {
          const activeImg = document.getElementById('lightboxImg');
          if (activeImg && lb.classList.contains('active') && currentLightboxIndex === idx) {
            activeImg.src = item.src;
          }
        }).catch(() => {});
      } else {
        fullImg.onload = () => {
          const activeImg = document.getElementById('lightboxImg');
          if (activeImg && currentLightboxIndex === idx) activeImg.src = item.src;
        };
      }

      // 4. Preload next and previous thumbnails
      const nextIdx = (idx + 1) % g.items.length;
      const prevIdx = (idx - 1 + g.items.length) % g.items.length;
      new Image().src = g.items[nextIdx].thumb;
      new Image().src = g.items[prevIdx].thumb;
    }

    function prevLightboxImage(e) {
      if (e) e.stopPropagation();
      const g = getActiveGame();
      if (!g || !g.items.length) return;
      const prevIdx = (currentLightboxIndex - 1 + g.items.length) % g.items.length;
      openLightbox(prevIdx);
    }

    function nextLightboxImage(e) {
      if (e) e.stopPropagation();
      const g = getActiveGame();
      if (!g || !g.items.length) return;
      const nextIdx = (currentLightboxIndex + 1) % g.items.length;
      openLightbox(nextIdx);
    }

    function closeLightbox(e) {
      if (e) e.stopPropagation();
      const lb = document.getElementById('lightbox');
      if (lb) lb.classList.remove('active');
      const media = document.getElementById('lightboxMedia');
      if (media) media.innerHTML = '';
      currentLightboxIndex = -1;
    }

    function handleLightboxBackdrop(e) {
      if (e.target.id === 'lightbox' || e.target.id === 'lightboxMedia') {
        closeLightbox(e);
      }
    }

    function openMethodology() {
      document.getElementById('methodologyModal').style.display = 'block';
    }

    function closeMethodology() {
      document.getElementById('methodologyModal').style.display = 'none';
    }

    function handleMethodologyClick(e) {
      if (e.target.id === 'methodologyModal') closeMethodology();
    }

    /* ─── GAME UNIVERSE SWITCHING ─── */
    function switchGame(gameKey) {
      if (!GAMES[gameKey]) return;
      currentGameKey = gameKey;
      document.body.setAttribute('data-game', gameKey);
      
      // Update Game Tabs
      document.querySelectorAll('.game-tab').forEach(tab => {
        tab.classList.toggle('active', tab.getAttribute('data-game') === gameKey);
      });

      // Update Tag in nav
      document.getElementById('currentTag').textContent = GAMES[gameKey].tag;

      // Update URL state
      const url = new URL(location);
      url.searchParams.set('game', gameKey);
      history.replaceState(null, '', url);

      // Re-mount Editorial view
      mount();
    }

    /* ─── STAGE MOUNTING & KEYBOARD SHORTCUTS ─── */
    const stage = document.getElementById('stage');

    function mount() {
      stage.innerHTML = renderEditorial();
    }

    // Keyboard bindings (Left/Right to flip plates, G for Game switch, Escape to close)
    document.addEventListener('keydown', (e) => {
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName) || e.target.isContentEditable) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      
      const lb = document.getElementById('lightbox');
      const isLbActive = lb && lb.classList.contains('active');

      if (isLbActive) {
        if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') {
          prevLightboxImage(e);
        } else if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') {
          nextLightboxImage(e);
        } else if (e.key === 'Escape') {
          closeLightbox(e);
        }
        return;
      }

      if (e.key === 'g' || e.key === 'G') {
        const gameKeys = Object.keys(GAMES);
        const nextIdx = (gameKeys.indexOf(currentGameKey) + 1) % gameKeys.length;
        switchGame(gameKeys[nextIdx]);
      } else if (e.key === 'Escape') {
        closeMethodology();
      }
    });

    // Touch swipe support on lightbox
    let touchStartX = 0;
    let touchStartY = 0;
    const lbEl = document.getElementById('lightbox');
    if (lbEl) {
      lbEl.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].clientX;
        touchStartY = e.changedTouches[0].clientY;
      }, { passive: true });

      lbEl.addEventListener('touchend', (e) => {
        const dx = e.changedTouches[0].clientX - touchStartX;
        const dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
          if (dx > 0) prevLightboxImage();
          else nextLightboxImage();
        }
      }, { passive: true });
    }

    // Initial load from URL search params
    const initialParams = new URLSearchParams(location.search);
    const initialGame = initialParams.get('game');
    if (initialGame && GAMES[initialGame]) {
      currentGameKey = initialGame;
      document.body.setAttribute('data-game', initialGame);
      document.querySelectorAll('.game-tab').forEach(tab => {
        tab.classList.toggle('active', tab.getAttribute('data-game') === initialGame);
      });
      document.getElementById('currentTag').textContent = GAMES[initialGame].tag;
    }

    mount();
  </script>
</body>
</html>
"""

# Import datasets directly from games_data
import games_data
games_dict = games_data.games_dict

# Augment each item with thumb and orig_thumb
for g_key, g_val in games_dict.items():
    for item in g_val["items"]:
        src = item["src"]
        dirname, fname = os.path.split(src)
        base, _ = os.path.splitext(fname)
        item["thumb"] = f"{dirname}/thumbs/{base}.jpg"
        
        if "orig" in item and item["orig"]:
            orig_src = item["orig"]
            o_dirname, o_fname = os.path.split(orig_src)
            o_base, _ = os.path.splitext(o_fname)
            item["orig_thumb"] = f"{o_dirname}/thumbs/{o_base}.jpg"

# Re-inject into template
games_json = json.dumps(games_dict, ensure_ascii=False, indent=2)
final_html = html_template.replace("DATASETS_PLACEHOLDER", games_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("index.html successfully updated with thumbnails, lazy loading, and impeccable typography!")
