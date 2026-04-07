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

// // atualização automática da página
// setInterval(() => {
//     fetch('/leituras?formato=json')
//         .then(res => {
//             if (!res.ok) throw new Error();
//             return res.json();
//         })
//         .then(dados => {
//             console.log("Atualizado com sucesso");
//         })
//         .catch(() => {
//             console.log("Offline — mantendo dados atuais");
//         });
// }, 5000);


// function deletar(id) {
//     if (!confirm('Deseja remover esta leitura?')) return;
//     fetch(`/leituras/${id}`, { method: 'DELETE' })
//         .then(() => location.reload());
// }

// function salvar(id) {
//     const temperatura = parseFloat(document.getElementById('temperatura').value);
//     const umidade     = parseFloat(document.getElementById('umidade').value);
//     fetch(`/leituras/${id}`, {
//         method: 'PUT',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ temperatura, umidade })
//     }).then(() => window.location.href = '/leituras');
// }

// // Controle de edição
// let editando = false;

// document.addEventListener('focusin', (e) => {
//     if (e.target.tagName === "INPUT") {
//         editando = true;
//     }
// });

// document.addEventListener('focusout', (e) => {
//     if (e.target.tagName === "INPUT") {
//         editando = false;
//     }
// });

// // Recursos para atualização da página
// setInterval(() => {
//     if (editando) {
//         console.log("Editando — pausa atualização");
//         return;
//     }

//     fetch('/leituras?formato=json')
//         .then(res => {
//             if (!res.ok) throw new Error();
//             return res.json();
//         })
//         .then(() => {
//             console.log("Atualizado com sucesso");
//         })
//         .catch(() => {
//             console.log("Servidor offline — mantendo dados atuais");
//         });
// }, 5000);