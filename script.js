document.addEventListener("DOMContentLoaded", () => {
    // Add timestamp query parameter to bypass browser/CDN cache
    fetch('./content.json?v=' + new Date().getTime())
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log("Loaded content:", data);
            
            // Update image and badge
            const imageEl = document.querySelector(".news-card img, #news-image, [alt*='Banner']");
            if (imageEl && data.image_url) {
                imageEl.src = data.image_url;
            }
            
            const badgeEl = document.querySelector(".badge, .badge-text");
            if (badgeEl && data.badge) {
                badgeEl.textContent = data.badge;
            }
            
            const categoryEl = document.querySelector(".category, .news-category");
            if (categoryEl && data.category) {
                categoryEl.textContent = data.category;
            }

            // Default language state (Sheng)
            let currentLang = "sheng";
            
            const titleEl = document.querySelector(".news-title, #news-title, h3");
            const bodyEl = document.querySelector(".news-body, #news-body, p");

            function updateDisplay() {
                if (data[currentLang]) {
                    if (titleEl) titleEl.textContent = data[currentLang].title;
                    if (bodyEl) bodyEl.textContent = data[currentLang].body;
                }
            }

            updateDisplay();

            // Language Toggle Setup
            const shengBtn = document.querySelector("#sheng-btn, .sheng-toggle");
            const englishBtn = document.querySelector("#english-btn, .english-toggle");

            if (shengBtn) {
                shengBtn.addEventListener("click", () => {
                    currentLang = "sheng";
                    updateDisplay();
                });
            }

            if (englishBtn) {
                englishBtn.addEventListener("click", () => {
                    currentLang = "english";
                    updateDisplay();
                });
            }
        })
        .catch(err => {
            console.error("Error loading content.json:", err);
        });
});
