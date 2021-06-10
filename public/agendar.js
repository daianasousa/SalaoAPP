/*Envia as informações do produto*/
function DadosCadastro(){
    const form_cadastrar = document.getElementById('form-cadastrar')
    const input_nome = document.getElementById('nome')
    const input_telefone = document.getElementById('telefone')
    const input_diames = document.getElementById('dia_mes')
    const input_hora = document.getElementById('hora')
    const input_desejafazer = document.getElementById('deseja_fazer')

    form_cadastrar.onsubmit = async (event) =>{
        event.preventDefault()
        const nome = input_nome.value
        const telefone = input_telefone.value
        const diames = input_diames.value
        const hora = input_hora.value
        const desejafazer = input_desejafazer.value

        await axios.post('http://localhost:8000/agendamento',{
            nome: nome,
            telefone: telefone,
            dia_mes: diames,
            hora: hora,
            deseja_fazer: desejafazer
        })
        alert('Agendamento realizado!') 
    }
}

function App(){
    console.log('App Iniciada')
    DadosCadastro()   
}
App()