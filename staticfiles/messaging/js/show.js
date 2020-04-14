var window_location_origin = window.location.origin
var dashboard_link = document.querySelector("#dashboard-link")
dashboard_link.href = window_location_origin


// Global Functions
function gcd(a, b){
    if(b == 0)
        return(a)
    else
        return(gcd(b, a % b))
}

function sieveOfEratosthenes(range_start, range_end) {
    const isPrime = new Array(range_end + 1).fill(true);
    isPrime[0] = false;
    isPrime[1] = false;

    const primes = [];

    for(let number = 2; number <= range_end; number += 1) {
        if(isPrime[number] === true){
            if(number >= range_start)
                primes.push(number);
            let nextNumber = number * number;

            while(nextNumber <= range_end){
                isPrime[nextNumber] = false;
                nextNumber += number;
            }
        }
    }
    return(primes[Math.floor(Math.random() * primes.length)]);
}


// Variables
const range_start = 1, range_end = 250;
var p, q, pk1, pk2, tot, k, pvky;
var element_p = document.querySelector("#prime-number-p")
var element_q = document.querySelector("#prime-number-q")
var element_pk1 = document.querySelector("#primary-key-1")
var element_pk2 = document.querySelector("#primary-key-2")
var element_tot = document.querySelector("#tot")
var element_k = document.querySelector("#k-constant")
var element_pvky = document.querySelector("#private-key")

p = sieveOfEratosthenes(range_start, range_end);
element_p.append(p);

q = sieveOfEratosthenes(range_start, range_end);
while(p == q){
    q = sieveOfEratosthenes(range_start, range_end);
}
element_q.append(q);

pk1 = p * q;
element_pk1.append(pk1);

tot = (p - 1) * (q - 1);
element_tot.append(tot);

pk2 = 2;
for( ; pk2 < tot; pk2 +=1 ){
    if(gcd(pk2, tot) == 1)
        break;
}
element_pk2.append(pk2);

k = 2;
while(true){
    let x = (1 + (k * tot))
    if(x % pk2 == 0){
        pvky = x/pk2;
        break;
    }
    k += 1;
}
element_k.append(k);
element_pvky.append(pvky);


var element_message = document.querySelector("#message")
var convert_btn = document.querySelector("#convert-btn")
var ascii_box = document.querySelector("#ascii-box")
var encrypted_box = document.querySelector("#encrypted-box")
var cipher_text = document.querySelector("#cipher-text")
var broken_box = document.querySelector("#broken-box")
var decrypt_box = document.querySelector("#decrypt-box")
var character_box = document.querySelector("#character-box")
var decrypted_text = document.querySelector("#decrypted-text")

convert_btn.addEventListener('click', event => {
    let message = element_message.value
    ascii_box.innerHTML = ''
    encrypted_box.innerHTML = ''
    cipher_text.innerHTML = ''
    broken_box.innerHTML = ''
    decrypt_box.innerHTML = ''
    character_box.innerHTML = ''
    decrypted_text.innerHTML = ''

    const ascii_num_list = [], enc_mssg_list = [];
    for(let i = 0; i < message.length; i += 1){
        ascii_box.append(message[i].charCodeAt(0) + " ")
        ascii_num_list.push(message[i].charCodeAt(0))
    }

    for(let i = 0; i < ascii_num_list.length; i += 1){
        let num =  Math.pow(ascii_num_list[i], pk2) % pk1
        encrypted_box.append(num + " ")
        cipher_text.append(num.toString().length, num);
        broken_box.append(num + " ")
        enc_mssg_list.push(num)
    }

    for(let i = 0; i < enc_mssg_list.length; i += 1){
        num = ascii_num_list[i]
        decrypt_box.append(num + " ");
        character_box.append(String.fromCharCode(num) + " ");
        decrypted_text.append(String.fromCharCode(num));
    }
    
});