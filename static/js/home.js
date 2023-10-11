
// collecting elements
const joinRoomForm = document.getElementById('hidden-input-div1-form');
const creatRoomForm = document.getElementById('hidden-input-div2-form');
const menuToggle = document.querySelector(".menu-toggle");
const overlay = document.getElementById("overlay");
const roomList = document.getElementById("roomList");
const generalPara = document.getElementById("general-para")
const messageInput = document.getElementById("message-input");
const chatMessages = document.getElementById("chat-messages");
const chatContainer = document.getElementById("chat-container")
const logoutButton= document.getElementById("logout-button")
// collecting elements

// collecting cookies
let userName
let RoomName

let username = document.cookie.split('; ').find(row => row.startsWith('user='));
if (username) {
    username = username.split('=')[1];
    userName = username
    document.getElementById('userName').innerText += username;
}
else {}
// collecting cookies

history.replaceState(null, '', '/chat/home/');

function closeDialog() {
    let dialogBox = document.getElementById('hidden-input-div1');
    dialogBox.style.display = 'none';
    let dialogBox2 = document.getElementById('hidden-input-div2');
    dialogBox2.style.display = 'flex';
    dialogBox2.style.justifyContent = 'center';
    dialogBox2.style.flexDirection = 'column'
    dialogBox2.style.alignItems = 'center';

}

function showDialog() {
    let dialogBox2 = document.getElementById('hidden-input-div2');
    dialogBox2.style.display = 'none';
    let dialogBox = document.getElementById('hidden-input-div1');
    dialogBox.style.display = 'flex';
    dialogBox.style.justifyContent = 'center';
    dialogBox.style.flexDirection = 'column'
    dialogBox.style.alignItems = 'center';
}


document.addEventListener("DOMContentLoaded", function () {
    
    menuToggle.addEventListener("click", function () {
        // overlay.classList.toggle("active");
        overlay.style.display = 'flex'
        overlay.style.justifyContent = "center"
        overlay.style.alignItems = "center"

    });

    overlay.addEventListener("click", function () {
        // overlay.classList.remove("active");
        overlay.style.display = 'none'
    });
});



function sendDataToRetrieveMessages(room_name) {
    const messageData = {
        room: room_name  
    };
    fetch('/chat/returnmessages/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(messageData),
    })
    .then(response => response.json())
    .then(data => {
        if(data.messages.length === 0) {
            chatMessages.textContent = ""
            chatMessages.style.display = "none"
        }
        else {
            messages = data.messages
            messages.forEach(message => {
                const messageElement = document.createElement("div")
                messageElement.textContent = `${message.user} : ${message.message}`
                chatMessages.appendChild(messageElement)
                chatMessages.style.display = "block"
                messageInput.value = ""
            });
        }
    })
    .catch(error => {
        console.error('Error sending message:', error);
    });
}


fetch("/chat/returnrooms/")
    .then(response => response.json())
    .then(data => {
        for (let room of data.user_rooms) {
            let listItem = document.createElement("li");
            listItem.textContent = room.room_name;
            roomList.appendChild(listItem)
            listItem.addEventListener("click", function() {
                RoomName = listItem.textContent
                sendDataToRetrieveMessages(listItem.textContent)
                generalPara.textContent = `Joined Room ${listItem.textContent}`;
                chatContainer.style.display = 'flex'
                chatContainer.style.flexDirection = 'column'
            });
        }
    })
    .catch(error => {
        console.error('Error fetching user rooms:', error);
    });



function sendDataToStoreMessages(roomName, message) {
    const messageData = {
        message: message,
        room: roomName  
    };
    fetch('/chat/storemessages/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(messageData),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message)
    })
    .catch(error => {
        console.error('Error sending message:', error);
    });
    
}


messageInput.addEventListener("keydown", function(event) {
    if(event.key === "Enter") {
        event.preventDefault()
        let message = messageInput.value
        const messageElement = document.createElement("div")
        sendDataToStoreMessages(RoomName, message)
        messageElement.textContent = `${userName} : ${message}`
        chatMessages.appendChild(messageElement)
        chatMessages.style.display = "block"
        messageInput.value = ""
    }
})




logoutButton.addEventListener("click", function() {

    fetch("/auth/logout/", {
      method : "GET"
    })
      .then(response => {
        if (response.ok) {
          return response.json()
        } else {
          throw new Error("Logout Failed")
        }
      })
      .then(data => {
        window.location.reload();
      })
      .catch(error => {
        console.error('An error occurred during the request.', error);
      })
  });
