var window_location_origin = window.location.origin

const api_call = async () => {
    let response = await fetch(window_location_origin + "/api/profiles/create/", {
        method: "GET",
    });
    if(response.ok){
        let json_obj = await response.json();

        // WRITE YOUR STUFF FROM HERE
        console.log(json_obj);
    }
    else{
        console.log("NETWORK Error occured, reload the page.");
    }
}

// On Page Load
window.addEventListener('load', (event) => {
    api_call();
});