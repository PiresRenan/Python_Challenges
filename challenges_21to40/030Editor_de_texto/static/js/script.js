document.addEventListener('DOMContentLoaded', function() {
    const filenameInput = document.getElementById('filename');
    const filenameLoadInput = document.getElementById('filename_load');

    // Atualizar o valor do input de carregar ao clicar no botão "Abrir Editor"
    document.getElementById('open-editor-btn').addEventListener('click', function() {
        filenameLoadInput.value = filenameInput.value;
    });
});