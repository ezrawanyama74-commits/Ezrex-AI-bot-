document.addEventListener("DOMContentLoaded", () => {
    const jsonUrl = 'content.json?v=' + new Date().getTime();

    fetch(jsonUrl)
        .then(res => res.json())
        .then(data => {
            // Elements
            const newsImg = document.querySelector('#news-img') || document.querySelector('.card-img-top') || document.querySelector('img');
            const newsTitle = document.querySelector('#news-title') || document.querySelector('h3');
            const newsBody = document.querySelector('#news-body') || document.querySelector('p');
            
            const btnSheng = document.querySelector('#btn-sheng') || document.querySelectorAll('.language-toggle button, a')[0];
            const btnEnglish = document.querySelector('#btn-english') || document.querySelectorAll('.language-toggle button, a')[1];

            // 1. Fix Image with reliable reliable tech placeholder fallback
            if (newsImg) {
                const validImg = data.image_url || "https://picsum.photos/800/400?tech";
                newsImg.src = validImg;
                newsImg.onerror = () => {
                    newsImg.src = "https://picsum.photos/800/400?technology";
                };
            }

            // 2. Set Default State (Sheng)
            let currentLang = 'sheng';

            function renderContent(lang) {
                if (!data[lang]) return;
                
                if (newsTitle) newsTitle.innerText = data[lang].title;
                if (newsBody) newsBody.innerText = data[lang].body;

                // Toggle active visual styles if buttons exist
                if (btnSheng && btnEnglish) {
                    if (lang === 'sheng') {
                        btnSheng.style.fontWeight = 'bold';
                        btnEnglish.style.fontWeight = 'normal';
                    } else {
                        btnEnglish.style.fontWeight = 'bold';
                        btnSheng.style.fontWeight = 'normal';
                    }
                }
            }

            // Initial Render
            renderContent('sheng');

            // 3. Attach Click Listeners for Language Switcher
            if (btnSheng) {
                btnSheng.addEventListener('click', (e) => {
                    e.preventDefault();
                    renderContent('sheng');
                });
            }

            if (btnEnglish) {
                btnEnglish.addEventListener('click', (e) => {
                    e.preventDefault();
                    renderContent('english');
                });
            }
        })
        .catch(err => console.error("Error loading content.json:", err));
});
