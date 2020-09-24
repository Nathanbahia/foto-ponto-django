# Sistema de Ponto via Foto em Django

[Link do Projeto](https://pontosulconta.pythonanywhere.com/)

### Sistema utilizado para verificação da ida de funcionários até determinada estação da empresa para verificação de problemas aos redor das instalações.

Todos os dia, um grupo de funcionários deve se deslocar até determinada estação elétrica da empresa em busca de animais mortos ao redor das instaçãoes elétricas para realizar a remoção, a fim de se evitar atrair urubus ao local, o que pode causar diversos dados na rede de energia quando este animais entram em contato com a fiação elétrica.

Como comprovação da ida até às estações, os colaboradores escalados para tal tarefa devem enviar uma foto de rosto com a instalação ao fundo.

**O sistema deve conter os seguintes inputs:**
1. Foto
2. Data e horários do sistema
3. Matricula do funcionário
4. Localização geográfica

**O sistema deve conter:**
1. Tela de login
2. Tela principal, onde serão realizados todos os procedimentos
3. O sistema deverá ser construído na arquitetura de um PWA

**O sistema deve realizar o seguinte processo:**
1. O usuário abre o sistema
2. Realiza o login com usuário e senha
3. Clica em um botão que abre a câmera
4. Realiza a captura da imagem
5. Após a confirmação da foto, o sistema salva em um banco de dados
6. A foto é enviada por e-mail à direção da empresa, com a data e nome do usuário
7. *O usuário recebe por e-mail, sms ou whatsapp uma mensagem de confirmação de envio (verificar)*
8. O sistema exibe uma mensagem de sucesso no envio

**DÚVIDAS:**
1. Caso haja mais de um colaborador escalado para ir à estação no mesmo dia, cada um deve enviar uma foto, ou os dois podem enviar uma única foto?
