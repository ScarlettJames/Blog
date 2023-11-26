const form = document.getElementById('commentForm');
const comment = document.getElementById('id_comment');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

// form.addEventListener('submit', handleSubmit);

function handleSubmit(user, post, url) {
    //prevent from submit form
    //event.preventDefault();
    //event.stopPropagation();
    const URL = url;
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value;
    data['comment'] = comment.value;
    data['author'] = user;
    data['post'] = post;

    // Send Form Data
    console.log('handleSubmit', URL);
    sendData(URL, data);
  }

  function sendData(url, data) {
    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      success: function (res) {
        console.log(res);
        window.location.reload();
      }
    })
  }