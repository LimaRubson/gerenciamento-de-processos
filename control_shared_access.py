import threading
import time

# Definição de semáforos para controle de acesso aos recursos compartilhados
semaphore_resource_1 = threading.Semaphore(1)
semaphore_resource_2 = threading.Semaphore(1)

# Recursos compartilhados (poderiam ser variáveis globais, buffers, etc.)
resource_1 = 0
resource_2 = 0

# Função para simular o acesso ao recurso 1
def access_resource_1(thread_id):
    global resource_1
    while True:
        semaphore_resource_1.acquire()
        print(f"Thread {thread_id} acessando Recurso 1")
        # Simulação de processamento no recurso 1
        resource_1 += 1
        time.sleep(1)
        print(f"Recurso 1 - Thread {thread_id}: {resource_1}")
        semaphore_resource_1.release()
        time.sleep(3)

# Função para simular o acesso ao recurso 2
def access_resource_2(thread_id):
    global resource_2
    while True:
        semaphore_resource_2.acquire()
        print(f"Thread {thread_id} acessando Recurso 2")
        # Simulação de processamento no recurso 2
        resource_2 += 1
        time.sleep(1)
        print(f"Recurso 2 - Thread {thread_id}: {resource_2}")
        semaphore_resource_2.release()
        time.sleep(3)

# Criação e inicialização das threads
thread_1 = threading.Thread(target=access_resource_1, args=(1,))
thread_2 = threading.Thread(target=access_resource_2, args=(2,))
thread_3 = threading.Thread(target=access_resource_1, args=(3,))
thread_4 = threading.Thread(target=access_resource_2, args=(4,))
thread_5 = threading.Thread(target=access_resource_1, args=(5,))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

# Aguarda as threads terminarem (não será alcançado devido ao loop infinito nas funções)
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
