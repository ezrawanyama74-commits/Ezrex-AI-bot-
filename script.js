const menuBtn = document.getElementById('menu-btn');
const navDrawer = document.getElementById('nav-drawer');
const overlay = document.getElementById('overlay');

let globalData = null;
const DEFAULT_IMAGE = "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80";

function toggleMenu() {
  navDrawer.classList.toggle('open');
  overlay.classList.toggle('active');
}

function closeMenu() {
  navDrawer.classList.remove('open');
  overlay.classList.remove('active');
}

if (menuBtn) {
  menuBtn.addEventListener('click', toggleMenu);
}

async function fetchContent() {
  try {
    const response = await fetch('./content.json?t=' + new Date().getTime());
    globalData = await response.json();

    if (globalData) {
      const imgElement = document.getElementById('news-image');
      
      // Set image URL or fallback to default tech image
      imgElement.src = globalData.image_url || DEFAULT_IMAGE;
      imgElement.onerror = () => { imgElement.src = DEFAULT_IMAGE; };

      document.getElementById('news-badge').textContent = globalData.badge || '✓ LIVE UPDATE';
      document.getElementById('news-category').textContent = globalData.category || 'TECH INSIGHTS';

      switchLanguage('sheng');
    }
  } catch (error) {
    console.error('Error loading content.json:', error);
  }
}

function switchLanguage(lang) {
  if (!globalData || !globalData[lang]) return;

  document.getElementById('btn-sheng').classList.toggle('active-tab', lang === 'sheng');
  document.getElementById('btn-english').classList.toggle('active-tab', lang === 'english');

  document.getElementById('news-title').textContent = globalData[lang].title;
  document.getElementById('news-body').textContent = globalData[lang].body;
}

document.addEventListener('DOMContentLoaded', () => {
  fetchContent();
  setInterval(fetchContent, 60000);
});
