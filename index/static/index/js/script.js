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
            sendData(audioBlob);
            audioChunks = [];
        });
    });

function sendData(data) {
  const XHR = new XMLHttpRequest();
  const FD = new FormData();

  // Append the audioBlob with the 'voice' field name
  FD.append('voice', data, 'audio.wav');

  // ALERTS
    // Define what happens on successful data submission
  // XHR.addEventListener("load", (event) => {
  //   alert("Yeah! Data sent and response loaded.");
  // });
  //
  // // Define what happens in case of an error
  // XHR.addEventListener("error", (event) => {
  //   alert("Oops! Something went wrong.");
  // });
  // Set up our request

  XHR.open("POST", "/audioAPI");

  // Send our FormData object; HTTP headers are set automatically
  XHR.send(FD);
}