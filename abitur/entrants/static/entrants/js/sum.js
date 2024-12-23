document.addEventListener('DOMContentLoaded', function () {
    // Получаем ссылки на все поля формы
    var field1 = document.getElementById('id_physics');
    var field2 = document.getElementById('id_math');
    var field3 = document.getElementById('id_language');
    var field4 = document.getElementById('id_ru_by');
    var field5 = document.getElementById('id_rating');
    var sumField = document.getElementById('id_overall_rating');

    // Добавляем обработчик события для каждого поля ввода
    field1.addEventListener('input', updateSumField);
    field2.addEventListener('input', updateSumField);
    field3.addEventListener('input', updateSumField);
    field4.addEventListener('input', updateSumField);
    field5.addEventListener('input', updateSumField);

    // Функция для обновления суммарного поля
    function updateSumField() {
        // Получаем значения из каждого поля
        var value1 = parseFloat(field1.value) || 0;
        var value2 = parseFloat(field2.value) || 0;
        var value3 = parseFloat(field3.value) || 0;
        var value4 = parseFloat(field4.value) || 0;
        var value5 = parseFloat(field5.value) || 0;

        // Вычисляем сумму значений
        var sum = value1 + value2 + value3 + value4 + value5;

        // Устанавливаем значение суммарного поля
        sumField.value = sum;
    }
});