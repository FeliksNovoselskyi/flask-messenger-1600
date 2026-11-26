let input_id = document.querySelector("#input-field")
const button = document.querySelector("#send-button")
const container = document.getElementById("message-container")

socket.emit("user_connect", {chat_id: chatId})


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


socket.on("display_status", (data) => {
    let members
    members = data.members

    console.log(members);
    // participants-container
    const participants = document.getElementById("participants-container")
    
    participants.innerHTML = ""

    let h3Header = document.createElement("h3")
    h3Header.textContent = "Участники чата"
    participants.appendChild(h3Header)

    members.forEach(element => {
        let members_div = document.createElement("div")
        members_div.style.display = 'flex'
        members_div.style.flexDirection = 'row'
        let p1 = document.createElement("p")
        let p2 = document.createElement("p")


        p1.textContent = element.email
        if (element.is_online) {

            p2.textContent = '🟢'
        } else {
            p2.textContent = '🔴'
        }
        
        members_div.appendChild(p1)
        members_div.appendChild(p2)
        participants.appendChild(members_div)
    });
})
