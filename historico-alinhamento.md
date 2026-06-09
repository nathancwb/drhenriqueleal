# Histórico de Alinhamento e Evolução - Landing Page VIP Dr. Henrique Leal

Este documento consolida o histórico de desenvolvimento, alinhamento estético e decisões de design tomadas para a criação da **Landing Page de Cursos & Mentorias VIP do Dr. Henrique Leal** (`cursos-vip.html`), garantindo que toda a equipe e o próprio doutor tenham visibilidade sobre os refinamentos de alta imersão implementados.

---

## 1. Visão Geral e Filosofia do Projeto

A página foi desenhada para representar o ápice do **luxo clínico** e **estética de agência premium**, inspirando-se no padrão Apple de design de interação e scrollytelling físico. A jornada de rolagem é fluida, misteriosa e focada exclusivamente em conversão.

*   **Público-Alvo:** Profissionais da saúde graduados e injetores (Dentistas, Biomédicos, Farmacêuticos e Médicos) que buscam mentorias exclusivas e práticas intensas (*Hands-On*).
*   **Foco em Conversão:** Uma página 100% livre de distrações. Foram removidos o menu superior tradicional, logos redundantes e links de navegação secundária. O foco do usuário está inteiramente na experiência imersiva e no formulário de candidatura.
*   **Aparência Visual:** Fundo azul-escuro profundo (midnight blue), detalhes e brilhos em ouro fosco/dourado e tipografia serifada luxuosa editorial (`Instrument Serif` para títulos em destaque, mesclada com a precisão minimalista de `Inter`).

---

## 2. Decisões de Design e Ajustes Críticos Resolvidos

Ao longo das iterações e feedbacks, os seguintes problemas visuais e de interação foram refinados com maestria:

### A. Eliminação de Ruídos Visuais e Menu de Navegação
*   **Decisão:** O menu superior (com links institucionais e botão de consultor) e os botões flutuantes em forma de bolinhas na lateral direita foram totalmente removidos. Isso garante que a página atue como um funil de conversão puro e focado de alta imersão.

### B. Correção de Contrastes e Legibilidade
*   **Endereço Físico:** Anteriormente, a seção final exibia o endereço com escrita dourada sobre fundo branco, o que anulava o contraste. O contêiner foi redesenhado como uma **cápsula escura translúcida (glassmorphism)** com bordas douradas sutis e texto branco de alto contraste, garantindo legibilidade perfeita e refinamento.
*   **Botão Secundário do Hero ("Conhecer Programas"):** O botão com contorno anteriormente sumia no fundo. Foi reestilizado com fundo branco translúcido (`rgba(255,255,255,0.08)`) com forte desfoque de fundo (backdrop-filter) e texto branco de alta definição.
*   **Campos de Formulário:** Os inputs e selects do formulário de candidatura foram completamente integrados ao tema escuro. Possuem fundos midnight blue semi-translúcidos, contornos de foco dourados e setas de seleção customizadas em vetor ouro.

### C. Bloco 4: Metodologia Crescente (3 Pilares)
*   **Mecânica:** O bloco traduz o scroll vertical em um crescendo cinematográfico.
*   **Elementos:**
    *   Um grid sutil dourado de fundo é exibido.
    *   Uma linha dourada vertical cresce de cima para baixo à medida que o usuário avança no scroll.
### D. Bloco 3: Eliminação do Vazio no Final das Mentorias (Cursos)
*   **Problema:** Ao passar por todas as mentorias no scroll, a coluna da direita ficava vazia (com um grande vácuo preto), pois a seção continuava travada (*sticky*) por causa de uma altura fixa de `380vh` e um espaçamento inferior de `45vh` no scrollable track.
*   **Solução:** 
    *   Alteramos a altura da seção `.scrolly-container-long` para **`auto`**. Isso faz com que a altura do bloco seja calculada dinamicamente com base na altura exata da coluna de rolagem da direita.
    *   Reduzimos o espaçamento inferior (*bottom spacer*) da coluna da direita de `45vh` para **`10vh`**.
    *   **Resultado:** Assim que a última mentoria (Card 4 - Harmonização Glútea) é focada e lida, a seção destrava imediatamente e sobe junto com o restante da página, transitando perfeitamente para a seção de Metodologia, eliminando 100% do espaço vazio.

### E. Bloco 3: Eliminação da Distorção 3D ("Warping") e Limitação de Largura das Mentorias
*   **Decisão:** O efeito 3D anterior (`rotateX` e `translate3d` com `perspective`) causava uma distorção trapezoidal nos cards durante a rolagem (dando a impressão visual de "esticado/deformado" e com aspecto datado/antigo).
*   **Solução:**
    *   Removemos a perspectiva 3D do contêiner e substituímos a transição dos cards por uma animação de deslizamento e escala plana em 2D (**`translateY(40px) scale(0.96)`** suavizada por curvas *cubic-bezier* de alta performance), idêntica às utilizadas em sites premium da Apple e Stripe.
    *   Definimos uma largura máxima de **`760px`** (`max-width: 760px;`) para os cards de mentorias.
    *   **Resultado:** Os cards agora deslizam com suavidade extrema e mantêm uma proporção perfeita e simétrica, livre de distorções visuais e com visual de altíssimo luxo editorial contemporâneo.

---

## 3. O Novo Carrossel Horizontal do Público-Alvo

Para tornar a seção de **Público Habilitado** (Bloco 2) verdadeiramente interativa, desenvolvemos um carrossel horizontal guiado por rolagem de alta performance:

1.  **Imersão e Sincronia:** O scroll vertical do usuário trava na tela (*sticky viewport*) enquanto a intensidade da rolagem translada horizontalmente os cards de público da direita para a esquerda.
2.  **Ritmo de Rolagem Perfeito:** Aumentamos a altura física de scroll da seção para **350vh** (anteriormente 200vh), tornando a transição horizontal 2.5 vezes mais lenta, suave e controlável para o usuário.
3.  **Remoção de Limites de Contêiner (Resolução de Clippings):**
    *   **Problema:** O viewport do carrossel estava envelopado dentro de um bloco `.container` (que possui largura máxima fixa de `1140px`). Isso quebrava os cálculos baseados em `vw` (largura do viewport), fazendo com que os cards se separassem demais, ficassem cortados nas pontas e deixassem o centro da tela vazio em telas maiores.
    *   **Solução:** Movemos o elemento `.publico-scrollytelling-viewport` para fora do `.container` principal. O título da seção continua perfeitamente alinhado dentro do container, mas o trilho de cards agora desliza livremente por toda a largura física da tela (**`100vw`**).
4.  **Visualização "Peek-Ahead" (Próximo Card Visível e Compacto):**
    *   Reduzimos a largura de cada contêiner de card no desktop de `100vw` para **`45vw`** e definimos o tamanho máximo físico do card em **`580px`** (`max-width: 580px;`). Isso evita o efeito esticado desproporcional e mantém a estrutura compacta, elegante e altamente legível.
    *   Adicionamos um preenchimento dinâmico de início e fim no trilho de **`27.5vw`** (`calc((100vw - 45vw) / 2)`).
    *   **Resultado:** Quando um card está focado e centralizado, a lateral do próximo card fica sutil e elegantemente visível na borda direita da tela (peek-ahead), instigando o usuário a continuar descendo de forma harmônica e garantindo que **sempre haja pelo menos um card em destaque visível**.
5.  **Aparecimento Perfeito do Último Card:** O trilho foi recalibrado matematicamente com uma distância máxima exata de viagem de **`98vw`** (`(3 cards - 1) * (45vw + 4vw)`), garantindo que o terceiro e último card (Médicos) apareça perfeitamente centralizado no final da jornada física do bloco, sem travar ou sumir.
6.  **Responsividade Impecável:** Em telas menores que `992px`, o carrossel se dissolve automaticamente e empilha os cards verticalmente com fundos pretos sólidos luxuosos, garantindo legibilidade e usabilidade intocáveis em dispositivos móveis.

## 4. Remoção do Efeito de Cursor Customizado (Mouse)
Para garantir uma experiência de navegação nativa, rápida e livre de atrasos visuais, o cursor customizado que seguia o mouse (`.cursor-dot` e `.cursor-ring` que ocultavam o ponteiro padrão com `cursor: none`) foi completamente removido do HTML, CSS e JavaScript. O site agora utiliza o ponteiro nativo do sistema operacional do usuário, oferecendo total leveza, agilidade e conforto de navegação.

## 5. Substituição e Otimização da Foto do FAQ (Henrique Leal)
*   **Problema:** A foto anterior em terno azul no FAQ precisava ser substituída por uma imagem ainda mais premium e condizente com a imersão de luxo. A foto ideal de alta definição disponível (`7G1A9991.jpg`) possuía 12MB, inviabilizando o desempenho e tempo de carregamento da landing page.
*   **Solução:**
    *   Substituímos o arquivo `henrique-portrait.jpg` no FAQ.
    *   Desenvolvemos e executamos um script de processamento de imagem em Python (`compress_photo.py`) utilizando interpolação bilinear avançada (LANCZOS) para redimensionar a foto profissional de 12MB e comprimi-la como uma imagem compacta e de altíssima fidelidade: **`henrique-faq-new.jpg`** (pesando apenas 160KB).
    *   **Resultado:** A foto exibe Dr. Henrique Leal em seu consultório com nitidez intocável e carregamento instantâneo, elevando a qualidade visual da seção estática final.

### F. Transição de Fade-Out Cinemático e União de Seções
*   **Problema:** Anteriormente, as transições entre seções com fundos escuros, fotos grandes e grades de metodologia possuíam linhas rígidas e emendas secas durante a rolagem de tela, quebrando a imersão e parecendo "cortadas".
*   **Solução:**
    *   Substituímos o controle individual de opacidades dos cards por uma **equação unificada de opacidade** em todas as 5 seções ativas de scrollytelling (`#block-hero`, `#block-publico`, `#block-mentorias`, `#b4` e `#block-candidatura`).
    *   As opacidades agora são calculadas com base nas coordenadas físicas e colisão com a tela (`getBoundingClientRect`), fazendo com que toda a seção anterior faça um **fade-out completo e gradual até `opacity: 0` antes de se desfixar (unpin)** do topo da tela, enquanto a próxima seção entra fazendo um **fade-in contínuo a partir do fundo preto/escuro**.
    *   **Resultado:** Uma fusão fluida e cinemática perfeita entre os blocos, parecendo uma transição contínua onde o site se redesenha no mesmo lugar sem cortes e sem emendas.

### G. Aceleração Gráfica por Hardware (will-change)
*   **Otimização:** Para garantir que a aplicação contínua de opacidades e transformações pelo motor JavaScript durante o scroll não sobrecarregasse a CPU ou gerasse pequenas engasgadas visuais (stuttering), adicionamos a propriedade **`will-change: opacity;`** nos viewports e contêineres de scrollytelling (`.scrolly-sticky`, `#block-mentorias`, `#b4-vp`).
*   **Resultado:** O navegador agora delega toda a renderização e composição de opacidade diretamente para a GPU (placa de vídeo), proporcionando uma rolagem macia a 60 FPS estáveis mesmo em monitores de alta taxa de atualização.

## 6. O Novo Refinamento de Responsividade Mobile e Conforto de Leitura
Para garantir que a Landing Page possua a mesma excelência estética de agência premium em smartphones, redesenhamos a experiência mobile sob `992px` de largura:

*   **Merged Stack do Hero sem Redundância:** Ao invés de empilhar Phase 1 e Phase 2 em sua totalidade (o que resultava em blocos repetitivos e gigantescos de texto na tela inicial), ocultamos a descrição secundária e as instruções de scroll da Phase 1. A abertura mobile agora flui de forma extremamente focada e direta: Tagline de Elite -> Título Principal de Impacto -> Card Glassmorphic VIP com a explicação e CTAs.
*   **Correção de Contraste e Imagem de Fundo Esticada:** No mobile, a imagem do Dr. Henrique Leal no Hero foi configurada como **plano de fundo estático fixo (`position: fixed`)** com opacidade reduzida para `0.32`. Todas as seções subsequentes agora possuem fundos escuros sólidos (`var(--color-bg-dark)`) com camadas de prioridade (`z-index: 2`). Isso significa que a imagem de fundo nunca se distorce ou estica de forma desproporcional, e o conteúdo textual desliza sobre ela com contraste, conforto de leitura e legibilidade excepcionais.
*   **Fim do Squeezing nas Duas Colunas do FAQ (Resolução de Bugs):** O layout de perguntas frequentes possuía uma grade inline rígida de duas colunas, o que espremia a foto do doutor e a lista de accordion em colunas minúsculas e ilegíveis em celulares. Criamos uma regra de substituição responsiva que colapsa o FAQ em uma única coluna vertical perfeita, com redimensionamento equilibrado de imagem (`280px`).
*   **Proporções, Margens e Botões Finger-Friendly:** Redimensionamos as margens de seção para `60px 16px`, redefinimos as fontes de headings para `1.35rem` a `1.85rem` nos cards, reduzimos os paddings internos de cards para `30px 20px`, e redimensionamos os botões para ocuparem exatamente 100% da largura, facilitando o toque em telas de toque (touchscreens) com rapidez e ergonomia.
*   **Fim dos Botões Repetitivos nas Mentorias (Mobile):** No desktop, cada um dos 4 cards de mentorias possui seu próprio botão "Garantir Minha Vaga" para auto-selecionar o curso correspondente. No entanto, no mobile, o empilhamento vertical criava 4 CTAs gigantescos idênticos seguidos, o que poluía a leitura. Ocultamos os botões individuais nos cards de mentorias no mobile e adicionamos um **único botão centralizado e proeminente no final do bloco** ("Quero me Candidatar a uma Vaga"), proporcionando uma leitura limpa, leve e profissional.
*   **Resolução do Bug de Altura dos Accordions do FAQ:** As caixas de respostas do FAQ possuíam um estilo de preenchimento inline no HTML (`padding: 0 20px 20px`). Por conta disso, a resposta ficava parcialmente visível (escorrida no rodapé do card) mesmo quando o accordion estava fechado (`max-height: 0`). Eliminamos o preenchimento inline do elemento `.faq-answer` e movemos a propriedade inteiramente para a classe interna `.faq-answer-inner`. Agora, ao fechar, a resposta se recolhe a exatamente `0px` e fica perfeitamente invisível.
*   **Novo Layout de Abas para as Mentorias no Mobile (Fim do Text Overload):**
    *   **O problema resolvido:** Os 4 cards de mentorias possuíam textos detalhados com parágrafos e 5 bullet points cada. No celular, empilhar todas essas informações de uma só vez gerava uma rolagem exaustiva de mais de 1200px de puro texto.
    *   **Interface por Abas Interativas:** Criamos um seletor de abas horizontal de luxo semi-translúcido no topo da seção de Mentorias no mobile (`mentorias-mobile-tabs`). 
    *   O usuário agora visualiza **apenas um card de mentoria por vez**, alternando entre "Fios de PDO", "Estética Íntima", "Full Face" e "Glúteos" com toques instantâneos e transição suave de opacidade.
    *   **Encarte Ilustrado (Mobile-Only Photo):** Inseri no topo de cada aba mobile uma foto premium correspondente ao procedimento, que fica oculta no desktop. A seção agora parece um aplicativo refinado de alta tecnologia, mantendo 100% da informação de forma compacta, leve e legível.
    *   **Resolução do Corte de Cabeça/Rosto do Doutor (Crop Bug):** As fotos das mentorias são retratos verticais. Ao usá-las em um contêiner horizontal no mobile com `object-fit: cover`, o navegador centralizava o enquadramento, cortando completamente a cabeça e o rosto do Dr. Henrique. Aumentamos a altura do contêiner para **`250px`** (melhorando a proporção) e adicionamos a regra **`object-position: top center !important;`** na folha de estilos mobile. Isso força o enquadramento a alinhar pelo topo físico da foto, exibindo o rosto e os ombros do doutor com nitidez absoluta e enquadramento impecável.
*   **Persistência da Foto no Desktop (Sem Fade-Out Prematuro):**
    *   **O problema resolvido:** A foto de destaque na coluna esquerda (foto do doutor no consultório) começava a esmaecer e ficar muito escura (caindo para 30% a 40% de opacidade) quando o usuário ainda estava lendo e interagindo com o quarto e último card ("Harmonização & Volumização Glútea"). Isso ocorria porque o espaçador final da seção era muito pequeno (10vh), fazendo com que a base da seção entrasse no visor e ativasse a saída prematuramente.
    *   **Resolução Matemática e Espacial:** Substituímos o espaçador inline por uma classe CSS responsiva (`.mentorias-bottom-spacer`) com altura de `40vh` em desktop e oculta (`display: none`) em celulares. Ajustamos a fórmula de fade-out do script (`exitProgress`) para dividir a base da seção por `(viewportHeight * 0.45)` em vez de `viewportHeight`.
    *   **Garantia de Visibilidade:** Com isso, a foto de destaque permanece **100% nítida e totalmente opaca (sem qualquer fade-out precoce)** durante toda a leitura do último card, iniciando o fade-out apenas quando a seção começa de fato a dar espaço ao próximo bloco (Metodologia).
*   **Fim do Esmaecimento Precoce de Todo o Site (Hero, Público, Metodologia e Candidatura):**
    *   **O problema resolvido:** Em várias partes da página (especialmente no Hero e no formulário de Candidatura), o contêiner começava a esmaecer e ficar muito escuro/transparente antes que o conteúdo (como o segundo card do Hero ou as perguntas e inputs do formulário) aparecesse 100% legível na tela. Isso acontecia devido à antiga fórmula `(rect.bottom - viewportHeight) / (viewportHeight * 0.35)` que ativava a redução de opacidade de forma prematura durante a fase fixa (pinned).
    *   **Resolução Sistemática:** Substituímos o cálculo de saída em todas as seções de scrollytelling (`#block-hero`, `#block-publico`, `#b4` e `#block-candidatura`) por `rect.bottom / (viewportHeight * 0.8)`.
    *   **Resultado:** Os blocos agora permanecem com **100% de opacidade e legibilidade absoluta** durante toda a sua fase ativa e interativa, iniciando o fade-out de saída com suavidade apenas quando a seção é unpinnada e realmente começa a subir para dar espaço ao bloco seguinte.



---

*Alinhamento gerado e implementado em Maio de 2026 para a clínica de estética avançada do Dr. Henrique Leal.*
