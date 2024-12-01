// LED 제어 함수 선언
function ledON() {
    var ref = database.ref('led');
    ref.update({ led: 1 })
  }
  
  function ledOFF() {
    var ref = database.ref('led');
    ref.update({ led: 0 })
  }
  
  // Firebase 접근 정보
  var config = {
    apiKey: "본인것 넣을 것, 아래도 마찬가지",
    authDomain: "test230729.firebaseapp.com",
    databaseURL: "https://test230729-default-rtdb.firebaseio.com",
    projectId: "test230729",
    storageBucket: "test230729.appspot.com",
    messagingSenderId: "853700741140",
    appId: "1:853700741140:web:929162eb54a746eb63bf01",
    measurementId: "G-3BTLVEK3N3"
  };
  
  //Firebase 데이터베이스 만들기
  firebase.initializeApp(config);
  database = firebase.database();
  
  // Firebase 데이터베이스 정보 가져오기
  var ref = database.ref("led");
  ref.on("value", gotData);
  
  function gotData(data) {
    var val = data.val();
  
    if (val.led == 0) {
      document.getElementById("ledstatus").innerHTML = "led가 현재 꺼짐";
      document.getElementById("img").src = "ledoff.jpg";
    }
    else {
      document.getElementById("ledstatus").innerHTML = "led가 현재 켜짐";
      document.getElementById("img").src = "ledon.jpg";
    }
  
    console.log(val)
  }
  
  var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
  
  recognition.lang = 'ko-KR';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;
  
  recognition.start();
  
  recognition.onresult = function(event) {
    var speechResult = event.results[0][0].transcript;
    console.log('인식된 텍스트: ' + speechResult);
  
    if (speechResult.indexOf('켜') !== -1) {
      ledON()
    }
  
    if (speechResult.indexOf('꺼') !== -1) {
      ledOFF()
    }
  };
  
  recognition.onerror = function(event) {
    console.log('오류 발생: ' + event.error);
  };
  
  // 음성 인식이 종료될 때마다 다시 시작합니다.
  recognition.onend = function() {
    recognition.start();
  };