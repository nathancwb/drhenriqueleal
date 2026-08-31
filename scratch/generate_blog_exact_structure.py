# -*- coding: utf-8 -*-
import os, json

POSTS = [
    # 1. Harmonização Facial
    {
        "slug": "harmonizacao-facial-mitos-e-verdades-curitiba",
        "title": "Harmonização Facial em Curitiba: 7 Mitos e Verdades que Você Precisa Saber",
        "category": "Harmonização Facial",
        "excerpt": "Descubra o que é verdade e o que é mito sobre a harmonização facial. Entenda como o procedimento preserva a naturalidade e valoriza seus traços em Curitiba.",
        "cover": "assets/img/resultados/caso-harmonizacao-feminina-1.webp",
        "coverAlt": "Antes e depois de harmonização facial feminina com naturalidade em Curitiba",
        "date": "2026-08-15",
        "readingMinutes": 5,
        "tags": ["Harmonização Facial", "Curitiba", "Ácido Hialurônico", "Naturalidade"],
        "lead": "A busca por procedimentos estéticos que valorizam a beleza natural sem exageros tem crescido expressivamente em Curitiba. No entanto, muitas dúvidas e desinformações ainda cercam a harmonização facial.",
        "sections": [
            {
                "id": "secao-artificial",
                "navTitle": "A harmonização deixa o rosto artificial?",
                "title": "1. A harmonização facial deixa o rosto artificial?",
                "p1": "<strong>Mito.</strong> O objetivo da harmonização bem executada pelo Dr. Henrique Leal é exatamente o oposto: realçar a beleza anatômica e devolver proporções equilibradas de forma discreta e elegante.",
                "p2": "Quando realizada com planejamento milimétrico e respeito aos ângulos da face, as pessoas ao seu redor percebem apenas que você está com uma fisionomia mais jovem, descansada e iluminada, sem identificar que houve intervenção.",
                "figure": {
                    "src": "assets/img/harmonizacao-facial-nova.webp",
                    "alt": "Avaliação clínica de proporção áurea com Dr. Henrique Leal",
                    "caption": "Planejamento individualizado respeitando a proporção áurea e a mímica facial no Água Verde."
                }
            },
            {
                "id": "secao-reversivel",
                "navTitle": "O procedimento é definitivo ou reversível?",
                "title": "2. O procedimento é definitivo ou reversível?",
                "p1": "<strong>Verdade.</strong> Os preenchedores modernos utilizados no consultório, como o ácido hialurônico de padrão ouro, são biocompatíveis e absorvidos de forma natural pelo organismo em um período de 12 a 18 meses.",
                "p2": "Além disso, uma das maiores vantagens do ácido hialurônico é a sua total reversibilidade: caso o paciente deseje ajustes imediatos, é possível aplicar a enzima hialuronidase para dissolver o produto de forma rápida e segura.",
                "list": [
                    "Ácido hialurônico de alta pureza e biocompatibilidade",
                    "Absorção gradual e estímulo secundário de hidratação",
                    "Possibilidade de reversão rápida com hialuronidase se necessário",
                    "Manutenção programada sem sobrecarregar a estrutura facial"
                ]
            },
            {
                "id": "secao-estica-pele",
                "navTitle": "Harmonização estica a pele como cirurgia?",
                "title": "3. Harmonização facial estica a pele como cirurgia plástica?",
                "p1": "<strong>Mito.</strong> A harmonização não estica nem puxa a pele cirurgicamente. Ela atua repondo coxins de gordura reabsorvidos com o envelhecimento, estruturando o suporte ósseo (mandíbula e queixo) e bioestimulando colágeno.",
                "p2": "O efeito de rejuvenescimento surge da reestruturação volumétrica dos pontos de sustentação, devolvendo o formato de triângulo invertido típico da juventude.",
                "quote": {
                    "text": "A verdadeira harmonização não transforma quem você é, mas restaura proporções e sustentações perdidas, preservando 100% da sua essência.",
                    "author": "Dr. Henrique Leal Rosa"
                }
            },
            {
                "id": "secao-avaliacao",
                "navTitle": "Como escolher o profissional em Curitiba",
                "title": "4. Como escolher o profissional certo em Curitiba",
                "p1": "Em Curitiba, priorize profissionais com dupla formação e profundo domínio anatômico. O Dr. Henrique Leal une a precisão cirúrgica da Odontologia (CRO-PR) ao conhecimento de biologia tecidual da Biomedicina (CRBM-PR).",
                "p2": "Durante a consulta no Edifício Today's Office (Água Verde), realizamos a análise facial completa em repouso, fala e sorriso, garantindo que o resultado seja impecável sob qualquer ângulo."
            }
        ]
    },
    # 2. Harmonização Masculina
    {
        "slug": "harmonizacao-facial-masculina-guia-curitiba",
        "title": "Harmonização Facial Masculina: Como Definir Mandíbula e Queixo sem Perder a Naturalidade",
        "category": "Harmonização Facial",
        "excerpt": "Guia completo sobre a estruturação mandibular e do mento masculino. Linhas firmes, ângulo reto e sofisticação no consultório do Dr. Henrique Leal em Curitiba.",
        "cover": "assets/img/resultados/slider-caso-masculino-depois.webp",
        "coverAlt": "Perfil e contorno mandibular masculino após harmonização facial em Curitiba",
        "date": "2026-08-10",
        "readingMinutes": 6,
        "tags": ["Harmonização Masculina", "Mandíbula", "Mento", "Curitiba"],
        "lead": "Cada vez mais homens em Curitiba buscam a harmonização facial para valorizar traços marcantes, conferir autoridade à fisionomia e definir o contorno do terço inferior do rosto sem parecerem operados.",
        "sections": [
            {
                "id": "secao-diferencas",
                "navTitle": "Diferenças da harmonização masculina",
                "title": "O que diferencia a harmonização masculina da feminina?",
                "p1": "A face masculina possui características anatômicas únicas: formato mais quadrado, ângulo mandibular próximo a 90 graus e queixo reto e projetado na mesma largura dos lábios.",
                "p2": "O planejamento do Dr. Henrique Leal foca exclusivamente em reforçar essas linhas de força sem projetar maçãs do rosto ou estreitar o queixo, preservando a virilidade e elegância natural.",
                "figure": {
                    "src": "assets/img/resultados/caso-contorno-mandibular-1.webp",
                    "alt": "Antes e depois de contorno mandibular masculino em Curitiba",
                    "caption": "Definição do ângulo da mandíbula e mento com ácido hialurônico de alta sustentação."
                }
            },
            {
                "id": "secao-procedimento",
                "navTitle": "Como é realizado o procedimento",
                "title": "Como é a sessão no consultório",
                "p1": "O procedimento é minimamente invasivo, realizado com microcânulas de ponta romba que não cortam vasos sanguíneos, minimizando o risco de hematomas.",
                "p2": "Utilizamos anestesia local odontológica para proporcionar conforto absoluto. A sessão dura cerca de 45 minutos e o paciente pode retornar ao trabalho no mesmo dia.",
                "list": [
                    "Anestesia local sem dor",
                    "Aplicação com microcânula segura",
                    "Sem cortes ou cicatrizes",
                    "Retorno imediato às atividades profissionais"
                ]
            },
            {
                "id": "secao-durabilidade",
                "navTitle": "Durabilidade e manutenção",
                "title": "Quanto tempo dura o resultado no homem?",
                "p1": "Devido à densidade do produto utilizado para estruturação óssea, os resultados costumam durar de 14 a 18 meses.",
                "p2": "Homens que praticam esportes de alta intensidade podem realizar manutenções leves a cada 12 meses para manter o contorno sempre afiado e definido.",
                "quote": {
                    "text": "O objetivo na face masculina é conferir autoridade, definição e firmeza, sem transformar os traços que fazem de você quem você é.",
                    "author": "Dr. Henrique Leal Rosa"
                }
            }
        ]
    },
    # 3. Botox Preventivo
    {
        "slug": "botox-preventivo-quando-comecar-curitiba",
        "title": "Botox Preventivo em Curitiba: Qual a Idade Certa para Começar?",
        "category": "Toxina Botulínica",
        "excerpt": "Entenda o conceito de toxina botulínica preventiva, como evitar que rugas de expressão se tornem marcas profundas na pele e os cuidados essenciais.",
        "cover": "assets/img/botox-nova.webp",
        "coverAlt": "Dr. Henrique Leal aplicando toxina botulínica em consultório em Curitiba",
        "date": "2026-08-04",
        "readingMinutes": 4,
        "tags": ["Botox", "Prevenção", "Rugas de Expressão", "Curitiba"],
        "lead": "A aplicação preventiva de toxina botulínica tornou-se um dos cuidados dermatológicos e estéticos mais procurados por jovens adultos em Curitiba que desejam envelhecer com viço e elegância.",
        "sections": [
            {
                "id": "secao-conceito",
                "navTitle": "O que é o Botox Preventivo?",
                "title": "O que é e como funciona o Botox Preventivo?",
                "p1": "Diferente da aplicação corretiva (feita quando as rugas já estão estáticas e visíveis mesmo com o rosto relaxado), o Botox preventivo relaxa suavemente os músculos hiperativos antes que a pele sofra fratura dérmica.",
                "p2": "Com microdoses personalizadas, evitamos que o ato de franzir a testa ao sol ou sorrir fortemente forme vincos permanentes no futuro.",
                "figure": {
                    "src": "assets/img/resultados/slider-caso-botox-depois.webp",
                    "alt": "Resultado natural de botox preventivo na testa e olhos",
                    "caption": "Testa lisa, sobrancelhas arqueadas com leveza e expressão totalmente preservada."
                }
            },
            {
                "id": "secao-idade",
                "navTitle": "Idade ideal para iniciar",
                "title": "Qual a idade certa para começar?",
                "p1": "Em média, a partir dos 25 aos 28 anos, momento em que a produção natural de colágeno desacelera e as primeiras linhas dinâmicas começam a marcar.",
                "p2": "No entanto, pessoas muito expressivas ou com pele clara exposta frequentemente à luz solar podem iniciar a avaliação preventiva mais cedo.",
                "list": [
                    "Previne a fixação de rugas na glabela (entre as sobrancelhas)",
                    "Suaviza linhas de 'pés de galinha' sem congelar o sorriso",
                    "Mantém o arqueamento elegante e natural do olhar",
                    "Economiza procedimentos invasivos no futuro"
                ]
            }
        ]
    },
    # 4. Durabilidade do Botox
    {
        "slug": "quanto-tempo-dura-o-botox-curitiba",
        "title": "Quanto Tempo Dura o Botox na Testa e Olhos? Dicas para Prolongar o Efeito",
        "category": "Toxina Botulínica",
        "excerpt": "Descubra fatores que influenciam na durabilidade da toxina botulínica e como manter seu rosto descansado e sem rugas por mais tempo em Curitiba.",
        "cover": "assets/img/resultados/botox-testa-depois.webp",
        "coverAlt": "Antes e depois de toxina botulínica na testa e glabela em Curitiba",
        "date": "2026-07-28",
        "readingMinutes": 5,
        "tags": ["Botox", "Durabilidade", "Testa e Olhos", "Cuidados"],
        "lead": "Uma das perguntas mais frequentes no consultório em Curitiba é: afinal, quantos meses dura o efeito do Botox e como fazer para que ele dure o máximo possível?",
        "sections": [
            {
                "id": "secao-duracao-media",
                "navTitle": "Tempo médio de durabilidade",
                "title": "Qual o tempo médio de duração da toxina botulínica?",
                "p1": "O efeito da toxina começa a ser notado em 48 a 72 horas, atinge o ápice por volta do 15º dia e se mantém estável por um período de 4 a 6 meses.",
                "p2": "Após esse período, as terminações nervosas voltam a se conectar gradativamente com o músculo, restaurando a mímica original de forma gradual e segura.",
                "figure": {
                    "src": "assets/img/resultados/botox-glabela-depois.webp",
                    "alt": "Suavização das rugas da glabela com toxina botulínica",
                    "caption": "Efeito de relaxamento muscular sem perda da expressividade no consultório do Água Verde."
                }
            },
            {
                "id": "secao-fatores",
                "navTitle": "Fatores que afetam a duração",
                "title": "O que faz o Botox durar mais ou menos tempo?",
                "p1": "Atletas de alto rendimento e praticantes de musculação intensa possuem metabolismo acelerado, o que pode reduzir a durabilidade para 3 a 4 meses.",
                "p2": "Por outro lado, o uso de marcas padrão ouro (como Dysport e Botox Allergan) com diluição e dosagem corretas garante a máxima fixação biológica possível.",
                "list": [
                    "Evitar massagear ou deitar nas primeiras 4 horas após aplicação",
                    "Usar protetor solar com alto fator de proteção diariamente",
                    "Manter suplementação de zinco e hidratação cutânea em dia",
                    "Evitar calor excessivo (sauna intensa) nos primeiros dias"
                ]
            }
        ]
    },
    # 5. Fios de PDO
    {
        "slug": "fios-de-pdo-lifting-sem-cirurgia-curitiba",
        "title": "Fios de PDO em Curitiba: Como Funciona o Lifting Facial sem Cortes",
        "category": "Fios de PDO",
        "excerpt": "Conheça a tecnologia dos fios de polidioxanona (PDO), técnica internacional aprendida na Coreia do Sul para reposicionar tecidos e estimular colágeno.",
        "cover": "assets/img/foto-fios-nova.webp",
        "coverAlt": "Dr. Henrique Leal aplicando fios de sustentação PDO em Curitiba",
        "date": "2026-07-20",
        "readingMinutes": 6,
        "tags": ["Fios de PDO", "Lifting Facial", "Coreia do Sul", "Curitiba"],
        "lead": "Os fios de sustentação de PDO (Polidioxanona) representam uma das maiores inovações da estética regenerativa mundial, proporcionando tração tecidual imediata e estímulo biológico contínuo de colágeno sem a necessidade de cirurgias ou internações.",
        "sections": [
            {
                "id": "secao-como-funciona",
                "navTitle": "Como os fios atuam no rosto",
                "title": "Como os Fios de PDO agem na pele?",
                "p1": "Fabricados com polidioxanona (material biocompatível e absorvível), os fios são inseridos na camada subcutânea por meio de microcânulas especiais.",
                "p2": "Os fios de tração (espiculados) possuem microgarras que ancoram a derme caída, tracionando o terço médio (bochechas), sulco nasogeniano ('bigode chinês') e linha da mandíbula.",
                "figure": {
                    "src": "assets/img/foto-fios.webp",
                    "alt": "Aplicação precisa de fios de PDO no consultório",
                    "caption": "Procedimento realizado sob anestesia local em ambiente seguro e confortável."
                }
            },
            {
                "id": "secao-tipos-fios",
                "navTitle": "Fios de Tração vs Fios de Estímulo",
                "title": "Qual a diferença entre fios espiculados e fios lisos?",
                "p1": "Os <strong>fios espiculados</strong> são destinados ao efeito lifting mecânico imediato, reposicionando a gordura facial que cedeu com o tempo.",
                "p2": "Já os <strong>fios lisos</strong> formam uma malha dérmica que não traciona, mas estimula uma produção massiva de colágeno em áreas de pele fina, como olheiras e código de barras.",
                "list": [
                    "Lifting não cirúrgico imediato",
                    "Estímulo prolongado de colágeno tipo I e III por até 2 anos",
                    "Absorção completa do fio em 6 a 8 meses",
                    "Sem cortes, pontos ou cicatrizes visíveis"
                ]
            }
        ]
    },
    # 6. Fios vs Bioestimulador
    {
        "slug": "fios-de-pdo-ou-bioestimulador-qual-escolher",
        "title": "Fios de PDO ou Bioestimulador de Colágeno: Qual o Ideal para o Seu Rosto?",
        "category": "Fios de PDO",
        "excerpt": "Comparativo completo entre fios de tração e bioestimuladores injetáveis para tratar flacidez e perda de contorno facial em Curitiba.",
        "cover": "assets/img/resultados/caso-rejuvenescimento-facial-1.webp",
        "coverAlt": "Caso de rejuvenescimento facial completo com fios de PDO e bioestimulador",
        "date": "2026-07-14",
        "readingMinutes": 5,
        "tags": ["Fios de PDO", "Bioestimuladores", "Flacidez", "Comparativo"],
        "lead": "Tanto os Fios de PDO quanto os Bioestimuladores de Colágeno são tecnologias consagradas no combate ao envelhecimento, mas cada uma atua em uma camada e com propósitos biomecânicos diferentes.",
        "sections": [
            {
                "id": "secao-comparativo",
                "navTitle": "Lifting mecânico vs Qualidade da pele",
                "title": "Lifting mecânico imediato vs Estímulo gradual de firmeza",
                "p1": "Se a sua principal queixa for a sensação de 'rosto derretendo', bochecha caída e perda da linha mandibular, os <strong>Fios de PDO</strong> proporcionam tração física instantânea.",
                "p2": "Se a sua queixa for a perda de espessura da pele, textura fina, 'craquelado' e flacidez difusa, os <strong>Bioestimuladores Injetáveis</strong> (Sculptra, Radiesse, Elleva) promovem o espessamento celular progressivo.",
                "figure": {
                    "src": "assets/img/bioestimulador-de-colageno.webp",
                    "alt": "Bioestimulador de colágeno injetável",
                    "caption": "Aplicação vetorizada de bioestimuladores para redensificação dérmica profunda."
                }
            },
            {
                "id": "secao-associacao",
                "navTitle": "A associação dos tratamentos",
                "title": "Por que associar Fios de PDO e Bioestimuladores?",
                "p1": "Na clínica do Dr. Henrique Leal em Curitiba, a combinação das duas técnicas é o padrão ouro: os fios reposicionam as estruturas caídas e o bioestimulador ancora a pele no novo lugar com firmeza biológica duradoura."
            }
        ]
    },
    # 7. Sculptra, Radiesse, Elleva
    {
        "slug": "sculptra-radiesse-elleva-comparativo-curitiba",
        "title": "Sculptra, Radiesse e Elleva: Diferenças entre os Melhores Bioestimuladores de Colágeno",
        "category": "Bioestimuladores",
        "excerpt": "Análise comparativa das principais marcas de bioestimuladores de colágeno do mercado. Saiba como escolher o melhor tratamento em Curitiba.",
        "cover": "assets/img/bioestimulador-de-colageno.webp",
        "coverAlt": "Frascos e tecnologia de bioestimuladores de colágeno em Curitiba",
        "date": "2026-07-05",
        "readingMinutes": 6,
        "tags": ["Sculptra", "Radiesse", "Elleva", "Bioestimuladores", "Curitiba"],
        "lead": "A partir dos 25 anos, perdemos aproximadamente 1% de colágeno anualmente. Os bioestimuladores injetáveis são a ferramenta médica mais potente para reverter essa perda de maneira biológica e duradoura.",
        "sections": [
            {
                "id": "secao-sculptra-elleva",
                "navTitle": "Sculptra e Elleva (PLLA)",
                "title": "1. Sculptra e Elleva (Ácido Poli-L-Láctico)",
                "p1": "Compostos por micropartículas biocompatíveis de PLLA, agem como potentes indutores biológicos que ativam os fibroblastos a sintetizarem colágeno tipo I novo ao longo de 90 dias.",
                "p2": "São indicados para tratar flacidez generalizada no rosto, pescoço, colo e glúteos, com durabilidade clínica que pode ultrapassar 24 meses.",
                "figure": {
                    "src": "assets/img/resultados/slider-caso-rejuvenescimento-depois.webp",
                    "alt": "Pele firme e rejuvenescida com bioestimuladores de colágeno",
                    "caption": "Rejuvenescimento natural com melhora evidente da elasticidade e firmeza facial."
                }
            },
            {
                "id": "secao-radiesse",
                "navTitle": "Radiesse (Hidroxiapatita de Cálcio)",
                "title": "2. Radiesse (Hidroxiapatita de Cálcio)",
                "p1": "Composto por microesferas de CaHA suspensas em gel carreador. Além do estímulo biológico potente de colágeno e elastina, oferece um efeito imediato de firmeza e ancoragem.",
                "p2": "Excelente para contorno mandibular, melhora da papada e rejuvenescimento do dorso das mãos com veias aparentes."
            }
        ]
    },
    # 8. Flacidez Rosto e Pescoço
    {
        "slug": "como-tratar-flacidez-facial-pescoco-curitiba",
        "title": "Como Tratar Flacidez no Rosto e Pescoço com Bioestimuladores em Curitiba",
        "category": "Bioestimuladores",
        "excerpt": "Dicas clínicas e protocolos modernos para recuperar a firmeza do pescoço, papada e contorno facial sem cirurgia.",
        "cover": "assets/img/resultados/caso-rejuvenescimento-facial-1-depois.webp",
        "coverAlt": "Contorno facial e pescoço rejuvenescidos com bioestimuladores",
        "date": "2026-06-28",
        "readingMinutes": 5,
        "tags": ["Pescoço", "Flacidez", "Rejuvenescimento", "Bioestimuladores"],
        "lead": "O pescoço e a linha da mandíbula frequentemente denunciam o envelhecimento antes do restante da face, pois possuem pele fina e baixa densidade de glândulas sebáceas.",
        "sections": [
            {
                "id": "secao-causas",
                "navTitle": "Por que o pescoço perde firmeza?",
                "title": "Por que a pele do pescoço perde sustentação?",
                "p1": "Além da degradação biológica do colágeno, o hábito moderno de olhar constantemente para telas (o chamado 'tech neck') acelera o surgimento de colares horizontais e flacidez na papada.",
                "p2": "O tratamento com bioestimuladores injetáveis vetorizados devolve a espessura dérmica, criando um 'efeito espartilho' natural que firma a pele frouxa.",
                "figure": {
                    "src": "assets/img/resultados/facial-completo.webp",
                    "alt": "Perfil facial rejuvenescido no consultório do Dr. Henrique Leal",
                    "caption": "Reestruturação anatômica integrada no bairro Água Verde em Curitiba."
                }
            }
        ]
    },
    # 9. Natural Lips
    {
        "slug": "preenchimento-labial-natural-lips-curitiba",
        "title": "Preenchimento Labial Natural Lips em Curitiba: Lábios Hidratados e sem Exageros",
        "category": "Preenchimento Labial",
        "excerpt": "Descubra a técnica Natural Lips do Dr. Henrique Leal: contorno sutil, hidratação profunda e respeito à anatomia da sua boca.",
        "cover": "assets/img/resultados/labio-antes-depois-3.webp",
        "coverAlt": "Antes e depois de preenchimento labial natural lips em Curitiba",
        "date": "2026-06-20",
        "readingMinutes": 4,
        "tags": ["Preenchimento Labial", "Natural Lips", "Ácido Hialurônico", "Curitiba"],
        "lead": "O receio de ficar com lábios exagerados ou artificiais ('efeito bico de pato') ainda afasta muitas mulheres do preenchimento. O conceito Natural Lips foi desenvolvido pelo Dr. Henrique Leal exatamente para superar esse medo.",
        "sections": [
            {
                "id": "secao-metodo",
                "navTitle": "O método Natural Lips",
                "title": "O que caracteriza o método Natural Lips?",
                "p1": "O foco não é injetar grandes volumes, mas sim desenhar com precisão o contorno do arco do cupido, evertir sutilmente a mucosa e hidratar as camadas internas com ácido hialurônico fluido de alta maleabilidade.",
                "p2": "Respeitamos a proporção áurea clássica (1 parte de volume no lábio superior para 1,6 partes no lábio inferior), garantindo harmonia no repouso e no sorriso.",
                "figure": {
                    "src": "assets/img/resultados/labio-resultado-4.webp",
                    "alt": "Lábios naturais, hidratados e sem excesso de volume",
                    "caption": "Resultado suave com contorno definido e brilho natural."
                }
            }
        ]
    },
    # 10. Cuidados Pós Preenchimento Labial
    {
        "slug": "cuidados-pos-preenchimento-labial-guia",
        "title": "Cuidados Pós-Preenchimento Labial: Recuperação, Inchaço e Duração",
        "category": "Preenchimento Labial",
        "excerpt": "O que fazer e o que evitar nos primeiros dias após o preenchimento labial para garantir uma cicatrização perfeita.",
        "cover": "assets/img/preenchimento-labial-depois-clean.webp",
        "coverAlt": "Lábios após preenchimento labial no consultório em Curitiba",
        "date": "2026-06-12",
        "readingMinutes": 4,
        "tags": ["Pós-Procedimento", "Preenchimento Labial", "Cuidados", "Inchaço"],
        "lead": "Os primeiros dias após o preenchimento labial exigem cuidados simples para que o ácido hialurônico se acomode perfeitamente nos tecidos e o edema inicial diminua com rapidez.",
        "sections": [
            {
                "id": "secao-linha-do-tempo",
                "navTitle": "Linha do tempo do inchaço",
                "title": "O que acontece nos primeiros dias?",
                "p1": "Nas primeiras 48 horas, é totalmente normal haver inchaço e leve sensibilidade ao toque. O resultado que você vê no primeiro dia ainda não é o definitivo.",
                "p2": "A partir do 5º ao 7º dia o edema regride cerca de 70%, e o formato final consolidado se estabelece entre 15 e 20 dias.",
                "list": [
                    "Fazer compressas frias leves nas primeiras 24 horas",
                    "Evitar alimentos excessivamente quentes ou condimentados no dia do procedimento",
                    "Não pressionar os lábios ou usar canudos nas primeiras 48 horas",
                    "Evitar atividade física pesada nas primeiras 24 a 48 horas"
                ],
                "figure": {
                    "src": "assets/img/resultados/labio-resultado-5.webp",
                    "alt": "Lábios cicatrizados com formato harmônico",
                    "caption": "Resultado consolidado após 15 dias de cicatrização."
                }
            }
        ]
    },
    # 11. Rinomodelação
    {
        "slug": "rinomodelacao-com-acido-hialuronico-curitiba",
        "title": "Rinomodelação em Curitiba: Como Empinar e Alinhar o Nariz sem Cirurgia",
        "category": "Rinomodelação",
        "excerpt": "Procedimento rápido e seguro para corrigir pequenas imperfeições no dorso nasal e levantar a ponta caída em Curitiba.",
        "cover": "assets/img/resultados/upnose-depois.webp",
        "coverAlt": "Antes e depois de rinomodelação up nose em Curitiba",
        "date": "2026-06-04",
        "readingMinutes": 5,
        "tags": ["Rinomodelação", "Up Nose", "Nariz", "Curitiba"],
        "lead": "A rinomodelação não cirúrgica é uma excelente alternativa à rinoplastia tradicional para pacientes que desejam empinar a ponta do nariz e disfarçar o ossinho saliente (giba) sem cortes ou anestesia geral.",
        "sections": [
            {
                "id": "secao-indicacoes",
                "navTitle": "O que a rinomodelação corrige",
                "title": "Quais queixas a rinomodelação consegue resolver?",
                "p1": "Com microdoses de ácido hialurônico de alta sustentação, conseguimos retificar o dorso nasal, camuflando a curvatura do osso e criando a ilusão óptica de um nariz mais reto e afilado.",
                "p2": "Além disso, através do protocolo Up Nose, estruturamos a base da columela para erguer a ponta caída ao sorrir.",
                "figure": {
                    "src": "assets/img/resultados/caso-rinomodelacao-perfil-1.webp",
                    "alt": "Perfil nasal alinhado com rinomodelação não cirúrgica",
                    "caption": "Correção de giba nasal e sustentação da ponta em sessão única de 30 minutos."
                }
            }
        ]
    },
    # 12. Rinomodelação Dúvidas
    {
        "slug": "rinomodelacao-doi-cuidados-e-duracao",
        "title": "Rinomodelação Dói? Riscos, Tempo de Recuperação e Durabilidade",
        "category": "Rinomodelação",
        "excerpt": "Tudo sobre o nível de dor, anestesia local, cuidados essenciais e tempo de durabilidade da rinomodelação.",
        "cover": "assets/img/resultados/caso-rinomodelacao-perfil-1-depois.webp",
        "coverAlt": "Nariz empinado e alinhado após rinomodelação",
        "date": "2026-05-28",
        "readingMinutes": 4,
        "tags": ["Rinomodelação", "Dúvidas", "Segurança", "Durabilidade"],
        "lead": "A rinomodelação é um dos procedimentos com maior impacto visual imediato, mas exige rigor técnico e segurança anatômica máxima por parte do profissional.",
        "sections": [
            {
                "id": "secao-seguranca",
                "navTitle": "Segurança e anestesia",
                "title": "A rinomodelação dói e é segura?",
                "p1": "Não dói: aplicamos anestésico local no ponto de entrada. Utilizamos microcânula flexível e sem ponta cortante, o que protege os vasos sanguíneos da região nasal.",
                "p2": "A durabilidade média é de 12 a 18 meses, pois o nariz é uma área de pouca mobilidade muscular, preservando o produto por mais tempo.",
                "figure": {
                    "src": "assets/img/resultados/upnose-antes.webp",
                    "alt": "Avaliação de perfil nasal no consultório",
                    "caption": "Estudo anatômico das proporções do dorso e ângulo nasolabial."
                }
            }
        ]
    },
    # 13. Estética Íntima Preenchimento
    {
        "slug": "estetica-intima-preenchimento-acido-hialuronico-curitiba",
        "title": "Preenchimento Íntimo Feminino em Curitiba: Como o Ácido Hialurônico Devolve Firmeza e Conforto",
        "category": "Estética Íntima",
        "excerpt": "Procedimento médico-estético delicado para recuperação de volume, hidratação e firmeza dos grandes lábios com total sigilo e conforto.",
        "cover": "assets/img/intimos-nova.webp",
        "coverAlt": "Estética íntima feminina no consultório do Dr. Henrique Leal em Curitiba",
        "date": "2026-05-20",
        "readingMinutes": 5,
        "tags": ["Estética Íntima", "Preenchimento Íntimo", "Curitiba", "Autoestima"],
        "lead": "Com o passar dos anos, emagrecimento severo ou oscilações hormonais na menopausa, a região genital feminina perde volume nos grandes lábios, gerando flacidez, atrito desconfortável com roupas e queda da autoestima.",
        "sections": [
            {
                "id": "secao-procedimento-intimo",
                "navTitle": "Como funciona o preenchimento íntimo",
                "title": "Como o ácido hialurônico atua na estética íntima?",
                "p1": "A aplicação de ácido hialurônico específico na derme dos grandes lábios restaura o turgor, protege as estruturas internas e rejuvenesce o aspecto visual da região íntima.",
                "p2": "No consultório em Curitiba, o procedimento é realizado com anestesia local, em ambiente estéril e com total sigilo e respeito ao conforto da paciente.",
                "figure": {
                    "src": "assets/img/intimos.webp",
                    "alt": "Cuidado e bem-estar na estética íntima feminina",
                    "caption": "Tratamento seguro e acolhedor para a saúde e autoestima da mulher."
                }
            }
        ]
    },
    # 14. Rejuvenescimento Íntimo
    {
        "slug": "rejuvenescimento-intimo-beneficios-e-autoestima",
        "title": "Rejuvenescimento Íntimo: Procedimentos Modernos para Saúde e Autoestima da Mulher",
        "category": "Estética Íntima",
        "excerpt": "Bioestimuladores, hidratação e fios na estética íntima: conheça os tratamentos que unem bem-estar, função e beleza.",
        "cover": "assets/img/intimos.webp",
        "coverAlt": "Procedimentos modernos de rejuvenescimento íntimo em Curitiba",
        "date": "2026-05-12",
        "readingMinutes": 5,
        "tags": ["Rejuvenescimento Íntimo", "Saúde Feminina", "Bioestimulador"],
        "lead": "O autocuidado íntimo moderno une tratamentos avançados de bioestímulo, preenchimento e clareamento para devolver conforto funcional e autoconfiança plena à mulher.",
        "sections": [
            {
                "id": "secao-opcoes-intimas",
                "navTitle": "Opções de tratamentos íntimos",
                "title": "Quais tratamentos podem ser associados?",
                "p1": "Além do ácido hialurônico para volume, podemos utilizar bioestimuladores de colágeno para combater a flacidez cutânea da vulva e clareamento para manchas decorrentes de depilação ou atrito.",
                "p2": "A avaliação presencial é o momento de tirar todas as dúvidas com tranquilidade e definir o plano de cuidados mais adequado.",
                "figure": {
                    "src": "assets/img/intimos-nova.webp",
                    "alt": "Consultório acolhedor e seguro em Curitiba",
                    "caption": "Atendimento humanizado com foco na sua saúde e bem-estar."
                }
            }
        ]
    },
    # 15. Protocolo Bioforce
    {
        "slug": "protocolo-bioforce-regeneracao-celular-curitiba",
        "title": "Protocolo Bioforce: O Tratamento Assinatura para Regeneração Facial Profunda",
        "category": "Protocolo Bioforce",
        "excerpt": "Associação exclusiva de bioestimuladores de última geração e peptídeos bioativos desenvolvida pelo Dr. Henrique Leal em Curitiba.",
        "cover": "assets/img/7G1A9991.webp",
        "coverAlt": "Dr. Henrique Leal Rosa no consultório em Curitiba",
        "date": "2026-05-04",
        "readingMinutes": 5,
        "tags": ["Protocolo Bioforce", "Regeneração", "Assinatura", "Curitiba"],
        "lead": "O Protocolo Bioforce é a assinatura clínica do Dr. Henrique Leal em Curitiba, desenvolvido para quem busca rejuvenescimento biológico profundo, viço incomparável e firmeza dérmica sem nenhum aspecto volumizado artificial.",
        "sections": [
            {
                "id": "secao-sinergia",
                "navTitle": "A ciência do Protocolo Bioforce",
                "title": "A sinergia entre Bioestimulação e Fatores Regenerativos",
                "p1": "O protocolo associa bioestimuladores importados de última geração com fatores de crescimento e peptídeos sinalizadores celulares.",
                "p2": "Essa combinação reprograma a atividade dos fibroblastos, promovendo uma neocolagênese acelerada que melhora poros, linhas finas e o tônus da pele em poucas semanas.",
                "figure": {
                    "src": "assets/img/henrique-portrait.webp",
                    "alt": "Dr. Henrique Leal Rosa - Cirurgião Dentista e Biomédico",
                    "caption": "Atendimento exclusivo no Edifício Today's Office, bairro Água Verde em Curitiba."
                }
            }
        ]
    },
    # 16. Peptídeos Bioativos
    {
        "slug": "peptideos-bioativos-e-antiaging-avancado",
        "title": "Peptídeos Bioativos na Estética Avançada: Como Estimular a Juventude da Pele",
        "category": "Protocolo Bioforce",
        "excerpt": "A ciência por trás dos peptídeos sinalizadores e como eles reprogramam a síntese de colágeno nas células da pele.",
        "cover": "assets/img/henrique-portrait.webp",
        "coverAlt": "Dr. Henrique Leal explicando a ciência dos peptídeos bioativos",
        "date": "2026-04-26",
        "readingMinutes": 4,
        "tags": ["Peptídeos", "Ciência", "Antiaging", "Regeneração"],
        "lead": "A estética moderna evoluiu da simples reposição volumétrica para a reprogramação celular inteligente através de biomoléculas sinalizadoras.",
        "sections": [
            {
                "id": "secao-peptideos",
                "navTitle": "Como os peptídeos funcionam",
                "title": "O papel dos peptídeos na matriz extracelular",
                "p1": "Os peptídeos bioativos atuam como 'chaves' químicas que ligam os receptores de membrana das células da pele, estimulando a síntese autóloga de ácido hialurônico, colágeno e elastina.",
                "p2": "O resultado é uma pele biologicamente mais jovem, densa e luminosa, com textura sedosa e viço saudável.",
                "figure": {
                    "src": "assets/img/dr-henrique.webp",
                    "alt": "Consulta estética com base em evidências científicas",
                    "caption": "Biotecnologia aplicada ao rejuvenescimento natural da face."
                }
            }
        ]
    },
    # 17. Ozonioterapia Benefícios
    {
        "slug": "ozonioterapia-beneficios-estetica-saude-curitiba",
        "title": "Ozonioterapia em Curitiba: Benefícios do Ozônio Medicinal para Pele e Inflamação",
        "category": "Ozonioterapia",
        "excerpt": "Como o gás ozônio atua na oxigenação celular, combate a radicais livres e potencialização de resultados estéticos em Curitiba.",
        "cover": "assets/img/henrique-clinic.webp",
        "coverAlt": "Sala de atendimento e consultório de ozonioterapia em Curitiba",
        "date": "2026-04-18",
        "readingMinutes": 5,
        "tags": ["Ozonioterapia", "Ozônio Medicinal", "Saúde", "Curitiba"],
        "lead": "A ozonioterapia medicinal é uma das práticas integrativas mais consagradas para melhora da microcirculação tecidual, combate a processos inflamatórios e revitalização da pele.",
        "sections": [
            {
                "id": "secao-ozonio-beneficios",
                "navTitle": "Aplicações do ozônio medicinal",
                "title": "Como o ozônio atua no organismo?",
                "p1": "A mistura de oxigênio-ozônio medicinal estimula as enzimas antioxidantes endógenas, combate bactérias e fungos, e melhora a liberação de oxigênio pelos glóbulos vermelhos nos tecidos periféricos.",
                "p2": "Na estética, é excelente para controle da acne ativa, revitalização cutânea e tratamento de celulite e gordura localizada.",
                "figure": {
                    "src": "assets/img/henrique-faq-new.webp",
                    "alt": "Avaliação e esclarecimento de dúvidas com Dr. Henrique Leal",
                    "caption": "Protocolos personalizados de ozonioterapia no consultório em Curitiba."
                }
            }
        ]
    },
    # 18. Ozonioterapia Pós Procedimento
    {
        "slug": "ozonioterapia-para-rejuvenescimento-e-cicatrizacao",
        "title": "Ozonioterapia no Pós-Procedimento: Aceleração da Cicatrização e Oxigenação Tecidual",
        "category": "Ozonioterapia",
        "excerpt": "Entenda por que o ozônio medicinal é utilizado para acelerar a recuperação de procedimentos estéticos e reduzir edemas.",
        "cover": "assets/img/henrique-faq-new.webp",
        "coverAlt": "Dr. Henrique Leal orientando paciente sobre pós-procedimento",
        "date": "2026-04-10",
        "readingMinutes": 4,
        "tags": ["Cicatrização", "Pós-Operatório", "Ozonioterapia"],
        "lead": "A aplicação do ozônio medicinal após procedimentos estéticos reduz expressivamente o tempo de edema, equimoses (roxos) e acelera a regeneração tecidual.",
        "sections": [
            {
                "id": "secao-cicatrizacao",
                "navTitle": "Aceleração da cicatrização",
                "title": "Por que o ozônio acelera a recuperação pós-estética?",
                "p1": "O ozônio promove a liberação imediata de óxido nítrico e fatores de crescimento endotelial, acelerando a vascularização e desinflamando a área tratada rapidamente.",
                "p2": "Isso proporciona ao paciente um pós-procedimento muito mais confortável, seguro e com retorno antecipado às suas atividades cotidianas.",
                "figure": {
                    "src": "assets/img/henrique-clinic.webp",
                    "alt": "Ambiente clínico seguro e esterilizado",
                    "caption": "Segurança e conforto para uma recuperação tranquila e rápida."
                }
            }
        ]
    },
    # 19. Terapia Capilar
    {
        "slug": "terapia-capilar-para-queda-de-cabelo-curitiba",
        "title": "Terapia Capilar em Curitiba: Como Tratar Queda de Cabelo e Calvície com Tecnologia",
        "category": "Terapia Capilar",
        "excerpt": "Protocolos integrados de estímulo folicular, nutrição capilar e combate à calvície masculina e feminina no Água Verde.",
        "cover": "assets/img/resultados/IMG_6808.webp",
        "coverAlt": "Tratamento de terapia capilar e recuperação dos fios em Curitiba",
        "date": "2026-04-02",
        "readingMinutes": 5,
        "tags": ["Terapia Capilar", "Queda de Cabelo", "Calvície", "Curitiba"],
        "lead": "A queda excessiva de cabelo (eflúvio telógeno) e a calvície genética (alopecia androgenética) afetam diretamente a autoestima. O tratamento precoce no consultório é decisivo para salvar os folículos pilosos antes que atrofiem definitivamente.",
        "sections": [
            {
                "id": "secao-protocolo-capilar",
                "navTitle": "Protocolo capilar integrado",
                "title": "Como funciona o tratamento capilar clínico?",
                "p1": "O protocolo do Dr. Henrique Leal em Curitiba combina microinfusão de medicamentos antiqueda (MMP), fatores de crescimento peptídicos e bioestimulação folicular.",
                "p2": "Esse combo desinflama a raiz do cabelo, bloqueia os efeitos locais da DHT e estimula a transição dos fios da fase de repouso (telógena) para a fase de crescimento ativo (anágena).",
                "figure": {
                    "src": "assets/img/resultados/IMG_4637.webp",
                    "alt": "Densidade capilar recuperada com estímulo folicular",
                    "caption": "Aumento significativo da densidade e calibre dos fios no consultório."
                }
            }
        ]
    },
    # 20. Microinfusão Capilar
    {
        "slug": "microinfusao-capilar-e-fortalecimento-dos-fios",
        "title": "Microinfusão e Fatores de Crescimento Capilar: Fortalecimento desde a Raiz",
        "category": "Terapia Capilar",
        "excerpt": "Entenda como a entrega direta de nutrientes no bulbo capilar desacelera o afinamento e estimula novos fios.",
        "cover": "assets/img/resultados/IMG_9716.webp",
        "coverAlt": "Microinfusão capilar no couro cabeludo com ativos antiqueda",
        "date": "2026-03-24",
        "readingMinutes": 4,
        "tags": ["Microinfusão", "Fatores de Crescimento", "Bulbo Capilar"],
        "lead": "A entrega direta de nutrientes e substâncias vasodilatadoras no bulbo capilar garante uma absorção centenas de vezes superior à de loções tópicas ou comprimidos orais.",
        "sections": [
            {
                "id": "secao-microinfusao",
                "navTitle": "Vantagens da microinfusão",
                "title": "Por que a microinfusão capilar é tão eficiente?",
                "p1": "Através de microagulhas precisas, os ativos antiqueda e aminoácidos são depositados exatamente onde a matriz do fio é produzida.",
                "p2": "O procedimento é rápido, confortável e promove o espessamento progressivo dos fios ralos, devolvendo volume e vitalidade ao couro cabeludo.",
                "figure": {
                    "src": "assets/img/resultados/caso-harmonizacao-masculina-2.webp",
                    "alt": "Paciente masculino com cabelo e contorno facial restaurados",
                    "caption": "Rejuvenescimento capilar e facial integrado no Água Verde."
                }
            }
        ]
    }
]

MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
def format_date_pt(d_str):
    y, m, d = d_str.split("-")
    return f"{int(d)} de {MONTHS[int(m)-1]} de {y}"

# Shared CSS for Article Pages matching exact user template
ARTICLE_CSS = """
        /* Tailwind-like base layout matching template */
        body { font-family: var(--font-body, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif); color: #374151; background-color: #FFFFFF; margin: 0; }
        .min-h-screen { min-height: 100vh; }
        .bg-white { background-color: #ffffff; }
        .bg-gray-50 { background-color: #f9fafb; }
        .bg-gray-800 { background-color: #1f2937; }
        .bg-gray-900 { background-color: #111827; }
        .text-white { color: #ffffff; }
        .text-gray-400 { color: #9ca3af; }
        .text-gray-500 { color: #6b7280; }
        .text-gray-600 { color: #4b5563; }
        .text-gray-700 { color: #374151; }
        .text-gray-800 { color: #1f2937; }
        .text-gray-900 { color: #111827; }
        
        .container { width: 100%; margin-left: auto; margin-right: auto; padding-left: 1rem; padding-right: 1rem; }
        .max-w-4xl { max-width: 56rem; }
        .max-w-5xl { max-width: 64rem; }
        .max-w-6xl { max-width: 72rem; }
        .max-w-xl { max-width: 36rem; }
        .max-w-3xl { max-width: 48rem; }
        .mx-auto { margin-left: auto; margin-right: auto; }
        .text-center { text-align: center; }
        
        /* Header */
        .fixed { position: fixed; }
        .top-0 { top: 0; }
        .z-50 { z-index: 50; }
        .w-full { width: 100%; }
        .h-full { height: 100%; }
        .shadow-md { box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06); }
        .py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
        .py-4 { padding-top: 1rem; padding-bottom: 1rem; }
        .py-8 { padding-top: 2rem; padding-bottom: 2rem; }
        .py-12 { padding-top: 3rem; padding-bottom: 3rem; }
        .pt-24 { padding-top: 6rem; }
        .pb-10 { padding-bottom: 2.5rem; }
        .py-10 { padding-top: 2.5rem; padding-bottom: 2.5rem; }
        .px-4 { padding-left: 1rem; padding-right: 1rem; }
        .px-6 { padding-left: 1.5rem; padding-right: 1.5rem; }
        .p-4 { padding: 1rem; }
        .p-6 { padding: 1.5rem; }
        .mb-2 { margin-bottom: 0.5rem; }
        .mb-4 { margin-bottom: 1rem; }
        .mb-5 { margin-bottom: 1.25rem; }
        .mb-6 { margin-bottom: 1.5rem; }
        .mb-8 { margin-bottom: 2rem; }
        .mb-10 { margin-bottom: 2.5rem; }
        .mt-2 { margin-top: 0.5rem; }
        .mt-4 { margin-top: 1rem; }
        .mt-6 { margin-top: 1.5rem; }
        .mt-7 { margin-top: 1.75rem; }
        .mt-8 { margin-top: 2rem; }
        .mt-12 { margin-top: 3rem; }
        .my-8 { margin-top: 2rem; margin-bottom: 2rem; }
        .my-10 { margin-top: 2.5rem; margin-bottom: 2.5rem; }
        
        /* Article Hero */
        .border-b { border-bottom-width: 1px; border-bottom-style: solid; }
        .border-t { border-top-width: 1px; border-top-style: solid; }
        .border-white\\/10 { border-color: rgba(255, 255, 255, 0.1); }
        .border-gray-100 { border-color: #f3f4f6; }
        .rounded-full { border-radius: 9999px; }
        .rounded-md { border-radius: 0.375rem; }
        .rounded-lg { border-radius: 0.5rem; }
        .rounded-xl { border-radius: 0.75rem; }
        .rounded-2xl { border-radius: 1rem; }
        .rounded-r-xl { border-top-right-radius: 0.75rem; border-bottom-right-radius: 0.75rem; }
        .overflow-hidden { overflow: hidden; }
        .object-cover { object-fit: cover; }
        .object-contain { object-fit: contain; }
        
        /* Typography */
        .text-xs { font-size: 0.75rem; line-height: 1rem; }
        .text-\\[11px\\] { font-size: 11px; }
        .text-sm { font-size: 0.875rem; line-height: 1.25rem; }
        .text-base { font-size: 1rem; line-height: 1.5rem; }
        .text-lg { font-size: 1.125rem; line-height: 1.75rem; }
        .text-xl { font-size: 1.25rem; line-height: 1.75rem; }
        .text-2xl { font-size: 1.5rem; line-height: 2rem; }
        .text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
        .text-4xl { font-size: 2.25rem; line-height: 2.5rem; }
        .text-5xl { font-size: 3rem; line-height: 1.15; }
        .font-medium { font-weight: 500; }
        .font-semibold { font-weight: 600; }
        .font-bold { font-weight: 700; }
        .italic { font-style: italic; }
        .not-italic { font-style: normal; }
        .leading-tight { line-height: 1.25; }
        .leading-relaxed { line-height: 1.75; }
        .uppercase { text-transform: uppercase; }
        .tracking-wider { letter-spacing: 0.05em; }
        .tracking-widest { letter-spacing: 0.1em; }
        .tracking-\\[0\\.2em\\] { letter-spacing: 0.2em; }
        
        /* Grid & Flex */
        .flex { display: flex; }
        .inline-flex { display: inline-flex; }
        .flex-col { flex-direction: column; }
        .flex-wrap { flex-wrap: wrap; }
        .items-center { align-items: center; }
        .justify-between { justify-content: space-between; }
        .justify-center { justify-content: center; }
        .gap-2 { gap: 0.5rem; }
        .gap-3 { gap: 0.75rem; }
        .gap-4 { gap: 1rem; }
        .gap-6 { gap: 1.5rem; }
        .gap-8 { gap: 2rem; }
        .gap-10 { gap: 2.5rem; }
        .grid { display: grid; }
        .grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        
        .relative { position: relative; }
        .h-4 { height: 1rem; }
        .w-\\[3px\\] { width: 3px; }
        .h-10 { height: 2.5rem; }
        .h-12 { height: 3rem; }
        .h-14 { height: 3.5rem; }
        .w-14 { width: 3.5rem; }
        .h-56 { height: 14rem; }
        
        .border-l-4 { border-left-width: 4px; border-left-style: solid; }
        .border-4 { border-width: 4px; border-style: solid; }
        .border-white\\/90 { border-color: rgba(255, 255, 255, 0.9); }
        .border-\\[\\#2A7DE1\\] { border-color: #2A7DE1; }
        .bg-\\[\\#2A7DE1\\] { background-color: #2A7DE1; }
        .bg-\\[\\#111111\\] { background-color: #111111; }
        .text-\\[\\#2A7DE1\\] { color: #2A7DE1; }
        .scroll-mt-32 { scroll-margin-top: 8rem; }
        .space-y-2 > :not([hidden]) ~ :not([hidden]) { margin-top: 0.5rem; }
        .list-decimal { list-style-type: decimal; }
        .pl-4 { padding-left: 1rem; }
        .pl-6 { padding-left: 1.5rem; }
        .pt-6 { padding-top: 1.5rem; }
        
        /* Sidebar Sticky Layout */
        @media (min-width: 1024px) {
            .lg\\:grid-cols-\\[280px_1fr\\] { grid-template-columns: 280px 1fr; }
            .lg\\:sticky { position: sticky; }
            .lg\\:top-32 { top: 8rem; }
            .lg\\:self-start { align-self: flex-start; }
            .lg\\:gap-14 { gap: 3.5rem; }
            .lg\\:block { display: block; }
        }
        @media (max-width: 1023px) {
            .hidden { display: none; }
        }
        @media (min-width: 768px) {
            .md\\:flex { display: flex; }
            .md\\:pt-36 { padding-top: 9rem; }
            .md\\:pb-14 { padding-bottom: 3.5rem; }
            .md\\:py-4 { padding-top: 1rem; padding-bottom: 1rem; }
            .md\\:py-16 { padding-top: 4rem; padding-bottom: 4rem; }
            .md\\:text-5xl { font-size: 3rem; }
            .md\\:text-4xl { font-size: 2.25rem; }
            .md\\:text-3xl { font-size: 1.875rem; }
            .md\\:text-2xl { font-size: 1.5rem; }
            .md\\:text-xl { font-size: 1.25rem; }
            .md\\:text-lg { font-size: 1.125rem; }
            .md\\:grid-cols-\\[1fr_auto\\] { grid-template-columns: 1fr auto; }
            .md\\:p-10 { padding: 2.5rem; }
            .md\\:h-\\[420px\\] { height: 420px; }
            .md\\:h-\\[400px\\] { height: 400px; }
            .md\\:h-80 { height: 20rem; }
            .md\\:w-64 { width: 16rem; }
            .md\\:mb-6 { margin-bottom: 1.5rem; }
            .md\\:mb-8 { margin-bottom: 2rem; }
            .md\\:px-8 { padding-left: 2rem; padding-right: 2rem; }
        }
        @media (min-width: 640px) {
            .sm\\:text-4xl { font-size: 2.25rem; }
            .sm\\:text-3xl { font-size: 1.875rem; }
            .sm\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
            .sm\\:flex-row { flex-direction: row; }
            .sm\\:items-center { align-items: center; }
            .sm\\:h-80 { height: 20rem; }
            .sm\\:h-72 { height: 18rem; }
        }
        
        /* Floating WhatsApp */
        .whatsapp-float { position: fixed; bottom: 24px; right: 24px; z-index: 999; }
        .whatsapp-btn { display: flex; align-items: center; justify-content: center; width: 60px; height: 60px; background-color: #22c55e; color: #ffffff; border-radius: 50%; box-shadow: 0 10px 25px rgba(34, 197, 94, 0.4); text-decoration: none; transition: transform 0.3s ease, background-color 0.3s ease; }
        .whatsapp-btn:hover { transform: scale(1.1); background-color: #16a34a; }
"""

for p in POSTS:
    tags_html = "".join([f'<span class="text-xs font-medium text-[#2A7DE1]">{t}</span>' for t in p["tags"]])
    
    # Generate left sidebar index links
    sidebar_links_html = ""
    for sec in p["sections"]:
        sidebar_links_html += f'<a href="#{sec["id"]}" class="border-b border-gray-100 py-3 text-sm font-medium transition-colors text-gray-800 hover:text-[#2A7DE1]" style="text-decoration: none;">{sec["navTitle"]}</a>\n'
    
    # Generate main article sections
    sections_html = ""
    for i, sec in enumerate(p["sections"]):
        p2_text = f'<p class="mb-5 text-base leading-relaxed text-gray-700 md:text-lg">{sec["p2"]}</p>' if "p2" in sec else ""
        sec_content = f"""
        <h2 id="{sec['id']}" class="mb-4 mt-12 scroll-mt-32 text-2xl font-bold text-gray-900 md:text-3xl">{sec['title']}</h2>
        <p class="mb-5 text-base leading-relaxed text-gray-700 md:text-lg">{sec['p1']}</p>
        {p2_text}
        """
        
        if "figure" in sec:
            fig = sec["figure"]
            sec_content += f"""
            <figure class="my-8">
                <div class="relative h-56 w-full overflow-hidden rounded-xl sm:h-80 md:h-[400px]">
                    <img alt="{fig['alt']}" loading="lazy" class="object-cover w-full h-full" src="{fig['src']}">
                </div>
                <figcaption class="mt-2 text-center text-sm text-gray-500">{fig['caption']}</figcaption>
            </figure>
            """
            
        if "list" in sec:
            list_items = "".join([f'<li class="leading-relaxed">{item}</li>' for item in sec["list"]])
            sec_content += f"""
            <ol class="mb-6 space-y-2 pl-6 text-base text-gray-700 md:text-lg list-decimal">
                {list_items}
            </ol>
            """
            
        if "quote" in sec:
            q = sec["quote"]
            sec_content += f"""
            <blockquote class="my-8 rounded-r-xl border-l-4 border-[#2A7DE1] bg-gray-50 p-6">
                <p class="text-lg italic leading-relaxed text-gray-800">“{q['text']}”</p>
                <cite class="mt-3 block text-sm not-italic text-gray-600">— {q['author']}</cite>
            </blockquote>
            """
            
        # Insert Dark Card CTA in the middle
        if i == 1 or (len(p["sections"]) == 1 and i == 0):
            sec_content += f"""
            <div class="not-prose my-10 overflow-hidden rounded-2xl bg-[#111111]">
                <div class="grid gap-6 p-6 md:grid-cols-[1fr_auto] md:items-center md:gap-10 md:p-10">
                    <div>
                        <div class="mb-4 flex items-center gap-2">
                            <span class="h-4 w-[3px] bg-[#2A7DE1]"></span>
                            <span class="text-[11px] font-semibold uppercase tracking-[0.2em] text-gray-400">Dr. Henrique Leal Rosa</span>
                        </div>
                        <h2 class="text-2xl font-bold uppercase leading-tight text-white sm:text-3xl md:text-4xl">
                            Deseja avaliar o seu caso <span class="text-[#2A7DE1]">em Curitiba?</span>
                        </h2>
                        <p class="mt-4 max-w-xl text-sm leading-relaxed text-gray-400">
                            Planejamento anatômico individualizado com foco em discrição, sofisticação e segurança clínica no Edifício Today's Office, Água Verde.
                        </p>
                        <div class="mt-6 grid grid-cols-2 gap-4 border-t border-white/10 pt-6 sm:grid-cols-4">
                            <div>
                                <p class="text-[11px] font-semibold uppercase tracking-widest text-white">Avaliação</p>
                                <p class="mt-1 text-[11px] uppercase tracking-wider text-gray-500">Personalizada</p>
                            </div>
                            <div>
                                <p class="text-[11px] font-semibold uppercase tracking-widest text-white">Local</p>
                                <p class="mt-1 text-[11px] uppercase tracking-wider text-gray-500">Água Verde</p>
                            </div>
                            <div>
                                <p class="text-[11px] font-semibold uppercase tracking-widest text-white">Segurança</p>
                                <p class="mt-1 text-[11px] uppercase tracking-wider text-gray-500">Padrão Ouro</p>
                            </div>
                            <div>
                                <p class="text-[11px] font-semibold uppercase tracking-widest text-white">Resultados</p>
                                <p class="mt-1 text-[11px] uppercase tracking-wider text-gray-500">Naturais</p>
                            </div>
                        </div>
                        <div class="mt-7 flex flex-col gap-4 sm:flex-row sm:items-center">
                            <a class="inline-flex items-center justify-center gap-2 rounded bg-[#2A7DE1] px-6 py-3 text-xs font-bold uppercase tracking-widest text-white transition-colors hover:bg-[#1E6BC9]" 
                               href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20li%20o%20artigo%20sobre%20{p['slug']}%20e%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o." target="_blank" rel="noopener" style="text-decoration: none;">
                                Agendar no WhatsApp
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </a>
                            <span class="text-[11px] uppercase tracking-widest text-gray-500">Atendimento com hora marcada</span>
                        </div>
                    </div>
                    <div class="relative h-56 w-full overflow-hidden rounded-lg border-4 border-white/90 sm:h-72 md:h-80 md:w-64">
                        <img alt="Dr. Henrique Leal Rosa" loading="lazy" class="object-cover w-full h-full" src="assets/img/henrique-portrait.webp">
                    </div>
                </div>
            </div>
            """
            
        sections_html += sec_content

    full_page_html = f"""<!DOCTYPE html>
<html lang="pt-BR" class="light" style="color-scheme: light;">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" href="assets/img/favicon.png?v=3">
    <link rel="apple-touch-icon" href="assets/img/favicon.png?v=3">
    <title>{p['title']} | Dr. Henrique Leal Rosa</title>
    <meta name="description" content="{p['excerpt']}">
    <meta name="author" content="Dr. Henrique Leal Rosa">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://drhenriqueleal.com.br/{p['slug']}.html">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{p['title']} | Dr. Henrique Leal Rosa">
    <meta property="og:description" content="{p['excerpt']}">
    <meta property="og:url" content="https://drhenriqueleal.com.br/{p['slug']}.html">
    <meta property="og:image" content="https://drhenriqueleal.com.br/{p['cover']}">
    <meta property="og:type" content="article">
    <meta property="article:published_time" content="{p['date']}">
    <meta property="article:author" content="Dr. Henrique Leal Rosa">
    
    <!-- Structured Data JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{p['title']}",
      "description": "{p['excerpt']}",
      "image": "https://drhenriqueleal.com.br/{p['cover']}",
      "datePublished": "{p['date']}",
      "author": {{
        "@type": "Person",
        "name": "Dr. Henrique Leal Rosa",
        "jobTitle": "Cirurgião Dentista (CRO-PR) & Biomédico (CRBM-PR)"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Dr. Henrique Leal Rosa",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://drhenriqueleal.com.br/assets/img/logo-sub-colorida.webp"
        }}
      }},
      "mainEntityOfPage": "https://drhenriqueleal.com.br/{p['slug']}.html"
    }}
    </script>
    
    <style>
{ARTICLE_CSS}
    </style>
</head>

<body>
    <div class="min-h-screen bg-white">
        
        <!-- Header -->
        <header class="fixed top-0 z-50 w-full bg-white py-2 shadow-md md:py-4">
            <div class="container mx-auto flex items-center justify-between px-4" style="max-width: 72rem;">
                <a class="flex items-center gap-2" href="index.html">
                    <img alt="Dr. Henrique Leal Rosa" width="180" height="42" class="object-contain" src="assets/img/logo-texto.webp">
                </a>
                <nav class="hidden items-center gap-8 md:flex">
                    <a class="font-medium text-gray-700 transition-colors hover:text-[#2A7DE1]" href="index.html" style="text-decoration: none;">Home</a>
                    <a class="font-medium text-gray-700 transition-colors hover:text-[#2A7DE1]" href="sobre.html" style="text-decoration: none;">Sobre</a>
                    <a class="font-medium text-[#2A7DE1] font-bold" href="blog.html" style="text-decoration: none;">Blog</a>
                    <a class="font-medium text-gray-700 transition-colors hover:text-[#2A7DE1]" href="procedimentos.html" style="text-decoration: none;">Procedimentos</a>
                    <a class="font-medium text-gray-700 transition-colors hover:text-[#2A7DE1]" href="index.html#localizacao" style="text-decoration: none;">Contato</a>
                    <div class="flex items-center gap-2 text-gray-700">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-[#2A7DE1]"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        <span class="text-sm font-medium">(41) 98857-7430</span>
                    </div>
                    <a href="https://wa.me/5541988577430" target="_blank" rel="noopener" style="text-decoration: none;">
                        <button style="cursor: pointer;" class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium h-10 px-4 py-2 bg-[#2A7DE1] text-white hover:bg-[#1E6BC9] border-0">
                            Entrar em Contato
                        </button>
                    </a>
                </nav>
            </div>
        </header>

        <!-- Article Header Section -->
        <section class="border-b border-gray-100 bg-gray-50 pt-24 md:pt-36">
            <div class="container mx-auto max-w-5xl px-4 pb-10 md:pb-14">
                
                <!-- Author Header -->
                <div class="mb-6 flex items-center gap-4">
                    <div class="relative h-14 w-14 overflow-hidden rounded-full md:h-16 md:w-16" style="border: 2px solid #2A7DE1;">
                        <img alt="Dr. Henrique Leal Rosa" class="object-cover w-full h-full" src="assets/img/henrique-portrait.webp">
                    </div>
                    <div>
                        <p class="text-lg font-bold text-gray-900 md:text-xl">Dr. Henrique Leal Rosa</p>
                        <p class="text-sm text-gray-600">Cirurgião Dentista (CRO-PR 31739) & Biomédico (CRBM-PR 8966)</p>
                    </div>
                </div>

                <!-- Category & Tags -->
                <div class="mb-5 flex flex-wrap items-center gap-3">
                    <span class="rounded-full bg-[#2A7DE1] px-3 py-1 text-xs font-semibold text-white">{p['category']}</span>
                    {tags_html}
                </div>

                <!-- Article Title -->
                <h1 class="max-w-4xl text-3xl font-bold leading-tight text-gray-900 sm:text-4xl md:text-5xl">
                    {p['title']}
                </h1>

                <!-- Human Reviewed Badge -->
                <div class="mt-6 inline-flex items-center gap-2 rounded-full bg-gray-800 px-4 py-2 text-xs font-medium text-white">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-[#2A7DE1]"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"></path><path d="m9 12 2 2 4-4"></path></svg>
                    Conteúdo médico revisado · Curitiba, PR
                </div>

                <!-- Meta Date & Time -->
                <div class="mt-6 flex flex-wrap items-center gap-6 text-sm text-gray-600">
                    <span class="flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-[#2A7DE1]"><path d="M8 2v4"></path><path d="M16 2v4"></path><rect width="18" height="18" x="3" y="4" rx="2"></rect><path d="M3 10h18"></path><path d="M8 14h.01"></path><path d="M12 14h.01"></path><path d="M16 14h.01"></path><path d="M8 18h.01"></path><path d="M12 18h.01"></path><path d="M16 18h.01"></path></svg>
                        {format_date_pt(p['date'])}
                    </span>
                    <span class="flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-[#2A7DE1]"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        {p['readingMinutes']} min de leitura
                    </span>
                </div>

            </div>
        </section>

        <!-- Body Section with 2-Column Grid (Sticky Sidebar + Article Content) -->
        <section class="py-10 md:py-16">
            <div class="container mx-auto max-w-6xl px-4">
                <div class="grid gap-10 lg:grid-cols-[280px_1fr] lg:gap-14">
                    
                    <!-- Left Sticky Sidebar Index -->
                    <aside class="lg:sticky lg:top-32 lg:self-start">
                        <h2 class="mb-4 text-xl font-bold text-gray-900">Índice do Artigo</h2>
                        <nav class="flex flex-col">
                            {sidebar_links_html}
                        </nav>
                        
                        <div class="mt-8 p-6 rounded-xl bg-gray-50 border border-gray-100 hidden lg:block">
                            <h3 class="text-sm font-bold uppercase tracking-wider text-gray-900 mb-2">Consultório Água Verde</h3>
                            <p class="text-xs text-gray-600 leading-relaxed mb-4">
                                Av. Rep. Argentina, 1237 - Sala 518 · Edifício Today's Office, Curitiba - PR.
                            </p>
                            <a href="https://wa.me/5541988577430" target="_blank" rel="noopener" class="text-xs font-bold text-[#2A7DE1] hover:underline" style="text-decoration: none;">
                                Agendar Consulta ↗
                            </a>
                        </div>
                    </aside>

                    <!-- Right Main Article Body -->
                    <article class="min-w-0">
                        
                        <!-- Lead Quote with Gold Left Border -->
                        <p class="mb-8 border-l-4 border-[#2A7DE1] pl-4 text-lg leading-relaxed text-gray-800 md:text-xl">
                            {p['lead']}
                        </p>

                        <!-- Main Featured Article Cover Image -->
                        <div class="relative mb-10 h-56 w-full overflow-hidden rounded-xl sm:h-80 md:h-[420px]">
                            <img alt="{p['coverAlt']}" fetchpriority="high" class="object-cover w-full h-full" src="{p['cover']}">
                        </div>

                        <!-- Dynamic Section Content -->
                        {sections_html}

                    </article>
                </div>
            </div>
        </section>

        <!-- Bottom Pre-Footer CTA Section -->
        <section class="bg-[#2A7DE1] py-12 text-white md:py-16">
            <div class="container mx-auto px-4">
                <div class="mx-auto max-w-3xl text-center">
                    <h2 class="mb-4 text-2xl font-bold sm:text-3xl md:text-4xl md:mb-6">Pronto para dar o próximo passo?</h2>
                    <p class="mb-6 text-sm text-white/90 md:mb-8 md:text-lg">
                        Fale diretamente com o Dr. Henrique Leal e descubra qual o planejamento ideal para harmonizar seus traços com naturalidade em Curitiba.
                    </p>
                    <div class="flex flex-col justify-center gap-3 sm:flex-row md:gap-4">
                        <a href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o%20com%20o%20Dr.%20Henrique." target="_blank" rel="noopener" style="text-decoration: none;">
                            <button style="cursor: pointer;" class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md font-medium h-12 bg-white px-6 py-4 text-base text-[#2A7DE1] hover:bg-gray-100 md:px-8 border-0">
                                Agendar Avaliação no WhatsApp
                                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </button>
                        </a>
                        <a href="procedimentos.html" style="text-decoration: none;">
                            <button style="cursor: pointer;" class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md font-medium h-12 border border-white bg-transparent px-6 py-4 text-base text-white hover:bg-white/20 md:px-8">
                                Ver Nossos Procedimentos
                            </button>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="bg-gray-900 py-8 text-white">
            <div class="container mx-auto px-4">
                <div class="text-center text-sm text-gray-400">
                    <p>© 2026 Dr. Henrique Leal Rosa. Todos os direitos reservados. CRO-PR 31739 · CRBM-PR 8966.</p>
                    <p class="mt-2 text-xs text-gray-500">Edifício Today's Office · Av. República Argentina, 1237 - Sala 518, Água Verde, Curitiba - PR.</p>
                </div>
            </div>
        </footer>

        <!-- Floating WhatsApp Button -->
        <div class="whatsapp-float">
            <a href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20gostaria%20de%20tirar%20uma%20d%C3%BAvida%20sobre%20os%20procedimentos." class="whatsapp-btn" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"></path></svg>
            </a>
        </div>

    </div>
</body>
</html>
"""
    with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(full_page_html)

print("Generated all 20 individual article pages matching EXACT template structure!")
