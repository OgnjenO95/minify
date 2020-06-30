function shorten() {
    let inputURL = document.getElementById('inputUrl').value;
    document.getElementById('error').style.visibility = 'hidden'

    const _data = {
        'url': inputURL
    };

    $.ajax({
        url: '/api/shorten-url',
        method: 'PUT',
        data: JSON.stringify(_data),
        // dataType: 'json'
    }).done(function (res) {
        let p = JSON.parse(res)
        let custom = p.message;
        $.ajax({
            url: '/api/url/' + custom,
            method: 'GET'
        }).done(function (res) {
            console.log(custom);

            document.getElementById('inputUrl').value = 'ognjen.digitalcube.rs/'+ custom
        }).fail(function (err) {
            console.log('Error: ', err.responseText);
        })

    }).fail(function (err) {
        let error = JSON.parse(err.responseText);
        console.log('Error: ', error.message);
        document.getElementById('error').style.visibility = 'visible'
    })

}

const btn = document.getElementById('button');
btn.addEventListener('click', shorten);


let inputUrl = document.getElementById("inputUrl");
inputUrl.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("button").click();
  }
})