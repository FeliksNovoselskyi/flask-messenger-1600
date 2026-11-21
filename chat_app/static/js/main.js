let input_id = document.querySelector("#input-field")
const button = document.querySelector("#send-button")
const container = document.getElementById("message-container")


if (button) {
    button.addEventListener("click", function() {
        let text = input_id.value;

        socket.emit(
            "message", 
            {
                message: text,
                chat_id: chatId
            }
        );

        input_id.value = "";
    })
}


socket.on("message", (data) => {
    console.log("2", chatId);
    if (container) {
        let messageText = data.message;
        
        const paraghraph = document.createElement("p");
        
        paraghraph.textContent = messageText;

        container.append(paraghraph);
    }
});
