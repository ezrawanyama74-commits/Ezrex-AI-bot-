// Ezrex AI Bot: Dual-Language Frontend Loader

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

// Default load: Sheng Desk
document.addEventListener('DOMContentLoaded', () => {
  loadContent('sheng');
});
