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

function redirect_to_login(){
    localStorage.removeItem('id');
    localStorage.removeItem('token');
    window.location = window_location_origin;
}

const logout_the_user = async () => {
    let temp_url = window_location_origin + "/api/profiles/logout/";
    let response = await fetch(temp_url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "Id": localStorage.getItem("id"),
            "Authorization": localStorage.getItem("token"),
        },
    });
    if(response.ok){
        redirect_to_login();
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}

const retrieve_user_detail = async () => {
    let temp_url = window_location_origin + "/api/profiles/rtd/";
    let response = await fetch(temp_url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "Id": localStorage.getItem("id"),
            "Authorization": localStorage.getItem("token"),
        },
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status){
            register_username.value = json_obj.user.username;
            register_email.value = json_obj.user.email;
            register_firstname.value = json_obj.user.first_name;
            register_surname.value = json_obj.user.last_name;
        }
        else{
            redirect_to_login();
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}

function hide_chat_space(){
    document.querySelector("#chat-space").style.display = "none";
}

function display_chat_space(){
    document.querySelector("#chat-space").style.display = "block";
}

function hide_search_space(){
    document.querySelector("#search-space").style.display = "none";
}

function display_search_space(){
    document.querySelector("#search-space").style.display = "block";
}

function hide_profile_update_space(){
    document.querySelector("#profile-update-space").style.display = "none";
}

function display_profile_update_space(){
    document.querySelector("#profile-update-space").style.display = "block";
}


// Chat Space
var chat_space = document.querySelector("#chat-space")

// Search Space
var search_space = document.querySelector("#search-space")

// Profile Update Space
var profile_update_space = document.querySelector("#profile-update-space")
var register_btn = document.querySelector("#register-submit")
var register_username = document.querySelector("#register-username")
var register_email = document.querySelector("#register-email")
var register_password = document.querySelector("#register-password")
var new_password = document.querySelector("#new-password")
var register_firstname = document.querySelector("#register-firstname")
var register_surname = document.querySelector("#register-surname")

const register_user = async () => {
    // This is executed when Profile is Updated
    let temp_url = window_location_origin + "/api/profiles/create/";
    let response = await fetch(temp_url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
            "Id": localStorage.getItem("id"),
            "Authorization": localStorage.getItem("token"),
        },
        body: JSON.stringify({
            "email" : register_email.value, 
            "username" : register_username.value,
            "current_password" : register_password.value, 
            "new_password" : new_password.value, 
            "first_name" : register_firstname.value,
            "last_name" : register_surname.value, 
        }),
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status && json_obj.token){
            window.alert(json_obj.message);
        }
        else if(!json_obj.token){
            redirect_to_login();
        }
        else{
            window.alert(json_obj.message);
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
    if(!(new_password.value)){
        flag = false;
        window.alert("Enter New Password")
    }
    if(!(register_password.value)){
        flag = false;
        window.alert("Enter Current Password")
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

function fill_update_profile_columns(){
    retrieve_user_detail();
}

// User Space
var user_name = document.querySelector("#user-name")
var search = document.querySelector("#search-btn")
var update_profile = document.querySelector("#update-profile")
var logout = document.querySelector("#logout")

search.addEventListener('click', event => {
    hide_chat_space();
    hide_profile_update_space();
    display_search_space();
});

update_profile.addEventListener('click', event => {
    hide_chat_space();
    hide_search_space();
    display_profile_update_space();
    fill_update_profile_columns();
});

logout.addEventListener('click', event => {
    logout_the_user();
});

// On Page Load
window.addEventListener('load', (event) => {
    let stored_token = localStorage.getItem("token");
    let stored_id = localStorage.getItem("id");
    if(!stored_token || !stored_id){
        redirect_to_login();
    }
    retrieve_user_detail();

});