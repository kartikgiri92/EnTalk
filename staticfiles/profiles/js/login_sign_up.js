var window_location_origin = window.location.origin

// Login Section Variables
var login_btn = document.querySelector("#login-submit")
var login_username = document.querySelector("#login-username")
var login_password = document.querySelector("#login-password")


// Register Section Variables
var register_btn = document.querySelector("#register-submit")
var register_username = document.querySelector("#register-username")
var register_email = document.querySelector("#register-email")
var register_password = document.querySelector("#register-password")
var register_firstname = document.querySelector("#register-firstname")
var register_surname = document.querySelector("#register-surname")


// Login Section



login_btn.addEventListener('click', event => {
    var flag = true;
    if(!(login_username.value)){
        flag = false;
        window.alert("Enter Login Username")
    }
    if(!(login_password.value)){
        flag = false;
        window.alert("Enter Login Password")
    }

    if(flag){
        // call API
    }
});


// Register Section




register_btn.addEventListener('click', event => {
    var flag = true;
    if(!(register_username.value)){
        flag = false;
        window.alert("Enter Register Username")
    }
    if(!(register_email.value)){
        flag = false;
        window.alert("Enter Register email")
    }
    if(!(register_password.value)){
        flag = false;
        window.alert("Enter Register Password")
    }
    if(!(register_firstname.value)){
        flag = false;
        window.alert("Enter Register First Name")
    }
    if(!(register_surname.value)){
        flag = false;
        window.alert("Enter Register SurName")
    }

    if(flag){
        // call API
    }
});

