const URL = '/audioAPI';

navigator.mediaDevices.getUserMedia({ audio: true})
    .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);

        document.querySelector('#start').addEventListener('click', function(){
            mediaRecorder.start();

        });
        let audioChunks = [];
        mediaRecorder.addEventListener("dataavailable",function(event) {
            audioChunks.push(event.data);
            console.log(audioChunks)
        });

        document.querySelector('#stop').addEventListener('click', function(){
            mediaRecorder.stop();

        });

        mediaRecorder.addEventListener("stop", function() {
            const audioBlob = new Blob(audioChunks, {type: 'audio/wav' });
            console.log(audioBlob)

            let fd = new FormData();

            fd.append('voice', audioBlob);

            const requset = new XMLHttpRequest();
            requset.open("POST", '/audioAPI');
            requset.send(fd);
            // sendVoice(fd)
            audioChunks = [];
        });
    });

// async function sendVoice(form) {
//     const body = JSON.stringify(Object.fromEntries(form));
//     let data = await fetch(URL, {
//         method: 'POST',
//         body
//     });
//     let response = await data.json();
//
// }
