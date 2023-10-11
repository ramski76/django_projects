
const joinRoomForm = document.getElementById('hidden-input-div1-form');
const creatRoomForm = document.getElementById('hidden-input-div2-form');
const roomList = document.getElementById("roomList");
const generalPara = document.getElementById("general-para")
const messageInput = document.getElementById("message-input");
const chatMessages = document.getElementById("chat-messages");
const chatContainer = document.getElementById("chat-container")
const logoutButton= document.getElementById("logout-button")

joinRoomForm.addEventListener('submit', function (e) {

    e.preventDefault();
    const roomName = document.getElementById('hidden-input1').value;
    const roomData = {
        roomname: roomName
    };
    fetch('/chat/joinroom/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify(roomData)
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// // //////////////////////////////


creatRoomForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const roomName = document.getElementById('hidden-input2').value;

    const roomData = {
        roomname: roomName
    };

    fetch('/chat/createroom/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify(roomData)
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
})
