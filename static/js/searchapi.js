

function apiRegistrion(){

}
function getDiary(id){
  fetch('http://127.0.0.1:5000/api/v1/entries/' + id)
  .then((res) => res.json())
  .then((data) => {
    let output = '<h2 class="mb-4">Posts</h2>';
    data.forEach(function(entry){
      entry += `
        <div class="card card-body mb-3">
          <h3>${entry.title}</h3>
          <p>${entry.body}</p>
        </div>
      `;
    });
    document.getElementById('output').innerHTML = output;
  })
}

// var r = confirm("Are You Sure To You To Delete Records?");
// if (r === true)

function addEntry(e){
  e.preventDefault();

  let title = document.getElementById('title').value;
  let body = document.getElementById('body').value;

function ApiRegistration(e){
    e.preventDefault();

    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let confirm_password = document.getElementById('confirm_password').value;
    let version = document.getElementById('version').value;

    fetch('http://127.0.0.1:5000/api/register', {
      method:'POST',
      headers: {
        'Content-Type':'application/json'
      },
      body:JSON.stringify({firstname:firstname, lastname:lastname,
        username:username, email:email, password:password,
        confirm_password:confirm_password, version:version})
    })
    .then((res) => res.json())
    .then((data) => console.log(data))
    if (data.message == "User Registered"){
      window.location.href = "/homepage"
    }.error =>(
      window.location.href = "/api/registration"
    );
  }
