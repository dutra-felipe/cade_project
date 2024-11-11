const translations = {
    pt: {
        // Menu de Navegação
        'menu': 'Menu',
        'about': 'Sobre o CADE',
        'press': 'Notas a Imprensa',
        'jurisprudence': 'Jurisprudência',
        'events': 'Eventos',
        // Seletor de Idioma
        'idiomas': 'Idiomas',
        /// Títulos e Filtros
        'news_title': 'Novidades do CADE',
        'filter_all': 'Todos',
        'filter_decisions': 'Decisões',
        'filter_concentration': 'Atos de Concentração',
        'filter_conduct': 'Condutas Anticompetitivas',
        'filter_international': 'Internacional',
        // Tags
        'tag_decisions': 'Decisões',
        'tag_international': 'Internacional',
        'tag_conduct': 'Condutas Anticompetitivas',
        'tag_concentration': 'Atos de Concentração',
        // Notícia 1
        'news1_title': 'CADE aprova sem restrições fusão entre empresas do setor tecnológico',
        'news1_text': 'O Tribunal do CADE aprovou, por unanimidade, a operação de fusão entre duas grandes empresas do setor de tecnologia, considerando que não haveria prejuízos à concorrência...',
        // Notícia 2
        'news2_title': 'CADE participa de encontro internacional sobre práticas anticompetitivas',
        'news2_text': 'Representantes do CADE participaram de importante encontro internacional para discutir práticas anticompetitivas no mercado digital e novas tecnologias...',
        // Notícia 3
        'news3_title': 'CADE instaura processo administrativo para investigar possível cartel',
        'news3_text': 'A Superintendência-Geral do CADE instaurou processo administrativo para investigar supostas práticas anticompetitivas no mercado de produtos farmacêuticos...',
        // Notícia 4
        'news4_title': 'Novo guia de análise de atos de concentração é publicado',
        'news4_text': 'O CADE publicou hoje seu novo guia de análise de atos de concentração, documento que traz orientações atualizadas sobre a análise de fusões e aquisições...',
        // Navegação
        'read_more': 'Ler mais',
        'previous': 'Anterior',
        'next': 'Próxima'
    },
    en: {
        // Menu de Navegação
        'menu': 'Menu',
        'about': 'About CADE',
        'press': 'Press Releases',
        'jurisprudence': 'Jurisprudence',
        'events': 'Events',
        // Seletor de Idioma
        'idiomas': 'Languages',
        // Titles and Filters
        'news_title': 'CADE News',
        'filter_all': 'All',
        'filter_decisions': 'Decisions',
        'filter_concentration': 'Concentration Acts',
        'filter_conduct': 'Anticompetitive Conduct',
        'filter_international': 'International',
        // Tags
        'tag_decisions': 'Decisions',
        'tag_international': 'International',
        'tag_conduct': 'Anticompetitive Conduct',
        'tag_concentration': 'Concentration Acts',
        // News 1
        'news1_title': 'CADE approves merger between technology companies without restrictions',
        'news1_text': 'CADE\'s Tribunal unanimously approved the merger operation between two major technology companies, considering there would be no harm to competition...',
        // News 2
        'news2_title': 'CADE participates in international meeting on anticompetitive practices',
        'news2_text': 'CADE representatives participated in an important international meeting to discuss anticompetitive practices in the digital market and new technologies...',
        // News 3
        'news3_title': 'CADE initiates administrative proceeding to investigate possible cartel',
        'news3_text': 'CADE\'s General Superintendence initiated an administrative proceeding to investigate alleged anticompetitive practices in the pharmaceutical products market...',
        // News 4
        'news4_title': 'New guide for concentration acts analysis is published',
        'news4_text': 'CADE published today its new guide for concentration acts analysis, a document that brings updated guidelines on the analysis of mergers and acquisitions...',
        // Navigation
        'read_more': 'Read more',
        'previous': 'Previous',
        'next': 'Next'
    },
    es: {
        // Menu de Navegação
        'menu': 'Menú',
        'about': 'Sobre CADE',
        'press': 'Notas de Prensa',
        'jurisprudence': 'Jurisprudencia',
        'events': 'Eventos',
        // Seletor de Idioma
        'idiomas': 'Idiomas',
        // Títulos y Filtros
        'news_title': 'Novedades del CADE',
        'filter_all': 'Todos',
        'filter_decisions': 'Decisiones',
        'filter_concentration': 'Actos de Concentración',
        'filter_conduct': 'Conductas Anticompetitivas',
        'filter_international': 'Internacional',
        // Etiquetas
        'tag_decisions': 'Decisiones',
        'tag_international': 'Internacional',
        'tag_conduct': 'Conductas Anticompetitivas',
        'tag_concentration': 'Actos de Concentración',
        // Noticia 1
        'news1_title': 'CADE aprueba sin restricciones fusión entre empresas del sector tecnológico',
        'news1_text': 'El Tribunal del CADE aprobó, por unanimidad, la operación de fusión entre dos grandes empresas del sector tecnológico, considerando que no habría perjuicios a la competencia...',
        // Noticia 2
        'news2_title': 'CADE participa en encuentro internacional sobre prácticas anticompetitivas',
        'news2_text': 'Representantes del CADE participaron en un importante encuentro internacional para discutir prácticas anticompetitivas en el mercado digital y nuevas tecnologías...',
        // Noticia 3
        'news3_title': 'CADE inicia proceso administrativo para investigar posible cartel',
        'news3_text': 'La Superintendencia General del CADE inició un proceso administrativo para investigar supuestas prácticas anticompetitivas en el mercado de productos farmacéuticos...',
        // Noticia 4
        'news4_title': 'Nueva guía de análisis de actos de concentración es publicada',
        'news4_text': 'El CADE publicó hoy su nueva guía de análisis de actos de concentración, documento que trae orientaciones actualizadas sobre el análisis de fusiones y adquisiciones...',
        // Navegación
        'read_more': 'Leer más',
        'previous': 'Anterior',
        'next': 'Siguiente'
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