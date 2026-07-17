document.addEventListener('DOMContentLoaded', () => {
    const langSwitch = document.getElementById('lang-switch');
    const htmlElement = document.documentElement;

    // Load saved language preference or default to Spanish ('es')
    const savedLang = localStorage.getItem('cv-lang') || 'es';
    
    // Set initial state
    setLanguage(savedLang);

    // Add change event listener to switch
    langSwitch.addEventListener('change', (e) => {
        const selectedLang = e.target.checked ? 'en' : 'es';
        setLanguage(selectedLang);
    });

    /**
     * Updates the page language and checkbox state.
     * @param {string} lang - The language code ('es' or 'en')
     */
    function setLanguage(lang) {
        // Save to local storage
        localStorage.setItem('cv-lang', lang);
        
        // Update html lang attribute
        htmlElement.setAttribute('lang', lang);
        
        // Update switch checkbox checked status
        // checked = true means 'en', checked = false means 'es'
        langSwitch.checked = (lang === 'en');
        
        // Update browser/tab title based on language
        if (lang === 'en') {
            document.title = "Adriel Avila | Senior Fullstack Developer";
        } else {
            document.title = "Adriel Avila | Desarrollador Fullstack Senior";
        }
    }
});
