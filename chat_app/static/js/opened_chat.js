
if (chatId) {
    socket.emit(
        "join_group_room", 
        {chat_id: chatId}
    );
};
