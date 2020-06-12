function shorten() {
    let inputURL = document.getElementById('inputUrl').value;

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

            document.getElementById('inputUrl').value = 'http://www.minify.rs/'+ custom
        }).fail(function (err) {
            console.log('Error: ', err);
        })

    }).fail(function (err) {
        console.log('Error: ', err);
    })

}


const btn = document.getElementById('button');
btn.addEventListener('click', shorten);





