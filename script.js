// Hamburger Toggle Logic
const menuBtn = document.getElementById('menu-btn');
const navDrawer = document.getElementById('nav-drawer');
const overlay = document.getElementById('overlay');

function toggleMenu() {
  navDrawer.classList.toggle('open');
  overlay.classList.toggle('active');
}

if (menuBtn) {
  menuBtn.addEventListener('click', toggleMenu);
}

// Page View Switcher Logic
function showPage(pageId) {
  const pages = document.querySelectorAll('.page-content');
  pages.forEach(page => page.classList.remove('active-page'));

  const targetPage = document.getElementById(pageId);
  if (targetPage) {
    targetPage.classList.add('active-page');
  }

  // Close drawer after selection
  if (navDrawer.classList.contains('open')) {
    toggleMenu();
  }
}

// Scraped Content Loader Logic
async function loadContent(lang) {
  try {
    const response = await fetch('./content.json');
    const data = await response.json();
    
    if (data[lang]) {
      document.getElementById('news-title').textContent = data[lang].title;
      document.getElementById('news-body').textContent = data[lang].body;
    }
  } catch (error) {
    console.error('Error loading content:', error);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  loadContent('sheng');
});
