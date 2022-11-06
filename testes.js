function calculaPorcentagemSorteio(assinante,minutosAssistidos) {
    const horasAssistidas = minutosAssistidos.map((valor) => {
      return Math.ceil(valor/60)
    })
    const pontuação = horasAssistidas.map((valor, index) => {
      return assinante[index] ? valor*2 : valor
    })
    const totalPontos = pontuação.reduce((acumulado, atual) => {
      return acumulado + atual
    })
    return pontuação.map((valor) => {
      return Math.round((valor/totalPontos)*100) })
    }