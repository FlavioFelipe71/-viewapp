from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# URL do aplicativo Streamlit
app_url = "https://scvsei901.streamlit.app/"

# Configuração do WebDriver
options = Options()
options.add_argument("--start-maximized")  # Abrir em tela cheia
# Substitua pelo caminho do seu WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Abrir o link do aplicativo Streamlit
    driver.get(app_url)

    # Função para ocultar elementos indesejados
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

    # Verificação contínua
    print("Verificação contínua para ocultar elementos iniciada. Pressione Ctrl+C para sair.")
    while True:
        hide_elements()
        time.sleep(1)  # Pausa de 1 segundo para evitar sobrecarga do navegador

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechar o navegador ao sair
    driver.quit()
