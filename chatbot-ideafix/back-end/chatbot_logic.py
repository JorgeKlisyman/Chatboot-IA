from models import resposta_padrao

def process_message(pergunta):
    pergunta = pergunta.lower().strip()

    if "adesivo" in pergunta:
        return "Oferecemos adesivos personalizados, decorativos, para carros e vitrines. Qual tipo você está procurando?"
    
    elif "orçamento" in pergunta or "preço" in pergunta:
        return "Claro! Para enviar um orçamento, precisamos saber o serviço desejado, medidas aproximadas e localização (se for instalação)."

    elif "serviços" in pergunta or "o que vocês fazem" in pergunta:
        return ("Oferecemos os seguintes serviços: adesivos personalizados, envelopamento de vitrines, fachadas comerciais, "
                "películas para vidro, banners, lonas, placas e muito mais.")

    elif "prazo" in pergunta or "quanto tempo" in pergunta:
        return "Nosso prazo de produção varia conforme o serviço. Por exemplo: adesivos personalizados levam 2 a 3 dias úteis. Instalações maiores, até 5 dias úteis."

    elif "pagamento" in pergunta:
        return "Aceitamos Pix, transferência bancária, boleto e cartão de crédito. Parcelamos em até 3x sem juros para valores acima de R$300."

    elif "entrega" in pergunta or "envio" in pergunta:
        return "Realizamos entregas em todo o Brasil via transportadora ou Correios. Em Recife e região, também oferecemos entrega via motoboy."

    elif "endereço" in pergunta or "onde fica" in pergunta:
        return "Estamos localizados na Av. Exemplo, 123 - Recife/PE. Atendemos com hora marcada. Deseja agendar uma visita?"

    elif "horário" in pergunta or "funcionamento" in pergunta:
        return "Funcionamos de segunda a sexta, das 8h às 17h. Aos sábados, atendimento mediante agendamento."

    elif "película" in pergunta:
        return "Trabalhamos com películas decorativas e de proteção solar para residências, comércios e veículos. Podemos mostrar modelos!"

    elif "fachada" in pergunta:
        return "Criamos fachadas em ACM, lona, PVC e outros materiais. Também fazemos instalação. Gostaria de enviar o nome do seu negócio?"

    elif "contato" in pergunta or "telefone" in pergunta:
        return "Você pode falar com a gente pelo WhatsApp: (81) 9 9999-9999 ou pelo e-mail contato@ideafix.com.br."

    elif "atende" in pergunta:
        return "Atendemos toda a região metropolitana de Recife. Para outras cidades, podemos combinar entrega e instalação dependendo da demanda."

    else:
        return resposta_padrao
