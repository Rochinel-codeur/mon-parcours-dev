// Script pour améliorer l'interaction utilisateur du générateur de code QR

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const input = document.querySelector('input[name="data"]');
    const submitButton = document.querySelector('button[type="submit"]');
    
    // Fonction pour valider l'entrée utilisateur
    function validateInput() {
        const value = input.value.trim();
        if (value.length === 0) {
            input.setAttribute('aria-invalid', 'true');
            return false;
        } else {
            input.setAttribute('aria-invalid', 'false');
            return true;
        }
    }
    
    // Validation en temps réel
    input.addEventListener('input', function() {
        validateInput();
    });
    
    // Validation lors de la soumission du formulaire
    form.addEventListener('submit', function(e) {
        if (!validateInput()) {
            e.preventDefault();
            // Afficher un message d'erreur visuel
            input.focus();
            return false;
        }
        
        // Désactiver le bouton pendant le traitement
        submitButton.disabled = true;
        submitButton.textContent = 'Génération...';
    });
    
    // Réactiver le bouton après un certain temps (au cas où la requête prendrait trop de temps)
    setTimeout(function() {
        submitButton.disabled = false;
        submitButton.textContent = 'Générer';
    }, 5000);
});