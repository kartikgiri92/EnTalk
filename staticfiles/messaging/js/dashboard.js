// Global Variables and functions
var window_location_origin = window.location.origin
var intervalID = ""
var profile_id_of_friend_for_sending_message = ""

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
            user_name.innerHTML = json_obj.user.username;
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

const send_message = async () => {    
    let temp_url = window_location_origin + "/api/messaging/createmessage/";
    let response = await fetch(temp_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
            "Id": localStorage.getItem("id"),
            "Authorization": localStorage.getItem("token"),
            "Friend": profile_id_of_friend_for_sending_message,
        },
        body: JSON.stringify({
            "message" : document.querySelector("#send-message-input").value, 
        }),
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status && json_obj.token){
            document.querySelector("#send-message-input").value = ''
            fill_chat_space(profile_id_of_friend_for_sending_message);
        }
        else{
            redirect_to_login();
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}

document.querySelector("#send-message-button").addEventListener('click', event => {
    if(profile_id_of_friend_for_sending_message)
        send_message();
});

function delete_interval(){
    clearInterval(intervalID);
}

function hide_chat_space(){
    delete_interval();
    document.querySelector("#chat-space").style.display = "none";
}

function display_chat_space(){
    document.querySelector("#chat-space").style.display = "block";
}

function hide_rough_space(){
    document.querySelector("#rough-space").style.display = "none";
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


// STart Chat Space
var chat_space = document.querySelector("#chat-space")
var my_message = "rounded d-flex justify-content-end p-2 m-2";
var friend_message = "rounded d-flex justify-content-start p-2 m-2";

const fill_chat_space = async (friend_profile_id) => {
    let temp_url = window_location_origin + "/api/messaging/getchat/";
    let response = await fetch(temp_url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
            "Id": localStorage.getItem("id"),
            "Authorization": localStorage.getItem("token"),
            "Friend": friend_profile_id,
        },
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status && json_obj.token){
            var show_conv = document.querySelector("#show-conversation")
            document.querySelector("#total-messages").innerHTML = json_obj.data.messages.length + " Total Messages";
            show_conv.innerHTML = ""; //deletes all mesaages
            json_obj.data.messages.forEach(function(pair){

                let temp_div = document.createElement("div");
                let created_div = document.createElement("div");
                created_div.innerHTML = pair[1];
                temp_div.append(created_div);
                show_conv.append(temp_div);
                created_div.style.maxWidth = "40%";

                if(pair[0] == '0'){
                    // This users message
                    temp_div.className = "d-flex justify-content-end m-2";
                    created_div.className = "rounded p-2";
                    created_div.style.background = "#ffde7a";
                }
                else{
                    // Receiver messsages
                    temp_div.className = "d-flex justify-content-start m-2";
                    created_div.className = "rounded p-2";
                    created_div.style.background = "#cee3e6";
                }
            });
        }
        else{
            redirect_to_login();
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }        
}

function fill_chat_space_helper(friend_username, friend_profile_id, friend_total_messages){
    hide_rough_space();
    hide_search_space();
    hide_profile_update_space();
    display_chat_space();
    delete_interval();

    document.querySelector("#friend-username").innerHTML = friend_username;
    document.querySelector("#total-messages").innerHTML = friend_total_messages + " Total Messages";
    profile_id_of_friend_for_sending_message = friend_profile_id
    fill_chat_space(friend_profile_id);
    intervalID = window.setInterval(function(){
        fill_chat_space(friend_profile_id);
    }, 5000);
}
// END Chat Space


// START Search Space
var search_space = document.querySelector("#search-space")
var search_friend_input = document.querySelector("#search-friend-input")
var search_friend_button = document.querySelector("#search-friend-button")
var search_friend_results = document.querySelector("#search-friend-results")

const search_friend_api = async () => {
    let temp_url = window_location_origin + "/api/profiles/searchfriend/";
    let response = await fetch(temp_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
            "Id": localStorage.getItem("id"),
            "Authorization": localStorage.getItem("token"),
        },
        body: JSON.stringify({
            "key" : search_friend_input.value, 
        }),
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status && json_obj.token){
            search_friend_results.innerHTML = "User Found";
            let create_temp_div = document.createElement("div");
            create_temp_div.className = "btn btn-sm btn-primary rounded p-2 ml-3";
            create_temp_div.innerHTML = json_obj.data.friend_username + "  (click to start chat)";
            search_friend_results.append(create_temp_div);
            create_temp_div.addEventListener('click', event => {
                fill_chat_space_helper(json_obj.data.friend_username, json_obj.data.friend_profile_id, json_obj.data.total_messages);
            })
        }
        else if(!json_obj.token){
            redirect_to_login();
        }
        else{
            search_friend_results.innerHTML = "Username Not Found";
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}

search_friend_button.addEventListener('click', event => {
    search_friend_api();
});

// END Search Space


// Profile Update Space Start
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
// Profile Update Space END

// User Chats START
const fill_user_chats = async () => {
    let user_chats_block = document.querySelector("#fill-user-chats")
    let temp_url = window_location_origin + "/api/messaging/gac/";
    let response = await fetch(temp_url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token, 
            "Id": localStorage.getItem("id"),
        },
    });
    if(response.ok){
        let json_obj = await response.json();
        if(json_obj.status){
            json_obj.data.forEach(function(ele_obj){
                temp_obj = document.querySelector("#user-chat-block-" + ele_obj.profile_id)
                if(temp_obj){
                    // Card Already exist so make only required changes
                    temp_obj.lastElementChild.innerHTML = ele_obj.total_messages + " Total Messages";
                }
                else{
                    // Making a new card
                    temp_obj = document.querySelector("#user-chat-block").cloneNode(true);
                    temp_obj.firstElementChild.innerHTML = ele_obj.username;
                    temp_obj.lastElementChild.innerHTML = ele_obj.total_messages + " Total Messages";
                    temp_obj.id = "user-chat-block-" + ele_obj.profile_id;
                    temp_obj.style.display = "block";
                    temp_obj.style.cursor = "pointer";
                    temp_obj.addEventListener('click', event => {
                        // When clicked, chat will be displayed
                        fill_chat_space_helper(ele_obj.username, ele_obj.profile_id, ele_obj.total_messages);
                    });
                    user_chats_block.prepend(temp_obj);
                }
            });
        }
        else{
            redirect_to_login();
        }
    }
    else{
        window.alert("Error occured, reload the page.")
    }
}

function fill_user_chats_helper(){
    window.setInterval(function(){
        fill_user_chats();
    }, 5000);
}

// User Chats END

// User Space START
var user_name = document.querySelector("#user-name")
var search = document.querySelector("#search-btn")
var update_profile = document.querySelector("#update-profile")
var logout = document.querySelector("#logout")

search.addEventListener('click', event => {
    hide_rough_space();
    hide_chat_space();
    hide_profile_update_space();
    display_search_space();
});

update_profile.addEventListener('click', event => {
    hide_rough_space();
    hide_chat_space();
    hide_search_space();
    display_profile_update_space();
    fill_update_profile_columns();
});

logout.addEventListener('click', event => {
    logout_the_user();
});
// USER SPACE END

// On Page Load
window.addEventListener('load', (event) => {
    let stored_token = localStorage.getItem("token");
    let stored_id = localStorage.getItem("id");
    if(!stored_token || !stored_id){
        redirect_to_login();
    }
    retrieve_user_detail();
    fill_user_chats();
    fill_user_chats_helper();
});