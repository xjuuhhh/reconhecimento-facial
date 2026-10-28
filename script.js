// Simulação de Base de Dados local para validação
const bancoDeDadosMock = [
    { codPaciente: "PAC101", cpf: "111.111.111-11", nome: "Ana Silva" },
    { codPaciente: "PAC202", cpf: "222.222.222-22", nome: "Carlos Souza" },
    { codPaciente: "PAC303", cpf: "333.333.333-33", nome: "Mariana Costa" }
];

const medicosAutorizados = ["MED123", "MED456", "MED789"];

// Lógica para ligar a webcam do computador
const btnAtivarCamera = document.getElementById('btn-ativar-camera');
const videoFeed = document.getElementById('video-feed');
const cameraPlaceholder = document.getElementById('camera-placeholder');

btnAtivarCamera.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoFeed.srcObject = stream;
        videoFeed.style.display = 'block';
        cameraPlaceholder.style.display = 'none'; // Esconde o aviso ao ligar
        btnAtivarCamera.textContent = 'Câmara Ativa';
        btnAtivarCamera.disabled = true;
        btnAtivarCamera.style.backgroundColor = '#4caf50';
    } catch (error) {
        alert('Não foi possível aceder à câmara. Verifique as permissões do browser.');
        console.error(error);
    }
});

// Formatação automática do CPF
const inputCpf = document.getElementById('cpf-paciente');
inputCpf.addEventListener('input', (e) => {
    let valor = e.target.value.replace(/\D/g, "");
    if (valor.length > 11) valor = valor.slice(0, 11);
    
    if (valor.length > 9) {
        valor = valor.replace(/^(\d{3})(\d{3})(\d{3})(\d{2}).*/, "$1.$2.$3-$4");
    } else if (valor.length > 6) {
        valor = valor.replace(/^(\d{3})(\d{3})(\d{3}).*/, "$1.$2.$3");
    } else if (valor.length > 3) {
        valor = valor.replace(/^(\d{3})(\d{3}).*/, "$1.$2");
    }
    e.target.value = valor;
});

// Lógica de submissão e Validação
const form = document.getElementById('consulta-form');
const divResultado = document.getElementById('resultado-validacao');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const codMedico = document.getElementById('cod-medico').value.trim();
    const codPaciente = document.getElementById('cod-paciente').value.trim();
    const cpfPaciente = inputCpf.value.trim();

    // 1. Validar se o médico existe
    if (!medicosAutorizados.includes(codMedico)) {
        mostrarMensagem('Erro: Código de médico não encontrado ou não autorizado.', 'erro');
        return;
    }

    // 2. Validar se o paciente existe na base de dados (código e CPF)
    const pacienteEncontrado = bancoDeDadosMock.find(
        p => p.codPaciente === codPaciente && p.cpf === cpfPaciente
    );

    if (pacienteEncontrado) {
        mostrarMensagem(`Sucesso! Paciente <strong>${pacienteEncontrado.nome}</strong> validado. Informações liberadas para o médico ${codMedico}.`, 'sucesso');
    } else {
        mostrarMensagem('Erro: Paciente não encontrado com o código e CPF informados.', 'erro');
    }
});

function mostrarMensagem(texto, tipo) {
    divResultado.className = `mensagem-oculta ${tipo}`;
    divResultado.innerHTML = texto;
}