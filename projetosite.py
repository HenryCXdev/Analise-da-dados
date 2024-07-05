import flet as ft

def main(pagina):

    titulo = ft.Text("chatZada")
    ttljanela = ft.Text("Bem vindo ao ChatZada")
    campo_usuario = ft.TextField(label="Escreva seu nome de usúario:")

    chat = ft.Column(scroll=True)

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)

        
        pagina.update()
 
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_men = campo_mensagem.value
        nome_usuario = campo_usuario.value
    
        mensagem = f"{nome_usuario}: {texto_men}"
        pagina.pubsub.send_all(mensagem)    
        campo_mensagem.value = ""

        pagina.update()
        
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)    
    botao_eviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    linha_mensagem = ft.Row([campo_mensagem, botao_eviar])
    def entrar_chat(evento):
        pagina.remove(titulo) 
        pagina.remove(botaoini)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        
        mensagem = f"{campo_usuario.value}: Entrou no chat"
        pagina.pubsub.send_all(mensagem)  

        
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=ttljanela, content=campo_usuario,actions=[botao_entrar]) 

    


    def iniciarchatzada(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()

    botaoini = ft.ElevatedButton("Iniciar ChatZada", on_click=iniciarchatzada)


    pagina.add(titulo)
    pagina.add(botaoini)


    


ft.app(main, view=ft.WEB_BROWSER)