const translations = {
    pt: {
        'menu': 'Menu',
        'about': 'Sobre o CADE',
        'press': 'Notas a Imprensa',
        'jurisprudence': 'Jurisprudência',
        'events': 'Eventos',
        'search-placeholder': 'Pesquisar...',
        'recent-cases': 'Casos recentes',
        'news': 'Novidades',
        'contact': 'Formulário de contato',
        'filtro' : 'Filtro',
        'documentTypes' : 'Tipos de documentos',
        'processos' : 'Processos',
        'years' : 'Ano',
        'setor' : 'Setor',

    },
    en: {
        'menu': 'Menu',
        'about': 'About CADE',
        'press': 'Press Releases',
        'jurisprudence': 'Jurisprudence',
        'events': 'Events',
        'search-placeholder': 'Search...',
        'recent-cases': 'Recent Cases',
        'news': 'News',
        'contact': 'Contact Form',
        'filtro' : 'Filter',
        'documentTypes' : 'Document types',
        'processos' : 'Processes',
        'years' : 'Year',
        'setor' : 'Sector',
        
    },
    es: {
        'menu': 'Menú',
        'about': 'Sobre CADE',
        'press': 'Notas de Prensa',
        'jurisprudence': 'Jurisprudencia',
        'events': 'Eventos',
        'search-placeholder': 'Buscar...',
        'recent-cases': 'Casos Recientes',
        'news': 'Novedades',
        'contact': 'Formulario de Contacto',
        'filtro' : 'Filtrar',
        'documentTypes' : 'Tipos de documentos',
        'processos' : 'Procesos',
        'years' : 'Año',
        'setor' : 'Sector',
    }
};

document.getElementById('langSelector').addEventListener('click', function() {
    document.getElementById('langDropdown').classList.toggle('show');
});

document.addEventListener('click', function(event) {
    if (!event.target.closest('.language-selector')) {
        document.getElementById('langDropdown').classList.remove('show');
    }
});

document.querySelectorAll('.language-option').forEach(option => {
    option.addEventListener('click', function() {
        const lang = this.dataset.lang;
        changeLanguage(lang);
        document.getElementById('langDropdown').classList.remove('show');
        
        const langText = this.querySelector('span').textContent;
        document.querySelector('.current-lang').textContent = langText;
    });
});

function changeLanguage(lang) {
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.dataset.translate;
        if (translations[lang] && translations[lang][key]) {
            if (element.tagName === 'INPUT') {
                element.placeholder = translations[lang][key];
            } else {
                element.textContent = translations[lang][key];
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.querySelector('.search-input');
    const clearSearchButton = document.getElementById('clearSearch');
    const filterCheckboxes = document.querySelectorAll('.filter-checkbox');
    let timeoutId;

    // Função para submeter o formulário
    function submitSearch() {
        searchForm.submit();
    }

    // Pesquisa ao digitar (com debounce)
    searchInput.addEventListener('input', function() {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(submitSearch, 500);
    });

    // Limpar pesquisa
    clearSearchButton.addEventListener('click', function() {
        searchInput.value = '';
        submitSearch();
    });

    // Submit ao mudar filtros
    filterCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', submitSearch);
    });

    // Remover filtros individuais
    document.getElementById('activeFilters').addEventListener('click', function(e) {
        if (e.target.classList.contains('bi-x-circle')) {
            const filterType = e.target.dataset.filter;
            const filterValue = e.target.dataset.value;

            if (filterType === 'query') {
                searchInput.value = '';
            } else {
                const checkbox = document.querySelector(`input[name="${filterType}"][value="${filterValue}"]`);
                if (checkbox) {
                    checkbox.checked = false;
                }
            }
            submitSearch();
        }
    });
});