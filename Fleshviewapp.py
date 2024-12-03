from flask import Flask, render_template
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# URL do aplicativo Streamlit
app_url = "https://scvsei901.streamlit.app/"

# Função para iniciar o Selenium
def start_selenium():
    # Configuração do WebDriver
    options = Options()
    options.add_argument("--start-maximized")  # Abrir em tela cheia
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(app_url)

        # Função para ocultar os elementos indesejados
        def hide_elements():
            try:
                # Ocultar o link "https://streamlit.io/cloud"
                link_element = driver.find_element(By.CSS_SELECTOR, 'a[href="https://streamlit.io/cloud"]')
                driver.execute_script("arguments[0].style.display = 'none';", link_element)
            except:
                pass  # Ignorar se o elemento não for encontrado

            try:
                # Ocultar a imagem do avatar
                img_element = driver.find_element(By.CSS_SELECTOR, 'img[data-testid="appCreatorAvatar"]')
                driver.execute_script("arguments[0].style.display = 'none';", img_element)
            except:
                pass  # Ignorar se o elemento não for encontrado

        # Loop para ocultar os elementos continuamente
        while True:
            hide_elements()
            time.sleep(1)  # Pausa de 1 segundo para evitar sobrecarga

    except Exception as e:
        print(f"Ocorreu um erro no Selenium: {e}")
    finally:
        driver.quit()

# Rota principal do Flask
@app.route('/')
def index():
    return render_template('index.html')

# Função para iniciar o Flask e o Selenium
def run_flask_and_selenium():
    # Criar e iniciar o thread para o Selenium
    selenium_thread = threading.Thread(target=start_selenium)
    selenium_thread.daemon = True  # Permite que o thread seja finalizado quando o programa principal terminar
    selenium_thread.start()

    # Iniciar o servidor Flask
    app.run(debug=True, use_reloader=False)  # use_reloader=False para evitar que o Flask reinicie o processo

# Iniciar o Flask e Selenium
if __name__ == '__main__':
    run_flask_and_selenium()
