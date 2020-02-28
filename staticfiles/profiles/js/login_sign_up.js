// Global Variables and functions
var window_location_origin = window.location.origin

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrf_token = getCookie("csrftoken");


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
const login_user = async () => {
    let temp_url = window_location_origin + "/api/profiles/login/";
    let response = await fetch(temp_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
        },
        body: JSON.stringify({
            "username" : login_username.value, 
            "password" : login_password.value
        }),
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status){
            // Save profile id and token in localStorage
            let token = json_obj.token;
            let id = json_obj.id;
            if(!token || !id){
                window.alert("Error occured, reload the page.");
            }
            else{
                localStorage.setItem("token", token);
                localStorage.setItem("id", id);
                window.location = window_location_origin + "/dashboard/";   
            }
        }
        else{
            window.alert(json_obj.message);
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}

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
        login_user();
    }
});


// Register Section
const register_user = async () => {
    let temp_url = window_location_origin + "/api/profiles/create/";
    let response = await fetch(temp_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
        },
        body: JSON.stringify({
            "email" : register_email.value, 
            "username" : register_username.value,
            "password" : register_password.value, 
            "first_name" : register_firstname.value,
            "last_name" : register_surname.value, 
        }),
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status){
            // Save profile id and token in localStorage
            let token = json_obj.token;
            let id = json_obj.id;
            if(!token || !id){
                window.alert("Error occured, reload the page.");
            }
            else{
                localStorage.setItem("token", token);
                localStorage.setItem("id", id);
                window.location = window_location_origin + "/dashboard/";
            }
        }
        else{
            window.alert(json_obj.message + "Change Email or Username");
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}


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
        register_user();
    }
});

// On Page Load
window.addEventListener('load', (event) => {

    let stored_token = localStorage.getItem("token");
    let stored_id = localStorage.getItem("id");
    if(stored_token && stored_id){
        window.location = window_location_origin + "/dashboard/";
    }

});