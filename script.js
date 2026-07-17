document.addEventListener('DOMContentLoaded', () => {
    // Elements
    const langSwitch = document.getElementById('lang-switch');
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const bodyElement = document.body;

    /* ==========================================
       LANGUAGE TOGGLE LOGIC
       ========================================== */
    const savedLang = localStorage.getItem('cv-lang') || 'es';
    setLanguage(savedLang);

    langSwitch.addEventListener('change', (e) => {
        const selectedLang = e.target.checked ? 'en' : 'es';
        setLanguage(selectedLang);
    });

    function setLanguage(lang) {
        localStorage.setItem('cv-lang', lang);
        htmlElement.setAttribute('lang', lang);
        langSwitch.checked = (lang === 'en');
        
        if (lang === 'en') {
            document.title = "Adriel Avila | Senior Fullstack Developer";
        } else {
            document.title = "Adriel Avila | Desarrollador Fullstack Senior";
        }
    }

    /* ==========================================
       THEME TOGGLE LOGIC
       ========================================== */
    const savedTheme = localStorage.getItem('cv-theme') || 'dark';
    setTheme(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = bodyElement.classList.contains('light-theme') ? 'light' : 'dark';
        const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
        setTheme(nextTheme);
    });

    function setTheme(theme) {
        localStorage.setItem('cv-theme', theme);
        const icon = themeToggleBtn.querySelector('i');
        
        if (theme === 'light') {
            bodyElement.classList.add('light-theme');
            icon.className = 'fa-solid fa-sun';
            themeToggleBtn.setAttribute('title', 'Activar tema oscuro / Activate dark mode');
        } else {
            bodyElement.classList.remove('light-theme');
            icon.className = 'fa-solid fa-moon';
            themeToggleBtn.setAttribute('title', 'Activar tema claro / Activate light mode');
        }
    }
});
