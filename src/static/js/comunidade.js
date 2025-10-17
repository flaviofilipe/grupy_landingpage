// JavaScript para a página de Comunidade

document.addEventListener('DOMContentLoaded', function() {
    // Mostrar/ocultar botão "Voltar ao Topo"
    const backToTopButton = document.querySelector('.back-to-top');
    
    if (backToTopButton) {
        // Inicialmente ocultar o botão
        backToTopButton.style.display = 'none';

        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.style.display = 'flex';
            } else {
                backToTopButton.style.display = 'none';
            }
        });

        // Scroll suave ao clicar no botão
        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Adicionar animação de entrada aos cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observar todos os cards de membros
    const memberCards = document.querySelectorAll('.member-card');
    memberCards.forEach(function(card, index) {
        // Configurar estado inicial
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        
        observer.observe(card);
    });

    // Adicionar feedback visual ao clicar nos cards
    memberCards.forEach(function(card) {
        card.addEventListener('click', function(e) {
            // Apenas se o clique não for em um link
            if (e.target.tagName !== 'A') {
                const profileLink = card.querySelector('.btn-view-profile');
                if (profileLink) {
                    profileLink.click();
                }
            }
        });

        // Adicionar classe ao card quando houver foco em um elemento interno
        const focusableElements = card.querySelectorAll('a, button');
        focusableElements.forEach(function(element) {
            element.addEventListener('focus', function() {
                card.classList.add('has-focus');
            });

            element.addEventListener('blur', function() {
                card.classList.remove('has-focus');
            });
        });
    });

    // Log para debug
    console.log('Página de Comunidade carregada');
    console.log(`Total de membros: ${memberCards.length}`);
});

