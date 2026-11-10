function demo_javascript_method() {
    const url = 'https://gta-project.ethz.ch/group6/api/access_with_javascript'
    fetch(url)
        .then(response => response.json())
        .then(json => {
            console.log(json);
            document.getElementById("demo").innerHTML = JSON.stringify(json)
        })
}

function demo_get_ajax() {
    $.ajax({
        // URL to the Vercel production deployment (vercel --prod will give you this link)
        url: 'https://exercise-pearl.vercel.app/access_with_javascript',
        type: 'GET',
        dataType: 'JSON',
        success: function (data) { 
            console.log(data);
            document.getElementById("demo").innerHTML = JSON.stringify(data)
        },
        error: function (data) { console.log(data); },
    });
}

function demo_post_ajax() {
    var users = {
        username: "Gta_user",
        password: 1234
      };
    $.ajax({
        // URL to the Vercel production deployment (vercel --prod will give you this link)
        url: 'https://exercise-pearl.vercel.app/using_post',
        type: 'POST',
        dataType: 'JSON',
        data: JSON.stringify(users),
        success: function (data) { console.log(data);},
        error: function (data) { console.log(data); },
    });
}

// TODO TASK 2 - call Python backend for decreasing or increasing the value
// function decrease_value() {
// 
function decrease_value() {
    const currentVal = document.getElementById("value_label").innerText;
    const url = 'https://gta-project.ethz.ch/group6/api/decrease_value?curr_val='+ currentVal;
    
    fetch(url)
        .then(response => response.json())
        .then(json => {
            console.log(json);
            document.getElementById("value_label").innerText = json;
        });
}

// }

// function increase_value() {

function increase_value() {
    const currentVal = document.getElementById("value_label").innerText;
    const url = 'https://gta-project.ethz.ch/group6/api/increase_value?curr_val=' + currentVal;
    
    fetch(url)
        .then(response => response.json())
        .then(json => {
            console.log(json);
            document.getElementById("value_label").innerText = json;
        });
}
// }

// TASK 3
function post_sum_of_list() {
    // Given frontend code for TASK 3 --> complete app.py to make it work!
    // This is data that we want to pass in the message body to the backend
    var number_list = [1, 2, 3, 4, 5];
    $.ajax({
        // URL to the Vercel production deployment (vercel --prod will give you this link)
        url: 'https://gta-project.ethz.ch/group6/api/compute_sum',
        type: 'POST',
        dataType: 'JSON',
        data: JSON.stringify(number_list),
        success: function (data) { 
            console.log(data);
            document.getElementById("sum").innerHTML = JSON.stringify(data)
        },
        error: function (data) { console.log(data); },
    });
}
