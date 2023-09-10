const URL = '/audioAPI';

navigator.mediaDevices.getUserMedia({ audio: true})
    .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);

        document.querySelector('.first_button').addEventListener('click', function(){
            mediaRecorder.start();

        });
        let audioChunks = [];
        mediaRecorder.addEventListener("dataavailable",function(event) {
            audioChunks.push(event.data);
        });

        document.querySelector('.second_button').addEventListener('click', function(){
            mediaRecorder.stop();
            location.reload();
            // wait 5 sec
            // play sound
        });

        mediaRecorder.addEventListener("stop", function() {
            const audioBlob = new Blob(audioChunks, {type: 'audio/wav' });
            sendData(audioBlob);
            audioChunks = [];
        });
        // document.getElementById("Play").click();
    });


function sendData(data) {
  const XHR = new XMLHttpRequest();
  const FD = new FormData();

  // Append the audioBlob with the 'voice' field name
  FD.append('voice', data, 'audio.wav');

  XHR.open("POST", "/audioAPI");

  // Send our FormData object; HTTP headers are set automatically
  XHR.send(FD);
}



document.getElementById("Play").addEventListener("click", function (music) {
    let audioElement = document.getElementById("Audio");
    audioElement.play();
}, false);