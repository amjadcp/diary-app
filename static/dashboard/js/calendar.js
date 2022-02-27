window.addEventListener('load', () => {
  $('#diary').hide()
  $('#diary-all').hide()
  $('#add').hide()
  $('#add-calendar').hide()
})

$('#allentries').click(() => {
  $('#diary-all').show()
  $('#element2').hide()
  $('#diary').hide()
  $('#add').hide()
})
$('#calendar').click(() => {
  $('#element2').show()
  $('#diary-all').hide()
})

var calendar = new ej.calendars.Calendar({
  change: function (args) {
    let date = args.value.toLocaleDateString()
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
          $('#diary-body').html(responce.body)
        } else {
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
