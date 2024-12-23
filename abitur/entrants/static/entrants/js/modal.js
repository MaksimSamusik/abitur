        document.addEventListener('DOMContentLoaded', function () {
            var modalOverlay = document.getElementById('modalOverlay');
            var closeBtn = document.getElementById('closeBtn');

            // Отображаем модальное окно при загрузке страницы
            modalOverlay.style.display = 'flex';

            // Закрываем модальное окно при нажатии на кнопку "Закрыть"
            closeBtn.addEventListener('click', function () {
                modalOverlay.style.display = 'none';
            });
        });