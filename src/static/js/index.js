/**
 * Script para a página inicial
 * Gerencia a busca de perfis do GitHub
 */

function searchGithub(event) {
    event.preventDefault();
    const username = document.getElementById('username').value.trim();
    
    if (username) {
        // Redireciona para a página de perfil
        window.location.href = `/github/${username}`;
    } else {
        alert('Por favor, digite um username do GitHub');
    }
}

// Adiciona validação em tempo real
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('username');
    
    if (input) {
        // Remove espaços ao digitar
        input.addEventListener('input', function(e) {
            e.target.value = e.target.value.replace(/\s/g, '');
        });
        
        // Foca no input ao carregar a página
        input.focus();
    }
});

