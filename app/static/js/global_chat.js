/**
 * Get DOM elements
 */
const messagesContainer = document.getElementById("messages-container");
const inputMessage = document.getElementById("input-message");
const onlineUsersContainer = document.getElementById("online-users-container");
const messageButtonSender = document.getElementById("message-button-sender");

// Initialize the list of online users
let currentOnlineUsers = [];

// Create the socket connection
const socket = io();

/**
 * Function to handle the update of online users
 * @param {Array} onlineUsers - List of online users
 */
function handleOnlineUsers(onlineUsers) {
   const currentUsersString = JSON.stringify(currentOnlineUsers.sort());
   const onlineUsersString = JSON.stringify(onlineUsers.sort());

   if (currentUsersString === onlineUsersString) {
      return;
   }

   currentOnlineUsers = onlineUsers;
   onlineUsersContainer.innerHTML = "";

   onlineUsers.forEach((username) => {
      const element = createAvatarOnlineUser(username);
      onlineUsersContainer.appendChild(element);
   });
}

/**
 * Function to handle incoming messages
 * @param {Object} payload - Object with message information
 */
async function handleMessage(payload) {
   if (payload.type !== "message") {
      return;
   }

   const isCurrentUser = payload.username === username;
   if (!isCurrentUser) {
      await playBeep();
   }

   const element = isCurrentUser
      ? createCurrentUserMessage(payload.message)
      : createOtherUserMessage(payload.username, payload.message);

   messagesContainer.appendChild(element);
   messagesContainer.lastElementChild.scrollIntoView({ behavior: "smooth" });
}

/**
 * Function to send a message
 */
function sendMessage() {
   if (inputMessage.value.trim() === "") {
      return;
   }

   socket.emit("chat_message", { message: inputMessage.value });
   inputMessage.value = "";
   inputMessage.focus();
}

// Socket events
socket.on("connect", () => {
   socket.emit("get_online_users");
   setInterval(() => socket.emit("get_online_users"), 5000);
});

socket.on("online_users", handleOnlineUsers);
socket.on("message", handleMessage);

// Input events
inputMessage.addEventListener("keyup", (event) => {
   if (event.key === "Enter") {
      sendMessage();
   }
});

messageButtonSender.addEventListener("click", sendMessage);
