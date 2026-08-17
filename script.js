const menuBtn = document.getElementById('menu-btn');
const navDrawer = document.getElementById('nav-drawer');
const overlay = document.getElementById('overlay');
const menuList = document.getElementById('menu-list');
const dynamicContainer = document.getElementById('dynamic-sections');

// Toggle Drawer Navigation
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

// Scraped Content Loader & Category Router
async function loadContent(lang) {
  try {
    const response = await fetch('./content.json');
    const data = await response.json();

    // Set active tab styling
    document.getElementById('btn-sheng').classList.toggle('active-tab', lang === 'sheng');
    document.getElementById('btn-english').classList.toggle('active-tab', lang === 'english');

    // Route standard news directly to the existing News card
    if (data[lang]) {
      document.getElementById('news-title').textContent = data[lang].title;
      document.getElementById('news-body').textContent = data[lang].body;
    }

    // Check for new categories in payload and inject them dynamically
    if (data.categories) {
      data.categories.forEach(cat => {
        const catId = `cat-${cat.slug}`;

        // If section doesn't exist yet, append section and menu item
        if (!document.getElementById(catId)) {
          // 1. Add item to Hamburger Menu
          const li = document.createElement('li');
          li.innerHTML = `<a href="#${catId}" onclick="closeMenu()">📌 ${cat.title}</a>`;
          menuList.appendChild(li);

          // 2. Append new category section to page
          const section = document.createElement('section');
          section.id = catId;
          section.className = 'editorial-card';
          section.innerHTML = `
            <span class="section-subtitle">NEW CATEGORY</span>
            <h2>${cat.title.toUpperCase()}</h2>
            <div class="news-content-box">
              <p>${cat.content}</p>
            </div>
          `;
          dynamicContainer.appendChild(section);
        }
      });
    }

  } catch (error) {
    console.error('Error loading content:', error);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  loadContent('sheng');
});
