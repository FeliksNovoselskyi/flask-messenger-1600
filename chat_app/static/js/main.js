let socket = io()

let input_id = document.querySelector("#input-field")

const button = document.querySelector("#send-button")

const container = document.getElementById("message-container")

button.addEventListener("click", function() {
    console.log("Кнопка была нажата")

    let text = input_id.value
    
    socket.emit("message", {message: text})
})


socket.on("message", (data) => {
    
    let messageText = data.message
    
    const paraghraph = document.createElement("p")
    // УКазать текст сообщения в параграфе
    paraghraph.textContent = messageText
    // Добавить параграф в container
    container.append(paraghraph)
})