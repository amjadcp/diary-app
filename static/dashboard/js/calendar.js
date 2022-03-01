window.addEventListener('load', () => {
  let check = localStorage.getItem('check')
  if (check === '1') {
    $('#diary').hide()
    $('#add').hide()
    $('#add-calendar').hide()
    $('#page').hide()
    $('#element2').hide()
    $('#diary-all').show()
    localStorage.setItem('check', '0')
  } else {
    $('#diary').hide()
    $('#diary-all').hide()
    $('#add').hide()
    $('#add-calendar').hide()
    $('#page').hide()
  }
})
$('#allentries').click(() => {
  $('#diary-all').show()
  $('#element2').hide()
  $('#diary').hide()
  $('#add').hide()
  $('#page').hide()
})
$('#calendar').click(() => {
  $('#element2').show()
  $('#diary-all').hide()
})
$('#add').click(() => {
  $('#date').html(localStorage.getItem('date'))
  $('#page').show()
  $('#add').hide()
})
$('#submit').click(() => {
  let title = $('#title').val()
  let text = $('#text').val()
  if (title === '') {
    alert('Write a title')
  } else if (text === '') {
    alert('Write a body')
  } else {
    let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    console.log(localStorage.getItem('date'))
    let data = {
      csrfmiddlewaretoken: csrf,
      date: localStorage.getItem('date'),
      title: title,
      text: text,
    }
    $.ajax({
      url: 'create-diary',
      method: 'POST',
      data: data,
      dataType: 'json',
      success: (responce) => {
        $('#title').val('')
        $('#text').val('')
        $('#page').hide()
        location.reload()
      },
    })
  }
})
$('#cancel').click(() => {
  $('#title').val('')
  $('#text').val('')
  $('#page').hide()
  $('#element2').hide()
  $('#diary-all').show()
})

const edit_diary = (id) => {
  let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
  let data = {
    csrfmiddlewaretoken: csrf,
    id: id,
  }
  $.ajax({
    url: 'edit-diary',
    method: 'POST',
    data: data,
    dataType: 'json',
    success: (responce) => {
      localStorage.setItem('date', responce.date)
      $('#diary-all').hide()
      $('#page').show()
      $('#date').html(responce.date)
      $('#title').val(responce.title)
      $('#text').val(responce.body)
    },
  })
}

const del_diary = (id) => {
  let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
  let data = {
    csrfmiddlewaretoken: csrf,
    id: id,
  }
  $.ajax({
    url: 'del-diary',
    method: 'POST',
    data: data,
    dataType: 'json',
    success: (responce) => {
      location.reload()
      localStorage.setItem('check', '1')
    },
  })
}

var calendar = new ej.calendars.Calendar({
  change: function (args) {
    let date = args.value.toLocaleDateString()
    localStorage.setItem('date', date)
    let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    let data = {
      csrfmiddlewaretoken: csrf,
      date: date,
    }
    $.ajax({
      url: 'calendar',
      method: 'POST',
      data: data,
      dataType: 'json',
      success: (responce) => {
        if (responce.message === '0') {
          $('#add').hide()
          $('#add-calendar').hide()
          $('#diary').show()
          $('#diary-title').html(responce.title)
          let converter = new showdown.Converter()
          let body = converter.makeHtml(responce.body)
          $('#diary-body').html(body)
        } else {
          $('#page').hide()
          $('#add').show()
          $('#add-calendar').show()
          $('#diary').hide()
        }
      },
    })
  },
})

// Render the initialized button.
calendar.appendTo('#element')
calendar.appendTo('#element2')
