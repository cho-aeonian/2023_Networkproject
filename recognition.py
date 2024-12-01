<!DOCTYPE html>
<html>
<body>
<script>
    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    recognition.lang = 'ko-KR';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = function(event) {
        var speechResult = event.results[0][0].transcript;
        console.log('인식된 텍스트: ' + speechResult);

        if (speechResult.indexOf('불켜') !== -1) {
            console.log('불켜를 인식하였습니다.');
            console.log(1);
        }

        if (speechResult.indexOf('불꺼') !== -1) {
            console.log('불꺼를 인식하였습니다.');
            console.log(0);
        }
    };

    recognition.onerror = function(event) {
        console.log('오류 발생: ' + event.error);
    };
</script>
</body>
</html>
