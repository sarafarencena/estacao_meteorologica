function deletar(id) {
    if (!confirm('Deseja remover esta leitura?')) return;
    fetch(`/leituras/${id}`, { method: 'DELETE' })
        .then(() => location.reload());
}

function salvar(id) {
    const temperatura = parseFloat(document.getElementById('temperatura').value);
    const umidade     = parseFloat(document.getElementById('umidade').value);
    fetch(`/leituras/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ temperatura, umidade })
    }).then(() => window.location.href = '/leituras');
}
