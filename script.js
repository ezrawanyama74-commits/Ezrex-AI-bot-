document.addEventListener("DOMContentLoaded", () => {
    // Fetch content.json with cache buster
    fetch('content.json?v=' + new Date().getTime())
        .then(res => res.json())
        .then(data => {
            const titleEl = document.querySelector('h3') || document.querySelector('.card-body h3') || document.querySelectorAll('h3, h4')[0];
            const bodyEl = document.querySelector('p') || document.querySelector('.card-body p');
            
            // Find language elements by text content or tag
            const links = Array.from(document.querySelectorAll('a'));
            const shengBtn = links.find(el => el.textContent.includes("Sheng' Desk"));
            const englishBtn = links.find(el => el.textContent.includes("World English"));

            function setLanguage(lang) {
                if (!data[lang]) return;

                // Update text
                if (titleEl) titleEl.innerText = data[lang].title;
                if (bodyEl) bodyEl.innerText = data[lang].body;

                // Highlight active tab visually
                if (shengBtn && englishBtn) {
                    if (lang === 'sheng') {
                        shengBtn.style.textDecoration = "underline";
                        shengBtn.style.fontWeight = "bold";
                        englishBtn.style.textDecoration = "none";
                        englishBtn.style.fontWeight = "normal";
                    } else {
                        englishBtn.style.textDecoration = "underline";
                        englishBtn.style.fontWeight = "bold";
                        shengBtn.style.textDecoration = "none";
                        shengBtn.style.fontWeight = "normal";
                    }
                }
            }

            // Set initial state to Sheng
            setLanguage('sheng');

            // Attach click event listeners
            if (shengBtn) {
                shengBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    setLanguage('sheng');
                });
            }

            if (englishBtn) {
                englishBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    setLanguage('english');
                });
            }
        })
        .catch(err => console.error("Error loading JSON:", err));
});
