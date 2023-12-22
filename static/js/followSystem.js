const addFollower = document.getElementById('addFollower');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

function handleSubmit(user, follower, url) {
    //prevent from submit form
    // event.preventDefault();
    // event.stopPropagation();
    const URL = url;
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value;
    data['user'] = user;
    data['follower'] = follower;
    sendData(URL, data);
}

function sendData(url, data) {
    console.log('Data', data);
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        success: function (res) {
        console.log(res);
        },
        error: function (err) {
            console.error(err);
        }
    })

}