const menuBtn = document.getElementById('menu-btn');
const navDrawer = document.getElementById('nav-drawer');
const overlay = document.getElementById('overlay');

let globalData = null;

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

// Fetch content from local scraper API payload
async function fetchContent() {
  try {
    const response = await fetch('./content.json?t=' + new Date().getTime());
    globalData = await response.json();

    if (globalData) {
      // Update Banner Image & Metadata
      document.getElementById('news-image').src = globalData.image_url;
      document.getElementById('news-badge').textContent = globalData.badge || '✓ LIVE UPDATE';
      document.getElementById('news-category').textContent = globalData.category || 'TECH INSIGHTS';

      // Default to Sheng text
      switchLanguage('sheng');
    }
  } catch (error) {
    console.error('Error loading JSON payload:', error);
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
  // Refresh content on client UI every 60 seconds
  setInterval(fetchContent, 60000);
});
