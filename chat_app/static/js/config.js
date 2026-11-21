let socket = io();

let parts = window.location.pathname.split("/");
const chatId = Number(parts[parts.length -1]);
