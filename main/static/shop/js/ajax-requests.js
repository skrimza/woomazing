$(document).ready(function () {
    e.preventDefault();
    $(".shop-navigation_button").on("click", function () {
        let buttonText = $(this).text(); // Получаем текст нажатой кнопки
        $.ajax({
            data: {
                button: buttonText
            },
            type: 'POST',
            url: '../../../json_requests.py'
        });
    });
});
// это будет контактная форма
// $('#form').on('submit', function (e) {
//     e.preventDefault(); // Отмена стандартной отправки формы (без перезагрузки страницы)

//     $.ajax({
//         data: {
//             username: $('#username').val(),
//             email: $('#email').val(),
//             message: $("#message").val()
//         },
//         type: 'POST',
//         url: '/contact',
//         success: function (data) {
//             var dataString = JSON.stringify(data);

//             if (dataString.startsWith("{")) {
//                 // Если данные начинаются с {, значит это JSON, и форма отправлена успешно
//                 $('#output').addClass("active");
//                 $('#output').text('Form submitted successfully!').show();
//                 $('#form')[0].reset();

//             } else {
//                 // Иначе это строка с сообщением об ошибке
//                 $('#output').text(data).show();
//                 $('#form')[0].reset();
//             }
//             setTimeout(function () {
//                 $('#output').removeClass('active');
//             }, 3000);
//         },
//         error: function (jqXHR, textStatus, errorThrown) {
//             // Обработка ошибок AJAX-запроса
//             $('#output').text('An error occurred: ' + textStatus).show();
//             setTimeout(function () {
//                 $('#output').removeClass('active').hide();
//             }, 3000);
//         }
//     });
// });