async function playBeep() {
   let beep = new Audio(
      "https://cdn.pixabay.com/download/audio/2023/03/18/audio_900b6765ed.mp3?filename=the-notification-email-143029.mp3",
   );
   try {
      await beep.play();
   } catch (err) {
      console.log(err)
   }
}
/**
 * Creates an HTML element representing a message from another user in a chat.
 *
 * @param {string} username - The username of the other user.
 * @param {string} message - The message content from the other user.
 * @returns {HTMLDivElement} - The HTML element representing the other user's message.
 */
function createOtherUserMessage(username, message) {
   // Create elements
   let colDiv = document.createElement("div");
   let dFlexDiv = document.createElement("div");
   let avatarDiv = document.createElement("div");
   let spanAvatarContent = document.createElement("span");
   let spanAvatarStatus = document.createElement("span");
   let bgSuccessDiv = document.createElement("div");

   colDiv.className =
      "col-12 align-self-start col-md-10 col-sm-11 text-white rounded ";
   dFlexDiv.className = "d-flex align-items-center";
   avatarDiv.className = "avatar bg-primary me-3";
   spanAvatarStatus.className = "avatar-status bg-success";
   bgSuccessDiv.className = "bg-shark-800 wrap d-flex shadow px-2 py-2 rounded";

   spanAvatarContent.className = "avatar-content font-bold";
   spanAvatarContent.textContent = username.slice(0, 2).toUpperCase();
   bgSuccessDiv.textContent = message;

   avatarDiv.appendChild(spanAvatarContent);
   avatarDiv.appendChild(spanAvatarStatus);
   dFlexDiv.appendChild(avatarDiv);
   dFlexDiv.appendChild(bgSuccessDiv);
   colDiv.appendChild(dFlexDiv);

   return colDiv;
}

/**
 * Creates an HTML element representing a message from the current user in a chat.
 *
 * @param {string} message - The message content from the current user.
 * @returns {HTMLDivElement} - The HTML element representing the current user's message.
 */
function createCurrentUserMessage(message) {
   // Create elements
   let colDiv = document.createElement("div");
   let dFlexDiv = document.createElement("div");
   let bgDiv = document.createElement("div");

   // Add classes
   colDiv.className =
      "col-12 align-self-end col-md-10 col-sm-11 text-white rounded";
   dFlexDiv.className = "d-flex align-items-center justify-content-end";
   bgDiv.className = "bg-shark-800 d-flex px-2 py-2 rounded";

   // Add text content
   bgDiv.textContent = message;

   // Add child elements to their respective parents
   dFlexDiv.appendChild(bgDiv);
   colDiv.appendChild(dFlexDiv);

   // Return the main element
   return colDiv;
}

function createAvatarOnlineUser(username) {
   // Crear los elementos necesarios
   var colDiv = document.createElement("div");
   var avatarDiv = document.createElement("div");
   var contentSpan = document.createElement("span");
   var statusSpan = document.createElement("span");

   // Añadir las clases necesarias
   colDiv.className = "col-1 col-md-3";
   avatarDiv.className = "avatar bg-primary me-3";
   contentSpan.className = "avatar-content font-bold";
   statusSpan.className = "avatar-status bg-success";

   // Añadir el contenido del nombre de usuario
   contentSpan.textContent = username.slice(0, 2).toUpperCase();

   // Añadir los elementos al DOM
   avatarDiv.appendChild(contentSpan);
   avatarDiv.appendChild(statusSpan);
   colDiv.appendChild(avatarDiv);

   // return element
   return colDiv;
}
