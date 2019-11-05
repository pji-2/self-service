<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.2.3/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/7.2.3/firebase-analytics.js"></script>

<script>
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyBLed39IVJumLraim3sSnQVsOV9dVUt7Eg",
    authDomain: "pji2-ade1a.firebaseapp.com",
    databaseURL: "https://pji2-ade1a.firebaseio.com",
    projectId: "pji2-ade1a",
    storageBucket: "pji2-ade1a.appspot.com",
    messagingSenderId: "568287405313",
    appId: "1:568287405313:web:bbce976a427d105d7f6700",
    measurementId: "G-PNNCDHWKWH"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
</script>

Comandos para instalar o firebase:

-Após diretório criado:
	'virtualenv -p /usr/bin/python3 venv'
	(caso não tenha virtualenv instalado: sudo apt install virtualenv)
	'. venv/bin/activate' (para ativar o virtualenv)
	'pip install requests python-firebase' (para adicionar o firebase no projeto)
	'pip freeze' (para ver as versões)
	'pip freeze > requirements.txt' (adicionar versões dentro do arquivo requirements, depois instala este arquivo para adicionar as versões da biblioteca)
	'touch teste.py' (para criar um arquivo vazio)


	comandos do git:
	'git branch' (para ver qual ramo está trabalhando)
	'git branch NOME' (para criar um ramo com nome NOME)
	'git checkout NOME' (para ir para ramo de nome NOME)
	no final deve-se dar um merge... pesquisar comando
