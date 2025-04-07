function Prime(num){
    if (num < 2) return false;
    for (let i=2; i<num / 2; i++) {
        if (num % i ==0) return false;
    }
    return true;
}

self.onmessage = function (e){
    // Work Task 로 부터 전달받은 숫자
    let number = e.data.input;

    output = number;
    output += (Prime(number)) ? "is PrimeNumber" : "is Not PrimeNumber";
    self.postMessage(output);
}


  