document.addEventListener("DOMContentLoaded", () => {
    fetch('content.json?v=' + new Date().getTime())
        .then(response => response.json())
        .then(data => {
            const bodyEl = document.querySelector('#news-body') || document.querySelector('.news-content p');
            const titleEl = document.querySelector('#news-title') || document.querySelector('h3');
            
            if (data.sheng && data.sheng.body) {
                if (bodyEl) bodyEl.innerText = data.sheng.body;
                if (titleEl) titleEl.innerText = data.sheng.title;
            }
        })
        .catch(err => console.error("Error loading JSON:", err));
});
